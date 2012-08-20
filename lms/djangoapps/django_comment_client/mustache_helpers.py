import django.core.urlresolvers as urlresolvers
import urllib
import sys
import inspect

def pluralize(content, text):
    num, word = text.split(' ')
    if int(num or '0') >= 2:
        return num + ' ' + word + 's'
    else:
        return num + ' ' + word

def url_for_user(content, user_id):
    return urlresolvers.reverse('django_comment_client.forum.views.user_profile', args=[content['course_id'], user_id])

def url_for_tags(content, tags): # assume that attribute 'tags' is in the format u'a, b, c'
    return urlresolvers.reverse('django_comment_client.forum.views.forum_form_discussion', args=[content['course_id']]) + '?' + urllib.urlencode({'tags': tags})

def close_thread_text(content):
    if content.get('closed'):
        return 'Re-open thread'
    else:
        return 'Close thread'

current_module = sys.modules[__name__]
all_functions = inspect.getmembers(current_module, inspect.isfunction)

mustache_helpers = {k: v for k, v in all_functions if not k.startswith('_')}
