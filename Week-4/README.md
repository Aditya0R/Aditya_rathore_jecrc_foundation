## Google Colab Notebook

Open the project directly in Google Colab:

**Colab Link:**
https://colab.research.google.com/drive/1rSoBMPfq3JpZV-YIZxJtZSMjXiPL1i_J

# CIFAR-10 Image Classification: ANN vs CNN vs Data Augmented CNN

## Project Overview

This project demonstrates image classification on the CIFAR-10 dataset using Deep Learning techniques. The objective is to compare the performance of Artificial Neural Networks (ANN) and Convolutional Neural Networks (CNN) and analyze the impact of advanced training strategies such as Data Augmentation and Early Stopping.

The project was implemented using TensorFlow and Keras in Google Colab.

## Dataset

**CIFAR-10** is a benchmark image classification dataset containing 60,000 color images of size 32×32 across 10 classes.

### Classes

* Airplane
* Automobile
* Bird
* Cat
* Deer
* Dog
* Frog
* Horse
* Ship
* Truck

### Dataset Split

* Training Images: 50,000
* Testing Images: 10,000


## Models Implemented

### 1. Baseline ANN

* Dense Layers
* ReLU Activation
* Dropout Regularization
* Flattened Image Input

### 2. Improved ANN

* Increased Dense Layer Configuration
* Additional Hidden Layers
* Early Stopping Integration

### 3. CNN

* Conv2D Layers
* Batch Normalization
* Max Pooling
* Dropout
* Dense Classification Layer

### 4. Data Augmented CNN

* RandomFlip
* RandomRotation
* RandomZoom
* Early Stopping
* Extended Training

## Training Strategies

* Image Normalization (0–255 → 0–1)
* Adam Optimizer
* Sparse Categorical Crossentropy Loss
* Validation Split
* Early Stopping
* Data Augmentation
* Extended Training (20 Epochs)

## Key Observations

* ANN loses spatial information because images are flattened into vectors.
* CNN captures local image features using convolution operations.
* Batch Normalization improves training stability.
* Data Augmentation helps improve generalization and reduces overfitting.
* CNN significantly outperforms ANN for image classification tasks.

## Technologies Used

* Python
* TensorFlow
* Keras
* NumPy
* Pandas
* Matplotlib
* Google Colab

## Project Files

* CIFAR10_ANN_CNN_Learning_Project.ipynb
* README.md
