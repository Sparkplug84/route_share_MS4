from django.contrib import admin
from .models import Route, BikeType, RouteType

# Register your models here.


class RouteAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'bike_type',
        'length',
        'route_type',
        'map_url',
        'country',
        'rating',
        'image',
    )

    ordering = ('bike_type',)


class BikeTypeAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class RouteTypeAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Route, RouteAdmin)


admin.site.register(BikeType, BikeTypeAdmin)


admin.site.register(RouteType, RouteTypeAdmin)