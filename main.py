#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
import cv2
import numpy as np
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import QTimer
from tensorflow.keras.models import load_model
from tensorflow.keras.applications.resnet50 import preprocess_input

# Load Haar cascade classifiers for face and eye detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# Class for the video display widget
class VideoDisplayWidget(QWidget):
    def __init__(self, model):
        super().__init__()
        self.setWindowTitle("Drug Eye Detection")
        self.video_capture = cv2.VideoCapture(0)
        self.video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        self.video_label = QLabel()
        layout = QVBoxLayout()
        layout.addWidget(self.video_label)
        self.setLayout(layout)
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(1000)  # Update every second
        self.model = model
        self.model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])  # Compile the model

    # Function to preprocess and classify frames
    def update_frame(self):
        ret, frame = self.video_capture.read()
        if ret:
            # Detect faces in the frame
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

            for (x, y, w, h) in faces:
                # Extract region of interest containing the face
                face_region = frame[y:y + h, x:x + w]

                # Detect eyes within the face region
                eyes = eye_cascade.detectMultiScale(face_region)

                # For each detected eye
                for (ex, ey, ew, eh) in eyes:
                    # Extract region of interest containing the eye
                    eye = face_region[ey:ey + eh, ex:ex + ew]

                    # Preprocess eye region
                    eye_resized = cv2.resize(eye, (224, 224))
                    eye_preprocessed = preprocess_input(np.expand_dims(eye_resized, axis=0))

                    # Perform inference
                    prediction = self.model.predict(eye_preprocessed)

                    # Display prediction on frame
                    label = 'Drugged Eye' if prediction > 0.5 else 'Normal Eye'
                    cv2.putText(frame, label, (x+ex, y+ey - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                    cv2.rectangle(frame, (x+ex, y+ey), (x+ex+ew, y+ey+eh), (255, 0, 0), 2)

            # Display frame on GUI
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(image)
            self.video_label.setPixmap(pixmap)


if __name__ == "__main__":
    # Load the trained model
    model = load_model('trained.h5')

    # Initialize the application
    app = QApplication(sys.argv)
    main_window = QWidget()
    layout = QVBoxLayout()
    video_widget = VideoDisplayWidget(model)
    layout.addWidget(video_widget)
    main_window.setLayout(layout)
    main_window.show()
    sys.exit(app.exec_())


# In[ ]:




