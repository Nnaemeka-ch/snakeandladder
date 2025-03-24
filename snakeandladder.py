import random

# Snakes and Ladders board
board = {
    # Ladders (Go Up)
    3: 22, 5: 8, 11: 26, 20: 29, 17: 4, 27: 56, 39: 60, 50: 66,
    53: 76, 61: 79, 63: 81, 70: 90,

    # Snakes (Go Down)
    16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 
    93: 73, 95: 75, 98: 78
}

class Player:
    def __init__(self, name):
        self.name = name  
        self.position = 0  # Start at position 0


    def roll_dice(self):
        while input(f"{self.name}, press Enter to roll the dice...").strip():
            print("❌ Invalid input! Just press Enter to roll.")

        roll = random.randint(1, 6)
        print(f"{self.name} rolled a {roll}!")
        return roll
    
    def move(self, roll):
        self.position += roll

        # Check for snake or ladder
        if self.position in board:
            if board[self.position] > self.position:
                print(f"🎉 {self.name} found a ladder! Climbing up to {board[self.position]}!")
            else:
                print(f"🐍 {self.name} got bitten by a snake! Sliding down to {board[self.position]}!")
            self.position = board[self.position]

        # Prevent moving past 100
        if self.position > 100:
            self.position -= roll  # Stay in place if roll overshoots 100
            print(f"{self.name} needs exactly {100 - self.position} to win.")

        print(f"{self.name} is now at position {self.position}\n")
        return self.position
    

# Get player names
player1_name = input("Enter name for Player 1: ")
player2_name = input("Enter name for Player 2: ")

# Create players
player1 = Player(player1_name)
player2 = Player(player2_name)

# Game loop: Keep playing until one player reaches 100
while True:
    # Player 1's turn
    roll = player1.roll_dice()
    if player1.move(roll) == 100:
        print(f"🎉🎊 {player1.name} wins the game! 🎊🎉")
        break  # End the game

    # Player 2's turn
    roll = player2.roll_dice()
    if player2.move(roll) == 100:
        print(f"🎉🎊 {player2.name} wins the game! 🎊🎉")
        break  # End the game



