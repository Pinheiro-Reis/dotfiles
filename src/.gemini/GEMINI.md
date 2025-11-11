## Instructions

This document contains mandatory guidelines that must be followed with absolute rigidity. These instructions apply to all development tasks without exception and deviation is not permitted. They must be reviewed and applied repeatedly to ensure strict adherence to project standards.

When available, automatic code formatters should be used exclusively instead of manual formatting. Direct formatting of code is strictly prohibited when formatter tools are accessible, ensuring consistency and code quality.

Documentation located in project roots, in .github/ directories, or in any other standard locations must be read and followed with absolute rigidity. This includes files such as README.md, CONTRIBUTING.md, SECURITY.md, and TESTING.md. These documents contain project-specific guidelines that supersede general practices. Ignoring such documentation is strictly prohibited.

### Core Principles

- **Clarity and Readability:** Prioritize self-explanatory code over comments. Comments should generally be avoided. If a comment is absolutely essential for clarity, seek explicit user permission before adding it, and ensure it is concise, helpful, and in English.
- **Maintainability:** Design code with maintenance in mind. This includes modularity, low coupling, high cohesion, and adherence to established design patterns. Make it easy to identify and fix bugs, as well as add new features.
- **Scalability and Performance:** Consider the performance and scalability of the solution. Optimize where necessary, but avoid premature optimization. Understand load requirements and how the system will behave under stress.
- **Robustness and Error Handling:** The system must be resilient to unexpected inputs and failures. Implement comprehensive and effective error handling, logging relevant information for debugging without exposing sensitive data.
- **Security:** Security must be a primary concern in all phases of development. Follow best security practices to protect against common vulnerabilities such as SQL injection, XSS, CSRF, and ensure the protection of sensitive data.
- **Testability:** Code should be designed to be easily testable. This means writing modular code, with well-defined dependencies, allowing for the creation of effective unit, integration, and system tests.
- **Consistency:** Maintain consistency throughout the project, from naming and code style to architecture and design patterns. This facilitates collaboration and code understanding.
- **Do Not Repeat Yourself (DRY):** Avoid code duplication. Refactor code to reuse common functionalities, promoting maintainability and reducing the chance of bugs.
- **You Aren't Gonna Need It (YAGNI):** Do not add functionality that is not strictly necessary at the moment. This helps keep the code simple, focused, and avoids unnecessary complexity.
- **Single Responsibility Principle (SRP):** Each module, class, or function should have only one reason to change. This promotes cohesion and reduces coupling.

### Code Quality and Standards

- **Code Review:** Actively participate in code reviews, offering constructive feedback and accepting criticism to improve code quality. Ensure that reviewed code meets project standards and best practices.
- **Testing:**
  - **Always Test and Update:** Always write tests when possible and update existing tests whenever new features are added or current ones are modified. Ensure tests are comprehensive.
  - **Unit Tests:** Write comprehensive unit tests for each code unit (functions, methods, classes), ensuring that each individual part works correctly.
  - **Integration Tests:** Create integration tests to verify that different modules or services interact correctly.
  - **End-to-End (E2E) Tests:** Develop E2E tests to simulate real user scenarios and ensure that the entire system functions as expected.
  - **Test Automation:** Automate the execution of all tests as part of the CI/CD pipeline to ensure quick feedback on code quality.
- **Code Documentation:**
  - **Docstrings/JSDoc:** For functions, classes, and modules, use docstrings or similar formats to describe their purpose, parameters, returns, and any side effects.
  - **READMEs:** Keep README files updated, providing clear instructions on how to set up, run, test, and contribute to the project.
- **Naming Conventions:** Strictly follow established naming conventions for variables, functions, classes, files, and directories, ensuring consistency and clarity.
- **Error and Exception Handling:** Implement consistent and robust error handling. Properly capture exceptions, log relevant details, and provide clear feedback to the user or monitoring systems. Avoid exposing sensitive internal details in public error messages.
- **Performance:** Monitor and optimize code performance when necessary, based on actual metrics and profiles. Avoid bottlenecks and use efficient data structures and algorithms. Consider caching and database optimization techniques.

### Project Conventions

- **Compliance with Existing Conventions:** Always follow project conventions when reading or modifying code. This includes code style, directory structure, design patterns, and architectural patterns.
- **Dependency Management:** Manage project dependencies explicitly and consistently. Use package management tools (npm, pip, Maven, etc.) to declare and control dependency versions. Keep dependencies updated to ensure security and performance, resolving conflicts when necessary.
- **Version Control (Git):**
  - **Workflow (Gitflow/GitHub Flow):** Follow a defined version control workflow (e.g., Gitflow, GitHub Flow) to manage branches, releases, and hotfixes.
  - **Commit Messages:** Write clear, concise, and descriptive commit messages, following a consistent pattern (e.g., Conventional Commits). Include a brief title and a body explaining the *why* of the change, not just the *what*.
  - **Branches:** Use short, descriptive branches for new features or bug fixes. Merge frequently to avoid large deviations from the main branch.
- **Environments (Development, Staging, Production):** Understand and respect the different project environments. Ensure that environment-specific configurations and data are managed securely and separately.
- **Continuous Integration/Continuous Delivery (CI/CD):** Use CI/CD pipelines to automate code building, testing, and deployment. Ensure that all commits pass CI pipelines before being merged into the main branch.
- **Avoid Framework/Library Assumptions:** Never assume that a library or framework is available or appropriate without verifying its use and acceptance in the project. Add new technologies only if there is a clear and justified need.
- **Style and Structure Mimicry:** When adding new features or files, mimic the style, structure, framework choices, typing, and architectural patterns of existing code to maintain consistency.
- **Inclusion of Tests for New Features:** Always include tests (unit, integration, E2E) when adding new features to ensure quality and prevent regressions.
- **Analysis of Similar Files:** Before making edits, analyze similar files to follow the current project pattern and avoid consistency failures.
- **Component Usage:** Whenever possible, utilize components in the most organized manner, considering both global and local components to promote reusability and maintain a clean architecture.


### Collaboration and Communication

- **Clear and Concise Communication:** Maintain clear, concise, and timely communication with the team, stakeholders, and users. Use appropriate communication tools for each context (e.g., chat for quick questions, email for formal discussions, project management systems for task updates).
- **Openness to Feedback and Review:** Be open to receiving and providing constructive feedback on code and design decisions. Actively participate in code reviews and technical discussions, contributing to the continuous improvement of the team and the project.
- **Task and Progress Management:** Use task management systems (Jira, Trello, GitHub Issues, etc.) to track task progress, report bugs, and manage features. Keep task statuses updated and provide realistic estimates.

### File Management

- **Use English for File Content:** The content of all code and documentation files (except when the content is language-specific for the end-user) should always be in English to ensure standardization and facilitate international collaboration.
- **Directory Structure:** Maintain a logical and consistent directory structure. Organize files so they are easy to find and understand, following common patterns for the language or framework used (e.g., `src`, `test`, `docs`, `config`).
- **Respect Structure and Formatting:** When making changes, always respect the original formatting and semantic structure (headings, sections) of files, unless explicitly instructed otherwise.

