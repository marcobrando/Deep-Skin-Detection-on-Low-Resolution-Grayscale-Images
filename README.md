# Deep Skin Detection on Low Resolution Grayscale Images

![skin_detection](results.jpg)


This project presents a facial skin detection method, based on a deep learning architecture,  that is able to precisely associate a skin label to each pixel of a given image depicting a face. This is an important preliminary step in many applications, such as remote photoplethysmography (rPPG) in which the hearth rate of a subject needs to be estimated analyzing a video of his/her face. The proposed method can detect skin pixels even in low resolution grayscale face images (64x32 pixel). 

## Model

The trained keras model could be find in "model/net.h5"

## Data

Labeled face segmentation data could be find in "data/GT". This are skin mask obtained from the MUCT and Helen dataset. These datasets are downloadable at http://www.milbo.org/muct/ and http://www.ifp.illinois.edu/~vuongle2/helen/ respectivly. Training labeled were obtained automatically (so there could be some errors), while testing ones were manually labeled.

## Dependencies

Python, Opencv, numpy, Keras, Tensorflow

## Testing the dataset

In order to test the model run:
```
python run_model.py
```
