from django.http.response import JsonResponse

def success(data):
    return JsonResponse({"status": True, "data": data, "message": ""}, status=200)

def fail(message):
    return JsonResponse({"status": False, "data": {}, "message": message}, status=400)
