from django.shortcuts import render,redirect,get_object_or_404
from .models import Image,Profile,Comment
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from .forms import NewImageForm,UpdatebioForm,CommentForm
from .email import send_welcome_email
from .forms import NewsLetterForm
# from .forms import NewArticleForm, NewsLetterForm

# @login_required(login_url='/accounts/login/')
# def home_images(request):
#     return render(request,'index.html')

# from django.http  import HttpResponse

# Create your views here.
# def home_images(request):
#     return HttpResponse('Welcome to the Moringa Tribune')

# display images
@login_required(login_url='/accounts/login/')
def home_images(request):
    # if request.GET.get('search_iterm'):
    #     pictures=Image.search(request.GET.get('search_iterm'))
    # else:
    pictures=Image.objects.all()

    form=NewsLetterForm
    if request.method== 'POST':
        form=NewsLetterForm(request.POST or None)
        if form.is_valid():
            name=form.cleaned_data['your_name']
            email=form.cleaned_data['email']
            recipient=NewsLetterRecipients(name=name,email=email)
            recipient.save()
            send_welcome_email(name,email)
            HttpResponseRedirect('home_images')
    return render(request,'index.html',{"pictures":pictures,'letterForm':form})
@login_required(login_url='/accounts/login/')
def new_image(request):
    current_user=request.user
    if request.method=='POST':
        form=NewImageForm(request.POST,request.FILES)
        if form.is_valid():
            image=form.save(commit=False)
            image.user=current_user
            image.save()
            return redirect('homePage')
        else:
            form=NewImageForm()
        return render(request,'registration/new_image.html',{"form":form})

# @login_required(login_url='/accounts/login/')
# def new_image(request):
#     current_user = request.user
#     if request.method == 'POST':
#         form = NewImageForm(request.POST, request.FILES)
#         if form.is_valid():
#             image = form.save(commit=False)
#             image.user = current_user
#             image.save()
#         return redirect('homePage')

#     else:
#         form = NewImageForm()
#     return render(request, 'registration/new_image.html', {"form": form})
