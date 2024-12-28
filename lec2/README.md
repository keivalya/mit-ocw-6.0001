# Branching and Iteration

## Strings in Python
- **Definition:** Strings consist of letters, special characters, spaces, and digits enclosed in quotation marks.
  ```python
  hi = "hello there"
  ```
- **String Operations:**
  - Concatenation: Combine strings with `+`.
  - Multiplication: Repeat strings using `*`.
  ```python
  name = "ana"
  greet = hi + " " + name
  silly = hi + " " + name * 3
  ```

---

## Input and Output
- **`print` Statement:** Displays output to the console.
  ```python
  x = 1
  print("My favorite number is", x)
  ```
- **`input` Statement:** Reads user input as a string.
  ```python
  num = int(input("Type a number... "))
  print(5 * num)
  ```

---

## Comparison and Logic Operators
- **Comparison Operators:** Return Boolean values (`True` or `False`).
  ```python
  i > j, i < j, i == j, i != j
  ```
- **Logical Operators:** Operate on Boolean values.
  ```python
  not a, a and b, a or b
  ```

---

## Control Flow: Branching
- **Conditional Statements:**
  ```python
  if <condition>:
      # code block
  elif <another_condition>:
      # another code block
  else:
      # fallback block
  ```
- **Key Points:**
  - `<condition>` must evaluate to `True` or `False`.
  - Indentation defines code blocks in Python.

---

## Control Flow: Loops
### `while` Loops
- Repeats code while the condition is `True`.
  ```python
  n = 0
  while n < 5:
      print(n)
      n += 1
  ```

### `for` Loops
- Iterates through a range of numbers or a sequence.
  ```python
  for n in range(5):
      print(n)
  ```
- **`range(start, stop, step)`:** Defines the range.
  ```python
  for i in range(7, 10):
      print(i)
  ```

### `break` Statement
- Exits the current loop immediately.
  ```python
  for i in range(5):
      if i == 3:
          break
      print(i)
  ```

---

## Comparing `for` and `while` Loops
- **`for` Loops:**
  - Used when the number of iterations is known.
  - Can be rewritten as `while` loops.
- **`while` Loops:**
  - Used for unbounded iterations.
  - May not always be convertible to `for` loops.

## In-Class Questions
1. **Strings** What is the value of variable `u` from the code below?
```python
once = "umbr"
repeat = "ella"
u = once + (repeat+" ")*4
```
**Ans.** `umbrella ella ella ella`

2. **Comparisons** What does the code below print?
```python
pset_time = 15
sleep_time = 8
print(sleep_time > pset_time)
derive = True
drink = False
both = drink and derive
print(both)
```
**Ans.** `False then False`

3. **Branching** What’s printed when x = 0 and y = 5?
```python
x = float(input("Enter a number for x: "))
y = float(input("Enter a number for y: "))
if x == y:
 if y != 0:
 print("x / y is", x/y)
elif x < y:
 print("x is smaller")
else:
 print("y is smaller") 
```
**Ans.** `x is smaller`

4. **While Loops** In the code below from Lecture 2, what is printed when you type “Right”?
```python
n = input("You're in the Lost Forest. Go left or right? ")
while n == "right":
 n = input("You're in the Lost Forest. Go left or right? ")
print("You got out of the Lost Forest!")
```
**Ans.** `You got out of the Lost Forest!`

5. **For Loops** What is printed when the below code is run?
```python
mysum = 0
for i in range(5, 11, 2):
 mysum += i
 if mysum == 5:
  break
  mysum += 1
print(mysum)
```
**Ans.** `5`