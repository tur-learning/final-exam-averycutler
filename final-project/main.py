# 1
# Import necessary modules
import json
from preprocess import preprocess
from dust3r import duster
from mast3r import master
from download_images import down_images


# 2
# input config.json to read configurations
with open("config.json") as f:
    config = json.load(f)


# 3
# implement logic to use different models based on the configured parameters
# delete current images (if they exist) and download new ones from file_ids
if config["down_files"]:
    down_images(fileids=config["file_ids"])
    print("We have downloaded our new files")

# First: preprocess and store in preprocess folder
if config["preprocess_image"]:
    preprocess(input=config["image_directory"],
               model=config["model_name"],
               output=config["output_directory"]) # downloaded to preprocessed
    print("We are going to preprocess the image to remove the background")
    print(f"This preprocessing is using model" + config["model_name"])

# Run the duster file, save output
if config["use_dust3r"]:
    duster(input=config["output_directory"])
    print("We are going to use dust3r APIs")

# Run the master file, output as the better output for the 3D image (in separate window)
if config["use_mast3r"]:
    print("We are going to use mast3r APIs")
    print("The following output is our final model")
    master(input=config["output_directory"])