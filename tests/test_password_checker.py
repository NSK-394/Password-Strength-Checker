from password_checker import entropy_bits, find_patterns, rate


def test_entropy_grows_with_length_and_charset():
    assert entropy_bits("aaaa") < entropy_bits("aA1!aA1!")


def test_common_password_is_weak():
    r = rate("password")
    assert r["strength"] == "Weak"
    assert any("common" in p.lower() for p in r["patterns"])


def test_sequential_and_repeat_detected():
    assert any("Sequential" in p for p in find_patterns("abc1234"))
    assert any("repeated" in p.lower() for p in find_patterns("aaabbb"))


def test_long_random_is_strong():
    assert rate("7Gx!qL9#vR2@wE5^nT8&")["strength"] == "Strong"
