#coding:utf-8
import memcache


class Cache:
    mem=None
    def __init__(self):
            self.mem=memcache.Client(['127.0.0.1:11211'])
       
    def set(self,key,time):
        def _set(func):
            def __set(*args):
                getValue=self.mem.get(key)
                if getValue!=None:
                    print "use cache"+":"+str(getValue)
                    return getValue
                else:
                    print "no cache"
                    setValue=func(*args)
                    self.mem.set(key,setValue,time)
                    return setValue
            return __set
            
        return _set