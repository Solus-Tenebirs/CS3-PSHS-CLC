Annex B
Computational Thinking Exercise: "Smart Vending Machine"
Section: 9-Samat                  Score:____________

C# / Name: #3 / Arellano, Joaquin Ethan D. Date: August 14,2026


Scenario
Your school installs a vending machine to provide snacks and drinks. However, students encounter several issues:

Sometimes the machine does not give the correct change.
Items run out, but the machine doesn’t notify anyone.
Students press the wrong buttons and get the wrong item.
The machine is slow when multiple students use it in succession.
Your task is to decompose this problem into smaller, manageable parts that could be solved with computational thinking (CT) Skills.

Step 1: Identify the Big Problem
Main Problem: Vending Machine is inefficient, is unreliable, and is prone to mechanical failures

Step 2: Identify three to four Sub-Problems
Please list possible sub-problems:

1. Vending machine does not notify the supplier when items run out

2. Vending machine fails to provide the correct change for the consumer goods
  
3. Vending machine starts to become sluggish after repeated use.
   
4. Vending machine does not confirm orders or when the buttons are pressed

Step 3: Define Computational Thinking Approaches
For each sub-problem, apply CT skills:

Sub-Problem 1:
Vending machine does not notify the supplier when items run out

CT Skill:
Decomposition

Example Solution
Compare current stock with the minimum threshold acceptable. Then, send an alert to the supplier of the item that exceeded the minimum accepted threshold.

Sub-Problem 2:
Vending machine fails to provide the correct change for the consumer goods


CT Skill: 
Algorithm

Example Solution:
Scan the coin or bill inserted. 
Then, compare the value of the coin/bill to the value of the desired consumer good.
Subtract the value of the desired consumer good from the value of the coin/bill.
Scan the coins/bills in the change registrar and compute how many of each shall be given to the consumer to match the change
Provide exactly how many of each coin/bill to the consumer


Sub-Problem 3:
Vending machine starts to become sluggish after repeated use.

   
CT Skill: 
Abstraction

Example Solution:
Treat every person as an individual instance instead of  a collection of data. 
Clear memory after every order.

Sub-Problem 4:
Vending machine does not confirm orders or when the buttons are pressed

CT Skill: 
Pattern recognition and Logical thinking

Example Solution:
Identify repeated human errors such as accidental presses, and implement a system which asks to confirm your selection.


Step 4: Draw a flowchart or write a pseudocode for the identified sub-problem (Your group could use a separate sheet of paper)

