import pygame
import random
import time
from Binary_Search import quickSort, binary_search

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 1500, 100
SCREEN = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Quicksort and Binary Search Timer")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Font
FONT = pygame.font.SysFont('Arial', 24)

# Generate random array
array_size = 100
array = [random.randint(1, 100) for _ in range(array_size)]
sorted_array = array[:]

# Function to display text input prompt
def draw_text_input_prompt():
    input_prompt = "Enter the target number:"
    text_surface = FONT.render(input_prompt, True, WHITE)
    text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    SCREEN.blit(text_surface, text_rect)

# Function to get user input
def get_user_input(array):
    running = True
    selected_number = None

    unique_numbers = list(set(array))  # Get unique numbers from the array
    num_options = min(len(unique_numbers), 15)  # Display at most 10 options

    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    running = False
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()
                elif pygame.K_1 <= event.key <= pygame.K_9:  # Number keys 1 to 9
                    index = event.key - pygame.K_1
                    if index < num_options:
                        selected_number = unique_numbers[index]
                        running = False

        SCREEN.fill(BLACK)
        input_prompt = "Select a number from the array:"
        text_surface = FONT.render(input_prompt, True, WHITE)
        text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 20))
        SCREEN.blit(text_surface, text_rect)

        # Calculate the total width needed for all options
        total_width = sum([FONT.size(str(num))[0] + 10 for num in unique_numbers[:num_options]])
        start_x = (WIDTH - total_width) // 2  # Starting x-coordinate for the options

        option_y = HEIGHT // 2 + 20
        for num in unique_numbers[:num_options]:
            option_text = f"{num}"
            option_surface = FONT.render(option_text, True, WHITE)
            option_rect = option_surface.get_rect(midleft=(start_x, option_y))
            SCREEN.blit(option_surface, option_rect)
            start_x += option_rect.width + 10  # Update start_x for next option
            option_y += 20

        pygame.display.flip()

    return selected_number




def draw_array(array, y_pos, selected_number=None):
    bar_width = WIDTH // len(array)
    for i, val in enumerate(array):
        color = GREEN if val == selected_number else RED  # Highlight selected column in green
        pygame.draw.rect(SCREEN, color, (i * bar_width, y_pos, bar_width, val * 5))


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

    # Get user input for target number
    target = get_user_input(sorted_array)

    selected_number = None
    while running:
        previous_array_displayed = False
        SCREEN.fill(BLACK)
        # Draw original array
        draw_array(array, HEIGHT // 4, selected_number)
        previous_array_displayed = True
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
                elif event.key == pygame.K_ESCAPE:
                    running = False

        if previous_array_displayed:
            SCREEN.fill(BLACK)
        # Draw sorted array
        draw_array(sorted_array, HEIGHT // 2, target)

        # Display timing information
        if start_sort and sorted:
            time_taken_sort = end_time_sort - start_time_sort
            time_text_sort = FONT.render(
                f'Time taken to sort: {time_taken_sort:.4f} seconds', True, WHITE)
            SCREEN.blit(time_text_sort, (WIDTH // 4, HEIGHT - 100))

        if start_search and found:
            time_taken_search = end_time_search - start_time_search
            time_text_search = FONT.render(
                f'Time taken to search: {time_taken_search:.4f} seconds', True, WHITE)
            SCREEN.blit(time_text_search, (WIDTH // 4, HEIGHT - 50))
            search_result_text = FONT.render(
                f'Target {target} found at index: {search_result}', True, GREEN if search_result != -1 else WHITE)
            SCREEN.blit(search_result_text, (WIDTH // 4, HEIGHT - 150))

        # Display instructions
        instructions = FONT.render(
            'Press SPACE to start sorting, then press SPACE again to start searching', True, RED)
        SCREEN.blit(instructions, (WIDTH // 8, 20))

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()

#TO DO
# - FIND OUT WHY ITS NOT LETTING ME INPUT MORE THAN 1 NUMBER 
