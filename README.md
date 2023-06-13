# Add-Up-To

Add-Up-To is a Python program designed to calculate math expressions in order to achieve a target sum of 10. This project was inspired by the mobile game "4=10," where players are given four numbers and are required to place mathematical operators between them to obtain a total of 10. Add-Up-To automates this process by generating and evaluating various combinations of operators and operands to find a solution.

</br>

## Screenshots

### Mobile Game Snapshot

![Mobile Game Snapshot](/img/four_ten_screenshot.jpeg)

### Add-Up-To Snapshot

![Add-Up-To Snapshot](/img/terminal_screenshot.png)

The above screenshots provide a visual representation of the "4=10" mobile game and the Add-Up-To program. They aim to give you an idea of how the game looks and how the program operates.

</br>

## Installation

To use Add-Up-To, follow these steps:

1. Clone the repository to your local machine using the following command:

```shell
git clone https://github.com/uhmin99/add-up-to.git
```

2. Ensure you have Python 3.x installed on your system.

3. Navigate to the project directory:

```shell
cd add-up-to
```

</br>

## Usage

To run Add-Up-To, execute the following command in your terminal or command prompt:

```shell
python3 main.py
```

You will be prompted to enter four numbers. After entering the numbers, the program will generate and evaluate mathematical expressions using the provided numbers to reach the target sum of 10. The program will display the valid expressions that yield the desired result.

## Example

Let's say you input the numbers 1, 2, 3, and 4. The program will evaluate various combinations of these numbers with mathematical operators (+, -, *, /) to find expressions that equal 10. For instance, it will display:

```
Find Expression for result 10
(To exit enter q)
INPUT NUMBERS : 1 2 3 4
ANSWER IS  1+2+3+4
(calculation time : 0.0004019737243652344 sec)
```

</br>

## Note

Please be aware that this program may have some bugs or limitations. While every effort has been made to ensure its accuracy, there could be edge cases or unanticipated scenarios where the program may not produce the desired result.

Furthermore, it's important to note that the program currently utilizes the eval() method in Python to evaluate the mathematical expressions. The eval() method can execute arbitrary code, so it is crucial to only input trusted and sanitized input. Using untrusted or unsanitized input with the eval() method can potentially lead to security vulnerabilities.

If you plan to use this program in a production environment or accept user input, it is strongly recommended to implement additional input validation and sanitization techniques to prevent potential security risks.

If you encounter any issues, discover vulnerabilities, or have suggestions for improvement, we encourage you to contribute to this project.

</br>

## Contributing

Contributions are welcome! If you would like to contribute to Add-Up-To, please follow these steps:

1. Fork the repository.
2. Create a new branch with a descriptive name related to your contribution.
3. Make your changes and ensure that the program is still functioning correctly.
4. Commit your changes and push them to your forked repository.
5. Submit a pull request, clearly describing the changes you have made.

Your contributions can include bug fixes, feature enhancements, or other improvements. We appreciate your effort in making this project better for everyone.