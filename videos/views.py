from django.shortcuts import render
from .models import Video
from django.contrib.auth.decorators import login_required

@login_required
def dashboard_view(request):
    query = request.GET.get('q', '')
    if query:
        videos = Video.objects.filter(name__icontains=query)
    else:
        videos = Video.objects.all()
    context = {
        'videos': videos,
        'query': query,
    }
    return render(request, 'videos/dashboard.html', context)
