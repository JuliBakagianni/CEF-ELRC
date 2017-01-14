import os
import sys

path = '/var/opt/ELRCSHARE'
if path not in sys.path:
 sys.path.insert(0, path)
sys.path.insert(0, '{0}/metashare'.format(path))
sys.path.append('{0}/lib/python2.7/site-packages'.format(path))

os.environ['DJANGO_SETTINGS_MODULE'] = 'metashare.settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()