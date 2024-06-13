# Welcome to NumbersView and Top Products Web Application

## NumbersView

### Description

NumbersView is a Django project that fetches numbers from various test servers, maintains a window of the last 10 fetched numbers for each type, and calculates the average of the numbers in the window.

### Setup Instructions

1. Ensure Django is installed:

   ```bash
   pip install django

Clone the project repository from GitHub Repository Link or download the project zip file.

Start the Django development server by running:

python manage.py runserver
Visit http://localhost:9876/numbers/<numberid>/ in your web browser, replacing <numberid> with the type of numbers you want to fetch (p, f, e, or r).

Usage:

Navigate to the appropriate URL endpoint (http://localhost:9876/numbers/<numberid>/) to fetch numbers of the specified type.
The response will include the fetched numbers, the previous state of the window, the current state of the window, and the average of the numbers in the window.
Ensure that the response time does not exceed 500 milliseconds.

![even_number](https://github.com/2100030888-praveen/2100030888/assets/110281775/cb0bc421-f507-4eb2-823c-e4363db145e8)
![fibo](https://github.com/2100030888-praveen/2100030888/assets/110281775/00233db3-3227-4170-ab58-2850219df9b0)
![prime](https://github.com/2100030888-praveen/2100030888/assets/110281775/c043968c-84a6-4ea8-a1c8-c714e9012950)
![random number](https://github.com/2100030888-praveen/2100030888/assets/110281775/1927b234-096e-462b-a77f-822b231ddd0a)


# Django Project - Project 2

## Description

This Django project serves as a web application for fetching and displaying top products from an external API based on company and category. This README specifically covers the structure and usage of the second part of the project, where the code has been modularized into separate components.

## Project Structure

The project is structured into several modules for better organization and maintainability:

- **api_client.py**: This module contains functions to communicate with the external API and fetch products.
- **product_handler.py**: This module handles the processing and pagination of products obtained from the API.
- **views.py**: This module contains Django view functions to serve the web requests and return JSON responses.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/2100030888-praveen/2100030888
Navigate to the project directory:


cd django_project_project_2

Set up the necessary configurations, including BEARER_TOKEN in confi.py.

Usage
To use the project, follow these steps:

Run the Django development server:

python manage.py runserver
Access the application in your web browser at http://localhost:9876/.

Use the provided API endpoints to fetch top products based on company and category. Example:

http://127.0.0.1:9876/companies/AMZ/categories/Laptop/products?top=10&minPrice=1&maxPrice=10000
Parameters:

n: Number of products to fetch (default: 10).
page: Page number for pagination (default: 1).
minPrice: Minimum price filter (default: 0).
maxPrice: Maximum price filter (default: 1000000).
sortBy: Sorting parameter (default: 'price').
order: Sorting order ('asc' or 'desc', default: 'asc').
Example request:
http://127.0.0.1:9876/companies/AMZ/categories/Laptop/products?top=10&minPrice=1&maxPrice=10000

![price](https://github.com/2100030888-praveen/2100030888/assets/110281775/a63cdf0d-dd42-433d-a643-89e7f21f2843)
![price1](https://github.com/2100030888-praveen/2100030888/assets/110281775/9b5d6dcc-f5b5-4d82-aee9-c3371cd67413)
![web_price](https://github.com/2100030888-praveen/2100030888/assets/110281775/290c2c1f-bfa5-4e15-a73a-ae7a456814ad)

