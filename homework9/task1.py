from task2 import Employee


class Company:
    """A class which representing the company."""

    def __init__(self, name, industry, best_company_products, country, number_employees, net_profit):
        """Initialize a Company object.

        Args:
            name (str): The name of the company.
            industry (str): The industry the company operates in.
            best_company_products (list): The main products manufactured by the company.
            country (str): The country where the company is established
            number_employees (int): The number of employees
            net_profit (int): The net income from the sale of products in the company during the last year, Euro
        """
        self.__name = name
        self.__industry = industry
        self.__best_company_products = best_company_products
        self.__country = country
        self.__number_employees = number_employees
        self.__net_profit = net_profit

    @property
    def name(self):
        """str: Get the name of the company."""
        return self.__name

    @name.setter
    def name(self, new_name):
        """Set the name of the company.

        Args:
            new_name (str): The new name value.
        """
        if isinstance(new_name, str) and len(new_name) < 15:
            self.__name = new_name
        else:
            raise TypeError(f'Name should be a string of length less than 20 {type(new_name)} : {len(new_name)}')

    @property
    def industry(self):
        """str: Get the industry the company operates in."""
        return self.__industry

    @industry.setter
    def industry(self, new_industry):
        """Set the industry of the company.

        Args:
            new_industry (str): The new industry value.
        """
        if isinstance(new_industry, str) and len(new_industry) < 40:
            self.__industry = new_industry
        else:
            raise TypeError(
                f'Industry should be a string of length less than 40 {type(new_industry)} : {len(new_industry)}')

    @property
    def best_company_products(self):
        """str: Get the company_products manufactured by the company."""
        return self.__best_company_products

    def add_new_product(self, *args: str):
        """Add new best company products of the company.

        Args:
        best_company_products (str): The new model of the best product.
        """
        for arg in args:
            if arg not in self.__best_company_products:
                self.__best_company_products.append(arg)

    @property
    def country(self):
        """str: Get the country where the company was found."""
        return self.__country

    @country.setter
    def country(self, new_country):
        """Set the country of the company.

        Args:
            new_country (str): The new country value.
        """
        if isinstance(new_country, str) and len(new_country) < 15:
            self.__country = new_country
        else:
            raise TypeError(
                f'Location should be a string of length less than 15 {type(new_country)} : {len(new_country)}')

    @property
    def number_employees(self):
        """int: Get the count of the employees of the company."""
        return self.__number_employees

    @number_employees.setter
    def number_employees(self, new_employees):
        """Set the count of the employees of the company.

        Args:
            new_employees (int): The new employees of the company.
        """
        if isinstance(new_employees, int):
            self.__number_employees = new_employees
        else:
            raise TypeError(f'Number of the employees should be an integer {type(new_employees)}')

    @property
    def net_profit(self):
        """int: Get the count of the employees of the company."""
        return self.__net_profit

    @net_profit.setter
    def net_profit(self, new_net_profit):
        """Set the net profit of the company.

        Args:
            new_net_profit (int): The net profit of last year.
        """
        if isinstance(new_net_profit, int):
            self.__net_profit = new_net_profit
        else:
            raise TypeError(f'Net profit should be an int')

    def get_info(self):
        """Get information about the company.

        Returns:
            str: A string containing information about the company.
        """
        return f'Company Name: {self.__name}. Industry: {self.__industry}. ' \
               f'The country where the company is established: {self.__country}. ' \
               f'Number of the employees: {self.__number_employees}. ' \
               f'The best products manufactured by the company: {self.__best_company_products}. ' \
               f'The net income from the sale of products of the last year is {self.__net_profit} Euro. '

    @staticmethod
    def classified_by_net_profit(net_profit):
        """Check if the company is considered a large company based on the net income from the sale of products.

        Args:
        net_profit (int): The net income from the sale of products in the company.

        Returns:
        bool: True if the company is considered large, False otherwise.
        """
        large_company = 50000000
        return net_profit >= large_company

    @classmethod
    def create_from_dict(cls, company_dict):
        """Create a Company object from a dictionary.

        Args:
            company_dict (dict): A dictionary containing company information.

        Returns:
            Company: A Company object created from the dictionary.
        """
        name = company_dict.get('name')
        industry = company_dict.get('industry')
        best_company_products = company_dict.get('best_company_products')
        country = company_dict.get('country')
        number_employees = company_dict.get('number_employees')
        net_profit = company_dict.get('net_profit')
        return cls(name, industry, best_company_products, country, number_employees, net_profit)


if __name__ == '__main__':
    # task 1
    the_company = Company('Samsung', 'Conglomerate', ['Samsung Galaxy Fold', 'Samsung S23 Ultra'],
                          'South Korea', 1000000, 5000000000)
    the_company.add_new_product('Samsung Galaxy Flip', 'Samsung Galaxy Watch 3 Titanium')
    company_info = the_company.get_info()
    print(company_info)
    if Company.classified_by_net_profit(the_company.net_profit):
        print(f'{the_company.name} is a large company!')
    else:
        print(f'{the_company.name} is not a large company!')

    my_company_dict = {
        'name': 'Select',
        'industry': 'Education',
        'best_company_products': ['Course of Agile Methodology'],
        'country': 'Ukraine',
        'number_employees': 800,
        'net_profit': 500000
    }

    my_company = Company.create_from_dict(my_company_dict)
    my_company.add_new_product('Go programming', 'English PRO')
    if Company.classified_by_net_profit(my_company.net_profit):
        print(f'{my_company.name} is a large company!')
    else:
        print(f'{my_company.name} is not a large company!')
    company_info_by_dict = my_company.get_info()
    print(company_info_by_dict)

    # task 2
    new_employee = Employee('Oleksiy Low', 25, 'Junior Java Developer', 1300)
    Employee.is_min_salary(new_employee.salary)
    check_salary_info = new_employee.get_info()
    print(check_salary_info)
    new_employee_increase = Employee.create_salary_increase('Oleksiy Low', 25, 'Junior Java Developer', 1300, 1100)
    check_creating_info = new_employee_increase.get_info()
    print(check_creating_info)
