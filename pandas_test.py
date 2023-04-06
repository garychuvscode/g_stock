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

        self.trace = ''

        pass

    def import_csv(self, file_name0, trace0=''):
        '''
        this function can open the csv file into panadas, enter the trace refer to below form

        '''
        if trace0 != '':
            # change the trace if the trace is not default trace
            self.trace = trace0

        data_frame0 = pd.read_csv(self.trace)
        self.data_frame = data_frame0
        print(self.data_frame.head(7))

        return self.data_frame


if __name__ == '__main__':
    #  the testing code for this file object

    data_1712 = data_obj('stock_1712')
    data_1712.import_csv()

    pass
