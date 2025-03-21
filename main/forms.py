from django import forms
from .models import Reservations

class ReservationForm(forms.ModelForm):
    date = forms.DateField(
        input_formats=['%d/%m/%Y', '%d-%m-%Y', '%d.%m.%Y'],
        widget=forms.DateInput(attrs={'class': 'form-control', 'id': 'date', 'placeholder': 'Date', 'data-rule': 'minlen:4', 'data-msg': 'Please enter at least 4 chars'}))

    def clean_name(self):
        user_name = self.data['name'].strip()
        return user_name.upper()

    class Meta:
        model = Reservations
        fields = ('name', 'email', 'phone', 'date', 'time', 'number_guests', 'message')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control',
                                           'name': 'name',
                                           'id': 'name',
                                           'placeholder': 'Your name',
                                           'data - rule': 'minlen:4',
                                           'data - msg': 'Please enter at least 4 chars'
                                            }),

            'email': forms.EmailInput(attrs={'class': 'form-control', 'id': 'email', 'name': 'email',
                                             'placeholder': 'Your Email', 'data-rule': 'email',
                                             'data-msg': 'Please enter a valid email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'id': 'phone', 'placeholder': '+38xxxxxxxxxx'}),
            # 'date': forms.DateInput(attrs={'class': 'form-control', 'id': 'date', 'placeholder': 'Date', 'data-rule': 'minlen:4', 'data-msg': 'Please enter at least 4 chars'}),
            'time': forms.TimeInput(attrs={'class': 'form-control', 'id': 'time', 'placeholder': 'Your Time' }),
            'number_guests': forms.NumberInput(attrs={'class': 'form-control', 'id': "people", 'placeholder': "# of people", 'data-rule': "minlen:1", 'data-msg': "Please enter at least 1 chars"}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'name': "message", 'rows': "5", 'placeholder': "Message"})
        }