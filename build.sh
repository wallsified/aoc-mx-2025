wget -qO- https://astral.sh/uv/install.sh | sh
uv init
uv add reflex==0.8.20
source .venv/bin/activate
reflex init
reflex export
unzip frontend.zip -d public
rm -f frontend.zip
deactivate