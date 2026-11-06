#!/usr/bin/env bash
# chinntu-wrapper.sh — symlinked to ~/.local/bin/chinntu.
# Activates the managed venv and execs the real chinntu CLI.

CHINNTU_HOME="${CHINNTU_HOME:-$HOME/.chinntu}"
VENV="$CHINNTU_HOME/.venv"

if [[ ! -d "$VENV" ]]; then
    echo "chinntu: venv not found at $VENV" >&2
    echo "Re-run the installer: curl -fsSL https://open-jarvis.github.io/OpenJarvis/install.sh | bash" >&2
    exit 1
fi

exec "$VENV/bin/chinntu" "$@"
