from datetime import datetime

# 三方包
from django.db import models
from django.contrib.auth.models import AbstractUser


# 自定义的包
# 个人信息


class UserProfile(AbstractUser):
    """
    用户数据表
    """
    phone = models.CharField(max_length=30, null=True, blank=True, verbose_name='电话号码') 

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username
