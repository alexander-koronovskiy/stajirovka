import pandas as pd


def solution():
    a = pd.read_csv('in_data_a.csv')
    p = pd.read_csv('in_data_p.csv')
    pp = p.drop(columns=['campaign'])\
        .groupby(['date', 'ad_id'])\
        .sum()
    aa = a.rename(columns={'Date':'date'})\
        .drop(columns = ['id'])\
        .set_index(['date','ad_id'])
    res = aa.join(pp, how='inner')\
        .reset_index()\
        .drop(columns = ['ad_id'])\
        .groupby(['Campaign', 'app', 'os', 'date'])\
        .sum()

    # В задании не указано, что делать в случае, когда
    # количество установок равно 0, поэтому оставим
    # значения cpi равные inf и Nan нетронутыми
    res['cpi'] = res['spend'] / res['Installs']

    res.to_csv('out.csv')


if __name__ == "__main__":
    solution()
