#!F:\Project\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'bashplotlib==0.6.5','console_scripts','hist'
__requires__ = 'bashplotlib==0.6.5'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('bashplotlib==0.6.5', 'console_scripts', 'hist')()
    )
