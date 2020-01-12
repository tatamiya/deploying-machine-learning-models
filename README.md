# deploying-machine-learning-models
Based on Udemy course 'Deployment of Machine Learning Models' (https://www.udemy.com/course/deployment-of-machine-learning-models/)

# Building and Running the Docker Container
## Build
```
docker build --build-arg PIP_EXTRA_INDEX_URL=$PIP_EXTRA_INDEX_URL -t ml_api:latest .
```

## Run
```
docker run --name ml_api -d -p 8000:5000 --rm ml_api:latest
```