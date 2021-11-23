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

To prepare the runtime environment and install app dependencies:
```
aai app install
```

To start the app:
```
aai app start
```

###Configuration Parameters
To run this app pass the appropriate configuration parameters to the `auto_annotate` method:
```
auto_annotate(dataset_name: str, video_path: str, model_id: str, labels: List[str], confidence_level: float, overlap_threshold: float, markup_image: bool)
```

Example:
```
auto_annotate('output_center_cam_demos', 'CenterCam.avi', 'ripteyedprod/posup-sides-m75-8-med', ["TwixRegular", "KitkatRegular", "MtnDewTwenty", "DeepRiverJalapeno", "KitkatLarge", "DietPepsiTwentyOz", "AquafinaTwentyOz", "TwixLarge", "TrolliSourWorms", "PepsiTwentyOz", "BakedLaysXLV", "DeepRiverOriginal", "Starburst", "DoritosXLV", "SabraHummus", "SabraRedPepper"], 0.2, 0.1, True)
```

###More Information
To change the computer vision model, the engine and accelerator, and add additional dependencies read [this guide](https://alwaysai.co/docs/application_development/configuration_and_packaging.html).

## Support
* [Documentation](https://alwaysai.co/docs/)
* [Community Discord](https://discord.gg/z3t9pea)
* Email: support@alwaysai.co
