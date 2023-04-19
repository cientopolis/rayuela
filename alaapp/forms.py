
from django import forms
from alaapp.models.project  import Project
from alaapp.models.badge import  Badge
from alaapp.models.user import User


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ["image"]
        
    def procces(self,path_image):
        if self.is_valid():    
            self.save()

class BadgeForm(forms.ModelForm):
    class Meta:
        model = Badge
        fields = ["image"]

    def procces(self,path_image):
        if self.is_valid():    
            self.save()

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['profile_image']

    def procces(self,path_image):
        if self.is_valid():    
            self.save()