from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
import datetime
from django.http import HttpResponse
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
    view_comment=comment_tb.objects.filter()
    if got_a_buddy.count() >0:
        view_post=post_tb.objects.filter().order_by('-date') 
        return render(request,'app_buddy/my_wall.html',{'key':name,'detail':buddy,'see':view_post,'bud_post':got_a_buddy,'comment':view_comment})  
    else:
        msg='Make friends to see what they posts'
        return render(request,'app_buddy/my_wall.html',{'key':name,'detail':buddy,'alert':msg})  
    
def my_post(request):
    my_id=request.session['yourself']
    buddy=register_tb.objects.filter(id=my_id)
    name=buddy[0].user_name
    view_post=post_tb.objects.filter(user_id_id=my_id)
    post_id=view_post[0].id
    liked_users=liked_by_tb.objects.filter(post_id_id=post_id)
    view_comment=comment_tb.objects.filter()
    return render(request,'app_buddy/my_posts.html',{'key':name,'detail':buddy,'see':view_post,'comment':view_comment,'likers':liked_users})

def delete_post(request,id):    
    post_tb.objects.filter(id=id).delete()
    comment_tb.objects.filter(post_id_id=id).delete()
    messages.add_message(request,messages.INFO,"Selected Post and all comments associated with it has been deleted.")
    return redirect('my_post')


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

def unfriend(request,id):
    my_id=request.session['yourself']
    get_buddy=friend_tb.objects.filter(id=id,status=my_id)
    bud_status_in_my_request=get_buddy[0].request_from_id
    friend_tb.objects.filter(id=id,status=my_id).delete()
    friend_tb.objects.filter(request_from_id=my_id,status=bud_status_in_my_request).delete()
    return redirect('friend_list')

def comment(request,id):
    my_id=request.session['yourself']
    post=post_tb.objects.filter(id=id)
    return render(request,'app_buddy/comment.html',{'say':post})
def commentaction(request):
    my_id=request.session['yourself']
    comment=request.POST['comment']
    post_id=request.POST['id']
    comment=comment_tb(comment=comment,post_id_id=post_id,user_id_id=my_id)
    comment.save()
    notify=notify=notifications_tb(post_id_id=post_id,user_id_id=my_id,comment='commented')
    notify.save()
    return redirect('home')

def reply(request,id):
    post=post_tb.objects.filter(id=id)
    return render(request,'app_buddy/comment.html',{'say':post})

def friend_list(request):
    my_id=request.session['yourself']
    my_friends=friend_tb.objects.filter(status=my_id)
    return render(request,'app_buddy/friend_list.html',{'key':my_friends})

def my_photos(request):
    my_id=request.session['yourself']
    pic=register_tb.objects.filter(id=my_id)
    view_post=post_tb.objects.filter(user_id_id=my_id)
    return render(request,'app_buddy/my_photos.html',{'see':view_post,'pro_pic':pic})

def about_me(request):
    my_id=request.session['yourself']
    my_details=register_tb.objects.filter(id=my_id)
    return render(request,'app_buddy/about_me.html',{'key':my_details})

def settings(request):
    my_id=request.session['yourself']
    my_details=register_tb.objects.filter(id=my_id)
    return render(request,'app_buddy/settings.html',{'key':my_details})
def change_photo(request):
    my_id=request.session['yourself']
    new_pic=request.FILES['photo']
    register_tb.objects.filter(id=my_id).update(photo=new_pic)
    messages.add_message(request,messages.INFO,'Profile Picture has been changed.')
    # following code is only to let your buddies know about your new photo
    date=datetime.date.today()
    time=datetime.datetime.now().strftime('%H:%M')
    title='Profile Picture Updated'
    post='see my new profile picture'    
    my_pic_change=post_tb(title=title,post=post,time=time,date=date,image=new_pic,user_id_id=my_id)
    my_pic_change.save()
    return redirect('settings')


def likes(request,id):
    my_id=request.session['yourself']    
    check_my_like=liked_by_tb.objects.filter(user_id_id=my_id,post_id_id=id)
    if check_my_like.count()==0:
        my_like=liked_by_tb(user_id_id=my_id,post_id_id=id)
        my_like.save()
        post_likes=post_tb.objects.filter(id=id)
        like_count=post_likes[0].likes
        post_tb.objects.filter(id=id).update(likes=like_count+1)
        notify=notifications_tb(post_id_id=id,user_id_id=my_id,like='liked')
        notify.save()
        return redirect('home')
    elif check_my_like.count()>0:
        liked_by_tb.objects.filter(user_id_id=my_id,post_id_id=id).delete()
        notifications_tb.objects.filter(user_id_id=my_id,post_id_id=id).delete()
        post_likes=post_tb.objects.filter(id=id)
        like_count=post_likes[0].likes
        post_tb.objects.filter(id=id).update(likes=like_count-1)
        return redirect('home')
    
def likers(request,id):
    post=post_tb.objects.filter(id=id)
    user=register_tb.objects.filter(id=id)
    post_id=post[0].id
    liker=liked_by_tb.objects.filter(post_id_id=post_id)
    return render(request,'app_buddy/liked_by.html',{'key':liker,'buddy':user})

def buddy(request):
    search_word=request.POST['this']
    buddy_details=register_tb.objects.filter(first_name__istartswith=search_word) | register_tb.objects.filter(user_name__istartswith=search_word)
    return render(request,'app_buddy/buddies.html',{'key':buddy_details})

def notifications(request,id):
    notify=notifications_tb.objects.filter(post_id_id=id).order_by('-id')
    msg="You have No Notifications"
    if notify.count()>0:
        return render(request,'app_buddy/notifications.html',{'ntfy':notify})
    else:
        return render(request,'app_buddy/notifications.html',{'show':msg})
    
def edit_comment(request,id):
    my_id=request.session['yourself']
    comment=comment_tb.objects.filter(user_id_id=my_id,id=id)
    return render(request,'app_buddy/edit_comment.html',{'key':comment})

def update_comment(request):
    cmnt_id=request.POST['id']
    updated_comment=request.POST['comment']
    try:
        comment_tb.objects.filter(id=cmnt_id).update(comment=updated_comment)
        return redirect('home')
    except:
        messages.add_message(request,messages.INFO,"No Changes Made")
        return redirect('home')