def slug(s: str) -> str:
    """Lowercase words joined by '-'."""
    return "-".join(s.lower().split())


def title_case(s):
    return " ".join(w[0].upper() + w[1:] for w in s.split(" "))
