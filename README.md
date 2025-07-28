# WireGuard TUI

[![PyPI](https://img.shields.io/pypi/v/wireguard-tui?color=brightgreen&style=flat-square)](https://pypi.org/project/wireguard-tui/)  
[![Python Version](https://img.shields.io/pypi/pyversions/wireguard-tui?style=flat-square)](https://pypi.org/project/wireguard-tui/)  
![License](https://img.shields.io/github/license/nefr7t/wireguard-tui?style=flat-square)  
[![Platform](https://img.shields.io/badge/platform-Linux-blue?style=flat-square)](#)

**WireGuard TUI** — minimalistic, terminal-based WireGuard VPN manager for Linux.  
Easily toggle your VPN with a clean, colorful, and intuitive text UI.

---

## Features

- ✅ Effortlessly **enable/disable** WireGuard VPN with a single keystroke
    
- 🔒 Securely **save `sudo` credentials and config name** in `settings.json`
    
- 🎨 Colorful terminal output powered by `colorama`
    
- 🐧 Native **Linux-only** tool leveraging `wg-quick`
    

---

## Installation

### Recommended (via pip)

```bash
pip install wireguard-tui
```

### From source

```bash
git clone https://github.com/nefr7t/wireguard-tui.git
cd wireguard-tui
pip install -r requirements.txt
python3 wireguard_tui.py
```

---

## Usage & Configuration

- On first run, enter your **`sudo` password** and WireGuard **configuration name** (e.g., `wg0`).
    
- Credentials and settings are saved securely in `settings.json` for seamless future use.
    

---

## Example Interface

```
__        ___                                    _ 
\ \      / (_)_ __ ___  __ _ _   _  __ _ _ __ __| |
 \ \ /\ / /| | '__/ _ \/ _` | | | |/ _` | '__/ _` |
  \ V  V / | | | |  __/ (_| | |_| | (_| | | | (_| |
   \_/\_/  |_|_|  \___|\__, |\__,_|\__,_|_|  \__,_|
                       |___/                       

    
Current config: wg0

Choose option:
[1] Turn on VPN
[2] Turn off VPN
[3] Change settings
[4] Info
[5] Exit

```

---

## Requirements

- Linux OS (tested on Fedora, Arch Linux / EndeavourOS)
    
- WireGuard installed and configured (`wg-quick`)
    
- Python 3.7 or higher
    

---

## Contributing & Support

Contributions, feature requests, and bug reports are welcome!  
Reach out via email: **[io1n@proton.me](mailto:io1n@proton.me)**  
or open an issue / pull request on GitHub.

---

## License

Distributed under the **MIT License** — free to use, modify, and distribute.

---

⭐ If you find this tool helpful, please consider giving it a star!

---

