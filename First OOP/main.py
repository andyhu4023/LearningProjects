from notebook import Note

n1= Note("Hello first")
n2 = Note("Hello", 'tag1 teg2')

print(n1.id, n2.id)
print(n1.match('Hello'), n2.match('he'))

from notebook import Notebook
n = Notebook()
n.new_note('Hello', 'first note in the note book')
n.new_note('See you')
print(n.notes)
for note in n.notes:
    print(note.id)
n.modify_tags(4, 'checked')
n.modify_memo(3, "Hello again!")
print(n.notes[0].memo, ';', n.notes[1].tags)
print(n.search('you'), n.search('You'))