# 2048.py

# importing the logic.py file
# where we have written all the
# logic functions used.
import logic


def handle_move(mat, move_function):
    mat, flag = move_function(mat)
    status = logic.get_current_state(mat)
    print(status)
    if status == "GAME NOT OVER":
        logic.add_new_2(mat)
    return mat, status


# Driver code
if __name__ == "__main__":

    # calling start_game function
    # to initialize the matrix
    mat = logic.start_game()

    while True:
        # taking the user input
        # for next step
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

        if status != "GAME NOT OVER":
            break

        # print the matrix after each move
        for row in mat:
            print(row)
