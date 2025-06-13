import random
import sys

class Board:
    """Simple Go board implementation supporting basic play and capture."""

    def __init__(self, size=19):
        self.size = size
        self.board = [['.' for _ in range(size)] for _ in range(size)]

    def is_on_board(self, x, y):
        return 0 <= x < self.size and 0 <= y < self.size

    def get_neighbors(self, x, y):
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if self.is_on_board(nx, ny):
                yield nx, ny

    def get_group(self, x, y):
        color = self.board[x][y]
        if color == '.':
            return set()
        group = set()
        stack = [(x, y)]
        while stack:
            cx, cy = stack.pop()
            if (cx, cy) in group:
                continue
            if self.board[cx][cy] != color:
                continue
            group.add((cx, cy))
            for nx, ny in self.get_neighbors(cx, cy):
                if self.board[nx][ny] == color:
                    stack.append((nx, ny))
        return group

    def has_liberty(self, group):
        for x, y in group:
            for nx, ny in self.get_neighbors(x, y):
                if self.board[nx][ny] == '.':
                    return True
        return False

    def remove_group(self, group):
        for x, y in group:
            self.board[x][y] = '.'

    def play_move(self, x, y, color):
        if not self.is_on_board(x, y) or self.board[x][y] != '.':
            return False
        stone = 'B' if color == 'black' else 'W'
        opponent = 'W' if stone == 'B' else 'B'
        self.board[x][y] = stone

        captured_groups = []
        for nx, ny in self.get_neighbors(x, y):
            if self.board[nx][ny] == opponent:
                group = self.get_group(nx, ny)
                if not self.has_liberty(group):
                    captured_groups.append(group)
        for group in captured_groups:
            self.remove_group(group)

        own_group = self.get_group(x, y)
        if not self.has_liberty(own_group):
            # undo move
            self.board[x][y] = '.'
            for group in captured_groups:
                for cx, cy in group:
                    self.board[cx][cy] = opponent
            return False
        return True

    def generate_random_move(self, color):
        moves = [(x, y) for x in range(self.size) for y in range(self.size)]
        random.shuffle(moves)
        for x, y in moves:
            if self.play_move(x, y, color):
                return x, y
        return None

    def print_board(self):
        for row in self.board:
            print(' '.join(row))
        print()


def ai_vs_ai_game(size=19, move_limit=200, verbose=True):
    """Run a game where two AIs play against each other."""
    board = Board(size)
    current = 'black'
    passes = 0
    moves = 0
    while passes < 2 and moves < move_limit:
        coord = board.generate_random_move(current)
        if coord is None:
            if verbose:
                print(f"{current} AI passes.")
            passes += 1
        else:
            if verbose:
                print(f"{current} AI plays at {coord[0]} {coord[1]}")
            passes = 0
        if verbose:
            board.print_board()
        current = 'white' if current == 'black' else 'black'
        moves += 1
    if verbose:
        print('AI vs AI game over.')
        board.print_board()
    return board


def main():
    if len(sys.argv) > 1 and sys.argv[1] == '--ai-vs-ai':
        ai_vs_ai_game()
        return

    board = Board(19)
    current = 'black'
    passes = 0
    while passes < 2:
        board.print_board()
        if current == 'black':
            move = input("Your move (x y) or 'pass': ")
            if move.strip().lower() == 'pass':
                passes += 1
            else:
                try:
                    x, y = map(int, move.split())
                except ValueError:
                    print('Invalid input. Use "x y" or "pass".')
                    continue
                if board.play_move(x, y, current):
                    passes = 0
                else:
                    print('Illegal move. Try again.')
                    continue
        else:
            coord = board.generate_random_move(current)
            if coord is None:
                print('AI passes.')
                passes += 1
            else:
                print(f'AI plays at {coord[0]} {coord[1]}')
                passes = 0
        current = 'white' if current == 'black' else 'black'
    print('Game over.')
    board.print_board()


if __name__ == '__main__':
    main()
