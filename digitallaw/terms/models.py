from django.db import models

class Term(models.Model):
    term_name = models.CharField(max_length=200, verbose_name="Название термина")
    term_description = models.TextField(verbose_name="Описание термина")

    def __str__(self):
        return self.term_name

    class Meta:
        ordering = ['term_name']

class Feedback(models.Model):
    name = models.CharField(max_length=100, verbose_name="Ваше имя")
    message = models.TextField(verbose_name="Сообщение")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата отправки")

    def __str__(self):
        return f"Сообщение от {self.name}"

    class Meta:
        verbose_name = "обратная связь"
        verbose_name_plural = "Обратная связь"