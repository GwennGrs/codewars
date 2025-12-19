![Coverage](./coverage.svg)

# Python/Codewars Project

This project is part of the required assignments for the **Computer Science Refresher** course.

### Content
* A collection of **10 Python files** solving algorithmic challenges of varying difficulty levels.
* All problems are sourced from [Codewars](https://www.codewars.com/).

### Features
* **Documentation**: Each solution is documented and includes a direct link to the associated Codewars challenge.
* **Automated Testing**: Comprehensive unit testing using **Pytest**. A **Coverage badge** is automatically shown in the readme by a GitHub Action.
* **Dependency**: **Poetry** allow an efficient dependencies management and quick project installation.
* **Code Quality Control**: Guaranteed **Pylint score of 10/10**. Github action will give and error message for score bellow **7.5**.

### Local Installation

**1/ Clone the repository:**
```bash
git clone git@github.com:GwennGrs/codewars.git
cd codewars
```

**2/ Install dependencies**
```bash
poetry install
```

**2/ Run unit tests and check pylint score**
```bash
poetry install
poetry run pylint src/codewars
```