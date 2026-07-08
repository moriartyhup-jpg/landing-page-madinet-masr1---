import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from .models import Lead

@csrf_exempt
@require_POST
def submit_lead(request):
    try:
        data = json.loads(request.body.decode('utf-8'))
    except json.JSONDecodeError:
        return JsonResponse({"status": "error", "message": "Invalid JSON data structure"}, status=400)

    name = data.get('name')
    phone = data.get('phone')

    # Basic Validation
    if not name or not phone:
        return JsonResponse({"status": "error", "message": "الاسم ورقم الهاتف مطلوبان."}, status=400)

    # Save the Lead
    try:
        lead = Lead.objects.create(
            name=name,
            phone=phone,
            project=data.get('project'),
            unit=data.get('unit'),
            source=data.get('source'),
            page=data.get('page'),
            url=data.get('url'),
            device=data.get('device'),
            notes=data.get('notes')
        )
        print(f"📥 New Lead Received: {lead.name} ({lead.phone}) for project {lead.project}")
        return JsonResponse({
            "status": "success",
            "message": "تم حفظ طلبك بنجاح.",
            "lead_id": lead.id
        }, status=201)
    except Exception as e:
        print(f"❌ Error saving lead: {str(e)}")
        return JsonResponse({"status": "error", "message": "حدث خطأ أثناء حفظ البيانات."}, status=500)
