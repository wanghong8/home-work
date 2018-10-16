#使用__new__方法创建单例模式的类：
#如果 cls._instance 为 None 则创建实例，否则直接返回 cls._instance。
class Singleton(object):
    __instance=None
    def __new__(cls):
        if cls.__instance==None: #如果__instance为空，则证明是第一次创建实例
            cls.__instance= object.__new__(cls)
            return cls.__instance
        else:
            return cls.__instance


a=Singleton()
b=Singleton()
print(id(a))
print(id(b))