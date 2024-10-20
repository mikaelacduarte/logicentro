from django.http import JsonResponse

# Função de view simples que retorna uma resposta JSON
def my_view(request):
    data = {
        "message": "Hello, this is the API response"
    }
    return JsonResponse(data)
