import copy

class BaseWorker(object):
    """
    Base class for Mycroft Workers. Workers accept an arbitrary set of keyword arguments.
    Use these to configure worker instances.

    Attributes:
        name (str): The name of your worker
    """

    def __init__(self, name,**kwargs ):

        self.name = name
        self.set_params(**kwargs)

    def execute(self, x = None):
        """
         Workers are expected to supply an execute method. This method will be called when the worker is run.
         Each execution operates on an mutates on a single input variable x.
        """

        raise NotImplementedError('You must implement an execute method')

        return x

    def get_param(self, param):
        return getattr(self, param)

    def preview(self, x=None):
        """
         Workers are may supply a preview method. This method delivers representative outputs without
         mutating the input variable.

        """
        raise NotImplementedError('Implement a preview method to provide a preview of the workers outputs')

        y = copy.deepcopy(x)

        return y

    def set_params(self, **params):
        for key,value in list(params.items()):

            setattr(self, key, value)

        return self