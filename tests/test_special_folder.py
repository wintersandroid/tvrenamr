import os

from .base import BaseTest
import filecmp


class TestSpecialFolder(BaseTest):
    def test_manually_setting_specials_folder_name(self):
        self.tv.debug = True
        args = ('foo', 'Chuck', 0, 'Specials')
        path = os.path.normpath(self.tv._build_organise_path(*args))
        assert path == os.path.normpath('foo/Chuck/Specials')

    def test_non_zero_season(self):
        self.tv.debug = True
        args = ('foo', 'Chuck', 2)
        path = os.path.normpath(self.tv._build_organise_path(*args))
        assert path == os.path.normpath('foo/Chuck/Season 2')

    def test_setting_specials_folder_when_build_path(self):
        self.tv.debug = True

        class File(object):
            name = 'Chuck'
            show_name = 'Chuck'
            season = 0
        path = os.path.normpath(self.tv.build_path(File(), self.files, True, 'Specials'))
        path2 = os.path.normpath(os.path.join(self.files, 'Chuck/Specials/Chuck'));
        assert path == path2
