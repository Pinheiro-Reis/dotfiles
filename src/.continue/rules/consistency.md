---
name: Consistency and Pattern Matching
---

# Consistency and Pattern Matching

## Core Rule
**Always follow existing project patterns and conventions.**

## Before Creating or Modifying Code

### 1. Read Similar Files
When creating a new file, find and read similar existing files:
- Similar components
- Same file type
- Related functionality
- Same layer (UI, service, model, etc.)

### 2. Analyze Similar Code Sections
When adding functionality, examine:
- Similar functions in the same file
- Similar implementations in related files
- Existing patterns for the same type of operation
- How errors are handled in similar contexts

### 3. Match Patterns
Follow the existing patterns for:
- File structure and organization
- Naming conventions (camelCase, PascalCase, snake_case, etc.)
- Import order and grouping
- Function/method signatures
- Error handling approaches
- Logging patterns
- Configuration management
- Test structure
- Documentation style

## Pattern Detection Areas

### Code Style
- Indentation (spaces/tabs, size)
- Quote style (single/double)
- Semicolons usage
- Line breaks and spacing
- Bracket placement

### Architecture Patterns
- How components are structured
- Dependency injection style
- State management approach
- Data flow patterns
- Module organization

### Naming Patterns
- File naming (kebab-case, PascalCase, etc.)
- Variable naming conventions
- Function naming patterns
- Class/interface naming
- Constant naming (UPPER_CASE, etc.)

### Technical Patterns
- How async operations are handled
- Error handling strategy
- Validation approach
- Type definitions location and style
- Configuration management
- Environment variables usage

## Workflow

1. **Search** for similar implementations in the codebase
2. **Read** at least 2-3 similar files/functions
3. **Identify** the patterns being used
4. **Follow** those patterns exactly
5. **Maintain** consistency even if you see a better way

## Suggesting Improvements

When you notice a potential improvement:
- **DO**: Mention it briefly after completing the task
- **DON'T**: Implement it unless explicitly requested
- **Format**: "Note: consider [brief suggestion] for [reason]"

**Example:**
"Files created following existing service pattern. Note: consider extracting validation logic to shared utility."

## When Patterns Conflict

If you find inconsistent patterns in the project:
1. Follow the most recent pattern
2. Follow the pattern in the same module/directory
3. Mention the inconsistency briefly
4. Let the user decide

## Priority Order

1. Project-specific conventions (highest)
2. Framework/library conventions
3. Language conventions
4. General best practices (lowest)

## Summary
Consistency > Personal preference. Always match the existing codebase style and patterns.
