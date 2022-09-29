#!/usr/bin/env bash

# Run migrate
echo "Running migrate..."
yoyo apply --database="postgresql://postgres:postgres@localhost:5436/challengedb" ./migrations --batch
