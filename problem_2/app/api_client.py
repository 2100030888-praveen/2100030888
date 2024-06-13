
import requests
from .confi import BEARER_TOKEN

def fetch_products(companyname, categoryname, n=10, min_price=0, max_price=1000000):
    url = f'http://20.244.56.144/test/companies/{companyname}/categories/{categoryname}/products'
    params = {
        'top': n,
        'minPrice': min_price,
        'maxPrice': max_price
    }

    headers = {
        'Authorization': f'Bearer {BEARER_TOKEN}',
    }

    response = requests.get(url, params=params, headers=headers)
    return response.json() if response.status_code == 200 else None
