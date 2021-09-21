# Face Detection with Python

This repository does face detection with Python and Opencv.

## Data

This repo comes with three image examples extracted from [[Berkeley Segmentation Dataset]](https://www2.eecs.berkeley.edu/Research/Projects/CS/vision/bsds/) proposed by [Matin et al., 2001]

## Roadmap of implementations

* [x] Haar Cascades
* [ ] YOLO

## Using the lib

As an example, we will discuss how to detect faces and eyes with Haar cascades. The algorithm is run by the class HaarDetector, in the facial_detection module. The implementation comes from opencv. You can detect faces and eyes as follows,

```python
from facial_detection import HaarDetector
from utils import plot_img_with_patches

im = ...
detector = HaarDetector()
(faces, eyes), exec_time = detector(im)
# Faces corresponds to the bounding boxes of faces
# Eyes corresponds to the bounding boxes of eyes
# Each bbox is an array (Nb, 4), where Nb is the number
# of bounding boxes. bbox_i is an array (x, y, h, w), 
# where x and y are the bbox positions, and h and w its size.
# For plotting:
plot_img_with_patches(im, faces, eyes)
```

## References

[Martin et al., 2001] Martin, David, et al. "A database of human segmented natural images and its application to evaluating segmentation algorithms and measuring ecological statistics." Proceedings Eighth IEEE International Conference on Computer Vision. ICCV 2001. Vol. 2. IEEE, 2001.
