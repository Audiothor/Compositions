# Used to manage global variables in the project

from django.conf import settings # import the settings file

def variables(request):
    # return the value you want as a dictionnary. you may add multiple values in there.
    return {'VERSION': settings.VERSION}