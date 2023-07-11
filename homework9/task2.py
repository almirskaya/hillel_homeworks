class Employee:
    """A class representing a worker/employee."""

    def __init__(self, name, age, position, salary):
        """Initialize an Employee object.

        Args:
            name (str): The name of the employee.
            age (int): The age of the employee.
            position (str): The position/role of the employee.
            salary (float): The salary of the employee.
        """
        self._name = name
        self._age = age
        self._position = position
        self._salary = salary

    @property
    def name(self):
        """str: Get the name of the employee."""
        return self._name

    @name.setter
    def name(self, new_name):
        """Set the name of the employee.

        Args:
            new_name (str): The new name value.
        """
        if isinstance(new_name, str) and len(new_name) < 30:
            self._name = new_name
        else:
            raise TypeError(f'Name should be a string of length less than 30 {type(new_name)} : {len(new_name)}')

    @property
    def age(self):
        """int: Get the age of the employee."""
        return self._age

    @age.setter
    def age(self, new_age):
        """Set the age of the employee.

        Args:
            new_age (int): The new age value.
        """
        if isinstance(new_age, int) and 18 <= new_age < 50:
            self._age = new_age
        else:
            raise TypeError(f'Age should be a positive integer more than 18 and less than {new_age}')

    @property
    def position(self):
        """str: Get the position of the employee."""
        return self._position

    @position.setter
    def position(self, new_position):
        """Set the position of the employee.

        Args:
            new_position (str): The new position value.
        """
        if isinstance(new_position, str) and len(new_position) < 30:
            self._position = new_position
        else:
            raise TypeError(f'Position value should be a string of length less than : {len(new_position)}')

    @property
    def salary(self):
        """float: Get the salary of the employee."""
        return self._salary

    @salary.setter
    def salary(self, new_salary):
        """Set the salary of the employee.

        Args:
            new_salary (float): The new salary value.
        """
        if isinstance(new_salary, float) or isinstance(new_salary, int):
            self._salary = new_salary
        else:
            raise TypeError(f'Salary value should be a float or int {type(new_salary)}')

    def get_info(self):
        """Get information about the employee.

        Returns:
            str: A string that contains information about the employee.
        """
        return f"Name: {self._name} Age: {self._age} Position: {self._position} Salary: {self._salary}"

    @staticmethod
    def is_min_salary(salary):
        """Check if the given age is considered retirement age.

        Args:
            salary (int): The salary to check.

        Returns:
            str: String that tells if the salary of the employee is minimal or not.
        """
        min_salary = 2400
        increase = min_salary - salary
        if salary > min_salary:
            return print(f'The salary will be {salary} Euro')
        else:
            return print(f'The salary will be increase by {increase} Euro')

    @classmethod
    def create_salary_increase(cls, name, age, position, salary, increase):
        """Initialize an Employee object with increase of salary.

        Args:
            name (str): The name of the employee.
            age (int): The age of the employee.
            position (str): The position/role of the employee.
            salary (float): The salary of the employee.
            increase (float): The increase of the salary of employee.
        """
        salary_with_increase = salary + increase
        return cls(name, age, position, salary_with_increase)
