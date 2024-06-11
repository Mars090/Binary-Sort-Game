import pygame
import random
import time
from Binary_Search import quickSort, binary_search  # import from other file

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 2000, 100
SCREEN = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Quicksort and Binary Search Thingy")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Font
FONT = pygame.font.SysFont('Verdana', 24)

# Generate random array
array_size = 1000
array = [random.randint(1, 100) for _ in range(array_size)]
sorted_array = array[:]

# Function to display text input prompt


def draw_text_input_prompt():
    input_prompt = "Enter the target number:"
    text_surface = FONT.render(input_prompt, True, WHITE)
    text_rect = text_surface.get_rect(
        center=(SCREEN.get_width() // 2, SCREEN.get_height() // 2))
    SCREEN.blit(text_surface, text_rect)

# Function to get user input


def get_user_input(array):
    running = True
    user_typed_number = ""

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                # Handle number keys 0-9
                if 48 <= event.key <= 57:  # Convert keycode to ascii value range for numbers
                    user_typed_number += chr(event.key)
                elif event.key == pygame.K_RETURN:
                    # Validate input (check length, range etc.)
                    if user_typed_number.isdigit():
                        return int(user_typed_number)
                    else:
                        # Display error message (e.g., "Invalid input. Please enter a two-digit number.")
                        pass

        SCREEN.fill(BLACK)
        draw_text_input_prompt()  # Call your function to display input prompt

        # Display current user-typed number
        number_surface = FONT.render(user_typed_number, True, WHITE)
        number_rect = number_surface.get_rect(
            center=(SCREEN.get_width() // 2, SCREEN.get_height() // 2 + 50))
        SCREEN.blit(number_surface, number_rect)

        pygame.display.flip()

    return None


def count_instances(array, target):
    return array.count(target)


def draw_array(array, y_pos, selected_number=None):
    bar_width = WIDTH // len(array)
    total_array_width = len(array) * bar_width
    start_x = (SCREEN.get_width() - total_array_width) // 2

    # keeps track of the amount of iterations in the array
    for i, val in enumerate(array):
        # Highlight selected column in green
        color = GREEN if val == selected_number else RED
        pygame.draw.rect(SCREEN, color, (i * bar_width,
                         y_pos - 300, bar_width, val * 5))


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

    # Get user input for target number
    target = get_user_input(sorted_array)

    selected_number = None
    while running:
        previous_array_displayed = False
        SCREEN.fill(BLACK)
        # Draw original array
        draw_array(array, SCREEN.get_height() // 4, selected_number)
        previous_array_displayed = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if not start_sort:
                        start_sort = True
                        start_time_sort = time.time()
                        # uses quickSort function from other file
                        quickSort(sorted_array, 0, len(sorted_array) - 1)
                        end_time_sort = time.time()
                        sorted = True
                    elif sorted and not start_search:
                        start_search = True
                        start_time_search = time.time()
                        # uses binary_search function from other file
                        search_result = binary_search(sorted_array, target)
                        end_time_search = time.time()
                        found = True
                        instance_count = count_instances(sorted_array, target)
                elif event.key == pygame.K_ESCAPE:
                    running = False

        if previous_array_displayed:
            SCREEN.fill(BLACK)
        # Draw sorted array
        draw_array(sorted_array, SCREEN.get_height() // 2, target)

        # Display timing information
        if start_sort and sorted:
            time_taken_sort = end_time_sort - start_time_sort
            time_text_sort = FONT.render(
                f'Time taken to sort: {time_taken_sort:.4f} seconds', True, WHITE)
            time_text_sort_rect = time_text_sort.get_rect(
                center=(SCREEN.get_width() // 2, SCREEN.get_height() - 150))
            SCREEN.blit(time_text_sort, time_text_sort_rect)

        if start_search and found:
            time_taken_search = end_time_search - start_time_search
            time_text_search = FONT.render(
                f'Time taken to search: {time_taken_search:.4f} seconds', True, WHITE)
            time_text_search_rect = time_text_search.get_rect(
                center=(SCREEN.get_width() // 2, SCREEN.get_height() - 100))
            SCREEN.blit(time_text_search, time_text_search_rect)
            search_result_text = FONT.render(
                f'Target {target} found at index: {search_result}', True, GREEN if search_result != -1 else WHITE)
            search_result_text_rect = search_result_text.get_rect(
                center=(SCREEN.get_width() // 2, SCREEN.get_height() - 200))
            SCREEN.blit(search_result_text, search_result_text_rect)
            instance_count_text = FONT.render(
                f'Number of instances of target {target}: {instance_count}', True, GREEN)
            instance_count_text_rect = instance_count_text.get_rect(
                center=(SCREEN.get_width() // 2, SCREEN.get_height() - 50))
            SCREEN.blit(instance_count_text, instance_count_text_rect)

        # Display instructions
        instructions = FONT.render(
            'Press SPACE to start sorting, then press SPACE again to start searching', True, RED)
        instructions_rect = instructions.get_rect(
            center=(SCREEN.get_width() // 2, 20))
        SCREEN.blit(instructions, instructions_rect)

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
