def is_on_board(position: tuple[int, int], max_dim: tuple[int, int] = (8, 8)):
    """
    
    Sprawdz, czy dane pole znajduje się na szachownicy o określonych maksymalnych wymiarach.

    """
    row, col = position
    max_row, max_col = max_dim

    if 0 <= row < max_row and 0 <= col < max_col:
        return True
    else:
        return False

# test
pole_A = (0, 0)
max_wymiary = (8, 8)

sprawdz = is_on_board(pole_A, max_wymiary)

print(f"A: {sprawdz}")
