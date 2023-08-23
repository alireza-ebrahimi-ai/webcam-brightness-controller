# Webcam Brightness Controller 📷💡

This is a Python script that automatically adjusts the screen brightness based on the average brightness of the webcam image. It uses OpenCV to capture the webcam image, numpy to calculate the average brightness, and screen_brightness_control to get and set the screen brightness. It also uses logging to record any changes or errors.

## Installation 🔧

To run this script, you need to have Python 3 and the following packages installed:

- opencv-python
- numpy
- screen_brightness_control

You can install them using pip:

```bash
pip install opencv-python numpy screen_brightness_control
```

You also need to download the light detection model from this [link](https://github.com/alireza-ebrahimi-ai/light-detection-model) and save it in the same folder as the script.

## Usage 🚀

To run the script, simply execute it from the command line:

```bash
python webcam_brightness.py
```

The script will start capturing images from your webcam and adjust the screen brightness accordingly. You can change the adjustment interval and the threshold for brightness difference in the script. To stop the script, press Ctrl+C.

## License 📄

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
