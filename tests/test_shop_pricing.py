import pytest
import math
from gameplay import shop_pricing as mod

CASES = [
    ("apply", 'm.apply(100, 0.2) == approx(80)'),
    ("stack", 'm.stack([0.2, 0.3]) == approx(0.5)'),
    ("cents", 'm.cents(0.1) == 10'),
    ("half", 'm.half_even(2.5) == 2'),
    ("stock", 'm.in_stock(3, 2) is True'),
    ("lock", 'm.lock("a") == "lock:a"'),
    ("refund", 'm.refund(80) == 80'),
    ("display", 'm.display(90) == 90'),
    ("version", 'm.version(3) == 3'),
    ("audit", 'm.audit("refund") == "refund"'),
    ("active", 'm.active(1, 10, 5) is True'),
    ("clamp", 'm.clamp_nonneg(-1) == 0'),
    ("format", 'm.format_price(1999) == "19.99"'),
    ("key", 'm.key(1) == "s:1"'),
    ("tax", 'm.tax(100, 0.1) == approx(110)')
]

@pytest.mark.parametrize("name,expr", CASES, ids=[c[0] for c in CASES])
def test_contract(name, expr):
    assert eval(expr, {"m": mod, "approx": pytest.approx, "math": math})
