import time
import unittest

from pyrdfrules.common.http.url import Url

import pyrdfrules.application
from pyrdfrules.common.task.task import Task
from pyrdfrules.config import Config

class TestRemoteApplication(unittest.IsolatedAsyncioTestCase):
        
    def skip_test_runs_workspace(self):
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
        
        with open("./tests/data/task.json", "r") as file:        
            task_json_from_file = file.read()
            task = rdfrules.task.create_task_from_string(task_json_from_file)
            self.assertIsNotNone(task, "Should not be None")
            
        rdfrules.task.run_task(task)
        
        print("Finished task")
        print(task.result)
            
        #for i in range(10):
        #    progress = rdfrules.task.get_task_by_id(task.id)
        #    self.assertIsNotNone(progress, "Should not be None")
        #    print(progress)
        #    time.sleep(10)
        
        app.stop()


if __name__ == '__main__':
    unittest.main()
