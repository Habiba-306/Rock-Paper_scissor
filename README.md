
# ✊ Rock-Paper-Scissors Game with Webcam

Real-time hand gesture recognition game using MediaPipe's 21-point hand landmark model and cvzone's HandTrackingModule.

[![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)]()
[![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=flat&logo=opencv&logoColor=white)]()
[![MediaPipe](https://img.shields.io/badge/MediaPipe-0097A7?style=flat&logo=google&logoColor=white)]()
[![cvzone](https://img.shields.io/badge/cvzone-FF6F00?style=flat&logo=python&logoColor=white)]()

---

## 🎮 Overview

This project implements a **real-time Rock-Paper-Scissors game** using computer vision. The game detects your hand gestures through your webcam and plays against an AI opponent.

**Key Innovation:** Gesture classification is done using **geometric reasoning** on hand landmarks, no external ML model training required. This makes the system fast, lightweight, and responsive.

---

## ✨ Features

- **Real-time Hand Tracking:** Uses MediaPipe's 21-point hand landmark model
- **Geometric Gesture Classification:** `fingersUp()` determines gestures via coordinate comparisons
- **Three Gestures Supported:**
  - ✊ Rock — All fingers down
  - 🖐️ Paper — All fingers up
  - ✌️ Scissors — Index + middle fingers up, others down
- **AI Opponent:** Random choice with visual feedback
- **10‑Round Match:** Play a best‑of‑10 series with a clear winner
- **Sudden Death Tie‑Breaker:** If tied after 10 rounds, the game continues until someone wins
- **Early Game End:** Press `E` to finish the match early
- **Game‑Over Screen:** Displays a winner image (`winner_you.png` or `winner_AI.png`) with the final score
- **Score Tracking:** Tracks wins, losses, and ties
- **Low-latency Gameplay:** Responsive interaction suitable for live play

---

## 🚀 Installation

### Prerequisites
- Python 3.7 or higher
- Webcam

---

### Step 1: Clone the Repository
```bash
git clone https://github.com/Habiba-306/Rock-Paper-Scissors.git
cd Rock-Paper-Scissors
``` 

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

Alternative (Manual Install):
```bash
pip install opencv-python mediapipe cvzone
```

### Step 3: Prepare Resources

Make sure the `resources/` folder contains the required images:

- **`BG.png`** – Background image (1280×720)
- **`1.png`**, **`2.png`**, **`3.png`** – AI move images (✊ Rock, 🖐️ Paper, ✌️ Scissors)
- **`winner_you.png`** – 🎉 Displayed when **you** win the match
- **`winner_AI.png`** – 🤖 Displayed when **AI** wins the match

### Step 4: Run the Game
```bash
python main.py
```

### Step 5: Play!

- Show your hand to the webcam
- Make a gesture: ✊ Rock, 🖐️ Paper, or ✌️ Scissors
- Press S to start a round
- The AI randomly selects its move – the result is displayed instantly
- After 10 rounds, the match ends – or press E to end early
- Press Q to quit at any time

---

## 📁 Project Structure

```
Rock-Paper-Scissors/
├── main.py              # Main game loop, UI, and match logic
├── game_logic.py        # Gesture detection and winner determination
├── hand_tracker.py      # Hand detection and gesture classification (if used)
├── resources/           # Images (background, AI moves, winner screens)
├── requirements.txt     # Dependencies
└──  README.md            # This file
```

---

## 🖐️ How Gesture Recognition Works

Gesture	Finger Pattern	Landmark Logic
- ✊ Rock	All fingers down	All tips below knuckles
- 🖐️ Paper	All fingers up	All tips above knuckles
- ✌️ Scissors	Index + Middle up	Only landmarks 8 and 12 extended

### 🎮 Game Logic

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


## 📊 Performance
<div align="center">

| Metric | Value |
|---|---|
| Gesture Classification Speed | < 10ms |
| Frame Rate | 15-30 FPS |
| Hand Tracking Accuracy | ✅ High (MediaPipe) |
| No. of Hand Landmarks | 21 |
| Gestures Supported | 3 (✊ Rock, 🖐️ Paper, ✌️ Scissors) |

</div>


## 🛠️ Tech Stack
<div align="center">
  
| Component | Technology |
|---|---|
| Language | Python 3.7+ |
| Hand Tracking | MediaPipe |
| Gesture Classification | cvzone HandTrackingModule |
| Image Processing | OpenCV |
| GUI | OpenCV window + custom overlays |

</div>


## 📸 Demo


<p align="center">
  <video width="600" controls autoplay muted loop playsinline>
    <source src="https://raw.githubusercontent.com/Habiba-306/Rock-Paper_scissor/main/demo.mp4" type="video/mp4">
    Your browser does not support the video tag.
  </video>
</p>

## 💡 Possible Extensions

  - Add multiplayer mode
  - Add voice feedback
  - Add gesture smoothing to reduce jitter
  - Add difficulty levels (AI with strategy, not random)
  - Save game history to CSV
  - Add hand orientation detection

## 📝 License

This project is developed for academic purposes at the University of Haripur.
Feel free to use and modify.


⭐ If you found this helpful, consider giving it a star!

---

## 📫 Connect

[![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white)](https://github.com/Habiba-306)  
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat&logo=linkedin&logoColor=white)](https://linkedin.com/in/habiba-javed)  
[![Email](https://img.shields.io/badge/Email-D14836?style=flat&logo=gmail&logoColor=white)](mailto:habibajaved150@gmail.com)

