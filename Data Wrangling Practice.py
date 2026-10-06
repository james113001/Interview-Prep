from decimal import Decimal, InvalidOperation

#time, symbol, price, volume input

def minute_bars(records):
    # 1. Parse and filter bad rows
    trades = []
    for rec in records:
        parts = rec.split(",")
        if len(parts) != 4:
            continue
        ts, symbol, price, qty = (p.strip() for p in parts)
        if not ts or not symbol:
            continue
        try:
            price = Decimal(price)
            vol = int(qty)
        except (InvalidOperation, ValueError):
            continue
        trades.append((ts, symbol, price, vol))

    # 2. Sort by time (ISO strings sort chronologically)
    trades.sort(key=lambda t: t[0])

    # 3. Build bars keyed by (symbol, minute)
    bars = {}
    for ts, symbol, price, vol in trades:
        key = (symbol, ts[:16])
        if key not in bars:
            bars[key] = {"open": price, "high": price,
                         "low": price, "close": price, "vol": vol}
        bar = bars[key]
        else:
            bar["high"] = max(bar["high"], price)
            bar["low"] = min(bar["low"], price)
            bar["close"] = price
            bar["vol"] += vol

    # 4. Sorted by symbol, then minute
    return [(s, m, b) for (s, m), b in sorted(bars.items())]


# Quick tests
data = [
    "2026-10-01T09:30:00.120,AAPL,187.50,100",
    "2026-10-01T09:30:14.900,MSFT,412.10,50",
    "2026-10-01T09:30:45.300,AAPL,187.80,200",
    "2026-10-01T09:31:02.050,AAPL,187.40,150",
    "2026-10-01T09:30:59.999,MSFT,412.00,25",
    "garbage,row",
]
out = minute_bars(data)
assert len(out) == 3
assert out[0][2]["vol"] == 300
assert out[2][2]["close"] == Decimal("412.00")  # out-of-order case
assert out[2][2]["vol"] == 75
assert minute_bars([]) == []
print("all tests pass")
