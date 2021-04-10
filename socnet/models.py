from django.db import models


class Users(models.Model):
    name = models.TextField(null=True, blank=True, verbose_name='Имя', max_length=20)
    sname = models.TextField(null=True, blank=True, verbose_name='Фамилия', max_length=30)
    birthday = models.DateField(db_index=True, verbose_name='День рождения')

    def __str__(self):
        return f'{self.name} {self.sname}'

    class Meta:
        verbose_name_plural = 'Пользователи'
        verbose_name = 'Пользователь'
        ordering = ['name']


class Messages(models.Model):
    message = models.TextField(null=True, blank=True, verbose_name='Сообщение', max_length=500)
    user = models.ForeignKey(Users, null=True, on_delete=models.CASCADE, verbose_name='Пользователь')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')

    class Meta:
        verbose_name_plural = 'Сообщения'
        verbose_name = 'Сообщения'
        ordering = ['-published']
