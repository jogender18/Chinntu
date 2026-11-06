"""Persistent Windows wake-word listener."""

from __future__ import annotations

import os
import shutil
import subprocess
from pathlib import Path

import click

TASK_NAME = "ChinntuWakeWord"


def _listener_script(model: str, wake_word: str, project_dir: Path, uv_path: str) -> Path:
    script = Path.home() / ".chinntu" / "wake-word.ps1"
    script.parent.mkdir(parents=True, exist_ok=True)
    values = {
        "project": str(project_dir),
        "uv": uv_path,
        "model": model,
        "wake": wake_word,
    }
    script.write_text(
        "$ErrorActionPreference = 'Stop'\n"
        f"Set-Location -LiteralPath {values['project']!r}\n"
        f"& {values['uv']!r} run --directory {values['project']!r} "
        f"chinntu chat --model {values['model']!r} "
        f"--wake-word {values['wake']!r}\n",
        encoding="utf-8",
    )
    return script


@click.command("wake-word")
@click.option("--model", default="llama3.2:3b", show_default=True)
@click.option("--wake-word", default="hey chinntu", show_default=True)
@click.option("--install", "install_task", is_flag=True, help="Start automatically at Windows login.")
@click.option("--uninstall", "uninstall_task", is_flag=True, help="Remove automatic startup.")
def wake_word(model: str, wake_word: str, install_task: bool, uninstall_task: bool) -> None:
    """Listen continuously for a wake phrase and start voice chat."""
    if os.name != "nt":
        raise click.ClickException("Persistent wake-word startup is currently supported on Windows only.")
    if install_task and uninstall_task:
        raise click.ClickException("Choose either --install or --uninstall, not both.")

    if uninstall_task:
        subprocess.run(
            ["schtasks", "/Delete", "/TN", TASK_NAME, "/F"],
            check=False,
            capture_output=True,
            text=True,
        )
        click.echo("Chinntu wake-word startup removed.")
        return

    uv_path = shutil.which("uv") or str(Path.home() / ".local" / "bin" / "uv.exe")
    if not Path(uv_path).exists():
        raise click.ClickException("Could not find uv.exe. Add uv to PATH and try again.")
    project_dir = Path.cwd().resolve()
    script = _listener_script(model, wake_word, project_dir, uv_path)
    task_command = f'powershell.exe -NoProfile -WindowStyle Hidden -ExecutionPolicy Bypass -File "{script}"'

    if install_task:
        result = subprocess.run(
            [
                "schtasks",
                "/Create",
                "/SC",
                "ONLOGON",
                "/TN",
                TASK_NAME,
                "/TR",
                task_command,
                "/F",
            ],
            check=False,
            capture_output=True,
            text=True,
        )
        if result.returncode:
            raise click.ClickException(result.stderr.strip() or result.stdout.strip())
        click.echo("Chinntu will listen for “Hey Chinntu” after your next Windows login.")
        return

    click.echo(f'Listening for "{wake_word}"… Press Ctrl+C to stop.')
    from chinntu.cli.chat_cmd import chat

    ctx = click.get_current_context()
    ctx.invoke(
        chat,
        engine_key=None,
        model_name=model,
        pick_model=False,
        agent_name=None,
        tools=None,
        system_prompt=None,
        persona_name=None,
        voice_mode=True,
        wake_word=wake_word,
        num_ctx=None,
        num_gpu=None,
        skip_runtime_panel=False,
    )
