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
from helpers import *
import cv2
import edgeiq
from lxml import etree
from lxml.builder import E
import numpy as np
from Autoannotate import *

"""Specify your video and labels here"""
labels = ['person', 'car']
dataset_path = 'images/' # either a video file e.g. "video.mp4" or an folder of images e.g. "images/" within the same folder as this app.py
confidence_level = 0.5
overlap_threshold = 0.1
markup_image = False
slideShowSpeed = 0.01# Time in seconds each image is shown on streamer; set to 0 to process as fast as possible
dataset_name = 'annotated_data'
use_images = True #if you change this to false, you need to change the dataset_path to point to a video file


model_id = 'alwaysai/mobilenet_ssd'

obj_detect = edgeiq.ObjectDetection(model_id)
obj_detect.load(engine=edgeiq.Engine.DNN)


def main():
    with edgeiq.Streamer() as streamer:
        if use_images == True:
            auto_annotator = AutoAnnotator(obj_detect, confidence_level, overlap_threshold, labels, markup_image)
            time.sleep(2)
            auto_annotator.make_directory_structure(dataset_name)
            image_files = get_all_files(dataset_path)
            for i in range(len(image_files)):
                img = cv2.imread(get_file(image_files[i], dataset_path))
                frame = np.array(img)
                frame2 = deepcopy(frame)
                (annotation_xml, frame, image_name, markedUpFrame, text) = auto_annotator.annotate(frame)
                auto_annotator.write_image(annotation_xml, frame, image_name)
                start = time.time()
                while (time.time() - start < slideShowSpeed):
                    streamer.send_data(markedUpFrame, text)
                auto_annotator.image_index += 1
                print("Processed image: ", auto_annotator.image_index)
        else:
            try:
                auto_annotator = AutoAnnotator(obj_detect, confidence_level, overlap_threshold, labels, markup_image)
                with edgeiq.FileVideoStream(video_path) as video_stream:
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
                print("Completed the video")
        print("Before zip")
        auto_annotator.write_default_file()
        auto_annotator.zip_annotations(dataset_name)
        streamer.close()
        quit()


if __name__ == "__main__":
    main()
