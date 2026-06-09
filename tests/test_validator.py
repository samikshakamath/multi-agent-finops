from agents.validator_agent import validate_query


def test_valid_select():

    result = validate_query(
        "SELECT * FROM sales"
    )

    assert result["valid"] is True


def test_drop_table():

    result = validate_query(
        "DROP TABLE sales"
    )

    assert result["valid"] is False


def test_delete_statement():

    result = validate_query(
        "DELETE FROM sales"
    )

    assert result["valid"] is False