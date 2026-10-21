# Port Inventory

Every TCP port an app or service on this machine is known to bind. Check this file before picking a port for anything new, and add the new port here in the same change.

Convention: each app owns a hundred-block in the 5xxx (UI) and 8xxx (API) ranges with matching last two digits. For example, an app on 5400 (UI) and 8400 (API) reserves 5400-5499 and 8400-8499.

Live check: `lsof -nP -iTCP -sTCP:LISTEN`

## Apps

### Sample App (`Apps/sample-app/`)

| Port | What | Mode | Bind |
|---|---|---|---|
| 5400 | Vite dev UI | `./run-dev.sh` | localhost |
| 8400 | uvicorn API with reload | `./run-dev.sh` | localhost |

Env: `SAMPLE_API_PORT` / `SAMPLE_UI_PORT`. Not managed by launchd; started by hand.

Reserved for growth: 5401-5499 / 8401-8499.

## System and background services

| Port | What | Owner | Bind |
|---|---|---|---|
| (none yet) | | | |

## Free blocks

- 5100-5399, 5500-5999
- 8100-8399, 8500-8999
