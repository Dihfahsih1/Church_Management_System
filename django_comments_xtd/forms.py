from django import forms
from django.apps import apps
from django.utils.translation import gettext_lazy as _

from django_comments.forms import CommentForm

from django_comments_xtd.conf import settings
from django_comments_xtd.models import TmpXtdComment


class XtdCommentForm(CommentForm):
    reply_to = forms.IntegerField(required=True, initial=0,
                                  widget=forms.HiddenInput())

    def __init__(self, *args, **kwargs):
        comment = kwargs.pop("comment", None)
        if comment:
            initial = kwargs.pop("initial", {})
            initial.update({"reply_to": comment.pk})
            kwargs["initial"] = initial
            followup_suffix = ('_%d' % comment.pk)
        else:
            followup_suffix = ''
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['name'] = forms.CharField(
            label=_("Name"),
            widget=forms.TextInput(attrs={'placeholder': _('Your Name'),
                                          'class': 'form-control'}))
   
        self.fields['comment'] = forms.CharField(
            widget=forms.Textarea(attrs={'placeholder': _('Your comment'),
                                         'class': 'form-control'}),
            max_length=settings.COMMENT_MAX_LENGTH)
        self.fields['comment'].widget.attrs.pop('cols')
        self.fields['comment'].widget.attrs.pop('rows')

    def get_comment_model(self):
        return TmpXtdComment

    def get_comment_create_data(self, site_id=None):
        data = super(CommentForm, self).get_comment_create_data(site_id=site_id)
        ctype = data.get('content_type')
        object_pk = data.get('object_pk')
        model = apps.get_model(ctype.app_label, ctype.model)
        target = model._default_manager.get(pk=object_pk)
        data.update({'thread_id': 0, 'level': 0, 'order': 1,
                     'parent_id': self.cleaned_data['reply_to'],
                     'content_object': target})
        return data