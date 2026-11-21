import math

def apply(base, discount):
    """折扣计算。"""
    raise NotImplementedError("TODO: apply")

def stack(discounts):
    """叠加上限。"""
    raise NotImplementedError("TODO: stack")

def cents(amount):
    """整数分。"""
    raise NotImplementedError("TODO: cents")

def half_even(value):
    """统一舍入。"""
    raise NotImplementedError("TODO: half_even")

def in_stock(stock, qty):
    """库存事务。"""
    raise NotImplementedError("TODO: in_stock")

def lock(key):
    """服务端锁。"""
    raise NotImplementedError("TODO: lock")

def refund(paid):
    """按成交价退款。"""
    raise NotImplementedError("TODO: refund")

def display(price):
    """同一计算源。"""
    raise NotImplementedError("TODO: display")

def version(value):
    """区域表版本。"""
    raise NotImplementedError("TODO: version")

def audit(action):
    """审计日志。"""
    raise NotImplementedError("TODO: audit")

def active(start, end, now):
    """折扣有效期。"""
    raise NotImplementedError("TODO: active")

def clamp_nonneg(value):
    """非负钳制。"""
    raise NotImplementedError("TODO: clamp_nonneg")

def format_price(cents):
    """价格格式。"""
    raise NotImplementedError("TODO: format_price")

def key(sku):
    """商品键。"""
    raise NotImplementedError("TODO: key")

def tax(price, rate):
    """税价。"""
    raise NotImplementedError("TODO: tax")
