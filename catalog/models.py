from django.db import models
from django.urls import reverse


# Create your models here.
class MyModelName(models.Model):
    # Model specifications here.

    my_field_name = models.CharField(max_length=20, help_text='Enter field documentation')

    # Metadata
    class Meta:
        ordering = ['-my_field_name']


    # Methods
    def get_absolute_url(self):
        """Returns the URL to access a particular instance of MyMdelName"""

        return reverse('model-detail-view', args=[str(self.id)])
    
    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.my_field_name
# A model can have arbitrary number of fields, of any type - each one represents a column of data that we want to store in 
#  in one of our database tables. Each database record(row) will consist one of each value. i.e.
# my_field_name = models.CharField(max_length=20, help_text='Enter field documentation')