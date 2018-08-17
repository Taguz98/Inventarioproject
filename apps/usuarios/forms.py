from django import form

class LoginForm(forms.ModelForm):
    username = forms.CharField(
        widget= forms.TextInput(
            attrs={'class':'usuario'}),
            label='Usuario')

    password = forms.CharField(
        widget= forms.TextInput(
            attrs={'class':'password'}),
            label='Contraseña')

        class Meta:
            model = User
            fields = ['username', 'password']
