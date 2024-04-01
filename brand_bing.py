'''
@create : lisa
@file :security_code
@Date :2024/3/6
@desc :
'''
from get_security_code import bind_security_code
import os

def main():
    folder_path = input("请选择防伪码的测试环境 (输入 1 为 test 环境, 输入 2 为 beta 环境): ")
    if folder_path == "1":
        folder_path = "data_test"
    elif folder_path == "2":
        folder_path = "data_beta"
    else:
        print("无效输入，退出...")
        return

    #品牌站枚举
    brands = ['elfbar','lostmary','ELFLIQ','FunkyRepublic','EBDesign','EBCREATE','FUNKY_LANDS','HIDESEEK','RabBeatsVape','LOSTY_LOSTY','MAD_EYES','OFF_STAMP','URBAN_TALE','LOSGAL','MARYLIQ']
    print("品牌编号（1-15）:")
    for i, brand in enumerate(brands, 1):
        print(f"{i}. {brand}", end='\t')
        if i % 5 == 0:  # 每打印5个品牌换行
            print()

    brand_selection = input("请选择需要创建防伪码的品牌编号: ")
    if not brand_selection.isdigit() or int(brand_selection) < 1 or int(brand_selection) > 15:
        print("无效输入，退出...")
        return
    brand_selection = int(brand_selection) - 1
    brand_name = brands[brand_selection]
    print(f"您选择了 {brand_name}")
    try:
        secuirty_code_out_files = os.path.join(folder_path,brand_name+'_secuirty_code_out.txt')  # 输出文件路径
        # 调用绑定防伪码方法之前清空OUT TXT
        with open(secuirty_code_out_files, 'w'):
            pass
        # HS数据库防伪码ID枚举
        HS_security_id = [17641, 17642, 17643, 17644, 17645]
        # HS数据库防伪码ID数量
        num = len(HS_security_id)
        # 调用绑定防伪码方法
        bind_security_code(folder_path, brand_name, HS_security_id, num)
        print("绑定防伪码完成")
    except:
        print("文件路径不存在，退出...")
        return



if __name__ == '__main__':
    main()
