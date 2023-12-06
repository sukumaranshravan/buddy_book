from django.db import models

# Create your models here.
class register_tb(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    gender=models.CharField(max_length=20)
    dob=models.CharField(max_length=20)
    email=models.CharField(max_length=20)
    phone=models.CharField(max_length=20)
    address=models.CharField(max_length=20)
    photo=models.FileField()
    user_name=models.CharField(max_length=20)
    password=models.CharField(max_length=20)

class post_tb(models.Model):
    user_id=models.ForeignKey(register_tb,on_delete=models.CASCADE)
    title=models.CharField(max_length=20)
    post=models.CharField(max_length=20)
    time=models.CharField(max_length=20)
    date=models.CharField(max_length=20)
    image=models.FileField(default=None)
    status=models.CharField(max_length=20,default='public')
    filter_status=models.CharField(max_length=20,default='unblocked')
    likes=models.PositiveIntegerField(default=0)
    dislikes=models.PositiveIntegerField(default=0)


class friend_tb(models.Model):
    requested_to=models.CharField(max_length=20,default=0)
    request_from=models.ForeignKey(register_tb,on_delete=models.CASCADE,default=0)
    status=models.CharField(max_length=20,default='pending')

class comment_tb(models.Model):
    user_id=models.ForeignKey(register_tb,on_delete=models.CASCADE)
    comment=models.CharField(max_length=20)
    post_id=models.ForeignKey(post_tb,on_delete=models.CASCADE,default=0)

class reply_tb(models.Model):
    user_id=models.ForeignKey(register_tb,on_delete=models.CASCADE)
    reply=models.CharField(max_length=20)
    post_id=models.ForeignKey(comment_tb,on_delete=models.CASCADE,default=0)

class liked_by_tb(models.Model):
    user_id=models.ForeignKey(register_tb,on_delete=models.CASCADE)
    post_id=models.ForeignKey(post_tb,on_delete=models.CASCADE)

class notifications_tb(models.Model):
    user_id=models.ForeignKey(register_tb,on_delete=models.CASCADE)
    post_id=models.ForeignKey(post_tb,on_delete=models.CASCADE)
    comment=models.CharField(max_length=20,default=0)
    like=models.CharField(max_length=20,default=0)
    
    