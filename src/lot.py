"""Lot rounding for 北陸商事 (demo stub)."""


def round_lot(qty: int, lot_size: int = 10) -> int:
    """Round quantity up to the nearest lot size.

    Demo: ISS-12 invoice/lot impact — seasonal lot warehouse transfer.
    """
    if lot_size <= 0:
        raise ValueError("lot_size must be positive")
    # ceil to lot
    return ((qty + lot_size - 1) // lot_size) * lot_size
