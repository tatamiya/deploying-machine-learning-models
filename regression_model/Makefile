lint:
	poetry run black --check regression_model/
	poetry run flake8 --exit-zero --count --max-line-length=88 --show-source --statistics regression_model/
	poetry run isort --check-only --profile black regression_model/
	poetry run mypy --ignore-missing-imports regression_model/

format:
	poetry run black regression_model/
	poetry run isort --profile black regression_model/