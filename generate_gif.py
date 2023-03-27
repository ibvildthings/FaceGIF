import sys
import cv2
import numpy as np
import imageio
import argparse

def generate_gif(input_image_path, output_gif_path, speed, threshold):
    img = cv2.imread(input_image_path)

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=threshold, minSize=(30, 30))

    cropped_faces = []
    max_size = 0
    for (x, y, w, h) in faces:
        cropped = img[y:y+h, x:x+w]
        cropped_faces.append(cropped)
        max_size = max(max_size, w, h)

    resized_faces = []
    for face in cropped_faces:
        resized = cv2.resize(face, (max_size, max_size))
        resized_faces.append(resized)

    resized_faces_rgb = [cv2.cvtColor(face, cv2.COLOR_BGR2RGB) for face in resized_faces]
    imageio.mimsave(output_gif_path, resized_faces_rgb, duration=speed)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate a GIF from an input image with detected faces.')
    parser.add_argument('input_image_path', help='Path to the input image')
    parser.add_argument('output_gif_path', help='Path to save the generated GIF')
    parser.add_argument('-s', '--speed', type=float, default=0.3, help='Duration of each frame in the GIF (in seconds, default: 0.3)')
    parser.add_argument('-t', '--threshold', type=int, default=5, help='Threshold for the face detection (default: 5)')
    args = parser.parse_args()

    generate_gif(args.input_image_path, args.output_gif_path, args.speed, args.threshold)
    print(f"Generated GIF saved to: {args.output_gif_path}")
