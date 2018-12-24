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
    userid = models.CharField(max_length=16)
    username = models.CharField(max_length=128)
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

    class Meta:
        db_table = 'web_list'

class test(models.Model):
    web = models.TextField()





























