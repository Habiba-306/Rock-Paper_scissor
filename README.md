# ✊✋✌️ Rock-Paper-Scissors Computer Vision Game

An interactive, AI-powered **Rock-Paper-Scissors** game built using **Python**, **OpenCV**, and **cvzone**. Play directly against an AI opponent in real-time by simply showing hand gestures to your webcam!

---

## ✨ Features

* **Real-Time Hand Tracking:** Uses the `cvzone` HandTrackingModule to accurately detect and classify your hand gestures instantly.
* **Smart Gesture Recognition:** * ✊ **Rock:** All fingers closed.
* ✋ **Paper:** All fingers open.
* ✌️ **Scissors:** Index and middle fingers open.


* **Automated Gameplay Loop:** Built-in start triggers, visual countdown timers, and automated scoring tracking for both the Player and AI.
* **Custom UI Overlays:** Seamlessly overlays PNG graphics and live web feeds onto a unified background dashboard.

---

## 🛠️ Prerequisites & Installation

Ensure you have **Python 3.8+** installed along with a functional webcam.

### 1. Clone or Setup the Project Folder

Create your project directory and place the main script inside it.

### 2. Install Dependencies

Install the required libraries via pip:

```bash
pip install opencv-python cvzone mediapipe

```

*(Note: `mediapipe` is required in the background as the backend engine for `cvzone`'s hand detection).*

### 3. Setup the Resources Folder

The game relies on custom graphical assets to render the UI. Ensure you have a folder named `resources` in your project directory containing:

* **`BG.png`**: The main interface background image (dimensions should accommodate a 1280x720 window layout as targeted by the overlay coordinates).
* **`1.png`**: AI graphic for Rock.
* **`2.png`**: AI graphic for Paper.
* **`3.png`**: AI graphic for Scissors.

*(Note: Update the absolute file paths in the script if your `resources` folder is located in a different directory).*

---

## 🚀 How to Play

Launch the game from your terminal:

```bash
python main.py

```

### Game Controls:

* **Start Round (`s`):** Press the **`s`** key on your keyboard to trigger the 2-second countdown timer.
* **Make Your Move:** Hold your hand gesture (Rock, Paper, or Scissors) clearly inside the webcam frame before the timer hits zero.
* **Quit Game (`q`):** Press the **`q`** key at any time to safely close the camera feed and exit the application.

---

## 🎮 Game Rules & Scoring

1. **Win/Loss Conditions:** Standard Rock-Paper-Scissors rules apply (Rock beats Scissors, Scissors beats Paper, Paper beats Rock).
2. **Ties:** If both you and the AI choose the same move, a **"Tie!"** message renders on screen for 3 seconds, and no points are awarded.
3. **Score Tracking:** The dashboard maintains a persistent score counter at the top of the screen for the duration of the session.

---

## 📝 License

This project is developed for academic purposes at the University of Haripur.
All rights reserved © .
