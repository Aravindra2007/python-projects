import cv2

camera = cv2.VideoCapture(0)

success,image = camera.read()

# if success:
#     cv2.imwrite("ak.jpg",image)


while True:
        if not camera.isOpened():
            print("Error: Could not open camera.")
        else:
            # Read a frame from the camera
            success, image = camera.read()

        if success:
                # Save the captured image
                cv2.imwrite("ak.jpg", image)
                print("Image saved as ak.jpg")
        else:
                print("Error: Failed to capture image.")

# Release the camera resource
#camera.release()