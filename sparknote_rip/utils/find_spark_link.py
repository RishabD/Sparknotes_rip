from utils.traverse_main import traverse_main
from googlesearch import search


def find_spark(name):
   name = 'Sparknotes' + name
   for result in search(name, tld="com", num=10, stop=10, pause=2):
       if('sparknotes' in result):
           print(result)
           traverse_main(result,name)
           break


