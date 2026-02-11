import unittest
from unittest.mock import MagicMock
from jb1_zoomies import setup

class TestExtension(unittest.TestCase):
    def test_setup(self):
        app = MagicMock()
        # Mock config to avoid errors when add_config_value is called
        app.config = MagicMock()
        
        result = setup(app)
        
        # Check if version is returned
        self.assertEqual(result['version'], '0.2')
        
        # Check if some config values were added
        self.assertTrue(app.add_config_value.called)
        self.assertTrue(app.connect.called)

    def test_on_builder_inited(self):
        from jb1_zoomies import on_builder_inited
        app = MagicMock()
        app.config.html_static_path = []
        
        on_builder_inited(app)
        
        self.assertTrue(len(app.config.html_static_path) > 0)
        self.assertTrue(app.config.html_static_path[0].endswith('static'))

if __name__ == '__main__':
    unittest.main()
