#! /usr/bin/env bash

python setup.py bdist_wheel
twine upload -r pypitest dist/*
