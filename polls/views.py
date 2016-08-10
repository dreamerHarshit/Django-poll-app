from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect , HttpResponse ,JsonResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
from django.shortcuts import render
from .models import Choice, Question , User_details, VoteDetails
from .forms import QuestionForm , DetailForm, LoginForm, SignUpForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import json


class IndexView(generic.ListView):
    login_url = '/polls/login_id/'
    template_name = 'polls/index.html'

    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5] 


class DetailView(LoginRequiredMixin,generic.DetailView):
    login_url = '/polls/login_id/'
    model = Question
    template_name = 'polls/detail.html'
    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(LoginRequiredMixin,generic.DetailView):
    login_url = '/polls/login_id/'
    model = Question
    template_name = 'polls/results.html'


@login_required(login_url='/polls/login_id/')
@csrf_exempt
def vote(request,question_id,message):
    question = get_object_or_404(Question, pk=question_id)
    Date_detail = VoteDetails()
    current_user = request.user
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        Date_detail.choice_id = selected_choice.id
        Date_detail.username_id = current_user.id
        Date_detail.presentdate = timezone.now()
        Date_detail.save()
    #return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
    return JsonResponse({"redirect": reverse('polls:results',args=(question.id,))},safe=False)

@login_required(login_url='/polls/login_id/')
@csrf_exempt
def get_name(request):
    if request.method== 'POST':
       form = QuestionForm(request.POST)
       if form.is_valid():
            print("Form is valid")
            ques=form.save()
            #data = serializers.serialize('json',[ques,])
            return JsonResponse({"redirect" : '/polls/'},safe=False)
    else:
        form = QuestionForm()

    return render(request,'polls/Question.html',{'form':form})


@login_required(login_url='/polls/login_id/')
def view_name(request):
    if request.method == 'POST':
        form = DetailForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({"redirect" :'/polls/'},safe = False)
        else :
            temp = form.errors
            print(temp)
    else:
        form = DetailForm()

    return render(request, 'polls/user.html',{'form': form})

@csrf_exempt
def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({"redirect": '/polls/login_id/'},safe=False)        
    else :
        form = SignUpForm()
    return render(request,'polls/signup.html',{'form':form})


@csrf_exempt
def login_view(request):
    form = LoginForm(request.POST or None)
    if request.method =='POST':
        if form.is_valid():
            user = form.save()
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return JsonResponse({"redirect" :'/polls/'},safe = False)
                else:
                    print("The user is Disabled")
            else:
                print("The user is invalid")
        else:
            print("The Form Is Invalid")
    else:        
        form = LoginForm()
    return render(request,'polls/login.html',{'form':form})


@login_required(login_url='/polls/')
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('polls:'))
    