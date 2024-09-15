import time
import unittest

from pydantic_core import Url

import pyrdfrules.application

class TestRemoteApplication(unittest.IsolatedAsyncioTestCase):
        
    async def test_runs_workspace(self):
        """
        Check if the application runs with a workspace, does not crash and terminates correctly.
        """
        
        app = pyrdfrules.application.Application()
        
        rdfrules = await app.start_remote(
            url = Url("http://rdfrules.vse.cz/api/")
        )
        
        self.assertIsNotNone(rdfrules, "Should not be None")
        await rdfrules.engine.check()
        
        await app.stop()


if __name__ == '__main__':
    unittest.main()
