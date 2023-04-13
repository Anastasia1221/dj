from django import template

register = template.Library()

bad_words = ['for', 'article']


@register.filter()
def censor(value):

    mylst = value.split()

    for i in range(len(mylst)):
        if mylst[i].lower() in bad_words:
            mylst[i] = "*"*len(mylst[i])

    return ' '.join(mylst)
