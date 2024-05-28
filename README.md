# CI/CD Example

## Python Files

### __init__.py
- **Purpose**: Initializes the package and defines what is available for import from the package.
- **Contents**:
  - Specifies that `Person` is the only class available for import from the package.
  - Imports the `Person` class from the `person` module.

### person.py
- **Purpose**: Defines the `Person` class, which models a person with a name, age, and jobs.
- **Class**: `Person`
  - **Attributes**:
    - `name`: The full name of the person (string).
    - `age`: The age of the person (integer).
    - `jobs`: A list of job titles the person has (optional, collection of strings).
  - **Methods**:
    - `__init__(self, name: str, age: int, *, jobs: Optional[Collection[str]] = None)`: Initializes a new `Person` object.
    - `forename(self) -> str`: Returns the first name of the person.
    - `surname(self) -> Optional[str]`: Returns the last name of the person if available, otherwise returns `None`.
    - `celebrate_birthday(self) -> None`: Increments the age of the person by one year.
    - `add_job(self, title: str) -> None`: Adds a job title to the person's job list.

### test_person.py
- **Purpose**: Contains unit tests for the `Person` class to ensure its methods and properties work correctly.
- **Framework**: `unittest`
- **Tests**:
  - `test_init(self)`: Tests the initialization of a `Person` object.
  - `test_forename(self)`: Tests the `forename` property.
  - `test_surname(self)`: Tests the `surname` property.
  - `test_celebrate_birthday(self)`: Tests the `celebrate_birthday` method.
  - `test_add_job(self)`: Tests the `add_job` method.
- **Setup**:
  - Adds the parent directory to the `sys.path` to ensure the `Person` class can be imported.

## Configuration

### main.yml
- **Purpose**: Configuration file for continuous integration (CI) using GitHub Actions.
- **Note**: This file is not accessible, but typically contains workflows for running tests and other CI/CD tasks.
