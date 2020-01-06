from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.forms import forms, HiddenInput, ModelForm
from authapp.models import ShopUser
from mainapp.models import ProductCategory, Product


class ShopUserAdminCreateForm(UserCreationForm):
    class Meta:
        model = ShopUser
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2', 'email', 'age', 'avatar')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form_fields'
            field.help_text = ''

    def clean_age(self):
        data = self.cleaned_data['age']
        if data < 18:
            raise forms.ValidationError("Лицам моложе 18-ти лет запрещено регистрироваться на сайте!")
        return data

    def clean_avatar(self):
        data = self.cleaned_data['avatar']
        if len(data) > (300 * 1024):
            raise forms.ValidationError("Размер аватарки не может превышать 300К")
        return data


class ShopUserAdminUpdateForm(UserChangeForm):
    class Meta:
        model = ShopUser
        fields = ('username', 'first_name', 'last_name',
                  'password', 'email', 'age', 'avatar', 'is_superuser', 'is_active')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form_fields'
            field.help_text = ''
            if field_name == 'password':
                field.widget = HiddenInput()

    def clean_age(self):
        data = self.cleaned_data['age']
        if data < 18:
            raise forms.ValidationError("Лицам моложе 18-ти лет запрещено регистрироваться на сайте!")
        return data


class ProductCategoryAdminUpdateForm(ModelForm):
    class Meta:
        model = ProductCategory
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form_fields'


class ProductAdminUpdateForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form_fields'