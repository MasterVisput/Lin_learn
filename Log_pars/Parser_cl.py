import json
import re
from collections import Counter

class Parser():
    def __init__(self):
        self.filename = '../logs/access-39204-d17ad0.log'
        self.re_ip_add = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
        self.re_methods = r'\"\[:alpha:]{3,4}'

    def reader(self, reg):
        with open(self.filename) as f:
            log = f.read()
            res_list = re.findall(reg, log)
        return res_list

    def count(self, res_list):
        count = Counter(res_list)
        return count