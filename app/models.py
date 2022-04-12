from django.db import models

# Create your models here.

class Upload(models.Model):
    upload_file = models.FileField()    
    upload_date = models.DateTimeField(auto_now_add =True)

class Tabel(models.Model):
    no=models.IntegerField(null=True)
    tanggal=models.CharField(max_length=11, null=True)
    data=models.IntegerField(null=True)
    ket1=models.CharField(max_length=5, null=True, default="")
    ket2=models.CharField(max_length=5, null=True, default="")
    peramalan=models.IntegerField(null=True, default=0)
    akurasi=models.CharField(max_length=5, null=True)
class Rata(models.Model):
    rata=models.CharField(max_length=5, null=True)

class Defuzzyfikasi(models.Model):
    cr=models.CharField(max_length=5, null=True)
    ns=models.CharField(max_length=30, null=True)
    peram=models.IntegerField(null=True, default=0)

class KelasInt(models.Model):
    ki=models.CharField(max_length=5, null=True)
    batasatas=models.IntegerField(null=True, default=0)
    batasbawah=models.IntegerField(null=True, default=0)
    midpoint=models.IntegerField(null=True, default=0)



class Dmaksmin(models.Model):
    
    d1=models.IntegerField()
    d2= models.IntegerField()
    def __str__(self):
        return self.d1

