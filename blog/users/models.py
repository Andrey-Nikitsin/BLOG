from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import pre_save
from django.dispatch.dispatcher import receiver

class Clients(AbstractUser):
    phone = models.CharField(max_length=15, verbose_name='telephone')

    class Meta:
        db_table = 'clients'
        verbose_name = 'client'
        verbose_name_plural = 'Clients'

    def __str__(self):
        return self.username 
        # + " | "  + self.phone 

            

@ receiver(pre_save, sender = Clients)
def hash_passwd(sender, instance, **kwargs):
    if (instance.id is None) or (sender.objects.get(id = instance.id).password != instance.password):
        instance.set_password(instance.password)

