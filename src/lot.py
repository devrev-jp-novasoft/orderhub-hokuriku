"""北陸商事 — 季節ロット振替（デモ用スタブ）."""


def transfer_seasonal_lot(sku: str, qty: int) -> dict:
    return {"sku": sku, "qty": qty, "warehouse": "SEASONAL", "custom": True}
