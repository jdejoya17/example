This is just and example of how we can develop an OpenAPI specification using
separate files and then utilize some tooling to merge individual YAML files
into a valid OpenAPI specification file.

Run the following to show utilities
```
make help
```

Quick Start
(1) use a virtual environment
```
python -m venv .venv
source .venv/bin/activate
```

(2) install openapi-generator-cli
```
make generate-server-stub
```

(3) run openapi server
```
make run
```

Tools Used:
- [openapi-merge-cli](https://www.npmjs.com/package/openapi-merge-cli)
- [openapi-generator-cli](https://pypi.org/project/openapi-generator-cli/)
