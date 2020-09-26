from django.db import models

class Commit(models.Model):
    """ Commit describes the characteristics of the database.
        body contains the input commit message.
    """
    body = models.CharField(max_length=500)
    SAR_nonSAR = models.CharField(max_length=10)
    intention = models.CharField(max_length=20)
    type_of_SAR = models.CharField(max_length=20)
