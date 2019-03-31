from django.contrib import admin

# Register your models here.
from .models import  Comment, Symptoms


    
class SymptomAdmin(admin.ModelAdmin):
	fieldsets=[
    (None,      {'fields':['name']}),
    ('Data Information',{'fields':['causes','symptom','remedy','link','image'],'classes':['collapse']})

	]
	list_display=('name','causes','symptom','remedy','link','image')
	search_fields=['name']

   
class CommentAdmin(admin.ModelAdmin):
	fieldsets=[
	(None, {'fields':['user']}),
	('Data Information', {'fields':['email','text','created_date'], 'classes':['collapse']})]
	list_display=('user','email','text','created_date')
	search_fields=['user']



admin.site.register(Comment, CommentAdmin)
admin.site.register(Symptoms, SymptomAdmin)
