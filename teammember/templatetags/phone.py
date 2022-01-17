from django import template
register=template.Library()
#Represntation of Phone number 
@register.filter
def phoneconcatinate(value):
    print(value,"rfgerg")
    return value[:3]+"-"+value[3:6]+"-"+value[6:]
