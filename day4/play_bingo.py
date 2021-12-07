import pprint

pp = pprint.PrettyPrinter(indent=2)


# Part 1
def find_winner(numbers, boards):
    map = {}
    winner_list = []
    for num in numbers:
        # print('Calling number {}'.format(num))
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
        winners = check_for_winners(map, boards)
        if len(winners) > 0:
            for w in winners:
                if w not in winner_list:
                    winner_list.append(w)
                    print('Winner: Board #{}'.format(w))
                    pp.pprint(boards[int(w)])
                    print('Winning score: {}, Last called number: {}'.format(
                        get_winning_board_score(boards[int(w)], num), num))
                    print('--------------------')


# Check all boards to see if there are any winners
def check_for_winners(map, boards):
    winners = []
    for board_num in map:
        board = boards[int(board_num)]
        # if len(map[board_num]) > 4:
        for row in board:
            if row.count('*') == 5:
                winners.append(board_num)
                # return board_num
        for col in range(5):
            if board[0][col] == '*' and board[1][col] == '*' and board[2][col] == '*' and board[3][col] == '*' and board[4][col] == '*':
                winners.append(board_num)
                # return board_num
    return winners


# Calculates final score
def get_winning_board_score(board, multiplier):
    sum = 0
    for row in board:
        for num in row:
            if num.isnumeric():
                sum += int(num)
    return sum * int(multiplier)


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
