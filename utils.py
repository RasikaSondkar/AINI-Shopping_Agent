def detect_product(text):
    text = text.lower()

    products = ["laptop", "smartphone", "headphones", "smartwatch"]

    for product in products:
        if product in text or product + "s" in text:
            return product

    return None