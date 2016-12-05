# Copyright (c) Twisted Matrix Laboratories.
# See LICENSE for details.

from twisted.trial.unittest import TestCase


class NoAPITestCase(TestCase):

    def test_no_api(self):
        """
        Nothing can be star imported from this package.
        """
        import twisted_platform_support
        self.assertEqual(twisted_platform_support.__all__, [])
