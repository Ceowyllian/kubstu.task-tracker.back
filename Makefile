v=${KUBSTU_FILEBOX_VENV_PATH}\Scripts\activate

venv:
	$(v)

freeze-requirements: venv
	pipenv requirements > src\requirements.txt \
 	&& pipenv requirements > src\requirements-dev.txt --dev-only

 black: venv
	black .

isort: venv
	isort .

flake8: venv
	flake8 .

format: black isort

migrations: venv
	python src\manage.py makemigrations

migrate: venv
	python src\manage.py migrate

version: venv
	git rebase dev master \
	&& semantic-release version --vcs-release --no-push \
	&& git rebase master dev && git push --all
