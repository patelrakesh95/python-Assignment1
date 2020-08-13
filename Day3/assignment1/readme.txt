System Properties in Python
1. Class name: SystemProperties
2. Input: Command
3. Output: Display user's name, OS name and user directory of OS
4. Logic: If command is
    a. "whoami" ->  Print user's name;
    b. "uname" -> Print OS name;
    c. "udir" -> Print user directory of Linux
    d. "all" -> Print All above
5. Make separate methods for each functionality.
6. The method will display the required command output.
7. Caller class name: ShowSystemProperties; 
    will only pass the argument from Command line to the public method of "SystemProperties".
    The decision of "Command" will be in callee class and not in the main() method.
