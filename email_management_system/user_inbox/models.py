from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
   pass


class UserTickets(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   subject = models.CharField(max_length=500)
   sender_email = models.CharField(max_length=500)
   status_choices = (
      (1, 'Open'),
      (2, 'Closed'),
      (3, 'Progress'),
   )
   status = models.CharField(max_length=300, choices=status_choices)
   priorities = (
      (1, 'Low'),
      (2, 'Medium'),
      (3, 'High')
   )
   priority = models.CharField(max_length=300, choices=priorities)
   email_send_time = models.DateField(("Email Send Time"))
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)
   
   class Meta:
      db_table = "user_tickets"

   