from tkinter import *
import newegg_scrapper, amazon_scrapper
app = Tk()

mainFrame = Frame(app, width=800, height=600)
mainFrame.pack()

intoLabel = Label(mainFrame, text="This app allows you to scrape either amazon or newegg for products")
intoLabel.pack()

searchFrame = Frame(mainFrame, width=300, height=200)
searchFrame.pack()

searchLabel = Label(searchFrame, text="Enter the term to search for:")
searchLabel.pack(side=LEFT)
searchInput = Entry(searchFrame)
searchInput.pack()

button = Button(mainFrame, text="Scrape")
button.pack()

app.mainloop()

