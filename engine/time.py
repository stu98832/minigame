class Clock():
    def __init__(self):
        self.last_update = 0
        self.curr_update = 0

    def initialize(self):
        import time
        
        self.last_update = time.time()
        self.curr_update = time.time()

    def update(self):
        import time

        self.curr_update = time.time()
        self.elapsed = self.curr_update - self.last_update
        self.last_update = self.curr_update

class Timer():
    def __init__(self, 
        active   = False, 
        delay    = 0,
        loop     = False,
        callback = lambda:None
        ):
        self.elapsed  = 0
        self.active   = active
        self.delay    = delay
        self.loop     = loop
        self.callback = callback

    def update(self, clock):
        if not self.active:
            return

        self.elapsed += clock.elapsed
        while self.active and self.elapsed >= self.delay:
            self.callback()
            self.elapsed -= self.delay
            self.active = self.loop

    def start(self):
        self.active  = True

    def pause(self):
        self.active = False

    def stop(self):
        self.elapsed = 0
        self.active = False
    

