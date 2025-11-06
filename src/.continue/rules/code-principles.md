---
name: Code Principles
---

# Code Principles

## Core Values
Prioritize simplicity, component architecture, well-thought code structure, and readability.

## Simplicity First
- Prefer simple solutions over complex ones
- Avoid over-engineering
- Use straightforward logic when possible
- Don't add features or abstractions until needed (YAGNI)
- Favor explicit over implicit
- Choose boring technology and proven patterns

## Component Architecture
- Break code into small, focused components
- Each component should have a single responsibility
- Components should be loosely coupled
- Make components reusable and composable
- Define clear interfaces between components
- Separate concerns (business logic, UI, data access, etc.)

## Well-Thought Structure
- Plan before coding
- Consider scalability and maintainability
- Think about edge cases and error handling
- Design for testability
- Consider the impact of changes
- Refactor when structure becomes unclear

## Code Organization
- Group related functionality together
- Use clear file and folder structure
- Keep files small and focused
- Separate configuration from implementation
- Organize imports logically
- Follow consistent project structure patterns

## Readability
- Code is read more than it's written
- Use descriptive, meaningful names
- Write self-documenting code
- Add comments only when necessary to explain "why", not "what"
- Keep functions/methods short and focused
- Use consistent formatting and style
- Prefer clarity over cleverness
- Make the code flow logically

## Code Quality Checklist
Before committing code, ensure:
- [ ] Is this the simplest solution?
- [ ] Are components properly separated?
- [ ] Is each component doing one thing well?
- [ ] Would another developer understand this code?
- [ ] Are names clear and descriptive?
- [ ] Is the code structure logical?
- [ ] Can this be tested easily?

## Anti-Patterns to Avoid
- God objects/classes
- Deep nesting
- Long functions (>20-30 lines)
- Cryptic variable names
- Duplicated code
- Tight coupling
- Hidden dependencies
- Magic numbers/strings
