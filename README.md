# bug-example-ddtrace-jsonschema

This repo is supposed to visualize a bug between ddtrace and jsonschema.

Opened issues:

- <https://github.com/DataDog/dd-trace-py/issues/9950>
- <https://github.com/python-jsonschema/jsonschema/issues/1289>

## Requirements

- Python
- Poetry (or any other method of installing and running the pip packages)

## Reproduction steps

1. Install the environment: `poetry install --no-root`
2. Run the test: `poetry run pytest`
3. See this error:

    ```txt
    test_main.py:1: in <module>
        import jsonschema
    <frozen importlib._bootstrap>:991: in _find_and_load
        ???
    <frozen importlib._bootstrap>:975: in _find_and_load_unlocked
        ???
    <frozen importlib._bootstrap>:671: in _load_unlocked
        ???
    .venv/lib/python3.8/site-packages/ddtrace/internal/module.py:220: in _exec_module
        self.loader.exec_module(module)
    .venv/lib/python3.8/site-packages/jsonschema/__init__.py:16: in <module>
        from jsonschema.validators import (
    <frozen importlib._bootstrap>:991: in _find_and_load
        ???
    <frozen importlib._bootstrap>:975: in _find_and_load_unlocked
        ???
    <frozen importlib._bootstrap>:671: in _load_unlocked
        ???
    .venv/lib/python3.8/site-packages/ddtrace/internal/module.py:220: in _exec_module
        self.loader.exec_module(module)
    .venv/lib/python3.8/site-packages/jsonschema/validators.py:603: in <module>
        meta_schema=SPECIFICATIONS.contents(
    .venv/lib/python3.8/site-packages/referencing/_core.py:483: in contents
        return self[uri].contents
    .venv/lib/python3.8/site-packages/referencing/_core.py:333: in __getitem__
        raise exceptions.NoSuchResource(ref=uri) from None
    E   referencing.exceptions.NoSuchResource: 'http://json-schema.org/draft-03/schema#'
    ========================================================================================================== short test summary info ===========================================================================================================
    ERROR test_main.py - referencing.exceptions.NoSuchResource: 'http://json-schema.org/draft-03/schema#'
    ```

4. uninstall ddtrace: `poetry remove ddtrace`
5. run the test: `poetry run pytest`
6. it works ¯\_(ツ)_/¯
