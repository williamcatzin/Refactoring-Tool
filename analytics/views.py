from django.shortcuts import render
from tool.models import Commit

def analytics_detail(request):
    """ returns the html format to display data from the database
        and analytics associated with the data.
    """
    messages = Commit.objects.all()
    return render(request, 'analytics_detail.html', {'messages':messages})
