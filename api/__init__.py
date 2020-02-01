'''
rest_framework reverse 补丁
'''
from rest_framework import relations


original_reverse = relations.reverse
def hack_reverse(alias, **kwargs):
    namespace = kwargs['request'].resolver_match.namespace
    if bool(namespace):
        name = "%s:%s" % (namespace, alias)
        return original_reverse(name, **kwargs)
    else:
        return original_reverse(alias, **kwargs)
relations.reverse = hack_reverse


original_resolve = relations.resolve
def hack_resolve(path, urlconf=None):
    match = original_resolve(path, urlconf=urlconf)
    if bool(match.app_name):
        preffix = match.app_name + ':'
        if match.view_name.startswith(preffix):
            match.view_name = match.view_name[len(preffix):]
    return match
relations.resolve = hack_resolve