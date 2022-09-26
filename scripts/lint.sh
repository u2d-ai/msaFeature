#!/usr/bin/env bash

set -e
set -x

mypy msaFeature
flake8 msaFeature docs_src
black msaFeature docs_src --check
isort msaFeature docs_src scripts --check-only

