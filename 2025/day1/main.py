def count_zero_hits_part1(start):
    """
    Part 1: Count how many times the dial is at 0 AFTER each rotation
    """
    pos = start
    zero_count = 0
    data = [line.strip() for line in open("input/input.in").readlines()]
    
    for move in data:
        direction = move[0]
        amount = int(move[1:])
        
        if direction == "L":
            pos = (pos - amount) % 100
        else:  # "R"
            pos = (pos + amount) % 100
        
        if pos == 0:
            zero_count += 1
    
    return zero_count


def count_zero_hits_part2(start):
    """
    Part 2: Count how many times the dial passes through or lands on 0
    during AND at the end of each rotation
    """
    pos = start
    zero_hits = 0
    data = [line.strip() for line in open("input/input.in").readlines()]
    
    for move in data:
        direction = move[0]
        amount = int(move[1:])
        
        if direction == "L":
            new_pos = (pos - amount) % 100
        else:  # "R"
            new_pos = (pos + amount) % 100
        
        # Count how many times we pass through 0 during the rotation
        # Important: if we land exactly ON 0, that doesn't count as passing through
        passes_during = 0
        
        if direction == "L":
            # Going left (counterclockwise)
            if pos == 0:
                # Starting at 0, we don't pass through when leaving
                # But might come back if amount >= 100
                passes_during = amount // 100
            elif new_pos == 0:
                # Ending at 0 - don't count as passing through
                # But check for complete loops
                if amount > pos:
                    remaining_after_first_wrap = amount - pos
                    passes_during = remaining_after_first_wrap // 100
            else:
                # Not starting or ending at 0
                if amount > pos:
                    # We wrap at least once, passing through 0
                    remaining = amount - pos - 1
                    passes_during = 1 + remaining // 100
        else:  # "R"
            # Going right (clockwise)
            if new_pos == 0:
                # Ending at 0 - don't count as passing through
                # But check for complete loops before getting there
                total = pos + amount
                passes_during = (total - 100) // 100 if total >= 100 else 0
            else:
                # Not ending at 0
                if pos + amount >= 100:
                    # We wrap at least once, passing through 0
                    passes_during = (pos + amount) // 100
        
        zero_hits += passes_during
        
        # Count if we END on 0
        if new_pos == 0:
            zero_hits += 1
        
        pos = new_pos
    
    return zero_hits


print("Part 1 (count zeros at end of rotations):", count_zero_hits_part1(50))
print("Part 2 (count all zero crossings):", count_zero_hits_part2(50))
