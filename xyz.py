#import pytest
import sys
# pytest.main()
from tvrenamr.cli.core import rename
#sys.argv.append('-d')
sys.argv.append('--no-cache')
sys.argv.append('-l')
sys.argv.append('DEBUG')
sys.argv.append('--config=tvrconfig.yml')
sys.argv.append('/home/mathew/Videos/Marvels.Agents.of.S.H.I.E.L.D.S04E05.720p.HDTV.X264-DIMENSION[eztv].mkv')
rename()