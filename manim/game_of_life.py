# manim -pqh --disable_caching game_of_life.py game_of_life -p

from manim import *
import copy
import random
import numpy as np

ELECTRIC_PURPLE = "#8F00FF"
DEEP_PURPLE = "#47015D"
TRUE_PURPLE = "#6A0DAD"
INDIGO = "#4B0082"


def evolve(input_array):
    input_array = np.array(input_array)
    output_array = np.zeros_like(input_array)
    # Create a padded version of the input array to handle edge cases
    padded_array = np.pad(input_array, 1, mode='constant')
    # Compute the sum of neighbors for each cell
    neighbor_sum = sum(np.roll(np.roll(padded_array, i, 0), j, 1)[1:-1, 1:-1]
                       for i in (-1, 0, 1) for j in (-1, 0, 1)
                       if (i != 0 or j != 0))
    # Update the output array based on the neighbor sum and the rules of the game
    output_array[(input_array == 1) & ((neighbor_sum < 2) | (neighbor_sum > 3))] = 0
    output_array[(input_array == 1) & ((neighbor_sum == 2) | (neighbor_sum == 3))] = 1
    output_array[(input_array == 0) & (neighbor_sum == 3)] = 1
    return output_array.tolist()

# def evolve(input_array):
#     input_array = np.array(input_array)
#     output_array = np.zeros_like(input_array)
#     # Create a padded version of the input array to handle edge cases
#     padded_array = np.pad(input_array, 1, mode='constant')
#     # Compute the sum of neighbors for each cell
#     neighbor_sum = sum(np.roll(np.roll(padded_array, i, 0), j, 1)
#                        for i in (-1, 0, 1) for j in (-1, 0, 1)
#                        if (i != 0 or j != 0))
#     # Update the output array based on the neighbor sum and the rules of the game
#     output_array[(input_array == 1) & ((neighbor_sum < 2) | (neighbor_sum > 3))] = 0
#     output_array[(input_array == 1) & ((neighbor_sum == 2) | (neighbor_sum == 3))] = 1
#     output_array[(input_array == 0) & (neighbor_sum == 3)] = 1
#     return output_array.tolist()

# def evolve(input_array):
#     output_array = [[0 for j in range(len(input_array[0]))] for i in range(len(input_array))]
#     # Update the output array based on the input array
#     for i in range(len(input_array)):
#         for j in range(len(input_array[0])):
#             neighbor_sum = 0
#             for x in range(max(0, i-1), min(i+2, len(input_array))):
#                 for y in range(max(0, j-1), min(j+2, len(input_array[0]))):
#                     if x != i or y != j:
#                         neighbor_sum += input_array[x][y]
#             if (neighbor_sum < 2):
#                 output_array[i][j] = 0
#             elif (neighbor_sum == 2):
#                 output_array[i][j] = input_array[i][j]
#             elif (neighbor_sum == 3):
#                 output_array[i][j] = 1
#             else:
#                 output_array[i][j] = 0
#     return output_array

class game_of_life(Scene):
    def construct(self):
        # Create a 10x10 grid of squares
        squares = []
        for i in range(70):
            row = []
            for j in range(40):
                square = Square(side_length=0.2, color=ELECTRIC_PURPLE, stroke_width=1, fill_opacity=1)
                square.move_to([-6.9 + i * 0.2, -3.9 + j * 0.2, 0])
                self.add(square)
                row.append(square)
            squares.append(row)

        array1 = [[random.choice([0, 1]) for j in range(40)] for i in range(70)]
        array2 = evolve(array1)

        current_gen = array1
        next_gen = array2

        frame_count = 0

        while frame_count < 1800:
            if frame_count % 12 == 0:
                self.update_colors(squares, current_gen)
                current_gen, next_gen = next_gen, current_gen
                next_gen = evolve(current_gen)
            self.wait(1/60)
            frame_count += 1

    def update_colors(self, squares, array):
        for i in range(len(array)):
            for j in range(len(array[0])):
                if array[i][j] == 1:
                    squares[i][j].set_fill(INDIGO)
                else:
                    squares[i][j].set_fill(BLACK)


