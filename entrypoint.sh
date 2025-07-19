#!/usr/bin/env bash
set -e

# Copy the environment variables to .env for posting
printenv | grep DEVICE > .env

exec "$@"