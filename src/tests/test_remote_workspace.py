import logging
import time
import unittest

from pydantic_core import Url

import pyrdfrules.application
from pyrdfrules.common.task.task import Task
from pyrdfrules.config import Config

class TestRemoteWorkspace(unittest.IsolatedAsyncioTestCase):
        
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
        
    def test_workspacek(self):
        """
        Check if the application can upload a file to the workspace.
        """
        
        app = pyrdfrules.application.Application()
        
        rdfrules = app.start_remote(
            url = Url("http://rdfrules.vse.cz/api/"),
            config=Config(
                task_update_interval_ms=1000,
                log_level=logging.DEBUG
            )
        )
        
        self.assertIsNotNone(rdfrules, "Should not be None")
                
        with open("./tests/data/asset.txt", "r") as file:        
            file_contents = file.read()
            rdfrules.workspace.upload_file("tests/asset.txt", file_contents)
            
        #for i in range(10):
        #    progress = rdfrules.task.get_task_by_id(task.id)
        #    self.assertIsNotNone(progress, "Should not be None")
        #    print(progress)
        #    time.sleep(10)
        
        app.stop()


if __name__ == '__main__':
    unittest.main()
