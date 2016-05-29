from django.db import models

from datetime import date


class Student(models.Model):

	student_id = models.CharField(primary_key= True, max_length = 10)

	scholarship_id = models.ForeignKey('Scholarship', default=0)

	first_name = models.CharField(max_length= 20, default= 'first')

	last_name = models.CharField(max_length= 20, default= 'last')
	
	middle_name = models.CharField(max_length= 20, default= 'middle', blank = True)
	
	email = models.EmailField(blank= True)
		
	address = models.TextField(blank= True)
	
	birthday = models.DateField(blank= True, default = '1990-11-01')

	GENDER_CHOICE = (
			('male', 'Male'),
			('female', 'Female')
		)

	gender = models.CharField(max_length= 6,
								choices= GENDER_CHOICE,
								blank= True
							)

	COURSES = {
		('Sciences', (
					('bscs', 'BS Computer Science'),
					('bsbio', 'BS Biology'),
					('bsmat', 'BS Mathematics'),
				)
			),
		('Social Sciences', (
					('baps', 'BA Political Science'),
					('bspsy', 'BA Psychology')
				)
			),
		('Arts and Humanities', (
					('bamc', 'BA  Mass Communication'),
					('bafap', 'BA Fine Arts (Product Design)'),
					('bafas', 'BA Fine Arts (Studio Arts)'),
				)
			),
		('Management', (
					('bsmgt', 'BS Management'),
				)
			),
	}

	course = models.CharField(max_length = 5,
							choices = COURSES,
							default='unkwn')

	YEAR_IN_SCHOOL = (
		('fr', 'Freshman'),
		('so', 'Sophomore'),
		('ju', 'Junior'),
		('se', 'Senior'),
	)

	year = models.CharField(max_length =2, 
							choices =YEAR_IN_SCHOOL,
							default='fr')

	term = models.CharField(max_length= 9, default='2015-2016')


	def __str__(self):
		return "%s %s %s" % (self.first_name, self.middle_name, self.last_name)

class Instructor(models.Model):

	instructor_id = models.CharField(primary_key= True, max_length = 10)

	first_name = models.CharField(max_length= 20, default= 'first')

	last_name = models.CharField(max_length= 20, default= 'last')
	
	middle_name = models.CharField(max_length= 20, default= 'middle', blank = True)
	
	email = models.EmailField(blank= True)
	
	address = models.TextField(blank= True)
	
	birthday = models.DateField(blank= True, default = '1990-11-01')

	GENDER_CHOICE = (
			('male', 'Male'),
			('female', 'Female')
		)

	gender = models.CharField(max_length= 6,
								choices= GENDER_CHOICE,
								blank= True
							)

	def __str__(self):
		return "%s %s %s" % (self.first_name, self.middle_name, self.last_name)



class Subject(models.Model):

	subject_id = models.CharField(primary_key= True, max_length = 10)

	Detail_id = models.ManyToManyField('Detail')
	
	lab_id = models.ForeignKey('Lab', default = 0,)


	title = models.CharField(max_length= 50,
							default='title')

	code = models.PositiveSmallIntegerField(default= '00000')

	description = models.TextField(blank= True)

	unit = models.PositiveSmallIntegerField(default= 3)

	has_lab = models.BooleanField(default= False)

	is_offered = models.BooleanField(default= True)

	def __str__(self):
		return "%s" % (self.title)


class Detail(models.Model):
	
	Detail_id = models.CharField(primary_key= True, max_length = 10)

	instructor_id = models.ForeignKey('Instructor',
								default= 0)

	title = models.CharField(max_length= 50,
							default='title')

	section = models.CharField(max_length= 3)

	slots = models.PositiveSmallIntegerField(default= 30)

	location = models.CharField(max_length= 25, blank= True)

	DAY_SCHEME = (
			('mth', 'Monday/Thursday'),
			('tfr', 'Tuesday/Friday'),
			('fri', 'Friday'),
			('wed', 'Wednesday'),
			('sat', 'Saturday'),
			('tba', 'To Be Announced')
		)

	day = models.CharField(max_length=3, choices = DAY_SCHEME, default='tba')

	start = models.TimeField()

	end = models.TimeField()

	def __str__(self):
		 return "%s %s" % (self.title,self.section)


class Lab(models.Model):
	
	lab_id = models.CharField(primary_key= True, max_length = 10)

	title = models.CharField(max_length= 50,
							default='title')

	Detail_id =  models.ManyToManyField('Detail')

	lab_fee = models.DecimalField(max_digits= 5,
								  decimal_places= 2,
								  default= 0.00)

	def __str__(self):
		return "%s" % (self.title)


class Scholarship(models.Model):

	scholarship_id = models.CharField(primary_key= True, max_length = 10)
	BRACKETS = (
			('nd', 'No Discount'),
			('pd40', 'Partial Discount (40%)' ),
			('pd60', 'Partial Discount (60%)' ),
			('pd80', 'Partial Discount (80%)' ),
			('fd', 'Full Discount' ),
			('fds', 'Full Discount and Stipend' ),
		)

	# todo: double-check default
	sts = models.CharField(max_length= 4,
							choices= BRACKETS,
							default= 'nd')

	#other scholarship
	other_scho = models.CharField(max_length= 30,
							blank= True)

	def __str__(self):
		return "%s" % (self.sts)

class Enrollment(models.Model):

	enrollment_id = models.CharField(primary_key= True, max_length = 10)
	
	subject_id =  models.ManyToManyField('Subject')

	student_id = models.ForeignKey('Student')

	grade_id = models.ForeignKey('Grade', default = 0)

	term = models.CharField(max_length= 9, default='2015-2016')

	def __str__(self):
		return "%s - %s" % (self.student_id.student_id, self.term)

class Grade(models.Model):

	grade_id = models.CharField(primary_key= True, max_length = 10)

	subject_id = models.ManyToManyField('Subject')

	GRADE_SCHEME = (
			('100' , '1.00'),
			('125' , '1.25'),
			('150' , '1.50'),
			('175' , '1.75'),
			('200' , '2.00'),
			('225' , '2.25'),
			('250' , '2.50'),
			('275' , '2.75'),
			('300' , '3.00'),
			('400' , '4.00'),
			('500' , '5.00'),
			('INC' , 'INCOMPLETE'),
			('DRP' , 'DROPPED'),
		)

	grade = models.CharField(max_length= 10, 
							choices= GRADE_SCHEME,
							blank= True)

	def __str__(self):
		return "%s" % (self.grade_id)

