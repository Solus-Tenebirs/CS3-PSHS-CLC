 
Annex C
Code Quality Assessment Worksheet
<br>
Section: 9-Samat                 
<br>
Score:____________

C# / Name: #1 / Abad,  Calix              
<br>

C# / Name: #2 / Angeles, Peter Jharielle

<br>

C# / Name: #3 / Arellano, Joaquin Ethan D.

<br>
Date: August 16,2026
_______________________________________________________________________________________________________________________
<br>
Instructions:

The problem: Finding the highest (Maximum) number from a given list of numbers.


PseudoCode 1

Algorithm FindMax1(numbers)

   max ← numbers[0]

   For i from 1 to length(numbers)-1

      If numbers[i] > max Then

         max ← numbers[i]

      EndIf

   EndFor

   Return max

EndAlgorithm

_______________________________________________________________________________________________________________________

Pseudocode 2

Algorithm FindMax2(numbers)

   For i from 0 to length(numbers)-1bigger ← true

      For j from 0 to length(numbers)-1

         If numbers[j] > numbers[i] Then

            bigger ← false

         EndIf

      EndFor

      If bigger = true Then

         Return numbers[i]

      EndIf

   EndFor

EndAlgorithm
_______________________________________________________________________________________________________________________
<br>

Questions with Checklists
1. Efficiency
Which algorithm is faster when the list of numbers is very large? Why?

<ins> **I believe that the first pseudocode is faster when the list of numbers is very large because it contains
fewer calculations compared to the second pseudocode. The first pseudocode only has one loop, while the 
second has two nested loops that perform the same operation as the loop in the first pseudocode.** </ins>



PseudoCode 1

Does the algorithm use one loop or two nested loops?
- **The algorithm uses one loop.**

Does the algorithm repeat work unnecessarily?
- **It does not.**

Which algorithm finishes in fewer steps?
- **The first one.**

<br>

PseudoCode 2

Does the algorithm use one loop or two nested loops?
- **It uses two nested loops.**

Does the algorithm repeat work unnecessarily?
- **It does.**

Which algorithm finishes in fewer steps?
- **The first one.**

_______________________________________________________________________________________________________________________


2. Readability

Which algorithm is easier to understand at first glance? What makes it clearer?

<ins> **In my opinion, the first algorithm is easier to understand at a first glance because 
it's processes are more compact and it does not waste lines on useless if and for statements.
It's logic is also easier to understand because there are fewer lines of code and the variable
names are clear, specific, and meaningful.** </ins>

Checklist to guide your answer:

PseudoCode 1

Are variable names meaningful (e.g., max vs. bigger)?
- **The variable names are meaningful.**
 
Is the logic simple or complicated?
- **The logic is simple.**

Are there fewer lines of code?
- **There is fewer lines of code.**

<br>

Psuedocode 2

Are variable names meaningful (e.g., max vs. bigger)?
- **The names are not meaningful.**

Is the logic simple or complicated?
- **The logic is complicated.**

Are there fewer lines of code?
- **There are more lines of code.**

_______________________________________________________________________________________________________________________


3. Maintainability
If you had to add a new feature (like finding both max and min), which algorithm would be easier to update? Why?

<ins> **The first algorithm would be easier to update because its structure is straightforward, and because it is so
straightforward; the user can easily identify which lines of code are the main processes, and add new steps
accordingly. This makes it have less chance to break from adding new steps, and decreases the probability
of errors appearing when updating.** </ins>


Checklist to guide your answer:

PseudoCode 1

Is the structure straightforward?
- **Yes, it is.**

Would adding new steps break the code easily?
- **No, it will not.**

Is there less chance of errors when updating?
- **Yes, there is.**

<br>

Pseudocode 2

Is the structure straightforward?
- **No, it is not.**

Would adding new steps break the code easily?
- **Yes, it may.**

Is there less chance of errors when updating?
- **No, there may not be.**

_______________________________________________________________________________________________________________________

4. Testability
Which algorithm is easier to test with different inputs? Why?

<ins> **The first pseudocode is easier to test different inputs since the user only needs to change
the contents of one list, and; the user does not need to worry as much on missing a condition, which
would lead to the code breaking from invalid input. The easy-to-read nature of the first pseudocode
also makes the output predictable and clear to the user, and it allows them to test both small lists
and large lists without issue.**
</ins>

Checklist to guide your answer:


PseudoCode 1

Can you test with small lists easily?
- **Yes, you can.**

Does the algorithm have fewer conditions to check?
- **Yes, it does.**

Is the output predictable and clear?
- **Yes, it is.**

<br>

Psuedocode 2

Can you test with small lists easily?
- **Yes, you can.**

Does the algorithm have fewer conditions to check?
- **No, it does not.**

Is the output predictable and clear?
- **No, it is not.**

_______________________________________________________________________________________________________________________


5. Security
Imagine the input list comes from a user. What should the algorithm check to avoid errors or misuse?

<ins> **The algorithm should check for empty lists, invalid inputs, or unusual inputs.**
</ins>

Checklist to guide your answer:

PseudoCode 1

Does the algorithm check if the list is empty?
- **Yes, it does.**

Does it handle invalid inputs (like letters instead of numbers)?
- **Yes, it does.**

Does it avoid crashing when inputs are unusual?
- **Perhaps, it does.**

<br>

Pseudocode 2

Does the algorithm check if the list is empty?
- **No, it does not.**

Does it handle invalid inputs (like letters instead of numbers)?
- **No, it does not.**

Does it avoid crashing when inputs are unusual?
- **Perhaps, it does**
_______________________________________________________________________________________________________________________ 

6. Final Answer
Based on your answers from 1 to 5, which one is the better algorithm that you will use to solve the problem of finding the highest number? Why? Summarize your answer

<ins> **Based on our answers, the better algorithm which we will use to solve the problem of finding the highest number
is the first algorithm, because; it handles invalid or unusual inputs well; it is easily testable; it is easy to update and append new features; it is easily readable, and it is efficient.**
</ins>
 
