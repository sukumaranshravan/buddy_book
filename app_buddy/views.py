from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
import datetime
# Create your views here.
def registeraction(request):
    f_name=request.POST['first_name']
    l_name=request.POST['last_name']
    gender=request.POST['gender']
    dob=request.POST['dob']
    email=request.POST['email']
    contact=request.POST['phone']
    address=request.POST['address']
    photo=request.FILES['photo']
    u_name=request.POST['user_name']
    p_word=request.POST['password']
    register_me=register_tb(first_name=f_name,last_name=l_name,gender=gender,dob=dob,email=email,phone=contact,address=address,photo=photo,user_name=u_name,password=p_word)
    register_me.save()
    messages.add_message(request,messages.INFO,f"{u_name} has registered Successfully")
    return redirect('start_up')

def post(request):
    my_id=request.session['yourself']
    buddy=register_tb.objects.filter(id=my_id)
    name=buddy[0].user_name
    return render(request,'app_buddy/post.html',{'key':name,'detail':buddy})
def postaction(request):
    my_id=request.session['yourself']
    buddy=register_tb.objects.filter(id=my_id)
    name=buddy[0].user_name
    date=datetime.date.today()
    time=datetime.datetime.now().strftime('%H:%M')
    title=request.POST['title']
    post=request.POST['post']
    image=request.FILES['image']
    my_post=post_tb(title=title,post=post,time=time,date=date,image=image,user_id_id=my_id)
    my_post.save()
    return render(request,'app_buddy/post.html',{'key':name,'detail':buddy})

def home(request):
    my_id=request.session['yourself']
    buddy=register_tb.objects.filter(id=my_id)
    name=buddy[0].user_name
    got_a_buddy=friend_tb.objects.filter(status=my_id)
    total=got_a_buddy.count()
    for i in range(total):
        buddy_id=got_a_buddy[i].request_from_id
        view_post=post_tb.objects.filter() 
        return render(request,'app_buddy/my_wall.html',{'key':name,'detail':buddy,'see':view_post,'bud_post':got_a_buddy})  
    
    
def my_post(request):
    my_id=request.session['yourself']
    buddy=register_tb.objects.filter(id=my_id)
    name=buddy[0].user_name
    view_post=post_tb.objects.filter(user_id_id=my_id)
    return render(request,'app_buddy/my_posts.html',{'key':name,'detail':buddy,'see':view_post})

def find_buddy(request):
    search_word=request.POST['entry']
    buddies=register_tb.objects.filter(first_name__istartswith=search_word) | register_tb.objects.filter(user_name__istartswith=search_word)
    return render(request,'app_buddy/buddies.html',{'key':buddies})
    

def request_for_friendship(request):
    my_id=request.session['yourself']
    friend_id=request.POST['friend_id']
    frnd=friend_tb.objects.filter(request_from_id=my_id,requested_to=friend_id)
    if int(my_id)==int(friend_id):
        messages.add_message(request,messages.INFO,"User and Requested ID is the same")
        return redirect('home')
    elif frnd.count() > 0:
        messages.add_message(request,messages.INFO,"This user is already in your friend list.")
        return redirect('home')
    else:
        action=friend_tb(request_from_id=my_id,requested_to=friend_id)
        action.save()
        return render(request,'app_buddy/friend_request.html')

def friend_request(request):
    my_id=request.session['yourself']
    friends=friend_tb.objects.filter(requested_to=my_id,status='pending') 
    if friends.count()>0:          
        return render(request,'app_buddy/friend_request.html',{'key':friends})
    else:
        messages.add_message(request,messages.INFO,'You have no friend request.')
        return redirect('home')

def accept(request,id):
    my_id=request.session['yourself']
    friend_id=request.POST['user_id']
    friend_tb.objects.filter(id=id).update(status=my_id)
    reciprocate=friend_tb(request_from_id=my_id,requested_to=friend_id,status=friend_id)
    reciprocate.save() # this will automatically make you his friend and him your firend else, he will be in your friend list but you will not appear in his list.
    return redirect('home')

def reject(request,id):
    my_id=request.session['yourself']
    friend_tb.objects.filter(id=id).delete()
    return redirect('home')

def comment(request):
    my_id=request.session['yourself']
    return
def reply(request):
    my_id=request.session['yourself']
    return

def friend_list(request):
    my_id=request.session['yourself']
    my_friends=friend_tb.objects.filter(status=my_id)
    return render(request,'app_buddy/friend_list.html',{'key':my_friends})

def about_me(request):
    return render(request,'app_buddy/about_me.html')