"""Lot rounding for 北陸商事 (webhook retest)."""


def round_lot(qty: int, lot_size: int = 10) -> int:
    """Ceil qty to lot size — ISS-12 webhook retest."""
    if lot_size <= 0:
        raise ValueError("lot_size must be positive")
    return ((qty + lot_size - 1) // lot_size) * lot_size


def warehouse_for_seasonal(sku: str) -> str:
    return "SEASONAL"
