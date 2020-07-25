from bs4 import BeautifulSoup
import requests
import webbrowser
import progressbar

from django.shortcuts import render

storeg_list = []

def crawl(request):
    if request.method == 'POST':
        url = request.POST['name']
        storeg_list.append(url)
        a = 0
        page_count = 1
        bar = progressbar.ProgressBar(maxval=100, \
                                      widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
        bar.start()
        while storeg_list[a]:
            r = requests.get(storeg_list[a])
            soup = BeautifulSoup(r.content, 'html.parser')
            for link in soup.find_all('a'):
                storeg_list.append(link.get('href'))

            for i in storeg_list:
                if i == None or i == '#' or i == '/':
                    continue
                elif i[0:4] == 'http':
                    page_count += 1
                    print("page_count ",page_count)
                    webbrowser.open(i)
                else:
                    webbrowser.open(url+i)
                    page_count += 1
                    print("page_count ", page_count)
                bar.update(page_count + 1)
                if page_count >= 100: break
            bar.finish()
            if page_count >= 100: break
            a += 1
            if storeg_list[a][0:4] != 'http':
                storeg_list[a] = url + storeg_list[a]

    return render(request, "index.html")




