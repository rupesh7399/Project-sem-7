from django.db import models
from  django.contrib.auth.models import User
from django.conf import settings
from datetime import*
from django_pandas.managers import DataFrameManager
        
class weather_data(models.Model):
    DATE = models.DateField()
    ET = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    EP = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    BSS = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    RF = models.FloatField()
    WD = models.CharField( max_length=50)
    WD1 = models.CharField( max_length=50)
    WS = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    DT1= models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    WT1= models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    DT2= models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    WT2= models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    MAXT= models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    MINT= models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    RH11= models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    RH22= models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    VP11= models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    VP22= models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    CLOUDM= models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    CLOUDE= models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    SOIL1= models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    SOIL2= models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    SOIL3= models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    SOIL4= models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    SOIL5= models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    SOIL6= models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    MinTtest= models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    MaxTtest1= models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    MaxTtest2= models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    
    objects = DataFrameManager()
    objects = models.Manager()
    pdobjects = DataFrameManager()

    class Meta:
        db_table = "weather_data"

  
    
    # def __str__(self):
        # return 'date:{0} ET:{1} EP:{2} BSS:{3} RF:{4} WD:{5} WD1:{6} WS:{7}	DT1:{8}	WT1:{9}	DT2:{10} WT2:{11} MAXT:{12}	MINT:{13} RH11:{14}	RH22:{15} VP11:{16}	VP22:{17} CLOUDM:{18} CLOUDE:{19} SOIL1:{20} SOIL2:{21}	SOIL3:{22} SOIL4:{23} SOIL5:{24} SOIL6:{25} MinTtest:{26} MaxTtest1:{27}	MaxTtest2:{27}'.format(self.date, self.ET, self.EP,	self.BSS, self.RF,	self.WD	self.WD1,	self.WS,self.DT1,self.WT1,self.DT2,self.WT2, self.MAXT,	self.MINT,	self.RH11,	self.RH22	self.VP11,	self.VP22,self.CLOUDM,	self.CLOUDE,	self.SOIL1,	self.SOIL2,	self.SOIL3,	self.SOIL4,	self.SOIL5, self.SOIL6, self.MinTtest, self.MaxTtest1,	self.MaxTtest2)

# https://github.com/vinpalace/inventory_management/blob/master/inventory_management_system/inventory/models.py
class university(models.Model):
    u_id = models.AutoField(primary_key=True)
    u_name = models.CharField(max_length=50)

    class Meta:
        db_table = "university"

class collage(models.Model):
    c_id = models.AutoField(primary_key=True)
    u_id = models.ForeignKey(university,'on_delete')
    c_name = models.CharField(max_length=50)

    class Meta:
        db_table = "collage"

class u_profile(models.Model):
    u_p_id = models.AutoField(primary_key=True)
    u_id = models.ForeignKey(university,'on_delete')
    c_id = models.ForeignKey(collage,'on_delete')
    user = models.ForeignKey(settings.AUTH_USER_MODEL,'on_delete')
    gender = models.CharField(max_length=10)
    phone = models.IntegerField()

    class Meta:
        db_table = "u_profile"





