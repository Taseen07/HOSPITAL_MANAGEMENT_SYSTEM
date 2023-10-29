from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import HospitalBeds


@login_required
def general_bed_search(request):
    """
    View function to search for general beds.

    Queries available beds for various general categories such as 'Delux Single', 'Standard Single', etc.

    Args:
        request (HttpRequest): HttpRequest object.

    Returns:
        Rendered template: Rendered template with available general beds.
    """
    available_beds = HospitalBeds.objects.filter(
        category__in=[
            'Delux Single', 'Standard Single', 'Luxury Single',
            'Double Bedded Room (per bed)', 'Standard Suite', 'Delux Suite',
            'General Ward (Male)', 'General Ward (Female)'
        ],
        is_available=True
    )

    context = {
        'available_beds': available_beds,
        'category': 'GENERAL BEDS',
    }
    return render(request, 'generalBedSearch.html', context)


def extensive_bed_search(request):
    """
    View function to search for ICU, CCU, and HDU beds.

    Queries available beds for the combined categories ICU, CCU, and HDU.

    Args:
        request (HttpRequest): HttpRequest object.

    Returns:
        Rendered template: Rendered template with available ICU, CCU, and HDU beds.
    """
    available_beds = HospitalBeds.objects.filter(
        category__in=['ICU', 'CCU', 'HDU'],
        is_available=True
    )

    context = {
        'available_beds': available_beds,
        'category': 'ICU/CCU/HDU',
    }
    return render(request, 'extensiveBedSearch.html', context)
