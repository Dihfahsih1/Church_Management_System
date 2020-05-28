from .models import *
from .views import *


def church_processor(request):
    if request.user.is_authenticated:
        user_access=request.user.Role == 'Secretary' or 'Admin' or 'SuperAdmin' or 'Assistant_Admin'
        context = {
            'user_access': user_access,

        }
        return context
    else:
        'none'    



