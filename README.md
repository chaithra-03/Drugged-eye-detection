# Drugged Eye Detection System

This project implements a **real-time drugged eye detection system** using deep learning techniques. The system classifies images of human eyes into two categories: "Normal Eyes" and "Drugged Eyes." The detection is performed using a fine-tuned ResNet50 model, and the system includes a user-friendly GUI built with PyQt5 for seamless interaction.

## Problem Statement
The increasing prevalence of drug abuse has raised concerns about public safety, especially when individuals under the influence of drugs engage in activities requiring clear vision, such as driving. Traditional methods of detecting impaired individuals may not always be effective. This project aims to develop a **real-time drugged eye detection system** that automates the classification of eye images into "Normal Eyes" or "Drugged Eyes," providing a solution for safety monitoring.

## Solution Overview
The solution involves the following components:
1. **Deep Learning Model:** A fine-tuned **ResNet50** model for classifying eye images as either "Normal" or "Drugged."
2. **Graphical User Interface (GUI):** Built using **PyQt5** to enable users to upload eye images and receive real-time classification results.
3. **Real-Time Image Processing:** Utilizes **OpenCV** for processing uploaded images and performing predictions using the trained deep learning model.

## Technologies Used
- **PyQt5:** For building the graphical user interface.
- **TensorFlow:** For training and inference of the deep learning model.
- **Keras:** To build and fine-tune the ResNet50 model.
- **OpenCV:** For real-time image processing.
- **Matplotlib:** To visualize model performance metrics (e.g., ROC curve).
- **Python:** The programming language used for the entire implementation.

## System Workflow
1. **Real-Time Video Input**:
    - The system uses **OpenCV** to capture video in real time from the user's webcam or other video sources.
    - The user interacts with the **PyQt5 GUI** to start or stop the video stream.
    - The system processes each frame of the video feed to detect whether the eyes are "Normal" or "Drugged" based on the trained deep learning model.

2. **Deep Learning Model**:
    - The model is built using **ResNet50** and fine-tuned for binary classification: **Normal Eyes** vs. **Drugged Eyes**.
    - The model is trained using a dataset of labeled images and employs transfer learning to leverage pre-trained features for efficient training.
  
3. **Real-Time Processing**:
    - **OpenCV** captures each frame from the video stream.
    - The frame is passed to the trained ResNet50 model to predict if the eyes in the frame are normal or drugged.
    - The prediction result is displayed in real time on the GUI.

## Model Training
The **ResNet50** model was pre-trained on the **ImageNet** dataset and fine-tuned using a custom dataset of eye images labeled as "Normal Eyes" or "Drugged Eyes." The model utilizes **transfer learning**, enabling it to classify eye images with high accuracy.

- **Input Image:** Eye image (preprocessed for the model).
- **Output:** Binary classification result: "Normal Eyes" or "Drugged Eyes."

## Results and Evaluation
The performance of the model can be evaluated using the following metrics:
- **Accuracy:** The percentage of correctly classified images.
- **Precision and Recall:** To measure the model's ability to correctly identify each class.
- **ROC Curve:** To visualize the trade-off between true positive rate and false positive rate.
- **Confusion Matrix:** To provide a breakdown of the true positives, true negatives, false positives, and false negatives.

Example evaluation results:
- **Accuracy:** 95%
- **Precision:** 93%
- **Recall:** 92%
- **AUC (Area Under Curve) in ROC:** 0.98

## Conclusion
This **Drugged Eye Detection System** offers an automated solution for detecting drug-induced eye changes, contributing to public safety. By utilizing **ResNet50** and **PyQt5**, the system is both accurate and easy to use. **OpenCV** ensures real-time processing of images, and **Matplotlib** helps visualize model performance.

Further improvements can include expanding the dataset, refining the model, and adding more advanced features to the GUI, such as displaying previous detection history or integrating with real-time monitoring systems.


