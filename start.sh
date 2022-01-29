#!/bin/bash
CURRENT_DIR=$(pwd)
export GOOGLE_APPLICATION_CREDENTIALS="${CURRENT_DIR}/service_account.json"
poetry run uvicorn fastapi_todoapp.main:app --reload --host 0.0.0.0