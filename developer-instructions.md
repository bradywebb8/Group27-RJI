-In order to use run our application you will need to create an ec2 instance or any other kind of server.

-You will need to download and install Flask using "sudo pip install flask" command.

-You will need to take the application.py file and all of our other files and put them on your server.

-The step above can we done by either FileZilla or by creating the files and copying the code to them.

-You will need to keep your .html files within a folder called templates with nothing else inside.

-Currently we have "complete.html", "gallery.html", and "upload.html" within our templates folder

-You can also have a "static" folder and inside that have a "css" folder to house differnet css styling.

-On the command line run sudo python application.py in your directory with application.py

-This will then start the server on whatever host you specifiy within application.py

-Connect to your amazon server using your public DNS.

-From here you should be able to view the main page and upload your own photos to your server.

-The images you upload will be put in a directory called images on your server. 

-From there you may do with the images as you please and add any other code to modify the pictures.

-Currently none of these programs access the database, as that is something we are currently working on 
implementing.
