#region Data preprocess

class InvalidFileExtensionException(ValueError):
    pass

class InvalidFileNameException(ValueError):
    pass

#endregion

#region Entities

class InvalidLanguageException(ValueError):
    pass

class ValueTypeException(TypeError):
    pass

class ValueBlankException(ValueError):
    pass

class ValueLetterCaseException(ValueError):
    pass

class ValueContainsNonENGLetters(ValueError):
    pass

class ValueContainsNonRUSLetters(ValueError):
    pass

class ValueContainsOtherCharactersException(ValueError):
    pass

#endregion
