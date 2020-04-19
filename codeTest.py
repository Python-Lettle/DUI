#!/usr/bin/env python
# -*- coding: cp936 -*-
#__author__ = "Lettle"
#QQ: 1071445082
#fileName: *.py
from DUI.bin.func import *

def strB2Q(ustring):
    """���ַ���ȫ��ת���"""
    ss = []
    for s in ustring:
        rstring = ""
        for uchar in s:
            inside_code = ord(uchar)
            if inside_code == 32:  # ȫ�ǿո�ֱ��ת��
                inside_code = 12288
            elif (inside_code >= 33 and inside_code <= 126):  # ȫ���ַ������ո񣩸��ݹ�ϵת��
                inside_code += 65248
            rstring += chr(inside_code)
        ss.append(rstring)
    return ''.join(ss)

def strQ2B(ustring):
    """���ַ���ȫ��ת���"""
    ss = []
    for s in ustring:
        rstring = ""
        for uchar in s:
            inside_code = ord(uchar)
            if inside_code == 12288:  # ȫ�ǿո�ֱ��ת��
                inside_code = 32
            elif (inside_code >= 65281 and inside_code <= 65374):  # ȫ���ַ������ո񣩸��ݹ�ϵת��
                inside_code -= 65248
            rstring += chr(inside_code)
        ss.append(rstring)
    return ''.join(ss)

print(slen("�ģգ�"))