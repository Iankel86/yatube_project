from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


# Create your models here.
class Post(models.Model):
    text = models.TextField()

    # Тип поля: DateTimeField, для хранения даты и времени;
    # параметр auto_now_add определяет, что в поле будет автоматически
    # подставлено время и дата создания новой записи
    pub_date = models.DateTimeField(auto_now_add=True)

    author = models.ForeignKey(
                                                   User,
                                                   on_delete=models.CASCADE,
                                                   related_name='posts'
                                                   )

    group = models.ForeignKey(
                                                   'Group',
                                                   blank=True,
                                                   null=True,
                                                   on_delete=models.SET_NULL,
                                                   related_name='posts'
                                                   )


class Group(models.Model):
    title = models.TextField()
    slug = models.SlugField(unique=True)
    description = models.TextField()

    def _str_(self) -> str:
        return self.title
