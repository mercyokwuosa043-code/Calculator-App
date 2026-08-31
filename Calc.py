import easygui
import math


def calculator():
    while True:
        choice = easygui.buttonbox(
            "What would you like to calculate ?",
            "Easy Calculator",
            choices=[
                "Addition (+)",
                "Subtraction (-)",
                "Multiplication (×)",
                "Division (÷)",
                "Power (xʸ)",
                "Square Root (√)",
                "Percentage (%)",
                "Quit"
            ]
        )

        if choice is None or choice == "Quit":
            break

        # Square root
        if choice == "Square Root (√)":
            number = easygui.enterbox(
                "Enter a number:",
                "Square Root"
            )

            if number is None:
                continue

            try:
                number = float(number)

                if number < 0:
                    easygui.msgbox(
                        "You cannot calculate the square root of a negative number.",
                        "Error"
                    )
                else:
                    answer = math.sqrt(number)
                    easygui.msgbox(
                        f"√{number} = {answer}",
                        "Answer"
                    )

            except ValueError:
                easygui.msgbox(
                    "Please enter a valid number.",
                    "Error"
                )

            continue

        # Percentage
        if choice == "Percentage (%)":
            values = easygui.multenterbox(
                "Enter the percentage and the number:",
                "Percentage",
                ["Percentage:", "Number:"]
            )

            if values is None:
                continue

            try:
                percentage = float(values[0])
                number = float(values[1])

                answer = (percentage / 100) * number

                easygui.msgbox(
                    f"{percentage}% of {number} = {answer}",
                    "Answer"
                )

            except ValueError:
                easygui.msgbox(
                    "Please enter valid numbers.",
                    "Error"
                )

            continue

        # Two-number calculations
        values = easygui.multenterbox(
            f"{choice}\n\nEnter the two numbers:",
            "Calculator",
            ["First number:", "Second number:"]
        )

        if values is None:
            continue

        try:
            num1 = float(values[0])
            num2 = float(values[1])

            if choice == "Addition (+)":
                answer = num1 + num2
                symbol = "+"

            elif choice == "Subtraction (-)":
                answer = num1 - num2
                symbol = "-"

            elif choice == "Multiplication (×)":
                answer = num1 * num2
                symbol = "×"

            elif choice == "Division (÷)":
                if num2 == 0:
                    easygui.msgbox(
                        "You cannot divide by zero!",
                        "Error"
                    )
                    continue

                answer = num1 / num2
                symbol = "÷"

            elif choice == "Power (xʸ)":
                answer = num1 ** num2
                symbol = "^"

            easygui.msgbox(
                f"{num1} {symbol} {num2} = {answer}",
                "Answer"
            )

        except ValueError:
            easygui.msgbox(
                "Please enter valid numbers.",
                "Error"
            )

        except OverflowError:
            easygui.msgbox(
                "That number is too large!",
                "Error"
            )


calculator()