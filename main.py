import random
import cv2
import cvzone
import os
import time
from cvzone.HandTrackingModule import HandDetector

# Import functions from game_logic
from game_logic import detect_player_gesture, determine_winner

# ────────────────────────────────────────────────
# Configuration
# ────────────────────────────────────────────────

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RESOURCES_DIR = os.path.join(BASE_DIR, "resources")

# ────────────────────────────────────────────────
# Game Functions
# ────────────────────────────────────────────────

def load_resource(filename, unchanged=True):
    """Load an image from the resources directory."""
    path = os.path.join(RESOURCES_DIR, filename)
    if unchanged:
        img = cv2.imread(path, cv2.IMREAD_UNCHANGED)
    else:
        img = cv2.imread(path)
    if img is None:
        raise FileNotFoundError(f"Resource not found: {path}")
    return img

# ────────────────────────────────────────────────
# Main Game Loop
# ────────────────────────────────────────────────

def main():
    # Initialize camera
    cap = cv2.VideoCapture(0)
    cap.set(3, 640)
    cap.set(4, 480)

    # Initialize hand detector
    detector = HandDetector(maxHands=1)

    # Load background
    try:
        imgBG = load_resource("BG.png", unchanged=False)
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return

    # Game state
    timer = 0
    initialTime = 0
    stateResult = False
    startGame = False
    scores = [0, 0]  # [AI, Player]
    tieTimer = 0
    showTieMessage = False
    current_ai_image = None
    
    # ── New End Game Variables ──
    rounds_played = 0
    gameOver = False
    gameOverTime = 0

    print("🎮 Rock-Paper-Scissors Game")
    print("Press 's' to start a round")
    print("Press 'e' to end the game early")
    print("Press 'q' to quit")

    # Name the window and force it to be a fixed size
    cv2.namedWindow("Rock-Paper-Scissors", cv2.WINDOW_AUTOSIZE)

    while True:
        # Create a copy of background for each frame
        imgBG_display = imgBG.copy()

        # Read camera
        success, img = cap.read()
        if not success:
            print("Error: Could not read from camera!")
            break

        # Resize and crop
        imgScaled = cv2.resize(img, (0, 0), None, 0.875, 0.875)
        imgScaled = imgScaled[:, 80:480]

        # Detect hands (only if game is not over)
        if not gameOver:
            hands, img = detector.findHands(imgScaled)
        else:
            hands = []

        # ── Game Logic ────────────────────────────────────
        if startGame and not gameOver:
            if not stateResult:
                # Countdown phase
                timer = time.time() - initialTime
                cv2.putText(imgBG_display, str(int(timer)), (605, 435),
                            cv2.FONT_HERSHEY_PLAIN, 6, (255, 0, 255), 4)

                if timer > 2:
                    stateResult = True
                    timer = 0

                    # Capture player gesture
                    playerMove = detect_player_gesture(hands, detector)

                    if playerMove is not None:
                        # AI selects random move
                        randomNumber = random.randint(1, 3)

                        # Load AI image
                        try:
                            current_ai_image = load_resource(f"{randomNumber}.png")
                        except FileNotFoundError:
                            current_ai_image = None

                        # Determine winner
                        result = determine_winner(playerMove, randomNumber)

                        if result == 0:
                            tieTimer = time.time()
                            showTieMessage = True
                            if rounds_played < 9:
                                rounds_played += 1
                        elif result == 1:
                            scores[1] += 1  # Player wins
                            rounds_played += 1
                        else:
                            scores[0] += 1  # AI wins
                            rounds_played += 1
                        
                        # Trigger game over ONLY if 10+ rounds are played AND there is a clear winner
                        if rounds_played >= 10 and scores[0] != scores[1]:
                            gameOverTime = time.time()
                            
                    else:
                        # No hand detected — skip this round
                        print("No hand detected. Try again.")
                        startGame = False
                        stateResult = False
                        continue

        # Check if 10 rounds are over and 2 seconds have passed to show result
        if not gameOver and gameOverTime > 0 and time.time() - gameOverTime > 2:
            gameOver = True
            startGame = False
            stateResult = False

        # ── UI Rendering ──────────────────────────────────

        # Overlay camera feed
        imgBG_display[234:654, 795:1195] = imgScaled

        # Display AI result if round is complete
        if stateResult and current_ai_image is not None and not gameOver:
            imgBG_display = cvzone.overlayPNG(imgBG_display, current_ai_image, (149, 310))

        # Show "Tie!" message
        if showTieMessage and not gameOver:
            cv2.putText(imgBG_display, "Tie!", (500, 600),
                        cv2.FONT_HERSHEY_PLAIN, 6, (0, 255, 0), 6)
            if time.time() - tieTimer > 3:
                showTieMessage = False
                tieTimer = 0

        # Update scores
        cv2.putText(imgBG_display, str(scores[0]), (410, 215),
                    cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 6)
        cv2.putText(imgBG_display, str(scores[1]), (1112, 215),
                    cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 6)

        # Show instructions at the bottom
        if not startGame and not gameOver:
            cv2.putText(imgBG_display, "Press 'S' to start | 'E' to end", (350, 700),
                        cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 0), 3)
        elif stateResult and not gameOver and rounds_played < 10:
            cv2.putText(imgBG_display, "Press 'S' for next round | 'E' to end", (250, 700),
                        cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 0), 3)

        # Show Current Level / Round / Tie-Breaker
        if not gameOver:
            if rounds_played >= 10 and scores[0] == scores[1]:
                level_text = "SUDDEN DEATH TIE-BREAKER!"
                color = (0, 0, 255) # Red for tension!
            elif rounds_played == 9 and showTieMessage:
                level_text = "FINAL ROUND REPLAY!"
                color = (0, 165, 255) # Orange for replay hype!
            else:
                current_level = rounds_played + 1
                if current_level > 10:
                    current_level = 10
                level_text = f"Round {current_level} / 10"
                color = (180, 220, 255) # Pastel yellow
                
            font_level = cv2.FONT_HERSHEY_DUPLEX
            l_size = cv2.getTextSize(level_text, font_level, 1.2, 2)[0]
            l_x = 640 - (l_size[0] // 2)  # Assuming ~1280 width
            
            # Draw text with a black outline
            cv2.putText(imgBG_display, level_text, (l_x, 160), font_level, 1.2, (0, 0, 0), 5)
            cv2.putText(imgBG_display, level_text, (l_x, 160), font_level, 1.2, color, 2)

        # ── Game Over Screen ──
        if gameOver:
            # 1. Dim the background with a semi-transparent black overlay
            overlay = imgBG_display.copy()
            cv2.rectangle(overlay, (0, 0), (1280, 720), (0, 0, 0), cv2.FILLED)
            # You can adjust 0.7 and 0.3 for darker/lighter dimming
            imgBG_display = cv2.addWeighted(overlay, 0.7, imgBG_display, 0.3, 0)
            
            # Load the custom winner image based on who won
            try:
                if scores[1] > scores[0]:
                    win_img = load_resource("winner_you.png", unchanged=True)
                elif scores[0] > scores[1]:
                    win_img = load_resource("winner_AI.png", unchanged=True)
                else:
                    win_img = None  # Fallback for Tie
            except FileNotFoundError:
                win_img = None
                
            font = cv2.FONT_HERSHEY_DUPLEX
                
            if win_img is not None:
                # If image exists, resize it to fit in the center nicely (600x350)
                win_img = cv2.resize(win_img, (600, 350))
                
                # Paste the image (handles both transparent PNGs and flat JPGs)
                if win_img.shape[2] == 4:
                    imgBG_display = cvzone.overlayPNG(imgBG_display, win_img, (340, 150))
                else:
                    imgBG_display[150:500, 340:940] = win_img
                    
                # Final Score below the image
                score_text = f"Final Score: {scores[1]} - {scores[0]}"
                score_size = cv2.getTextSize(score_text, font, 1.2, 3)[0]
                score_x = 340 + (600 - score_size[0]) // 2
                cv2.putText(imgBG_display, score_text, (score_x, 550), font, 1.2, (255, 255, 255), 3)
                
                # Instructions
                inst_text = "Press 'S' to Restart | 'Q' to Quit"
                inst_size = cv2.getTextSize(inst_text, font, 0.8, 2)[0]
                inst_x = 340 + (600 - inst_size[0]) // 2
                cv2.putText(imgBG_display, inst_text, (inst_x, 600), font, 0.8, (200, 200, 200), 2)
                
            else:
                # ── Fallback (If Tie or missing image) ──
                cv2.rectangle(imgBG_display, (340, 200), (940, 550), (255, 255, 255), cv2.FILLED)
                cv2.rectangle(imgBG_display, (340, 200), (940, 550), (0, 0, 0), 5)
                
                if scores[1] > scores[0]:
                    text, color = "YOU WON THE MATCH!", (0, 200, 0)
                elif scores[0] > scores[1]:
                    text, color = "AI WON THE MATCH!", (0, 0, 200)
                else:
                    text, color = "MATCH TIED!", (255, 0, 0)
                    
                text_size = cv2.getTextSize(text, font, 1.5, 4)[0]
                text_x = 340 + (600 - text_size[0]) // 2
                cv2.putText(imgBG_display, text, (text_x, 300), font, 1.5, color, 4)
                
                score_text = f"Final Score: {scores[1]} - {scores[0]}"
                score_size = cv2.getTextSize(score_text, font, 1.2, 3)[0]
                score_x = 340 + (600 - score_size[0]) // 2
                cv2.putText(imgBG_display, score_text, (score_x, 400), font, 1.2, (0, 0, 0), 3)
                
                inst_text1 = "Press 'S' to Restart"
                inst_text2 = "Press 'Q' to Quit"
                i_x1 = 340 + (600 - cv2.getTextSize(inst_text1, font, 0.8, 2)[0][0]) // 2
                i_x2 = 340 + (600 - cv2.getTextSize(inst_text2, font, 0.8, 2)[0][0]) // 2
                cv2.putText(imgBG_display, inst_text1, (i_x1, 480), font, 0.8, (100, 100, 100), 2)
                cv2.putText(imgBG_display, inst_text2, (i_x2, 520), font, 0.8, (100, 100, 100), 2)

        # Display
        cv2.imshow("Rock-Paper-Scissors", imgBG_display)

        # ── Key Handling ─────────────────────────────────
        key = cv2.waitKey(1)
        
        if key == ord('s'):
            if gameOver:
                # Completely Reset Game
                startGame = False
                stateResult = False
                current_ai_image = None
                scores = [0, 0]
                rounds_played = 0
                gameOver = False
                gameOverTime = 0
            elif rounds_played < 10 or (rounds_played >= 10 and scores[0] == scores[1]):
                # Start Next Round
                startGame = True
                stateResult = False
                current_ai_image = None
                initialTime = time.time()
                
        if key == ord('e') and not gameOver:
            # End game early manually
            gameOver = True
            startGame = False
            stateResult = False

        if key == ord('q'):
            break

    # Cleanup
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
