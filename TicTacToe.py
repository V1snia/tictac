import tkinter as tk
from tkinter import messagebox


class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("TicTacToe")

        self.current_player = "X"
        self.board = [[" " for _ in range(3)] for _ in range(3)]

        self.turn_label = tk.Label(root, text=f"Žaidėjo {self.current_player} Eilė", font=("Arial", 12))
        self.turn_label.grid(row=3, column=0, columnspan=3)

        self.result_label = tk.Label(root, text="", font=("Arial", 14))
        self.result_label.grid(row=4, column=0, columnspan=3)

        self.buttons = [[None for _ in range(3)] for _ in range(3)]

        for row in range(3):
            for col in range(3):
                self.buttons[row][col] = tk.Button(
                    root,
                    text=" ",
                    font=("Arial", 24),
                    width=5,
                    height=2,
                    command=lambda r=row, c=col: self.handle_click(r, c),
                )
                self.buttons[row][col].grid(row=row, column=col)

        self.play_again_button = tk.Button(root, text="Žaisti dar karta", font=("Arial", 12), command=self.reset_board)
        self.play_again_button.grid(row=5, column=0, columnspan=3)

    def handle_click(self, row, col):
        if self.board[row][col] == " ":
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)

            if self.check_winner(self.current_player):
                self.result_label.config(text=f"Žaidėjas {self.current_player} laimi!")
                self.disable_buttons()
            elif self.is_board_full():
                self.result_label.config(text="Lygiosios!")
                self.disable_buttons()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                self.turn_label.config(text=f"Žaidėjo {self.current_player} Eilė")

    def check_winner(self, player):
        for row in self.board:
            if all(cell == player for cell in row):
                return True

        for col in range(3):
            if all(self.board[row][col] == player for row in range(3)):
                return True

        if all(self.board[i][i] == player for i in range(3)) or all(self.board[i][2 - i] == player for i in range(3)):
            return True

        return False

    def is_board_full(self):
        return all(cell != " " for row in self.board for cell in row)

    def disable_buttons(self):
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(state=tk.DISABLED)

    def reset_board(self):
        for row in range(3):
            for col in range(3):
                self.board[row][col] = " "
                self.buttons[row][col].config(text=" ", state=tk.NORMAL)

        self.current_player = "X"
        self.turn_label.config(text=f"Žaidėjo {self.current_player} Eilė")
        self.result_label.config(text="")


if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
