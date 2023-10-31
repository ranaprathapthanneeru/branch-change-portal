from django.contrib import admin
from django.http import HttpResponse
# Register your models here
from .forms import SignUpForm
from .models import BranchChange, Student, Results

def export_csv(modeladmin, request, queryset):
    import csv
    from django.utils.encoding import smart_str
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=input_options.csv'
    writer = csv.writer(response, csv.excel)
    response.write(u'\ufeff'.encode('utf8')) # BOM (optional...Excel needs it to open UTF-8 file properly)
    
    for obj in queryset:
        writer.writerow([
            smart_str(obj.roll_no),
            smart_str(obj.name),
            smart_str(obj.current_branch),
            smart_str(obj.cpi),
            smart_str(obj.category),
            smart_str(obj.preference1),
            smart_str(obj.preference2),
            smart_str(obj.preference3),
            smart_str(obj.preference4),
        ])
    return response
export_csv.short_description = u"Export CSV"


class StudentAdmin(admin.ModelAdmin):
	list_display = ["roll_no","cpi"]
	class Meta:
		model = Student

admin.site.register(Student, StudentAdmin)

class ResultsAdmin(admin.ModelAdmin):
    list_display = ["roll_no","name","curr_branch","dest_branch"]
    class Meta:
        model = Results

admin.site.register(Results, ResultsAdmin)        

class BranchChangeAdmin(admin.ModelAdmin):
	actions = [export_csv]
	list_display = ["__str__", "roll_no", "cpi","preference1","preference2"]
	class Meta:
		model = BranchChange

admin.site.register(BranchChange, BranchChangeAdmin)