# WireGuard TUI

**WireGuard TUI** is a simple terminal-based tool for managing WireGuard VPN on Linux.
It allows you to easily enable or disable VPN via a user-friendly text menu.

---

## Features

* Turn WireGuard VPN **on** and **off**.
* Save your `sudo` password and configuration name in `settings.json`.
* Colorful terminal output (via `colorama`).
* Works on **Linux only**.

---

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/nefr7t/wireguard-tui.git
   cd wireguard-tui
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the program:**

   ```bash
   python3 wireguard_tui.py
   ```

---

## Configuration

* On the first launch, the program will prompt you to enter your **sudo password** and WireGuard configuration name (e.g., `wg0`).
* This information is saved in a `settings.json` file (created automatically).

---

## Requirements

* **Linux** (uses `wg-quick`).
* Installed **WireGuard**.
* Python 3.7 or higher.

---

## Contributions & Ideas

If you have suggestions or want to improve the project, contact me at **[io1n@proton.me](mailto:io1n@proton.me)** or create a Pull Request.

---

## License

**MIT License** – free to use, modify, and distribute.

