import pandas as pd


# 按某些列名分组，计算某一列的数量

def data_maxByGroup(folder_path, max_file_name, cal_name, group_by_name):
    # 读取CSV文件并包含表头
    df = pd.read_csv(folder_path)  # 编码默认UTF-8，若乱码自行更改
    print(df)
    # group_by_name = [df.columns[i] for i in range(group_by_num)]  # 按哪几列分组排序 进行计算
    group_by_name = [df[i] for i in group_by_name]

    df_max = df[df.groupby(group_by_name)[cal_name].rank(method="first", ascending=False) == 1]  # 求每组最大cal_name的值

    df_max.to_csv(max_file_name, encoding="utf_8_sig", index=False, mode='w')


if __name__ == '__main__':
    root_path = r'D:\developingHome'
    read_file_name = r'\sample.csv'
    folder_path = root_path + read_file_name

    sum_column_name = "count"  # 要计算的列名

    group_by_name = ["session_id", "item_id"]  # 指定的列名
    max_file_name = root_path + r'\max.csv'  # 计算后的文件名

    data_maxByGroup(folder_path, max_file_name, sum_column_name, group_by_name)
