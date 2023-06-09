from django.db import models


class Car(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    available = models.IntegerField(default=0)
    image = models.CharField(max_length=1000, blank=True, default='')

    def cars_left(self) -> int:
        ordered = Order.objects.filter(car=self).count()
        purchased = Purchase.objects.filter(car=self).count()
        return purchased - ordered

    def __str__(self):
        return f"{self.name}, available: {self.available}"


class Order(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=15)
    status = models.CharField(max_length=100, default="created")

    def __str__(self):
        return f"{self.id}, {self.car}, {self.name}, phone: {self.phone}, " \
               f"status: {self.status}"


class Purchase(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.car}, purchased date: {self.date}"

