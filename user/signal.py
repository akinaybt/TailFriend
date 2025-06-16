from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import *


@receiver(post_save, sender=CustomUser)
def create_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
        print('USER PROFILE HAS BEEN CREATED!')
    if not created:
        if not instance.is_vetworker:
            instance.profile.delete()
            VetClinicUser.objects.create(
                user=instance
            )
            print('Vet clinic user has been created!')