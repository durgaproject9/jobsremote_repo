from django.contrib import admin
from testapp.models import hydjobs,banglorejobs,mumbaijobs,punejobs

# Register your models here.
class hydjobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phonenumber']

class banglorejobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phonenumber']

class mumbaijobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phonenumber']

class punejobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phonenumber']

admin.site.register(hydjobs,hydjobsAdmin)
admin.site.register(banglorejobs,banglorejobsAdmin)
admin.site.register(mumbaijobs,mumbaijobsAdmin)
admin.site.register(punejobs,punejobsAdmin)
