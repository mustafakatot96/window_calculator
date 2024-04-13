def calculate_window_dimensions(x1, x2, q):
    # Implement calculations for different types of windows
    # Return the dimensions for each type of window
    # Example:
    a1 = x1 - 3
    a2 = x2 - q
    b1 = (a1 / 2) - 0.1
    b2 = a2 - 8.3
    b3 = b1 - 1.4
    b4 = b2
    u = b2 + 0.5
    c1 = x1 + 10
    c2 = x2 + 10
    d1 = x1 - 0.3
    d2 = q - 0.3
    t = x1 - 2.7
    f = x1 - 8.5
    r = x1 - 4.5
    h = x1 - 0.3
    k1 = x1 - 11
    k2 = a2 / 5.4
    j1 = x1
    j2 = q
    g1 = b1 - 5.5
    g2 = b2 - 9.2
    e1 = b3 - 11.6
    e2 = b4 - 11.6
    y = a2 + 4

    # Modify calculation for M
    m = ((x1 + 10) * (x2 + 10)) / 10000

    # Modify calculation for mt
    mt = ((x1 + 10) * (x2 + 10)) / 10000

    return {
        'A1': a1,
        'A2': a2,
        'B1': b1,
        'B2': b2,
        'B3': b3,
        'B4': b4,
        'U': u,
        'C1': c1,
        'C2': c2,
        'D1': d1,
        'D2': d2,
        'T': t,
        'F': f,
        'R': r,
        'H': h,
        'K1': k1,
        'K2': k2,
        'J1': j1,
        'J2': j2,
        'G1': g1,
        'G2': g2,
        'E1': e1,
        'E2': e2,
        'Y': y,
        'M': m,  # Include the modified calculation for M
        'MT': mt  # Include the modified calculation for mt
    }

def get_number_of_pieces():
    return {
        'A1': 2,
        'A2': 2,
        'B1': 2,
        'B2': 2,
        'B3': 2,
        'B4': 2,
        'U': 2,
        'C1': 2,
        'C2': 2,
        'D1': 2,
        'D2': 2,
        'T': 1,
        'F': 1,
        'R': 1,
        'H': 1,
        'K1': 2,
        'K2': 2,
        'J1': 2,
        'J2': 2,
        'G1': 2,
        'G2': 2,
        'E1': 2,
        'E2': 2,
        'Y': 2
    }
