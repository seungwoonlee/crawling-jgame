#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from selenium import webdriver
import pickle
import sys
 
url_ps4 = "https://m.cafe.naver.com/jgameshop/4228"     # JGame NaverCafe Mobile Page Used PS4 Titles
 
def print_games(games, start = 0):
    '''   
    :param games: 게임목록 리스트
    :param start: 출력을 시작할 행
    :return:
    '''
    current = -1
    for i in games:
        current += 1
        if current < start:
            continue
        if i[0] == '#':
            continue
        print(i)
 
def check_equal_lists(list1, list2):
    for i in list1:
        if i not in list2:
            return False
    for j in list2:
        if j not in list1:
            return False
    return True
 
# 지난 정보 로딩
try:
    games_ps4_old = []
    f = open('ps4', 'rb')
    games_ps4_old = pickle.load(f)
    f.close()
except:
    print("ERROR : ps4 file read error")
finally:
    pass
    #print_games(games_ps4_old, 11)
 
# Chrome Headless 웹드라이버 설정
options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome('chromedriver', options=options)
 
# 새 정보 읽기
driver.get(url_ps4)
games_ps4_new = driver.find_element_by_xpath('//*[@id="postContent"]').text.split('\n')     # '\n' 으로 끊어서 List로
driver.quit()
#print(games_ps4_new[11:])
 
if check_equal_lists(games_ps4_old, games_ps4_new):
    print("변경이 없으므로 프로그램을 종료합니다.")
    sys.exit()
 
# 새 파일로 덮어쓰기
try:
    f = open('ps4', 'wb')
    pickle.dump(games_ps4_new, f)
    f.close()
except:
    print("ERROR : ps4 file write error")
finally:
    pass
 
# 게임변경 검색
games_ps4_sold = []
games_ps4_incomming = []
for old in games_ps4_old:
    if old not in games_ps4_new:
        games_ps4_sold.append(old)
 
for new in games_ps4_new:
    if new not in games_ps4_old:
        games_ps4_incomming.append(new)
 
print("팔린 PS4 Games")
print(games_ps4_sold)
print("새로들어온 PS4 Games")
print(games_ps4_incomming)
