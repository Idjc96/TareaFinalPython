from rest_framework import viewsets
from .serializer import SenapiSerializer
from .models import Senapi


# Create your views here.

class ApisenaView(viewsets.ModelViewSet):
    serializer_class = SenapiSerializer
    queryset = Senapi.objects.all()