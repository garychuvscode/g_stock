'''
this file builds up the example code for pandas, and knowing how to use pandas well for the
data analysis and collection, output the sorted object or file

230409: fix the stock data path with below:
'c:\\py_gary\\stock_data\\'

'''

import pandas as pd


class data_obj ():

    def __init__(self, data_title_0, date0=0, stock_num0=0, stock_name0=''):
        '''
        data_obj for testing, data_title can input the description of this object
        this is the initialization part of data object
        '''

        # sim_obj = 0 => in simuation mode, test_out_index != 0, output file will be record
        self.sim_obj = 1

        self.data_title = data_title_0
        print(f'data object {self.data_title} is generated')

        # assign the default parameter in the initialization of object
        '''
        path - trace with file name (full path)
        trace - trace with only to folder
        => input and output can be separate, now is set to the same
        '''
        self.path_read_full = ''
        self.path_save_full = ''
        self.read_file_name = ''
        self.save_file_name = 'save_temp_default'
        # this is the default path (not full trace)
        self.trace_default = 'c:\\py_gary\\stock_data\\'
        self.trace_read = self.trace_default
        self.trace_save = self.trace_default

        # define the default format for related object
        self.format = '.csv'

        # parameter must have in class
        self.main_data_frame = 0
        self.stock_number = stock_num0
        self.stock_name = stock_name0
        self.processing_date = date0

        # file output testing parameter, assign by each point
        self.test_out_index = 0

        pass

    def import_csv(self, file_name0, trace0=''):
        '''
        file_name0: don't contain the type, just name
        this function can open the csv file into panadas, enter the trace refer to below form
        1. 'c:\\py_gary\\stock_data\\' => trace is the trace before file name
        2. the next will be the file name
        3. last one will be the '.csv' to give the full file name

        '''

        self.read_file_name = file_name0

        if trace0 != '':
            # change the trace if the trace is not default trace
            self.path_read_full = str(
                trace0) + str(self.read_file_name) + str(self.format)
            self.trace_read = trace0
        else:
            # add the default trace
            self.path_read_full = self.trace_default + \
                str(self.read_file_name) + str(self.format)

        self.main_data_frame = pd.read_csv(
            self.path_read_full, delimiter=',', encoding='big5', skiprows=2)
        # to prevent error, need to skip the row not contain data (title)

        print(self.main_data_frame.head(7))

        return self.main_data_frame

    def two_column_to_one(self):
        '''
        this function turn the two column data to one column
        input the raw data frame and output 1 column data frame
        if no data frame input, use the data frame in this object as default
        '''

        # 230409 not to change data frame when not at input, prevent logic error
        # if pd_data_frame0 == 0:
        #     df_raw = self.main_data_frame
        # else:
        #     # re-new the basic data frame and used as target
        #     self.main_data_frame = pd_data_frame0
        #     print('data fram had been change by two column function')
        #     df_raw = pd_data_frame0

        df_raw = self.main_data_frame

        # check the assigned df
        print(df_raw)

        # separate the first and second column
        df_raw1 = df_raw.iloc[:, :5]
        df_raw2 = df_raw.iloc[:, 6:]
        # refer to pandas function
        print(df_raw1)
        print(df_raw2)

        # re-name the items for df_raw2
        df_raw2.rename(columns={'序號.1': '序號', '券商.1': '券商', '價格.1': '價格',
                       '買進股數.1': '買進股數', '賣出股數.1': '賣出股數'}, inplace=True)
        print(df_raw2)
        df_raw3 = pd.concat([df_raw1, df_raw2], ignore_index=True)
        # combine two column to one column
        print(df_raw3)
        self.obj_to_file(out_file_name0='out_set',
                         test_out_index0=1, test_df=df_raw3)
        df_raw3.dropna(axis=0, inplace=True)
        print(df_raw3)
        self.obj_to_file(out_file_name0='out_set',
                         test_out_index0=2, test_df=df_raw3)
        df_raw3.sort_values(by=["序號"], ascending=True,
                            inplace=True, ignore_index=True)
        df_raw3['序號'] = df_raw3['序號'].astype('uint32')
        # uint32 => used 32bit integer, 因為交易比數會太多
        print(df_raw3)
        self.obj_to_file(out_file_name0='out_set',
                         test_out_index0=3, test_df=df_raw3)
        df_raw3.insert(0, "日期", self.processing_date)
        df_raw3.insert(1, "證券代號", self.stock_number)
        df_raw3.insert(1, "證券名稱", self.stock_name)

        # file output will be at another function
        # df_raw3.to_csv(outputfilename, index=False, compression="gzip")
        # df_raw3.to_csv(outputfilename, index=False, compression=None)

        self.main_data_frame = df_raw3

        return df_raw3

    def obj_to_file(self, out_file_name0, trace0='', index0=False, compression0=None, test_out_index0=0, test_df=0):
        '''
        this function transfer the data frame to output file
        > index default set to faulse, so there are no extra index in column 1
        > compression will be option, refer to the panadas, to_csv function for detail
        > test_out_index used to check output file status
        > test_ef is the related data frame save during testing, set to 0 and will save the main
        '''
        # this few lines just for test_df to become data frame variable
        a = 0
        if a == 1:
            test_df = self.main_data_frame

        # for real mode output file
        out_df_buffer = self.main_data_frame

        if test_out_index0 == 0:
            # update file name and record to object
            self.save_file_name = out_file_name0

            if trace0 != '':
                # change the trace if the trace is not default trace
                self.trace_save = trace0
                self.path_save_full = str(
                    self.trace_save) + str(self.save_file_name) + str(self.format)
            else:
                # add the default trace
                self.path_save_full = self.trace_default + \
                    str(self.save_file_name) + str(self.format)

            self.main_data_frame.to_csv(
                self.path_save_full, index=index0, compression=compression0)

            pass

        elif self.sim_obj == 0 and test_out_index0 != 0:
            # run the test mode saving
            # update file name and record to object for test mode
            self.test_out_index = test_out_index0
            self.save_file_name = 't_' + out_file_name0 + \
                '_t_' + str(self.test_out_index)

            if trace0 != '':
                # change the trace if the trace is not default trace
                self.trace_save = trace0
                self.path_save_full = str(
                    self.trace_save) + str(self.save_file_name) + str(self.format)
            else:
                # add the default trace
                self.path_save_full = self.trace_default + \
                    str(self.save_file_name) + str(self.format)

            out_df_buffer = test_df
            out_df_buffer.to_csv(
                self.path_save_full, index=index0, compression=compression0)

            # self.main_data_frame.to_csv(
            #     self.path_save_full, index=index0, compression=compression0)

            pass

        else:
            # when sim_obj == 1 , bypass all the testing result saving command
            # (case with test_out_index != 0)

            pass

        pass

    '''
    230414 plan:
    1. plan to separate different node data and change to single file or sheet for each node
    2. add the algorithm of filter the good node
    brief: calculated the average price of all the stock in this node, and lower the price is
    is better the operation this node is doing
    3. plan to record the
    '''

    def sort_by_index():

        pass


if __name__ == '__main__':
    #  the testing code for this file object

    test_index = 0

    data_1712 = data_obj(data_title_0='stock_1712',
                         date0='230104', stock_num0='1712', stock_name0='hsin')

    if test_index == 0:

        '''
        to run the testing process make file format ready for sorting
        two column to 1 and generate the new file

        next step is to add result of new file to a summary file
        '''

        # set to simulation mode and record each check point file
        data_1712.sim_obj = 0

        a = data_1712.import_csv('1712_230406')
        data_1712.two_column_to_one()
        data_1712.obj_to_file(out_file_name0='temp')

    pass
