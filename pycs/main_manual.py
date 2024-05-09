#正常不爬源 主程序 txt/new_url.txt + txt/finished.txt
import os

"""给定文件主要格式
	txt/new_url.txt	name,url		#新找到的数据复制到这个文件中
txt/finished.txt	name,url${序号}{地址}{分辨率高度}	#处理完成后的资源
txt/over.txt	name,url		#处理中出现失败的数据
txt/wating.txt	name,url		#处理中可用，但未被选用的数据
txt/rename.txt	new_name,old_name	#频道名称统一目录
txt/catalogue.txt	name,num_catalogueipv,name_catalogueiptv,channel	#频道号目录
txt/address.txt	server,address	#IP地址归属与运行商目录"""
print("注意：如果需要抓取网络资源，请先关闭窗口，待crawling_iptv.py运行完后再运行本程序！"'\n')

print("合并merge	new_rul、finished、crawling_iptv文件合并，删除url中符号$及右边的内容后删除不是name,url格式的行；各行url比对，删除重复行数据，只保留一行，结果以name,url 的格式存入txt/merge.txt。"'\n')
#调用运行merge.py
os.system("python merge.py")

print("检测temp 输出 txt/test.txt,失败项 txt/over.txt"'\n')
os.system("python test.py")

print("txt/test.txt 按url去重，保留height最小值，输出 txt/test_unique.txt"'\n')
os.system("python test_unique.py")

print("时移/回看review 并对大于1080P的增加UHD字样，输出 txt/review.txt"'\n')
os.system("python review.py")

print("提取地址address 输出 txt/address.txt"'\n')
os.system("python address.py")

print("提取频道chanel 输出 txt/chanel.txt,未收藏 txt/waiting.txt"'\n')
os.system("python channel.py")

print("复制 txt/chanel.txt 到txt/channel_finished.txt"'\n')

with open('txt/channel.txt', 'r', encoding='utf-8') as source_file:
    with open('txt/channel_finished.txt', 'w', encoding='utf-8') as destination_file:
        destination_file.write(source_file.read())


print("txt/chanel.txt 文件已备份至txt/channel_finished.txt.")


print("排序sort 输出 txt/sort.txt"'\n')
os.system("python sort.py")


print("输出finished 输出 txt/finished.txt"'\n')
os.system("python finished.py")


print("分别对 txt/over.txt 与 txt/waiting.txt 去重"'\n')
os.system("python unique.py")

print("读取台标图片"'\n')
os.system("python review_finished.py")

input("按回车键退出...")