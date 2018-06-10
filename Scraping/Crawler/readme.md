#### Clone the whole folder!

**Run the main.py first**

**main.py** internally calls **general.py, spider.py, domain.py** and **link_finder.py**

In **main.py** the link of website and domain name of the website is passed.
**Spider.py** is called by the **main.py**.
So when the first instance of **Spider** is created it generates pool of links. This links now are crawled by various spiders
generated. The program generates two files:

1. **crawled.txt** : It consist of links which are already crawled 

2. **queue.txt** : It consist of links which havent yet crawled.

The **domain.py** returns the domain name from the url passed in main.py

The **general.py** is meant for saving sets data into files i.e crawled.txt and queue.txt

The **link_finder.py** returns all links present in page which is currently crawled.
