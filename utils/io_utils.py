import cv2
import numpy as np


def imread(path):
    im = cv2.imread(path)
    # cv2 reads images as B G R if image has colors
    if len(im.shape) > 2:
        # if that is the case, we need to convert from BGR to RGB
        # Converts to R G B
        _im = np.zeros_like(im)
        _im[:, :, 0] = im[:, :, 2].copy()
        _im[:, :, 1] = im[:, :, 1].copy()
        _im[:, :, 2] = im[:, :, 0].copy()
        return _im
    # if not, we don't do anything
    return im