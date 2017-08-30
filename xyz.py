#import pytest
import sys
# pytest.main()
from tvrenamr.cli.core import rename
#sys.argv.append('-d')
sys.argv.append('--no-cache')
sys.argv.append('-l')
sys.argv.append('DEBUG')
sys.argv.append('--dry-run')
sys.argv.append('--config=tvrconfig.yml')
sys.argv.append('--log-file=tvr.log')
sys.argv.append('Lucifer.S01E08.HDTV.x264-LOL[eztv].mp4')
rename()  # pylint: disable=E1120
