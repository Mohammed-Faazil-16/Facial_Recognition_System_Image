import cv2
from deepface import DeepFace

# Load the reference image (e.g., an image of Elon Musk)
reference_img = cv2.imread("reference.png")  # Path to the reference image
input_img = cv2.imread("elon_musk.png")  # Path to the input image you want to test

# Verify the face
try:
    result = DeepFace.verify(input_img, reference_img.copy())
    if result['verified']:
        print("MATCH!")
    else:
        print("NO MATCH!")
except ValueError:
    print("Error in processing the images")

# Display the input image with the result
if result['verified']:
    cv2.putText(input_img, "MATCH!", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)
else:
    cv2.putText(input_img, "NO MATCH!", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)

cv2.imshow('Result', input_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
