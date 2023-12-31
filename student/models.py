import random
import string
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    sold = models.BooleanField(default=False)
    num_of_pic = models.PositiveIntegerField(default=0)
    code_parainage = models.CharField(max_length=20, blank=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    parrain = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)
    generated_code = models.BooleanField(default=False)  # Champ pour marquer si le code a été généré

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# Fonction pour générer un code de parrainage aléatoire
def generate_unique_code():
    prefix = 'INFAS2023-'
    code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    unique_code = prefix + code
    if Student.objects.filter(code_parainage=unique_code).exists():
        return generate_unique_code()
    return unique_code

# Utilisation d'un signal pour générer le code de parrainage avant la sauvegarde
@receiver(pre_save, sender=Student)
def generate_student_code(sender, instance, **kwargs):
    if not instance.code_parainage:
        instance.code_parainage = generate_unique_code()

    # Si l'étudiant a un code de parrainage et qu'il n'a pas été généré précédemment
    if instance.code_parainage and not instance.generated_code:
        try:
            parrain = Student.objects.get(code_parainage=instance.code_parainage)
            parrain.num_of_pic += 1  # Ajouter +1 au compteur du parrain
            parrain.generated_code = True  # Marquer que le code a été généré
            parrain.save()
        except Student.DoesNotExist:
            pass

