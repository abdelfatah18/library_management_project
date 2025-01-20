from django.http import JsonResponse

def api_overview(request):
    return JsonResponse({"message": "Welcome to the Library Management System API!"})
