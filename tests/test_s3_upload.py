import unittest

from syncr import S3
from syncr import sync
from syncr import Syncr


class S3UploadTest(unittest.TestCase):

    def setUp(self) -> None:
        self.s3 = S3()

    def test_upload(self):
        self.s3.bucket = "bucket name"
        self.s3.path = "/file/to/upload"
        syncr = Syncr(self.s3)
        assert sync(syncr) == 1
