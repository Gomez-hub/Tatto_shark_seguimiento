from django import forms
from .models import contacto, Iniciarseccion
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


from django import forms

# class LoginForm(forms.Form):
#     username = forms.CharField()
#     password = forms.CharField(widget=forms.PasswordInput)



# class RegistrationForm(forms.Form):
#     username = forms.CharField(max_length=150)
#     email = forms.EmailField()
#     password1 = forms.CharField(widget=forms.PasswordInput)
#     password2 = forms.CharField(widget=forms.PasswordInput)

#     def clean_username(self):
#         username = self.cleaned_data['username']
#         if User.objects.filter(username=username).exists():
#             raise forms.ValidationError("Este nombre de usuario ya está en uso.")
#         return username

#     def clean_email(self):
#         email = self.cleaned_data['email']
#         if User.objects.filter(email=email).exists():
#             raise forms.ValidationError("Este correo electrónico ya está en uso.")
#         return email

#     def clean(self):
#         cleaned_data = super().clean()
#         password1 = cleaned_data.get('password1')
#         password2 = cleaned_data.get('password2')
#         if password1 and password2 and password1 != password2:
#             raise forms.ValidationError("Las contraseñas no coinciden.")


#Contacto
class ContactoForm(forms.ModelForm):
    
	class Meta:
		model = contacto
		# fields = ["name", "Email", "Message"]
		fields = "__all__"
		
	name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
	Email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}))
	Message = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))





