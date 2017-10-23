REQ = $(shell pip freeze)

all: test build

test:
	pytest

build:
	pex . -r requirements.txt -e pexExample.main:main -o dist/example.pex
