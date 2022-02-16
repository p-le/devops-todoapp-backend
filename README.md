# Setup ENVIRONMENT
Install poetry
```
https://python-poetry.org/docs/#installation
```

Install packages
```
poetry install
```

# Using Docker-compose
```
docker-compose up
```
- API URL: http://localhost:8080/
- Examples: http://localhost:8080/api/tasks

# Manual deploy to GCP Artifact Registry (For Demo)

*Required*: Update `IMAGE_TAG` and `GCP_PROJECT_ID`
```
./script/deploy.sh
```