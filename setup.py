# py2exe download link: http://sourceforge.net/projects/py2exe/files/py2exe/0.6.9/


from distutils.core import setup
import py2exe , sys, os



sys.argv.append("py2exe")
setup(
    options = {'py2exe': {'bundle_files': 1}},
 
    windows = [{'script': "Grabdoor-Cli.py"}],    
    zipfile = None,
    
)
