from django.db import models

class Term(models.Model):
    term_name = models.CharField(max_length=200, verbose_name="Терминнің атауы")
    term_description = models.TextField(verbose_name="Терминнің сипаттамасы")

    def __str__(self):
        return self.term_name

    class Meta:
        ordering = ['term_name']

class Feedback(models.Model):
    name = models.CharField(max_length=100, verbose_name="Сіздің атыңыз")
    message = models.TextField(verbose_name="Хабарлама")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Жөнелту күні")

    def __str__(self):
        return f"Хабарлама {self.name}"

    class Meta:
        verbose_name = "Кері байланыс"
        verbose_name_plural = "Кері байланыс"


class Review(models.Model):
    name = models.CharField(max_length=100, verbose_name="Аты-жөні")
    profession = models.CharField(max_length=100, verbose_name="Кәсібі")
    text = models.TextField(verbose_name="Пікір")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Қосылған уақыты")

    class Meta:
        verbose_name = "Пікір"
        verbose_name_plural = "Пікірлер"
        ordering = ['-created_at']