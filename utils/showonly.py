'''
Created on Aug 2, 2011

From http://djangosnippets.org/snippets/1185/
Adapted to include support for choice/select widgets
'''
from django import forms

class ShowOnly(forms.Widget):
    """
    Show only the data do NOT have a input field
    """
    input_type = 'hidden'

    def render(self, name, value, attrs=None):
        from django.utils.safestring import mark_safe
        from django.utils.encoding import force_unicode
        if value is None: 
            value = ''
        final_attrs = self.build_attrs(attrs, type=self.input_type, name=name)
        # Fall back, updated if we find a better match
        showtext = force_unicode(value)
        if final_attrs.get('showtext'):
            showtext = final_attrs.get('showtext')
            del final_attrs['showtext']
        elif self.choices: # If we have choices, try to find the one matching the value
            choice_list = [v[1] for i, v in enumerate(self.choices) if v[0] == value]
            if len(choice_list) > 0:
                showtext = force_unicode(choice_list[0])
        if value != '':
            # Only add the 'value' attribute if a value is non-empty.
            value = force_unicode(value)
            final_attrs['value'] = force_unicode(value)
        return mark_safe(u'<input%s />%s' % (forms.util.flatatt(final_attrs),showtext))