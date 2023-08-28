from typing import Tuple


def get_authorization_scheme_param(
    authorization_header_data: str | None = None,
) -> Tuple[str, str]:
    if not authorization_header_data:
        return "", ""
    scheme, _, param = authorization_header_data.partition(" ")
    return scheme, param
