from django.contrib import admin
from .models import Settings, NavbarModel, Footer, WorksSectionModel, WorkModel,\
    WorkImageModel, AboutModel, AboutImageModel, ContactModel, ContactSocNetModel, \
    ContactAddressModel, NavbarGuestModel


admin.site.register(Settings)
admin.site.register(NavbarModel)
admin.site.register(Footer)
admin.site.register(WorksSectionModel)
admin.site.register(WorkModel)
admin.site.register(WorkImageModel)
admin.site.register(AboutModel)
admin.site.register(AboutImageModel)
admin.site.register(ContactModel)
admin.site.register(ContactAddressModel)
admin.site.register(ContactSocNetModel)
admin.site.register(NavbarGuestModel)




