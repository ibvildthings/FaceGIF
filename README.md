# FaceGIF

Create Face GIFs from Group Photos.

![Output GIF](./output.gif)


![Input Image](./input.jpg)


This Python script takes an input image, detects faces using OpenCV's Haar cascades, crops and resizes the faces to the same size, and generates an animated GIF from the cropped faces.

## Dependencies

- Python 3.6 or higher
- OpenCV
- imageio

You can install the required packages using pip:

```bash
pip install opencv-python-headless imageio
```

## Usage

To generate a GIF from an input image, use the following command:

```bash
python generate_gif.py input_image_path output_gif_path [--speed SPEED] [--threshold THRESHOLD]
```

**input_image_path:** Path to the input image file.
output_gif_path: Path to save the generated GIF.

**--speed:** (Optional) Duration of each frame in the GIF, in seconds (default: 0.3).

**--threshold:** (Optional) Threshold for face detection (default: 5).

## For example:

```bash
python generate_gif.py input.jpg output.gif --speed 0.3 --threshold 3
```

## Parameters

**--speed:** Controls the duration of each frame in the generated GIF. Increase the value to slow down the animation or decrease it to speed up the animation.

**--threshold:** Controls the sensitivity of the face detection algorithm. Increase the value for fewer detections and higher accuracy, or decrease the value for increased sensitivity and potentially more false positives.


## Note

It works best with front facing photos. You can try to improve this script by using tensorflow or some other ML library.
