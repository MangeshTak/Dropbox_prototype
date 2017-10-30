from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from .forms import *
from django.contrib.auth.models import User
from Box.models import *
from django.views.generic import TemplateView,ListView
from django.contrib.auth.decorators import login_required
from DropBox import settings

def user_login(request):

    if request.method == 'POST':
        print(request.user)
        form=Loginform(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            user=authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('in')

                else:
                    return HttpResponse('Disabled account')
            else:
                return render(request, 'accounts/invalid.html')
    else:
        form=Loginform()
        return render(request, 'accounts/login.html', {'form':form})

def user_logout(request):
    logout(request)
    return redirect('login')

def user_in(request):

    if not request.user.is_authenticated:
        return render(request, 'accounts/logout.html')
    else:
            data = user_files.objects.filter(user_uploaded=request.user)
            args = {'data': data}
            return render(request, 'accounts/in.html', args)

def user_upload(request):

    if not request.user.is_authenticated:
        return render(request, 'accounts/logout.html')
    else:
        if request.method == 'POST':
            form_new = Fileupload(request.POST, request.FILES )
            if form_new.is_valid():
                instance = form_new.save(commit=False)
                instance.user_uploaded=request.user
                instance.save()
                return redirect('upload')
        else:
            form_new = Fileupload()
            args = {'form_new': form_new}
            return render(request, 'accounts/upload.html', args)

def user_invalid(request):
    return render(request, 'accounts/invalid.html')

def user_welcome(request):
    return render(request, 'accounts/welcome.html')

def user_register(request):

    if request.method=="POST":
        user_form = UserRegistration(request.POST)

        if user_form.is_valid():
            new_user=user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'accounts/reg_done.html', {'new_user': new_user})
    else:
        user_form=UserRegistration()
        return render(request, 'accounts/register.html',{'user_form':user_form})


def user_reg_done(request):
    return render(request, 'accounts/reg_done.html')


def user_share(request):
    user_data=User.objects.all()
    file_data = user_files.objects.filter(user_uploaded=request.user)
    select_user=request.POST.get('dropdown1')
    select_file=request.POST.get('dropdown2')

    if request.method=="POST":
        user_form = Share_file(request.POST)
        data=share_files(select_user=select_user,select_file=select_file,from_user=request.user)
        data.save()
        return redirect('share')

        if user_form.is_valid():
            new_user=user_form.save(commit=False)
            new_user.save()
            return redirect('share')
            #return render(request, 'accounts/reg_done.html', {'new_user': new_user})
    else:
        user_form=Share_file()
        return render(request, 'accounts/share.html',{'user_form':user_form, 'user_data':user_data, 'file_data':file_data})

def user_delete(request):
    file_data = user_files.objects.filter(user_uploaded=request.user)
    select_user=request.POST.get('dropdown1')

    if request.method=="POST":
        user_form = Share_file(request.POST)
        data=user_files.objects.filter(Filename=select_user)
        data.delete()
        return redirect('delete')

    else:
        user_form=delete_file()
        return render(request, 'accounts/delete.html',{'user_form':user_form, 'file_data':file_data})

def user_files_all(request):

    if not request.user.is_authenticated:
        return render(request, 'accounts/logout.html')
    else:
            data = user_files.objects.filter(user_uploaded=request.user)
            data1 = share_files.objects.filter(select_user=request.user)
            #data2 = user_files.objects.filter(Filename=data1.select_file,user_uploaded=data1.from_user)
            args = {'data': data,'data1':data1}
            return render(request, 'accounts/files.html', args)

def user_profile(request):

    if not request.user.is_authenticated:
        return render(request, 'accounts/logout.html')
    else:
            data = User.objects.filter(username=request.user)
            args = {'data': data}
            return render(request, 'accounts/profile.html', args)
