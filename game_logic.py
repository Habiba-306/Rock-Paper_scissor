def detect_player_gesture(hands, detector):
    """Return player move (1=Rock, 2=Paper, 3=Scissors) or None."""
    if not hands:
        return None
    
    hand = hands[0]
    fingers = detector.fingersUp(hand)
    
    if fingers == [0, 0, 0, 0, 0]:
        return 1  # Rock
    elif fingers == [1, 1, 1, 1, 1]:
        return 2  # Paper
    elif fingers == [0, 1, 1, 0, 0]:
        return 3  # Scissors
    return None


def determine_winner(player_move, ai_move):
    """
    Returns:
        1 -> Player wins
        -1 -> AI wins
        0 -> Tie
    """
    if player_move == ai_move:
        return 0  # Tie
    
    # Player wins if:
    # Rock(1) beats Scissors(3), Paper(2) beats Rock(1), Scissors(3) beats Paper(2)
    if (player_move == 1 and ai_move == 3) or \
       (player_move == 2 and ai_move == 1) or \
       (player_move == 3 and ai_move == 2):
        return 1  # Player wins
    return -1  # AI wins
