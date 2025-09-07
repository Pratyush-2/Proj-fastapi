
import requests

def search_food_by_name(food_name: str):
    """
    Searches for a food by name using the Open Food Facts API and sorts the results
    to place exact matches at the top.
    """
    url = f"https://world.openfoodfacts.org/cgi/search.pl"
    params = {
        "search_terms": food_name,
        "search_simple": 1,
        "action": "process",
        "json": 1,
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        products = data.get("products", [])
        
        exact_matches = []
        other_results = []
        
        for product in products:
            product_name = product.get("product_name", "").lower()
            serving_size = product.get("serving_size", "100g") # Default to 100g
            product["serving_size"] = serving_size

            if product_name == food_name.lower():
                exact_matches.append(product)
            else:
                other_results.append(product)
        
        data["products"] = exact_matches + other_results
        return data
    return None
