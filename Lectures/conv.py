import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

import os

def adaptive_gaussian_notes(filename, new_filename):
    img = cv.imread(filename, 0)
    th = cv.adaptiveThreshold(img,
                              255,
                              cv.ADAPTIVE_THRESH_GAUSSIAN_C,
                              cv.THRESH_BINARY,
                              15,
                              10)
    cv.imwrite(new_filename, th)
    return th


def main():
    lectures = os.listdir(".")[2:]

    for directory in lectures:
        notes = os.listdir(directory)
        for note in notes:
            # skip image if it is already converted
            if "_" in note:
                continue
            filename = os.path.join(directory, note)
            # conversion rule : add _ before an extension
            new_filename = os.path.join(directory,
                                        note.replace(".jpg", "_.png").replace(".jpeg", "_.png"))
            print(new_filename)
            th = adaptive_gaussian_notes(filename, new_filename)
            

main()
