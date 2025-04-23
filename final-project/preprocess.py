from gradio_client import Client, handle_file
import os, shutil
from pathlib import Path
from utils import convert_png_to_jpg


def preprocess(input, output, model): # MAKE THER ROOT DIRECTORY AN INPUT FROM CONFIG, model type has a default but can be changed

    # This variable can be put in the config file
    images_path = os.listdir(input) # changable with input

    # Visit this page to view the possible models that can be used:
    # https://huggingface.co/spaces/KenjieDec/RemBG
    client = Client("KenjieDec/RemBG")

    preprocessed_dir = Path(output).resolve() # MAKE PREPROCESSED THE OUTPUT
    # Initially removes dir
    shutil.rmtree(preprocessed_dir)
    Path.mkdir(preprocessed_dir)

    for image in images_path:
        result = client.predict(
                file=handle_file(os.path.join(input, image)),
                mask="Default",
                model= model, # this is user changable
                x=3,
                y=3,
                api_name="/inference"
        )
        result = Path(result)
        print(result)
        print("Copying preprocessed image to output directory")
        shutil.copyfile(result, os.path.join("preprocessed", result.parent.name+result.suffix))

    # Images are converted to jpg for integration with dust3r model
    convert_png_to_jpg(preprocessed_dir)
    return preprocessed_dir 

    # removes background and puts in folder
    # made from png to jpeg


    # make the function return an output that would be useful in the main.py
    