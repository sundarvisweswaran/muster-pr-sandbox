def slug(s: str) -> str:
    """Lowercase words joined by '-'."""
    return "-".join(s.lower().split())
