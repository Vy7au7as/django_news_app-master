from django.shortcuts import render
import requests
import json


def home(request):
    query = request.GET.get('q')
    suggestions = []

    if query:
        params = {
            'client': 'firefox',
            'q': query,
            'h1': 'en',
        }
        url = f'http://suggestqueries.google.com/complete/search?hl=en&ds=yt&client=youtube&hjson=t&cp=1&q={query}&format=5&alt'
        resp = requests.get(url, params=params)
        result = resp.json()[1]
        suggestions = result
        all_results = [result]

        suggestion_letters = [f'{query} a', f'{query} b', f'{query} c', f'{query} d', f'{query} e', f'{query} g', f'{query} h',
                       f'{query} i', f'{query} j', f'{query} k', f'{query} m', f'{query} n', f'{query} o', f'{query} p',
                       f'{query} q', f'{query} r', f'{query} s', f'{query} t', f'{query} u', f'{query} v', f'{query} w',
                       f'{query} x', f'{query} y', f'{query} z', f'{query} 1', f'{query} 2', f'{query} 3', f'{query} 4',
                       f'{query} 5', f'{query} 6', f'{query} 7', f'{query} 8', f'{query} 9', f'{query} 0']

        for letter in suggestion_letters:
            params['q'] = f'{query} {letter}'
            url = f'http://suggestqueries.google.com/complete/search?hl=en&ds=yt&client=youtube&hjson=t&cp=1&q={params["q"]}&format=5&alt'
            resp = requests.get(url, params=params)
            result = resp.json()[1]

            suggestions += result
            all_results.append(result)

    context = {
        'query': query,
        'suggestions': suggestions

    }
    return render(request, 'youtube.html', context)
