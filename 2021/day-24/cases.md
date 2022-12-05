
The parameters of the various steps differ as follows (in the format `[AA, BB, CC]`).  Note that `BB` (divisor) comes before `AA` in the actual instruction sequences since I saw `AA` first.
```python
PARAMETERS = [
    [11, 1, 6],    # 0  - a
    [11, 1, 12],
    [15, 1, 8],
    [-11, 26, 7],  # 3  - d
    [15, 1, 7],
    [15, 1, 12],
    [14, 1, 2],    # 6  - g
    [-7, 26, 15],
    [12, 1, 4],
    [-6, 26, 5],   # 9  - j
    [-10, 26, 12],
    [-15, 26, 11],
    [-9, 26, 13],  # 12
    [0, 26, 7],
]
```

Decompiling the repeating blocks of instructions:
```python
for ix in range(14):
    w = next(model_iter)
    x = z % 26

    z = math.trunc(z / PARAMETERS[ix][1])
    x += PARAMETERS[ix][0]

    if x != w:
        z *= 26
        y = w + PARAMETERS[ix][2]
        z += y
```

Convert `z` into an actual stack, since that's its purpose:
```python
for ix in range(14):
    w = next(model_iter)
    x = stack[-1]

    if ix in [3, 7, 9, 10, 11, 12, 13]:
        stack.pop()
    x += PARAMETERS[ix][0]

    if x != w:
        y = w + PARAMETERS[ix][2]
        stack.push(y)
```

For the additive cases (0, 1, 2, 4, 5, 6, 8), the `x != w` check always returns `True`, since we're adding numbers and get something that is outside the range of a single Base10 digi.

However, for the subtractive cases (3, 7, 9, 10, 11, 12, 13), we are popping things, before (potentially) removing things.  So, for these cases, we are either decreasing the number of items on the stack (getting us closer to the zero that we desire), or, at worst, we are keeping the numbers the same.

To get to `z == 0` at the end, we need to ensure that the `stack.pop()` commands are not undone by additional `stack.push()`s.  Therefore, for the subtractive cases, we need to ensure that `x` **equals** `w + CC`.  Any model number for which these checks are not valid will lead to additional `stack.push()`s.

Taking Block 3 as an example:
* `x == stack_prev + AA_3`
* `x == c + CC_2 + AA_3`
* `x == c + 8 - 11`
* `x == c - 3`

```
Push A - 0          [A]
 Push B - 1         [A, B]
  Push C - 2        [A, B, C]
  Pop C - 3         [A, B]
  -- nil D - 3                      c:2 and d:3
  Push E - 4        [A, B, E]
   Push F - 5       [A, B, E, F]
    Push G - 6      [A, B, E, F, G]
    Pop G - 7       [A, B, E, F]
    -- nil H - 7                    g:6 and h:7
    Push I - 8      [A, B, E, F, I]
    Pop I - 9       [A, B, E, F]
    -- nil J - 9                    i:8 and j:9
   Pop F - 10       [A, B, E]
   -- nil K - 10                    f:5 and k:10
  Pop E - 11        [A, B]
  -- nil L - 11                     e:4 and l:11
 Pop B - 12         [A]
 -- nil M - 12                      b:1 and m:12
Pop A - 13          []
-- nil N - 13                       a:0 and n:13
```

* 3:  `c + CC_2 + AA_3`, becomes `c + 8 - 11`, therefore **`d == c - 3`**
* 7:  `g + CC_6 + AA_7` becomes `g + 2 - 7`, therefore **`h == g - 5`**
* 9:  `i + CC_8 + AA_9` becomes `i + 4 - 6`, therefore **`j == i - 2`**
* 10: `f + CC_5 + AA_10` becomes `f + 12 - 10`, therefore **`k == f + 2`**
* 11: `e + CC_4 + AA_11` becomes `e + 7 - 15`, therefore **`l == e - 8`**
* 12: `b + CC_1 + AA_12` becomes `b + 12 - 9`, therefore **`m == b + 3`**
* 13: `a + CC_0 + AA_13` becomes `a + 6 - 0`, therefore **`n == a + 6`**

So, for the number `abcd efgh ijkl mn`, we need the following relationships and pairings of `(X, Y)` (for example, `(e, l) == (9, 1)`):
* **`d == c - 3`** &rarr; `(c, d)`: `[(4, 1), (5, 2), (6, 3), (7, 4), (8, 5), (9, 6)]` 
* **`h == g - 5`** &rarr; `(g, h)`: `[(6, 1), (7, 2), (8, 3), (9, 4)]`
* **`j == i - 2`** &rarr; `(i, j)`: `[(3, 1), (4, 2), ... (9, 7)]`
* **`k == f + 2`** &rarr; `(f, k)`: `[(1, 3), (2, 4), ... (7, 9)]`
* **`l == e - 8`** &rarr; `(e, l)`: `[(9, 1)]`
* **`m == b + 3`** &rarr; `(b, m)`: `[(1, 4), (2, 5), ... (6, 9)]`
* **`n == a + 6`** &rarr; `(a, n)`: `[(1, 7), (2, 8), (3, 9)]`


## Running
Run `./alu-monad-sre.py input.txt`, which only takes a few seconds to verify the possible model numbers.

Other files (`alu-standalone.py` and `alu-monad-check.py`) were prior, failed (and horrible) attempts at other approaches.

