# Codegen Solutions Repository

Welcome to the **Codegen Solutions** repository! This repository provides example solutions to common problems in software development, such as framework migrations, codebase restructures, and more. Each solution is designed to offer a comprehensive guide for developers interested in using Codegen to quickly solve the problem at-hand.

## Overview

This repository offers a series of solution folders that each contain:
- A **canonical starting repository** for a problem (e.g., a codebase set up with SQLAlchemy 1.6).
- A **step-by-step guide** to apply the solution (e.g., instructions for migrating from SQLAlchemy 1.6 to 2.0).
- An **example resulting repository**, showing the canonical starting repo with the solution applied.

These solutions are structured to be practical, actionable, and easy to follow for engineers dealing with similar issues.

## Structure

Each solution is located in a dedicated folder within the `solutions` directory. The structure for each solution is as follows:
```
solutions/
│
└── [Solution Name]/
    ├── starting-repo/         # Canonical starting repository for this solution
    ├── guide.md               # Step-by-step guide for applying the solution
    └── resulting-repo/        # Example resulting repository after solution is applied
```

### Example

For a solution such as "Migrate SQLAlchemy 1.6 to 2.0," the structure might look like this:
```
solutions/
│
└── migrate-sqlalchemy-1.6-to-2.0/
    ├── starting-repo/
    ├── guide.md
    └── resulting-repo/
```
Each solution’s guide provides context, requirements, and detailed steps to take a developer from the starting repo state to the fully migrated or updated state.
