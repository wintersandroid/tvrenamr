#import pytest
import sys
# pytest.main()
from tvrenamr.cli.core import rename
#sys.argv.append('-d')
sys.argv.append('--no-cache')
sys.argv.append('-r')
sys.argv.append('-l')
sys.argv.append('DEBUG')
sys.argv.append('--dry-run')
sys.argv.append('--config=tvrconfig.yml')
sys.argv.append('--log-file=tvr.log')
sys.argv.append('--rename-dir=/tmp')
# sys.argv.append('CHANGELOG.rst')
sys.argv.append('the.handmaids.tale.s02e07.internal.1080p.web.h264-bamboozle.mkv')
print (rename())  # pylint: disable=E1120
