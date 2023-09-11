from datetime import timezone
from django.db import models
from django.utils import timezone
# Create your models here.

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('Unesite username')
        #email = self.normalize_email(email)
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    #kada pokrenemo naredbu manage.py createsuper user ovo se pokreće
    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, password, **extra_fields)
    
class DomZdravlja(models.Model):
    naziv_doma_zdravlja = models.CharField(max_length=40)
    adresa_doma_zdravlja = models.CharField(max_length=30)
    opis_doma_zdravlja = models.TextField()
    
    def __str__(self):
        return self.naziv_doma_zdravlja
    

class Doktor(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(blank=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    #ako se obriše dom_zdravlja, npr ruši se zgrada, postavi doktoru dom_zdravlja na null (nema smisla brisat doktora)
    dom_zdravlja = models.ForeignKey(DomZdravlja, default=1, on_delete=models.SET_NULL, null=True)

    # Add custom fields here
    opis_doktora = models.TextField()
    iskustvo_doktora = models.TextField()


    specijalizacija_doktora_izbori = [
        ("Anesteziolog", "Anesteziolog"),
        ("Infektolog", "Infektolog"),
        ("Kardiolog", "Kardiolog"),
        ("Pedijatar", "Pedijatar"),
        ("Reumatolog", "Reumatolog"),
        ("Pulmolog", "Pulmolog"),
        ("Urolog", "Urolog"),
        ("Onkolog", "Onkolog")
    ]
    #vazno da je default inace dobijem error da id ne postoji
    specijalizacija_doktora = models.CharField(max_length=30, choices=specijalizacija_doktora_izbori, default="AN")

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Narudzba(models.Model):
    odabir_vremena = (
        ('jutro', "Jutro"),
        ('večer', "Večer")
    )
    ime_pacijenta = models.CharField(max_length=30)
    prezime_pacijenta = models.CharField(max_length=30)
    telefon_pacijenta = models.CharField(max_length=20)
    email_pacijenta = models.EmailField()
    #ako se izbriše doktor izbriše se i narudžba
    doktor = models.ForeignKey(Doktor, on_delete=models.CASCADE)
    datum_pregleda = models.DateField(default=timezone.now)
    vrijeme_pregleda = models.CharField(choices=odabir_vremena, max_length=10)
    # vrijeme_pregelda = models.TimeField(
    #     default='08:00',
    #     blank=False,
    #     null=False
    # )
    simptomi = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Doktor {self.doktor.first_name} {self.doktor.last_name} - Pacijent {self.ime_pacijenta} {self.prezime_pacijenta}"
    
class MedicinskaSestra(models.Model):
    ime_sestre = models.CharField(max_length=30)
    prezime_sestre = models.CharField(max_length=30)
    godine_staza_sestre = models.IntegerField()
    #ako se obriše doktor, npr da otkaz, postavi medicinskoj sestri doktor na null (nema smisla brisat sestru)
    doktor = models.ForeignKey(Doktor, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return f"{self.ime_sestre} {self.prezime_sestre}" 