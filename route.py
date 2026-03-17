def route_query(text):

    text = text.lower()

    if "laptop" in text or "smartphone" in text or "headphones" in text or "smartwatch" in text:
        return "PRODUCT"

    return "AI"