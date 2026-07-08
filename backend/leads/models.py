from django.db import models

class Lead(models.Model):
    name = models.CharField(max_length=255, verbose_name="الاسم")
    phone = models.CharField(max_length=50, verbose_name="رقم الهاتف")
    project = models.CharField(max_length=255, blank=True, null=True, verbose_name="المشروع")
    unit = models.CharField(max_length=255, blank=True, null=True, verbose_name="الوحدة المهتم بها")
    source = models.CharField(max_length=255, blank=True, null=True, verbose_name="المصدر / مكان التسجيل")
    page = models.CharField(max_length=255, blank=True, null=True, verbose_name="عنوان الصفحة")
    url = models.URLField(max_length=500, blank=True, null=True, verbose_name="رابط الصفحة")
    device = models.CharField(max_length=50, blank=True, null=True, verbose_name="نوع الجهاز")
    notes = models.TextField(blank=True, null=True, verbose_name="تفاصيل الاهتمام والملاحظات")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ التسجيل")

    class Meta:
        verbose_name = "طلب تسجيل (Lead)"
        verbose_name_plural = "طلبات التسجيل (Leads)"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.phone}"
