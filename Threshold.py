import os
import numpy as np
import cv2
from sklearn.metrics import roc_curve, auc
from tensorflow.keras.models import load_model
from tensorflow.keras.applications.resnet50 import preprocess_input
import matplotlib.pyplot as plt

# Load your model
model = load_model('trained.h5')

# Function to load and preprocess images
def load_and_preprocess_image(image_path):
    img = cv2.imread(image_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (224, 224))
    img = preprocess_input(img)
    return img

# Path to the validation folders
validation_dir = 'Dataset/valid'
drugged_dir = os.path.join(validation_dir, 'drugged_eyes')
normal_dir = os.path.join(validation_dir, 'Normal_Eyes')

# Load and preprocess images, and create labels
X_val = []
y_val = []

# Load drugged images
for img_file in os.listdir(drugged_dir):
    img_path = os.path.join(drugged_dir, img_file)
    img = load_and_preprocess_image(img_path)
    X_val.append(img)
    y_val.append(1)  # Label for drugged

# Load normal images
for img_file in os.listdir(normal_dir):
    img_path = os.path.join(normal_dir, img_file)
    img = load_and_preprocess_image(img_path)
    X_val.append(img)
    y_val.append(0)  # Label for normal

X_val = np.array(X_val)
y_val = np.array(y_val)

# Get prediction probabilities on the validation set
y_val_pred_prob = model.predict(X_val)

# Debugging: Print some of the predictions and labels
print("Sample predictions:", y_val_pred_prob[:10])
print("Sample labels:", y_val[:10])

# Ensure y_val and y_val_pred_prob are numpy arrays
y_val_pred_prob = y_val_pred_prob.flatten()  # Flatten if necessary

# Calculate the ROC curve
fpr, tpr, thresholds = roc_curve(y_val, y_val_pred_prob)

# Debugging: Check the FPR, TPR, and thresholds
print("FPR:", fpr)
print("TPR:", tpr)
print("Thresholds:", thresholds)

# Calculate the AUC score
roc_auc = auc(fpr, tpr)
print(f"ROC AUC: {roc_auc:.2f}")

# Find the optimal threshold where (tpr - fpr) is maximized
optimal_idx = np.argmax(tpr - fpr)
optimal_threshold = thresholds[optimal_idx]
print(f"Optimal Threshold: {optimal_threshold:.2f}")

# Optionally, plot the ROC curve
plt.figure()
plt.plot(fpr, tpr, color='darkorange', lw=2, label='ROC curve (area = %0.2f)' % roc_auc)
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic')
plt.legend(loc="lower right")
plt.show()
