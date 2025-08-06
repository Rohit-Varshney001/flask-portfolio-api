conversion_rates = {
    'IN': 1,
    'US': 0.012,
    'FR': 0.011,
    'ES': 0.011,
}

def convert_price(base_price, country_code):
    rate = conversion_rates.get(country_code.upper(), 1)
    return round(base_price * rate, 2)
