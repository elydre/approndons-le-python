class line:
    def __init__(self, inp: str):
        self.brut = inp
        self.type = None
        self.value = None
    
    def analyse(self):
        # parser python
        match self.brut.split(" "):
            case "for", var, "in range", end:
                self.type = "for range"
                self.value = 
            case "if":
                self.type = "if"
                self.value = "if"
            case "elif":
                self.type = "elif"
                self.value = "elif"
            case "else":
                self.type = "else"
                self.value = "else"
            case "while":
                self.type = "while"
                self.value = "while"
            case "def":
                self.type = "def"
                self.value = "def"
            case "class":
                self.type = "class"
                self.value = "class"
            case "import":
                self.type = "import"
                self.value = "import"
            case "from":
                self.type = "from"
                self.value = "from"
            case "return":
                self.type = "return"
                self.value = "return"
            case "print":
                self.type = "print"
                self.value = "print"
            case "input":
                self.type = "input"
                self.value = "input"
            case "break":
                self.type = "break"
                self.value = "break"
            case "continue":
                self.type = "continue"
                self.value = "continue"
            case "try":
                self.type = "try"
                self.value = "try"
            case "except":
                self.type = "except"
                self.value = "except"
            case "raise":
                self.type = "raise"
                self.value = "raise"
            case "pass":
                self.type = "pass"
                self.value = "pass"
            case "lambda":
                self.type = "lambda"
                self.value = "lambda"