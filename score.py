def calculate_best_site(results):
    best_site = None
    best_score = float("-inf")

    for site, data in results.items():
        score = (
            (data["rating"] * 2) +         # rating weight
            (data["reviews"] / 5000) -     # trust factor
            (data["price"] / 50000)        # price penalty
        )

        if score > best_score:
            best_score = score
            best_site = site

    return best_site
