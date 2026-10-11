"""Challenge 2: Modulo Arithmetic & The Euclidean Clock
Topic: Negative division (//), modulo (%), operator precedence, type casting.

Problem: Build a 24-hour time adjuster. Given a starting time in "HH:MM"
string format (24-hour clock) and an integer shift delta_minutes (which can
be positive, large, or negative):
- Parse the string into numeric hours and minutes.
- Calculate the new time strictly using arithmetic operators (//, %, +, *).
- Format the result back into a two-digit padded string "HH:MM" using f-string alignment ({:02d}).
"""


def adjust_time(start_time: str, delta_minutes: int) -> str:
    """Adjusts a 24-hour clock time by delta_minutes.

    Parameters:
        start_time (str): Time in "HH:MM" 24-hour format (e.g. "01:15").
        delta_minutes (int): Shift in minutes (can be positive, zero, or negative).

    Returns:
        str: Adjusted time formatted as "HH:MM".
    """
    # 1. Parse string into numeric hours and minutes (type casting)
    hours_str, minutes_str = start_time.split(":")
    hours = int(hours_str)
    minutes = int(minutes_str)

    # 2. Compute total elapsed minutes from 00:00
    # Multiplication (*) has higher precedence than addition (+)
    total_minutes = hours * 60 + minutes + delta_minutes

    # 3. Euclidean / Floored division arithmetic:
    # Python's // rounds towards negative infinity, and % retains the divisor's sign.
    # Total hours passed: total_minutes // 60
    # Wrapping hours into 24-hour format [0, 23]: (total_minutes // 60) % 24
    # Wrapping minutes into [0, 59]: total_minutes % 60
    new_hours = (total_minutes // 60) % 24
    new_minutes = total_minutes % 60

    # 4. Format back into two-digit zero-padded "HH:MM"
    return f"{new_hours:02d}:{new_minutes:02d}"


if __name__ == "__main__":
    # Test cases including specified edge cases
    test_cases = [
        ("01:15", -120, "23:15"),
        ("00:00", -1, "23:59"),
        ("23:45", 1500, "00:45"),
        ("12:00", 0, "12:00"),
        ("10:30", -630, "00:00"),
        ("00:05", -1440, "00:05"),  # full 24-hour negative shift
    ]

    print("Running Euclidean Clock Tests:\n" + "-" * 32)
    for start, delta, expected in test_cases:
        actual = adjust_time(start, delta)
        status = "PASS" if actual == expected else "FAIL"
        print(f"[{status}] start={start!r}, delta={delta:>6} -> got {actual!r} (expected {expected!r})")
