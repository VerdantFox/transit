#!/usr/bin/env bash

set -euo pipefail
cd "$(dirname "$0")/.."

files="${1:-}"

if [[ -z "$files" ]]
then
files=app/templates
fi

jinja-ninja "$files"
