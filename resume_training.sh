#!/usr/bin/env sh

/home/laurae-linux/Downloads/caffe/build/tools/caffe train \
    --solver=/home/laurae-linux/Documents/Data_Science/Caffe/solver.prototxt \
    --snapshot=/home/laurae-linux/Documents/Data_Science/Caffe/models/train_iter_100.solverstate 2>&1 | tee -a /home/laurae-linux/Documents/Data_Science/Caffe/log/my_model.log --ignore-interrupts
