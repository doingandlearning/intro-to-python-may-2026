def tip_amount(subtotal, tip_percent):
    return subtotal * (tip_percent / 100)

def amounts_above(amounts, threshold):
    out = []
    for amount in amounts:
        if amount > threshold:
            out.append(amount)
    return out

def summarise_checks(amounts, tip_percent):
    n = len(amounts)
    sum_sub = 0.0
    sum_tip = 0.0
    sum_total = 0.0
    for sub in amounts:
        tip = tip_amount(sub, tip_percent)
        sum_sub += sub
        sum_tip += tip
        sum_total += sub + tip
    print(f"Cheques: {n}")
    print(f"Average subtotal: {sum_sub / n:.2f}")
    print(f"Average tip: {sum_tip / n:.2f}")
    print(f"Average total (with tip): {sum_total / n:.2f}")

check_amounts = [
    45.00,
    32.50,
    78.20,
    19.99,
    54.00,
    120.00,
    28.75,
    63.40,
    15.00,
    41.10,
]

summarise_checks(check_amounts, 18)