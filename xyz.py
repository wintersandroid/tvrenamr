#import pytest
import sys
# pytest.main()
from tvrenamr.cli.core import rename
#sys.argv.append('-d')
sys.argv.append('--no-cache')
sys.argv.append('-l')
sys.argv.append('DEBUG')
sys.argv.append('--config=tvrconfig.yml')
sys.argv.append('/home/mathew/Videos/Lucifer.S01E08.HDTV.x264-LOL[eztv].mp4')
rename()