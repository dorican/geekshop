from django import forms
from django.forms import ModelForm
from callbackapp.models import CallbackApplication


class CallbackForm(ModelForm):
    class Meta:
        model = CallbackApplication
        fields = ('name', 'phone',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'callback_name'})
        self.fields['phone'].widget.attrs.update({'class': 'callback_phone'})



    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     for field_name, field in self.fields.items():
    #         field.widget.attrs['class'] = 'form_fields'
    #         field.help_text = ''

    # name = forms.CharField(widget=forms.TextInput(attrs={'class': 'callback-form-field'}))
    # phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'callback-form-field-phone'}))

