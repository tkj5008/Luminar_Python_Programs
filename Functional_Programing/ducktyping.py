class vscode:
    def compile(self):
        print("compiling using vscode")
    def execute(self):
        print("Executing using vscode")
    def debug(self):
        print("Debug using vscode")
class pycharm:
    def compile(self):
        print("compiling using pycharm")
    def execute(self):
        print("Executing using pycharm")
    def debug(self):
        print("Debug using pycharm")
class programmer:
    def coding(self,ide):
        ide.compile()
        ide.execute()
        ide.debug()
dev=programmer()
pyc=pycharm()
dev.coding(pyc)
