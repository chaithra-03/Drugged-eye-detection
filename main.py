"""Backward-compatible entrypoint for realtime detection."""

from drugged_eye_detection.cli import main


if __name__ == "__main__":
    raise SystemExit(main())
