from .models import Deration
from modeltranslation.translator import translator, TranslationOptions






class DTranslation(TranslationOptions):
    fields = ('title','text')


# translator.register(Deration,DTranslation)