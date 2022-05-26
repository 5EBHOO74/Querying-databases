
"""
NO FUNCTIONS SHOULD BE ADDED OR REMOVED FROM THIS MODULE. SIMPLY COMPLETE EACH FUNCTION AS DESCRIBED.
YOU SHOULD ALSO NOT REMOVE ANY OF THE COMMENTS OR CHANGE THE STRUCTURE IN ANY WAY OTHER THAN AS INSTRUCTED.

This module is responsible for processing the data.
"""
import tui



def execute(action, headings, records):
    """
    Task 17: Execute process action

    The function should check the value of action (which is the process menu option specified by the user)
    and execute the relevant process function.
    For example,
        If action is 1 then the function should invoke the record_by_id function.
        If action is 2 then the function should invoke the records_by_customers function.

    In each case, the result of executing relevant process function should be displayed using the appropriate tui
    function.
    For example,
        The result of executing the record_by_id function should be displayed using the tui display_record function.
        The result of executing the records_by_shipment_mode function should be displayed using the tui display_groups
        function

    If the action is invalid then the error message 'Invalid selection.' should be displayed using the tui error
    function.

    :param action: An integer indicating which action (process option) to perform.
    :param headings: A list of headings for the records.
    :param records: A list of records.
    :return: Does not return anything.
    """
    print(
        """
        Please select one of the following options:
        [1] Record by id
        [2] Record by customers
        [3] Record by shipment mode
        [4] Record by summary
        """)
    action = int(input())
    print(f"You have selection option: {action}")
    if action == 1:
        tui.display_record(record_by_id(headings,records))
    elif action == 2:
        tui.display_records(records_by_customers(headings,records))
    elif action == 3:
        tui.display_groups(records_by_shipment_mode(headings,records))
    elif action == 4:
        tui.display_summary(records_summary(headings, records))
    else:
        tui.error('Invalid selection.')


def record_by_id(headings, records):
    """
    Task 18: Retrieve a record by a record id.

    The function should use the appropriate tui function to retrieve a record id.
    The function should then find the record with a matching record id and return the record.
    The parameter 'records' contains the records that are to be searched.

    For higher marks (advance task):
        - The function should create a list of valid ids. These are ids for which a record exists in the 'records' list.
        - The function should pass the list of valid ids to the tui function when retrieving a record id

    :param headings: A list of headings for the records.
    :param records: A list of records.
    :return: An individual record with the specified record id.
    """

    record_id = tui.record_id()
    val_ids =[]
    for record in records:
        if record_id in record[0]:
            val_ids.append(record_id)
            return record

def records_by_customers(headings, records):
    """
    Task 19: Retrieve records for specified customers.

    The function should use the appropriate function in tui to retrieve a list of customer ids.
    The function should return a list containing records where the customer id matches one of the customer ids
    specified by th user.
    The parameter 'records' contains the list of records that are to be searched.


    :param headings: A list of headings for the records.
    :param records: A list of records.
    :return: A list of records where a record contains a specified customer id.
    """

    cus_ids = tui.customers()
    cus_records = []
    for record in records:
        if cus_ids in record[5]:
            cus_records.append(record)
    return cus_records



def records_by_shipment_mode(headings, records):
    """
    Task 20: Retrieve records grouped by shipment mode.

    The function should return a dictionary where the keys are the different shipment modes and the values are a list
    of records for each shipment mode.

    For example, the key could be 'Standard Class' and the value for this key would be a list of records where
    the shipment mode is 'Standard Class'.

    For higher marks (advance task):
        - The function should retrieve a sample size from the user by invoking the tui sample_size function.
        The default size for the function should be the number of records in (parameter) 'records'.
        - The function should use the sample size to control how many records are added to each group.
        - For example, if the sample size is 5 then only 5 records should be added to each shipment mode group.

    :param headings: A list of headings for the records.
    :param records: A list of records.
    :return: A dictionary with shipment mode as the keys and a list of records for each shipment mode as the values.
    """

    shipment_modes = {}

    standard_class = first_class = second_class = same_day = 0
    for record in records:
        if record[4] == "Standard_Class":
            standard_class.append(record)
        elif record[4] == "First Class":
            first_class.append(record)
        elif record[4] == "Second Class":
            second_class.append(record)
        else:
            same_day.append(record)

    shipment_modes["Standard Class"] = standard_class
    shipment_modes["Second Class"] = second_class
    shipment_modes["First Class"] = first_class
    shipment_modes["Same Day"] = same_day
    return shipment_modes


def records_summary(headings, records):
    """
    Task 21: Retrieve a sales summary for each state.

    The function should return a dictionary where the keys are the states and the values are nested dictionaries
    containing sales, quantity, discount and profit totals.

    The structure of the dictionary should be as follows:
    state: { 'sales': total_sales, 'quantity': total_quantity, 'discount': total_discount, 'profit': total_profit }

    E.g. New York: {'sales': 215336.16, 'quantity': 2935, 'discount': 44.4, 'profit': 50887.75}

    Where total_sales, total_quantity, total_discount and total_profit are the totals for the state.

    For higher marks (advance task):
        - The final totals for sales, quantity, discount and profit for each state should be rounded
        to 2 decimal places.

    :param headings: A list of headings for the records.
    :param records: A list of records.
    :return: A dictionary where the keys are the names of the states and the values are dictionaries containing
    the totals for sales, quantity, discount and profit.
    """
    summary_of_records = {}

    for record in records:
        state = record[10]
        t_sales = record[17]
        qty = record[18]
        disct = record[19]
        prft = record[20]
        if summary_of_records[state]:
            summary_of_records[state] ={"Sales": summary_of_records[state]["sales"] + t_sales,
                                      "Quantity": summary_of_records[state]['quantity'] + qty,
                                      "Discount": summary_of_records[state]["discount"] + disct,
                                      "Profit": summary_of_records[state]["profit"] + prft}
            return summary_of_records
        else:
            print("Cannot find Key")
