# forms.py
from django import forms

class SqlQueryForm(forms.Form):
    query = forms.CharField(widget=forms.Textarea(attrs={
                'rows': 10,  # Increase the number of rows (height)
                'cols': 10,  # Increase the number of columns (width)
                'style': 'width:70%; font-size:16px;',  # Additional styling if needed
            }), label="Enter SQL Query", required=True)
