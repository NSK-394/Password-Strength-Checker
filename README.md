# Password Strength Checker

![tests](https://github.com/NSK-394/Password-Strength-Checker/actions/workflows/tests.yml/badge.svg)

Scores a password by **estimated entropy** and flags **weak patterns** that raw entropy misses.

## What it measures
- **Entropy (bits)**: `length × log2(charset size)` — the classic estimate of how large the guessing space is. ~28 bits is weak, ~60+ is strong against offline attacks.
- **Pattern penalties**: entropy alone calls `Password1` strong, but it's trivially guessable. So the checker also flags common passwords, repeated characters, sequential digits (`1234`), keyboard runs (`qwerty`), and word-then-digits (`summer2024`). Any pattern hit forces a **Weak** rating regardless of entropy.

## Usage
```bash
python password_checker.py "7Gx!qL9#vR2@wE5"      # pass directly
python password_checker.py                        # prompt (hidden input)
```
```
Entropy: ~98.0 bits
Strength: Strong
```

## Note on the entropy estimate
`length × log2(charset)` assumes every character is independently random, which real passwords are not — that's exactly why the pattern layer exists. For production use, a library like [zxcvbn](https://github.com/dropbox/zxcvbn) models real-world guessing far better; this project reimplements the core ideas to show how they work.

## Tests
```bash
pip install pytest && pytest -q
```
