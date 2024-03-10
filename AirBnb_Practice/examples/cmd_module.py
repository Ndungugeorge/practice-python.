import cmd 
class command(cmd.Cmd):
    prompt = "console "
    """Simple command line interpreter"""
    def do_greet(self,line):
        
        """prints my name"""
        print("hello George")
    def do_quit(self, line):
        
        return True
    do_exit = do_quit
    def do_EOF(self, line):
        print()
        return True
    def default(self, line: str):
        print("UNknown command: {}".format(line))
    def help_quite(self, line):
        print("This exits the prompt")
    


if __name__ == "__main__":
    command().cmdloop()