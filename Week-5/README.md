# Text Generation using Vanilla RNN, LSTM and GRU

## colab link

https://colab.research.google.com/drive/1CtS5c8oQHLSZg1xryq0q4dHxQL7MCO-0?usp=sharing

## Overview

This project demonstrates text generation using three recurrent neural network architectures:

* Vanilla RNN
* LSTM (Long Short-Term Memory)
* GRU (Gated Recurrent Unit)

The objective is to learn grammar, sentence structure, and contextual dependencies from a text corpus and generate meaningful text through next-word prediction.

## Problem Statement

Design and implement a Deep Learning model capable of learning the underlying structure, grammar, and contextual dependencies of a given text corpus to generate coherent and meaningful text sequences using:

1. Vanilla RNN
2. LSTM
3. GRU

## Features

* Text preprocessing and tokenization
* N-gram sequence generation
* Word embeddings
* Vanilla RNN implementation
* LSTM implementation
* GRU implementation
* Training loss comparison
* Accuracy comparison
* Text generation using trained models

## Technologies Used

* Python
* TensorFlow / Keras
* NumPy
* Matplotlib

## Project Workflow

1. Load text corpus
2. Tokenize text data
3. Create n-gram sequences
4. Build and train RNN model
5. Build and train LSTM model
6. Build and train GRU model
7. Compare performance
8. Generate text sequences

## Results

The experimental results show:

* Vanilla RNN learns short-term patterns effectively.
* LSTM captures long-term dependencies through memory cells.
* GRU provides performance similar to LSTM with fewer parameters and faster training.

## Future Improvements

* Train on larger datasets such as Shakespeare text
* Use Bidirectional LSTM
* Apply Attention Mechanisms
* Experiment with Transformer-based architectures
