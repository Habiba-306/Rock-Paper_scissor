# ✊ Rock-Paper-Scissors Game with Webcam

Real-time hand gesture recognition game using MediaPipe's 21-point hand landmark model and cvzone's HandTrackingModule.

[![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)]()
[![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=flat&logo=opencv&logoColor=white)]()
[![MediaPipe](https://img.shields.io/badge/MediaPipe-0097A7?style=flat&logo=google&logoColor=white)]()
[![cvzone](https://img.shields.io/badge/cvzone-FF6F00?style=flat&logo=python&logoColor=white)]()

---

## 🎮 Overview

This project implements a **real-time Rock-Paper-Scissors game** using computer vision. The game detects your hand gestures through your webcam and plays against an AI opponent.

**Key Innovation:** Gesture classification is done using **geometric reasoning** on hand landmarks — no external ML model training required. This makes the system fast, lightweight, and responsive.

---

## ✨ Features

- **Real-time Hand Tracking:** Uses MediaPipe's 21-point hand landmark model
- **Geometric Gesture Classification:** `fingersUp()` determines gestures via coordinate comparisons
- **Three Gestures Supported:**
  - ✊ Rock — All fingers down
  - 🖐️ Paper — All fingers up
  - ✌️ Scissors — Index + middle fingers up, others down
- **AI Opponent:** Random choice with visual feedback
- **Score Tracking:** Keeps track of wins, losses, and ties
- **Low-latency Gameplay:** Responsive interaction suitable for live play

---

## 🚀 Installation

### Prerequisites
- Python 3.7 or higher
- Webcam

### Steps

```bash
# 1. Clone the repository
git clone https://github.com/Habiba-306/Rock-Paper-Scissors.git
cd Rock-Paper-Scissors

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the game
python main.py
