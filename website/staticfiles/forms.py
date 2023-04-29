from django import forms
from django.contrib.auth.models import User

class ContactMe(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your name',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Your email',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    description = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Describe how we can help',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))

    def save(self):
        user = User.objects.create_user(
            username=self.cleaned_data['email'],
            password=self.cleaned_data['email'] # use email as password
        )
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['name']
        user.save()




# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User


# class ContactMe(UserCreationForm):

#     class Meta:
#         model = User
#         fields = ('name', 'email', 'description','password1', 'password2')


#     name = forms.CharField(widget=forms.TextInput(attrs={
#         'placeholder': 'Your name',
#         'class': 'w-full py-4 px-6 rounded-xl'
#     }))
#     email = forms.CharField(widget=forms.EmailInput(attrs={
#         'placeholder': 'Your email',
#         'class': 'w-full py-4 px-6 rounded-xl'
#     }))
#     description = forms.CharField(widget=forms.TextInput(attrs={
#         'placeholder': 'Describe how we can help',
#         'class': 'w-full py-4 px-6 rounded-xl'
#     }))
#     def __init__(self, *args, **kwargs):
#         super(ContactMe, self).__init__(*args, **kwargs)
#         del self.fields['password1']
#         del self.fields['password2']
