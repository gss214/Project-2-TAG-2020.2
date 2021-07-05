# Project-2-TAG-2020.2

## Development Information

Project 2 of the theory and application of graphs course at UnB in 2020.2

University of Brasilia, Institute of Exact Sciences,  Computer Science Department

Theory and Application of Graphs - 2020.2

Developed by: Guilherme Silva Souza

Language used: Python

## Description

For the purpose of this project, consider that a certain unit of the federation held a competition and one hundred (100) new teachers for public schools were approved. Each approved teacher has one (1), two (2), or even (3) content qualifications in which they can act. Fifty (50) schools are eligible to receive new teachers, some of which may receive a maximum of one (1) teacher, and others a maximum of two (2) teachers. Schools can indicate teacher preferences by indicating whether 3, 2 or 1 qualification candidates must have at least. In turn, each teacher can choose an order of up to four (4) schools where they would like to work. An algorithm is implemented that makes a maximum stable matching, which must include at least 1 teacher for each school, and indicate how many teachers can be stably allocated.

The solutions given in (Abraham, Irving & Manlove, 2007) are useful and any can be implemented with relevant variations. An [entradaProj2TAG.txt](entradaProj2TAG.txt) file with the teacher code indications, school qualifications and preferences, as well as schools with their preferences in terms of teacher qualifications is provided as input. A public version of the article by (Abraham, Irving & Manlove, 2007) is provided for reading.

For better reading of the output, run the program:

python3 [main.py](main.py) > output.txt

and open the output.txt file