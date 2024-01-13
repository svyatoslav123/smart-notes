from PyQt6.QtWidgets import *
app = QApplication([])

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
main_line.addLayout(v1)
main_line.addLayout(v2)
window.setLayout(main_line)

window.show()
app.exec()