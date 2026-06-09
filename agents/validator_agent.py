import sqlglot


FORBIDDEN_KEYWORDS = {
    "DROP",
    "DELETE",
    "TRUNCATE",
    "ALTER",
    "UPDATE",
    "INSERT"
}


def validate_query(query: str):

    try:

        parsed = sqlglot.parse_one(query)

        upper_query = query.upper()

        for keyword in FORBIDDEN_KEYWORDS:

            if keyword in upper_query:

                return {
                    "valid": False,
                    "reason": f"Forbidden keyword detected: {keyword}"
                }

        if not upper_query.strip().startswith(
            ("SELECT", "WITH")
        ):

            return {
                "valid": False,
                "reason": "Only SELECT queries are allowed"
            }

        return {
            "valid": True,
            "reason": "Query is valid"
        }

    except Exception as e:

        return {
            "valid": False,
            "reason": str(e)
        }