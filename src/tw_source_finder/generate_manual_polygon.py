"""
A script that examines an image and generates polygons (== contours) at 
locations where the signal in the image is above a specified level.
It outputs the contours for analysis in later acripts
"""

import json
import math
import os
import subprocess
import sys
import weakref

import astropy.visualization as vis
import matplotlib.cm as cm
import matplotlib.pylab as plt
import numpy as np
from astropy.io import fits
from astropy.utils.data import get_pkg_data_filename
from astropy.wcs import WCS
from shapely.geometry import Point, Polygon

from tw_source_finder.check_array import check_array


class make_manual_polygon:
    def __init__(self, file_name):
        self.coords = []
        self.out_data = {}
        self.file_name = file_name
        hdu_list = fits.open(self.file_name)
        self.hdu = hdu_list[0]
        self.image = check_array(self.hdu.data)
        self.compare_fields()

    # def __str__(self):
    #       print("polygons =", self.out_data)

    def write(self, d=None):
        print(self.__dict__)

    # Simple mouse click function to store coordinates
    def onclick(self, event):
        if event.button == 1:
            ix, iy = event.xdata, event.ydata
            #     print('*** raw pos', ix, iy)

            # assign global variable to access outside of function
            loc = (ix, iy)
            #     print('even_loc', loc)
            self.coords.append(loc)
            if len(self.coords) > 1:
                x = []
                y = []
                for i in range(len(self.coords)):
                    x.append(self.coords[i][0])
                    y.append(self.coords[i][1])
                x = np.array(x)
                y = np.array(y)
                #       print('x,y', x,y)
                ax = plt.gca()
                ax.plot(x, y, "y")
                ax.figure.canvas.draw()
            self.title = self.file_name + " Manual Polygon for Flux Density Analysis"
            self.outpic = self.title.replace(" ", "_") + ".png"
            if os.path.isfile(self.outpic):
                os.remove(self.outpic)
            plt.savefig(self.outpic)
        if event.button == 3:
            ax = plt.gca()
            self.coords = []
            for line in ax.get_lines():  # ax.lines:
                line.remove()
            ax.figure.canvas.draw()
            if os.path.isfile(self.outpic):
                os.remove(self.outpic)
        return

    def compare_fields(self):
        cen_x = self.hdu.header["CRPIX1"]
        cen_y = self.hdu.header["CRPIX2"]

        # We can examine the two images (this makes use of the wcsaxes package behind the scenes):

        wcs = WCS(self.hdu.header)
        print("orginal wcs", wcs)
        # print('wcs', wcs)
        fig = plt.figure(1)

        # print('starting plot')
        cid = fig.canvas.mpl_connect("button_press_event", self.onclick)

        # set NaNs to zero
        self.image = np.nan_to_num(self.image)
        plt.subplot(projection=wcs.celestial)
        interval = vis.PercentileInterval(99.9)
        vmin, vmax = interval.get_limits(self.image)
        vmin = 0.0
        norm = vis.ImageNormalize(vmin=vmin, vmax=vmax, stretch=vis.LogStretch(1000))
        #   plt.grid(color='white', ls='solid')
        plt.xlabel("RA")
        plt.ylabel("DEC")
        plt.title(self.file_name)

        plt.imshow(self.image, cmap=plt.cm.gray, norm=norm, origin="lower")
        plt.show()
        fig.canvas.mpl_disconnect(cid)
        length = len(self.coords)
        if length > 2:
            locations = []
            for i in range(length):
                print("initial", self.coords[i])
                x = self.coords[i][0]
                y = self.coords[i][1]
                loc = (y, x)
                locations.append(loc)
            print("************* coords to be dumped", locations)
            num_contours = 1
            self.out_data["num_contours"] = num_contours
            self.out_data["0"] = locations
            p = Polygon(locations)
            self.out_data["manual"] = True
        print("returning ", self.out_data)
        return self.out_data


def main(argv):
    print("args ", argv)
    polygon_gen = make_manual_polygon(argv[1])


# print('polygon generated ', polygon_gen.out_data)
if __name__ == "__main__":
    print("generate_manual_polygons argv", sys.argv)
    main(sys.argv)
