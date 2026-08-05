"""北陸商事 — 季節ロット振替（デモ用。改修ポインタ対象）."""

from __future__ import annotations


WAREHOUSE_STANDARD = "MAIN"
WAREHOUSE_SEASONAL = "SEASONAL"


def is_seasonal_sku(sku: str) -> bool:
    """季節限定 SKU かどうか（北陸カスタム判定）."""
    return sku.upper().startswith("SEA-")


def transfer_seasonal_lot(sku: str, qty: int) -> dict:
    """
    季節限定ロットを別倉庫へ振替する。

    標準 OrderHub に無いルール。UC1 カスタム / UC23 影響確認の対象。
    """
    if qty <= 0:
        return {"ok": False, "error": "invalid_qty"}
    dest = WAREHOUSE_SEASONAL if is_seasonal_sku(sku) else WAREHOUSE_STANDARD
    return {
        "sku": sku,
        "qty": qty,
        "warehouse": dest,
        "custom": True,
        "partner": "hokuriku",
    }


def round_lot_qty(qty: float) -> int:
    """ロット数量の切上げ（設定変更候補。標準丸めマスタと突合）."""
    import math

    return int(math.ceil(qty))
