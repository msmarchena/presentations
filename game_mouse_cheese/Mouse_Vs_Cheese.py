# Mouse vs Cheese 
# Focus: variables, loops, conditionals, input()

BOARD_SIZE = 5
MOUSE = "M"
CHEESE = "C"
EMPTY = "."

# Start positions (row, col)
mouse_row, mouse_col = 0, 0
cheese_row, cheese_col = 4, 4
moves = 0

print("=== MOUSE vs CHEESE ===")
print("Controls: w=up, s=down, a=left, d=right")
print("Goal: Reach the cheese!")

while True:
    # --- Create the board step by step ---
    board = []                                # start with an empty board
    for row in range(BOARD_SIZE):             # for each row
        current_row = []                      # make a new empty row
        for col in range(BOARD_SIZE):         # for each column
            current_row.append(EMPTY)         # add EMPTY cell
        board.append(current_row)             # add row to board

    # --- Place mouse and cheese on the board ---
    # board[row][col] → row = vertical, col = horizontal
    board[mouse_row][mouse_col] = MOUSE  
    board[cheese_row][cheese_col] = CHEESE

    # --- Print the board ---
    print("\n" + "=" * (BOARD_SIZE * 2 + 1))
    for row in board:
        print("|" + " ".join(row) + "|")
    print("=" * (BOARD_SIZE * 2 + 1))
    print(f"Moves: {moves}")

    # --- Check win condition ---
    if mouse_row == cheese_row and mouse_col == cheese_col:
        print(f"\n🎉 YOU WIN! Total moves: {moves}")
        break

    # --- Player input ---
    move = input("Your move (w/a/s/d): ").lower()

    # --- Update position ---
    new_row, new_col = mouse_row, mouse_col
    if move == "w":      # up
        new_row -= 1
    elif move == "s":    # down
        new_row += 1
    elif move == "a":    # left
        new_col -= 1
    elif move == "d":    # right
        new_col += 1
    else:
        print("Invalid move! Use w/a/s/d.")
        continue  # skip rest of loop

# 👉 So the rule is:
# Change the row number → go up or down
# Change the col number → go left or right

    # --- Check boundaries ---
    if 0 <= new_row < BOARD_SIZE and 0 <= new_col < BOARD_SIZE:
        mouse_row, mouse_col = new_row, new_col
        moves += 1
    else:
        print("You hit the wall of the board!")
