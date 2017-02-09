from registration.forms import RegistrationForm

from register.models import MyUser


class MyCustomUserForm(RegistrationForm):
    class Meta:
        model = MyUser
        fields = '__all__'