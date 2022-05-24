import pandas as pd


# 按列 合并两个文件
def merge(input1, input2, index, merge_file):
    df1 = pd.read_csv(input1, encoding='utf-8')
    df2 = pd.read_csv(input2, encoding='utf-8')
    outfile = pd.merge(df1, df2, how='left', on=index)
    outfile.to_csv(merge_file, index=False, encoding='utf-8')
    print("saved")


if __name__ == '__main__':
    folder_path = r'D:\developingHome\\'

    max_file_name = folder_path + r'\max.csv'  # 计算后的文件名
    count_file_name = folder_path + r'\count.csv'  # 计算后的文件名

    group_by_name = ["session_id", "item_id"]  # 指定的列名

    merge_file_name = r'\merge.csv'
    merge_file = folder_path + merge_file_name
    merge(max_file_name, count_file_name, group_by_name, merge_file)
