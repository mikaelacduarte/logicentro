from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions
from operacao.models import Operacao
from operacao.serializers import OperacaoSerializer

# Create your views here.
class OperacaoViewSet(viewsets.ModelViewSet):
    queryset = Operacao.objects.all()
    serializer_class = OperacaoSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [DjangoFilterBackend]  # Adiciona o backend de filtro
    filterset_fields = ['status']  # Define o campo de filtragem

def listar_operacoes(request):
    operacoes=Operacao.objects.values('placa', 'lacre', 'id_empresa_origem', 'id_empresa_destino', 'id_motorista', 'dta_saida')
    return JsonResponse(list(operacoes), safe=False)