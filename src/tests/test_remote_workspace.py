import logging
import os
import time
import unittest

from pyrdfrules.common.http.url import Url

import pyrdfrules.application
from pyrdfrules.common.task.task import Task
from pyrdfrules.config import Config

class TestRemoteWorkspace(unittest.TestCase):
        
    def test_runs_workspace(self):
        """
        Check if the application runs with a workspace, does not crash and terminates correctly.
        """
        
        app = pyrdfrules.application.Application()
        
        rdfrules = app.start_remote(
            url = Url("http://rdfrules.vse.cz/api/")
        )
        
        self.assertIsNotNone(rdfrules, "Should not be None")
        rdfrules.workspace.get_files()
        
        app.stop()
        
    def test_workspace_upload(self):
        """
        Check if the application can upload a file to the workspace.
        """
        
        app = pyrdfrules.application.Application()
        
        path = os.path.join(os.path.dirname((os.path.realpath(__file__))), "data/asset.txt")
        
        rdfrules = app.start_remote(
            url = Url("http://rdfrules.vse.cz/api/"),
            config=Config(
                task_update_interval_ms=1000,
                log_level=logging.DEBUG
            )
        )
        
        self.assertIsNotNone(rdfrules, "Should not be None")
                
        with open(path, "r") as file:        
            #file_contents = file.read()
            rdfrules.workspace.upload_file("data/asset.txt", file)
            
        rdfrules.workspace.delete_file("data/asset.txt")
        
        app.stop()


if __name__ == '__main__':
    unittest.main()
