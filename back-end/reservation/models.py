from django.db import models

from brevity.models import Brevity


class Reservation(models.Model):
    price = models.IntegerField()
    tax = models.IntegerField()
    subtotal = models.IntegerField()
    fees = models.IntegerField()
    total_price = models.IntegerField()
    brevity = models.ForeignKey(Brevity, on_delete=models.CASCADE)

    class Meta:
        db_table = 'reservation'

    def __str__(self):
        return f'[{self.pk}] {self.id}' \
               f'결제내역: {self.price}' \
               f'부가가치세: {self.tax}' \
               f'수수료 붙기 전 총금액: {self.subtotal}' \
               f'여행수수료: {self.fees}' \
               f'총금액: {self.total_price}' \
               f'{self.brevity}'
