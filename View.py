import cmd
import matplotlib.pyplot as plt


class View(cmd.Cmd):
    def __init__(self, new_controller=None):
        cmd.Cmd.__init__(self, new_controller)
        self.my_controller = new_controller
        self.prompt = "Input:  "
        self.intro = "Console Started! Use the \"help\" command to find available commands."

    def do_quit(self, args=""):
        """
        Saves currently loaded data to be loaded on next startup and exits the interpreter

        Usage:
            quit
        """

        self.my_controller.save_data()
        print("BYE!!")
        return 1

    def default(self, line):
        """
        Incorrect commands are output back to the user with a help message.

        :param line: Incorrect commands are output back in the statement.
        return: None
        """
        print("Command not recognised enter \"help\" to see available commands ")

        print("\"" + line + "\" is not a recognised command enter \"help\" to see available commands ")

    def do_load_csv(self, args=""):
        """
        Loads data from a csv to the model so it can later be displayed
        Usage:
            load_csv args

        :param args: Full file path for .csv file you want to load.
        """

        print("Loading..")
        if args == "":
            print("This command requires a full file path to a .csv file after the command name \n load_csv [filename]")
            return 0
        self.my_controller.load_data(args)
        print("File \"" + args + "\" loaded")
        return 0

    def do_load_plain(self, args=""):
        """
        Loads data from a .txt to the model so it can later be displayed
        Values in text file must be separated by commas and each data point should be on its own line.
        Usage:
            load_plain args

        :param args: Full file path for .txt file you want to load.
        """

        print("Loading..")
        if args == "":
            print("This command needs a full file path to a .txt file after the command name \n load_plain [filename]")
            return 0
        self.my_controller.load_data(args)
        print("File \"" + args + "\" loaded")
        return 0

    def do_delete_all(self, args):
        """
        Deletes all data currently loaded into the program
        Usage:
            delete_all

        :param args: there are no arguments for this method
        """
        self.my_controller.delete_data()
        print("Data deleted!")
        return 0

    def do_display_sales(self, args):
        """
        Outputs the sales data as bar chart.
        Usage:
            display_sales

        :param args there are no arguments for this method
        """

        data = self.my_controller.get_sales_data()
        x = range(len(data))
        plt.title("Sales in NZ$")
        plt.xlabel('Employee')
        plt.ylabel('Sales')
        plt.bar(x, data)
        plt.show()
        return 0

    def do_display_weight(self, args):
        """
        Outputs the employee weight data as bar chart.
        Usage:
            display_weight_pie

        :param args there are no arguments for this method
        """
        labels = "Normal", "Overweight", "Obesity", "Underweight"
        sizes = self.my_controller.get_weight_data()
        colour = ['green', 'gold', 'orange', 'grey']
        explode = (0, 0.1, 0.1, 0)
        fig = plt.figure()
        fig.suptitle('Weight Status of Employees', fontsize=20)
        plt.pie(sizes, explode=explode, labels=labels, colors=colour, autopct='%1.1f%%', shadow=True, startangle=90)
        plt.axis('equal')
        plt.show()

    def do_display_gender(self, args):
        """
        Outputs the gender of employees as pie chart.
        Usage:
            display_gender

        :param args there are no arguments for this method
        """
        data = self.my_controller.get_gender_data()
        labels = "Male", "Female"
        colour = ['lightblue', 'darkred']
        if data[0] > data[1]:
            explode = (0, 0.1)
        else:
            explode = (0.1, 0)
        figure = plt.figure()
        figure.suptitle('Male to Female Ratio of Employment', fontsize=20)
        plt.pie(data, explode=explode, labels=labels, colors=colour, autopct='%1.1f%%', shadow=True, startangle=90)
        plt.axis('equal')
        plt.show()

