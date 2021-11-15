from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
# Create your views here.
from dayplanner.services import yelp_client
from resources.days.models import Day


def explore(requets):
    context = {}
    with transaction.atomic():
        try:
            days = Day.objects.all()
            context["days"] = days
        except Exception as e:
            return HttpResponse("Error Code: %s" % e)

    return render(requets,"explore/explore.html", context)

def day_summary(requests, day_id):
    day = get_object_or_404(Day, pk=day_id)
    context = {}
    context["day"] = day
    DayVenues = day.dayvenue_set.all()
    fetch_list = []
    for dv in DayVenues:
        fetch_list.append(dv.venue.yelp_id)

    responses = yelp_client.fetch_many(fetch_list)
    coordinates = []
    # [{"latitude":<lat_val>,"longitude":<long_val>,"name":<name>}]
    for resp in responses:
        data = resp["coordinates"]
        data["name"] = resp["name"]
        coordinates.append(data)
    context["coordinates"] = coordinates
    print(context["coordinates"])

    return render(requests, "explore/day_summary.html", context)