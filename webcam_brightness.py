import cv2
import numpy as np
import screen_brightness_control as sbc
import time
import logging

logging.basicConfig(filename='webcam_brightness.log', level=logging.INFO)

# Initialize webcam
cap = cv2.VideoCapture(0)

while True:
    try:
        # Capture image from webcam
        ret, frame = cap.read()
        if not ret:
            break

        # Calculate average brightness of image
        avg_brightness = np.mean(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY))

        # Get current brightness
        current_brightness = sbc.get_brightness()[0]  # assuming one screen

        # Calculate the difference between current brightness and average brightness
        brightness_diff = int(avg_brightness) - current_brightness

        # If the difference is significant (greater than a threshold), adjust the brightness
        if abs(brightness_diff) > 10:
            new_brightness = current_brightness + brightness_diff // 10
            new_brightness = max(0, min(75, new_brightness))  # ensure it's in 0-75 range
            sbc.set_brightness(new_brightness)
            logging.info(f'Adjusted brightness from {current_brightness} to {new_brightness}')

        # Wait for a specified interval
        time.sleep(1)
    except Exception as e:
        logging.error(f'Error occurred: {e}')
        break

# Release the webcam
cap.release()
