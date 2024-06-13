
def process_products(products, companyname, categoryname, page=1, n=10, sort_by='price', order='asc'):
    if not products:
        return None

    for product in products:
        product['company'] = companyname
        product['category'] = categoryname

    reverse_order = order == 'desc'
    products = sorted(products, key=lambda x: x.get(sort_by, 0), reverse=reverse_order)

    start_index = (page - 1) * n
    end_index = start_index + n
    paginated_products = products[start_index:end_index]

    return {
        'total_products': len(products),
        'total_pages': (len(products) + n - 1) // n,
        'current_page': page,
        'products': paginated_products
    }
