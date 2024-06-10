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
LUCEA = (15, 75, 140)

# Font
FONT = pygame.font.SysFont('Verdana', 24)

# Load sounds
pygame.mixer.music.load('Doom Eternal OST - The Only Thing They Fear Is You (Mick Gordon) [Doom Eternal Theme].mp3')
win_sound = pygame.mixer.Sound('yay sound effect.mp3')
lose_sound = pygame.mixer.Sound('Sad Trombone - Sound Effect (HD).mp3')

pygame.mixer.music.play(-1)

# Function to display text input prompt
def draw_text_input_prompt(prompt):
    text_surface = FONT.render(prompt, True, WHITE)
    text_rect = text_surface.get_rect(center=(SCREEN.get_width() // 2, SCREEN.get_height() // 2))
    SCREEN.blit(text_surface, text_rect)

# Function to get user input
def get_user_input():
    running = True
    user_typed_number = ""

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return None
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return None
                elif event.key == pygame.K_RETURN:
                    if user_typed_number.isdigit():
                        return int(user_typed_number)
                    else:
                        user_typed_number = ""
                elif event.key == pygame.K_BACKSPACE:
                    user_typed_number = user_typed_number[:-1]
                elif event.key in range(pygame.K_0, pygame.K_9+1):
                    user_typed_number += event.unicode

        SCREEN.fill(BLACK)
        draw_text_input_prompt("Guess a number between 1 and 50")
        number_surface = FONT.render(user_typed_number, True, WHITE)
        number_rect = number_surface.get_rect(center=(SCREEN.get_width() // 2, SCREEN.get_height() // 2 + 50))
        SCREEN.blit(number_surface, number_rect)
        pygame.display.flip()

    return None

# Function to draw the array
def draw_array(array, y_pos, selected_number=None):
    bar_width = WIDTH // len(array)
    total_array_width = len(array) * bar_width
    start_x = (SCREEN.get_width() - total_array_width) // 2

    for i, val in enumerate(array):
        color = GREEN if val == selected_number else RED
        pygame.draw.rect(SCREEN, color, (start_x + i * bar_width, y_pos - val * 5 + 350, bar_width, val * 5))

# Function to display the current level
def draw_level(level):
    level_text = FONT.render(f'Level: {level}', True, WHITE)
    SCREEN.blit(level_text, (10, 10))

# Function to display points
def draw_points(points):
    point_text = FONT.render(f'Points: {points}', True, WHITE)
    SCREEN.blit(point_text, (1850, 10))

# Main game function
def main():
    running = True
    points = 50  # start with 50 points
    level = 1  # start at level 1

    while running:
        array_size = 10 * level
        array = [random.randint(1, 10) for _ in range(array_size)]
        sorted_array = array[:]
        bet_number = get_user_input()
        if bet_number is None:
            break
        target = random.choice(array)
        correct_guess = False

        start_sort = False
        start_search = False
        sorted = False
        found = False
        start_time_sort = 0
        end_time_sort = 0
        start_time_search = 0
        end_time_search = 0
        search_result = -1

        while True:
            SCREEN.fill(BLACK)
            draw_array(array, SCREEN.get_height() // 4, None)
            draw_level(level)
            draw_points(points)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    break
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
                    elif event.key == pygame.K_ESCAPE:
                        running = False
                        break

            if not running:
                break

            if sorted:
                SCREEN.fill(BLACK)
                draw_array(sorted_array, SCREEN.get_height() // 2 - 200, target)
                draw_level(level)
                draw_points(points)

                time_taken_sort = end_time_sort - start_time_sort
                time_text_sort = FONT.render(f'Time taken to sort: {time_taken_sort:.4f} seconds', True, WHITE)
                time_text_sort_rect = time_text_sort.get_rect(center=(SCREEN.get_width() // 2, SCREEN.get_height() - 150))
                SCREEN.blit(time_text_sort, time_text_sort_rect)

                if found:
                    time_taken_search = end_time_search - start_time_search
                    time_text_search = FONT.render(f'Time taken to search: {time_taken_search:.4f} seconds', True, WHITE)
                    time_text_search_rect = time_text_search.get_rect(center=(SCREEN.get_width() // 2, SCREEN.get_height() - 100))
                    SCREEN.blit(time_text_search, time_text_search_rect)
                    search_result_text = FONT.render(f'The target was {target}', True, GREEN if search_result != -1 else WHITE)
                    search_result_text_rect = search_result_text.get_rect(center=(SCREEN.get_width() // 2, SCREEN.get_height() - 250))
                    SCREEN.blit(search_result_text, search_result_text_rect)
                    user_number = FONT.render(f'Your number was {bet_number}', True, GREEN if search_result != -1 else WHITE)
                    user_number_rect = user_number.get_rect(center=(SCREEN.get_width() // 2, SCREEN.get_height() - 200))
                    SCREEN.blit(user_number, user_number_rect)

                    if not correct_guess:
                        if bet_number == search_result:
                            points += 100
                            level += 2
                            pygame.mixer.Sound.play(win_sound)
                            result_text = FONT.render(f'Congratulations! You won the bet! +100 points AND you skip an level?!', True, GREEN)
                            correct_guess = True
                        elif abs(bet_number - search_result) <= 5:
                            points += 10
                            level += 1
                            pygame.mixer.Sound.play(win_sound)
                            result_text = FONT.render(f'Close enough, +10 points', True, GREEN)
                            correct_guess = True
                        else:
                            points = max(0, points // 2)  # Ensure points don't go negative
                            level = max(1, level - 1)
                            pygame.mixer.Sound.play(lose_sound)
                            if points <= 0:
                                result_text = FONT.render(f'You Lose! The Casino now owns your soul!', True, RED)
                            else:
                                result_text = FONT.render(f'Sorry, you lost the bet. Half your points have been deducted', True, RED)

                        result_text_rect = result_text.get_rect(center=(SCREEN.get_width() // 2, SCREEN.get_height() - 50))
                        SCREEN.blit(result_text, result_text_rect)
                        points_text = FONT.render(f'Your points: {points}', True, WHITE)
                        points_text_rect = points_text.get_rect(center=(SCREEN.get_width() // 2, SCREEN.get_height() - 20))
                        SCREEN.blit(points_text, points_text_rect)

                        pygame.display.flip()

                        if points <= 0:
                            game_over_text = FONT.render(f'Game Over! You ran out of points.', True, RED)
                            game_over_text_rect = game_over_text.get_rect(center=(SCREEN.get_width() // 2, SCREEN.get_height() // 2))
                            SCREEN.blit(game_over_text, game_over_text_rect)
                            pygame.display.flip()
                            time.sleep(5)
                            running = False
                            break

                    if running:
                        time.sleep(5)
                        break

            instructions = FONT.render('Press SPACE to start sorting, then press SPACE again to start searching', True, RED)
            instructions_rect = instructions.get_rect(center=(SCREEN.get_width() // 2, 20))
            SCREEN.blit(instructions, instructions_rect)

            pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
