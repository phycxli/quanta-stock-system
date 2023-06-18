import pandas as pd

class cal_factors:
    def __init__(self,stock_file_path) -> None:
        self.stock_file_path = stock_file_path
    
    def pre_read(self):
        df = pd.read_csv(self.stock_file_path,encoding='gbk',skiprows=1)
        return df


class select_stock:
    def __init__(self,select_num:int,hold_period:int) -> None:
        '''
        :param select_num: 选股数量
        "param hold_period: 持仓周期
        '''
        self.select_num = select_num
        self.hold_period = hold_period
    