#python /home/laurae-linux/Downloads/caffe/build/tools/extra/parse_log.py /home/laurae-linux/Documents/Data_Science/Caffe/log/my_model.log .
#gnuplot -persist /home/laurae-linux/Documents/Data_Science/Caffe/gnuplot_commands

refresh_log() {
  while true; do
    python /home/laurae-linux/Downloads/caffe/tools/extra/parse_log.py /home/laurae-linux/Documents/Data_Science/Caffe/log/my_model.log /home/laurae-linux/Documents/Data_Science/Caffe/log
    sleep 10 
  done
}
refresh_log & 
sleep 2
gnuplot /home/laurae-linux/Documents/Data_Science/Caffe/gnuplot_commands
