import threading
import thread
import time

class my_thread (threading.Thread):
        def __init__(self, thread_ID, name, function, radians):
            threading.Thread.__init__(self)
            self.thread_ID = thread_ID
            self.name = name
            self.function = function
            self.radians = radians
        def run(self):
            print "Starting " + self.name
            return function(*radians)
            print "Exiting " + self.name