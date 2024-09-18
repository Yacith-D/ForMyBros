from django.db import models

# # Create your models here.
# class Book(models.Model):
#     id = models.AutoField(primary_key=True)
#     author = models.CharField(max_length=255)
#     title = models.TextField()
#     year = models.CharField(max_length=255)
#     created_at = models.DateTimeField(auto_now_add=True)
#     update_at = models.DateTimeField(auto_now=True)
#     @classmethod
#     def class_method(cls):
#         pass
    
#     def instance_method():
    
#     Book.my_method()
        
    

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.CharField(max_length=255)
    title = models.TextField()
    year = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True),