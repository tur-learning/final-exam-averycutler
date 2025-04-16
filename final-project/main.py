# 1
# Import necessary modules
import json
from preprocess import preprocess
from dust3r import duster
from mast3r import master

# 2
# input config.json to read configurations
with open("config.json") as f:
    config = json.load(f)


# 3
# implement logic to use different models based on the configured parameters
def process_image(inputs, config1):
    if config1["preprocess_image"]:
        preprocess(inputs) # could also be preprocessed or downloads
        print("We are going to preprocess the image to remove the background")


def duster (inputs, config2):
    if config2["use_dust3r"]:
        duster(inputs)
        print("We are going to use dust3r APIs")

def master (inputs, config3):
    if config3["use_mast3r"]:
        master(inputs)
        print("We are going to use mast3r APIs")

inputs = "downloads" # this defined variable is the element of the input that the user can change. consider changing to preprocessed
config1 = {"preprocess_image": True}
config2 = {"use_dust3r": True}
config3 = {"use_mast3r": True}
process_image(inputs, config1)
duster(inputs, config2)
master(inputs, config3)

# right now theres a duster input with config2 and master doesn't have the equivilant. there's an error with the duster when i run the main.py
# ask about whats wrong with this and what i should be doing