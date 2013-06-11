#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2013-06-10
# @Author  : Mick Han (catmic27@gmail.com)
# @Link    : http://mickhan.com
# @Version : 0.1
# @Description : 学习日语50音图的小程序
import os
from random import sample


gojuon = [
    ("a", "あ"),
    ("i", "い"),
    ("u", "う"),
    ("e", "え"),
    ("o", "お"),
    ("ka", "か"),
    ("ki", "き"),
    ("ku", "く"),
    ("ke", "け"),
    ("ko", "こ"),
]


def one_item(item, char=True, rome=True, pron=True):
    '''
    输出字型、罗马音和读音，读取命令行输入并判断
    '''
    if char:
        print item[1],
    if rome:
        print item[0]
    if pron:
        os.system("say " + item[1])
    kb = raw_input("> ")
    if kb == item[1]:
        return True
    else:
        return False


def main():
    '''
    step 1: 顺序显示所有平假名/罗马音/读音，在命令行输入正确平假名才能进入下一个
    step 2: 随机显示所有平假名/罗马音/读音，在命令行输入正确平假名才能进入下一个
    step 3: 随机显示所有平假名/读音，在命令行输入正确平假名才能进入下一个
    step 4: 随机显示所有罗马音/读音，在命令行输入正确平假名才能进入下一个
    step 5: 随机显示所有罗马音，在命令行输入正确平假名才能进入下一个
    step 6: 随机显示所有平假名，在命令行输入正确平假名才能进入下一个
    step 7: 随机显示所有读音，在命令行输入正确平假名才能进入下一个
    '''
    #step 1
    for item in gojuon:
        while not one_item(item):
            pass
    #step 2
    for item in sample(gojuon, len(gojuon)):
        while not one_item(item):
            pass
    #step 3
    for item in sample(gojuon, len(gojuon)):
        while not one_item(item, rome=False):
            pass
    #step 4
    for item in sample(gojuon, len(gojuon)):
        while not one_item(item, char=False):
            pass
    #step 5
    for item in sample(gojuon, len(gojuon)):
        while not one_item(item, char=False, pron=False):
            pass
    #step 6
    for item in sample(gojuon, len(gojuon)):
        while not one_item(item, rome=False, pron=False):
            pass
    #step 7
    for item in sample(gojuon, len(gojuon)):
        while not one_item(item, char=False, rome=False):
            pass

if __name__ == '__main__':
    main()
