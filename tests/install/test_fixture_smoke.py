"""Smoke test that the tmp_chinntu_home fixture works."""

from __future__ import annotations

from pathlib import Path

from chinntu.core import config as config_mod


def test_fixture_redirects_default_config_dir(tmp_chinntu_home: Path) -> None:
    assert config_mod.DEFAULT_CONFIG_DIR == tmp_chinntu_home
    assert tmp_chinntu_home.exists()
    assert (tmp_chinntu_home / ".state").exists()
    assert (tmp_chinntu_home / ".state" / "models").exists()


def test_fixture_redirects_config_path(tmp_chinntu_home: Path) -> None:
    assert config_mod.DEFAULT_CONFIG_PATH == tmp_chinntu_home / "config.toml"
