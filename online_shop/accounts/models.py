from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, AbstractUser, User
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.validators import UnicodeUsernameValidator

from .manager import MyUserManager
from core.models import BaseModel

# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):

    username_validator = UnicodeUsernameValidator()
    phone = models.CharField(max_length=12)
    image = models.ImageField(upload_to="users/images", null=True, blank=True)

    username = models.CharField(
        _("username"),
        max_length=150,
        unique=True,
        help_text=_(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        validators=[username_validator],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )
    first_name = models.CharField(_("first name"), max_length=150, blank=True)
    last_name = models.CharField(_("last name"), max_length=150, blank=True)
    email = models.EmailField(_("email address"), blank=True)
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)

    objects = MyUserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["phone"]

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)

class Address(BaseModel):
    state_choices =[('Ahvaz','Ahvaz'), ('Arak','Arak'), ('Ardabil','Ardabil'), ('Bandar Abbas','Bandar Abbas'), ('Birjand','Birjand'), ('Bojnord', 'Bojnord'), ('Bushehr','Bushehr'), ('Gorgan',  'Gorgan'), ('Hamadan', 'Hamadan'), ('Ilam', 'Ilam'), ('Isfahan', 'Isfahan'), ('Karaj', 'Karaj'), ('Kerman', 'Kerman'), ('Kermanshah', 'Kermanshah'), ('Khorramabad' 'Khorramabad'), ('Mashhad', 'Mashhad'), ('Qazvin', 'Qazvin'), ('Qom','Qom'), ('Rasht', 'Rasht'), ('Sanandaj', 'Rasht'), ('Sari', 'Sari'), ('Semnan', 'Semnan'), ('Shahr-e Kord', 'Shahr-e Kord'),( 'Shiraz', 'Shiraz'), ('Tabriz', 'Tabriz'), ('Tehran', 'Tehran'), ('Urmia', 'Urmia'), ('Yasuj', 'Yasuj'), ('Yazd', 'Yazd'), ('Zahedan', 'Zahedan'),('Zanjan', 'Zanjan')]
    title = models.CharField(max_length=100)
    state = models.CharField(max_length=50, choices=state_choices)
    city = models.CharField(max_length=50)
    # city = models.CharField(max_length=50, choices=city_choices)
    zip_code = models.PositiveIntegerField()
    detailed_adress = models.TextField()

    