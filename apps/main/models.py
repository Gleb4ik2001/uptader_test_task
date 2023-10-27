from django.db import models


class ChildrenElement(models.Model):
    title = models.CharField(
        verbose_name='название',
        max_length=100
    )
    slug = models.SlugField(
        verbose_name='URL',
        unique=True,
        db_index=True,
        max_length=255
    )

    def __str__(self) -> str:
        return f'{self.title} | {self.slug}'
    
    class Meta:
        verbose_name = 'дочерний элемент'
        verbose_name_plural = 'дочерние элементы'
        ordering = ('title',)

class MenuItem(models.Model):
    title = models.CharField(
        verbose_name='название',
        max_length=100
    )
    slug = models.SlugField(
        verbose_name='ссылка айтема',
        unique=True,
        db_index=True,
        max_length=255
    )
    children = models.ManyToManyField(
        verbose_name='дочерние элементы',
        to=ChildrenElement,
        null=True,
        blank=True
    )

    def __str__(self) -> str:
        return f'{self.title} | URL: {self.title} | parent: {self.children.values_list()}'
    
    class Meta:
        verbose_name = 'элемент меню'
        verbose_name_plural = 'элементы меню'
        ordering = ('title',)

    
class Menu(models.Model):
    title = models.CharField(
        verbose_name='название меню',
        max_length=100,
        unique=True
    )
    slug = models.SlugField(
        verbose_name='ссылка меню',
        unique=True,
        db_index=True,
        max_length=255,
        default=None
    )
    items  = models.ManyToManyField(
        verbose_name='айтемы',
        to=MenuItem,
        null=False,
        blank=False
    )

    def __str__(self) -> str:
        items_names = self.items.values_list('title',flat=True)
        return f'{self.title} | {items_names}'
    
    class Meta:
        verbose_name = 'меню'
        verbose_name_plural= 'менюшки'
        ordering = ('title',)
