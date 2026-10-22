# Lumenfold

Landing site for **Lumenfold**, a fictional creative-collaboration app for film, design, and campaign studios. Teams share one room per show, pin notes to a frame, and stamp a decision before the next cut.

This repository is Plato6. The home page has the pitch, a feature grid, a pricing calculator (seats, plan, and billing), an FAQ, and a waitlist form. The changelog is a second page with a filter.

The painting in `assets/background.jpg` is the background of every page. It is set once on the page root with `background_size="cover"`, `background_position="center"`, and `background_attachment="fixed"`, so it stays put while the page scrolls. Sections sit on semi-transparent panels so the picture shows through.

## Python version

Reflex **0.10.0** supports Python 3.14. Its package metadata requires `>=3.11,<4.0` and lists `Programming Language :: Python :: 3.14`. Support was added in Reflex 0.8.15. This project targets **Python 3.14.4**, which is also the contents of `.python-version`.

## Run it on Ubuntu

You need Python 3.14 available as `python3.14` (3.14.4 is the version this site was built and checked with), plus `curl` and `unzip`. The first `reflex run` downloads Bun and compiles the frontend, so it needs network access and can take a few minutes.

If `python3.14` is not installed yet, install exactly 3.14.4 with [uv](https://docs.astral.sh/uv/):

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
source "$HOME/.local/bin/env"
uv python install 3.14.4
```

`uv` puts `python3.14` on your PATH. If `python3.14 -m venv` then says the venv module is missing, install it with `sudo apt install python3.14-venv` and run the venv command again.

```bash
git clone https://github.com/Gooberin95/Plato6.git
cd Plato6
python3.14 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
reflex init --no-agents
reflex run
```

`reflex init` is optional here. `rxconfig.py` and the `lumenfold` package are already in the repo, so init does not scaffold over this app. `--no-agents` keeps it from writing an extra agent guide. You can skip that line and run `reflex run` directly.

Open [http://localhost:3000](http://localhost:3000). The changelog is at [http://localhost:3000/changelog](http://localhost:3000/changelog). Reflex also starts its backend on port 8000; use the frontend URL above. If port 3000 is already taken, the terminal prints the port it chose. Stop the server with Ctrl+C.

## Fonts

Syne and Outfit are included under `assets/fonts/` and licensed under the SIL Open Font License. See `assets/fonts/Syne-OFL.txt` and `assets/fonts/Outfit-OFL.txt`.
