# Model-Assisted Annotation
Use [Object Detection](https://alwaysai.co/docs/application_development/core_computer_vision_services.html#object-detection) to detect objects in a real-time camera stream. The types of objects detected can be changed by selecting different models.

## Requirements
* [alwaysAI account](https://alwaysai.co/auth?register=true)
* [alwaysAI Development Tools](https://alwaysai.co/docs/get_started/development_computer_setup.html)

## Usage
Once the alwaysAI tools are installed on your development machine (or edge device if developing directly on it) you can install and run the app with the following CLI commands:

To perform initial configuration of the app:
```
aai app configure
```

Select ```Create new Project``` and provide a name for your application

When prompted with ```How would you like to initialize your project?```

Choose ```As an empty app```

Finally, choose your ```local computer``` for the destination

To prepare the runtime environment and install app dependencies:
```
aai app install
```

To start the app:
```
aai app start
```

## Configuration Parameters
If you open the app.py function, you will see a set of parameters where you can specify video to be processed, labels, and more variables:
```
labels = ['person', 'car']
video_path = 'front_short.mp4'
confidence_level = 0.5
overlap_threshold = 0.1
markup_image = False
slideShowSpeed = 1
dataset_name = 'annotated_data'
```
SlideshowSpeed specifies how long each image shown on the streamer(localhost:5000), if you set slideShowSpeed to ```0``` then the images will be processed as fast as possible.

## Changing the model

The model id is set with the variable ```model_id```. Change this variable to the name of the model you would like to use and don't forget to run ```aai app models add <model_id>``` in the command line to download add model to this project.

## Using your annotations to train a model

In order to train a model with your annotated dataset, open the folder ```annotated_data``` in your project. (Note: this folder will only appear after you have run the application)

Select the ```.zip``` and upload to the alwaysAI dataset tab and begin training your model.

## Uploading your dataset to CVAT for editing

In order to view your annotations on CVAT or make adjustments, open the folder ```annotated_data``` in your project. (Note: this folder will only appear after you have run the application)

Open the folder ```Annotations``` and select every ```xml``` file in the folder at the same time.  Choose```Compress``` or ```Zip``` on your OS system (For Mac it is right click, for Windows 10+ you may have to download unarchiver or 7zip)

Create a new task/job on CVAT with identical labels to your annotation variable ```labels``` and when CVAT prompts you to upload your images or video, select every image in the folder ```JPEGImages```

Finish creating the task/job and open the task/job.

Once you have loaded into the annotation page, you should see your images ready for annotation. In the upper right select ```Menu``` then select ```Upload annotations``` and ```PASCAL VOC``` as the format.

CVAT should open a file browser and you can select the zipped Annotations file you created a moment earlier. CVAT will give you a warning that uploading new annotations with erase and current annotations in that task. Since you just created a new task/job, you shouldn't have any issues and move forward with the upload.


If you have any further questions, please reach out to dalton@alwaysai.co


## More Information
To change the computer vision model, the engine and accelerator, and add additional dependencies read [this guide](https://alwaysai.co/docs/application_development/configuration_and_packaging.html).

## Support
* [Documentation](https://alwaysai.co/docs/)
* [Community Discord](https://discord.gg/z3t9pea)
* Email: support@alwaysai.co
