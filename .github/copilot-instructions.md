# DSA Learning Repository - Copilot Instructions

This repository contains implementations of data structures and algorithms in multiple languages (Python, Java, C++). When working in this codebase, follow these patterns and conventions.

## Architecture & Project Structure

- **Multi-language approach**: Each data structure is implemented in Python, Java, and/or C++ to demonstrate language-specific patterns
- **Flat organization**: All files are in the root directory for easy access during learning
- **Interactive implementations**: Most files include menu-driven interfaces for testing functionality
- **No external dependencies**: All implementations use only standard library features

## Code Patterns & Conventions

### Python Files (`*.py`)
- **Class-based implementations**: Use classes for data structures (e.g., `Stack`, `Queue`, `BST`)
- **Interactive menus**: Include a `menu()` function that provides numbered options for testing
- **Dynamic resizing**: Implement automatic capacity adjustment (see `stack.py` resize logic)
- **Error handling**: Use print statements for overflow/underflow conditions, not exceptions
- **Method naming**: Use camelCase for methods (`isEmpty`, `enQueue`, `deQueue`)

Example pattern from `stack.py`:
```python
class Stack:
    def __init__(self, capacity=1):
        self.top = -1
        self.capacity = capacity
        self.A = [None] * capacity

    def push(self, data):
        if self.isFull():
            # Dynamic resizing logic here
```

### Java Files (`*.java`)
- **Static methods**: Use static methods for utility functions in application classes
- **HashMap usage**: Prefer HashMap for key-value storage (see `AttendanceSystem.java`)
- **Scanner pattern**: Use `Scanner sc = new Scanner(System.in)` as class-level static variable
- **Menu systems**: Implement do-while loops with switch-case for user interaction
- **Input validation**: Include input validation loops for user choices

### C++ Files (`*.cpp`)
- **Fixed-size arrays**: Use compile-time constants for array sizes (`#define SIZE 5`)
- **Class initialization**: Initialize arrays in constructors using loops
- **Linear probing**: Implement collision resolution in hash tables using modular arithmetic
- **Input loops**: Use do-while patterns for continuous input until user stops

## Development Workflow

### Building & Running
- **Python**: Run directly with `python filename.py` - all files include `if __name__ == "__main__"`
- **Java**: Compile with `javac` then run with `java` (see existing `.class` files)
- **C++**: Use VS Code C++ Runner extension or compile manually with `g++`

### Testing Approach
- **Interactive testing**: All implementations include menu-driven test interfaces
- **Manual verification**: Use the provided menu options to test edge cases
- **Console output**: Implementations use descriptive print statements for debugging

## File Naming Patterns

- **Descriptive names**: `stack.py`, `queue.py`, `circularLinkedList.py`
- **Algorithm implementations**: Prefix with source when appropriate (`gfgInfixtoPostfix.py`)
- **Temporary files**: Use `tempCodeRunnerFile.*` for VS Code runner temporary files
- **Project files**: Larger implementations in single files (like `DSL_mini_project`)

## Key Implementation Details

### Memory Management
- **Python**: Use list resizing for dynamic structures
- **C++**: Manual array management with fixed sizes
- **Java**: Leverage built-in collections where appropriate

### Error States
- **Consistent messaging**: Use "Stack/Queue Overflow/Underflow" terminology
- **Return patterns**: Use `None`/`null` returns for empty state access
- **Validation**: Always check empty/full states before operations

### Menu Systems Pattern
All interactive files follow this structure:
1. Display numbered options
2. Get user input with `int(input())` or `Scanner.nextInt()`
3. Use switch-case or if-elif chains
4. Include exit option
5. Loop until user chooses to exit

When implementing new data structures, follow these established patterns for consistency with the existing codebase.