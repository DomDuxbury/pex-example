all: dev_requirements test build

dev_requirements:
	tail -n +4 requirements.txt > prod_requirements.txt

test:
	pytest

build:
	pex . -r prod_requirements.txt -e pexExample.main:main -o dist/example.pex
