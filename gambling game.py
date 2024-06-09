import pygame
import random
import time
from Binary_Search import quickSort, binary_search

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 2000, 1000
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gambling Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Font
FONT = pygame.font.SysFont('Verdana', 24)

# Generate random array
array_size = 10
array = [random.randint(1, 10) for _ in range(array_size)]
sorted_array = array[:]

# Function to display text input prompt
def draw_text_input_prompt():
    input_prompt = "Place your bet (enter a number between 1 and 100):"
    text_surface = FONT.render(input_prompt, True, WHITE)
    text_rect = text_surface.get_rect(center=(SCREEN.get_width() // 2, SCREEN.get_height() // 2))
    SCREEN.blit(text_surface, text_rect)

# Function to get user input
def get_user_input():
    running = True
    user_typed_number = ""

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if 48 <= event.key <= 57:  # Convert keycode to ascii value range for numbers
                    user_typed_number += chr(event.key)
                elif event.key == pygame.K_RETURN:
                    if user_typed_number.isdigit():
                        return int(user_typed_number)
                    else:
                        pass

        SCREEN.fill(BLACK)
        draw_text_input_prompt()

        number_surface = FONT.render(user_typed_number, True, WHITE)
        number_rect = number_surface.get_rect(center=(SCREEN.get_width() // 2, SCREEN.get_height() // 2 + 50))
        SCREEN.blit(number_surface, number_rect)

        pygame.display.flip()

    return None

def draw_array(array, y_pos, selected_number=None):
    bar_width = WIDTH // len(array)
    total_array_width = len(array) * bar_width
    start_x = (SCREEN.get_width() - total_array_width) // 2

    for i, val in enumerate(array):
        color = GREEN if val == selected_number else RED
        pygame.draw.rect(SCREEN, color, (start_x + i * bar_width, y_pos - val * 5 + 350, bar_width, val * 5))

def main():
    running = True
    start_sort = False
    start_search = False
    sorted = False
    found = False
    start_time_sort = 0
    end_time_sort = 0
    start_time_search = 0
    end_time_search = 0
    search_result = -1
    instance_count = 0

    bet_number = get_user_input()
    target = random.choice(array)
    selected_number = None
    points = 50 #start with 50 points
    level = 1
    array_size = 10 * level  # Start with 10 arrays

    while running:
        correct_guess = False  # Reset the flag at the beginning of each round

        SCREEN.fill(BLACK)
        draw_array(array, SCREEN.get_height() // 4, selected_number)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if not start_sort:
                        start_sort = True
                        start_time_sort = time.time()
                        quickSort(sorted_array, 0, len(sorted_array) - 1)
                        end_time_sort = time.time()
                        sorted = True
                    elif sorted and not start_search:
                        start_search = True
                        start_time_search = time.time()
                        search_result = binary_search(sorted_array, target)
                        end_time_search = time.time()
                        found = True

        if sorted:
            SCREEN.fill(BLACK)
            draw_array(sorted_array, SCREEN.get_height() // 2, target)

            time_taken_sort = end_time_sort - start_time_sort
            time_text_sort = FONT.render(f'Time taken to sort: {time_taken_sort:.4f} seconds', True, WHITE)
            time_text_sort_rect = time_text_sort.get_rect(center=(SCREEN.get_width() // 2, SCREEN.get_height() - 150))
            SCREEN.blit(time_text_sort, time_text_sort_rect)

            if found:
                time_taken_search = end_time_search - start_time_search
                time_text_search = FONT.render(f'Time taken to search: {time_taken_search:.4f} seconds', True, WHITE)
                time_text_search_rect = time_text_search.get_rect(center=(SCREEN.get_width() // 2, SCREEN.get_height() - 100))
                SCREEN.blit(time_text_search, time_text_search_rect)
                search_result_text = FONT.render(f'Target {target} found at index: {search_result}', True, GREEN if search_result != -1 else WHITE)
                search_result_text_rect = search_result_text.get_rect(center=(SCREEN.get_width() // 2, SCREEN.get_height() - 200))
                SCREEN.blit(search_result_text, search_result_text_rect)

                if not correct_guess:  # Check if the player has already guessed correctly in the current round
                    if bet_number == search_result:
                        points += 100
                        result_text = FONT.render(f'Congratulations! You won the bet! +100 points', True, GREEN)
                        correct_guess = True  # Set the flag to True if the guess is correct
                    elif abs(bet_number - search_result) <= 10:
                        points += 10
                        result_text = FONT.render(f'You were close! +10 points', True, GREEN)
                    else:
                        points = 0
                        result_text = FONT.render(f'Sorry, you lost the bet. Try again! 0 points', True, RED)

                result_text_rect = result_text.get_rect(center=(SCREEN.get_width() // 2, SCREEN.get_height() - 50))
                SCREEN.blit(result_text, result_text_rect)
                points_text = FONT.render(f'Your points: {points}', True, WHITE)
                points_text_rect = points_text.get_rect(center=(SCREEN.get_width() // 2, SCREEN.get_height() - 20))
                SCREEN.blit(points_text, points_text_rect)

                if points <= 0:  # Game over condition
                    game_over_text = FONT.render(f'Game Over! You ran out of points.', True, RED)
                    game_over_text_rect = game_over_text.get_rect(center=(SCREEN.get_width() // 2, SCREEN.get_height() // 2))
                    SCREEN.blit(game_over_text, game_over_text_rect)
                    pygame.display.flip()
                    time.sleep(5)  # Pause for 5 seconds before quitting
                    pygame.quit()
                    return

        instructions = FONT.render('Press SPACE to start sorting, then press SPACE again to start searching', True, RED)
        instructions_rect = instructions.get_rect(center=(SCREEN.get_width() // 2, 20))
        SCREEN.blit(instructions, instructions_rect)

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
