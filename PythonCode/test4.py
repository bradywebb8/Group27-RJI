import cv2
import numpy as np
from matplotlib import pyplot as plt


# load picture(s)
img = cv2.imread("/Users/Vic/PycharmProjects/histogram_tests/pics/images-8.jpeg")
red = cv2.imread("/Users/Vic/PycharmProjects/histogram_tests/pics/red.jpg")
green = cv2.imread("/Users/Vic/PycharmProjects/histogram_tests/pics/green.jpg")

# need matrix to store histogram data
# note -- nbins, the bin count, dictates the row count
# col 1 = n: the number of pixels in each bin
# col 2 = bins: the edges of the bins (length nbins + 1 -- to measure left of 1st bin to right of last bin)
# col 3 = patches: a 'silent_list' of patches used to graph histogram

nbins = 10
picture_data = np.zeros((nbins, 3))
pd2 = np.zeros((nbins, 3))
pd3 = np.zeros((nbins, 3))

# create histogram, load its data into our array
picture_data = plt.hist(img.ravel(),nbins,[0,nbins], density=None, weights=None, cumulative=False, bottom=None, histtype='bar', align='mid', orientation='vertical', rwidth=None, log=False, color=None, label=None, stacked=False, normed=None)
pd2 = plt.hist(red.ravel(),nbins,[0,nbins], density=None, weights=None, cumulative=False, bottom=None, histtype='bar', align='mid', orientation='vertical', rwidth=None, log=False, color=None, label=None, stacked=False, normed=None)
pd3 = plt.hist(green.ravel(),nbins,[0,nbins], density=None, weights=None, cumulative=False, bottom=None, histtype='bar', align='mid', orientation='vertical', rwidth=None, log=False, color=None, label=None, stacked=False, normed=None)

# display
plt.show()

# display the picture's data
for row in picture_data:
    print([str(x) for x in row]); print("\n")

for row in pd2:
    print([str(x) for x in row]); print("\n")

for row in pd3:
    print([str(x) for x in row]); print("\n")

# test print of pixel frequency in bin 1 of picture 2
print("\n\n\nPIXEL FREQUENCY IN BIN 1 OF PICTURE 2: ", pd2[0][0])

# test for calculating blur level
scale = 40  # user can set scale, which increases sensitivity to detecting blur
blur_res = np.floor(nbins / scale)  # is value that bins will be grouped into to calculate standard deviations
i = 0
j = 0

# deviations is an array of the standard deviations across the 'blur_res' number of bins
deviations = []

# compute the standard deviation between pixel frequency across the 'blur_res' number of bins
while (i < nbins - blur_res):
    k = 0
    while (k < blur_res):
        deviations[j] = picture_data[i + k][0]
        k += 1

# if the standard deviation for a given group of bins is close to 0, there is little difference between then
# if many groups of bins' standard deviations are close to 0, it is likely that the image is blurry
