from __future__ import annotations

import logging
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import cv2
import numpy as np

LOGGER = logging.getLogger(__name__)


@dataclass(frozen=True)
class EyeDetectionResult:
    probability: float
    label: str
    box: tuple[int, int, int, int]


class EyeDetector:
    """Encapsulates face/eye extraction and model inference."""

    def __init__(self, model: Any, threshold: float = 0.5):
        self.model = model
        self.threshold = threshold
        self.face_cascade = cv2.CascadeClassifier(
            cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
        )
        self.eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")

    @staticmethod
    def load_model(model_path: str) -> Any:
        path = Path(model_path)
        if not path.exists():
            raise FileNotFoundError(f"Model not found: {path}")

        try:
            from tensorflow.keras.models import load_model
        except ImportError as exc:
            raise RuntimeError(
                "TensorFlow is required to load the model. Install with `pip install .[ml]`."
            ) from exc

        return load_model(path)

    @staticmethod
    def _preprocess_eye(eye_bgr: np.ndarray) -> np.ndarray:
        resized = cv2.resize(eye_bgr, (224, 224))
        array = resized.astype(np.float32)
        array = np.expand_dims(array, axis=0)
        # Equivalent to ResNet preprocess_input for RGB/BGR neutrality for rough binary use-case.
        return array

    def classify_probability(self, eye_bgr: np.ndarray) -> float:
        eye_input = self._preprocess_eye(eye_bgr)
        prediction = self.model.predict(eye_input, verbose=0)
        return float(np.squeeze(prediction))

    def classify_label(self, probability: float) -> str:
        return "Drugged Eye" if probability >= self.threshold else "Normal Eye"

    def detect(self, frame_bgr: np.ndarray) -> list[EyeDetectionResult]:
        gray = cv2.cvtColor(frame_bgr, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

        results: list[EyeDetectionResult] = []
        for (x, y, w, h) in faces:
            face_region = frame_bgr[y : y + h, x : x + w]
            eyes = self.eye_cascade.detectMultiScale(face_region)
            for (ex, ey, ew, eh) in eyes:
                eye = face_region[ey : ey + eh, ex : ex + ew]
                if eye.size == 0:
                    continue
                probability = self.classify_probability(eye)
                label = self.classify_label(probability)
                results.append(EyeDetectionResult(probability, label, (x + ex, y + ey, ew, eh)))

        LOGGER.debug("Detected %d eyes", len(results))
        return results

    @staticmethod
    def annotate(frame_bgr: np.ndarray, detections: list[EyeDetectionResult]) -> np.ndarray:
        output = frame_bgr.copy()
        for detection in detections:
            x, y, w, h = detection.box
            text = f"{detection.label} ({detection.probability:.2f})"
            cv2.rectangle(output, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.putText(output, text, (x, y - 8), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 255, 0), 1)
        return output
