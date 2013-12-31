# hardnessProfile.py
# -------------
# Licensing Information:
# This project is licensed under the GNU General Public License V2 as open source software.
# The license is available at https://github.com/EntilZha/sg-snowprofile/blob/master/LICENSE
# Use of this software is subject to (1) adhering to the GNU General Public License V2,
# (2) you retain this notice, and (3) you provide clear attribution to SnowGeek, including a link to
# http://snowgeek.org/
#
# Attribution Information: This software was developed by SnowGeek.
# The project was created by Pedro Rodriguez and Santiago Rodriguez. For more information
# about SnowGeek, please visit http://snowgeek.org/

import re
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from Tkinter import Tk
from tkFileDialog import askopenfile

HARNDESS_CONVERSIONS = {
    'F-': 1, 'F': 2, '4F-': 3, '4F': 4, '1F-': 5, '1F': 6, 'P-': 7, 'P': 8, 'K-': 9, 'K': 10
}

HARDNESSES = ('', 'F-', 'F', '4F-', '4F', '1F-', '1F', 'P-', 'P', 'K-', 'K')
COLOR_CONVERSIONS = {
    1: (0.9, 0.1, 0.1), 2: (0.9, 0.1, 0.1),
    3: (1, 0.6, 0), 4: (1, 0.6, 0),
    5: (0.1, 0.4, 1), 6: (0.1, 0.4, 1),
    7: (0.4, 0.2, 0.9), 8: (0.4, 0.2, 0.9),
    9: (0.5, 0.9, 0.1), 10: (0.5, 0.9, 0.1)
}


def loadData():
    root = Tk()
    root.withdraw()
    f = askopenfile('rU', parent=root)
    #f = open(filename, 'rU')
    pattern = re.compile(r'\s+')
    data = []
    for line in f:
        elements = pattern.split(line)
        depth = elements[0]
        hardness = elements[1]
        data.append((depth, hardness))
    return data


def widthFromData(data):
    widths = []
    for i in range(len(data)):
        widths.append(hardnessToNumber(data[i][1]))
    return widths


def createHardnessProfile(widths, heights):
    fig = plt.figure()
    fig.clear()
    ax = fig.add_axes([.2, .2, .6, .6])
    currentHeight = 0
    for i in range(len(widths) - 1):
        color = COLOR_CONVERSIONS[widths[i]]
        patch = patches.Rectangle((0, 1.0 * currentHeight), 1.0 * widths[i], heights[i], color=color)
        currentHeight += heights[i]
        ax.add_patch(patch)
    plt.title('Snow Profile Hardness by SnowGeek')
    ax.set_xticks(range(11))
    ax.set_xticklabels(HARDNESSES)
    ax.set_xlabel('Hardness')
    ax.set_ylabel('Depth (cm)')
    ax.set_yticks(range(0, int(sum(heights)) + 1, 10))
    plt.gca().invert_yaxis()
    plt.show()


def hardnessToNumber(hardness):
    return HARNDESS_CONVERSIONS[hardness]


def layerHeightFromData(data):
    heights = []
    for i in range(len(data) - 1):
        bot = float(data[i][0])
        top = float(data[i + 1][0])
        heights.append(top - bot)
    return heights


def main():
    data = loadData()
    widths = widthFromData(data)
    depths = layerHeightFromData(data)
    createHardnessProfile(widths, depths)

if __name__ == '__main__':
    main()


