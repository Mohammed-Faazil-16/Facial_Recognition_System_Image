Face Recognition with DeepFace
This project implements a real-time face recognition system using the DeepFace library. The system captures live video from a webcam, compares detected faces with a reference image, and displays whether there is a match or not.

Features
Real-time face detection and recognition using DeepFace.
Utilizes threading to handle face recognition tasks without slowing down the video stream.
Supports any reference image for face matching.
Displays live video with match status overlay.
Requirements
Python 3.x
OpenCV
DeepFace
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/face-recognition-deepface.git
cd face-recognition-deepface
Install the required packages:

You can install the required packages using pip:

bash
Copy code
pip install opencv-python deepface
Download the VGG-Face model weights:

DeepFace will automatically download the required model weights (like VGG-Face) when you run the code for the first time. Alternatively, you can manually download them from here.

Usage
Place your reference image:

Replace reference.png with the image of the person you want to recognize.

Run the project:

Execute the script to start the face recognition process:

bash
Copy code
python face_recognition.py
The script will open a webcam window and display "MATCH!" if the detected face matches the reference image, or "NO MATCH!" if it doesn't.

Exit the program:

Press the q key to quit the program.

How It Works
Video Capture:

The program captures video from the default webcam using OpenCV.
Face Verification:

Every 30 frames, the current frame is compared with the reference image using DeepFace's verify method.
The comparison is performed in a separate thread to ensure smooth video playback.
Display Results:

If the face in the frame matches the reference image, "MATCH!" is displayed on the video feed.
Otherwise, "NO MATCH!" is displayed.
Example Output

Contributing
Feel free to open issues or submit pull requests if you find bugs or want to add new features. Contributions are welcome!

License
This project is licensed under the MIT License. See the LICENSE file for more details.

Acknowledgments
Thanks to the DeepFace library for making face recognition easy to implement.
The project uses pre-trained models, including VGG-Face, for accurate face recognition.
