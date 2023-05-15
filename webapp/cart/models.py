from django.db import models

from survey.models import Survey
from template.models import Template


class Cart(models.Model):
    class Meta:
        db_table = "cart"
        verbose_name = "Cart"
        verbose_name_plural = "Carts"

    survey = models.ForeignKey(Survey, verbose_name="설문", on_delete=models.CASCADE, null=False)
    template = models.ForeignKey(Template, verbose_name="템플릿", on_delete=models.CASCADE, null=False)
    quantity = models.IntegerField(verbose_name="템플릿 수량", null=False)

