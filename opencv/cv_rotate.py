import cv2
import numpy as np

def cv_rotate_image(image, angle):
    """ cv rotate image """
    center=tuple(np.array(image.shape[0:2])/2)
    rot_mat = cv2.getRotationMatrix2D(center, angle, 1.0)
    return cv2.warpAffine(image, rot_mat, image.shape[0:2], flags=cv2.INTER_LINEAR)

def cv_read_image(path='../pat/image0.dat'):
    """ cv read image """
    return cv2.imread(path)

def cv_dump_image(des, image):
    """ cv dump image q """
    img_h, img_w = image.shape[0:2]
    cv2.namedWindow(des)
    cv2.resizeWindow(des, img_h, img_w)
    cv2.imshow(des, image)

def cv_close_image(delay=0):
    """ cv wait event to close image """
    key = cv2.waitKey(delay)
    if key == 27 or key == ord('q'):
        cv2.destroyAllWindows()
        exit()

def cv_iter_image(image):
    """ cv iterator image from left to right, top to down """
    img_h, img_w = image.shape[0:2]
    return [int(cv2.cv.Get2D(cv2.cv.fromarray(image), h, w)) for h in xrange(0, img_h) for w in xrange(0, img_w)]


def clone_image(image):
    """ clone image """
    return image.copy()

def rotate_image_90(image):
    """ rotate image 90 degree """

   img_h, img_w = image.shape[0:2]

    # transpose
    for h in xrange(0, img_h):
        for w in xrange(h, img_w):
            w_h, h_w = cv2.cv.Get2D(cv2.cv.fromarray(image), w, h), cv2.cv.Get2D(cv2.cv.fromarray(image), h, w)
            cv2.cv.Set2D(cv2.cv.fromarray(image), h, w, w_h)
            cv2.cv.Set2D(cv2.cv.fromarray(image), w, h, h_w)

    # reverse each row
    for w in xrange(0, img_w):
        for h in xrange(0, img_h/2):
            w_h_0, w_h_1 = cv2.cv.Get2D(cv2.cv.fromarray(image), w, h), cv2.cv.Get2D(cv2.cv.fromarray(image), w, img_h - h -1)
            cv2.cv.Set2D(cv2.cv.fromarray(image), w, h, w_h_1)
            cv2.cv.Set2D(cv2.cv.fromarray(image), w, img_h - h - 1, w_h_0)


def rotate_image_270(image):
    """ rotate image 270 degree """

    img_h, img_w = image.shape[0:2]

    # transpose
    for h in xrange(0, img_h):
        for w in xrange(h, img_w):
            w_h, h_w = cv2.cv.Get2D(cv2.cv.fromarray(image), w, h), cv2.cv.Get2D(cv2.cv.fromarray(image), h, w)
            cv2.cv.Set2D(cv2.cv.fromarray(image), h, w, w_h)
            cv2.cv.Set2D(cv2.cv.fromarray(image), w, h, h_w)

    # reverse each column(width)
    for h in xrange(0, img_h):
        for w in xrange(0, img_w/2):
            h_w_0, h_w_1 = cv2.cv.Get2D(cv2.cv.fromarray(image), h, w), cv2.cv.Get2D(cv2.cv.fromarray(image), h, img_w - w -1)
            cv2.cv.Set2D(cv2.cv.fromarray(image), h, w, h_w_1)
            cv2.cv.Set2D(cv2.cv.fromarray(image), h, img_w - w - 1, h_w_0)


if __name__ == '__main__':
    """ rotate 270 example """
    image = cv_read_image(path='../pat/image0.dat')
    cv_dump_image('org image', image)
    new_image = cv_rotate_image(image=image, angle=270)
    cv_dump_image('after rotate 270 degree via cv', new_image)
    rotate_image_270(image)
    cv_dump_image('after rotate 270 degree via it', image)
    cv_close_image(0)
