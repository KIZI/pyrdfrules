import time
import unittest

import pyrdfrules.application

class TestApplication(unittest.IsolatedAsyncioTestCase):

    async def test_runs_local(self):
        """
        Check if the application runs locally, does not crash and terminates correctly.
        """
        
        app = pyrdfrules.application.Application()
        rdfrules = await app.start_local(
            install_jvm = True,
            install_rdfrules = True
        )
        self.assertIsNotNone(rdfrules, "Should not be None")
        time.sleep(10)
        await app.stop()


if __name__ == '__main__':
    unittest.main()
