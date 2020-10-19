# Scissors-Rock-Cloth
Algorithm introduction:
1. Mapping rock-paper-scissors into specific integers;
Such as scissors-0, rock-1, cloth-2
2. Perform difference calculation between the punch value given by human and computer;
3. The results are:
a. In a tie (scissors-scissors, rock-rock, cloth-cloth) the difference is 0;
b. When a person wins (scissors-cloth, rock-scissors, cloth-rock) the difference is -2, 1, 1;
c. When the person is negative (scissors-rock, rock-cloth, cloth-scissors), the difference is -1, -1, 2;
4. Only judge the difference and get the result of the guessing box;
