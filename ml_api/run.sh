#!/usr/bin/env bash
exec uvicorn api.main:app --host 0.0.0.0 --port 5000