from .models import Profile


def profile(request):
    profile = Profile.objects.first()
    return {'profile': profile}
