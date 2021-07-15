coin = {
    'BTC': {
        'opening_price': '44405000',
        'closing_price': '38806000',
        'min_price': '36640000',
        'max_price': '44999000',
        'prev_closing_price': '44404000',
        'fluctate_24H': '-7463000',
        'fluctate_rate_24H': '-16.13',
    },
    'XRP': {
        'opening_price': '364.5',
        'closing_price': '311.9',
        'min_price': '284.2',
        'max_price': '372.7',
        'prev_closing_price': '364.2',
        'fluctate_24H': '-90.6',
        'fluctate_rate_24H': '-22.51',
    },
}

#1. 최대 가격
# def a(k):
#     for i in coin['BTC'.itmes()]:
#         return i
#     print(i)
# k=coin['BTC']
# a(k)

# a=coin['BTC']
# b=a.items()
# print(b)

# a=coin['BTC']['max_price']
# print(a)


#2. btc 시가와 xrop시가 더한 결과 출력

# b=int(coin['BTC']['opening_price'])
# c=float(coin['XRP']['opening_price'])
# print(b+c) #---> 숫자 붙어서 나옴---> type 입력해줘야 함
# print(type(b+c))

movie = {
    'movieInfo': {
        'movieNm': '광해, 왕이 된 남자',
        'movieNmEn': 'Masquerade',
        'showTm': '131',
        'prdtYear': '2012',
        'openDt': '20120913',
        'typeNm': '장편',
        'nations': [{'nationNm': '한국'}],
        'genres': [{'genreNm': '사극'}, {'genreNm': '드라마'}],
        'directors': [{'peopleNm': '추창민', 'peopleNmEn': 'CHOO Chang-min'}],
        'actors': [
            {'peopleNm': '이병헌', 'peopleNmEn': 'LEE Byung-hun', 'cast': '광해/하선'},
            {'peopleNm': '류승룡', 'peopleNmEn': 'RYU Seung-ryong', 'cast': '허균'},
            {'peopleNm': '한효주', 'peopleNmEn': 'HAN Hyo-joo', 'cast': '중전'},
        ],
    }
}

#1. 영화 제목
print(movie['movieInfo']['movieNm'])

#2. 다음 movie 감독의 영어 이름
a=movie['movieInfo']['directors'][0]['peopleNmEn']
print(a)
#3. 다음 movie 배우의 인원 출력
b=movie['movieInfo']['actors']    ###### 갹 len을 안쓰고 counter를 했다!
print(len(b))

##

