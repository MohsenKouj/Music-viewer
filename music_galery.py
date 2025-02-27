import Listener # type: ignore
from Music_Light_Class import Provider,Events # type: ignore

class music_viewer():
    provider = Provider()
    events = Events()
    path = ""
    event = 0
    occupation = False

    def play(self,path):
        self.path = path
        self.occupation = True
        self.event = self.provider.AttrebDisplay(self.path)
        self.occupation = False
        return self


    def if_event_close(self):
        if(self.event == self.events.close()):
            return True
        return False

    def if_event_next(self):
        if(self.event == self.events.next()):
            return True
        return False

    def if_event_prev(self):
        if(self.event == self.events.prev()):
            return True
        return False

    def if_event_end(self):
        if(self.event == self.events.end()):
            return True
        return False
    
musics = [
    r"D:\Majid Razavi - Manam (320).mp3",
    r"D:\Mehrab - Khianat 128.mp3",
    r"D:\Mohsen Yahaghi - Gele (320).mp3",
    r"D:\Naser Zeynali - Tavalod (320).mp3"
]
mv = music_viewer()
round_ = 0
while(True):
    if mv.if_event_close():
        break
    elif mv.if_event_next() or mv.if_event_end():
        if round_ < len(musics)-1:
            round_ += 1
    elif mv.if_event_prev():
        if round_ > 0:
            round_ -= 1

    mv.play(musics[round_])
    