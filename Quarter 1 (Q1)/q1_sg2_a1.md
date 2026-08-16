Annex B
Computational Thinking Exercise: "Smart Vending Machine"
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


Scenario
Your school installs a vending machine to provide snacks and drinks. However, students encounter several issues:

Sometimes the machine does not give the correct change.
Items run out, but the machine doesn’t notify anyone.
Students press the wrong buttons and get the wrong item.
The machine is slow when multiple students use it in succession.
Your task is to decompose this problem into smaller, manageable parts that could be solved with computational thinking (CT) Skills.

Step 1: Identify the Big Problem
Main Problem: The school vending machine is unreliable, lacks proper feedback, is prone to user error, and performs poorly under repeated use and that results in a frustrating and unsatisfactory experience for students.

Step 2: Identify three to four Sub-Problems
Please list possible sub-problems:

1. Missing stock monitoring and alert system - The machine cannot detect when items are sold out, nor automatically send a notification to staff to restock.

2. Incorrect change - The machine fails to properly compute, count, or return the correct amount of money after payment.

3. Slow performance during prolonged use - The machine’s processing or dispensing speed degrades when many students use it one after another, which shows inefficient workflow.

4. Unclear or error-prone user interface - Buttons/labels are confusing or lack  steps, so students easily select the wrong products.


Step 3: Define Computational Thinking Approaches
For each sub-problem, apply CT skills:

Sub-Problem 1:
Missing stock monitoring and alert system - The machine cannot detect when items are sold out, nor automatically send a notification to staff to restock.

CT Skill:
Decomposition

Example Solution
Divide the monitoring into different steps.
1.) Check current stock
2.) Compare current stock with the minimum threshold acceptable.  
3.) If an item falls below the minimum threshold, identify said item
4.) Send an alert to the supplier of the item that fell below the minimum accepted threshold.

Sub-Problem 2:
Incorrect change - The machine fails to properly compute, count, or return the correct amount of money after payment.


CT Skill: 
Algorithm

Example Solution:
Scan the coin or bill inserted. 
Then, compare the value of the coin/bill to the value of the desired consumer good.
Subtract the value of the desired consumer good from the value of the coin/bill.
Scan the coins/bills in the change registrar and compute how many of each shall be given to the consumer to match the change
Provide exactly how many of each coin/bill to the consumer


Sub-Problem 3:
Slow performance during prolonged use - The machine’s processing or dispensing speed degrades when many students use it one after another, which shows inefficient workflow.

   
CT Skill: 
Abstraction

Example Solution:
Treat every person as an individual instance instead of keeping data from previous transactions. 
Keep only the required data for the current transaction and clear memory of unnecessary data after every order.

Sub-Problem 4:
Unclear or error-prone user interface - Buttons/labels are confusing or lack  steps, so students easily select the wrong products.

CT Skill: 
Pattern recognition and Logical thinking

Example Solution:
Identify repeated human errors such as accidental presses, and implement a system which asks to confirm your selection.
Show a screen which displays the item and its price with the words Confirm and Cancel at the bottom. 
If the person clicks cancel, remove the item from their transaction.
If the person clicks confirm, add the item to their transaction.


Step 4: Draw a flowchart or write a pseudocode for the identified sub-problem (Your group could use a separate sheet of paper)
[- **Flowchart for Sub problem 2** -](https://canva.link/d4nse31t7fmz4w5)
