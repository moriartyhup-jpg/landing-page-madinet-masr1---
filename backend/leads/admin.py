import csv
from django.http import HttpResponse
from django.contrib import admin
from .models import Lead

@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'project', 'unit', 'notes', 'source', 'device', 'created_at')
    list_filter = ('project', 'source', 'device', 'created_at')
    search_fields = ('name', 'phone', 'project', 'unit', 'source', 'notes')
    readonly_fields = ('created_at',)
    date_hierarchy = 'created_at'
    actions = ["export_as_csv"]

    # Make the admin view clean and readable
    fieldsets = (
        ("بيانات العميل الأساسية", {
            'fields': ('name', 'phone')
        }),
        ("معلومات الاهتمام والتسجيل", {
            'fields': ('project', 'unit', 'notes', 'source')
        }),
        ("معلومات تقنية", {
            'fields': ('page', 'url', 'device', 'created_at')
        }),
    )

    def export_as_csv(self, request, queryset):
        # Fields to export in order
        fields_to_export = [
            ('name', 'الاسم'),
            ('phone', 'رقم الهاتف'),
            ('project', 'المشروع'),
            ('unit', 'الوحدة المهتم بها'),
            ('notes', 'تفاصيل الاهتمام والملاحظات'),
            ('source', 'المصدر / مكان التسجيل'),
            ('page', 'عنوان الصفحة'),
            ('url', 'رابط الصفحة'),
            ('device', 'نوع الجهاز'),
            ('created_at', 'تاريخ التسجيل'),
        ]

        response = HttpResponse(content_type='text/csv; charset=utf-8-sig')
        response['Content-Disposition'] = 'attachment; filename=leads_export.csv'
        writer = csv.writer(response)

        # Write header
        writer.writerow([label for _, label in fields_to_export])

        # Write data
        for obj in queryset:
            row = []
            for field_name, _ in fields_to_export:
                val = getattr(obj, field_name)
                # Format datetime to string if needed
                if hasattr(val, 'strftime'):
                    val = val.strftime('%Y-%m-%d %H:%M:%S')
                elif val is None:
                    val = ''
                row.append(val)
            writer.writerow(row)

        return response

    export_as_csv.short_description = "تصدير طلبات التسجيل المحددة كـ ملف Excel / CSV"
