from properties.forms import PropertySearchForm


def search_form(request):
    return {"search_form": PropertySearchForm(request.GET or None)}
