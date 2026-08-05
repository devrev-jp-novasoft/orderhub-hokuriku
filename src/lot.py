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


def round_lot_qty(qty: float, *, mode: str = "ceil") -> int:
    """ロット数量の丸め（設定変更候補。標準丸めマスタと突合）.

    mode: ceil（既定・北陸）| floor | round_half_up
    """
    import math

    if mode == "floor":
        return int(math.floor(qty))
    if mode == "round_half_up":
        return int(math.floor(qty + 0.5))
    return int(math.ceil(qty))

# TOWARDS_RETEST: ensure /towards creates C-CODECHANGE

# POST_REINSTALL_MERGE 20260805T064045Z

# WEBHOOK_VERIFY 20260805T065058Z
