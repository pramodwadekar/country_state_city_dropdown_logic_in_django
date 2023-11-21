from django.db import models






class Country(models.Model):
    country_name = models.CharField(max_length=50)

    def __str__(self):
        return self.country_name


class State(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True)
    state_name = models.CharField(max_length=50)

    def __str__(self):
        return self.state_name


class City(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE, null=True)
    city_name = models.CharField(max_length=50)

    def __str__(self):
        return self.city_name

class student(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.name
