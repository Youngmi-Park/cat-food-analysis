import csv
import re
import time
import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

def move_page(url,page_num):
    # 페이지 이동-url 재설정
    url = 'https://www.chewy.com/b/dry-food-388'+"_p"+str(page_num)

url_list=['https://www.chewy.com/b/dry-food-388','https://www.chewy.com/b/dry-food_c388_p2',
          'https://www.chewy.com/b/dry-food_c388_p3', 'https://www.chewy.com/b/dry-food_c388_p4', 'https://www.chewy.com/b/dry-food_c388_p5',
          'https://www.chewy.com/b/dry-food_c388_p6', 'https://www.chewy.com/b/dry-food_c388_p7', 'https://www.chewy.com/b/dry-food_c388_p8',
          'https://www.chewy.com/b/dry-food_c388_p9', 'https://www.chewy.com/b/dry-food_c388_p10', 'https://www.chewy.com/b/dry-food_c388_p11',
          'https://www.chewy.com/b/dry-food_c388_p12', 'https://www.chewy.com/b/dry-food_c388_p13', 'https://www.chewy.com/b/dry-food_c388_p14',
          'https://www.chewy.com/b/dry-food_c388_p15', 'https://www.chewy.com/b/dry-food_c388_p16',  'https://www.chewy.com/b/dry-food_c388_p17']

request_headers = {
    'User-Agent': ('Mozilla/5.0 (Windows NT 10.0;Win64; x64)\
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98\
Safari/537.36'), }

with open('crawling_review.csv', 'w', newline='') as file:
  writer = csv.writer(file)

  table = []  # 전체 데이터
  for i in url_list[0:2]:
      # Chrome의 경우 다운받은 chromedriver의 위치를 지정해준다.
      # 본인 노트북경로 가져와서 괄호에 넣어주면됩니다!
      driver1 = webdriver.Chrome('C:/Users/s_py9/chromedriver')  # 사료 페이지 링크 크롤링용 드라이버
      driver1.implicitly_wait(10)  # 웹 자원 로드를 위해 delay해줌.

      # 'chewy' 사이트에서 cat>food>dry food url
      url = i
      response = requests.get(url, headers=request_headers)
      driver1.get(url)  # url 접근
      time.sleep(1)
      print(response)  # 연결상태 200이 나오면 정상 접속

      # beautifulsoup 연결
      html = driver1.page_source
      soup = BeautifulSoup(html, 'html.parser')

      count = 0  # 사이트 페이지 카운트 변수 1~17
      link_list = []

      # 테스트를 위해서 2로 지정해놨는데 페이지 가져오는 부분 수정 후 변수 넣어주면됩니당

      links = soup.find_all('a', {'class': "product"})  # 제품별 링크 가져오기
      for link in links:
          link_list.append("https://www.chewy.com" + link["href"])  # 찾은 a태그의 href 값 크롤링
          # print(count+1 ,".", "https://www.chewy.com"+link["href"] ) - 사이트 개수, 링크 확인용

      print(link_list)

      for i in range(1):
          driver2 = webdriver.Chrome('C:/Users/s_py9/chromedriver')  # 사료 페이지 링크 크롤링을 위한 드라이버
          driver2.implicitly_wait(10)  # 웹 자원 로드를 위해 기다려 준다.

          url = link_list[i]
          response = requests.get(url, headers=request_headers)  # url 접근
          print(response)  # 연결상태 확인
          driver2.get(url)
          # soup
          html = driver2.page_source
          soup = BeautifulSoup(html, 'html.parser')
          time.sleep(3)  # delay해줌

          row = []  # 사료 1개의 정보를 담는 변수
          # 각 사료 페이지에 들어가서 내용을 크롤링하는 함수
          # Description
          product = soup.select('#product-title > h1')[0].text  # 제품명
          brand = soup.select('#product-subtitle > a > span')[0].text  # 브랜드명

          # 리뷰 개수
          try:
              review_num = soup.select(
                  '#ugc-section > header > div > span.ugc-list__header--reviews.ugc-list__header--reviews--pdp > a > span')[
                  0].text
          except:
              review_num = ''
          # 리뷰 평점
          try:
              review_star = soup.select('#ugc-section > header > div > span.ugc-list__header--count > span')[
                  0].text
          except:
              review_star = ''
          # 리뷰내용
          try:
              review_text = soup.find_all('span', {'class': 'ugc-list__review__display'})
          except:
              review_text = ''
          driver2.close()  # driver2 종료


          print(review_num)
          print(len(review_text))
          print(review_text)

          # 데이터 삽입
          row.append(product.strip())
          row.append(brand.strip())
          row.append(review_num.strip())
          row.append(review_star.strip())
          for review in review_text:
              row.append(review.get_text())

          writer.writerow(row)# 파일에 데이터 입력

