#!/usr/bin/env bash

find . -name migrations -exec rm -rf '{}' \;
find . -name __pycache__ -exec rm -rf '{}' \;
find . -name *.pyc -exec rm -rf '{}' \;