from django.core.exceptions import ValidationError
from django.db import models
from rest_framework import status, exceptions
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError as ValErr


class Contacts(models.Model):
    """Модель контактов для поставщиков"""
    email = models.EmailField(help_text='email', null=True, blank=True)
    country = models.CharField(max_length=25, help_text='страна')
    city = models.CharField(max_length=25, help_text='город')
    street = models.CharField(max_length=50, help_text='улица')
    house_number = models.PositiveIntegerField(help_text='номер дома', null=True, blank=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'


class Products(models.Model):
    """Модель продукции, выпускаемой поставщиками"""
    name = models.CharField(max_length=100, help_text='название продукта')
    model = models.CharField(max_length=50, help_text='модель')
    release_date = models.DateField(help_text='дата выхода на рынок', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Supplier(models.Model):
    """Модель поставщиков продукции"""

    ENTERPRISE_TYPE_CHOICES = [
        ('factory', 'завод'),
        ('retail', 'розничная сеть'),
        ('self-employed', 'индивидуальный предприниматель')
        ]

    name = models.CharField(
        max_length=100, help_text='название поставщика'
    )
    enterprise_type = models.CharField(
        choices=ENTERPRISE_TYPE_CHOICES, max_length=13,
        help_text='тип предприятия', default='self-employed'
    )
    contacts = models.ManyToManyField(
        to=Contacts, help_text='контакты', blank=True
    )
    products = models.ManyToManyField(
        to=Products, help_text='продукты', blank=True
    )
    provisioner = models.ForeignKey(
        to='self', on_delete=models.SET_NULL, help_text='поставщик',
        blank=True, null=True
    )
    debt = models.DecimalField(
        max_digits=12, decimal_places=2,
        help_text='задолженность перед поставщиком', default=0
    )
    created_at = models.DateTimeField(
        auto_now_add=True, help_text='дата и время создания'
    )

    def clean(self, *args, **kwargs):
        """Задаём условия для валидации данных"""
        if not self.provisioner and self.debt:
            raise ValidationError(
                'Для того чтобы установить задолженность в поле "debt" '
                'необходимо заполнить поле поставщик "provisioner" либо '
                'оставьте 0 в поле "debt"')
        if self.enterprise_type == 'factory' and self.provisioner:
            raise ValidationError(
                'Завод не может иметь поставщика, '
                'оставьте поле "provisioner" незаполненным')

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        """Формируем корректный Response для API на случай ValidationError"""
        try:
            self.clean()
            return super().save(force_insert=False, force_update=False, using=None, update_fields=None)
        except ValidationError as err:
            raise exceptions.ValidationError(
                {'Ошибка': err.message}
            )

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'

    def __str__(self):
        return self.name
