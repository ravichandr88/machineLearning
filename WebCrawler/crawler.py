from selenium import webdriver
import os
print(os.path.dirname(os.path.realpath(__file__)))
browser = webdriver.Firefox(r"D:\crawler")


# print(len(open("D:/crawler",'r').readlines()))