from django.db import models

# Create your models here.

# 行业资讯表
class industry_information(models.Model):
    title = models.TextField()
    date = models.CharField(max_length=256)
    origin = models.CharField(max_length=256)
    content = models.TextField()

    class Meta:
        db_table = 'industry_information'

class Announcement(models.Model):
    title = models.TextField()
    date = models.CharField(max_length=256)
    view_number = models.CharField(max_length=16)
    content = models.TextField()

    class Meta:
        db_table = 'Announcement'

class User(models.Model):
    username = models.CharField(max_length=16)
    nickname = models.CharField(max_length=128,default='默认用户')
    password = models.CharField(max_length=128)
    user_icon = models.ImageField(upload_to='icons')

    class Meta:
        db_table = 'user'

class analyse_of_market(models.Model):
        title = models.TextField()
        date = models.CharField(max_length=256)
        origin = models.CharField(max_length=256)
        content = models.TextField()

        class Meta:
            db_table = 'analyse_of_market'

class web_list(models.Model):
    web_name = models.TextField()
    web_url = models.TextField()
    web_type = models.CharField(max_length=32)
    web_icon = models.ImageField(upload_to='web_icon')

    class Meta:
        db_table = 'web_list'

class test(models.Model):
    web = models.TextField()

class web_lists(models.Model):
    web_name = models.TextField()
    web_url = models.TextField()
    web_type = models.CharField(max_length=32)
    web_icon = models.ImageField(upload_to='web_icon',null=True)
    web_info = models.TextField(default=111)

    class Meta:
        db_table = 'web_lists'



























