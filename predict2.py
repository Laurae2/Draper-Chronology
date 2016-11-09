import os
import caffe
import numpy as np


MODEL_FILE = '/home/laurae-linux/Documents/Data_Science/Caffe/deploy.prototxt'
PRETRAINED = '/home/laurae-linux/Documents/Data_Science/Caffe/models_regression_new/train_iter_560.caffemodel'


caffe.set_mode_gpu()
caffe.set_device(0)
net = caffe.Classifier(MODEL_FILE, PRETRAINED,
                       mean=np.load('/home/laurae-linux/Documents/Data_Science/Caffe/mean_image.npy').mean(1).mean(1),
                       channel_swap=(2,1,0),
                       raw_scale=255,
                       input_scale=0.04,
                       image_dims=(228, 296))
print "successfully loaded classifier"

# test on images

path = "/home/laurae-linux/Documents/Data_Science/Caffe/train_rgb/"
dirs = os.listdir(path)
os.chdir(path)

with open("/home/laurae-linux/Documents/Data_Science/Caffe/submission.csv", 'w') as myfile:
    for file in dirs:
        input_image = caffe.io.load_image(file)
        # predict takes any number of images,
        # and formats them for the Caffe net automatically
        pred = net.predict([input_image])
        pred = pred[0]
        print(str(file) + " " + str(pred))
        myfile.write(str(file) + " " + str(pred) + '\n')
