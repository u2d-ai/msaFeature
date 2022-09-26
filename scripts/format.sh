#!/bin/sh -e
set -x

autoflake --remove-all-unused-imports --recursive --in-place msaFeature docs_src --exclude=__init__.py
black msaFeature docs_src
isort msaFeature docs_src
