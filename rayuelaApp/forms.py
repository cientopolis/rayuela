
from django import forms
from rayuelaApp.models.project  import Project
from rayuelaApp.models.badge import  Badge
from rayuelaApp.models.user import User


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