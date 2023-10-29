from django.shortcuts import render

# Create your views here.

def home_screen_view(request):
    # context = {}
    # context['some_string'] = "this is the string from view"

    context = {
        'some_string': "this is the string from view",
    }

    list_of_values = []
    list_of_values.append("first entry")
    list_of_values.append("second entry")
    list_of_values.append("third entry")
    list_of_values.append("fourth entry")

    context = {}
    context['list_of_values'] = list_of_values

    return render(request, "homepage/homepage.html", context)