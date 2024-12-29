# String Manipulation, Guess and Check, Approximations, Bisection

## String Manipulation
- **Definition:** Strings are sequences of case-sensitive characters.
- **Operations:**
  - Length: `len(s)`
  - Indexing: Use square brackets to access characters.
    ```python
    s = "abc"
    s[0]  # "a"
    s[-1]  # "c"
    ```
  - Slicing: Use `[start:stop:step]`.
    ```python
    s = "abcdefgh"
    s[3:6]  # "def"
    s[::-1]  # "hgfedcba"
    ```
  - **Immutability:** Strings cannot be modified in place.
    ```python
    s = "hello"
    s[0] = 'y'  # Error
    s = 'y' + s[1:]  # Allowed
    ```

---

## Strings and Loops
- Use `for` loops to iterate over strings.
- Example:
  ```python
  for char in "hello":
      print(char)
  ```

---

## Guess-and-Check Algorithm
- **Definition:** Systematically guess and check possible solutions.
- **Example: Finding Cube Roots**
  ```python
  cube = 8
  for guess in range(abs(cube) + 1):
      if guess**3 == abs(cube):
          if cube < 0:
              guess = -guess
          print(f"Cube root of {cube} is {guess}")
          break
  else:
      print(f"{cube} is not a perfect cube")
  ```

---

## Approximate Solutions
- **Approach:** Start with a guess and refine until the solution is "good enough."
- **Example:**
  ```python
  cube = 27
  epsilon = 0.01
  guess = 0.0
  increment = 0.0001
  while abs(guess**3 - cube) >= epsilon and guess <= cube:
      guess += increment
  print(f"{guess} is close to the cube root of {cube}")
  ```

---

## Bisection Method
- **Concept:** Halve the search space each iteration.
- **Steps:**
  1. Start with `low` and `high` bounds.
  2. Calculate `guess = (low + high) / 2.0`.
  3. Adjust bounds based on whether `guess**3` is less or greater than the target.
  - **Efficiency:** Converges in \(O(\log_2 N)\) steps.
- **Example:**
  ```python
  cube = 27
  epsilon = 0.01
  low = 0
  high = cube
  guess = (high + low) / 2.0
  while abs(guess**3 - cube) >= epsilon:
      if guess**3 < cube:
          low = guess
      else:
          high = guess
      guess = (high + low) / 2.0
  print(f"{guess} is close to the cube root of {cube}")
  ```

## In-Class Questions
1. **String Manipulations** What does the code below print?
```python
s = "6.00 is 6.0001 and 6.0002"
new_str = ""
new_str += s[-1]
new_str += s[0]
new_str += s[4::30] 
new_str += s[13:10:-1]
print(new_str)
```
**Ans.** `26 100`

2. **For Loops with Strings** How many times will the code below print “common letter”?
```python
s1 = "mit u rock"
s2 = "i rule mit"
if len(s1) == len(s2):
    for char1 in s1:
        for char2 in s2:
            if char1 == char2:
                print("common letter")
                break
```
**Ans.** `7`