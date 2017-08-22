import pandas as pd

def disp_uniqueData_inCol(list_of_column_names, df, these_unique_on=True, how_many_unique_on=True, times_appear_on=True, uniqueVal_freq_chart=False):
    """(1) Print the unique values for each column in the list. (Default = ON)
       (2) Print number of unique values in each column. (Default = ON)
       (3) Print the times that each unique value appears. (Default = ON)
       (4) Display a new dataframe with cols 'unique values' and 'frequency'. (Default = OFF)
       * Turn these functions on/off individually by setting 'on' values in function variables equal to True/False
       """
    for column_name in list_of_column_names:
        these_unique = list(df.loc[:, column_name].unique())
        times_appear = list(df.loc[:, column_name].value_counts())
        if these_unique_on:
            print('Unique values in the column', column_name, 'include: \n', these_unique, '\n\n')
        if how_many_unique_on:
            how_many_unique = len(these_unique)
            print('There are ', how_many_unique, 'unique values\n\n')
        if times_appear_on:
            print('Times these unique values appear: \n', times_appear, '\n\n')
        if uniqueVal_freq_chart:
            uniqueVals_freq = pd.DataFrame(
                {'Unique Values': these_unique,
                 'Frequency': times_appear
               }, columns= ['Unique Values', 'Frequency'])
            print(uniqueVals_freq)
