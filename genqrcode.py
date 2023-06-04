import cv2
import qrcode
from pyzbar.pyzbar import decode

def encoder():
    # Data to be encoded
    data = input("Enter the information that you want to encode: ")

    # Encoding data using make() function
    qr = qrcode.QRCode()
    qr.add_data(data)
    qr.make(fit=True)

    # Creating an image from the QR code
    img = qr.make_image()

    # Saving the image as a file
    img.save('MyQRCode1.png')
    print("QR code saved as MyQRCode1.png")


def decoder():
    cam = cv2.VideoCapture(0)
    cam.set(3, 640)  # Set width
    cam.set(4, 480)  # Set height

    while True:
        success, frame = cam.read()

        # Decoding QR codes from the frame
        barcodes = decode(frame)

        for barcode in barcodes:
            barcode_data = barcode.data.decode('utf-8')
            barcode_type = barcode.type

            # Drawing bounding box and text on the frame
            x, y, w, h = barcode.rect
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, 'Type: ' + barcode_type, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
            cv2.putText(frame, 'Data: ' + barcode_data, (x, y + h + 30), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

        cv2.imshow('QR Scanner', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()


print("What do you want to do?")
print("1. Encode")
print("2. Decode")

take_input = input()
x = take_input.lower()

if x in ['encode', '1', 'encoder']:
    encoder()
elif x in ['decode', '2', 'decoder']:
    decoder()
