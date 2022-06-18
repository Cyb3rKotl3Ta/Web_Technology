from django.db import models

class sports_accessories(models.Model):
    category = models.CharField(max_length=255)
    cat_id = models.ForeignKey('category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.category


class category(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    cost = models.BigIntegerField()


    def __str__(self):
        return self.title, self.cost

