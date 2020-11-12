from django import forms
from .models import Route, RouteType, BikeType


class RouteForm(forms.ModelForm):

    class Meta:
        model = Route
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        route_type = RouteType.objects.all()
        route_type_friendly_names = (
            [(r.id, r.get_friendly_name()) for r in route_type])
        bike_type = BikeType.objects.all()
        bike_type_friendly_names = (
            [(b.id, b.get_friendly_name()) for b in bike_type])

        self.fields['route_type'].choices = route_type_friendly_names
        self.fields['bike_type'].choices = bike_type_friendly_names
        for field_name, field in self.fields.items():
            field.widgets.attrs['class'] = (
                'bg-black text-white p-3 rounded-wrapper')
