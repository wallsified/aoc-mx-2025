python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install reflex=0.8.20
rm -rf public
reflex init
reflex export
unzip frontend.zip -d public
rm -f frontend.zip
deactivate