# Drugged Eye Detection (Production-Ready Baseline)

A hardened baseline for real-time eye-state classification ("Normal" vs "Drugged") using OpenCV + a trained Keras model.

## What was improved

- **Packaging and dependency management** via `pyproject.toml`.
- **Config management** with `.env` support and environment variable overrides.
- **CLI entrypoint** (`drugged-eye-detect`) for reliable local/server execution.
- **Structured core module** (`src/drugged_eye_detection`) separating config, detection logic, and app startup.
- **Quality guardrails** with `pytest`, `ruff`, and a Makefile.
- **Containerization** through a minimal Dockerfile.

## Project structure

```text
.
├── src/drugged_eye_detection/
│   ├── __init__.py
│   ├── cli.py
│   ├── config.py
│   └── detector.py
├── tests/
│   └── test_detector.py
├── main.py
├── pyproject.toml
├── .env.example
├── Dockerfile
└── Makefile
```

## Quick start

### 1) Install

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .[ml,dev]
```

### 2) Configure

```bash
cp .env.example .env
# edit .env if needed
```

### 3) Run

```bash
python main.py
# or
# drugged-eye-detect --model trained.h5 --threshold 0.5
```

Press **q** to quit.

## Environment variables

All variables are optional and prefixed with `DETECTOR_`:

- `DETECTOR_MODEL_PATH` (default: `trained.h5`)
- `DETECTOR_DECISION_THRESHOLD` (default: `0.5`)
- `DETECTOR_CAMERA_INDEX` (default: `0`)
- `DETECTOR_FRAME_WIDTH` (default: `640`)
- `DETECTOR_FRAME_HEIGHT` (default: `480`)
- `DETECTOR_UPDATE_INTERVAL_MS` (default: `250`)
- `DETECTOR_LOG_LEVEL` (default: `INFO`)

## Developer workflow

```bash
make install-dev
make lint
make test
```

## Training and threshold scripts

Existing training/evaluation scripts remain in this repository:

- `Training.py` for model training
- `Threshold.py` for ROC/threshold analysis

For production ML lifecycle, a next step is to migrate these into a versioned training pipeline with dataset checks, model registry, and reproducible experiment tracking.

## Disclaimer

This project is a technical baseline and **not a medical or legal diagnostic tool**. Use only in compliant and ethically reviewed contexts.
