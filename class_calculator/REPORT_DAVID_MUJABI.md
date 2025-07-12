*** TASK3: Language feature analysis ***
1. Language choice and justfication
 . Python programming language 
 . Infuluence : Python has high readability, simplicity and its clean syntax hence found it convenient to be used in this project.
 . Suitability: Yes — Python is highly suitable for this calculator project. It is beginner-friendly and powerful, offering robust libraries and features that enhance the functionality and scalability of the calculator

 2. Language Evaluation Criteria Analysis
    -- **Readability**: 
    . My code is very easy and with clear syntax to read and understand.

    . *** Example of a readable code snippet***
        def save_calculations(operation, result):
            try:
                with open('calculations.txt', 'a') as file:
                    file.write(f"Operation: {operation}\nResult: {result}\n\n")
                    print("\nCalculations saved successfully.")
            except FileNotFoundError:
                print("\nError occurred while saving calculations.")
            finally:
                file.close()
    ***end of the snippet***

    -- **Writability** :
    . It was easy to write the code and implement the required functionality.

    . Features: made it easier 
        - Simplicity of the programming language - the syntax is clear and easy to implement
        - Orthogonality - Python has few primitive constructs hence making it easier for me (as programmer) to grub most of the writing tools of python hence writable.
        - Expressitivity - python has powerful short hand notations such as ternary operations hence making it writable in this domain.
        - Support for abstraction - python supports abstraction hence ability to define and use complex structures is enhanced.
    
    . No - I only required few lines of code within a few time I was done. My code is only 120 lines of code.

    -- **Reliability**
    . Clear and readble syntax - making it easy to debug the code.
    . Automatic memory management - prevents leak of the memory as the gabbage collection is done automatically.
    . Strong dynamic typing handles the type correctness hence making the code reliable.
    . Exception handling - ability of a program to intercept runtime errors and handle them gracefully is a key feature of python hence making the code reliable.

    -- Yes python has strong type checking but of dynamic typing hence one cannot mix incompatible data types without explicit conversion.

    -- How i handled the runtime errors?
    . Exception handling - I used the try ... except blocks to handle errors

    -- **cost**
    . I spent around 2 weeks of concistent learnig python syntax and I was able to manouver using the programming language.
    -- Yes python is free and open source as one doesn't need to pay for the interpreter or the coding tools.
    --Python is accessible in most of the operating systems such as windows, linux and macOS.
    -- Yes it is cost effective for a business project - No licensing is required and there is robust libraries hence making it cost effective.

3. Implementation Challenges and Solutions

    -- The most challenging part was handling unexpected user input such as division by zero or the user inputing strings where integers are required.
    -- Features:
        - Dynamic typing helped me handle user input and explicit errors.
        - Built in functions such as input() helped me collect user input for the operations to perform.
        - Error handling - I used try...except blocks to handle the errors.

    -- if i used different programming language like JAVA and c++
    . I would benefit from compile-time type checking, which catches some errors earlier, before running the program.
    . However, I would also have to write more boilerplate code (like class definitions, type declarations, and input handling), which would make the project more complex and time-consuming for a beginner-level task.
    . Additionally, Java and C++ have more verbose syntax, which might make the code harder to read

4. Language Comparison
    . Python and Javascript
    - Both are high-level, interpreted languages with a focus on simplicity and ease of use.
    - python uses dynamic typing while javascript uses static typing.

    -- Python would be better due to its simplicity and ease of use. Python has a more extensive standard library . Python also uses dynamic typing hence easier to track the bugs and prevent logic errors.

    -- example of how implementation occurs
    . Python
    - def add(x, y):
        return x + y
    - print(add(3, 5))
    
    . Javascript
    - function add(x, y) {
            return x + y;
        }
    - console.log(add(3, 5));
