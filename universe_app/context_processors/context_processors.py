from universe_app.models import NavbarModel, Settings, Footer, NavbarGuestModel

def context(request):
    context={}
    settings_queryset = Settings.objects.all().first()
    navbar_queryset = NavbarModel.objects.all()
    footer_queryset = Footer.objects.all()
    guest_queryset = NavbarGuestModel.objects.all()
    context['settings_queryset']= settings_queryset
    context['navbar_queryset']= navbar_queryset
    context['footer_queryset']= footer_queryset
    context['guest_queryset'] = guest_queryset
    return context #render(request, 'index.html', context)