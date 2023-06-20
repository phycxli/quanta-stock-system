import tushare as ts
from update_config import *
from datetime import *
from joblib import Parallel, delayed

# 建立tushare的链接
pro = ts.pro_api(tushare_api)

class update_data:
    def __init__(self,ts_code="",trade_date="",start_time="",end_time="",limit="") -> None:
        self.ts_code = ts_code
        self.trade_date = trade_date
        self.start_time = start_time
        self.end_time = end_time
        self.limit = limit

    def get_ts_code(self):
        '''
        获取当日市场上所有股票的代码
        '''
        df = pro.stock_basic(**{"ts_code": "","name": "","exchange": "","market": "","is_hs": "","list_status": "","limit": "","offset": ""}, fields=["ts_code","symbol","name","area","industry","market","list_date","fullname","enname","cnspell","exchange","curr_type","list_status","delist_date","is_hs"])
        code_list = df['ts_code'].to_list()
        return code_list
    
    def get_rename_data(self,code):
        '''
        获取股票更名数据
        :param code: 股票代码，ts格式，xxxxxx.SZ/SH/BJ
        '''
        df_name = pro.namechange(**{
            "ts_code": code,
            "start_date": "",
            "end_date": "",
            "limit": "",
            "offset": ""
        }, fields=[
            "ts_code",
            "name",
            "start_date",
            "end_date",
            "ann_date",
            "change_reason"
        ])
        return df_name
    
    def get_money_flow_data(self,code):
        '''
        获取股票资金流数据
        :param code: 股票代码，ts格式，xxxxxx.SZ/SH/BJ
        '''
        df_money = pro.moneyflow(**{
            "ts_code": code,
            "trade_date": "",
            "start_date": "",
            "end_date": "",
            "limit": "",
            "offset": ""
        }, fields=[
            "trade_date",
            "buy_sm_vol",
            "buy_sm_amount",
            "sell_sm_vol",
            "sell_sm_amount",
            "buy_md_vol",
            "buy_md_amount",
            "sell_md_vol",
            "sell_md_amount",
            "buy_lg_vol",
            "buy_lg_amount",
            "sell_lg_vol",
            "sell_lg_amount",
            "buy_elg_vol",
            "buy_elg_amount",
            "sell_elg_vol",
            "sell_elg_amount",
            "net_mf_vol",
            "net_mf_amount",
            "trade_count"
        ])
        return df_money

    def get_daily_data(self,ts_code,start_dates):
        '''
        获取日线数据
        :param" ts_code: 股票代码(Tushare格式，xxxxxxx.SH/SZ/BJ)
        :param start_dates: 获取日线行情的数据的起始日期
        :return: 返回当前这支股票的历史日线数据
        '''
        df = pro.daily(self.data_type)(**{
            "ts_code": ts_code,
            "trade_date": self.trade_date,
            "start_date": start_dates,
            "end_date": "",
            "offset": "",
            "limit": self.limit
        }, fields=[
            "ts_code",
            "trade_date",
            "open",
            "high",
            "low",
            "close",
            "pre_close",
            "change",
            "pct_chg",
            "vol",
            "amount"
        ])
        return df
    
    def history_daily_data(self):
        code_list = update_data.get_ts_code()
        return code_list
