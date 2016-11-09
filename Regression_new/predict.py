import os
import caffe
import numpy as np


MODEL_FILE = '/home/laurae-linux/Documents/Data_Science/Caffe/deploy.prototxt'
PRETRAINED = '/home/laurae-linux/Documents/Data_Science/Caffe/models/train_iter_12.caffemodel'


caffe.set_mode_gpu()
caffe.set_device(0)
net = caffe.Net(MODEL_FILE, PRETRAINED, caffe.TEST)
print "successfully loaded classifier"

mu = np.load('/home/laurae-linux/Documents/Data_Science/Caffe/mean_image.npy')
mu = mu.mean(1).mean(1)  # average over pixels to obtain the mean (BGR) pixel values
print 'mean-subtracted values:', zip('BGR', mu)

transformer = caffe.io.Transformer({'data': net.blobs['data'].data.shape})
transformer.set_transpose('data', (2,0,1))  # move image channels to outermost dimension
transformer.set_mean('data', mu)            # subtract the dataset-mean value in each channel
transformer.set_raw_scale('data', 255)      # rescale from [0, 1] to [0, 255]
transformer.set_input_scale('data', 0.04)      # rescale from [0, 255] to [0, 255*0.04]
transformer.set_channel_swap('data', (2,1,0))  # swap channels from RGB to BGR
net.blobs['data'].reshape(1,        # batch size
                          3,         # 3-channel (BGR) images
                          228, 296)  # image size is 228x296

# test on images

path = "/home/laurae-linux/Documents/Data_Science/Caffe/train_rgb/"
dirs = os.listdir(path)
os.chdir(path)

with open("/home/laurae-linux/Documents/Data_Science/Caffe/submission.csv", 'w') as myfile:
    for file in dirs:
        input_image = caffe.io.load_image(file)
        net.blobs['data'].data[...] = transformer.preprocess('data', input_image)
        # predict takes any number of images,
        # and formats them for the Caffe net automatically
        out = net.forward()
        pred = out['fc9'][0]
        print(str(file) + " " + str(pred))
        myfile.write(str(file) + " " + str(pred) + '\n')
