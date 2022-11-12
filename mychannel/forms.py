# import pickle

from django import forms
# from django.core.exceptions import ValidationError
from django.forms import Form, fields, widgets
# from nltk import tokenize
# from nltk.tokenize import WordPunctTokenizer
# from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

from mychannel.choices import ChannelCategories
from mychannel.models import UserChannel


class UpdateChannelForm(forms.ModelForm):
    class Meta:
        model = UserChannel
        fields = ['name', 'description', 'banner']
        widgets = {
            'banner': widgets.FileInput()
        }


class CustomizationForm(forms.ModelForm):
    class Meta:
        model = UserChannel
        fields = ['name', 'description']


class UploadVideoForm(Form):
    title = fields.CharField(max_length=100)
    description = fields.CharField(max_length=400)
    category = fields.ChoiceField(choices=ChannelCategories.choices)
    age_restriction = fields.BooleanField()
    allow_comments = fields.BooleanField()
    video = fields.FileField(allow_empty_file=False, required=True)

    def clean(self):
        cleaned_fields = super().clean()

        # This section will attempt to classify the
        # level of offensivness contained in the video's
        # title and description.
        # In other words, if the video's title or description
        # contains offensive words, it cannot be uploaded to
        # to the website
        # with open('', mode='rb') as m:
        #     model = pickle.load(m)

        #     tokenizer = WordPunctTokenizer()
        #     tokenizer.tokenize(cleaned_fields['title'])

        #     count_vectorizer = CountVectorizer()
        #     count_result = count_vectorizer.fit(
        #         [cleaned_fields['title'], cleaned_fields['description']]
        #     )
        #     vectorizer = TfidfVectorizer()
        #     matrix = vectorizer.fit(count_result)

        #     prediction = model.predict(matrix)
        #     if prediction[-1] < .5:
        #         raise ValidationError('The title or description are no valid')

        # # Check whether the category is within the
        # # channel catgories
        # categories = [choice[-1] for choice in ChannelCategories.choices]
        # if cleaned_fields['category'] not in categories:
        #     raise ValidationError('The category is not a valid one')
        return cleaned_fields
