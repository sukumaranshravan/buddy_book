from django.contrib import admin
from app_admin.models import *
from app_buddy.models import *
# Register your models here.
admin.site.register(register_tb)
admin.site.register(post_tb)
admin.site.register(friend_tb)
