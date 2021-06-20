from django.db import models


class BitCoinData(models.Model):
    class Meta:
        db_table = 'bit_coin_data'

    product_code = models.CharField(
        null=False,
        max_length=100
    )

    state = models.CharField(
        null=False,
        max_length=100
    )

    open_price = models.IntegerField(
        null=False
    )

    high_price = models.IntegerField(
        null=False
    )

    low_price = models.IntegerField(
        null=False
    )

    close_price = models.IntegerField(
        null=False
    )

    truncate_hour_time = models.DateTimeField(
        null=True
    )

    truncate_minute_time = models.DateTimeField(
        null=True
    )

    truncate_second_time = models.DateTimeField(
        null=True
    )

    unixtime = models.CharField(
        max_length=20,
        null=True
    )

    created_time = models.DateTimeField(
        null=False,
        auto_now=True
    )

    update_time = models.DateTimeField(
        null=False,
        auto_now_add=True
    )

    is_delete = models.BooleanField(
        default=False
    )
