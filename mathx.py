def clamp(x: float, lo: float, hi: float) -> float:
    """Return x limited to the closed range [lo, hi]; raise ValueError if lo > hi."""
    if lo > hi:
        raise ValueError(f"lo ({lo}) must be <= hi ({hi})")
    return max(lo, min(x, hi))
