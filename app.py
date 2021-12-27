"""
Auto Annotation Application

Lets you chose an alwaysai model and a video to annotate. You can choose labels to annotate and toy around with
confidence level.

Look at the performance of the annotations on the streamer.

To upload to CVAT upload the files in jpeg images to a task. Then click Add annotations and upload the annotations zip
"""
import os
import shutil
from typing import List
import zipfile
import time
from copy import deepcopy

import cv2
import edgeiq
from lxml import etree
from lxml.builder import E
import numpy
from Autoannotate import *


model_id = 'alwaysai/mobilenet_ssd'
'output_center_cam_demos', 'front_short.mp4'

obj_detect = edgeiq.ObjectDetection(model_id)
obj_detect.load(engine=edgeiq.Engine.DNN)


labels = obj_detect.labels
confidence_level = 0.5
overlap_threshold = 0.1
markup_image = False
slideShowSpeed = 1 # Time in seconds each image is shown
dataset_name = 'output_center_cam_demos'
video_path = 'front_short.mp4'

def main():
    try:
        auto_annotator = AutoAnnotator(obj_detect, confidence_level, overlap_threshold, labels, markup_image)
        with edgeiq.FileVideoStream(video_path) as video_stream, edgeiq.Streamer() as streamer:
            time.sleep(2)
            auto_annotator.make_directory_structure(dataset_name)
            while True:
                frame = video_stream.read()
                frame2 = deepcopy(frame)

                (annotation_xml, frame, image_name, markedUpFrame, text) = auto_annotator.annotate(frame)
                auto_annotator.write_image(annotation_xml, frame, image_name)
                start = time.time()
                while (time.time() - start < slideShowSpeed):
                    streamer.send_data(markedUpFrame, text)
                auto_annotator.image_index += 1
    except edgeiq.NoMoreFrames:
        auto_annotator.write_default_file()
        auto_annotator.zip_annotations(dataset_name)


if __name__ == "__main__":
    main()
