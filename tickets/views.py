from django.shortcuts import render
from django.db.models import Q, Avg, Max, Min
from django.http import HttpResponse
from .models import Route


def index(request):
    return render(request, "tickets/index.html")


def home(request):
    return HttpResponse("<h1>Fantastic Four</h1>")


def searchView(request):
    qs = Route.objects.all()
    source_query = request.GET.get("source")
    destination_query = request.GET.get("destination")
    startDate_query = request.GET.get("startDate")
    finalDate_query = request.GET.get("finalDate")
    isPlane_query = request.GET.get("isPlane")
    print("Plane")
    print(isPlane_query)
    isTrain_query = request.GET.get("isTrain")
    print("Train")
    print(isTrain_query)
    isBus_query = request.GET.get("isBus")

    if source_query != "" and source_query is not None:
        qs = qs.filter(source=source_query)

    if destination_query != "" and destination_query is not None:
        qs = qs.filter(destination=destination_query)

    if startDate_query != "" and startDate_query is not None:
        qs = qs.filter(departure__date__gte=startDate_query)

    if finalDate_query != "" and finalDate_query is not None:
        qs = qs.filter(departure__date__lte=finalDate_query)

    if isPlane_query == "on" and isTrain_query == "on" and isBus_query == "on":
        print("good")
    elif isPlane_query == None and isTrain_query == None and isBus_query == None:
        print("good")
    elif isBus_query == None:
        # qs = qs.filter(Q(isPlane=(isPlane_query=='on')) | Q(isTrain=(isTrain_query=='on')) | Q(isBus=(isBus_query=='on')))
        if isPlane_query == "on" and isTrain_query == "on":
            qs = qs.filter(Q(isPlane=True) | Q(isTrain=True))
        elif isPlane_query == "on":
            qs = qs.filter(isPlane=True)
        else:
            qs = qs.filter(isTrain=True)

    else:
        if isPlane_query == "on":
            qs = qs.filter(isTrain)
        if isTrain_query == "on":
            qs = qs.filter(isTrain=True)
    try:
        planeQs = qs.filter(isPlane=True)
        min = planeQs.order_by("price").first()
        print(min.departure)
        minPrice = min.price
        minPriceDeparture = min.departure
        minPriceCompany = min.company
        max = planeQs.order_by("price").last()
        maxPrice = max.price
        maxPriceDeparture = max.departure
        maxPriceCompany = max.company
        average = planeQs.aggregate(Avg("price"))
        averagePrice = int(average["price__avg"])
    except:
        minPrice = maxPrice = averagePrice = 0
        minPriceDeparture = minPriceCompany = maxPriceDeparture = maxPriceCompany = "NA"

    try:
        trainQS = qs.filter(isTrain=True)
        tmin = trainQS.order_by("price").first()
        tminPrice = tmin.price
        tmax = trainQS.order_by("price").last()
        tmaxPrice = tmax.price
        taverage = trainQS.aggregate(Avg("price"))
        taveragePrice = int(taverage["price__avg"])
    except:
        tminPrice = tmaxPrice = taveragePrice = 0
        tminPriceDeparture = (
            tminPriceCompany
        ) = tmaxPriceDeparture = tmaxPriceCompany = "NA"

    context = {
        "queryset": qs,
        "minPrice": minPrice,
        "minPriceDeparture": minPriceDeparture,
        "minPriceCompany": minPriceCompany,
        "maxPrice": maxPrice,
        "maxPriceDeparture": maxPriceDeparture,
        "maxPriceCompany": maxPriceCompany,
        "averagePrice": averagePrice,
        "tminPrice": tminPrice,
        "tmaxPrice": tmaxPrice,
        "taveragePrice": taveragePrice,
    }
    return render(request, "tickets/search.html", context)

    # context
    # return render(request, "tickets/visual.html", context)
