# T1W8 Saturday
# Virtual Environments
- They help create isolated environments for your projects, ensuring each project has its own dependencies.

# Testing
- Allows us to confirm whether the application works as intended or not.
- Helps catch bugs early and ensure that your code behaves smoothly.

## Types of Testing
- Manual vs Automated
    - Manual: When a person manually performs tasks, based on events.
    - Automated: Programmed tests, also called scripts, to automatically perform tasks without human involvement.
- Unit testing: Testing specific components/functions/methods.
- Integration testing:  Testing the compatibility with other modules or packages.
- Chaos testing: Making a program break on purpose by disabling a function or feature to see how errors are handled.
- Stress testing: Testing in high volume of data/inputs (depending on use-case).
- End to end / Acceptance testing: Testing done towards the end of the project, when it is almost complete, to ensure things work effectively.

Note: Great idea to organise your directory structure for maintenance and easy access.

## pytest
- Power and user-friendly testing framework.
- Simple yet powerful.
- pytest follows the principle of 'assert'-ing that things are true in order for a test to pass.
- For a test to pass, the assert value must be true.

- Reading test output: . means pass, F means failed, E means exceptions.

### Exceptions
- Used to check what happens when things go wrong.
- How your program is handled when things go wrong.

### Parameterized tests
- Might want to test the same function with multiple inputs.
- parametrize creates different test cases for all the inputs provided.
- Make sure you initialise the packages to use them in other folders.

### Fixtures
- Arrange and prepare data before running tests.
- Reusable code.
- Fixture Scopes: function, class, module, package, session (when to destroy the fixture)

# File Handling
- Read and write data from and to files.
- Before performing any operation, its important to open the file, and close when you're done.
- Operations:
    - Open
    - Read
    - Write
    - Close (Why close? Ensures buffers are flushed and resources are freed.)
- 'with' statement: Automatically closes file when you are done.