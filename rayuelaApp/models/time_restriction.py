from django.db import models
from datetime import datetime
        
class TimeRestriction(models.Model):
    name=models.CharField(blank=False,null=False,max_length=100)
    date_from=models.DateField(blank=True,null=True,max_length=10)
    date_to=models.DateField(blank=True,null=True,max_length=10)
    hour_from=models.CharField(blank=True,null=True,max_length=10)
    hour_to=models.CharField(blank=True,null=True,max_length=10)
    days=models.ManyToManyField('rayuelaApp.day')
    
  
    class Meta:
        verbose_name='TimeRestriction'
        verbose_name_plural="TimesRestrictions"
        db_table='time_restriction'

    def __str__(self):
        return f'{self.name},{self.date_from},{self.date_to},{self.hour_from},{self.hour_to}'  


    def is_valid_time(self,date):  
        return ( date>= (self.date_from.strftime("%Y-%m-%d")+ ' ' + self.hour_from) and date  <= (self.date_to.strftime("%Y-%m-%d") + ' ' + self.hour_to) and self.is_valid_day())
    
    def is_valid_day(self):
        from rayuelaApp.models.day import Day
        return self.days.all().contains(Day.objects.get(id=datetime.today().isoweekday()))
        
        #for day in Day.objects.all():
        #   if day.is_my_day(datetime.today().isoweekday()) 
        #       return True
        #return False        
        


    def add_days(self,days):       
        from rayuelaApp.models.day import Day
        for day in Day.objects.all():
            if days.get(day.get_id())=='on':
                self.days.add(day)
        self.save()
    
    def add_hours(self,bool,hf,ht):
        if bool !='on':
            self.hour_from = '00:00'
            self.hour_to = '23:59'
        else:
            self.hour_from = hf
            self.hour_to = ht
        self.save()
        
    def get_id(self):
        return self.id
