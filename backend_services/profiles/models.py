from django.db import models
from django.contrib.auth.models import User
from simple_history import register
from simple_history.models import HistoricalRecords

register(User)
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_by = models.ForeignKey(
        User, 
        null=True,
        related_name='profile_creator',
        blank=True, 
        on_delete=models.CASCADE
    )
    updated_by = models.ForeignKey(
        User, 
        null=True, 
        related_name='profile_updater',
        blank=True, 
        on_delete=models.CASCADE
    )
    
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    full_name = models.CharField(max_length=256)
    role = models.CharField(max_length=20)
    archive = models.BooleanField(default=False)
    
    history = HistoricalRecords()
    
    #Timestamps
    date_created = models.DateTimeField(auto_created=True, auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        if self.first_name and self.last_name:
            return "{} | {} | {}".format(self.id, self.first_name, self.last_name)
        else:
            return "{}".format(self.id)

    def save(self, *args, **kwargs):
        self.full_name = self.first_name + " " + self.last_name
        super(Profile, self).save(*args, **kwargs)    

    class Meta:
        ordering = ['id']