import requests
url_1='http://leanpub.com/s/SCfelEtD0eXtG7CBg9kH0g.pdf'
url_2='https://leanpub.com/s/G1QDvnAiYLKYcfOQd4p1zQ.pdf'

# url_2='http://leanpub.com/s/SCfelEtD0eXtG7CBg8kH0g.pdf'


with requests.Session() as a:
    r_1=a.get(url_1)
    print("url_1 ",r_1.status_code)
    r_2=a.get(url_2)
    print("url_2 ",r_2.status_code)
