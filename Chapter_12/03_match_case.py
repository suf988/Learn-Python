# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  MATCH CASE
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# the match-case statement in python is the same as the switch-case statement in any other language.

def http_status(status):
    match status:
        case 200:
            return f"{status}: OK"
        case 400:
            return f"{status}: Bad Request"
        case 403:
            return f"{status}: Forbidden"
        case 404:
            return f"{status}: Not Found"
        case 500:
            return f"{status}: Internal Server Error"
        case 503:
            return f"{status}: Service Unavailable"
        case _:
            return "Unknown Status"
        

print(http_status(200)) # OK
print(http_status(400)) # Bad Request
print(http_status(403)) # Forbidden
print(http_status(404)) # Not Found
print(http_status(500)) # Internal Server Error
print(http_status(503)) # Service Unavailable
print(http_status(205)) # Unknown Status