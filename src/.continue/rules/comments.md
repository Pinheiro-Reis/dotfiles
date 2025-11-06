---
name: Comments Policy
---

# Comments Policy

## Default Rule
**Avoid comments. Write readable code instead.**

Code should be self-explanatory through:
- Clear variable names
- Descriptive function names
- Well-structured logic
- Small, focused functions

## When Comments Are Acceptable

### 1. Grouping Multiple Definitions
When multiple related constants, types, or configurations need grouping for readability:
```typescript
// Database configuration
const DB_HOST = 'localhost';
const DB_PORT = 5432;
const DB_NAME = 'myapp';

// Cache settings
const CACHE_TTL = 3600;
const CACHE_MAX_SIZE = 1000;
```

### 2. Following Project Standards
When the existing codebase has an established commenting pattern, maintain consistency.

### 3. TODO Markers
For marking temporary code or future work:
```typescript
// TODO: Implement caching mechanism
// TODO: Add input validation
// FIXME: Handle edge case when array is empty
```

### 4. User Request
When explicitly requested by the user.

## Comments to NEVER Write

❌ **Obvious comments** - explaining what the code clearly does
```typescript
// Bad
let count = 0; // Initialize count to zero
count++; // Increment count
```

❌ **Redundant comments** - repeating the function/variable name
```typescript
// Bad
// Gets the user name
function getUserName() { ... }
```

❌ **Outdated comments** - better to remove than keep wrong information

❌ **Commented-out code** - use version control instead

❌ **Explaining "what"** - code should show what it does

## Better Alternative: Refactor

Instead of commenting, refactor:

**Bad:**
```typescript
// Check if user is adult and has valid subscription
if (user.age >= 18 && user.subscription && user.subscription.endDate > Date.now()) {
```

**Good:**
```typescript
const isAdult = user.age >= 18;
const hasActiveSubscription = user.subscription?.endDate > Date.now();

if (isAdult && hasActiveSubscription) {
```

## Documentation vs Comments

- **Comments**: In-code explanations (minimize)
- **Documentation**: External docs, README, API docs (encouraged)
- Use proper documentation tools (JSDoc, docstrings) only when creating public APIs or libraries

## Summary
Write code so clear that comments are unnecessary. If you feel the need to comment, first try to refactor.
