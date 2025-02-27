import logic
import os


def handle_move(mat, move_function):
    mat, flag = move_function(mat)
    status = logic.get_current_state(mat)
    print(status)
    if status == "GAME NOT OVER":
        logic.add_new_2(mat)
    return mat, status


def save_high_score(score):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    high_score_file = os.path.join(script_dir, "highscore.txt")

    if os.path.exists(high_score_file):
        with open(high_score_file, "r") as file:
            high_score = int(file.read())
    else:
        high_score = 0

    if score > high_score:
        with open(high_score_file, "w") as file:
            file.write(str(score))
        print(f"New high score: {score}")
    else:
        print(f"High score: {high_score}")


# Driver code
if __name__ == "__main__":
    mat = logic.start_game()
    score = 0

    while True:
        x = input("Press the command : ").upper()

        if x == "W":
            mat, status = handle_move(mat, logic.move_up)
        elif x == "S":
            mat, status = handle_move(mat, logic.move_down)
        elif x == "A":
            mat, status = handle_move(mat, logic.move_left)
        elif x == "D":
            mat, status = handle_move(mat, logic.move_right)
        else:
            print("Invalid Key Pressed")
            continue

        score = logic.calculate_score(mat)

        if status != "GAME NOT OVER":
            save_high_score(score)
            break

        for row in mat:
            print(row)
