import wget
from bs4 import BeautifulSoup
import httplib2
import tkinter as tk

def download_files(baseurl, folder):
    url = baseurl.get()
	fol = folder.get()
	soup = BeautifulSoup(url,"html.parser")
    for link in soup.find_all('a'):
        download = link.get('href')
        wget.download(download, '/Users/Misha/Downloads/'+fol+'/'+link.get_text())
		
root= tk.Tk()

canvas1 = tk.Canvas(root, width = 400, height = 400)
canvas1.pack()

entry1 = tk.Entry(root)
canvas.create_window(200,140, window = entry1)


entry2 = tk.Entry(root)
canvas.create_window(300,140, window = entry2)

tk.Button(text='Download', command=download_files, bg='brown', fg='white', font=('helvetica', 9, 'bold')