from abc import ABC, abstractmethod


class FacialDetector(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def __call__(self, im, **kwargs):
        pass