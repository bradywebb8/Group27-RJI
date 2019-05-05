Our image classification system uses the Imutils library to load images from a folder.
The Open CV library computes the Laplacian on the image.
Then, we compute the variance on that.
This value is an indicator of how distinctly different the tonal intensity of the pixels are in relation to 
their neighboring pixels.
A higher value means a higher quality image.
Three thresholds were set in order to grade pictures by level of clarity.
This means we can sort out overly blurry images (as well as rank the remaining ones).
Using another library Piexif we can write an EXIF tag to the JPG file to give it a score based on that value.
