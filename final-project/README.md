## Useful commands

To run a python server:

    python -m http.server

Once the model has been generated and the server is running, you can open the webpage and select viewer.html to visualize your model. After that, you can just refresh the page once a new model is generated.

WELCOME TO AVERY'S FINAL CODE PROJECT!!
Read below to learn more.

SUMMARY OF CODE:
the download_images.py works to download the images from whatever the input of the config file says. this means that with the change of file inputs, the different photos would be downloaded. i incorporated this into the main.py file so that if the down_files is true, then the old downloaded files are deleted and replaced with the news ones. if it is false, the files that are already downloaded will be processed again. 

the main.py works to use a variety of different functions from other scripts to output an 3D image from inputed images. 
these images are uploaded through the first function: preprocessing. these images come from a google drive link, the backgrounds are removed, and they are sent to a new file called preprocessed. this file becomes the input for the duster and master files

for duster, the preprocessed images are inputed and a images.zip file is created. then this saves a .glb file

for master, the same input of preprocessed images is sent. using the huggingface token, they export a model.glb file which is an even better export than the duster. then, we can upload this export to the viewer file to see the 3d image. this image can then be viewed through the html viewer to see the 3d model in a new window.


CHANGES YOU CAN MAKE TO THE CODE:
turn off different functions from running by changing true and false commands. consider using duster, master, and down_files.
change the directory if you wanted to use different photo inputs -- this would require creating a new folder to store these images in.
change model names using https://huggingface.co/spaces/KenjieDec/RemBG. this change is printed in the terminal.
change the file IDs in the config file, make sure the down_files is true so that any previously downloaded files are deleted.

Enjoy your time exploring the code!!