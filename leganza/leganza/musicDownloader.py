from bs4 import BeautifulSoup
import requests
import os

def getMusics(mood) : 
    print(os.path.abspath)
    preUrl = {'Happy' : 'https://gongu.copyright.or.kr/gongu/wrt/wrtCl/listWrtSound.do?menuNo=200020&pageIndex=1&moodCdStr=%EB%B0%9D%EC%9D%80_%EA%B2%BD%EC%BE%8C_%EB%93%9C%EB%9D%BC%EB%A7%88&genreCdStr=%ED%85%8C%EB%A7%88%EB%AE%A4%EC%A7%81_%EB%B0%9C%EB%9D%BC%EB%93%9C&nclsrCdStr=&tempoCdStr=&sortSe=down&depth2ClSn=&licenseCd=&searchWrd=&pageUnit=3&moodCd=%EB%B0%9D%EC%9D%80&moodCd=%EA%B2%BD%EC%BE%8C&moodCd=%EB%93%9C%EB%9D%BC%EB%A7%88&genreCd=%ED%85%8C%EB%A7%88%EB%AE%A4%EC%A7%81&genreCd=%EB%B0%9C%EB%9D%BC%EB%93%9C',
    'Sad' : 'https://gongu.copyright.or.kr/gongu/wrt/wrtCl/listWrtSound.do?menuNo=200020&pageIndex=1&moodCdStr=%EB%93%9C%EB%9D%BC%EB%A7%88_%EC%8A%AC%ED%94%88&genreCdStr=&nclsrCdStr=&tempoCdStr=%EB%8A%90%EB%A6%AC%EA%B2%8C&sortSe=down&depth2ClSn=&licenseCd=&searchWrd=&pageUnit=3&moodCd=%EB%93%9C%EB%9D%BC%EB%A7%88&moodCd=%EC%8A%AC%ED%94%88&tempoCd=%EB%8A%90%EB%A6%AC%EA%B2%8C'
    ,'Angry' : 'https://gongu.copyright.or.kr/gongu/wrt/wrtCl/listWrtSound.do?menuNo=200020&pageIndex=1&moodCdStr=%EB%AF%B8%EC%8A%A4%ED%84%B0%EB%A6%AC_%EC%96%B4%EB%91%90%EC%9B%80&genreCdStr=&nclsrCdStr=&tempoCdStr=%EB%B9%A0%EB%A5%B4%EA%B2%8C&sortSe=down&depth2ClSn=&licenseCd=&searchWrd=&pageUnit=3&moodCd=%EB%AF%B8%EC%8A%A4%ED%84%B0%EB%A6%AC&moodCd=%EC%96%B4%EB%91%90%EC%9B%80&tempoCd=%EB%B9%A0%EB%A5%B4%EA%B2%8C'
    , 'Neutral' : 'https://gongu.copyright.or.kr/gongu/wrt/wrtCl/listWrtSound.do?menuNo=200020&pageIndex=1&moodCdStr=%EB%B0%9D%EC%9D%80_%EA%B2%BD%EC%BE%8C_%EB%AA%85%EC%83%81_%EB%93%9C%EB%9D%BC%EB%A7%88_%EC%83%81%ED%81%BC&genreCdStr=%ED%85%8C%EB%A7%88%EB%AE%A4%EC%A7%81_%EB%B0%9C%EB%9D%BC%EB%93%9C&nclsrCdStr=&tempoCdStr=%EB%8A%90%EB%A6%AC%EA%B2%8C&sortSe=down&depth2ClSn=&licenseCd=&searchWrd=&pageUnit=3&moodCd=%EB%B0%9D%EC%9D%80&moodCd=%EA%B2%BD%EC%BE%8C&moodCd=%EB%AA%85%EC%83%81&moodCd=%EB%93%9C%EB%9D%BC%EB%A7%88&moodCd=%EC%83%81%ED%81%BC&genreCd=%ED%85%8C%EB%A7%88%EB%AE%A4%EC%A7%81&genreCd=%EB%B0%9C%EB%9D%BC%EB%93%9C&tempoCd=%EB%8A%90%EB%A6%AC%EA%B2%8C'
    ,'Disgust' : 'https://gongu.copyright.or.kr/gongu/wrt/wrtCl/listWrtSound.do?menuNo=200020&pageIndex=1&moodCdStr=%EB%AF%B8%EC%8A%A4%ED%84%B0%EB%A6%AC_%EC%96%B4%EB%91%90%EC%9B%80&genreCdStr=&nclsrCdStr=&tempoCdStr=%EB%B9%A0%EB%A5%B4%EA%B2%8C&sortSe=down&depth2ClSn=&licenseCd=&searchWrd=&pageUnit=3&moodCd=%EB%AF%B8%EC%8A%A4%ED%84%B0%EB%A6%AC&moodCd=%EC%96%B4%EB%91%90%EC%9B%80&tempoCd=%EB%B9%A0%EB%A5%B4%EA%B2%8C'
    }
    # mood : List[str], String형식의 분위기 원소를 가진 List
    html = requests.get(preUrl[mood])
    soup = BeautifulSoup(html.text, 'html.parser')
    data = soup.select('span.tit > a')
    desc = soup.select('li > p.txt')
    author = soup.select('span.ico_person')

    musicList = []
    for i in data : 
        musicList.append([i.text, i['href'].split('&')[0].split('=')[1]])
    for i in range(len(data)) : 
        musicList[i].append(desc[i].text)
        musicList[i].append(author[i].text.strip())
    # 음악 다운로드
    for i, t in enumerate(musicList) : 
        idx = 1
        while True :
            targetUrl = 'https://gongu.copyright.or.kr/gongu/wrt/cmmn/wrtFileDownload.do?wrtSn='+ str(t[1]) +'&fileSn=' + str(idx) + '&wrtFileTy=03'
            response = requests.get(targetUrl)
            ext = response.headers['Content-Disposition'].split(';')[1].split('\"')[1].split('.')[-1]
            
            if ext == 'mp3':
                with open('./leganza/static/rec'+ str(i) + '.' + ext, "wb") as file :
                    file.write(response.content)
                break
            idx += 1
    return musicList