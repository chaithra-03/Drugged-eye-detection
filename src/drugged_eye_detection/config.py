from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    model_path: str = Field(default="trained.h5", description="Path to model file")
    decision_threshold: float = Field(default=0.5, ge=0.0, le=1.0)
    camera_index: int = Field(default=0, ge=0)
    frame_width: int = Field(default=640, ge=160)
    frame_height: int = Field(default=480, ge=120)
    update_interval_ms: int = Field(default=250, ge=20)
    log_level: str = Field(default="INFO")

    model_config = SettingsConfigDict(
        env_prefix="DETECTOR_",
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )
