from facial_detection import HaarDetector
from utils import imread, plot_img_with_patches

im = imread('./data/181018.jpg')
detector = HaarDetector()
(faces, eyes), elapsed_time = detector(im)

print('Detection took {} seconds'.format(elapsed_time))
plot_img_with_patches(im, faces, eyes)