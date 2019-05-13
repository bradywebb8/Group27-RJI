import cv2
from imutils import paths
import piexif

# Compute Laplacian of the image, then compute variance on that -- higher value = more clarity


def laplacian_variance(image):
    return cv2.Laplacian(image, cv2.CV_64F).var()

# The "focus" is the variance of the Laplacian
# The focus value assigns the rating from 1 to 4 based on tested thresholds

poorThresh = 180
fairThresh = 250
goodThresh = 600

# Scores to assign to picture meta data {1, 2, 3, 4}

score1 = {piexif.ImageIFD.Rating: "1"}
score2 = {piexif.ImageIFD.Rating: "2"}
score3 = {piexif.ImageIFD.Rating: "3"}
score4 = {piexif.ImageIFD.Rating: "4"}

# Load filepath containing pictures


for imagePath in paths.list_images('/User/Photos/Particular_Folder'):

    image = cv2.imread(imagePath)
    grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    focus = laplacian_variance(image)

    # Compare focus to thresholds of quality to assign score
    # The score is written to the picture's EXIF "Rating" field

    if focus <= poorThresh:

        exif_bytes = piexif.dump(score1)
        piexif.insert(exif_bytes, imagePath)

    if focus > poorThresh and focus <= fairThresh:

        exif_bytes = piexif.dump(score2)
        piexif.insert(exif_bytes, imagePath)

    if focus > fairThresh and focus <= goodThresh:

        exif_bytes = piexif.dump(score3)
        piexif.insert(exif_bytes, imagePath)

    if focus > goodThresh:

        exif_bytes = piexif.dump(score4)
        piexif.insert(exif_bytes, imagePath)
