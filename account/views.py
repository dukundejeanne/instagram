from django.shortcuts import render,redirect,get_object_or_404
from .models import Image,Profile,Comment
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from .forms import NewImageForm,UpdatebioForm,CommentForm
from .email import send_welcome_email
from .forms import NewsLetterForm

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
    if request.GET.get('search_iterm'):
        pictures=Image.search(request.GET.get('search_iterm'))
    else:
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
    return render(request,'index.html',{'pictures':pictures,'letterForm':form})

def image(request,id):
    try:
        image=Image.objects.get(pk=id)
    except DoesNotExist:
        raise Http404()
    current_user=request.user
    comments=Comment.get_comment(Comment, id)
    if request.method== 'POST':
        form=CommentForm(request.POST )
        if form.is_valid():
            comments=form.cleaned_data['comment']
            comment=Comment()
            comment=image=image
            comment.user=current_user
            comment.comment=comment
            comment.save()
    else:
        form=CommentForm()
        return render(request,'image.html',{'image':image,'form':form,'comments':comments})

@login_required(login_url='/accounts/login/')
def new_image(request):
    current_user=request.user
    if request.method=='POST':
        if form.is_valid():
            image=form.save(commit=False)
            image.user=current_user
            image.save()
        return redirect('homePage')
    else:
        form = NewImageForm()
    return render(request,'registration/new_image.html',{"form":form})


# view a image by id
def user_list(request):
    user_list=User.objects.all()
    context={'user_list':user_list}
    return render(request,'user_list.html',context)


@login_required(login_url='/accounts/login/')
def edit_profile(request):
    current_user=request.user
    if request.method=='POST':
        form=UpdatebioForm(request.POST,request.FILES)
        if form.is_valid():
            image=form.save(commit=False)
            image.user=current_user
            image.save()
        return redirect('homePage')
    else:
        form = UpdatebioForm()
    return render(request,'registration/edit_profile.html',{"form":form})

@login_required(login_url='/accounts/login/')
def individual_profile_page(request,username=None):
    if not username:
        username=request.user.username
    images=Image.objects.filter(user_id=username)
    return render(request,'registration/user_image_list.html',{'images':images,'username':username})

def search_users(request):
    if 'user' in request.GET and request.GET['user']:
        search_iterm=request.GET.get('user')
        searched_users=Profile.search_users(search_iterm)
        message=f"{search_iterm}"

        return render(request,'search.html',{"message":message,"profiles":searched_users})
    else:
        message ="no person correspond"
        return render(request,'search.html',{"message":message})

@login_required(login_url='/accounts/login/')
def myprofile(request,username=None):
    if not username:
        username=request.user.username
    images=Image.objects.filter(user_id=username)
    return render(request,'myprofile.html',locals())

# search images
def search_image(request):
    if 'image' in request.GET and request.GET['image']:
        search_iterm=request.GET.get('image')
        searched_images=Image.search_image(search_iterm)
        message=f"{search_iterm}"

        return render(request,'search.html',{"message":message,"pictures":searched_images})
    else:
        message ="no images"
        return render(request,'search.html',{"message":message})

@login_required(login_url='/accounts/login/')
def individual_profile_page(request,username):
    print(username)
    if not username:
        username=request.user.username
    images=Image.objects.filter(user_id=username)
    user=request.user
    profile=Profile.objects.get(user=user)
    userf=User.objects.get(pk=username)
    if userf:
        print('user found')
        profile=Profile.objects.get(user=userf)
    else:
        print('no such user')
    return render(request,'registration/user_image_list.html',{'images':images,'username':username,'profile':profile,'user':user})

