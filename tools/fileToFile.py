import os
import pandas as pd


# folder_path: 文件夹路径, filetype:文件类型 默认为txt
def transTxtToCsv(folder_path, filetype='txt'):
    # 如果文件夹中没有子文件夹的时候直接使用推导式来生产txt文件的list
    txt_file_list = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if
                     os.path.join(folder_path, file).endswith('.' + filetype)]

    for txt_file in txt_file_list:
        data_txt = pd.read_csv(txt_file, sep='\\s+')  # 按字符串切割
        data_txt_df = pd.DataFrame(data_txt)
        save_file_name = txt_file.replace(".txt", ".csv")
        data_txt_df.to_csv(save_file_name, index=False, sep=",", mode='w')  # 写入csv，以','分割


def transCsvToTxt(folder_path, filetype='csv'):
    # 如果文件夹中没有子文件夹的时候直接使用推导式来生产txt文件的list
    txt_file_list = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if
                     os.path.join(folder_path, file).endswith('.' + filetype)]

    for txt_file in txt_file_list:
        data_txt = pd.read_csv(txt_file, sep=',')  # 按,切割

        data_txt_df = pd.DataFrame(data_txt)

        save_file_name = txt_file.replace(".csv", ".txt")
        data_txt_df.to_csv(save_file_name, index=False, sep=" ", mode='w')  # 写入csv，以' '分割


if __name__ == '__main__':
    root_path = r'D:/developingHome/'
    filetype1 = '.txt'  # .txt  .csv
    transTxtToCsv(root_path, filetype1)
    filetype2 = '.csv'
    transCsvToTxt(root_path, filetype2)
