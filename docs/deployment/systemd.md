# systemd Service (Linux)

Chinntu includes a systemd unit file for running the API server as a managed background service on Linux. This provides automatic startup on boot, crash recovery, and integration with standard Linux service management tools.

## Prerequisites

Before installing the service, ensure that:

1. Chinntu is installed in a virtual environment at `/opt/chinntu/.venv` (or adjust paths accordingly).
2. A dedicated `chinntu` system user exists (recommended for security).
3. An inference engine (such as Ollama) is running and accessible.

Create the user and installation directory:

```bash
sudo useradd --system --create-home --home-dir /opt/chinntu chinntu
sudo -u chinntu python3 -m venv /opt/chinntu/.venv
sudo -u chinntu git clone https://github.com/jogender18/Chinntu.git /opt/chinntu/Chinntu
cd /opt/chinntu/Chinntu && sudo -u chinntu uv sync --extra server
```

## Installing the Service

The unit binds `0.0.0.0`, so an **API key is required** — and the unit
declares `EnvironmentFile=/etc/chinntu/env` (no `-` prefix), so it will
**fail to start** until that file exists with a key. Create it first:

```bash
sudo mkdir -p /etc/chinntu
echo "CHINNTU_API_KEY=$(chinntu auth generate-key)" | sudo tee /etc/chinntu/env
sudo chmod 600 /etc/chinntu/env
```

Then copy the unit file, reload the daemon, and enable the service:

```bash
sudo cp deploy/systemd/chinntu.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable chinntu
sudo systemctl start chinntu
```

Clients must send `Authorization: Bearer <key>` on `/v1/*` and `/api/*`
requests. (If you instead bind to `127.0.0.1`, the key is optional and you
can drop the `EnvironmentFile` line.)

Verify it is running:

```bash
sudo systemctl status chinntu
```

## Service File Reference

The provided unit file at `deploy/systemd/chinntu.service`:

```ini
[Unit]
Description=Chinntu API Server
After=network.target

[Service]
Type=simple
User=chinntu
WorkingDirectory=/opt/chinntu
ExecStart=/opt/chinntu/.venv/bin/chinntu serve --host 0.0.0.0 --port 8000
Restart=on-failure
RestartSec=5
Environment=HOME=/opt/chinntu

[Install]
WantedBy=multi-user.target
```

### `[Unit]` Section

| Directive     | Value              | Description                                                                 |
|---------------|--------------------|-----------------------------------------------------------------------------|
| `Description` | `Chinntu API Server` | Human-readable name shown in `systemctl status` and logs.              |
| `After`       | `network.target`   | Delays startup until the network stack is available, since the server binds to a network socket and may need to reach a remote engine. |

### `[Service]` Section

| Directive          | Value                                                              | Description                                                                                     |
|--------------------|--------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| `Type`             | `simple`                                                           | The process started by `ExecStart` is the main service process. systemd considers the service started immediately. |
| `User`             | `chinntu`                                                       | Runs the server as the `chinntu` user rather than root, limiting the blast radius of any security issue. |
| `WorkingDirectory` | `/opt/chinntu`                                                  | Sets the working directory for the process. This is where Chinntu looks for local files and writes data. |
| `ExecStart`        | `/opt/chinntu/.venv/bin/chinntu serve --host 0.0.0.0 --port 8000` | The command to start the server. Uses the full path to the `chinntu` binary inside the virtual environment. |
| `Restart`          | `on-failure`                                                       | Automatically restarts the service if it exits with a non-zero exit code. Does not restart on clean shutdown (`systemctl stop`). |
| `RestartSec`       | `5`                                                                | Waits 5 seconds before attempting a restart, preventing rapid restart loops if the service crashes immediately on startup. |
| `Environment`      | `HOME=/opt/chinntu`                                             | Sets the `HOME` environment variable so Chinntu finds its configuration at `~/.chinntu/config.toml` (resolving to `/opt/chinntu/.chinntu/config.toml`). |

### `[Install]` Section

| Directive    | Value               | Description                                                                                 |
|--------------|---------------------|---------------------------------------------------------------------------------------------|
| `WantedBy`   | `multi-user.target` | The service starts when the system reaches multi-user mode (standard boot target for servers). `systemctl enable` creates a symlink under this target. |

## Configuration Options

### Changing the Bind Address and Port

Edit the `ExecStart` line to change the host or port:

```ini
ExecStart=/opt/chinntu/.venv/bin/chinntu serve --host 127.0.0.1 --port 9000
```

!!! tip
    Binding to `127.0.0.1` restricts access to localhost only. Use this when running behind a reverse proxy like Nginx or Caddy.

### Setting the Engine and Model

Pass additional flags to `chinntu serve`:

```ini
ExecStart=/opt/chinntu/.venv/bin/chinntu serve --host 0.0.0.0 --port 8000 --engine ollama --model qwen3:8b
```

### Adding Environment Variables

Add multiple `Environment` directives or use `EnvironmentFile` for complex configurations:

```ini
[Service]
Environment=HOME=/opt/chinntu
Environment=CHINNTU_ENGINE_DEFAULT=vllm
Environment=CHINNTU_OLLAMA_HOST=http://localhost:11434
```

Or load from a file:

```ini
[Service]
EnvironmentFile=/opt/chinntu/.env
```

### Changing the User

If you prefer a different service user, update both the `User` directive and the paths:

```ini
[Service]
User=myuser
WorkingDirectory=/home/myuser/chinntu
ExecStart=/home/myuser/chinntu/.venv/bin/chinntu serve --host 0.0.0.0 --port 8000
Environment=HOME=/home/myuser/chinntu
```

### Using a Configuration File

Ensure the configuration file exists at the path where `HOME` points:

```bash
sudo -u chinntu mkdir -p /opt/chinntu/.chinntu
sudo -u chinntu cp config.toml /opt/chinntu/.chinntu/config.toml
```

The server reads `~/.chinntu/config.toml` on startup, where `~` resolves from the `HOME` environment variable.

## Viewing Logs

Chinntu logs are captured by journald. View them with `journalctl`:

```bash
# View all logs for the service
sudo journalctl -u chinntu

# Follow logs in real time
sudo journalctl -u chinntu -f

# View logs since the last boot
sudo journalctl -u chinntu -b

# View logs from the last hour
sudo journalctl -u chinntu --since "1 hour ago"

# View only error-level messages
sudo journalctl -u chinntu -p err
```

## Managing the Service

### Start, Stop, and Restart

```bash
# Start the service
sudo systemctl start chinntu

# Stop the service
sudo systemctl stop chinntu

# Restart the service (stop + start)
sudo systemctl restart chinntu

# Reload configuration without full restart (sends SIGHUP)
sudo systemctl reload-or-restart chinntu
```

### Check Status

```bash
sudo systemctl status chinntu
```

Example output:

```
● chinntu.service - Chinntu API Server
     Loaded: loaded (/etc/systemd/system/chinntu.service; enabled; preset: enabled)
     Active: active (running) since Fri 2026-02-21 10:00:00 UTC; 2h ago
   Main PID: 12345 (chinntu)
      Tasks: 4 (limit: 4915)
     Memory: 256.0M
        CPU: 1min 23s
     CGroup: /system.slice/chinntu.service
             └─12345 /opt/chinntu/.venv/bin/python /opt/chinntu/.venv/bin/chinntu serve --host 0.0.0.0 --port 8000
```

### Enable and Disable on Boot

```bash
# Enable automatic start on boot
sudo systemctl enable chinntu

# Disable automatic start on boot
sudo systemctl disable chinntu
```

### Apply Changes After Editing the Unit File

After modifying `/etc/systemd/system/chinntu.service`, reload the systemd daemon and restart the service:

```bash
sudo systemctl daemon-reload
sudo systemctl restart chinntu
```

## Running Alongside Ollama

If Ollama is also managed via systemd, you can add an ordering dependency so the Chinntu service waits for Ollama to start:

```ini
[Unit]
Description=Chinntu API Server
After=network.target ollama.service
Requires=ollama.service
```

| Directive  | Description                                                              |
|------------|--------------------------------------------------------------------------|
| `After`    | Ensures Chinntu starts after Ollama.                                  |
| `Requires` | If Ollama fails to start, Chinntu will not start either.              |

!!! note
    Use `Wants` instead of `Requires` if you want Chinntu to start even when Ollama is unavailable (for example, if you plan to start Ollama manually later).
