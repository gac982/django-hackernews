from django.contrib import admin

# Register your models here.
from app.api.models import News

# con esta linea mmodificamos el titulo que se muestra en el panel administraivo de djangp
admin.site.site_header = "Panel Administrativo Personalizado"

# Aqui registramos los models que importamos en la parte superior
@admin.register(News)
# aqui vamos a configurar que se vean las opciones junto a la presgunta que estan asociadas
class NewsAdmin(admin.ModelAdmin):
	readonly_fields = ('votes',)
	list_display = ('title', 'created')