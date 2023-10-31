from django.shortcuts import render
from django.contrib import messages
from .forms import SignUpForm, BranchChangeForm, LogoutForm
from django.http import HttpResponse, HttpResponseRedirect
from .models import BranchChange, Student, Results
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
def home(request):
	title = "Login To Your Account"
	form = SignUpForm(request.POST or None)
	context = {
           "template_title": title,
           "form": form,
    }

	if form.is_valid():
		roll_no = form.cleaned_data['roll_no']
		request.session['roll_no']=roll_no
		return HttpResponseRedirect('/fill/')
	return  render(request, "home.html", context) 

def fill(request):
	title = "Welcome to BranchChangeForm"
	roll_no=request.session['roll_no']
	if roll_no == "Invalid":
		context = {
				"template_title":"Cannot record your Response, Please login",
		}
		return render(request, "response.html", context)
	try:
		person = Student.objects.get(roll_no=roll_no)
		name = person.name
		cpi = person.cpi
		branch = person.curr_branch
		cate = person.category
	except ObjectDoesNotExist:	
		context = {
			"template_title":"You are not enrolled in this institute",
		}
		return render(request, "response.html", context)


	warning = "" 
	if ((cate == "GE" or cate == "OBC") and cpi <8.0) or ((cate == "ST" or cate == "SC" or cate == "PwD") and cpi <7.0):
		warning = "You are not eligible for branch change"  


	data = {'roll_no': roll_no,'current_branch':branch,'cpi': cpi,'category':cate}
	form1 = LogoutForm(request.POST or None)
	form = BranchChangeForm(request.POST or None, initial = data)
	context = {
			"template_title":title,
			"warning":warning,
			"form":form,
			"form1":form1,
	}

	if form.is_valid():
		try:
			bc = BranchChange.objects.get(roll_no=roll_no)
			bc.delete()
		except ObjectDoesNotExist:
			hello = "none"
		form_roll_no = form.cleaned_data['roll_no']
		form_cpi = form.cleaned_data['cpi']
		form_category = form.cleaned_data['category']
		form_currbranch = form.cleaned_data['current_branch']
		if not form_roll_no	== roll_no	or not form_cpi == cpi or not form_category == cate or not form_currbranch == branch:
			context = {
			"template_title":title,
			"warning":warning,
			"form":form,
			"form1":form1,
			"warning1":"Do not alter your personal details",
			}

			return render(request,'bc.html', context)
				
	
		form.save()	
		request.session['roll_no']="Invalid"
		context = {
				"template_title":"You have submitted your Response",
		}
		return render(request, "response.html", context)

	return render(request, "bc.html", context)

def logout(request):
	request.session['roll_no']="Invalid"
	context = {
				"template_title":"You have logged out",
		}
	return render(request, "response.html", context)

def results(request):
	results_all = Results.objects.all()
	context = {
				"template_title":"Results are here",
				"results_all":results_all,
		}


	return render(request, "results.html", context)

def changepass(request):
	context = {
				"template_title":"Change Password  here",
		}		

	return render(request, "changepassword.html", context)		