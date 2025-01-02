from django.shortcuts import render
import random

# Predefined list of quotes
quotes = [
    "The only limit to our realization of tomorrow is our doubts of today. - Franklin D. Roosevelt",
    "In the middle of every difficulty lies opportunity. - Albert Einstein",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
    "Do not wait to strike till the iron is hot; but make it hot by striking. - William Butler Yeats",
    "Life is 10% what happens to us and 90% how we react to it. - Charles R. Swindoll",
]

def random_quote_view(request):
    quote = random.choice(quotes)
    return render(request, 'random_quote.html', {'quote': quote})
