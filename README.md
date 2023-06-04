# QR Code Encoder and Decoder

This project is a Python script that enables you to encode and decode QR codes using the OpenCV and pyzbar libraries. It provides a command-line interface for easy interaction.

## Features

- Encode text information into a QR code image.
- Decode QR codes from a live video stream or webcam.

## Requirements

- Python 3.x
- OpenCV (`cv2`) library
- qrcode library
- pyzbar library

## Installation

1. Clone this repository or download the `script.py` file.
2. Install the required libraries using pip:

```bash
pip install opencv-python
pip install qrcode
pip install pyzbar
```

## Usage

1. Open a terminal or command prompt and navigate to the project directory.
2. Run the script by executing the following command:

```bash
python script.py
```

3. You will be prompted with a menu asking what you want to do. Enter your choice by typing the corresponding number or keyword:

- `1` or `encode` to encode text into a QR code.
- `2` or `decode` to decode QR codes from a live video stream.

4. Follow the on-screen instructions to provide the required information or use the webcam for decoding.

## Examples

### Encoding

- When prompted for information to encode, enter the text you want to convert into a QR code.

### Decoding

- The script will open a window displaying the video stream from your webcam.
- Hold a QR code in front of the camera.
- The script will detect and decode the QR code, displaying the type and data in the console.
- Press `q` to exit the script.
