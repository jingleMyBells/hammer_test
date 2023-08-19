from django.contrib.auth import get_user_model

from referrals.models import Referring


User = get_user_model()


def create_referring(user, code):
    referrer = User.objects.filter(referrer_code=code).first()
    if referrer:
        Referring.objects.create(referrer=referrer, referral=user)
        user.invitation_code = referrer.referrer_code
        user.save()
        return True
    return False


def check_referring(user):
    referring = Referring.objects.select_related(
        'referrer',
    ).filter(referral=user)
    if referring.exists():
        return referring.first().referrer.referrer_code
