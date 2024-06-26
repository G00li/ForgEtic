from django.core.exceptions import PermissionDenied
from django.utils.decorators import method_decorator



class BlockSuperuserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
                # Permitir acesso a superusers ao /admin
        if request.path.startswith('/admin'):
            return self.get_response(request)

        if request.user.is_authenticated and request.user.is_superuser:
            raise PermissionDenied("Superusers não tem acesso a esta pagina.")
        
        response = self.get_response(request)
        return response
    
def block_superuser(view_func):
    def _wrapped_view_func(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_superuser:
            raise PermissionDenied("Superusers não tem acesso a esta pagina.")
        return view_func(request, *args, **kwargs)
    return _wrapped_view_func