from django.db.models.signals import post_save
from accounts.models import CustomUser
from django.dispatch import receiver
from dash.models import Students
from django.core.exceptions import ObjectDoesNotExist

@receiver(post_save,sender=CustomUser)
def create_students(sender,instance,created,**kwargs):
    """
    """
    if created:
        Students.objects.create(roll=instance)


@receiver(post_save,sender=CustomUser)
def save_students(sender,instance,created,**kwargs):
    """
    """
    try:
        instance.students.save()
    except ObjectDoesNotExist:
        Students.objects.create(roll=instance)
