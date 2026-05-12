import random
import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector
import time

# Initialize camera
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

# Initialize hand detector
detector = HandDetector(maxHands=1)

# Game variables
timer = 0
stateResult = False
startGame = False
scores = [0, 0]  # [AI, Player]
tieTimer = 0  # Tie timer initialization
showTieMessage = False  # Flag to control tie message visibility
gameOver = False  # Flag to control game over state

while True:
    imgBG = cv2.imread(
        r"C:\Users\PMYLS\OneDrive - Higher Education Commission\Desktop\habibaa\project AI\venv\Rope-Paper\resources\BG.png")
    if imgBG is None:
        print("Error: Background image 'BG.png' not found in the resources folder!")
        break

    success, img = cap.read()
    if not success:
        print("Error: Could not read from camera!")
        break

    imgScaled = cv2.resize(img, (0, 0), None, 0.875, 0.875)
    imgScaled = imgScaled[:, 80:480]

    # Find Hands
    hands, img = detector.findHands(imgScaled)  # with draw

    if startGame:
        if not stateResult:
            timer = time.time() - initialTime
            cv2.putText(imgBG, str(int(timer)), (605, 435),
                        cv2.FONT_HERSHEY_PLAIN, 6, (255, 0, 255), 4)

            if timer > 2:
                stateResult = True
                timer = 0

                if hands:
                    playerMove = None
                    hand = hands[0]
                    fingers = detector.fingersUp(hand)

                    if fingers == [0, 0, 0, 0, 0]:
                        playerMove = 1  # Rock
                    elif fingers == [1, 1, 1, 1, 1]:
                        playerMove = 2  # Paper
                    elif fingers == [0, 1, 1, 0, 0]:
                        playerMove = 3  # Scissors

                    # AI move
                    randomNumber = random.randint(1, 3)
                    imgAI = cv2.imread(
                        f"C:\\Users\\PMYLS\\OneDrive - Higher Education Commission\\Desktop\\habibaa\\project AI\\venv\\Rope-Paper\\resources\\{randomNumber}.png", cv2.IMREAD_UNCHANGED)
                    # "C:\Users\PMYLS\Desktop\habiba\project AI\resources\1.png"
                    if imgAI is None:
                        print(
                            f"Error: AI move image '{randomNumber}.png' not found!")
                    else:
                        imgBG = cvzone.overlayPNG(imgBG, imgAI, (149, 310))

                    # Check game result
                    if playerMove == randomNumber:
                        tieTimer = time.time()
                        showTieMessage = True
                    else:
                        # Player Wins
                        if (playerMove == 1 and randomNumber == 3) or \
                           (playerMove == 2 and randomNumber == 1) or \
                           (playerMove == 3 and randomNumber == 2):
                            scores[1] += 1
                        # AI Wins
                        else:
                            scores[0] += 1

    # Display "Game Tie!" message for 3 seconds
    if showTieMessage:
        cv2.putText(imgBG, "Tie!", (500, 600),
                    cv2.FONT_HERSHEY_PLAIN, 6, (0, 255, 0), 6)
        if time.time() - tieTimer > 3:
            showTieMessage = False
            tieTimer = 0

    imgBG[234:654, 795:1195] = imgScaled

    if stateResult:
        if imgAI is not None:
            imgBG = cvzone.overlayPNG(imgBG, imgAI, (149, 310))

    cv2.putText(imgBG, str(scores[0]), (410, 215),
                cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 6)
    cv2.putText(imgBG, str(scores[1]), (1112, 215),
                cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 6)

    cv2.imshow("BG", imgBG)

    key = cv2.waitKey(1)
    if key == ord('s'):
        startGame = True
        initialTime = time.time()
        stateResult = False

    if key == ord('q'):  # Press 'q' to quit
        break

cap.release()
cv2.destroyAllWindows()
