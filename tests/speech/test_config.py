"""Tests for speech configuration."""

from chinntu.core.config import ChinntuConfig, SpeechConfig


def test_speech_config_defaults():
    cfg = SpeechConfig()
    assert cfg.backend == "auto"
    assert cfg.model == "base"
    assert cfg.language == ""
    assert cfg.device == "auto"
    assert cfg.compute_type == "float16"


def test_chinntu_config_has_speech():
    cfg = ChinntuConfig()
    assert hasattr(cfg, "speech")
    assert isinstance(cfg.speech, SpeechConfig)
    assert cfg.speech.backend == "auto"


def test_chinntu_system_has_speech_backend():
    """ChinntuSystem has a speech_backend attribute."""
    from chinntu.system import ChinntuSystem

    assert "speech_backend" in ChinntuSystem.__dataclass_fields__
