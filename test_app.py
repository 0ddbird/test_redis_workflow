import unittest
import app


class TestApp(unittest.TestCase):
    def test_redis_connection(self):
        r = app.main()
        self.assertIsNotNone(r)


if __name__ == "__main__":
    unittest.main()
