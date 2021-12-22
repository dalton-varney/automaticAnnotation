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

import cv2
import edgeiq
from lxml import etree
from lxml.builder import E
import numpy
from Autoannotate import *


model_id = 'safiralvi/licenseplate'

obj_detect = edgeiq.ObjectDetection(model_id)
obj_detect.load(engine=edgeiq.Engine.DNN)


labels = obj_detect.labels
confidence_level = 0.2
overlap_threshold = 0.1
markup_image = True
streamer = edgeiq.Streamer()
slideShowSpeed = 10

def auto_annotate(dataset_name: str, video_path: str):




    with edgeiq.FileVideoStream(video_path) as video_stream :
        time.sleep(2)

        auto_annotator = AutoAnnotator(video_stream, obj_detect, confidence_level, overlap_threshold, labels, markup_image)
        auto_annotator.make_directory_structure(dataset_name)
        for annotation_xml, frame, image_name in auto_annotator.annotate():
            auto_annotator.write_image(annotation_xml, frame, image_name)

            start = time.time()
            while (time.time() - start < slideShowSpeed):
                streamer.send_data(frame, f'Image: {auto_annotator.image_index}')
            auto_annotator.image_index += 1
            if streamer.check_exit():
                break
        auto_annotator.write_default_file()
        auto_annotator.zip_annotations(dataset_name)

    print("Program Ending")


auto_annotate('output_center_cam_demos', 'front_short.mp4')
