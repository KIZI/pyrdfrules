#!/bin/bash

echo "Installing dependencies"

pip install hatch
pip install coverage==7.6.10

echo "Running tests"

hatch run coverage run -m unittest discover -s src/tests