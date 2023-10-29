from django.shortcuts import render
from .models import DiagnosticCategory, DiagnosticTest


def diagnostics(request):
    """
    Handles the display of diagnostic categories and tests.

    For POST requests, it filters tests by category and optional search.
    For GET requests, it shows all categories.

    Parameters:
    - request: The incoming HTTP request.

    Returns:
    - Rendered template (either diagnostics_detail.html or diagnostics.html) with context.
    """

    if request.method == 'POST':
        category_id = request.POST.get('category')
        search_query = request.POST.get('search_query', '').lower()

        if category_id:
            tests = DiagnosticTest.objects.filter(
                category_id=category_id,
                name__icontains=search_query
            )
            category = DiagnosticCategory.objects.get(pk=category_id)
            return render(request, 'diagnostics_detail.html', {'tests': tests, 'category': category})

    categories = DiagnosticCategory.objects.all()  # Moved outside the else block to ensure it's always defined
    return render(request, 'diagnostics.html', {'categories': categories})
