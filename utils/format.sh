#!/usr/bin/env bash
# Run the pre-commit checks right now

set -euo pipefail
cd "$(dirname "$0")/.."

echo "Sorting python imports with isort."
isort .

echo "Auto-formatting python code with black."
black .
