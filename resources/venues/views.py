from django.db.models import Model
from django.shortcuts import render, get_object_or_404
from dayplanner.services import yelp_client
import requests, json, os
from dayplanner.settings import YELP_API
from .models import Venue

# Create your views here.
Sampe_ID =  "WavvLdfdP6g8aZTtbBQHTw"

def index(request):
    return render(request, 'venues/_index.html', {
        'venues': Venue.objects.all()
    })

def detail(request, venue_id):
    venue = get_object_or_404(Venue, pk=venue_id)
    context = {
        'venue': venue,
        'raw_yelp_data': venue.raw_yelp_data()
    }
    return render(request, 'venues/_detail.html', context)

def search_view(request):

    if request.method == 'GET':
        return render(request, 'venues/_search.html')
    elif request.method =='POST':
        context = {}
        user_input = request.POST['user_input']
        bussiness_data = yelp_client.search(user_input)


        context['data'] = bussiness_data['businesses']

        # Model creation
        # for bussness in bussiness_data['businesses']:
        #     try:
        #         Venue.objects.create(yelp_id=bussness["id"])
        #     except:
        #         continue


        return render(request,"venues/_sample_yelp_output.html",context)



def sample_yelp_single_output(request, yelp_id):
    venue, is_created = Venue.objects.get_or_create(yelp_id=yelp_id)
    context = {
        'data': venue.raw_yelp_data()
    }
    return render(request, 'venues/_sample_yelp_single_output.html', context)
