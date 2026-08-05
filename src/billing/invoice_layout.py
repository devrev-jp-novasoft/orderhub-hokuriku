"""北陸商事 — 請求書レイアウト拡張（部署コード列）.

インボイス記載項目変更時は本モジュールも影響確認対象（UC23）。
"""

from __future__ import annotations

from typing import Any


STANDARD_COLUMNS = ("invoice_no", "buyer_name", "tax_id", "amount", "tax")
# 適格請求書の備考列（制度改正デモ: 記載項目追加フック）
OPTIONAL_COLUMNS = ("remarks",)


def invoice_columns(*, include_dept_code: bool = True, include_remarks: bool = False) -> tuple[str, ...]:
    """請求書列。北陸は部署コード列を追加（標準外カスタム）."""
    cols = list(STANDARD_COLUMNS)
    if include_dept_code:
        cols.append("dept_code")
    if include_remarks:
        cols.extend(OPTIONAL_COLUMNS)
    return tuple(cols)


def render_invoice_row(payload: dict[str, Any]) -> dict[str, Any]:
    """適格請求書行を組み立てる。dept_code 欠落時は空文字."""
    row = {col: payload.get(col, "") for col in invoice_columns()}
    # インボイス必須項目の簡易チェック（制度改正デモ用フック）
    row["invoice_ready"] = bool(row.get("tax_id") and row.get("amount") != "")
    return row

# ISS-17 invoice layout 20260805T090819Z
