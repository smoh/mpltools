""" Functions related to I/O """

import urllib
import os, errno
from urllib2 import urlopen, URLError, HTTPError

__all__ = ['mkdir_p', 'downloadfile']

def mkdir_p(path):
    """
    Mimic mkdir -p
    """
    try:
        os.makedirs(path)
    except OSError as exc: # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else: raise

def downloadfile(url, savename=None, prefix=None):
    """
    Download a file from url

    url : url
    savename : target filename (default=basename of url)
    prefix : directory prefix (created if not there)
    """
    if not savename:
        savename = os.path.basename(url)
    if not prefix:
        prefix = './'

    mkdir_p(prefix)
    try:
        f = urlopen(url)
        localname = prefix + '/' + savename
        if os.path.isfile(localname):
            pass
        else:
            # Open our local file for writing
            with open(localname, "wb") as local_file:
                local_file.write(f.read())
                local_file.close()
        return 1
    #handle errors
    except HTTPError, e:
        print "HTTP Error:", e.code, url
        return 0
    except URLError, e:
        print "URL Error:", e.reason, url
        return 0
