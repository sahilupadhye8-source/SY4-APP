def report_header(func):
    def wrapper(self):
        print("=",40)
        print("          Report Generator")
        print("=",40)

        function(self)

        print("=",40)
        print("           End of Report")
        print("=",40)
    return wrapper

class Report:
    def __init__(self,title,section):
        self.title= title
        self.section=section

    @classmethod
    def sample_report(cls):
        title="student performance report"
        section=[
            "name:sahil",
            "rollno:100"
            "python:A"
            "DELD:FR"
            "attendance:10%"
        ]
        return cls(title,section)

    @report_header
    def display(self):

        print("title:",self.title) 
        print()

        for item in self.section:
            print(item)

def __str__(self):
    return f"Report title:{self.title}"
def __len__(self):
    return len(self.section)

report=Report.sample_report()
print(report)
print("total section:",len(report))

report.display()


                                                                            