"""Core package for production-ready drugged eye detection."""

from .config import Settings
from .detector import EyeDetectionResult, EyeDetector

__all__ = ["Settings", "EyeDetector", "EyeDetectionResult"]
