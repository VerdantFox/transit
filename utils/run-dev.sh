#!/usr/bin/env bash

set -euo pipefail
cd "$(dirname "$0")/.."

# python main.py
flask --app main.py --debug run
