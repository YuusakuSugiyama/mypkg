#!/usr/bin/env python3

import random

rospy.init_node('omikuji')

result = [
        '大吉！！',
        '中吉！！',
        '末吉！！',
        '吉！！',
        '小吉！！',
        '凶！！',
        '大凶！！',]

omikuji = random.choice(result)

name = input(’あなたの名前を入力してください:')
        print(name + 'さんの運勢は' + omikuji)
