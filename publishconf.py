# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

GA_TRACKING_ID = os.environ.get('GOOGLE_ANALYTICS')

# If your site is available via HTTPS, make sure SITEURL begins with https://

SITEURL = 'https://github.com/teenageorge'
RELATIVE_URLS = False

DELETE_OUTPUT_DIRECTORY = True

# GA
GOOGLE_ANALYTICS = GA_TRACKING_ID