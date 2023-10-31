from django import forms

from .models import BranchChange, Student
from django.core.exceptions import ObjectDoesNotExist

class SignUpForm(forms.Form):
	roll_no = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Roll Number'}))
	pass_word = forms.CharField(max_length=400,widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
	fields = ['roll_no', 'pass_word']

	def clean_roll_no(self):
		roll_no =  self.cleaned_data.get('roll_no')
		roll_str = str(roll_no)
		first_two = roll_str[:2] 
		if not first_two == "15":
			raise forms.ValidationError("Please Give a Valid Roll Number . Eg:1500a00bc")
		if not len(roll_str) == 9:
			raise forms.ValidationError("Please Give a Valid Roll Number . Eg:1500a00bc")
		return roll_no

	def clean_pass_word(self):
		roll_no =  self.cleaned_data.get('roll_no')
		hello= "h"
		try:
			bc = Student.objects.get(roll_no=roll_no)
		except ObjectDoesNotExist:
			hello = "n"
			raise forms.ValidationError("Invalid User")	
		if not hello == "n":	
			pass_word = self.cleaned_data.get('pass_word')
			pass_word_str = str(pass_word)
			if not pass_word_str == bc.password:
				raise forms.ValidationError("Password is incorrect")
		return pass_word

class LogoutForm(forms.Form):
	fieds = ['','']		

class BranchChangeForm(forms.ModelForm):
	class Meta:
		model = BranchChange
		fields = ['roll_no','name', 'current_branch','cpi', 'category', 'preference1', 'preference2', 'preference3',
		 'preference4', 'preference5', 'preference6', 'preference7', 'preference8', 'preference9', 'preference10',
		 'preference11','preference12','preference13','preference14','preference15','preference16']		
		
	def clean_roll_no(self):
		roll_no =  self.cleaned_data.get('roll_no')
		roll_str = str(roll_no)
		first_two = roll_str[:2] 
		if not first_two == "15":
			raise forms.ValidationError("Please Give a Valid Roll Number . Eg:1500a00bc")
		if not len(roll_str) == 9:
			raise forms.ValidationError("Please Give a Valid Roll Number . Eg:1500a00bc")
		return roll_no

	def clean_cpi(self):	
		cpi = self.cleaned_data.get('cpi')
		if cpi > 10 :
			raise forms.ValidationError("Please Give a Valid CPI")
		if cpi < 0 :
			raise forms.ValidationError("Please Give a Valid CPI")
		return cpi		


