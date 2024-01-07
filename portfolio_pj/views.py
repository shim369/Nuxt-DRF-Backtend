from django.http import HttpResponseRedirect

def redirect_to_documentation(request):
    return HttpResponseRedirect('/api/documentation/')