def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    first_operands = []
    second_operands = []
    operators = []
    results = []
    
    for problem in problems:
        parts = problem.split()
        if len(parts) != 3:
            return "Error: Invalid format."
        
        first, operator, second = parts
        
        if not (first.isdigit() and second.isdigit()):
            return "Error: Numbers must only contain digits."
        
        if operator not in ("+", "-"):
            return "Error: Operator must be '+' or '-'."
        
        if len(first) > 4 or len(second) > 4:
            return "Error: Numbers cannot be more than four digits."

        first_operands.append(first)
        second_operands.append(second)
        operators.append(operator)

        # Calcul du résultat si demandé
        if show_answers:
            result = str(eval(first + operator + second))
            results.append(result)

    # Construction des lignes
    first_line = ""
    second_line = ""
    dashes_line = ""
    result_line = ""

    for i in range(len(problems)):
        width = max(len(first_operands[i]), len(second_operands[i])) + 2
        first_line += first_operands[i].rjust(width) + "    "
        second_line += operators[i] + " " + second_operands[i].rjust(width - 2) + "    "
        dashes_line += "-" * width + "    "
        if show_answers:
            result_line += results[i].rjust(width) + "    "

    # Suppression des espaces en trop à la fin
    arranged_problems = first_line.rstrip() + "\n" + second_line.rstrip() + "\n" + dashes_line.rstrip()
    if show_answers:
        arranged_problems += "\n" + result_line.rstrip()

    return arranged_problems


# Exemple d'utilisation
print(arithmetic_arranger(["3801 - 2", "123 + 49"], True))
