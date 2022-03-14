import pickle
class IO:
    """A collection of the Input / Output operations """
    @staticmethod
    def read_file(fileName):
        """
        function to read in two numbers from file fileName and return these

        Args:
            fileName (string): file name to read the numbers from

        Returns:
            numA (int): first number in file fileName.
            numB (int): second number in file fileName.

        """
        inputFile = open(fileName, "rb")
        tuple = pickle.load(inputFile)
        inputFile.close()
        return tuple

    @staticmethod
    def write_file(fileName, results):
        """
        function to write the math results to file fileName

        Args:
            fileName (string): file Name to write the results to.
            results (list): The results

        Returns:
            None.

        """
        outputFile = open(fileName, "ab")
        pickle.dump(results,outputFile)
        outputFile.close()

tuple = (1,2)
IO.write_file("./mathIn.txt",tuple)

alist = IO.read_file("./mathOut.txt")
for elem in alist:
    print(elem)


