import unittest

import pyrdfrules.application

class TestApplication(unittest.IsolatedAsyncioTestCase):
    
    async def test_start_local(self): 
        app = pyrdfrules.application.Application()
        rdfrules = await app.start_local()
        self.assertIsNotNone(rdfrules, "Should not be None")


if __name__ == '__main__':
    unittest.main()
