# What is computation?

### Readings
Chapters 1 and 2.1 of textbook.

### Key Topics Covered
1. **What is Computation?**
   - Performing calculations and storing results.
   - Built-in vs. user-defined calculations.
2. **Types of Knowledge:**
   - Declarative: Statements of fact.
   - Imperative: Step-by-step instructions (e.g., algorithms).

3. **Introduction to Algorithms:**
   - Defined as a sequence of steps with a flow of control and a stopping condition.

4. **Machine Basics:**
   - Fixed program computers (e.g., calculators) vs. stored program computers.
   - Basic architecture includes memory, control unit, arithmetic logic unit, and input/output.

### Programming Fundamentals
- **Programming Languages:**
  - Provide primitive operations and allow creation of complex expressions.
  - Syntax and semantics are critical:
    - Syntax: Structure of valid statements.
    - Semantics: Meaning of valid statements.
  - Common errors include syntax errors, static semantic errors, and unintended semantic meanings.

- **Python Basics:**
  - **Data Types:** `int`, `float`, `bool`, `NoneType`.
  - **Type Conversions:** Convert data types with functions like `int()`, `float()`.
  - **Operators:**
    - Arithmetic: `+`, `-`, `*`, `/`, `**`.
    - Precedence: Parentheses > `**` > `*` and `/` > `+` and `-`.
  - **Variables and Binding:**
    - Variables store values in memory.
    - Assign values with `=`.
    - Reassigning variables creates new bindings.

- **Expressions and Calculations:**
  - Combine objects and operators to form expressions.
  - Abstract expressions by naming values for reusability.

## In-Class Questions
1. **Shell vs. Editor.** You run the code below from the editor.
```python
type(5)
print(3.0-1)
```
What’s printed?
**Ans.** `2.0`

2. **Python vs. Math** Which is allowed in Python?
**Ans.** `xy = 2`

3. **Bindings** You run the code below from the file editor.
```python
usa_gold = 46
uk_gold = 27
romania_gold = 1

total_gold = usa_gold + uk_gold + romania_gold
print(total_gold)

romania_gold += 1
print(total_gold)
```
What’s printed?
**Ans.** `74 then 74`