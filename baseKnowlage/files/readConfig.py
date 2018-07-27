#coding:utf-8
#主要是介绍利用configparser读取与修改ini文件

import configparser

#读
with open("../../config.ini","r") as cfgIni:
    config = configparser.ConfigParser()
    config.read_file(cfgIni)
    name = config.get("info","name")
    print(name)


#写（新建）
with open("../../config.ini","w") as cfgIni2:
    config = configparser.ConfigParser()
    config.add_section("info")
    config.set("info","age","28")
    cfgIni.close()
    print(config.get("info","age")) #此时还是在缓存中
    config.write(cfgIni2) #写入文件

#修改(添加)
config = configparser.ConfigParser()
config.read("../../config.ini")
config.set("info","name","uncle")
config.set("info","sex","male")
config.add_section("newSection")
config.set("newSection","value","test new section")
config.add_section("deletion")
config.set("deletion","deleItems","delecontent")
fp = open("../../config.ini","w+") #r+,w,w+
config.write(fp)
fp.close()

#删除
config.read("../../config.ini")
config.remove_option("deletion","deleItems")
config.remove_section("deletion")











