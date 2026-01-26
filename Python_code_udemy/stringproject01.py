#[82]Url Parsing
""" 
    Data science community website 
       https://www.kaggle.com/datasets

       (https  [protocol]), (.kaggle.   [domain name]), (datasets [page])

"""
url='https://www.kaggle.com/datasets'
protocol=url[0:url.find(':')]

dot1=url.find('.')
dot2=url.find('.',dot1+1)
domain=url[dot1:dot2]

page=url[url.find('/',dot2):]
print(protocol)
print(domain)
print(page)
