# a script to subtract specified areas from a radio_cutout field

import math
import os.path
import sys
from optparse import OptionParser

import numpy as np
from astropy.io import fits

from tw_source_finder.check_array import check_array
from tw_source_finder.process_polygon_data import *


def analyze_image(filename, second_file, use_math):
    hdu_list = fits.open(filename)
    hdu = hdu_list[0]
    data = hdu.data
    print("input array min and max", data.min(), data.max())
    try:
        hdu_list_mask = fits.open(second_file)
        hdu = hdu_list_mask[0]
        data1 = hdu.data
        print("second array min and max", data1.min(), data1.max())
    except:
        data1 = float(second_file)
        print("second parameter has numerical value", data1)
    if use_math == "a":
        hdu.data = data + data1
        out_file = "image_math_add.fits"
    if use_math == "s":
        hdu.data = data - data1
        out_file = "image_math_subt.fits"
    if use_math == "m":
        hdu.data = data * data1
        out_file = "image_math_mult.fits"
    if use_math == "d":
        hdu.data = data / data1
        out_file = "image_math_div.fits"
    hdu.header["DATAMAX"] = hdu.data.max()
    hdu.header["DATAMIN"] = hdu.data.min()
    hdu.writeto(out_file, overwrite=True)


def main(argv):
    parser = OptionParser(usage="%prog [options] ")
    parser.add_option(
        "-f",
        "--file",
        dest="filename",
        help="Filename with radio source names, positions, redshift etc (default = None)",
        default=None,
    )
    parser.add_option(
        "-s",
        "--second_file",
        dest="filename2",
        help="Filename with radio source names, positions, redshift etc OR numerical value (default = None)",
        default=None,
    )
    a = "a"
    parser.add_option(
        "-m",
        "--use_m",
        dest="use_math",
        help="use math (default = a)",
        default=a,
    )
    (options, args) = parser.parse_args()
    print("options", options)
    filename = options.filename
    filename2 = options.filename2
    use_math = options.use_math
    analyze_image(filename, filename2, use_math)


if __name__ == "__main__":
    main(sys.argv)
