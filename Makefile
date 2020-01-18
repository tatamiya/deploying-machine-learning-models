NAME=udemy-ml-api
COMMIT_ID=$(shell git rev-parse HEAD)

build-ml-api-aws:
		docker build --build-arg PIP_EXTRA_INDEX_URL=${PIP_EXTRA_INDEX_URL} -t $(NAME):$(COMMIT_ID) .

push-ml-api-aws:
		docker push $(AWS_ACCOUNT_ID).dkr.ecr.ap-northeast-1.amazonaws.com/$(NAME):$(COMMIT_ID)

tag-ml-api:
		docker tag $(NAME):$(COMMIT_ID) $(AWS_ACCOUNT_ID).dkr.ecr.ap-northeast-1.amazonaws/$(NAME):$(COMMIT_ID)