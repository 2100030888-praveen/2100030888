from collections import deque

TEST_SERVER_URLS = {
    'p': 'http://20.244.56.144/test/primes',
    'f': 'http://20.244.56.144/test/fibo',
    'e': 'http://20.244.56.144/test/even',
    'r': 'http://20.244.56.144/test/rand',
}

BEARER_TOKEN='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJNYXBDbGFpbXMiOnsiZXhwIjoxNzE4MjYzMTQ2LCJpYXQiOjE3MTgyNjI4NDYsImlzcyI6IkFmZm9yZG1lZCIsImp0aSI6IjA5NmJjOWEwLWIzZTEtNDg2ZC1iZjY0LTFmNzJhNWE3ZTNjNCIsInN1YiI6Im1hbWRpZGlwcmF2ZWVuMjc4NEBnbWFpbC5jb20ifSwiY29tcGFueU5hbWUiOiJLTCBVTklWRVJTSVRZIiwiY2xpZW50SUQiOiIwOTZiYzlhMC1iM2UxLTQ4NmQtYmY2NC0xZjcyYTVhN2UzYzQiLCJjbGllbnRTZWNyZXQiOiJJcG10aE1Tc0dFVUNKdW5XIiwib3duZXJOYW1lIjoiTUFNSURJIE5BVkVFTiBEVVJHQSBQUkFWRUVOIiwib3duZXJFbWFpbCI6Im1hbWRpZGlwcmF2ZWVuMjc4NEBnbWFpbC5jb20iLCJyb2xsTm8iOiIyMTAwMDMwODg4In0.9-uieyR_1LMRtzJ5OF019smBIZJwdrbdtZguL21yFzk'


windows = {
    'p': deque(maxlen=10),
    'f': deque(maxlen=10),
    'e': deque(maxlen=10),
    'r': deque(maxlen=10)
}