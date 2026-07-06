# GNOME Tuner

> A simple, modern instrument tuner for the GNOME desktop — built with GTK4 and libadwaita.

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](LICENSE)
[![Made with GTK4](https://img.shields.io/badge/GTK-4-729fcf.svg)](https://www.gtk.org/)
[![libadwaita](https://img.shields.io/badge/libadwaita-1-9141ac.svg)](https://gnome.pages.gitlab.gnome.org/libadwaita/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

GNOME Tuner aims to be a small, friendly app that helps you tune your instrument
without leaving your desktop. It follows the [GNOME Human Interface Guidelines](https://developer.gnome.org/hig/)
and is written in Python with PyGObject.

> **Status: early development (v0.1).** The app currently shows a window skeleton —
> the fun parts are still to be built. This is a great time to jump in and help shape it!

## Planned features

- [ ] Real-time pitch detection from the microphone
- [ ] Chromatic tuning with cents offset display
- [ ] Presets for common instruments (guitar, bass, ukulele, violin, …)
- [ ] Adjustable reference pitch (A4 = 440 Hz by default)
- [ ] Flatpak packaging and Flathub release

Have an idea? [Open an issue](../../issues) — feature discussions are very welcome.

## Screenshots

*Coming soon — the UI is still hatching.* 🐣

## Running from source

### Requirements

- Python ≥ 3.10
- GTK 4 and libadwaita 1
- PyGObject

On most Linux distributions these are already present on a GNOME desktop.
Otherwise:

```bash
# Fedora
sudo dnf install python3-gobject gtk4 libadwaita

# Debian / Ubuntu
sudo apt install python3-gi gir1.2-gtk-4.0 gir1.2-adw-1

# Arch
sudo pacman -S python-gobject gtk4 libadwaita
```

> **Note:** PyGObject is best installed through your distribution's package
> manager rather than pip, since the pip build requires system development
> headers. The [requirements.txt](requirements.txt) is provided for
> completeness and CI use.

### Run

```bash
git clone https://github.com/AliAkbariAlashti/gnome-tuner.git
cd gnome-tuner
python3 run.py
```

## Project layout

```
gnome-tuner/
├── run.py            # Entry point
├── src/
│   ├── app.py        # Adw.Application subclass
│   └── window.py     # Main application window
├── ui/
│   └── tuner_view.py # Tuner display widget (note, frequency, meter)
├── data/             # Desktop entry, icons, metainfo
└── flatpak/          # Flatpak manifest (planned)
```

## Contributing

Contributions of every kind are welcome — code, design, testing, translations,
and ideas. Please read [CONTRIBUTING.md](CONTRIBUTING.md) to get started, and
note that this project follows the [GNOME Code of Conduct](CODE_OF_CONDUCT.md).

Good first steps:

1. Run the app and poke around the code (it's tiny — by design).
2. Check the [open issues](../../issues) for something that interests you.
3. Say hi in an issue before starting bigger work, so efforts don't collide.

## License

This project is licensed under the [GNU General Public License v3.0 or later](LICENSE).
