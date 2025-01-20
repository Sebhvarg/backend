from django.db import models

class MainModel(models.Model):
        
    class Meta:
        permissions = [
            ("index_viewer", "Can show to index view (function-based)"),
        ]

# Create your models here.
