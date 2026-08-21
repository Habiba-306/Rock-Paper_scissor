
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
```

---

### 🖐️ How Gesture Recognition Works

**Step 1: Hand Landmark Detection**  
MediaPipe detects 21 hand landmarks in 3D space (x, y, z coordinates).

**Step 2: Finger State Detection**  
The `fingersUp()` method determines if each finger is extended:

- Index finger (landmark 8): Extended if y-coordinate < landmark 5 (knuckle)
- Middle finger (landmark 12): Extended if y-coordinate < landmark 9
- Ring finger (landmark 16): Extended if y-coordinate < landmark 13
- Pinky (landmark 20): Extended if y-coordinate < landmark 17
- Thumb (landmark 4): Extended if x-coordinate < landmark 2 (for right hand)

**Step 3: Gesture Mapping**
                                        
                                        | Gesture   | Finger Pattern          | Landmark Logic                         |
                                        |-----------|--------------------------|----------------------------------------|
                                        | ✊ Rock   | All fingers down        | All tips below knuckles                |
                                        | 🖐️ Paper | All fingers up          | All tips above knuckles                |
                                        | ✌️ Scissors| Index + Middle up       | Only landmarks 8 and 12 extended       |

---

## 📁 Project Structure

```
Rock-Paper-Scissors/
├── main.py              # Main game loop and GUI
├── hand_tracker.py      # Hand detection and gesture classification
├── game_logic.py        # Rock-Paper-Scissors game rules
├── requirements.txt     # Dependencies
├── README.md            # This file
└── .gitignore           # Git ignore rules
```

---

## 🎮 Game Logic

The AI opponent randomly selects Rock, Paper, or Scissors. Standard rules apply:

<table align="center" style="border-collapse: collapse; font-size: 1.1em; text-align: center; width: 70%; margin: 20px auto; border-radius: 12px; overflow: hidden; box-shadow: 0 8px 16px rgba(0,0,0,0.1);">
  <thead>
    <tr style="background: #2c3e50; color: #ffffff; font-weight: bold; text-transform: uppercase; letter-spacing: 0.5px;">
      <th style="padding: 14px 10px; border-right: 1px solid #444;">🧑 Player</th>
      <th style="padding: 14px 10px; border-right: 1px solid #444;">🤖 AI</th>
      <th style="padding: 14px 10px;">🏆 Result</th>
    </tr>
  </thead>
  <tbody>
    <!-- Win rows -->
    <tr style="background: #eafaf1; border-bottom: 1px solid #ddd;">
      <td style="padding: 12px;">✊ Rock</td>
      <td style="padding: 12px;">✌️ Scissors</td>
      <td style="padding: 12px; font-weight: bold; color: #1e8449;">✅ Win</td>
    </tr>
    <tr style="background: #fdedec; border-bottom: 1px solid #ddd;">
      <td style="padding: 12px;">✊ Rock</td>
      <td style="padding: 12px;">🖐️ Paper</td>
      <td style="padding: 12px; font-weight: bold; color: #922b21;">❌ Lose</td>
    </tr>
    <tr style="background: #eafaf1; border-bottom: 1px solid #ddd;">
      <td style="padding: 12px;">🖐️ Paper</td>
      <td style="padding: 12px;">✊ Rock</td>
      <td style="padding: 12px; font-weight: bold; color: #1e8449;">✅ Win</td>
    </tr>
    <tr style="background: #fdedec; border-bottom: 1px solid #ddd;">
      <td style="padding: 12px;">🖐️ Paper</td>
      <td style="padding: 12px;">✌️ Scissors</td>
      <td style="padding: 12px; font-weight: bold; color: #922b21;">❌ Lose</td>
    </tr>
    <tr style="background: #eafaf1; border-bottom: 1px solid #ddd;">
      <td style="padding: 12px;">✌️ Scissors</td>
      <td style="padding: 12px;">🖐️ Paper</td>
      <td style="padding: 12px; font-weight: bold; color: #1e8449;">✅ Win</td>
    </tr>
    <tr style="background: #fdedec; border-bottom: 1px solid #ddd;">
      <td style="padding: 12px;">✌️ Scissors</td>
      <td style="padding: 12px;">✊ Rock</td>
      <td style="padding: 12px; font-weight: bold; color: #922b21;">❌ Lose</td>
    </tr>
    <!-- Tie row -->
    <tr style="background: #fef9e7;">
      <td style="padding: 12px; font-weight: 500;">🔄 Same</td>
      <td style="padding: 12px; font-weight: 500;">🔄 Same</td>
      <td style="padding: 12px; font-weight: bold; color: #b7950b;">🤝 Tie</td>
    </tr>
  </tbody>
</table>

---

<h3 align="center">📊 Performance</h3>

<table align="center" style="border-collapse: collapse; font-size: 1em; text-align: left; width: 65%; margin: 10px auto; border-radius: 12px; overflow: hidden; box-shadow: 0 8px 16px rgba(0,0,0,0.08);">
  <thead>
    <tr style="background: #2c3e50; color: #ffffff; font-weight: bold; text-transform: uppercase; letter-spacing: 0.5px;">
      <th style="padding: 14px 20px; border-right: 1px solid #444;">⚙️ Metric</th>
      <th style="padding: 14px 20px;">📈 Value</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background: #f8f9fa; border-bottom: 1px solid #e9ecef;">
      <td style="padding: 12px 20px; border-right: 1px solid #e9ecef;">Gesture Classification Speed</td>
      <td style="padding: 12px 20px; font-weight: 500; color: #1a73e8;">&lt; 10ms</td>
    </tr>
    <tr style="background: #ffffff; border-bottom: 1px solid #e9ecef;">
      <td style="padding: 12px 20px; border-right: 1px solid #e9ecef;">Frame Rate</td>
      <td style="padding: 12px 20px; font-weight: 500; color: #1a73e8;">15-30 FPS</td>
    </tr>
    <tr style="background: #f8f9fa; border-bottom: 1px solid #e9ecef;">
      <td style="padding: 12px 20px; border-right: 1px solid #e9ecef;">Hand Tracking Accuracy</td>
      <td style="padding: 12px 20px; font-weight: 500; color: #2e7d32;">✅ High (MediaPipe)</td>
    </tr>
    <tr style="background: #ffffff; border-bottom: 1px solid #e9ecef;">
      <td style="padding: 12px 20px; border-right: 1px solid #e9ecef;">No. of Hand Landmarks</td>
      <td style="padding: 12px 20px; font-weight: 500; color: #1a73e8;">21</td>
    </tr>
    <tr style="background: #f8f9fa;">
      <td style="padding: 12px 20px; border-right: 1px solid #e9ecef;">Gestures Supported</td>
      <td style="padding: 12px 20px; font-weight: 500; color: #1a73e8;">3 (✊ Rock, 🖐️ Paper, ✌️ Scissors)</td>
    </tr>
  </tbody>
</table>

<br>

<h3 align="center">🛠️ Tech Stack</h3>

<table align="center" style="border-collapse: collapse; font-size: 1em; text-align: left; width: 65%; margin: 10px auto; border-radius: 12px; overflow: hidden; box-shadow: 0 8px 16px rgba(0,0,0,0.08);">
  <thead>
    <tr style="background: #2c3e50; color: #ffffff; font-weight: bold; text-transform: uppercase; letter-spacing: 0.5px;">
      <th style="padding: 14px 20px; border-right: 1px solid #444;">🧩 Component</th>
      <th style="padding: 14px 20px;">⚡ Technology</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background: #f8f9fa; border-bottom: 1px solid #e9ecef;">
      <td style="padding: 12px 20px; border-right: 1px solid #e9ecef;">Language</td>
      <td style="padding: 12px 20px; font-weight: 500; color: #1a73e8;">Python 3.7+</td>
    </tr>
    <tr style="background: #ffffff; border-bottom: 1px solid #e9ecef;">
      <td style="padding: 12px 20px; border-right: 1px solid #e9ecef;">Hand Tracking</td>
      <td style="padding: 12px 20px; font-weight: 500; color: #1a73e8;">MediaPipe</td>
    </tr>
    <tr style="background: #f8f9fa; border-bottom: 1px solid #e9ecef;">
      <td style="padding: 12px 20px; border-right: 1px solid #e9ecef;">Gesture Classification</td>
      <td style="padding: 12px 20px; font-weight: 500; color: #1a73e8;">cvzone HandTrackingModule</td>
    </tr>
    <tr style="background: #ffffff; border-bottom: 1px solid #e9ecef;">
      <td style="padding: 12px 20px; border-right: 1px solid #e9ecef;">Image Processing</td>
      <td style="padding: 12px 20px; font-weight: 500; color: #1a73e8;">OpenCV</td>
    </tr>
    <tr style="background: #f8f9fa;">
      <td style="padding: 12px 20px; border-right: 1px solid #e9ecef;">GUI</td>
      <td style="padding: 12px 20px; font-weight: 500; color: #1a73e8;">OpenCV window + custom overlays</td>
    </tr>
  </tbody>
</table>

## 📸 Demo

[Add a GIF or screenshot here]

---


## 📫 Connect

[![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white)](https://github.com/Habiba-306)  
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat&logo=linkedin&logoColor=white)](https://linkedin.com/in/yourprofile)  
[![Email](https://img.shields.io/badge/Email-D14836?style=flat&logo=gmail&logoColor=white)](mailto:youremail@example.com)

---

## 📝 License

This project is developed for academic purposes at the University of Haripur.
Feel free to use and modify.

---
⭐ If you found this helpful, consider giving it a star!
```
