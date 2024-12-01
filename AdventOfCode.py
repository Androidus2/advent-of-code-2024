class AdventOfCode:
    @staticmethod
    def __d1p1(fileName):
        """
        Read the file and return the result to the first part of the first day's problem
        """
        v1 = []
        v2 = []
        with open(fileName, "r") as file:
            content = file.read()

            lines = content.split("\n")

            for line in lines:
                a, b = line.split("   ")

                a = int(a)
                b = int(b)

                v1.append(a)
                v2.append(b)

            file.close()

        v1.sort()
        v2.sort()

        sum = 0

        for i in range(len(v1)):
            sum += abs(v1[i] - v2[i])

        return sum
    
    @staticmethod
    def __d1p2(fileName):
        """
        Read the file and return the result to the second part of the first day's problem
        """
        v1 = {}
        v2 = {}
        with open(fileName, "r") as file:
            content = file.read()

            lines = content.split("\n")

            for line in lines:
                a, b = line.split("   ")
                a = int(a)
                b = int(b)
                
                if not a in v1:
                    v1[a] = 0
                if not b in v2:
                    v2[b] = 0
                
                v1[a] += 1
                v2[b] += 1

            file.close()

        sum = 0

        for num in v1.keys():
            if num in v2:
                sum += v1[num] * v2[num] * num
        
        return sum

    # Table of functions for each day and part
    __table = {
        1: {
            1: __d1p1,
            2: __d1p2
        }
    }

    @staticmethod
    def Solve(day, part, fileName):
        """
        Solve the problem for the given day and part, while reading the input from the given file
        """
        try :
            print(f"Day {day} Part {part}: {AdventOfCode.__table[day][part](fileName)}")
        except KeyError:
            print("Day or part not found")

# Usage
AdventOfCode.Solve(1, 1, "input.txt")