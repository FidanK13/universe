from django.db.models.signals import post_save
# from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import WorkModel , CustomUser
from django.conf import settings
from django.core.mail import send_mail

@receiver(post_save, sender=WorkModel)
def work(instance, created, **kwargs):
    if created:
        print("cretaion success")
        send_mail('subject',
                  'message',
                  'fidan.kamranli95@gmail.com',
                  ['azura.sadiq.stardust@gmail.com',],
                  fail_silently=False)

@receiver(post_save, sender=CustomUser)
def product(instance, created, **kwargs):
    if created:
        print("cretaion success")
        send_mail('new user',
                  'pliz activate',
                  'fidan.kamranli95@gmail.com',
                  ['azura.sadiq.stardust@gmail.com',],
                  fail_silently=False)


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        login(request, user)
        return redirect('login')
    else:
        return render(request, "Backend/accounts/activation_fail.html")