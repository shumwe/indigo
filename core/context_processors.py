from core.models import Path, Topic, Tutorial

def get_paths(request):
    paths = Path.objects.all()
    return dict(paths=paths)