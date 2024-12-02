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

    @staticmethod
    def __d2p1(fileName):
        """
        Read the file and return the result to the first part of the second day's problem
        """

        cnt = 0

        with open(fileName, 'r') as file:
            content = file.read()

            lines = content.split("\n")

            for line in lines:
                nums = [int(a) for a in line.split()]
                
                if len(nums) == 0:
                    continue
                    
                elif len(nums) == 1:
                    cnt += 1
                    continue
                    
                prev = nums[0]
                increasing = True
                ok = True

                if nums[0] > nums[1]:
                    increasing = False

                for i in range(1, len(nums)):
                    if abs(nums[i] - prev) < 1 or abs(nums[i] - prev) > 3:
                        ok = False
                    
                    if (nums[i] > prev) != increasing:
                        ok = False
                    
                    prev = nums[i]
                
                if ok:
                    cnt += 1
        
        return cnt

    @staticmethod
    def __d2p2(fileName):
        """
        Read the file and return the result to the second part of the second day's problem
        """
        cnt = 0

        def isValid(numbers):
            if len(numbers) < 2:
                return True
            
            prev = numbers[0]
            increasing = True
            ok = True

            if numbers[0] > numbers[1]:
                increasing = False
            
            for i in range(1, len(numbers)):
                if abs(numbers[i] - prev) < 1 or abs(numbers[i] - prev) > 3:
                    ok = False
                
                if (numbers[i] > prev) != increasing:
                    ok = False

                prev = numbers[i]
            return ok

        with open(fileName, 'r') as file:
            content = file.read()

            lines = content.split('\n')

            for line in lines:
                nums = [int(a) for a in line.split()]

                ok = isValid(nums)

                for i in range(len(nums)):
                    newNums = []
                    for j in range(len(nums)):
                        if i != j:
                            newNums.append(nums[j])
                    ok = ok or isValid(newNums)
                if ok:
                    cnt += 1
        
        return cnt
                
                

    # Table of functions for each day and part
    __table = {
        1: {
            1: __d1p1,
            2: __d1p2
        },
        2: {
            1: __d2p1,
            2: __d2p2
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
AdventOfCode.Solve(2, 2, "Inputs/Day2/p2.txt")