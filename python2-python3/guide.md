# Guide: Migrating from Python 2 to Python 3 with Codegen

This guide walks you through the steps to migrate your codebase from Python 2 to Python 3 using Codegen. Follow along to modernize your print statements, handle Unicode strings, and update dictionary iteration while ensuring compatibility with Python 3. Each step includes a direct link to the appropriate codemod for easy implementation.

---

## 🎉 Overview of Changes

The migration focuses on these key updates:

1. **Convert Print Statements to Function Calls**  
   This codemod converts print statements in Python 2 to function calls in Python 3.  
   [Run the Convert Print Statements to Function Calls Codemod](https://www.codegen.sh/preview/7583)

2. **Unicode to Str Conversion**  
   This codemod updates Unicode string handling to be compatible with Python 3, where all strings are Unicode by default.  
   [Run the Unicode to Str Conversion Codemod](https://www.codegen.sh/preview/7587)

3. **Update Dictionary Iteration**  
   This codemod updates dictionary iteration to use the view objects returned by `dict.keys()`, `dict.values()`, and `dict.items()` in Python 3.  
   [Run the Update Dictionary Iteration Codemod](https://www.codegen.sh/preview/7590)

---

## How to Migrate

### Step 1: Convert Print Statements to Function Calls

Use the codemod to convert print statements in Python 2 to function calls in Python 3.

👉 [Run the Convert Print Statements to Function Calls Codemod](https://www.codegen.sh/preview/7583)

### Step 2: Unicode to Str Conversion

Use the codemod to update Unicode string handling to be compatible with Python 3.

👉 [Run the Unicode to Str Conversion Codemod](https://www.codegen.sh/preview/7587)

### Step 3: Update Dictionary Iteration

Use the codemod to update dictionary iteration to use the view objects returned by `dict.keys()`, `dict.values()`, and `dict.items()` in Python 3.

👉 [Run the Update Dictionary Iteration Codemod](https://www.codegen.sh/preview/7590)

---

## Need Help?

If you encounter issues or have specific edge cases not addressed by the codemods, reach out to the Codegen support team or visit the [Codegen Documentation](https://www.codegen.sh/docs) for detailed guidance.

Start your Python 3 migration today and enjoy the benefits of a cleaner, modern codebase!
