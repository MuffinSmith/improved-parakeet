# Bitwise Operators and XOR

In this activity, you'll 
- Develop an intuition for the behavior of XOR
- Build "truth tables" for AND, OR, and XOR

**Truth tables** depict all possible outputs of the AND, OR, and XOR operators. They help clarify why XOR is useful for cryptography, while AND and OR are not.

## Instructions

### XOR Practice

Write the result of applying XOR to each of the pairs of bytes below.

- `10110101 ^ 10101010`

- `11011010 ^ 10001010`

- `01000001 ^ 11001100`

- `11111111 ^ 11111111`

- `00000000 ^ 11111111`

- `00000000 ^ 00000000`

### Truth Tables

Fill out each of the tables below.

#### AND

Left  Operator  Right   Result
  0      &        0      
  0      &        1      
  1      &        0      
  1      &        1      

#### OR 

Left  Operator  Right   Result
  0      |        0      
  0      |        1      
  1      |        0      
  1      |        1      

#### XOR 

Left  Operator  Right   Result
  0      ^        0      
  0      ^        1      
  1      ^        0      
  1      ^        1      

### Questions

Refer to the Truth Tables above to answer the questions below.

- If you AND two randomly-chosen bits, what's the probability you'll end up with 1?

- If you OR two randomly-chosen bits, what's the probability you'll end up with 1?

- If you XOR two randomly-chosen bits, what's the probability you'll end up with 1?