Purpose: The project aims to provide a Python-based solution for encoding and decoding QR codes.
Encoding: The script allows users to input information they want to encode into a QR code using the encoder() function. The qrcode library is used to generate the QR code image, which is saved as a png file.
Decoding: The decoder() function uses the OpenCV library to access the camera and continuously captures frames. It utilizes the pyzbar library to detect and decode QR codes from the frames, displaying the results on the frame itself.
User Interaction: The script prompts the user to choose between encoding and decoding. Based on the input, the corresponding function is executed. The user can enter the information to be encoded or view the real-time decoding of QR codes from the camera feed.
Libraries Used: The project relies on the cv2 library for camera access and frame processing, the qrcode library for QR code generation, and the pyzbar library for QR code decoding.
In summary, this project provides a Python solution for generating and reading QR codes, offering a convenient way to encode and decode information using QR codes. 
