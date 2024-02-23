from django.db import models
from django.contrib.auth.models import User
from simple_history import register
from simple_history.models import HistoricalRecords

# Create your models here.
class Category(models.Model):
    created_by = models.ForeignKey(
        User, 
        null=True,
        related_name='category_creator',
        blank=True, 
        on_delete=models.CASCADE
    )
    updated_by = models.ForeignKey(
        User, 
        null=True, 
        related_name='category_updater',
        blank=True, 
        on_delete=models.CASCADE
    )
    
    title = models.CharField(max_length=256)
    description = models.CharField(max_length=256)
    archive = models.BooleanField(default=False)
    
    history = HistoricalRecords()
    
    #Timestamps
    date_created = models.DateTimeField(auto_created=True, auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        if self.title:
            return "{} | {}".format(self.id, self.title)
        else:
            return "{}".format(self.id)

    def save(self, *args, **kwargs):
        super(Category, self).save(*args, **kwargs)    

    class Meta:
        ordering = ['id']