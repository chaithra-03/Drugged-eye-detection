import numpy as np

from drugged_eye_detection.detector import EyeDetector


class DummyModel:
    def __init__(self, value: float):
        self.value = value

    def predict(self, inputs, verbose=0):
        assert inputs.shape[0] == 1
        return np.array([[self.value]], dtype=np.float32)


def test_classify_label_threshold() -> None:
    detector = EyeDetector(model=DummyModel(0.7), threshold=0.5)
    assert detector.classify_label(0.8) == "Drugged Eye"
    assert detector.classify_label(0.2) == "Normal Eye"


def test_classify_probability_float() -> None:
    detector = EyeDetector(model=DummyModel(0.42), threshold=0.5)
    eye = np.zeros((32, 32, 3), dtype=np.uint8)
    probability = detector.classify_probability(eye)
    assert isinstance(probability, float)
    assert 0 <= probability <= 1
