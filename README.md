# 需求分建表
### user
```
username
email
password
phone
```
### history 历史提问
```
user
question
created_time

```

### comment 问题反馈

```
user
comment
created_time

```

### suggest 评价和意见
```
user
conmment
created_time
```

### book 知识图谱结果保存

```
title
created_time

```
#PDF --》 TXT
```shell script
先执行 python trans_pdf_to_text.py 获取exam.txt文件
手动删除部分脏数据，exam.txt的开头的目录数据
再执行 python save_to_django.py 把行数据保存的数据库
```
#把数据同步到es中
```
下在es es-head 主要是es
https://blog.csdn.net/mini_panda/article/details/81736277

同步：
	python manage.py rebuild_index
```