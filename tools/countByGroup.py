import pandas as pd


# 按某些列名分组，计算某一列的数量
# folder_path:文件路径，count_file_name：计算完保存的文件路径，count_name：计算个数的列，
# sum_column_name：计算的值存放的列，group_by_name：按哪些列进行分组
def data_count(read_file_name, count_file_name, count_name, reset_name, group_by_name):
    # 读取CSV文件并包含表头
    df = pd.read_csv(read_file_name)  # 编码默认UTF-8，若乱码自行更改
    print(df)
    # group_by_name = [df.columns[i] for i in range(group_by_num)]  # 按哪几列分组排序 进行计算
    print(group_by_name)
    group_by_name = [df[i] for i in group_by_name]
    # 分组对count_name计数，并将结果返回到sum_column_name列
    df_count = df.groupby(group_by_name)[count_name].count().reset_index(name=sum_column_name)
    df_count.to_csv(count_file_name, encoding="utf_8_sig", index=False, mode='w')


if __name__ == '__main__':
    root_path = r'D:\developingHome'
    read_file_name = r'\sample.csv'
    folder_path = root_path + read_file_name

    count_name = "count1"  # 要计算的列名
    reset_name = "count2"

    group_by_name = ["session_id", "item_id"]  # 指定的列名
    count_file_name = root_path + r'\count.csv'  # 计算后的文件名

    data_count(folder_path, count_file_name, count_name, reset_name, group_by_name)
