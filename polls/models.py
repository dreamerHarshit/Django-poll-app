import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
	   return self.question_text
    
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days = 1) <= self.pub_date <=now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently'


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
	    return self.choice_text
        
    def was_published_recently(self):
            now = timezone.now()
            return now - datetime.timedelta(days=1) <= self.pub_date <= now

class VoteDetails(models.Model):
    
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    username = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete =models.CASCADE)
    presentdate = models.DateTimeField(null = False,blank = False)


def test_was_published_recently_with_old_question(self):

    time = timezone.now() - datetime.timedelta(days=30)
    old_question = Question(pub_date=time)
    self.assertEqual(old_question.was_published_recently(), False)

def test_was_published_recently_with_recent_question(self):
    """
    was_published_recently() should return True for questions whose
    pub_date is within the last day.
    """
    time = timezone.now() - datetime.timedelta(hours=1)
    recent_question = Question(pub_date=time)
    self.assertEqual(recent_question.was_published_recently(), True)


class User_details(models.Model):
    first_name = models.CharField(max_length = 50)
    middle_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    dob = models.DateTimeField(null = True ,blank = True)
    age = models.IntegerField()
    maritalstatus = models.BooleanField(default = False)


