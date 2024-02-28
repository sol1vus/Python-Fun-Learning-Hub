from random import randint


class Board:
    def __init__(self) -> None:
        self.winning_hand = '💎'
        self.losing_hand = '✋'
        self.__board = [
            ['✊', '✊', '✊', '✊', '✊', '✊', '✊', '✊', '✊', '✊'],
            ['1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣', '6️⃣', '7️⃣', '8️⃣', '9️⃣', '🔟']
        ]

    def draw_board(self) -> None:
        custom_format = '{}{}{}{}{}{}{}{}{}{}\n{} {} {} {} {} {} {} {} {} {}'
        print(custom_format.format(*self.__board[0], *self.__board[1]))

    def update_board(self, index: int, value: str) -> None:
        self.__board[0][index - 1] = value

    def is_valid_guess(self, index: int) -> bool:
        if index > 10 or index < 1:
            return False
        if self.__board[0][index - 1] == self.losing_hand:
            return False
        return True


class Game:
    def __init__(self):
        self.board = Board()
        self.score = 0
        self.winning_number = randint(1, 10)

    def make_guess(self, index: int) -> bool:
        if self.board.is_valid_guess(index):
            self.board.update_board(index, self.board.losing_hand)
            self.score += 1
            return True
        return False

    def check_winner(self, index: int) -> bool:
        if index == self.winning_number:
            self.board.update_board(index, self.board.winning_hand)
            return True
        return False