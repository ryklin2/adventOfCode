import numpy
""" 
AoC1 Secret Entrance
This module contains functions to solve the Advent of Code Day 1 challenge.

finish decorating by dec 12th
dial from 0 to 99
clicks when reaching the right number

YOU MUST ADD AN L50 OR R50 TO THE INPUT.TXT TO GET THE CORRECT ANSWER
"""
##open and read input.txt
def parse_and_track_sums(filename):
    sumL = 50
    sumR = 0
    matches = 0
    dial = 50
    past0 = 0
    
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            
            direction = line[0]
            value = int(line[1:])
            
            if direction == 'L':
                sumL += value
            elif direction == 'R':
                sumR += value
                
            if sumL % 100 == sumR % 100:
                matches += 1
                
            if sumL - sumR <=100:
                matches += 1
                
                
            
    print(f"Total Left Sum: {sumL}")
    print(f"Total Right Sum: {sumR}")
    print(f"Number of Matches: {matches}")
    print(f"times passed 0: 
    
    
    return sumL, sumR, matches


if __name__ == "__main__":
    parse_and_track_sums('input.txt')