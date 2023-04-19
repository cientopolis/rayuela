from django.db import models
from alaapp.models.user  import User
from werkzeug.security import check_password_hash
class Token(models.Model):
    user_id=models.ForeignKey(User,null=True,blank=False,on_delete=models.DO_NOTHING)
    token=models.CharField(max_length=30,blank=False,null=False)

    def __str__(self):
        return f'{self.user_id},{self.token}'

    class Meta:
        verbose_name='Token'
        verbose_name_plural="Tokens"
        db_table='token'

    def get_user(self):
        return self.user_id

    def user_equal(self,user_id):
        if check_password_hash(user_id[15:len(user_id)],str(self.get_user().get_id())):           
            return self.get_user().get_id()
        return None