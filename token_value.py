class Token:
    def __init__(self, id, value):
        self.id = id
        self.value = value

        if self.id in ["OP", "NUM", "ID"]:
            self.token = f"{self.id}: {self.value}"
        else:
            if self.value == "(":
                self.token = "LPAR" 
            elif self.value == ")":
                self.token = "RPAR"
            elif self.value == ";":
                self.token = "SEMICOLON"
            elif self.value == "div":
                self.token = "DIV"
            elif self.value == "mod":
                self.token = "MOD"
            else:
                self.token = "error" 

    def __str__(self) -> str:
        return self.token

    