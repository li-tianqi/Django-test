#!/usr/bin/env python3
# coding=utf-8

from django import forms

class AddForm(forms.Form):
    a = forms.IntegerField()
    b = forms.IntegerField()


class AddForm_def(forms.Form):
    def_bw = forms.IntegerField()
