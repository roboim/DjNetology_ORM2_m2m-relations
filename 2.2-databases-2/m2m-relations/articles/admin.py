from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag, Scope


class RelationInlineFormset(BaseInlineFormSet):
    def clean(self):
        main_tag_qty = 0
        for form in self.forms:
            # В form.cleaned_data будет словарь с данными
            # каждой отдельной формы, которые вы можете проверить
            print(form.cleaned_data['is_main'])
            if form.cleaned_data['is_main'] is True:
                main_tag_qty += 1
            #     # if (main_tag_qty == 0):
            #     #     main_tag_name = form.cleaned_data['tag']
            # вызовом исключения ValidationError можно указать админке о наличие ошибки
            # таким образом объект не будет сохранен,
            # а пользователю выведется соответствующее сообщение об ошибке
            print(main_tag_qty)
        if main_tag_qty != 1:
            raise ValidationError('Ошибка формы (проверьте количество главных тегов)')
        return super().clean()  # вызываем базовый код переопределяемого метода


class RelationInline(admin.TabularInline):
    model = Scope
    formset = RelationInlineFormset
    extra = 1


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    # pass
    list_display = ['title', 'text', 'published_at', 'image']
    inlines = [RelationInline]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    # pass
    list_display = ['name']
    inlines = [RelationInline]

