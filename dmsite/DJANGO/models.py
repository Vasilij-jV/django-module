from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# определение новой модели Django, `Post`, которая наследуется от `models.Model`
class Post(models.Model):
    # определение набора выбора (`choices`) для поля `status`, который включает в себя возможные значения статуса
    # поста: 'draft' (черновик) и 'published' (опубликованный).
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )
    title = models.CharField(max_length=250)  # определение поля `title` как поле текста (`CharField`) с максимальной
    # длиной 250 символов.

    slug = models.SlugField(max_length=200, unique_for_date='publish')  # определение поля `slug` как поле "slug" с
    # максимальной длиной 200 символов. Также указано, что `slug` должен быть уникален для каждого дня на основе поля
    # `publish`.

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='DJANGO_posts')  # определение поля
    # `author` как внешнего ключа (`ForeignKey`), ссылающегося на модель `User`. Если связанный объект `User` будет
    # удален, все связанные посты также будут удалены (`on_delete=models.CASCADE`). Свойство `related_name` позволяет
    # обращаться к связанным объектам из модели `User` (в данном случае `DJANGO_posts`).

    body = models.TextField()  # определение поля `body` как текстовое поле (`TextField`), которое может хранить длинные
    # тексты.

    publish = models.DateTimeField(default=timezone.now)  # определение поля `publish` как поле даты и времени
    # (`DateTimeField`), с текущим временным шаблоном по умолчанию.

    created = models.DateTimeField(auto_now_add=True)  # определение поля `created` как поля даты и времени
    # (`DateTimeField`), которое будет автоматически установлено в текущее время при создании объекта (`auto_now_add=True`).

    updated = models.DateTimeField(auto_now=True)  # определение поля `updated` как поля даты и времени
    # (`DateTimeField`), которое будет автоматически обновлено в текущее время при каждом изменении объекта (
    # `auto_now=True`).

    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')  # определение поля `status`

    # как поля текста (`CharField`), с максимальной длиной 10 символов, с набором выбора `STATUS_CHOICES` и значением по
    # умолчанию 'draft'.

    #  определение класса `Meta` внутри модели `Post`, который позволяет настроить поведение модели на
    #  уровне метаданных.
    class Meta:
        ordering = ('-publish',)  # установка порядока сортировки объектов модели `Post` по дате публикации в обратном

    # порядке (`-publish`).

    # определение метода `__str__` для модели `Post`, который возвращает строковое представление
    # объекта, обычно используемое в выводе (например, в административной панели Django). Здесь возвращается значение
    # поля `title`.
    def __str__(self):
        return self.title
