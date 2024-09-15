import time
import unittest

from pydantic_core import Url

import pyrdfrules.application
from pyrdfrules.common.task.task import Task

class TestRemoteApplication(unittest.IsolatedAsyncioTestCase):
        
    async def skip_test_runs_workspace(self):
        """
        Check if the application runs with a workspace, does not crash and terminates correctly.
        """
        
        app = pyrdfrules.application.Application()
        
        rdfrules = await app.start_remote(
            url = Url("http://rdfrules.vse.cz/api/")
        )
        
        self.assertIsNotNone(rdfrules, "Should not be None")
        await rdfrules.workspace.get_files()
        
        await app.stop()
        
    async def test_runs_task(self):
        """
        Check if the application runs with a task, does not crash and terminates correctly.
        """
        
        app = pyrdfrules.application.Application()
        
        rdfrules = await app.start_remote(
            url = Url("http://rdfrules.vse.cz/api/")
        )
        
        self.assertIsNotNone(rdfrules, "Should not be None")
        
        task : Task = None
        
        with open("./tests/data/task.json", "r") as file:        
            task_json_from_file = file.read()
            task = await rdfrules.task.create_task_from_string(task_json_from_file)
            self.assertIsNotNone(task, "Should not be None")
        
        progress = await rdfrules.task.get_task_by_id(task.id)
        self.assertIsNotNone(progress, "Should be None")
        print(progress)
        
        await app.stop()


if __name__ == '__main__':
    unittest.main()
