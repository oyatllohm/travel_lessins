from django.db import models

# Create your models here.


class Deration(models.Model):
    title = models.CharField(max_length= 55 )
    image = models.ImageField(upload_to='image')
    text  = models.TextField(blank=True)
    duration = models.PositiveIntegerField(default=0)
    reg_date = models.DateField(auto_now_add=True)
    pirice = models.PositiveIntegerField(verbose_name="UZS",default=100)
    pirice_usd = models.PositiveIntegerField(verbose_name="USD",default=100)
    leave = models.DateField(blank=True,null=True)
    bakc_to = models.DateField(blank=True,null=True)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Yo'nalish"
        verbose_name_plural = "Yo'nalishlar"


class News(models.Model):
    title = models.CharField(max_length= 55 )
    image = models.ImageField(upload_to='image')
    text  = models.TextField(blank=True)
    reg_date =  models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "yangilik"
        verbose_name_plural = "yangiliklar"


class Cantact(models.Model):
    name = models.CharField(max_length=124)
    email = models.EmailField()
    subject = models.CharField(max_length=150)
    text = models.TextField()

    def __str__(self):
        return self.name
