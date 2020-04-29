from datetime import datetime

# 三方包
from django.db import models
from apps.user.models import UserProfile
from django.contrib.auth.models import AbstractUser


# 
class Question(models.Model):
    question = models.CharField(max_length=50, null=False, blank=False, verbose_name='提问内容')

    user = models.ForeignKey(UserProfile, null=False, blank=False, verbose_name="提问者", related_name="historys",
                             on_delete=models.PROTECT)
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    class Meta:
        verbose_name = '历史提问'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.question


class Answer(models.Model):
    question = models.ForeignKey(Question, null=False, blank=False, verbose_name="回答的提问", related_name="answers",
                                 on_delete=models.PROTECT)
    answer = models.TextField(verbose_name='回答内容')
    user = models.ForeignKey(UserProfile, null=False, blank=False, verbose_name="回答者", related_name="answers",
                             on_delete=models.PROTECT)

    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    class Meta:
        verbose_name = '答案'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.question


class Comment(models.Model):
    comment = models.CharField(max_length=50, null=False, blank=False, verbose_name='反馈内容')

    user = models.ForeignKey(UserProfile, null=False, blank=False, verbose_name="反馈者", related_name="comments",
                             on_delete=models.PROTECT)
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    class Meta:
        verbose_name = '问题反馈'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.comment


class Suggest(models.Model):
    comment = models.ForeignKey(Comment, null=False, blank=False, verbose_name="反馈目标", related_name="suggests",
                                on_delete=models.PROTECT)
    suggest = models.TextField(verbose_name='回复反馈的内容')

    user = models.ForeignKey(UserProfile, null=False, blank=False, verbose_name="反馈者", related_name="suggests",
                             on_delete=models.PROTECT)
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    class Meta:
        verbose_name = '问题的建议'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.suggest
