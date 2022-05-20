"""
NO FUNCTIONS SHOULD BE ADDED OR REMOVED FROM THIS MODULE. SIMPLY COMPLETE EACH FUNCTION AS DESCRIBED.
YOU SHOULD ALSO NOT REMOVE ANY OF THE COMMENTS OR CHANGE THE STRUCTURE IN ANY WAY OTHER THAN AS INSTRUCTED.

This module is responsible for setting up and querying the database.
"""
import sqlite3
import tui

def execute(action, headings, records):
    """
    Task 22: Execute database action.

    The function should check the value of action (which is the database menu option specified by the user)
    and execute the relevant database function.
    For example,
        If action is 1 then the function should invoke the setup_database function.
        If action is 2 then the function should invoke the retrieve_customers_alphabetically function.

    In each case, with the exception of the setup_database function, the result of executing relevant database function
    should be displayed using the appropriate tui function.
    For example,
        The result of executing the retrieve_customers_alphabetically function should be displayed using the tui
        display_records function.

    If the action is invalid then the error message 'Invalid selection.' should be displayed using the tui error
    function.

    :param action: An integer indicating which action (database option) to perform.
    :param headings: A list of headings for the records.
    :param records: A list of records.
    :return: Does not return anything.
    """
    # TODO: Your code here (replace this TODO and remove the keyword pass)
    pass


def setup_database(headings, records):
    """
    Task 23: Create a database and populate it.

    The function should create a database named 'sales.db' stored in the 'data' folder with a single table
    named 'records'.
    The function should populate the database using the records passed as a parameter.

    For higher marks (advance task):
        - Normalise the database into 2 or more tables.
    """
    # TODO: Your code here (replace this TODO and remove the keyword pass)
    pass


def retrieve_customers_alphabetically():
    """
    Task 24: Retrieve customers sorted alphabetically.

    The function should query the database to retrieve all customer names sorted alphabetically
    by first name and then last name.
    The function should return the results.

    :param headings: A list of headings for the records.
    :param records: A list of records.
    :return A list or tuple containing the records retrieved from the database.
    """
    # TODO: Your code here (replace this TODO and remove the keyword pass)
    pass


def retrieve_total_product_sales():
    """
    Task 25: Retrieve the total product sales.

    The function should query the database to retrieve the total sales for each product.
    The function should sort the results by the product name in alphabetical and ascending order.
    The function should return the results.

    :param headings: A list of headings for the records.
    :param records: A list of records.
    :return: A list or tuple containing the records retrieved from the database.
    """
    # TODO: Your code here (replace this TODO and remove the keyword pass)
    pass


def retrieve_top_product_categories():
    """
    Task 26: Retrieve the top 3 product categories.

    The function should query the database to retrieve the top 3 product categories.
    The top 3 product categories are the categories of products that result in the highest profits.
    The results should include the name of the category and the amount of profit.

    :param headings: A list of headings for the records.
    :param records: A list of records.
    :return: A list or tuple containing the records retrieved from the database.
    """
    # TODO: Your code here (replace this TODO and remove the keyword pass)
    pass


def retrieve_top_product_subcategories():
    """
    Task 27: Retrieve the top 3 product sub-categories.

    The function should query the database to retrieve the top 3 product sub-categories for specific dates.
    The dates will be specified by the user.
    The top 3 product sub-categories are those that have the highest sales on the specified dates.
    The results should include the name of each sub-category and the amount of sales for each sub-category.

    :param headings: A list of headings for the records.
    :param records: A list of records.
    :return: A dictionary where the keys are the dates and the values are the top 3 product sub-categories (with
    the name and the sales for each sub-category) for that date.
    """
    # TODO: Your code here (replace this TODO and remove the keyword pass)
    pass
