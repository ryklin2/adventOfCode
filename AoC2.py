def solve(filename):
    position = 50  # Dial starts at 50
    part1_matches = 0
    part2_clicks = 0
    
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            
            direction = line[0]
            value = int(line[1:])
            
            if direction == 'R':
                new_pos = position + value
                part2_clicks += new_pos // 100
                position = new_pos % 100
            else:  # L
                if position > 0 and value >= position:
                    part2_clicks += 1  
                    remaining = value - position
                    part2_clicks += remaining // 100  # Additional full rotations
                elif position == 0:
                    part2_clicks += value // 100
                position = (position - value) % 100
            
            if position == 0:
                part1_matches += 1
                
                
    print(f"Number of Matches: {part1_matches}")
    print(f"Number of Matches: {part2_clicks}")
    return part1_matches, part2_clicks

if __name__ == "__main__":
    solve('input.txt')