from datetime import datetime

# 三方包
from django.db import models
from django.contrib.auth.models import AbstractUser


# 自定义的包
# 个人信息


class Book(models.Model):
     
  

    title = models.CharField(max_length=300, null=False, blank=False, verbose_name='分词内容')
    
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")


    class Meta:
        verbose_name = '分词内容'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
