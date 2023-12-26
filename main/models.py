from django.db import models

# Create your models here.
class Club(models.Model):

    name=models.CharField('Название клуба',max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Клуб'
        verbose_name_plural='Клубы'

class Ring(models.Model):

    breed=models.CharField('Порода',max_length=100)

    def __str__(self):
        return self.breed

    class Meta:
        verbose_name='Ринг'
        verbose_name_plural='Ринги'

class Expert(models.Model):

    full_name=models.CharField('ФИО',max_length=100, db_index=True)
    club_id=models.ForeignKey('Club', on_delete=models.PROTECT)
    ring_id = models.ForeignKey('Ring', on_delete=models.PROTECT)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name='Эксперт'
        verbose_name_plural='Эксперты'

class Participant(models.Model):
    name = models.CharField('Кличка', max_length=100, db_index=True)
    club_id = models.ForeignKey('Club', on_delete=models.PROTECT, verbose_name='Клуб')
    ring_id = models.ForeignKey('Ring', on_delete=models.PROTECT, verbose_name='Ринг')
    age=models.IntegerField('Возраст')
    mother=models.CharField('Мать', max_length=200)
    father = models.CharField('Отец', max_length=200)
    medal=models.CharField('Медаль', max_length=100, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Участник'
        verbose_name_plural = 'Участники'