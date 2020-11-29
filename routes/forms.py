from django import forms
from .widgets import CustomClearableFileInput
from .models import Route, RouteType, BikeType


class RouteForm(forms.ModelForm):

    class Meta:
        model = Route
        exclude = ('rating', 'image_url', 'user', 'save_route')

    image = forms.ImageField(
        label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        """ Getting foreign key friendly names and setting paceholder names """
        super().__init__(*args, **kwargs)
        route_type = RouteType.objects.all()
        route_type_friendly_names = (
            [(r.id, r.get_friendly_name()) for r in route_type])
        bike_type = BikeType.objects.all()
        bike_type_friendly_names = (
            [(b.id, b.get_friendly_name()) for b in bike_type])
        placeholders = {
            'name': 'Route Name',
            'description': 'Route Description',
            'bike_type': 'Bike Type',
            'length': 'Length (min. 5km)',
            'route_type': 'Route Type',
            'map_url': 'Google Map Code',
            'country': 'Country',
            'image': 'Route Image',
        }

        self.fields['name'].widget.attrs['autofocus'] = True
        self.fields['route_type'].choices = route_type_friendly_names
        self.fields['bike_type'].choices = bike_type_friendly_names
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False
