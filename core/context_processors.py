from core.models import Path

def get_paths(request):
    paths = Path.objects.all()
    return dict(paths=paths)