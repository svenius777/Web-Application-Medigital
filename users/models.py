from django.db import models

from zdravstveni_sustav_app.models import Doktor

# Create your models here.
class profil(models.Model):
    #user field ima 1 to 1 relationship sa User modelom
    #cascade znaci ako je korisnik obrisan izbrisi i profil
    doktor = models.OneToOneField(Doktor, on_delete=models.CASCADE)
    #upload_to je direktorij gdje se slike uploadaju
    #default.jpg je default image za svakog korisnika
    image = models.ImageField(default='default.png', upload_to='profilne_slike')

    #dunder objekt
    def __str__(self):
        return f'{self.doktor.username} Profile'