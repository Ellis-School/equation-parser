

def get_elements(equation):
    terms = equation.split(" ")

    total_terms = []

    for term in terms:
        coeff = ""
        actual_coeff = 0
        current_term = ""
        is_in_term = False
        for c in term:
            if (c.isnumeric() or c == ".") and not is_in_term:
                coeff += c
            else:
                is_in_term = True
                if not coeff:
                    coeff = "1"
                actual_coeff = float(coeff)
                current_term += c

        if actual_coeff > 0:
            total_terms.append((actual_coeff, current_term))

    term_count = {}
    for term in total_terms:
        if term[1] in term_count:
            term_count[term[1]] = term_count[term[1]] + term[0]
        else:
            term_count[term[1]] = term[0]

    elements = {}
    for key in term_count:
        value = term_count[key]
        current_element = ""
        current_coeff = ""
        for c in key:
            if not c.isalnum():
                continue
            
            if c.isnumeric():
                current_coeff += c
            elif c.isupper() and current_element:
                if current_element in elements:
                    if current_coeff:
                        elements[current_element] = elements[current_element] + (value * float(current_coeff))
                    else:
                        elements[current_element] = elements[current_element] + value
                else:
                    if current_coeff:
                        elements[current_element] = value * float(current_coeff)
                    else:
                        elements[current_element] = value
                current_element = c
                current_coeff = ""
            else:
                current_element += c
                
        if current_element:
            if current_element and current_element in elements:
                if current_coeff:
                    elements[current_element] = elements[current_element] + (value * float(current_coeff))
                else:
                    elements[current_element] = elements[current_element] + value
            else:
                if current_coeff:
                    elements[current_element] = value * float(current_coeff)
                else:
                    elements[current_element] = value
    return elements
    
def count(equation):
    elements = get_elements(equation)

    for key in elements:
        print(f"{key}, {elements[key]}")

def balance(equation):
    sides = equation.split("=")
    reactants = get_elements(sides[0])
    products = get_elements(sides[1])
    print(reactants, products)

def main():
    while True:
        arg_input = input("> ")
        args = arg_input.split(" ", 1)

        if len(args) < 2:
            print("Min 2 args.")

        if args[0] == "count":
            count(args[1])
        elif args[0] == "balance":
            balance(args[1])
        else:
            break;

if __name__ == "__main__":
    main()
