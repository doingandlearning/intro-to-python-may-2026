def amounts_above(amounts, threshold):
    out = []
    for amount in amounts:
        if amount > threshold:
            out.append(amount)
    return out

def amounts_above(amounts, threshold):
  # Pythonic Approach (idiomatic python)
  return [amount for amount in amounts if amount > threshold]

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

high_check_amounts = []

for check in check_amounts:
  if check > 60:
    high_check_amounts.append(round(check*100))

print(high_check_amounts)

list_comp_high_check_amounts = [round(c * 100) for c in check_amounts if c > 60]
print(list_comp_high_check_amounts)