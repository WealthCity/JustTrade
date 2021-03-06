from django.shortcuts import render
from django.http import HttpResponse
from tasks.models import tradingTask

from scripts.quote import Quote

def landing_view(request):
	return render(request, 'landing.html')


def index_view(request):
	tasks = tradingTask.objects.all()
	return render(request, 'index.html', {'tasks': tasks})


def index_quote_api(request):
	# symbol, time interval in seconds, day
	nasdaq = Quote('IXIC', 300, 1).to_json()
	# sp500 = quote.GoogleIntradayQuote('IXIC', 300, 1)
	return HttpResponse(nasdaq, content_type='application/json')
