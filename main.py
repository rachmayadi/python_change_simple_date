# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pandas as pd


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def load_data(file_input=None):
    dataframe_vals = pd.read_csv(file_input)
    if dataframe_vals:
        print('load done')
        return dataframe_vals


def change_date_format(df_input=None):
    changed_dataframe = False
    return changed_dataframe


def write_dataframe_to_csv(df_input=None,
                           csv_filename=None):
    return True


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    dataframe_vals = load_data(file_input="sales_records.csv")
    changed_dataframe = change_date_format(df_input=dataframe_vals)
    write_result = write_dataframe_to_csv(df_input=changed_dataframe,
                                          csv_filename="changed_sales_records.csv")
    if write_result:
        print('done')
    else:
        print('failed')
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
