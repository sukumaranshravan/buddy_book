from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *
from app_buddy.models import *
# Create your views here.

def start_up(request):
    return render(request,'app_admin/start_up.html')

def log_in(request):
    u_name=request.POST['user_name']
    p_word=request.POST['password']
    admin_check=admin_tb.objects.filter(user_name=u_name,password=p_word)
    buddy_check=register_tb.objects.filter(user_name=u_name,password=p_word)
    if admin_check.count()>0:
        messages.add_message(request,messages.INFO,'Admin logged in Successfully')
        return render(request,'app_admin/admin_home.html')
    elif buddy_check.count()>0:
        request.session['yourself']=buddy_check[0].id
        my_id=request.session['yourself']
        got_a_buddy=friend_tb.objects.filter(status=my_id)
        view_post=post_tb.objects.filter()
        if got_a_buddy.count()>0:
            messages.add_message(request,messages.INFO,f'{u_name} logged in Successfully')    
            return render(request,'app_buddy/my_wall.html',{'key':u_name,'detail':buddy_check,'see':view_post,'me':my_id,'bud_post':got_a_buddy})
        else:
            msg='Make friends to see what they posts'            
            return render(request,'app_buddy/my_wall.html',{'key':u_name,'detail':buddy_check,'alert':msg})

def log_out(request):
    request.session.flush()
    messages.add_message(request,messages.INFO,"Sign Off Successfully.")
    return redirect('start_up')
def register(request):
    return render(request,'app_buddy/register.html')