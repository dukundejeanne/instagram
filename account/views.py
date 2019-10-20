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
            # HttpResponseRedirect('hamePage')
        return redirect('homePage')
    else:
        form=NewImageForm()
    return render(request,'registration/new_image.html',{"form":form})


def image(request,id):
    try:
        image=Image.objects.get(pk=id)
    except DoesNotExist:
        raise Http404()

    current_user=request.user
    comments=Comment.get_comment(Comment,id)
    if request.method=='POST':
        form =CommentForm(request.POST)
        if form.is_valid():
            comment=form.cleaned_data_data['comments']
            comment=Comment()
            comment.image=image
            comment.user=current_user
            comment.comments=comments
            comment.save()
    else:
        form=CommentForm()
    return render(request,'image.html',{"image":image,"form":form,"comments":comments})

@login_required(login_url='/accounts/login/')
def profilemy(request,username=None):
    if not username:
        username=request.user.username
        images=Image.objects.filter(name=username)
        return render(request,'profilemy.html',locals())

@login_required(login_url='/accounts/login/')
def profile_edit(request):
    current_user=request.user
    if request.method=='POST':
        form=UpdatebioForm(request.POST,request.FILES)
        if form.is_valid():
            image=form.save(commit=False)
            image.user=current_user
            image.save()
        return redirect('homePage')
    else:
        form=UpdatebioForm()
    return render(request,'registration/profile_edit.html',{"form":form})

def user_list(request):
    user_list=User.objects.all()
    context={'user_list':user_list}
    return render(request,'user_list.html',context)

     
# def search_results(request):

#     if 'profile_pic' in request.GET and request.GET["profile_pic"]:
#         search_iterm = request.GET.get("profile_pic")
#         searched = Profile.search(search_iterm)
#         message = f"{search_iterm}"

#         return render(request, 'all_news/search.html',{"message":message,"profile": searched})

#     else:
#         message = "You haven't searched for any term"
#         return render(request, 'all_news/search.html',{"message":message})

def search_results(request):

    if 'article' in request.GET and request.GET["article"]:
        search_term = request.GET.get("article")
        searched_articles = Profile.search(search_term)
        message = f"{search_term}"

        return render(request, 'all_news/search.html',{"message":message,"articles": searched_articles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all_news/search.html',{"message":message})