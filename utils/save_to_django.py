# coding:utf-8
"""
当pdf转化成text后 下一步就是把数据保存到数据库中,完成了知识图谱的整理入库
"""

# 用脚本独立使用django的model，相关文档地址：  https://docs.djangoproject.com/en/1.11/topics/settings/
import sys
import os

# 获取当前文件的路径的目录，即：data/文件夹
# 这里不用os.path.insert的里理由是不像setting.py文件下BASE_DIR可以参考
# 获取当前文件的文件夹，即db_tools/
pwd = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
pwd = pwd
print(pwd)
sys.path.append(pwd)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djqa.settings")
# 初始化呢django
import django

django.setup()

from apps.book.models import Book

f = open("exam.txt", mode="r", encoding="utf-8")
for i in f.readlines():
    tmp = i.strip().replace("\n", '').replace('\t', '').replace('\r', '')
    try:
        int(tmp)
    except Exception:
        print(tmp)
        Book.objects.create(title=tmp)
print(Book.objects.all())
