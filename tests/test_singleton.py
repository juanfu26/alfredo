
from app.utils.singleton import Singleton

class InstaceOfSingleton(metaclass=Singleton):
        pass

class TestSingleton():
    
    def test_singleton_is_always_same_object(self):
        assert InstaceOfSingleton() is InstaceOfSingleton()

        # Sanity check - a non-singleton class should create two separate
        #  instances
        class NonSingleton:
            pass
        assert NonSingleton() is not NonSingleton()

