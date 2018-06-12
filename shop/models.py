from django.db import models

class Bicycle(models.Model):
    model = models.CharField(max_length=200)
    marca = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=7, decimal_places=2)
    imagen = models.ImageField(upload_to='img', max_length=200, default='img/bici.png')
    video = models.FileField(upload_to='vid', max_length=200, default='vid/sample.mp4')
    stock = models.IntegerField(default=0)

    def __unicode__(self):
        return self.marca + ', ' + self.modelo
