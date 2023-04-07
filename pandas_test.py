'''
this file builds up the example code for pandas, and knowing how to use pandas well for the
data analysis and collection
'''

import pandas as pd


class data_obj ():

    def __init__(self, data_title_0):
        '''
        data_obj for testing, data_title can input the description of this object
        this is the initialization part of data object
        '''

        self.data_title = data_title_0
        print(f'data object {self.data_title} is generated')

        # assign the default parameter in the initialization of object (trace_f is the full trace)
        self.trace_f = ''
        self.file_name = ''
        # this is the default path (not full trace)
        self.trace_df = 'c:\\py_gary\\stock_data\\'
        # define the default format for related object
        self.format = '.csv'

        pass

    def import_csv(self, file_name0, trace0=''):
        '''
        this function can open the csv file into panadas, enter the trace refer to below form
        1. 'c:\\py_gary\\stock_data\\' => trace is the trace before file name
        2. the next will be the file name
        3. last one will be the '.csv' to give the full file name

        '''

        self.file_name = file_name0

        # add the default trace
        # self.trace_f = 'c:\\py_gary\\stock_data\\' + str(file_name0) + '.csv'
        self.trace_f = self.trace_df + str(self.file_name) + str(self.format)

        if trace0 != '':
            # change the trace if the trace is not default trace
            self.trace_f = str(trace0) + str(self.file_name) + str(self.format)

        data_frame0 = pd.read_csv(
            self.trace_f, delimiter=',', encoding='big5', skiprows=2)
        self.data_frame = data_frame0
        print(self.data_frame.head(7))

        return self.data_frame


if __name__ == '__main__':
    #  the testing code for this file object

    data_1712 = data_obj('stock_1712')
    a = data_1712.import_csv('1712_230406')

    pass
