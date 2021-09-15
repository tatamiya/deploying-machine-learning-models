lint:
	black --check .
	flake8 --exit-zero --count --max-line-length=88 --show-source --statistics ./**/*.py
	isort --check-only --profile black .
	mypy --ignore-missing-imports --namespace-packages --explicit-package-bases .

format:
	black .
	isort --profile black .