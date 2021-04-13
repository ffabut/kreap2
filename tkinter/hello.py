import tkinter

window = tkinter.Tk()

listbox_entries = ["Entry 1", "Entry 2",
                   "Entry 3", "Entry 4"]
listbox_widget = tkinter.Listbox(
  window,
  selectmode=tkinter.MULTIPLE)

for entry in listbox_entries:
    listbox_widget.insert(tkinter.END, entry)

listbox_widget.pack()


while True:
  window.update()
  items = []
  
  selected = listbox_widget.curselection() #tuple obsahujici indexy oznacenych prvku
  for i in selected:
    item = listbox_widget.get(i) #pomoci metody get(index) ziskame hodnotu prvku pod danym indexem
    items.append(item)

  print(items)