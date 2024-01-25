from django import forms

from catalog.models import Product, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Product
        # fields = '__all__'
        fields = ('product_name', 'product_description', 'product_image', 'category', 'product_price', 'is_published')
        # exclude = ('date_created', 'date_last_modified',)

    def clean_product_name(self):
        cleaned_data = self.cleaned_data['product_name']

        banned_names = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        for banned_name in banned_names:
            if banned_name in cleaned_data:
                raise forms.ValidationError('В названии содержится запрещенное слово')

        return cleaned_data

    def clean_product_description(self):
        cleaned_data = self.cleaned_data['product_description']

        banned_names = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        for banned_name in banned_names:
            if banned_name in cleaned_data:
                raise forms.ValidationError('В описании содержится запрещенное слово')

        return cleaned_data


class VersionForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Version
        fields = '__all__'
        # fields = ('product_name', 'version_number', 'version_name', 'is_active', )
