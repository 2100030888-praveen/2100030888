# views.py

from django.http import JsonResponse
from .api_client import fetch_products
from .handler import process_products


def get_top_products(request, companyname, categoryname):
    n = int(request.GET.get('n', 10))
    page = int(request.GET.get('page', 1))
    min_price = request.GET.get('minPrice', 0)
    max_price = request.GET.get('maxPrice', 1000000)
    sort_by = request.GET.get('sortBy', 'price')
    order = request.GET.get('order', 'asc')

    products = fetch_products(companyname, categoryname, n, min_price, max_price)
    if products:
        response_data = process_products(products, companyname, categoryname, page, n, sort_by, order)
        if response_data:
            return JsonResponse(response_data)

    return JsonResponse({'error': 'Failed to fetch products'}, status=500)
