from functools import reduce
from django.core import validators
import re
from django.core.validators import URLValidator
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
import re

from django import forms
from .models import Player

class Registerform(UserCreationForm):
    email=forms.EmailField(required=True)
    class Meta:
        model=User
        fields=['username','email','password1','password2']


'''class candidate_Form(forms.ModelForm):
    class Meta:
        model = Candidate
        fields = "__all__" '''

CHOICES=[('item1','Male'),
         ('item2','Female')]
option = [('a', 'Beginner'),
           ('b', 'Intermediate'),('c', 'Advanced')]
from django import forms
from .models import Player


'''def date_join(self):
    doj = self.doj_2.text()
    doj = doj.split("-")
    doj = reduce(lambda i, j: i + "-" + j, doj[::-1])
    return doj'''
class playerform(forms.ModelForm):
    #dob=forms.DateField(validators=date_join)
    gender = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    standard = forms.ChoiceField(choices=option, widget=forms.RadioSelect())

    class Meta:
        model = Player
        fields = "__all__"

from django import forms
from .models import Coach
class coachform(forms.ModelForm):
    #dob=forms.DateField(validators=[date_join])
    gender = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())

    class Meta:
        model = Coach
        fields = "__all__"




#from .models import Candidate

'''Category=[('1','UNDER 14'),
          ('2','UNDER 17'),
          ('3','UNDER 19'),
          ('4','UNDER 21')]
Standard=[('1','BEGINNER'),
         ('2','INTERMEDIATE'),
         ('3','ADVANCED')]
Session=[('1','FORENOON'),
         ('2','AFTERNOON')]
def validate_mobile(value):
    mobile=str(value)
    pattern=re.compile("[6-9][0-9]{9}")
    if not (pattern.match(mobile)):
        raise forms.ValidationError("invalid phone no")'''







'''class candidate_Form(forms.ModelForm):
    GENDER_MALE = 0
    GENDER_FEMALE = 1
    GENDER_CHOICES = [(GENDER_MALE, 'Male'), (GENDER_FEMALE, 'Female')]
    name = forms.CharField(widget=forms.TextInput)
    #dob = forms.DateField(widget=forms.SelectDateWidget)
    gender = forms.ChoiceField(choices=GENDER_CHOICES,widget=forms.RadioSelect)
    session = forms.ChoiceField(choices=Session,widget=forms.Select)
    email = forms.EmailField(widget=forms.EmailInput)
    #category = forms.ChoiceField(choices=Category,widget=forms.Select)
    #parent_name = forms.CharField(widget=forms.TextInput)
    #phone_no = forms.IntegerField(validators=[validate_mobile])
    #standard = forms.ChoiceField(choices=Standard,widget=forms.Select)
    #doj = forms.DateField(widget=forms.SelectDateWidget)
    address = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Candidate 
        fields = '__all__' '''