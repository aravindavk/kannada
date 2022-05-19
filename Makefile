py-docgen:
	python3 python/docgen.py > python/README.md

docgen: py-docgen

test-python:
	pip3 install -e python/
	pytest python/tests/
