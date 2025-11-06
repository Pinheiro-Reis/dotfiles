---
name: Code Quality and Testing
---

# Code Quality and Testing

## Core Principle
All generated or modified code must be validated against the project's existing quality assurance tools before being considered complete.

## Validation Workflow
Before finalizing any code changes, execute the following checks if the corresponding tools are set up in the project:

- **1. Run Tests:** Execute the entire test suite (unit, integration, e2e) to confirm that existing functionality is not broken and new functionality is covered.
- **2. Lint the Code:** Run the project's linter to ensure the code adheres to established style guides and best practices.
- **3. Check Types:** Use the type-checker (e.g., TypeScript, MyPy) to identify and fix any type-related errors.
- **4. Format the Code:** Apply the project's code formatter (e.g., Prettier, Black) to maintain a consistent code style.

## Success Criteria
Code is only ready for submission when it passes all configured checks without any errors.
