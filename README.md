# Fruit-Detection-Robot-with-OpenCV-and-Webots
This project demonstrates a fruit detection system using OpenCV for image processing and Webots for simulating robotic arm control. The system uses computer vision to identify objects, and a simulated robotic arm in Webots performs actions like picking and dropping fruits.
Fruit Detection Robot with OpenCV and Webots
Overview
This project combines computer vision and robotics to simulate a robotic arm that detects and interacts with fruits (apples and oranges) in a virtual environment. Using OpenCV for real-time image processing, the robot can identify fruits based on color and shape, and a Webots simulation controls the robotic arm to perform tasks such as picking and dropping fruits.

# Key Features
Real-time Fruit Detection: Detects apples and oranges using OpenCV by color segmentation and contour analysis.
Simulated Robotic Arm: The Webots simulator controls the arm for fruit picking and dropping tasks.
Customizable: Easily extendable to detect other objects or to refine detection methods.
Performance Feedback: Displays detection information, including fruit counts, on the terminal and GUI.
![Universal Robot](https://github.com/user-attachments/assets/22858180-f11c-4237-981c-c750c8bacf3c)

# Technologies Used
Python: Main programming language.
OpenCV: For image processing and object detection.
Webots: Simulation environment for robotics.
Numpy: For image data handling and mathematical operations.

# Setup Instructions
## Prerequisites
Ensure you have the following installed:

Python 3.x
OpenCV
Numpy
Webots
Installation Steps
Clone the repository:

bash
Copy code
git clone https://github.com/ankur-mali/Fruit-Detection-Robot.git
Navigate into the project directory:

bash
Copy code
cd Fruit-Detection-Robot
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Run the OpenCV webcam version:

bash
Copy code
python fruit_detection_webcam.py
To run the full simulation with Webots, follow these steps:

Open the Webots project file and start the simulation.
Run the Python controller script for the robotic arm.
Usage
Start the Webots simulation and observe how the robotic arm interacts with fruits based on the image data.


# Future Improvements
Improve fruit detection by using machine learning models.
Add more fruit types and refine detection methods to avoid false positives (like skin being detected as fruit).
Integrate the project with cloud platforms like Google Cloud or Azure for remote simulation control.
## Contributing
Feel free to contribute by submitting pull requests or reporting issues. Contributions to improve the detection algorithm or simulation environment are welcome!

## License
This is for educational purpose only
