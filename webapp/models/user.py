from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length=20)
    mail = models.CharField(max_length=20 , default = '')
class CustomUserAdmin(models.Model):
    inlines = (User, )
    list_display = ('mail', 'first_name', 'last_name')
    list_select_related = ('User', )