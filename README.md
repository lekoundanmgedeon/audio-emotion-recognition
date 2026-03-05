# 🎵 Audio Emotion Recognition Competition

## 📌 Description
This competition challenges students to train a neural network capable of recognizing the emotion expressed in a voice recording.  
The emotions to predict include: **happiness, anger, sadness, neutral, fear, disgust, surprise**.

The goal is to practice **Deep Learning techniques applied to audio**, using spectrograms and CNN/RNN architectures.

---

## 📂 Dataset
We will use the **RAVDESS Emotional Speech Audio** dataset, available on Kaggle:  
👉 [RAVDESS Emotional Speech Audio](https://www.kaggle.com/uwrfkaggler/ravdess-emotional-speech-audio)

The dataset contains:
- 24 actors (12 male, 12 female)
- 8 emotions
- Audio recordings in `.wav` format

---

## ⚙️ Learning Objectives
- Transform audio files into **spectrograms** to make them suitable for CNNs.
- Compare different architectures (MLP, CNN, RNN, LSTM).
- Experiment with regularization and data augmentation techniques.
- Evaluate performance with metrics adapted to imbalanced classes.

---

## 🏆 Evaluation
Models will be evaluated based on:
- **Macro F1-score** (to balance class performance)
- **Overall accuracy**
- **Confusion matrix** to visualize misclassifications

---

## 🚀 Instructions
1. **Download the dataset** from Kaggle.
2. **Preprocessing**:
   - Convert `.wav` files into spectrograms (Mel-spectrogram or MFCC).
   - Normalize the data.
3. **Modeling**:
   - Implement a baseline model (simple CNN).
   - Experiment with more complex architectures (RNN, LSTM, or CNN+RNN).
4. **Submission**:
   - Provide a `.ipynb` notebook with code and results.
   - Include evaluation metrics and a short analysis.

---

## 📖 Useful Resources
- [Introduction to Spectrograms](https://pytorch.org/tutorials/beginner/audio_preprocessing_tutorial.html)
- [TensorFlow Audio Documentation](https://www.tensorflow.org/tutorials/audio)
- [Kaggle RAVDESS Dataset](https://www.kaggle.com/uwrfkaggler/ravdess-emotional-speech-audio)

---

## 📌 Baseline Example
A simple baseline model could include:
- Conversion of audio files into **Mel-spectrograms**
- CNN with 2–3 convolutional layers
- Adam optimizer
- Training for 10 epochs

---

## 📅 Deadline
Submissions must be made before **[date to be defined]**.  
Results will be compared and discussed in class.

---

## 👩‍💻 Repository Structure
