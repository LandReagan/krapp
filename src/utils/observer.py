"""
Observer pattern implementation.

Any observable object shall inherit from Observable, and an observer from
Observer.
"""

from abc import ABC, abstractmethod


class Observer(ABC):
    """
    Observer class needs to be added in Observable container of Observers.
    Implement update() to define what happens on Observable notifications.
    """
    @abstractmethod
    def update(self, data: any) -> None:
        """
        namedtuple from collections python module is recommended for passing
        data to observers.
        :param data: any, use namedtuple! or whatever you want.
        """
        pass


class Observable(ABC):
    """
    Observable keeps a list of Observers, and it notifies them when method
    notify() is called. Use the different methods to deal with Observers.
    """

    @abstractmethod
    def add_observer(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def remove_observer(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def notify_observers(self) -> None:
        """
        Method to invoke for observers notification.
        """
        pass
