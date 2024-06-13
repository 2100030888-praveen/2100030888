import requests
from django.http import JsonResponse
from django.views import View
from .config import TEST_SERVER_URLS, BEARER_TOKEN, windows

class NumbersView(View):

    def get(self, request, numberid):
        if numberid not in TEST_SERVER_URLS:
            return JsonResponse({'error': 'Invalid'}, status=400)
        url = TEST_SERVER_URLS[numberid]
        try:
            headers = {
                'Authorization': f'Bearer {BEARER_TOKEN}'
            }
            response = requests.get(url, headers=headers, timeout=0.5)
            response.raise_for_status()
            fetched_numbers = response.json().get('numbers', [])
        except requests.RequestException as e:
            return JsonResponse({'error': 'Failed to fetch'}, status=500)

        prev_window_state = list(windows[numberid])
        for num in fetched_numbers:
            if num not in windows[numberid]:
                windows[numberid].append(num)

        curr_window_state = list(windows[numberid])
        avg = sum(curr_window_state) / len(curr_window_state) if curr_window_state else 0

        response_data = {
            "numbers": fetched_numbers,
            "windowPrevState": prev_window_state,
            "windowCurrState": curr_window_state,
            "avg": avg
        }
        return JsonResponse(response_data)
