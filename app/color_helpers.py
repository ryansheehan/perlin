from random import randint


def RGB_2_HSV(RGB):
    '''
    Converts an integer RGB tuple (value range from 0 to 255) to an HSV tuple
    '''

    # Unpack the tuple for readability
    R, G, B = RGB

    # Compute the H value by finding the maximum of the RGB values
    RGB_Max = max(RGB)
    RGB_Min = min(RGB)

    # Compute the value
    V = RGB_Max
    if V == 0:
        H = S = 0
        return (H, S, V)

    # Compute the saturation value
    S = 255 * (RGB_Max - RGB_Min) // V

    if S == 0:
        H = 0
        return (H, S, V)

    # Compute the Hue
    if RGB_Max == R:
        H = 0 + 43*(G - B)//(RGB_Max - RGB_Min)
    elif RGB_Max == G:
        H = 85 + 43*(B - R)//(RGB_Max - RGB_Min)
    else:  # RGB_MAX == B
        H = 171 + 43*(R - G)//(RGB_Max - RGB_Min)

    return (H, S, V)


def HSV_2_RGB(HSV):
    '''
    Converts an integer HSV tuple (value range from 0 to 255) to an RGB tuple
    '''

    # Unpack the HSV tuple for readability
    H, S, V = HSV

    # Check if the color is Grayscale
    if S == 0:
        R, G, B = V, V, V
        return (R, G, B)

    # Make hue 0-5
    region = H // 43

    # Find remainder part, make it from 0-255
    remainder = (H - (region * 43)) * 6

    # Calculate temp vars, doing integer multiplication
    P = (V * (255 - S)) >> 8
    Q = (V * (255 - ((S * remainder) >> 8))) >> 8
    T = (V * (255 - ((S * (255 - remainder)) >> 8))) >> 8

    # Assign temp vars based on color cone region
    if region == 0:
        R, G, B = V, T, P
    elif region == 1:
        R, G, B = Q, V, P
    elif region == 2:
        R, G, B = P, V, T
    elif region == 3:
        R, G, B = P, Q, V
    elif region == 4:
        R, G, B = T, P, V
    else:
        R, G, B = V, P, Q

    return (R, G, B)


def create_hsv():
    # v = randint(0, 255)
    r = randint(0, 255)  # v
    g = randint(0, 255)  # v
    b = randint(0, 255)  # v

    # hsv = RGB_2_HSV((r, g, b))
    # return hsv

    return (r, g, b)

    # h = randint(0, 255)
    # s = 200
    # v = 255

    # return (h, s, v)


def get_rgb(values):
    # h, s, v = values
    # rgb = HSV_2_RGB((int(h), int(s), int(v)))
    # return rgb
    return values
