# from django.db import models
# from django.contrib.auth import get_user_model
#
# User = get_user_model()
#
#
# class Commit(models.Model):
#     body = models.TextField()
#     task = models.ForeignKey('Task', on_delete=models.CASCADE)
#     users = models.ForeignKey(User, on_delete=models.CASCADE)
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)
#
#     class Meta:
#         ordering = ('created',)
#
#     def __str__(self):
#         return f"{self.users}'s commit of {self.task}"
#
#
