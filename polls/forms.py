from django import forms
from .models import Question, Choice  ,User_details
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.utils import timezone

class QuestionForm(forms.Form):
    Your_Question = forms.CharField(label='Your_Question',max_length=200)
    Choice_1 = forms.CharField(label = 'Your_Choice1',max_length=50)
    Choice_2 = forms.CharField(label = 'Your_Choice2',max_length=50)
    Choice_3 = forms.CharField(label = 'Your_Choice3',max_length=50, required=False)
    Choice_4 = forms.CharField(label = 'Your_Choice4',max_length=50, required = False)
    Choice_5 = forms.CharField(label = 'Your_Choice5',max_length=50, required = False)
    
    def save(self):
        Question.objects.all()
        q = Question(question_text = self.cleaned_data['Your_Question'],pub_date = timezone.now())
        q.save()
        q.choice_set.create(choice_text = self.cleaned_data['Choice_1'], votes=0)
        q.choice_set.create(choice_text=self.cleaned_data['Choice_2'], votes=0)
        q.choice_set.create(choice_text=self.cleaned_data['Choice_3'], votes=0)
        q.choice_set.create(choice_text=self.cleaned_data['Choice_4'], votes=0)
        q.choice_set.create(choice_text=self.cleaned_data['Choice_5'], votes=0)
        return q


class DetailForm(forms.Form):
    first_name = forms.CharField(label = 'first_name',max_length = 50)
    middle_name = forms.CharField(label = 'middle_name',max_length = 50)
    last_name = forms.CharField(label = 'last_name',max_length = 50)
    dob = forms.DateTimeField(label = 'dob',required = False)
    age = forms.IntegerField(label = 'age')
    maritalstatus = forms.BooleanField(label = 'maritalstatus',required = False)

    def save(self):
        u = User_details(first_name = self.cleaned_data['first_name'],middle_name = self.cleaned_data['middle_name'],last_name = self.cleaned_data['last_name'],dob = self.cleaned_data['dob'],age = self.cleaned_data['age'],maritalstatus = self.cleaned_data['maritalstatus'])
        u.save()


class LoginForm(forms.Form):
    user_name = forms.CharField(label='user_name',max_length=20)
    pass_word = forms.CharField(label = "pass_word", min_length= 5)

    def save(self):
        username = self.cleaned_data['user_name']
        password = self.cleaned_data['pass_word']
        l = authenticate(username=username,password =password)
        return l


class SignUpForm(forms.Form):
    user_name = forms.CharField(label = "user_name",max_length = 20)
    pass_word = forms.CharField(label = "pass_word", min_length = 5)

    def save(self):
        username = self.cleaned_data['user_name']
        password = self.cleaned_data['pass_word']
        s = User.objects.create_user(username,username,password)
        s.save()