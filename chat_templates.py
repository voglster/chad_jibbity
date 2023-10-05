templates = {
    "Typing & Documentation": """
Refactor this function to make it easier to read, focus on English like syntax, rename variables and 
extract variables.  Add typing on input and return, and if its not obvious on the inside of the 
function.  For Typing use the dict[]/list[] syntax over the legacy Dict[] style which requires you to 
import from typing.

Assume that any functions called but not sent are already defined.

Your reply should be code only as it will be pasted directly into an IDE, I do not require comments or explanations 
about what it is or why you chose those things.  I want the code to read as close to English as possible. Using 
python 3.10.  Follow the typing already in the function.  
    """,
    "Code": """
Assume that any functions called but not described are already defined in the locals.

Your reply should be code only as it will be pasted directly into an IDE, I do not require comments or explanations 
about what it is or why you chose those things.  I want the code to read as close to English as possible. Using 
python 3.10.  Follow the typing already in the function.  
    """,
    "Refactor Loops": """
    Refactor this by extracting inner loops into functions focus on making it as human readable as possible.

Assume that any functions called but not described are already defined in the locals.

Your reply should be code only as it will be pasted directly into an IDE, I do not require comments or explanations 
about what it is or why you chose those things.  I want the code to read as close to English as possible. Using 
python 3.10.  Follow the typing already in the function.  
    """,
    "Variable Naming": """
    Refactor this by changing and extracting variables to human readable names

Assume that any functions called but not described are already defined in the locals.

Your reply should be code only as it will be pasted directly into an IDE, I do not require comments or explanations 
about what it is or why you chose those things.  I want the code to read as close to English as possible. Using 
python 3.10.  Follow the typing already in the function.  
    """,
}
