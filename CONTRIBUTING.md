# Contributing to GNOME Tuner

Thanks for your interest in contributing! This project is young and small,
which makes it a perfect place for first-time contributors.

## Getting set up

1. Fork the repository and clone your fork:

   ```bash
   git clone https://github.com/<your-username>/gnome-tuner.git
   cd gnome-tuner
   ```

2. Make sure GTK4, libadwaita, and PyGObject are installed
   (see the [README](README.md#requirements)).

3. Run the app:

   ```bash
   python3 run.py
   ```

## Making changes

- Create a branch for your work: `git checkout -b my-feature`.
- Keep changes focused — one topic per pull request.
- Follow the existing code style (PEP 8, clear names, minimal cleverness).
- UI work should follow the [GNOME Human Interface Guidelines](https://developer.gnome.org/hig/).

## Commit messages

Use short, descriptive commit messages in the imperative mood, optionally
with a [Conventional Commits](https://www.conventionalcommits.org/) prefix:

```
feat: add chromatic tuning mode
fix: handle missing microphone gracefully
docs: expand installation instructions
```

## Submitting a pull request

1. Push your branch to your fork.
2. Open a pull request against `main`.
3. Describe **what** the change does and **why**.
4. Link any related issues (e.g. `Closes #12`).

## Reporting bugs and requesting features

Open an [issue](../../issues) using the provided templates. For bugs, please
include your distribution, GNOME/GTK version, and steps to reproduce.

## Code of conduct

By participating in this project you agree to uphold the
[GNOME Code of Conduct](CODE_OF_CONDUCT.md). Be kind — this is a fun project.
