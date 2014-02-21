#!/usr/bin/python
import os, sys
import site

site.addsitedir("/home/<compte>/.local")

_PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0, _PROJECT_DIR) 
sys.path.insert(0, os.path.dirname(_PROJECT_DIR)) 

_PROJECT_NAME = _PROJECT_DIR.split('/')[-1] 
os.environ['DJANGO_SETTINGS_MODULE'] = "%s.settings.%s" % (_PROJECT_NAME, "staging")

from django.core.servers.fastcgi import runfastcgi 
runfastcgi(method="threaded", daemonize="false")  
