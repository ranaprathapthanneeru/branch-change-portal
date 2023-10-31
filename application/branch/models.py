from django.db import models

# Create your models here.

value = 1
class Student(models.Model):
	roll_no = models.IntegerField(blank=False)
	name = models.CharField(max_length=400,blank=True)
	cpi = models.FloatField(blank=False)
	password = models.CharField(max_length=8,blank=False)
	category = models.CharField(max_length=100,blank=False)
	curr_branch = models.CharField(max_length = 100,blank=False)	
    
	def __str__(self):
		return self.name

class Results(models.Model):
	roll_no = models.IntegerField(blank=False)
	name = models.CharField(max_length = 400,blank=False)
	curr_branch = models.CharField(max_length = 100, blank=False)
	dest_branch = models.CharField(max_length = 100,blank=False)	

	def __str__(self):
		return self.name		

class BranchChange(models.Model):
	LIST_COURSES = (
        ('AE B.Tech', 'AE B.Tech'),
        ('CL B.Tech', 'CL B.Tech'),
        ('MM B.Tech', 'MM B.Tech'),
        ('MM Dual Deg Y2', 'MM Dual Deg Y2'),
        ('MM Dual Deg Y1', 'MM Dual Deg Y1'),
        ('CE B.Tech', 'CE B.Tech'),
        ('ME B.Tech', 'ME B.Tech'),
        ('ME Dual Deg M2', 'ME Dual Deg M2'),
        ('EN Dual Deg', 'EN Dual Deg'),
        ('CS B.Tech', 'CS B.Tech'),
        ('EE Dual Deg E1', 'EE Dual Deg E1'),
        ('EE Dual Deg E2', 'EE Dual Deg E2'),
        ('EE B.Tech', 'EE B.Tech'),
        ('EP B.Tech', 'EP B.Tech'),
        ('EP Dual Deg N1', 'EP Dual Deg N1'),
        ('CH','CH'),
    )
	LIST_CATEGORY = (
        ('GE', 'GE'),
        ('SC', 'SC'),
        ('OBC', 'OBC'),
        ('ST', 'ST'),
        ('Pwd', 'Pwd'),
    )
	roll_no = models.IntegerField(blank=False)	
	name = models.CharField(max_length=400, blank=False)
	current_branch = models.CharField(max_length=100, blank=False)	
	cpi = models.FloatField(blank=False)
	category = models.CharField(max_length=3, blank=False)
	preference1 = models.CharField(max_length=100, blank=True, choices=LIST_COURSES)
	preference2 = models.CharField(max_length=100, blank=True, choices=LIST_COURSES)
	preference3 = models.CharField(max_length=100, blank=True, choices=LIST_COURSES)
	preference4 = models.CharField(max_length=100, blank=True, choices=LIST_COURSES)
	preference5 = models.CharField(max_length=100, blank=True, choices=LIST_COURSES)
	preference6 = models.CharField(max_length=100, blank=True, choices=LIST_COURSES)
	preference7 = models.CharField(max_length=100, blank=True, choices=LIST_COURSES)
	preference8 = models.CharField(max_length=100, blank=True, choices=LIST_COURSES)
	preference9 = models.CharField(max_length=100, blank=True, choices=LIST_COURSES)
	preference10 = models.CharField(max_length=100, blank=True, choices=LIST_COURSES)
	preference11 = models.CharField(max_length=100, blank=True, choices=LIST_COURSES)
	preference12 = models.CharField(max_length=100, blank=True, choices=LIST_COURSES)
	preference13 = models.CharField(max_length=100, blank=True, choices=LIST_COURSES)
	preference14 = models.CharField(max_length=100, blank=True, choices=LIST_COURSES)
	preference15 = models.CharField(max_length=100, blank=True, choices=LIST_COURSES)
	preference16 = models.CharField(max_length=100, blank=True, choices=LIST_COURSES)
	def __str__(self):
		return self.name
