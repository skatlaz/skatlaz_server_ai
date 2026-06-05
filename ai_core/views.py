import json
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .services.mcp_runtime import run_task

@csrf_exempt
def mcp_task(request):
    if request.method == "GET":
        return render(request, "ai_core/mcp_task.html")
    payload = request.POST.dict()
    if request.content_type and "application/json" in request.content_type:
        try:
            payload = json.loads(request.body.decode("utf-8"))
        except Exception:
            payload = {}
    result = run_task(
        payload.get("task_type", "code"),
        payload.get("prompt", ""),
        payload.get("language", "html"),
        payload.get("target_os", "all"),
        payload.get("agent_slug", ""),
    )
    return JsonResponse(result, json_dumps_params={"ensure_ascii": False, "indent": 2})
