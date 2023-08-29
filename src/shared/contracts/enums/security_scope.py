from enum import Enum


class SecurityScope(str, Enum):
    SINGLE = "SINGLE"
    MULTI = "MULTI"
