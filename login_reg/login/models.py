from django.db import models

# Create your models here.

class RegisterUser(models.Model):
    #邮箱字段
    reg_mail = models.CharField(max_length=16, blank=False)
    #密码字段
    reg_pwd = models.CharField(max_length=16, blank=False)