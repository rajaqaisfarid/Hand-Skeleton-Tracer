# Hand Skeleton Tracer

A real-time computer vision application built with Python, OpenCV, and MediaPipe that maps 21 3D hand landmarks and toggles an isolated black-canvas "skeleton mode" when a finger snap is detected.

## Features
* **Real-Time Hand Landmark Tracking:** Detects and renders 21 skeletal keypoints across up to two hands simultaneously.
* **Gesture-Based Mode Switching:** Calculates the Euclidean distance between the thumb tip (Landmark 4) and middle fingertip (Landmark 12) with a frame cooldown to detect finger snaps without flickering.
* **Dual Display Modes:** Toggles seamlessly between live webcam overlay mode and a high-contrast black-canvas skeleton view.
* **One-Click Windows Launcher:** Includes `run.bat` to launch the application directly using the local `.venv` Python interpreter.

## Tech Stack
* **Language:** Python 3.11
* **Computer Vision & AI:** OpenCV (`opencv-python`), Google MediaPipe (`mediapipe==0.10.14`)
* **Matrix Operations:** NumPy

## Installation & Usage

1. **Clone the repository:**
   ```bash
   git clone https://github.com/rajaqaisfarid/Hand-Skeleton-Tracer.git
   cd Hand-Skeleton-Tracer
   ```

2. **Create and activate a Python 3.11 virtual environment:**
   ```bash
   py -3.11 -m venv .venv
   .venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the tracker:**
   ```bash
   python snap.py
   ```
   *(On Windows, you can also double-click `run.bat` after setup. Press **`q`** in the video window to exit.)*