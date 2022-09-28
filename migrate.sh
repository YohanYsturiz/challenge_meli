#!/usr/bin/env bash

# Run migrate
echo "Running migrate..."
yoyo apply --database="${CHALLANGE_DB}" ./migrations
