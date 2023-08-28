from django import forms

class ImageWidget(forms.Widget):

    def render(self, name, value, attrs=None, renderer=None):
        # Define how the widget should be rendered
        # 'name' is the name of the form field
        # 'value' is the current value of the form field
        # 'attrs' are additional HTML attributes
        control = (f'<div><table><tr><td>'
               f'<img id="{name}-id" src="{value}" alt="preview" /><td><td rowspan="2"><a href="https://images.google.com">Find images</a></td></tr>'
               f'<tr><td><input type="url" placeholder="http://www.example.com" id="{name}-url" name="{name}-url" value="{value}" /></td></tr>'
               f'</table></div>')
        return control

