cp -fR /home/laurae-linux/Documents/Data_Science/Caffe/train_sm /home/laurae-linux/Documents/Data_Science/Caffe/data
cd /home/laurae-linux/Documents/Data_Science/Caffe/data
mogrify -resize 192x192! -quality 100 *.jpeg
rm -rf /home/laurae-linux/Documents/Data_Science/Caffe/data/train_sm
