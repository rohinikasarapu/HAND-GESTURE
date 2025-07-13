Gesture Control Interface - README
🖐️ Project Overview
This is a real-time hand gesture recognition system built with Python.
It uses a webcam to capture hand movements and maps specific gestures to keyboard actions using computer vision and automation libraries.
🚀 Features
- Real-time hand gesture detection using MediaPipe
- Maps gestures to arrow key inputs using PyAutoGUI
- Works offline with just a webcam and Python
- No external sensors or hardware needed
🧠 Gesture Mapping
| Gesture          | Action Triggered |
|------------------|------------------|
| ☝️ One Finger     | Up Arrow (↑)      |
| ✊ Fist           | Down Arrow (↓)    |
| ✌️ Peace Sign     | Left Arrow (←)    |
| 🖐️ Open Hand      | Right Arrow (→)   |
🛠️ Technologies Used
- Python 3.10
- OpenCV
- MediaPipe
- PyAutoGUI
📦 Installation
1. Clone the repository:
git clone https://github.com/yourusername/gesture-control.git

2. Navigate to the project folder:
cd gesture-control

3. Create and activate a virtual environment:
python -m venv venv
venv\Scripts\activate  (on Windows)

4. Install dependencies:
pip install opencv-python mediapipe pyautogui
▶️ Usage
1. Run the script:
python gesture_control.py

2. Make the defined gestures in front of your webcam.

3. Observe the corresponding key presses (try in Notepad or browser).
🧪 Testing
Try opening Notepad and using gestures to move the cursor. Observe how your hand movements translate into arrow key presses.
💡 Future Enhancements
- Add GUI overlay to display gesture labels
- Voice feedback on gesture detection using pyttsx3
- Support for additional gestures like thumbs up, OK sign
- Media control (volume, brightness)
📄 License
This project is licensed under the MIT License.
Feel free to fork, modify, and build on it!
🙋‍♀️ Author
Created by Kasarapu Rohini
GitHub: https://github.com/rohinikasarapu
LinkedIn:(https://www.linkedin.com/in/kasarapu-rohini-756ab52b7/)
