import time
import unittest

from pyrdfrules.common.http.url import Url

import pyrdfrules.application
from pyrdfrules.common.task.task import Task
from pyrdfrules.config import Config
import os

class TestRemoteApplication(unittest.IsolatedAsyncioTestCase):
        
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
        
    def test_runs_task(self):
        """
        Check if the application runs with a task, does not crash and terminates correctly.
        """
        
        app = pyrdfrules.application.Application()
        
        rdfrules = app.start_remote(
            url = Url("http://rdfrules.vse.cz/api/"),
            config=Config(
                task_update_interval_ms=1000
            )
        )
        
        self.assertIsNotNone(rdfrules, "Should not be None")
        
        task : Task = None
        
        path = os.path.realpath(os.path.join(os.path.dirname((os.path.realpath(__file__))), "data", "task.json")) 
        
        with open(path, "r") as file:        
            task_json_from_file = file.read()
            task = rdfrules.task.create_task_from_string(task_json_from_file)
            self.assertIsNotNone(task, "Should not be None")
            
        gen = rdfrules.task.run_task(task)
        
        print("Started a task task")
        
        for t in gen:
            print("Task step")
            self.assertIsInstance(t, Task, "Should be an instance of Task")
            pass
        
        self.assertIsNotNone(task.result, "Should not be None")
        self.assertTrue(task.finished, "Should be finished")
        
        app.stop()


if __name__ == '__main__':
    unittest.main()
