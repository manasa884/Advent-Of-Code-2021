import pprint

pp = pprint.PrettyPrinter(indent=2)


# Part 1
def find_winner(numbers, boards):
    map = {}
    for num in numbers:
        for b_idx, board in enumerate(boards):
            for r_idx, row in enumerate(board):
                if num in row:
                    # Mark board
                    boards[b_idx][r_idx][row.index(num)] = '*'
                    # Update map
                    if str(b_idx) not in map:
                        map[str(b_idx)] = [num]
                    else:
                        map[str(b_idx)].append(num)
        winner = check_for_winners(map, boards)
        if winner != None:
            print('Winner: Board #{}'.format(winner))
            pp.pprint(boards[int(winner)])
            print('Winning score: {}'.format(
                get_winning_board_score(boards[int(winner)], num)))
            break


# Check all boards to see if there are any winners
def check_for_winners(map, boards):
    for board_num in map:
        board = boards[int(board_num)]
        if len(map[board_num]) > 4:
            for row in board:
                if row.count('*') == 5:
                    return board_num
            for col in range(5):
                if board[0][col] == '*' and board[1][col] == '*' and board[2][col] == '*' and board[3][col] == '*' and board[4][col] == '*':
                    return board_num
    return None


# Calculates final score
def get_winning_board_score(board, num):
    sum = 0
    for row in board:
        for num in row:
            if num.isnumeric():
                sum += int(num)
    return sum * int(num)


# Part 2
# def get_position_with_aim(lines):


# Main
def main():
    file = open('./bingo.txt', 'r')
    lines = file.readlines()

    call_numbers = lines[0].split(sep=',')
    lines.pop(0)

    boards = []
    board = []

    # Create array of boards
    for line in lines:
        if len(line) == 1 and len(board) > 1:
            boards.append(board)
            board = []
        elif len(line) > 1:
            board.append(line.split())

    find_winner(call_numbers, boards)


if __name__ == "__main__":
    main()
