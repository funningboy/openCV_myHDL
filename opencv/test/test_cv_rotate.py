from cv_rotate import *
from unittest import TestCase
import unittest

class TestRotateProperties(TestCase):

    def setUp():
        pass

    def tearDown():
        pass

    def test_rotate_270():
        image = cv_read_image(path='../pat/image0.dat')
        cv_image = cv_rotate_image(image=image, angle=270)
        it_image = clone_image(image)
        rotate_image_270(it_image)
        cv_dump_image('org image', image)
        cv_dump_image('after rotate 270 degree via cv', cv_image)
        cv_dump_image('after rotate 270 degree via it', it_image)
        self.asseTrue(cv_iter_image(cv_image) == cv_iter_image(it_image))
        cv_close_image(0)

    def test_rotate_90():
        image = cv_read_image(path='../pat/image0.dat')
        cv_image = cv_rotate_image(image=image, angle=90)
        it_image = clone_image(image)
        rotate_image_90(it_image)
        cv_dump_image('org image', image)
        cv_dump_image('after rotate 90 degree via cv', cv_image)
        cv_dump_image('after rotate 90 degree via it', it_image)
        self.asseTrue(cv_iter_image(cv_image) == cv_iter_image(it_image))
        cv_close_image(0)


if __name__ == '__main__':
    unittest.main()
