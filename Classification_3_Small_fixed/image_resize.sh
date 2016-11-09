cp -fR /home/laurae-linux/Documents/Data_Science/Caffe/old_data /home/laurae-linux/Documents/Data_Science/Caffe/data
cd /home/laurae-linux/Documents/Data_Science/Caffe/data
mogrify -resize 256x192! -quality 100 *.jpg
rm -rf /home/laurae-linux/Documents/Data_Science/Caffe/data/old_data
