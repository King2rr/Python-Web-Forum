from django.shortcuts import render

from .models import Topic

# Create your views here.
def index(request):
	"""The home page for web forum"""
	return render(request, 'web_forums/index.html')

def topics(request):
	"""Show all topics."""
	topics = Topic.objects.order_by('date_added')
	context = {'topics': topics}
	return render(request, 'web_forums/topics.html', context)

def topic(request, topic_id):
	"""Show single topics and the entries."""
	topic = Topic.objects.get(id=topic_id)
	entries = topic.entry_set.order_by('-date_added')
	context = {'topic': topic, 'entries': entries}
	return render(request, 'web_forums/topic.html', context)

def bars(request):
	"""Show all bars."""
	bars = Topic.objects.order_by('date_added')
	context = {'bars': bars}
	return render(request, 'web_forums/bars.html', context)

def venues(request):
	"""Show all bars."""
	venues = Topic.objects.order_by('date_added')
	context = {'venues': venues}
	return render(request, 'web_forums/venues.html', context)