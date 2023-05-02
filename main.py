import requests
from bs4 import BeautifulSoup
import json
import pprint
import requests

import requests

def get_auto_complete(keyword):
    cookies = {
        'NNB': 'IZBJERH4DQMGI',
        'ASID': '798f73fa0000018710b1765100000069',
        'nx_ssl': '2',
        '_ga_8P4PY65YZ2': 'GS1.1.1682903623.1.1.1682903773.0.0.0',
        '_ga': 'GA1.2.2015093219.1682903623',
        'nid_inf': '-1221317091',
        'NID_AUT': 'El/fLajCubWw1WgLoDDlx5gt6VvXJrEadqtWkciHfNxCnUoZmh34l07cb2XltusE',
        'NID_JKL': 'L0XDOj8q72QKS1Gq/mev+aAWYWG91G7KXXDPeQlr/7g=',
        'CBI_SES': '9T/F57iTfgqB4AL9pAkFC98t7VUmCHbS5BIqQA//V7lyRmBNxPJ7MCR7lBRLbkbRp0RGh+odhW/7QNarKc/BHu+BVOCYgfnEl6fj/kEMNf4re3uorhPqRbSM+ctJPT11YzBX5XGbOTOaRLBYPNWeSsmodAVqdZdmba+XpVRN5lXDOW4B+IQ1u+iNo6HzReMvgjkVW0dnuRnlY8gA3fmnyBcO/5b/yOh1Fdx1RsQBbGgiGCaYJY2FQzYfK4SuTU5QUFFqZJ+bvsj3W+ArsOSP6P0JjENBwwaLbvs8cgT93U8Nlx1yjpx2Ht/B/ZH2P/BhOU19lUgUss0u1rjgNNbgrx78POHNbvhvVMvGqFbZwzXv5wTbuPsMACHhB3XYiHcWJpz/1ydvXb1zmVU7n7/OZJJEpdeGnp6MTHVB/dhBMU/1PN93GPTOG2vlzbw/vlyKkoZiSUN9BGoLKScDfGjr3tX/XF8qki3baAzLYaOZfjE=',
        'page_uid': 'iau9Kwp0YihssNo7fGdssssstwN-389281',
        'CBI_CHK': '"r5V0mf9uRUZHZ/vmLGy3ez7f4/k4aqWXL5o03eN68fqmtn3i/1fk2+lQ73F3ActQwXA3ebyWFycKyrYxf9Hx2zQwfLDhsoq4rSiIfEf21n4dsG+DnKsVlLQzbe6uNjKL8oz1c6f63TKqibGK26Y6NxqOfZGyR2a4ZYZf1AdQOuc="',
        'NID_SES': 'AAABt/8jdC/6BpXxoKKtFcv4qC1Ge9o2vbxQhazzkFSJl3SHCMEiDTVvBHXAZ+VJz2qwvq1JgAOK6zdFXX85Dh3EVX6YwTCSDS0Lubb4Kke7EqlDDwS+cwlgRp1R+YkK/raQpCJmrhpHDmNCASmJ5UrTyPb3TGaRmXciX/t4dDRIgKJ/geS+URjVJNdDEkrjsxtBeewI7yDf5mTv9Pfj8EH/XZxFh8+dMuLU4XTh2bd8Zz4zoaEmZdkXMwmFpmBxnOh3XolQq38FBXISSdVBMiGdWUEkJbAHcZ4aA+2OB17mSHL1dUK/DLTKN1yF7uYUzKSSpBDB5HUjMkjNoqNdHe4DRcY7GwfqHCPo+Ys0yxusdLMkB97fatzvPIxqnHVUNufOM3rEjK+A2+BC3e5cWG+85ocVj4POq+AZ61yvFCLn4vOav3jeyvF6qfOzZodZovB8V0CMU0PuReGd+Oakl388pSWLXqT2hPeY7Q88r1VSlrYjjd6UBgAZHbabUkCZpHFYeWSCK2B6XkjGO/tL+0K1y8Htbh+W0yYG67XjjsyeAYC97TBHLI5YUsDC45w/zv2IIHSS8oOxEet7IQpAH+lS4dA=',
        '_naver_usersession_': '2ePIEVjB2apdiNlP7ZMGCSKp',
    }

    headers = {
        'authority': 'ac.search.naver.com',
        'accept': '*/*',
        'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
        # 'cookie': 'NNB=IZBJERH4DQMGI; ASID=798f73fa0000018710b1765100000069; nx_ssl=2; _ga_8P4PY65YZ2=GS1.1.1682903623.1.1.1682903773.0.0.0; _ga=GA1.2.2015093219.1682903623; nid_inf=-1221317091; NID_AUT=El/fLajCubWw1WgLoDDlx5gt6VvXJrEadqtWkciHfNxCnUoZmh34l07cb2XltusE; NID_JKL=L0XDOj8q72QKS1Gq/mev+aAWYWG91G7KXXDPeQlr/7g=; CBI_SES=9T/F57iTfgqB4AL9pAkFC98t7VUmCHbS5BIqQA//V7lyRmBNxPJ7MCR7lBRLbkbRp0RGh+odhW/7QNarKc/BHu+BVOCYgfnEl6fj/kEMNf4re3uorhPqRbSM+ctJPT11YzBX5XGbOTOaRLBYPNWeSsmodAVqdZdmba+XpVRN5lXDOW4B+IQ1u+iNo6HzReMvgjkVW0dnuRnlY8gA3fmnyBcO/5b/yOh1Fdx1RsQBbGgiGCaYJY2FQzYfK4SuTU5QUFFqZJ+bvsj3W+ArsOSP6P0JjENBwwaLbvs8cgT93U8Nlx1yjpx2Ht/B/ZH2P/BhOU19lUgUss0u1rjgNNbgrx78POHNbvhvVMvGqFbZwzXv5wTbuPsMACHhB3XYiHcWJpz/1ydvXb1zmVU7n7/OZJJEpdeGnp6MTHVB/dhBMU/1PN93GPTOG2vlzbw/vlyKkoZiSUN9BGoLKScDfGjr3tX/XF8qki3baAzLYaOZfjE=; page_uid=iau9Kwp0YihssNo7fGdssssstwN-389281; CBI_CHK="r5V0mf9uRUZHZ/vmLGy3ez7f4/k4aqWXL5o03eN68fqmtn3i/1fk2+lQ73F3ActQwXA3ebyWFycKyrYxf9Hx2zQwfLDhsoq4rSiIfEf21n4dsG+DnKsVlLQzbe6uNjKL8oz1c6f63TKqibGK26Y6NxqOfZGyR2a4ZYZf1AdQOuc="; NID_SES=AAABt/8jdC/6BpXxoKKtFcv4qC1Ge9o2vbxQhazzkFSJl3SHCMEiDTVvBHXAZ+VJz2qwvq1JgAOK6zdFXX85Dh3EVX6YwTCSDS0Lubb4Kke7EqlDDwS+cwlgRp1R+YkK/raQpCJmrhpHDmNCASmJ5UrTyPb3TGaRmXciX/t4dDRIgKJ/geS+URjVJNdDEkrjsxtBeewI7yDf5mTv9Pfj8EH/XZxFh8+dMuLU4XTh2bd8Zz4zoaEmZdkXMwmFpmBxnOh3XolQq38FBXISSdVBMiGdWUEkJbAHcZ4aA+2OB17mSHL1dUK/DLTKN1yF7uYUzKSSpBDB5HUjMkjNoqNdHe4DRcY7GwfqHCPo+Ys0yxusdLMkB97fatzvPIxqnHVUNufOM3rEjK+A2+BC3e5cWG+85ocVj4POq+AZ61yvFCLn4vOav3jeyvF6qfOzZodZovB8V0CMU0PuReGd+Oakl388pSWLXqT2hPeY7Q88r1VSlrYjjd6UBgAZHbabUkCZpHFYeWSCK2B6XkjGO/tL+0K1y8Htbh+W0yYG67XjjsyeAYC97TBHLI5YUsDC45w/zv2IIHSS8oOxEet7IQpAH+lS4dA=; _naver_usersession_=2ePIEVjB2apdiNlP7ZMGCSKp',
        'referer': 'https://www.naver.com/',
        'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'script',
        'sec-fetch-mode': 'no-cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    }

    params = {
        'q': str(keyword),
        'con': '1',
        'frm': 'nv',
        'ans': '2',
        'r_format': 'json',
        'r_enc': 'UTF-8',
        'r_unicode': '0',
        't_koreng': '1',
        'run': '2',
        'rev': '4',
        'q_enc': 'UTF-8',
        'st': '100',
        '_callback': '_jsonp_10',
    }

    response = requests.get('https://ac.search.naver.com/nx/ac', params=params, cookies=cookies, headers=headers)
    # print(response.text)
    position_fr=response.text.find("{")
    position_rr = response.text.rfind("}")
    result=json.loads(response.text[position_fr:position_rr+1])['items'][0]
    # pprint.pprint(result)
    keywordList=[]
    for elem in result:
        keywordElem=elem[0]
        keywordList.append(keywordElem)
    print('keywordList:',keywordList)

keyword="아쿠아슈즈"
get_auto_complete(keyword)