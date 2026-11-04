def slug(s: str) -> str:
    """Lowercase words joined by '-'."""
    return "-".join(s.lower().split())


def title_case(s: str) -> str:
    """Capitalize the first letter of each space-separated word, preserving spacing."""
    return " ".join(w[:1].upper() + w[1:] for w in s.split(" "))


def snake_case(s):
    return "_".join(s.lower().split(" "))
