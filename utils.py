# -*- coding:utf-8 -*-

import pandas as pd
from pathlib import Path
import streamlit as st

@st.cache_data
def load_data():
    comp_dir = Path('data/store-sales-time-series-forecasting')
    train = pd.read_csv(comp_dir / 'train_sample_201516.csv')
    stores = pd.read_csv(comp_dir / 'stores.csv')
    oil = pd.read_csv(comp_dir / 'oil.csv')
    transactions = pd.read_csv(comp_dir / 'transactions.csv')
    holidays_events = pd.read_csv(comp_dir / 'holidays_events.csv')
    bk_holidays = pd.read_csv(comp_dir / 'cd_holidays.csv')
    bk_oil = pd.read_csv(comp_dir / 'cd_oil.csv')
    bk_stores = pd.read_csv(comp_dir / 'cd_stores.csv')
    bk_train = pd.read_csv(comp_dir / 'cd_train.csv')
    bk_transactions = pd.read_csv(comp_dir / 'cd_transaction.csv')

    return train, stores, oil, transactions, holidays_events, bk_holidays, bk_oil, bk_stores, bk_train, bk_transactions


# Date Selection
def date_select(data, col):
    data[col] = pd.to_datetime(data[col])
    data['year'] = data[col].dt.year
    data['month'] = data[col].dt.month
    data['day'] = data[col].dt.day

    new_df = data.loc[data['year'].isin([2015, 2016]), :]
    return new_df