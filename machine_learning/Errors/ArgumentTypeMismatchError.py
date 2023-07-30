class ArgumentTypeMistmatchError(Exception):
    """A child of the exception class used to define an error of types
    being mismatched. 

    Args:
        expectedType (_type_): The type expected to be provided
        providedType (_type_): The type provided

    """
    def __init__(self, parameter, expectedType, providedType):
        self.parameter = parameter
        self.expectedType = expectedType
        self.providedType = providedType
        self.message = f"Expected type {expectedType} for parameter named {parameter}, but was given {providedType}"
        super().__init__(self.message)
        return
        