

test:
	@py.test

coverage:
	@py.test --cov=async_signal tests/

requirements:
	@pip install -r requirements.txt

clean:
	@find . -name '*.pyc' -exec rm -f {} \;
	@find . -name '.coverage' -exec rm -f {} \;
	@find . -name 'Thumbs.db' -exec rm -f {} \;
	@find . -name '*~' -exec rm -f {} \;
	@find . -name '__pycache__' -exec rm -fr {} +
	@find . -name '.cache' -exec rm -fr {} +
