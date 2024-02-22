from django.db import models
from django.contrib.auth.models import User
from simple_history import register
from simple_history.models import HistoricalRecords

# Create your models here.
class Payment(models.Model):
    created_by = models.ForeignKey(
        User, 
        null=True,
        related_name='payment_creator',
        blank=True, 
        on_delete=models.CASCADE
    )
    updated_by = models.ForeignKey(
        User, 
        null=True, 
        related_name='payment_updater',
        blank=True, 
        on_delete=models.CASCADE
    )
    
    title = models.CharField(max_length=256)
    description = models.CharField(max_length=256, null=True, blank=True)
    transaction_id = models.CharField(max_length=256)
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
        super(Payment, self).save(*args, **kwargs)    

    class Meta:
        ordering = ['id']