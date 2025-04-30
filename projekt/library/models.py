from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone

class Vyvojar(models.Model):
    jmeno = models.CharField(max_length=100, verbose_name="Jméno vývojáře")

    class Meta:
        verbose_name = "Vývojář"
        verbose_name_plural = "Vývojáři"

    def __str__(self):
        return self.jmeno


class Zanr(models.Model):
    nazev = models.CharField(max_length=50, unique=True, verbose_name="Žánr")

    class Meta:
        verbose_name = "Žánr"
        verbose_name_plural = "Žánry"

    def __str__(self):
        return self.nazev


class Hra(models.Model):
    nazev = models.CharField(max_length=100, verbose_name="Název hry")
    vyvojar = models.ForeignKey(Vyvojar, on_delete=models.SET_NULL, null=True, verbose_name="Vývojář")
    datum_vydani = models.DateField(null=True, blank=True, verbose_name="Datum vydání")
    hodnoceni = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True, verbose_name="Hodnocení")
    obrazek = models.ImageField(upload_to="hry_obrazky/", blank=True, null=True, verbose_name="Obrázek hry")
    popis = models.TextField(blank=True, verbose_name="Popis")
    zanry = models.ManyToManyField(Zanr, related_name="hry", verbose_name="Žánry")

    class Meta:
        verbose_name = "Hra"
        verbose_name_plural = "Hry"
        ordering = ['-datum_vydani']

    def __str__(self):
        return self.nazev


class Uzivatel(models.Model):
    jmeno = models.CharField(max_length=100, verbose_name="Jméno uživatele")
    email = models.EmailField(unique=True, verbose_name="Email")
    heslo = models.CharField(max_length=255, verbose_name="Heslo")
    datum_registrace = models.DateTimeField(default=timezone.now, verbose_name="Datum registrace")

    class Meta:
        verbose_name = "Uživatel"
        verbose_name_plural = "Uživatelé"

    def __str__(self):
        return self.jmeno


class Recenze(models.Model):
    hra = models.ForeignKey(Hra, on_delete=models.CASCADE, related_name="recenze", verbose_name="Hra")
    uzivatel = models.ForeignKey(Uzivatel, on_delete=models.CASCADE, related_name="recenze", verbose_name="Uživatel")
    text = models.TextField(verbose_name="Text recenze")
    hodnoceni = models.PositiveSmallIntegerField(verbose_name="Hodnocení")
    datum = models.DateTimeField(default=timezone.now, verbose_name="Datum recenze")

    class Meta:
        verbose_name = "Recenze"
        verbose_name_plural = "Recenze"
        ordering = ['-datum']

    def __str__(self):
        return f"{self.uzivatel} - {self.hra} ({self.hodnoceni}/10)"
