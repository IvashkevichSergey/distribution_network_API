from django.db import models


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
    name = models.CharField(max_length=100, help_text='название поставщика')
    contacts = models.ManyToManyField(to=Contacts, help_text='контакты', blank=True, null=True)
    products = models.ManyToManyField(to=Products, help_text='продукты', blank=True, null=True)
    provisioner = models.ForeignKey(to='self', on_delete=models.SET_NULL, help_text='поставщик', blank=True, null=True)
    debt = models.DecimalField(max_digits=12, decimal_places=2, help_text='задолженность перед поставщиком', default=0)
    created_at = models.DateTimeField(auto_now_add=True, help_text='дата и время создания')

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'

    def __str__(self):
        return self.name
