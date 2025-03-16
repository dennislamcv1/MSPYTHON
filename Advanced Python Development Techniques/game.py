class Game:
    def __init__(self):
        self.score = 0
        self._game_over = False

    def is_game_over(self) -> bool:
        return self._game_over

    def get_final_score(self) -> int:
        """Returns the player's final score. Only valid after game is over."""
        if not self.is_game_over():
            raise ValueError("Game is not over yet.")
        return self.score