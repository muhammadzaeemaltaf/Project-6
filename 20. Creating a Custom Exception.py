class InvalidAgeError(Exception):
    """Raised when the provided age is less than 18"""
    pass


def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be at least 18")
    return True


try:
    check_age(16)
except InvalidAgeError as e:
    print(f"InvalidAgeError: {e}")
else:   
    print("Age is valid")
