import sys

ORD_A = 65
ORD_X = 88


def calculate_score(game):
    """
    Calculate score from opponent vs my draw.

    A = Rock
    B = Paper
    C = Scissor

    X = Rock
    Y = Paper
    Z = Scissor
    """

    score = ord(game[1]) - ORD_X + 1

    # Check for a win or draw
    if (
        (game[0] == "A" and game[1] == "Y")
        or (game[0] == "B" and game[1] == "Z")
        or (game[0] == "C" and game[1] == "X")
    ):
        score += 6
    elif (ord(game[0]) - ORD_A) == (ord(game[1]) - ORD_X):
        score += 3

    return score


def calculate_score_2(game):
    """
    Calculate score from opponent vs my draw given outcome.

    A = Rock
    B = Paper
    C = Scissor

    X = lose
    Y = draw
    Z = win
    """

    selections = ["A", "B", "C"]

    score = 0
    if game[1] == "X":
        selection = selections[selections.index(game[0])-1]
    elif game[1] == "Y":
        score += 3
        selection = game[0]
    else:
        score += 6
        selection = selections[(selections.index(game[0])+1) % len(selections)]

    score += ord(selection) - ORD_A + 1

    return score


if __name__ == "__main__":
    in_data = sys.argv[1]
    with open(in_data, "r") as fh:
        lines = [line.strip() for line in fh.readlines()]

    games = [line.split(" ") for line in lines]

    score = 0
    for game in games:
        score += calculate_score(game)

    print("[Task 1] Total score is: {}".format(score))

    score = 0
    for game in games:
        score += calculate_score_2(game)

    print("[Task 2] Total score is: {}".format(score))
