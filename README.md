Activate a virtualenv then run:

```
pip install -r requirements.txt
```

To build an example .pex file run:

```
pex . -r <(pip freeze) -e pexExample.main:main -o dist/example.pex
```
