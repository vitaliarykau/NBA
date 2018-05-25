from django.contrib.auth.models import User
from django import forms



class RegistrationForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput,
                                label='Password', help_text='Enter a password. Min length is 6 symbols',
                                min_length=6)
    password2 = forms.CharField(widget=forms.PasswordInput,
                                label='Repeat a password', help_text='Confirm your password',
                                min_length=6)

    error_messages = {
        'password_mismatch': "The two password fields didn't match.",
        'username_exists': "This username is already exist"
    }
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def clean_password2(self):
        if (self.cleaned_data['password1'] != self.cleaned_data['password2']):
            raise forms.ValidationError("Passwords do not match")
        return self.cleaned_data['password1']

    def new_username(self):
        if User.objects.get(username=self.cleaned_data['username']).exist():
            raise forms.ValidationError("This username is already exist")
        return self.cleaned_data['username']

    def save(self, commit=True):
        user = super().save(commit=False)
        print("Im in save")
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


