try:
    from .gemini_mcp_builder import build_mcp_json
    from .template_scanner import scan_pugex_templates
except Exception:
    from ai_core.services.gemini_mcp_builder import build_mcp_json
    from ai_core.services.template_scanner import scan_pugex_templates

try:
    from ai_core.models import AIAgent, AIGeneratedArtifact
except Exception:
    AIAgent = AIGeneratedArtifact = None


def run_task(task_type: str, prompt: str, language: str = "", target_os: str = "all", agent_slug: str = ""):
    agent = None
    if AIAgent and agent_slug:
        agent = AIAgent.objects.filter(slug=agent_slug, active=True).first()
    if agent:
        language = language or agent.language
        target_os = target_os or agent.target_os
    data = build_mcp_json(task_type, prompt, language, target_os)
    if task_type == "code":
        result = {"action": "ai.generate_code", "mcp": data, "templates": scan_pugex_templates(language or "html")}
    elif task_type == "debug":
        result = {"action": "ai.fix_error", "mcp": data, "errors_json": data.get("errors_json", {})}
    elif task_type == "image":
        result = {"action": "ai.create_image", "mcp": data, "image_json": data.get("image_json", {})}
    elif task_type == "documents":
        result = {"action": "ai.documents", "mcp": data, "documents_json": data.get("documents_json", {})}
    else:
        result = {"action": "ai.chat", "mcp": data}
    if AIGeneratedArtifact:
        AIGeneratedArtifact.objects.create(title=f"{task_type}: {prompt[:60]}", task_type=task_type, agent=agent, input_prompt=prompt, output_json=result)
    return result
