"""Password strength checker with entropy estimation and pattern detection."""

from __future__ import annotations

import argparse
import math
import re

COMMON = {"password", "123456", "123456789", "qwerty", "111111", "iloveyou", "admin", "letmein", "welcome"}


def charset_size(password: str) -> int:
    size = 0
    if re.search(r"[a-z]", password):
        size += 26
    if re.search(r"[A-Z]", password):
        size += 26
    if re.search(r"\d", password):
        size += 10
    if re.search(r"[^a-zA-Z0-9]", password):
        size += 32  # rough printable-symbol pool
    return size


def entropy_bits(password: str) -> float:
    """Shannon entropy estimate: length * log2(charset size)."""
    pool = charset_size(password)
    return round(len(password) * math.log2(pool), 1) if pool else 0.0


def find_patterns(password: str) -> list[str]:
    issues: list[str] = []
    low = password.lower()
    if low in COMMON:
        issues.append("Exact match for a very common password")
    if re.search(r"(.)\1\1", password):
        issues.append("Three or more repeated characters in a row")
    if re.search(r"(?:0123|1234|2345|3456|4567|5678|6789)", password):
        issues.append("Sequential digits")
    if re.search(r"(?:abcd|bcde|cdef|qwer|asdf|zxcv)", low):
        issues.append("Keyboard/alphabet sequence")
    if re.fullmatch(r"[A-Za-z]+\d{1,4}", password):
        issues.append("Word-then-digits pattern (easy to guess)")
    return issues


def rate(password: str) -> dict:
    bits = entropy_bits(password)
    patterns = find_patterns(password)
    if patterns or bits < 28:
        strength = "Weak"
    elif bits < 60:
        strength = "Medium"
    else:
        strength = "Strong"
    return {"entropy_bits": bits, "strength": strength, "patterns": patterns}


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Password strength checker (entropy + patterns)")
    ap.add_argument("password", nargs="?", help="password to check (prompted if omitted)")
    args = ap.parse_args(argv)
    import getpass
    pw = args.password or getpass.getpass("Password: ")

    r = rate(pw)
    print(f"Entropy: ~{r['entropy_bits']} bits")
    print(f"Strength: {r['strength']}")
    for p in r["patterns"]:
        print(f"  ! {p}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
