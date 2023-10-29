from django.shortcuts import render, redirect
from django.contrib import messages
from .models import EmergencyService, EmergencyServiceRequest
from .forms import EmergencyServiceRequestForm


def emergency_services_view(request):
    """
    Handles emergency services requests.

    On POST, validates the form and processes the request. If the form is valid, checks for
    confirmation. If confirmed, saves the request; otherwise, renders a confirmation page.
    On GET, displays available emergency services.

    Args:
        request (HttpRequest): The incoming request.

    Returns:
        HttpResponse: Rendered page based on the request type and form validation.
    """

    services = EmergencyService.objects.all()

    if request.method == 'POST':
        form = EmergencyServiceRequestForm(request.POST)

        if form.is_valid():
            if 'confirm' in request.POST:
                request_obj = form.save(commit=False)
                request_obj.status = 'Pending'
                request_obj.save()

                messages.success(
                    request,
                    f"Request sent! Your request for {request_obj.service.service_type} is now pending for approval."
                )
                return redirect('emergency_services')

            else:
                selected_service = EmergencyService.objects.get(pk=request.POST.get('service'))
                context = {
                    "service_type": selected_service.service_type,
                    "service_details": selected_service
                }
                return render(request, "confirm.html", context)

    return render(request, "emergency.html", {"services": services, "form": EmergencyServiceRequestForm()})
