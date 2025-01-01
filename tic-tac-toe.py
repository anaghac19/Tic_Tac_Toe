import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 600, 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Fonts
FONT = pygame.font.SysFont("comicsans", 60)

# Create game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe")

# Grid and board variables
GRID_SIZE = 3
CELL_SIZE = WIDTH // GRID_SIZE
board = [["" for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

# Game state
current_player = "X"
game_over = False
winner = None

# Function to draw the game board
def draw_board():
    # Background color
    screen.fill(WHITE)
    
    # Draw grid lines
    for row in range(1, GRID_SIZE):
        pygame.draw.line(screen, BLACK, (0, row * CELL_SIZE), (WIDTH, row * CELL_SIZE), 5)
        pygame.draw.line(screen, BLACK, (row * CELL_SIZE, 0), (row * CELL_SIZE, HEIGHT), 5)
    
    # Draw X and O
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            if board[row][col] == "X":
                text = FONT.render("X", True, BLUE)
                screen.blit(text, (col * CELL_SIZE + CELL_SIZE // 4, row * CELL_SIZE + CELL_SIZE // 4))
            elif board[row][col] == "O":
                text = FONT.render("O", True, RED)
                screen.blit(text, (col * CELL_SIZE + CELL_SIZE // 4, row * CELL_SIZE + CELL_SIZE // 4))

# Function to check for a winner
def check_winner():
    global game_over, winner

    # Check rows and columns
    for i in range(GRID_SIZE):
        if board[i][0] == board[i][1] == board[i][2] != "":
            winner = board[i][0]
            game_over = True
            return
        if board[0][i] == board[1][i] == board[2][i] != "":
            winner = board[0][i]
            game_over = True
            return
    
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != "":
        winner = board[0][0]
        game_over = True
        return
    if board[0][2] == board[1][1] == board[2][0] != "":
        winner = board[0][2]
        game_over = True
        return
    
    # Check for a draw
    if all(board[row][col] != "" for row in range(GRID_SIZE) for col in range(GRID_SIZE)):
        game_over = True

# Function to handle mouse click
def handle_click(pos):
    global current_player

    if game_over:
        return

    # Calculate row and column from mouse position
    col = pos[0] // CELL_SIZE
    row = pos[1] // CELL_SIZE

    # Place the current player's symbol if the cell is empty
    if board[row][col] == "":
        board[row][col] = current_player
        check_winner()
        current_player = "O" if current_player == "X" else "X"

# Function to display the game winner or draw
def display_winner():
    if winner:
        text = FONT.render(f"{winner} Wins!", True, BLACK)
    else:
        text = FONT.render("It's a Draw!", True, BLACK)
    screen.blit(text, (WIDTH // 4, HEIGHT // 2))

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            handle_click(pygame.mouse.get_pos())

    # Draw the board and update display
    draw_board()
    if game_over:
        display_winner()
    pygame.display.update()

# Quit Pygame
pygame.quit()
sys.exit()
