﻿from tokenize import blank_re
from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    title = models.CharField(
        verbose_name='Название',
        max_length=100,
        null=False,
        blank=False
    )
    description = models.TextField(
        verbose_name='Описание',
        max_length=800,
        null=False,
        blank=True,
        default=''
    )
    date_begin = models.DateField(
        verbose_name='Дата начала',
        max_length=10,
        null=False,
        blank=False
    )
    date_end = models.DateField(
        verbose_name='Дата окончания',
        max_length=10,
        default='',
        null=True,
        blank=True
    )
    user = models.ManyToManyField(
        to=User,
        related_name='projects',
        verbose_name = 'Пользователь',
        blank=True
    )


    def __str__(self):
        return f'{self.title}'