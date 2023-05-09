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
    bk_holidays = pd.read_excel(comp_dir / 'codebook.xlsx', sheet_name='sheet1')
    bk_oil = pd.read_excel(comp_dir / 'codebook.xlsx', sheet_name='sheet2')
    bk_stores = pd.read_excel(comp_dir / 'codebook.xlsx', sheet_name='sheet3')
    bk_train = pd.read_excel(comp_dir / 'codebook.xlsx', sheet_name='sheet4')
    bk_transactions = pd.read_excel(comp_dir / 'codebook.xlsx', sheet_name='sheet5')

    return train, stores, oil, transactions, holidays_events, bk_holidays, bk_oil, bk_stores, bk_train, bk_transactions


# Date Selection
def date_select(data, col):
    data[col] = pd.to_datetime(data[col])
    data['year'] = data[col].dt.year
    data['month'] = data[col].dt.month
    data['day'] = data[col].dt.day

    new_df = data.loc[data['year'].isin([2015, 2016]), :]
    return new_df