# Draper-Chronology

![](http://5047-presscdn.pagely.netdna-cdn.com/wp-content/uploads/2016/09/draper_lg.png)

Draper Image Chronology competition on Kaggle: Deep Learning tests (Caffe)

This repository includes many neural architectures. They all fail to train for better than random predictions, in any case.

The objective is to maximize the **Spearman Correlation Coefficient**. Not easy as it is both an image processing task, but also an ranking/ordinality task!

# Kaggle Blog Post

See the Kaggle blog post for a working solution (does not involve any neural networks, only feature engineering via ImageJ, and Extreme Gradient Boosting via data augmentation): http://blog.kaggle.com/2016/09/08/draper-satellite-image-chronology-damien-soukhavong/ - it also highlights a real world usage (depicting a failed attempt proven statistically via a Monte-Carlo).

My solution was very quick and took under 2 hours when using multi-threading appropriately, especially on ImageJ. A single laptop with an i7 4x-core + 8GB RAM can handle this easily. People would say I am crazy to select 0.0xxx submissions for the private LB. But if we know they work on Cross-Validation, why not selecting them?

![](http://5047-presscdn.pagely.netdna-cdn.com/wp-content/uploads/2016/09/image04.jpg)

# Image pre-processing

To pre-process the data, I recommend to use ImageJ to lower the risk of overfitting (will not occur, anyway): https://www.kaggle.com/laurae2/draper-satellite-image-chronology/imagej-pre-processing-for-deep-learning

# Applications

## Google Earth Images

Here is a Monte-Carlo simulation on Google Earth Images on the best model, Y representing the Spearman Correlation Coefficient:

![](http://5047-presscdn.pagely.netdna-cdn.com/wp-content/uploads/2016/09/image02.png)

## Real world images

Here is a Monte-Carlo simulation on my pictures I took for the best model, Y representing the Spearman Correlation Coefficient:

![](http://5047-presscdn.pagely.netdna-cdn.com/wp-content/uploads/2016/09/image01.png)

# My Competition Solution

My competition solution highlighted on Kaggle Blog Post is not posted here. Some highlighted pictures are below:

![](http://5047-presscdn.pagely.netdna-cdn.com/wp-content/uploads/2016/09/image00.png)

![](http://5047-presscdn.pagely.netdna-cdn.com/wp-content/uploads/2016/09/stack_aligned_selection-900x676.gif)

![](http://5047-presscdn.pagely.netdna-cdn.com/wp-content/uploads/2016/09/RGB_stack-1024x770.jpg)
