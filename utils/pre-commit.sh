#!/usr/bin/env bash
# pre-commit: wrapper to run pre-commit against all (staged) files
# Note that `pre-commit run --all-files` won't run against unstaged files
# To run against those files, first stage the files
# or run `pre-commit run --files FILENAME1 FILENAME2 ETC`

set -euo pipefail
cd "$(dirname "$0")/.."

pre-commit install
pre-commit run --all-files
