Here’s the **English version** of your README:

---

# WireGuard TUI (Terminal User Interface)

A simple terminal-based interface for managing WireGuard VPN on Linux.

## Features

* **Turn VPN on/off** using `wg-quick up/down`.
* **Save settings** (sudo password and config name) to `settings.json`.
* **Interactive menu** for easy VPN control.
* **Colorful interface** powered by `colorama`.

## Requirements

* **Linux** (this script works only on Linux).
* **Python 3.8+**.
* Installed **WireGuard** (`wg-quick` must be available in PATH).
* Python dependencies:

  ```bash
  pip install colorama
  ```

## Installation & Run

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/wireguard-tui.git
   cd wireguard-tui
   ```
2. Run the script:

   ```bash
   python3 main.py
   ```
3. On the first run, the program will ask for your sudo password and the WireGuard config name (e.g., `wg0`).

## Usage

The menu provides the following options:

```
[1] Turn on VPN      — start VPN.
[2] Turn off VPN     — stop VPN.
[3] Change settings  — update password or config name.
[4] Info             — program info.
[5] Exit             — quit the program.
```

## Settings

All settings are stored in the `settings.json` file in the project root:

```json
{
  "password": "your_sudo_password",
  "config": "wg0"
}
```

## Warnings

* Your `sudo` password is stored in **plain text** in `settings.json`!
  Use this script **only on personal devices** you fully trust.
* The script requires `sudo` privileges to execute `wg-quick`.

## Contact

For improvements or feedback, email: **[io1n@proton.me](mailto:io1n@proton.me)**.

---

Would you like me to **add an ASCII-art preview of your menu** (like in your `menu()` function) and include a ready-to-use `requirements.txt` in this README?

