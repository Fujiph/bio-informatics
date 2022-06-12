#Ask for sequences from the user
sequence_1 = input("Enter or paste sequence 1:")
sequence_2 = input("Enter or paste sequence 2:")
match_reward = input("Enter or paste match reward:")
mismatch_penalty = input("Enter or paste mismatch penalty:")
gap_penalty = input("Enter or paste gap penalty:")

# Constant varaibles
n_rows = len(sequence_1)
n_cols = len(sequence_2)

# Generate scoreboard as 2D array
score_board = []
for i in range(n_rows):
    col = []
    for j in range(n_cols):
        col.append(0)
    score_board.append(col)

# Needleman Wunsch alignment
for row in range(n_rows):
    for col in range(n_cols):        
        if row == 0 and col == 0:
            score = 0

        elif row == 0:
            previous_score = score_board[row][col - 1]
            score = previous_score + gap_penalty

        elif col == 0:
            previous_score = score_board[row -1][col]
            score = previous_score + gap_penalty

        else: 
            cell_to_the_left = score_board[row][col-1]
            from_left_score = cell_to_the_left + gap_penalty
             
            above_cell = score_board[row-1][col]
            from_above_score = above_cell + gap_penalty
            
            diagonal_left_cell = score_board[row-1][col-1]
            
            if sequence_1[row-1] == sequence_2[col-1]:
                diagonal_left_cell_score = diagonal_left_cell + mismatch_penalty
            else:
                diagonal_left_cell_score = diagonal_left_cell + mismatch_penalty
            
            score = max([from_left_score,from_above_score,diagonal_left_cell_score])

        score_board[row][col] = score

# Generate pretty display
def displayView():
    format_row = "{:>12}" * (n_rows + 1)
    print(format_row.format("", *sequence_1))
    for v, row in zip(sequence_2, score_board):
        print(format_row.format(v, *row))

# Display section
displayView()