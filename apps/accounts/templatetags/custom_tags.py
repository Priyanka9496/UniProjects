from django import template

register = template.Library()


@register.filter(name='has_group')
def has_group(user, group_name):
    print(f"Checking group for {user.username}")
    return user.groups.filter(name=group_name).exists()
