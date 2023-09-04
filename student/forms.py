from django import forms
from .models import Student

class AddStudentForm(forms.ModelForm):
    code_parainage = forms.CharField(max_length=20, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'phone', 'code_parainage']
        labels = {
            'first_name': 'Nom',
            'last_name': 'Prénom',
            'phone': 'Numéro de téléphone',
            'code_parainage': 'Code de parrainage (facultatif)',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'code_parainage': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if len(phone) != 10:
            raise forms.ValidationError('Le numéro de téléphone doit comporter 10 chiffres.')
        return phone

    def clean_code_parainage(self):
        code_parainage = self.cleaned_data['code_parainage']
        if code_parainage:
            if not Student.objects.filter(code_parainage=code_parainage).exists():
                raise forms.ValidationError('Code de parrainage invalide. Veuillez entrer un code valide.')
        return code_parainage