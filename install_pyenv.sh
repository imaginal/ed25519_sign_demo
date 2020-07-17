#!/bin/sh
python3 -m venv venv
. venv/bin/activate
pip install --upgrade pip wheel setuptools
pip install ed25519
bash -i
