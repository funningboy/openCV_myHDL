""" need double check why the rotate results are diff on CV and alg """

import sys
sys.path.append("../")

from cv_rotate import *
from unittest import TestCase
import unittest

class TestRotateProperties(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_rotate_270(self):
        """ check with golden model """
        image = cv_read_image(path='../../pat/image0.ipg')
        cv_image = cv_rotate_image(image=image, angle=270)
        it_image = clone_image(image)
        rotate_image_270(it_image)
        self.assertTrue(cv_iter_image(cv_image) == cv_iter_image(it_image))

    def test_rotate_90(self):
        """ check with golden model """
        image = cv_read_image(path='../../pat/image0.jpg')
        cv_image = cv_rotate_image(image=image, angle=90)
        it_image = clone_image(image)
        rotate_image_90(it_image)
        self.assertTrue(cv_iter_image(cv_image) == cv_iter_image(it_image))

if __name__ == '__main__':
    unittest.main()
