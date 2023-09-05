from django import forms
from .models import Student

class AddStudentForm(forms.ModelForm):
    code_parain = forms.CharField(max_length=20, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'phone', 'code_parain']
        labels = {
            'first_name': 'Nom',
            'last_name': 'Prénom',
            'phone': 'Numéro de téléphone',
            'code_parain': 'Code de parrainage (facultatif)',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'code_parain': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if len(phone) != 10:
            raise forms.ValidationError('Le numéro de téléphone doit comporter 10 chiffres.')
        return phone

    def clean_code_parain(self):
        code_parain = self.cleaned_data['code_parain']
        if code_parain:
            if not Student.objects.filter(code_parainage=code_parain).exists():
                raise forms.ValidationError('Code de parrainage invalide. Veuillez entrer un code valide.')
        return code_parain
