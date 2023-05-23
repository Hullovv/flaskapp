#!/bin/sh
set -e
cd /app
pip3 freeze > requirements.txt
exec "$@"