from PyQt6.QtWidgets import *
from PyQt6.QtWidgets import *
from PyQt6.QtWidgets import *
from PyQt6.QtWidgets import *
app = QApplication([])
app.setStyleSheet("""
     QWidget {
        background: #ccdaed;
     }
     QPushButton {
        background: #e9edf2;
        border-style: outset;
        min-height: 30px;
        min-width: 100px;
     }
     QListWidget { 
        background: #ccdbd5;
     }
     QTextEdit { 
        background: #e1ede8;
     }

      QPushButton {
        color: blue;
        font-size: 15px;
        font-family: Impact;
        border-width: 2px;
        border-color: black;
        border-radius: 5px;
     }
      QPushButton#save_btn {
        color: green;
        font-size: 20px;
        font-family: Impact;
        border-width: 4px;
        border-color: black;
        border-radius: 5px;
      }

 """)
import json


notes = {}
window = QWidget()
window.resize(700, 500)
text_edit = QTextEdit()
list_widget = QListWidget()
create_btn = QPushButton("Створити замітку")
delate_btn = QPushButton("Видалити замітку")
save_btn = QPushButton("Зберегти замітку")
list_tegs = QListWidget()
enter_teg = QLineEdit("Введіть тег...")
add_to_notes = QPushButton("Додати до  замітки")
open_to_notes = QPushButton("Відкрити до замітки")
search_notes_for_teg = QPushButton("Шукати замітку по тегу")
list_notes_lbl = QLabel("Список заміток")
list_tegs_lbl = QLabel("Список тегів")
skunytu =  QLabel("Скинути пошук")
save_btn.setObjectName("save_btn")




main_line = QHBoxLayout()

v1 = QVBoxLayout()
v1.addWidget(text_edit)
v2 = QVBoxLayout()
v2.addWidget(list_notes_lbl)
v2.addWidget(list_widget)
v2.addWidget(create_btn)
v2.addWidget(delate_btn)
v2.addWidget(save_btn)
v2.addWidget(list_tegs_lbl)
v2.addWidget(list_tegs)
v2.addWidget(enter_teg)
v2.addWidget(add_to_notes)
v2.addWidget(open_to_notes)
v2.addWidget(search_notes_for_teg)
v2.addWidget(skunytu)
main_line.addLayout(v1)
main_line.addLayout(v2)
window.setLayout(main_line)
def read_data():
    global notes
    with open("database.json", "r", encoding="utf-8") as file:
       notes = json.load(file)

def write_data():
    global notes
    with open("database.json", "w", encoding="utf-8") as file:
        json.dump(notes, file, ensure_ascii=False, indent=4)
read_data()
list_widget.addItems(notes)
def vmist_note():
    name = list_widget.selectedItems()[0].text()
    text_edit.setText(notes[name]["вміст"])
    list_tegs.clear()
    list_tegs.addItems(notes[name]["теги"])
list_widget.itemClicked.connect(vmist_note)
def change_note():
    name = list_widget.selectedItems()[0].text()
    notes[name]["вміст"] = text_edit.toPlainText()
    write_data()
save_btn.clicked.connect(change_note)
def add_note():
    res, ok = QInputDialog.getText(window, "Введення", "Введіть назву замітки")
    if ok:
        notes[res] = {
            "вміст" : "",
            "теги" : []
        }
    list_widget.clear()
    list_widget.addItems(notes)
    write_data()
def del_note():
    res, ok = QInputDialog.getText(window, "Введення", "Введіть назву замітки")
    if ok:
        notes.pop(res)
        list_widget.clear()
        list_widget.addItems(notes)
        write_data()
def save_note():
    text_edit.setText(notes[name]["вміст"])
    notes[name]["вміст"] = text_edit.toPlainText()

    write_data()
def add_tag():
    name = list_widget.selectedItems()[0].text()
    tag = enter_teg.text()
    notes[name]["теги"].append(tag)
    list_tegs.clear()
    list_tegs.addItems(notes[name]["теги"])
    write_data()
def delete_tag():
    name = list_widget.selectedItems()[0].text()
    name_tag = list_tegs.selectedItems()[0].text()
    notes[name]["теги"].remove(name_tag)
    list_tegs.clear()
    list_tegs.addItems(notes[name]["теги"])
    write_data()
def search_tag():  # кнопка "шукати замітку за тегом"
    button_text = search_notes_for_teg.text()
    tag = enter_teg.text()

    if button_text == "Шукати замітки за тегом":
        apply_tag_search(tag)
    elif button_text == "Скинути пошук":
        list_widget.clear()
        list_widget.addItems(notes)
        search_notes_for_teg.setText(skunytu)

def apply_tag_search(tag):
    notes_filtered = {}
    for note, value in notes.items():
        if tag in value["теги"]:
            notes_filtered[note] = value

    search_notes_for_teg.setText("Скинути пошук")
    list_widget.clear()
    list_tegs.clear()
    list_widget.addItems(notes_filtered)

open_to_notes.clicked.connect(delete_tag)

save_btn.clicked.connect(save_note)
add_to_notes.clicked.connect(add_tag)
create_btn.clicked.connect(add_note)
delate_btn.clicked.connect(del_note)
window.show()
app.exec()