import datetime
last_id = 0

class Note:
    """Represent a note in a note book. Match by memo strings or tags in search."""

    def __init__(self, memo, tags=''):
        """Inialize a note with memo and optional space seperated tags. Creation date and id are set
        automatically."""
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()
        global last_id
        last_id += 1
        self.id = last_id

    def match (self, filt):
        """Determine if the note matches the filter string. Return True if it match and false otherwise.
        The search is case sensitive and the range is in memo and tags"""
        return filt in self.memo or filt in self.tags

class Notebook:
    """Represent a collection of notes that can be tagged, modified, searched."""

    def __init__(self):
        """Initialize with empty list"""
        self.notes=[]

    def new_note(self, memo, tags=''):
        """Create new notes"""
        self.notes.append(Note(memo, tags))

    def _find_note(self, note_id):
        """find a note by id"""
        for note in self.notes:
            if str(note.id) == str(note_id):
                return note
        return None

    def modify_memo(self, note_id, memo):
        """Search note by id, change tags to new given value"""
        note = self._find_note(note_id)
        if note:
            note.memo = memo
            return True
        return False

    def modify_tags (self, note_id, tags):
        """Search note by id, change tags to new given value"""
        note = self._find_note(note_id)
        if note:
            note.tags = tags
            return True
        return False

    def search(self, filt):
        """Search by mathing the filter sting"""
        return [note for note in self.notes if note.match(filt)]


if __name__ == '__main__':
    print('hello')
