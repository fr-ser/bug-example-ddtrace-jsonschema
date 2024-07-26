import jsonschema


def test_error() -> None:
    jsonschema.exceptions.ValidationError(
        message="",
        path=[],
        validator="",
        validator_value="",
    )
