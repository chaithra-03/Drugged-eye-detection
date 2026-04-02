from __future__ import annotations

import argparse
import logging

import cv2

from .config import Settings
from .detector import EyeDetector


def configure_logging(level: str) -> None:
    logging.basicConfig(
        level=getattr(logging, level.upper(), logging.INFO),
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Realtime drugged eye detection")
    parser.add_argument("--model", help="Path to trained model")
    parser.add_argument("--threshold", type=float, help="Decision threshold, default from env/.env")
    parser.add_argument("--camera-index", type=int, help="Camera index")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    settings = Settings()

    model_path = args.model or settings.model_path
    threshold = args.threshold if args.threshold is not None else settings.decision_threshold
    camera_index = args.camera_index if args.camera_index is not None else settings.camera_index

    configure_logging(settings.log_level)
    logger = logging.getLogger("drugged_eye_detection")

    model = EyeDetector.load_model(model_path)
    detector = EyeDetector(model=model, threshold=threshold)

    cap = cv2.VideoCapture(camera_index)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, settings.frame_width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, settings.frame_height)

    if not cap.isOpened():
        logger.error("Unable to open camera index %s", camera_index)
        return 1

    logger.info("Detection started. Press 'q' to exit.")
    while True:
        ret, frame = cap.read()
        if not ret:
            logger.warning("Failed to capture frame; stopping")
            break

        detections = detector.detect(frame)
        annotated = detector.annotate(frame, detections)
        cv2.imshow("Drugged Eye Detection", annotated)

        if cv2.waitKey(settings.update_interval_ms) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
