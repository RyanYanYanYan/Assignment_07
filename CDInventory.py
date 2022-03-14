#------------------------------------------#
# Title: CDInventory.py
# Desc: simple demonstrator for classes
# Change Log: (Who, When, What)
# Ziqi Yan, 2022-Mar-13, Created File
#------------------------------------------#

import pickle

# -- DATA -- #
strFileInput = 'mathIn.txt'
strFileOutput = 'mathOut.txt'

# -- PROCESSING -- #
class SimpleMath:
    """A collection of simple math processing functions """

    @staticmethod
    def get_sum(val1 = 0.0, val2 = 0.0):
        """Function for adding two values


        Args:
            val1: the first number to add
            val2: the second number to add


        Returns:
            A float corresponding to the sum of val1 and val2
        """
        return float(val1 + val2)

    @staticmethod
    def get_diffference(val1 = 0.0, val2 = 0.0):
        """Function for subtracting two values


        Args:
            val1: the number to subtract from
            val2: the number to subtract


        Returns:
            A float corresponding to the difference of val1 and val2
        """
        return float(val1 - val2)

    @staticmethod
    def get_product(val1 = 0.0, val2 = 0.0):
        """Function for multiplying two values


        Args:
            val1: the first number to multiply
            val2: the second number to multiply


        Returns:
            A float corresponding to the product of val1 and val2
        """
        return float(val1 * val2)

    @staticmethod
    def get_quotient(val1 = 0.0, val2 = 0.0):
        """Function for dividing two values


        Args:
            val1: the number to divide
            val2: the number to divide by


        Returns:
            A float corresponding to the quotient of val1 and val2
        """

        try:
            _ = val1/val2
        except Exception as error:
            print("divide error")
            raise error

        return float(val1 / val2)


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
        obj = pickle.load(inputFile)
        inputFile.close()

        return obj

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


# -- PRESENTATION (Input/Output) -- #
print('Basic Math script. Calculating the Sum, Difference, Product and Quotient of two numbers.')
try:
    intNumA, intNumB = IO.read_file(strFileInput)
except Exception as error:
    print("read file failed!")
    raise error
lstResults = []
lstResults.append(SimpleMath.get_sum(intNumA, intNumB))
lstResults.append(SimpleMath.get_diffference(intNumA, intNumB))
lstResults.append(SimpleMath.get_product(intNumA, intNumB))
lstResults.append(SimpleMath.get_quotient(intNumA, intNumB))
try:
    IO.write_file(strFileOutput, lstResults)
except Exception as error:
    print("write file failed!")
    raise error

