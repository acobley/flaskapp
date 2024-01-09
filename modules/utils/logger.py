# A very simple logging interface for coloured text

class cmd_color:
    # Colour SRC - https://pkg.go.dev/github.com/whitedevops/colors - 09/01/2024
	BLACK       = "\033[30m"
	RED         = "\033[31m"
	GREEEN      = "\033[32m"
	YELLOW      = "\033[33m"
	MAGENTA     = "\033[35m"
	CYAN        = "\033[36m"
	WHITE       = "\033[97m"


def LOG_ERROR(data):
    print(cmd_color.RED + data + cmd_color.WHITE)
    
def LOG_WARNING(data):
    print(cmd_color.YELLOW + data + cmd_color.WHITE)
    
def LOG_SUCCESS(data):
    print(cmd_color.GREEEN + data + cmd_color.WHITE)
    
def LOG_MESSAGE(data):
    print(cmd_color.CYAN + data + cmd_color.WHITE)
    
def LOG_TRACE(data):
    print(cmd_color.MAGENTA + data + cmd_color.WHITE)