from django.db import models

class sports_accessories(models.Model):
    title = models.CharField(max_length=255)
    weight = models.DecimalField(max_digits=7,decimal_places=2)
    cat = models.ForeignKey('category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title


class category(models.Model):
    category = models.CharField(max_length=255, db_index=True)

    def __str__(self):
        return self.category


