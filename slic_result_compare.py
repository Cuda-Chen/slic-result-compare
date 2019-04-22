from skimage.segmentation import slic,mark_boundaries
from skimage import io
import numpy as np
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('input_file', type=str, help='input image path')
parser.add_argument('num_superpixel', type=int, help='number of superpixel')
parser.add_argument('compactness', type=int, help='compactness of superpixel')
args = parser.parse_args()

inputfile = args.input_file
label_color = (1, 0, 0)
outputfile = os.path.splitext(inputfile)[0] + '_' + str(args.num_superpixel) + '_' + str(args.compactness) + '.bmp'

image = io.imread(inputfile)

segments = slic(image, n_segments=args.num_superpixel, compactness=args.compactness)
output = mark_boundaries(image, segments, color=label_color)

io.imsave(outputfile, output)
