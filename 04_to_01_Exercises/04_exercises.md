<div align="center">
  <h1>30 Days Of Python: Days 01–04 Exercises</h1>
  <p><strong>Mastery Challenges covering Data Types, Variables, Built-ins, Operators, and Strings</strong></p>
</div>

---

## 📌 Overview

These exercises are designed to push beyond basic syntax and test your problem-solving depth using concepts introduced in **Days 01 through 04**:
- **Day 01:** Python data types (`int`, `float`, `complex`, `str`, `bool`, etc.), type inspection, numeric expressions.
- **Day 02:** Variables, dynamic typing, unpacking, built-in functions (`ord`, `chr`, `divmod`, `abs`, `round`, `len`, `min`, `max`, `sum`, etc.).
- **Day 03:** Arithmetic edge cases, negative floor division, modulo behavior, identity (`is`) vs equality (`==`), bitwise manipulation (`&`, `|`, `^`, `~`, `<<`, `>>`), and short-circuit evaluation.
- **Day 04:** String sequence mechanics, positive/negative slicing strides, advanced f-string formatting specifiers, text transformations (`split`, `join`, `strip`, `maketrans`, `translate`, `partition`, `casefold`), and character encodings.

---

## 🎯 Section 1: Number Theory, Precision & Bitwise Logic (Days 01–03)

### Challenge 1: The Zero-Arithmetic Bitwise Calculator
**Topic:** Bitwise operators (`^`, `&`, `<<`, `~`), logical operators, variables.

Write a script that computes the sum and difference of two non-negative integers **without using the arithmetic operators** `+` or `-`.

- **Requirements:**
  1. Use only bitwise operators (`^`, `&`, `<<`, `~`) and variable reassignments.
  2. Implement integer addition via bitwise carry-and-add logic:
     - Half-adder sum: `a ^ b`
     - Carry: `(a & b) << 1`
  3. Verify your solution for boundary values: `(0, 0)`, `(1, 255)`, `(1024, 2048)`.
- **Expected Outcome:**
  ```python
  # Given a = 37, b = 25
  # Sum calculated without '+' => 62
  ```

---

### Challenge 2: Modulo Arithmetic & The Euclidean Clock
**Topic:** Negative division (`//`), modulo (`%`), operator precedence, type casting.

In Python, `-13 // 5` evaluates to `-3`, and `-13 % 5` evaluates to `2`. This differs from languages like C/C++ or Java where remainder retains the dividend's sign.

- **Problem:**
  Build a 24-hour time adjuster. Given a starting time in `"HH:MM"` string format (24-hour clock) and an integer shift `delta_minutes` (which can be positive, large, or negative):
  1. Parse the string into numeric hours and minutes.
  2. Calculate the new time strictly using arithmetic operators (`//`, `%`, `+`, `*`).
  3. Format the result back into a two-digit padded string `"HH:MM"` using f-string alignment (`{:02d}`).
- **Edge cases to handle:**
  - `start = "01:15"`, `delta_minutes = -120` $\rightarrow$ `"23:15"`
  - `start = "00:00"`, `delta_minutes = -1` $\rightarrow$ `"23:59"`
  - `start = "23:45"`, `delta_minutes = 1500` $\rightarrow$ `"00:45"`

---

### Challenge 3: Arbitrary Base Converter (Base-2 to Base-36)
**Topic:** Built-ins (`int`, `str`), loops or recursion logic, string indexing, arithmetic operators.

Python provides `bin()`, `oct()`, `hex()`, and `int(val, base)`. 

- **Problem:**
  1. Given an integer $N$ and a target base $B$ ($2 \le B \le 36$), convert the decimal integer to its base-$B$ string representation using string indexing from the alphabet string:
     `"0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"`
  2. Perform the reverse operation: take the custom-base string and convert it back to decimal **without using `int(s, base)`**; use arithmetic accumulation with powers (`**` or `*`) and character lookup using `.index()` or `ord()`.
- **Sample Test:**
  - Number: `48879`, Base: `16` $\rightarrow$ `"BEEF"`
  - Number: `123456`, Base: `36` $\rightarrow$ `"2N9C"`

---

## ✂️ Section 2: Slicing Mastery & Sequence Surgery (Day 04)

### Challenge 4: The Palindrome Invariant & Substring Reversals
**Topic:** Advanced slicing (`[::-1]`, step values, start/stop bounds), string methods (`casefold`, `replace`).

A phrase is a *strict alphanumeric palindrome* if it reads the same backward and forward when ignoring punctuation, spacing, and case distinctions (e.g., German `"ß"` expands to `"ss"` under `.casefold()`).

- **Tasks:**
  1. Given a dirty sentence such as:
     `"Eva, can I see bees in a cave?"` or `"A man, a plan, a canal: Panama!"`
  2. Clean the string using pure string methods (or membership testing `in`) to retain only alphanumeric characters.
  3. Check if the string is identical to its reverse using a single slicing operation.
  4. **Extra Twist:** Extract the middle 3 characters of the cleaned palindrome using dynamic indexing based on `len(cleaned) // 2`.

---

### Challenge 5: Multi-Step De-interleaving & Matrix-like Slicing
**Topic:** Slicing with positive and negative steps, string concatenation.

You receive an obfuscated message created by interleaving two strings of equal or near-equal length:
`obfuscated = "P3y1t0hdoyns- Oiff -PPyytthhoonn"`

- **Tasks:**
  1. Extract every even-indexed character: `even_chars = obfuscated[0::2]`.
  2. Extract every odd-indexed character: `odd_chars = obfuscated[1::2]`.
  3. Reverse `odd_chars` using slicing.
  4. Check whether any common substring longer than 4 characters exists between `even_chars` and `odd_chars[::-1]`.
  5. Slice the string into three equal segments using calculated indices (account for string lengths that are not divisible by 3).

---

### Challenge 6: Caesar Cipher & Custom Substitution via `maketrans`
**Topic:** `ord()`, `chr()`, `str.maketrans()`, `str.translate()`, string indexing.

- **Problem:**
  1. Create a Caesar Cipher with shift $k = 13$ (ROT13) for both lowercase and uppercase English letters.
  2. Do **not** use conditional chains. Instead, construct the shifted alphabet string using slicing:
     ```python
     alphabet_lower = "abcdefghijklmnopqrstuvwxyz"
     shifted_lower = alphabet_lower[k:] + alphabet_lower[:k]
     ```
  3. Build a translation table using `str.maketrans()` and encode/decode an arbitrary text paragraph.
  4. Ensure all punctuation, numbers, and whitespace remain completely unaffected.

---

## 🔍 Section 3: String Analysis, Parsing & Validation (Days 02–04)

### Challenge 7: Query String Parser & Serializer
**Topic:** `split()`, `join()`, `partition()`, `strip()`, boolean validation (`startswith`, `isalnum`).

Web URLs communicate data through query strings (e.g., `"?user=alice&id=402&role=admin&active=true"`).

- **Problem:**
  Write a string parser that:
  1. Strips any leading `'?'`.
  2. Splits key-value pairs separated by `'&'`.
  3. Splits each pair on the first `'='` using `.partition('=')` or `.split('=', 1)`.
  4. Validates each key: must be a valid Python identifier (`.isidentifier()`).
  5. Validates values:
     - If all digits, convert to `int`.
     - If `'true'` or `'false'` (case-insensitive), convert to `bool`.
     - Otherwise, keep as trimmed string.
  6. Reconstruct the query string into a standardized alphabetical sorted format:
     `"active=true&id=402&role=admin&user=alice"`.

---

### Challenge 8: Semantic Version Comparator
**Topic:** String splitting, integer conversion, comparison operators (`<`, `>`, `==`).

Given two version strings conforming to SemVer format (e.g., `"v2.14.3"` and `"v2.4.10"`):

- **Tasks:**
  1. Strip leading `'v'` or `'V'` if present.
  2. Split the version string by `'.'` into Major, Minor, and Patch components.
  3. Cast each part into an integer.
  4. Compare the two versions and determine which is greater, or if they are equal:
     - Note: Lexicographical string comparison fails here because `"14" < "4"` is `False` in string comparison, but numerically `14 > 4`!
  5. Output a clean formatted sentence:
     `"Version 2.14.3 is newer than Version 2.4.10 by 10 minor versions."`

---

### Challenge 9: Credit Card Masker & Luhn Check Validator
**Topic:** String slicing, negative indexing, `.replace()`, `.isdigit()`, arithmetic & modulo.

- **Tasks:**
  1. Given a raw credit card input string like `"4532 - 8920 - 1234 - 5678"` or `"6011.1111.2222.3333"`:
     - Remove all dashes, spaces, and dots.
     - Validate that the cleaned string contains strictly digits (`.isdigit()`) and has a length between 13 and 19 characters.
  2. **Format Mask:** Display only the first 2 digits and last 4 digits, replacing all intermediate digits with `'*'`, grouped in blocks of 4 separated by hyphens (e.g., `"45**-****-****-5678"`).
  3. **Luhn Algorithm Verification:**
     - Reverse the cleaned digits.
     - Double every second digit. If doubling results in a number $> 9$, subtract 9.
     - Sum all the digits.
     - Check if `total_sum % 10 == 0`.

---

## 🎨 Section 4: Advanced Formatting & Alignment (Days 03–04)

### Challenge 10: Financial Invoice ASCII Table Generator
**Topic:** f-string specifiers (width, alignment `<, ^, >`, decimal precision `:.2f`, thousands separator `,`).

Create a python script that formats a financial invoice receipt strictly using f-strings and format specifiers.

- **Input Data:**
  - Header: Company name, invoice ID, date.
  - Line items: Each item has a description (`str`), quantity (`int`), unit price (`float`), and tax rate (`float`).
- **Formatting Requirements:**
  - Table border width: 64 characters using `'-'` and `'|'`.
  - Column 1: Description (Left-aligned, 26 chars).
  - Column 2: Qty (Centered, 6 chars).
  - Column 3: Unit Price (Right-aligned, 12 chars, formatted as `$#,##0.00`).
  - Column 4: Total (Right-aligned, 14 chars, formatted as `$#,##0.00`).
  - Summary section: Subtotal, total tax, and Grand Total with double-underline (`'=' * 64`).

*Sample Target Preview:*
```text
+----------------------------------------------------------------+
| Description                |  Qty |   Unit Price |        Total |
+----------------------------------------------------------------+
| Wireless Mechanical Kbd    |   2  |      $129.50 |      $259.00 |
| 4K Ultra-wide Monitor      |   1  |      $649.99 |      $649.99 |
| USB-C Braided Cable 2m     |   5  |       $14.25 |       $71.25 |
+----------------------------------------------------------------+
| Subtotal:                                            $980.24   |
| Tax (8.25%):                                          $80.87   |
| GRAND TOTAL:                                       $1,061.11   |
+================================================================+
```

---

### Challenge 11: Binary, Hex & Octal Dynamic Bit-Matrix
**Topic:** f-strings with numeric bases (`{:b}`, `{:08b}`, `{:X}`, `{:o}`), string concatenation, multiplication.

Write a script that takes a list of integers from `0` to `255` and outputs an 8-bit visual bitmask representation:
- Each row should show:
  - Decimal value right-padded to 3 places.
  - Hexadecimal representation with `'0x'` prefix uppercase (`0x{:02X}`).
  - Octal representation with `'0o'` prefix (`0o{:03o}`).
  - An 8-bit binary representation (`{:08b}`).
  - A visual "pin indicator" where `1` is replaced with `'●'` and `0` with `'○'`.
- Example for `42`:
  `[ 42]  HEX: 0x2A  OCT: 0o052  BIN: 00101010  PINS: ○○●○●○●○`

---

## 🧠 Section 5: Python Internals, Identity & Edge Cases (Days 01–04)

### Challenge 12: The Identity (`is`) vs Equality (`==`) Investigation
**Topic:** Memory addresses (`id()`), integer interning, string interning, operator difference.

Investigate and document the behavior of the following comparisons. Predict the output **before** running the code, and explain the underlying Python behavior for each:

```python
# Case A: Small integers vs Large integers
x = 256
y = 256
print(x == y, x is y)

a = 257
b = 257
print(a == b, a is b)

# Case B: String interning and compile-time constants
s1 = "hello_world"
s2 = "hello_world"
print(s1 is s2)

s3 = "".join(["hello", "_", "world"])
print(s1 == s3, s1 is s3)

# Case C: Dynamic construction vs literal
c1 = "python!"
c2 = "python!"
print(c1 is c2)
```
- **Question:** What is Python's integer interning range? Why does string interning apply to `s1` and `s2` but not necessarily to `s3` or `c1` in dynamic contexts?

---

### Challenge 13: Short-Circuit Logic Puzzles
**Topic:** Truthy/Falsy values, short-circuit evaluation of `and` & `or`.

In Python, `a and b` does not merely return a boolean `True`/`False`; it returns the operand that determined the result!

Predict the exact returned value and type for each of the following expressions:
1. `"" or "default_username"`
2. `0 and "never_reached"`
3. `[] or () or 0 or "Found!" or False`
4. `"admin" and 0 and "super"`
5. `not "" and (0 or 42)`

---

## 🚀 Section 6: Comprehensive Capstone Exercises

### Challenge 14: Custom Run-Length Encoding (RLE) & Decoder
**Topic:** Iteration logic, string indexing, string methods, length calculation.

Run-Length Encoding is a basic compression technique where consecutive identical characters are replaced by the character followed by the count.

- **Example:**
  - Input: `"AAAAABBBCCDAA"`
  - Encoded: `"A5B3C2D1A2"`
- **Tasks:**
  1. Write an encoder that takes an arbitrary string of uppercase letters and produces the RLE string.
  2. Write a decoder that takes the RLE compressed string (e.g., `"A5B3C2D1A2"`) and recovers the original uncompressed string.
  3. Compute the compression ratio:
     $$\text{Compression Ratio} = \left(1 - \frac{\text{len(encoded)}}{\text{len(original)}}\right) \times 100\%$$
  4. Format the final output to 2 decimal places with a percentage sign (`f"{ratio:.2f}%"`).

---

### Challenge 15: The Mini String Template Engine
**Topic:** `str.find()`, `str.replace()`, slicing, string validation.

Build a lightweight templating engine without using regular expressions or third-party libraries:

- **Template Example:**
  ```python
  template = "Hello, {{ name }}! Your account balance is ${{ balance:.2f }}. Membership status: {{ status }}."
  ```
- **Requirements:**
  1. Detect placeholders surrounded by double curly braces `{{` and `}}`.
  2. Extract the variable name and optional format specification (e.g., `name` or `balance:.2f`).
  3. Clean whitespace inside the braces (`.strip()`).
  4. Substitute values from provided variables:
     - `name = "Ada Lovelace"`
     - `balance = 1432.5`
     - `status = "ACTIVE"`
  5. If a template variable is missing from the provided variables, leave a placeholder tag: `"[MISSING: variable_name]"` instead of raising an unhandled exception.

---

## 🏆 Checklist for Completion

- [ ] Completed Section 1 (Bitwise math, Euclidean clock, Base converter)
- [ ] Completed Section 2 (Slicing tricks, de-interleaving, Caesar cipher)
- [ ] Completed Section 3 (URL query parser, SemVer comparator, Luhn validator)
- [ ] Completed Section 4 (Financial ASCII table, bit-matrix visualizer)
- [ ] Completed Section 5 (Memory/interning investigation, short-circuit logic)
- [ ] Completed Section 6 (RLE compressor, mini template engine)
