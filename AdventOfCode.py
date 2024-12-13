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
    
    @staticmethod
    def __d3p1(fileName):
        """
        Read the file and return the result to the first part of the third day's problem
        """
        sum = 0
        with open(fileName, 'r') as file:
            content = file.read()

            lines = content.split('\n')

            for line in lines:
                start = 0
                
                while True:
                    ind = line.find('mul(', start)
                    if ind == -1:
                        break

                    comma = line.find(',', ind)
                    if comma == -1:
                        break

                    end = line.find(')', comma)
                    if end == -1:
                        break

                    start = ind + 1

                    aStr = line[ind + 4:comma]
                    bStr = line[comma + 1:end]

                    if aStr.isdigit() and bStr.isdigit():
                        a = int(line[ind + 4:comma])
                        b = int(line[comma + 1:end])

                        sum += a * b
        
        return sum

    @staticmethod
    def __d3p2(fileName):
        """
        Read the file and return the result to the second part of the third day's problem
        """
        sum = 0
        with open(fileName, 'r') as file:
            content = file.read()

            lines = content.split('\n')

            shouldDo = True

            for line in lines:
                start = 0
                
                while True:
                    ind = line.find('mul(', start)
                    if ind == -1:
                        break

                    
                    lastDoIndex = line.find('do()', start, ind)
                    while lastDoIndex != -1 and line.find('do()', lastDoIndex + 4, ind) != -1:
                        lastDoIndex = line.find('do()', lastDoIndex + 4, ind)
                    lastDontIndex = line.find('don\'t()', start, ind)
                    while lastDontIndex != -1 and line.find('don\'t()', lastDontIndex + 7, ind) != -1:
                        lastDontIndex = line.find('don\'t()', lastDontIndex + 7, ind)
                    
                    if lastDoIndex > lastDontIndex:
                        shouldDo = True
                    elif lastDoIndex < lastDontIndex:
                        shouldDo = False


                    comma = line.find(',', ind)
                    if comma == -1:
                        break

                    end = line.find(')', comma)
                    if end == -1:
                        break

                    start = ind + 1

                    aStr = line[ind + 4:comma]
                    bStr = line[comma + 1:end]

                    if aStr.isdigit() and bStr.isdigit() and shouldDo:
                        a = int(line[ind + 4:comma])
                        b = int(line[comma + 1:end])

                        sum += a * b
        
        return sum

    @staticmethod
    def __d4p1(fileName):
        """
        Read the file and return the result to the first part of the fourth day's problem
        """

        cnt = 0

        with open(fileName, 'r') as file:
            content = file.read()
            lines = content.split('\n')

            # search for horizontal
            for line in lines:
                ind = 0
                while line.find('XMAS', ind) != -1:
                    cnt += 1
                    ind = line.find('XMAS', ind) + 1
                
                ind = 0
                while line.find('SAMX', ind) != -1:
                    cnt += 1
                    ind = line.find('SAMX', ind) + 1

            # search for vertical
            for i in range(len(lines) - 3):
                for j in range(len(lines[i])):
                    if lines[i][j] == 'X' and lines[i + 1][j] == 'M' and lines[i + 2][j] == 'A' and lines[i + 3][j] == 'S':
                        cnt += 1
                    if lines[i][j] == 'S' and lines[i + 1][j] == 'A' and lines[i + 2][j] == 'M' and lines[i + 3][j] == 'X':
                        cnt += 1

            # search for first diagonal
            for i in range(len(lines) - 3):
                for j in range(len(lines[i]) - 3):
                    if lines[i][j] == 'X' and lines[i + 1][j + 1] == 'M' and lines[i + 2][j + 2] == 'A' and lines[i + 3][j + 3] == 'S':
                        cnt += 1
                    if lines[i][j] == 'S' and lines[i + 1][j + 1] == 'A' and lines[i + 2][j + 2] == 'M' and lines[i + 3][j + 3] == 'X':
                        cnt += 1
            
            # search for second diagonal
            for i in range(len(lines) - 3):
                for j in range(3, len(lines[i])):
                    if lines[i][j] == 'X' and lines[i + 1][j - 1] == 'M' and lines[i + 2][j - 2] == 'A' and lines[i + 3][j - 3] == 'S':
                        cnt += 1
                    if lines[i][j] == 'S' and lines[i + 1][j - 1] == 'A' and lines[i + 2][j - 2] == 'M' and lines[i + 3][j - 3] == 'X':
                        cnt += 1
            
        return cnt

    @staticmethod
    def __d4p2(fileName):
        """
        Read the file and return the result to the second part of the fourth day's problem
        """
        cnt = 0

        with open(fileName, 'r') as file:
            content = file.read()
            lines = content.split('\n')

            for i in range(len(lines) - 2):
                for j in range(len(lines[i]) - 2):
                    if (lines[i + 1][j + 1] == 'A' and ( (lines[i][j] == 'M' and lines[i + 2][j + 2] == 'S') or (lines[i][j] == 'S' and lines[i + 2][j + 2] == 'M'))) and \
                        ((lines[i + 2][j] == 'M' and lines[i][j + 2] == 'S') or (lines[i + 2][j] == 'S' and lines[i][j + 2] == 'M')):
                        cnt += 1
        
        return cnt

    @staticmethod
    def __d5p1(fileName):
        """
        Read the file and return the result to the first part of the fifth day's problem
        """

        req = {}
        suma = 0

        with open(fileName, 'r') as file:
            content = file.read()
            lines = content.split('\n')
            inReqs = True

            for line in lines:
                if line == '':
                    inReqs = False
                    continue

                if inReqs:
                    reqs = line.split('|')
                    if not reqs[1] in req:
                        req[reqs[1]] = {}
                    req[reqs[1]][reqs[0]] = True
                else:
                    nums = line.split(',')

                    ok = True

                    for i in range(len(nums)):
                        for j in range(i):
                            if nums[j] in req and nums[i] in req[nums[j]]:
                                ok = False
                    
                    if ok:
                        suma += int(nums[len(nums) // 2])
        
        return suma


    @staticmethod
    def __d5p2(fileName):
        """
        Read the file and return the result to the second part of the fifth day's problem
        """

        req = {}
        suma = 0

        with open(fileName, 'r') as file:
            content = file.read()
            lines = content.split('\n')
            inReqs = True

            for line in lines:
                if line == '':
                    inReqs = False
                    continue

                if inReqs:
                    reqs = line.split('|')
                    if not reqs[1] in req:
                        req[reqs[1]] = {}
                    req[reqs[1]][reqs[0]] = True
                else:
                    nums = line.split(',')

                    ok = True
                    isSorted = True

                    while True:
                        isSorted = True
                        for i in range(len(nums)):
                            for j in range(i):
                                if nums[j] in req and nums[i] in req[nums[j]]:
                                    ok = False
                                    nums[i], nums[j] = nums[j], nums[i]
                                    isSorted = False
                        
                        if isSorted:
                            break

                    if not ok:
                        suma += int(nums[len(nums) // 2])
        
        return suma


    @staticmethod
    def __d6p1(fileName):
        """
        Read the file and return the result to the first part of the sixth day's problem
        """

        import sys

        sys.setrecursionlimit(10000)


        def rec(guard, mat, n, m):
            if guard[0] < 0 or guard[0] >= n or guard[1] < 0 or guard[1] >= m:
                return

            if mat[guard[0]][guard[1]] == '#':
                if guard[2] == 0:
                    guard[0] += 1
                elif guard[2] == 1:
                    guard[1] -= 1
                elif guard[2] == 2:
                    guard[0] -= 1
                else:
                    guard[1] += 1
                guard[2] = (guard[2] + 1) % 4
            else:
                mat[guard[0]][guard[1]] = 'X'

            if guard[2] == 0:
                guard[0] -= 1
            elif guard[2] == 1:
                guard[1] += 1
            elif guard[2] == 2:
                guard[0] += 1
            else:
                guard[1] -= 1

            rec(guard, mat, n, m)


        cnt = 0

        with open(fileName, 'r') as file:
            content = file.read()
            lines = content.split('\n')
            mat = []

            for line in lines:
                mat.append(list(line))

            guard = [0, 0, 0]
            n = len(mat)
            m = len(mat[0])

            for i in range(n):
                for j in range(m):
                    if mat[i][j] != '.' and mat[i][j] != '#':
                        guard[0] = i
                        guard[1] = j
                        if mat[i][j] == '^':
                            guard[2] = 0
                        elif mat[i][j] == '>':
                            guard[2] = 1
                        elif mat[i][j] == 'v':
                            guard[2] = 2
                        else:
                            guard[2] = 3
            
            rec(guard, mat, n, m)

            #print(mat)

            for i in range(n):
                for j in range(m):
                    if mat[i][j] == 'X':
                        cnt += 1
        
        return cnt
    


    @staticmethod
    def __d6p2(fileName):
        """
        Read the file and return the result to the second part of the sixth day's problem
        """

        import sys

        sys.setrecursionlimit(10000)


        def isLoop(guard, mat, n, m, viz):
            if guard[0] < 0 or guard[0] >= n or guard[1] < 0 or guard[1] >= m:
                return False

            if (guard[0], guard[1], guard[2]) in viz:
                return True
            
            viz.add((guard[0], guard[1], guard[2]))

            if mat[guard[0]][guard[1]] == '#':
                if guard[2] == 0:
                    guard[0] += 1
                elif guard[2] == 1:
                    guard[1] -= 1
                elif guard[2] == 2:
                    guard[0] -= 1
                else:
                    guard[1] += 1
                guard[2] = (guard[2] + 1) % 4
            else:
                mat[guard[0]][guard[1]] = 'X'

            if guard[2] == 0:
                guard[0] -= 1
            elif guard[2] == 1:
                guard[1] += 1
            elif guard[2] == 2:
                guard[0] += 1
            else:
                guard[1] -= 1

            return isLoop(guard, mat, n, m, viz)


        cnt = 0

        with open(fileName, 'r') as file:
            content = file.read()
            lines = content.split('\n')
            mat = []

            for line in lines:
                mat.append(list(line))

            guard = [0, 0, 0]
            n = len(mat)
            m = len(mat[0])

            for i in range(n):
                for j in range(m):
                    if mat[i][j] != '.' and mat[i][j] != '#':
                        guard[0] = i
                        guard[1] = j
                        if mat[i][j] == '^':
                            guard[2] = 0
                        elif mat[i][j] == '>':
                            guard[2] = 1
                        elif mat[i][j] == 'v':
                            guard[2] = 2
                        else:
                            guard[2] = 3

            #print(mat)
            print(n, m)
            
            for i in range(n):
                for j in range(m):
                    if mat[i][j] == '.':
                        cMat = [x[:] for x in mat]
                        cGuard = guard[:]
                        
                        cMat[i][j] = '#'

                        viz = set()
                        if isLoop(cGuard, cMat, n, m, viz):
                            cnt += 1
        
        return cnt
            


    @staticmethod
    def __d7p1(fileName):
        """
        Read the file and return the result to the first part of the seventh day's problem
        """


        def eval(nums, ops):
            if len(nums) == 0:
                return 0
            ret = nums[0]

            for i in range(len(ops)):
                if ops[i] == '+':
                    ret += nums[i + 1]
                else:
                    ret *= nums[i + 1]
            
            return ret


        def backt(nums, ops, ind, target):
            if ind == len(ops):
                rez = eval(nums, ops)
                if rez == target:
                    return True
                return False
            
            ret = False

            ops[ind] = '+'
            ret = ret or backt(nums, ops, ind + 1, target)
            ops[ind] = '*'
            ret = ret or backt(nums, ops, ind + 1, target)

            return ret


        sum = 0

        with open(fileName, 'r') as file:
            content = file.read()
            lines = content.split('\n')

            for line in lines:
                spl = line.split(':')
                target = int(spl[0])

                nums = [int(x) for x in spl[1].split() if x.isdigit()]
                ops = [''] * (len(nums) - 1)

                if backt(nums, ops, 0, target):
                    sum += target
        
        return sum
    


    @staticmethod
    def __d7p2(fileName):
        """
        Read the file and return the result to the second part of the seventh day's problem
        """


        def eval(nums, ops):
            if len(nums) == 0:
                return 0
            ret = nums[0]

            for i in range(len(ops)):
                if ops[i] == '+':
                    ret += nums[i + 1]
                elif ops[i] == '*':
                    ret *= nums[i + 1]
                else:
                    noDigits = 0
                    cn = nums[i + 1]
                    while cn > 0:
                        noDigits += 1
                        cn //= 10
                    
                    ret = ret * (10 ** noDigits) + nums[i + 1]
            
            return ret


        def backt(nums, ops, ind, target):
            if ind == len(ops):
                rez = eval(nums, ops)
                if rez == target:
                    return True
                return False
            
            ret = False

            ops[ind] = '+'
            ret = ret or backt(nums, ops, ind + 1, target)
            ops[ind] = '*'
            ret = ret or backt(nums, ops, ind + 1, target)
            ops[ind] = '||'
            ret = ret or backt(nums, ops, ind + 1, target)

            return ret


        sum = 0

        with open(fileName, 'r') as file:
            content = file.read()
            lines = content.split('\n')

            for line in lines:
                spl = line.split(':')
                target = int(spl[0])

                nums = [int(x) for x in spl[1].split() if x.isdigit()]
                ops = [''] * (len(nums) - 1)

                if backt(nums, ops, 0, target):
                    sum += target
        
        return sum



    @staticmethod
    def __d8p1(fileName):
        """
        Read the file and return the result to the first part of the eighth day's problem
        """

        cnt = 0

        with open(fileName, 'r') as file:
            content = file.read()
            lines = content.split('\n')

            dic = {}
            antinodes = set()

            print(len(lines), len(lines[0]))

            for i in range(len(lines)):
                for j in range(len(lines[i])):
                    if lines[i][j] != '.':
                        if not lines[i][j] in dic:
                            dic[lines[i][j]] = []
                        dic[lines[i][j]].append((i, j))
            
            for key in dic.keys():
                for i in range(len(dic[key])):
                    for j in range(i + 1, len(dic[key])):
                        pos1 = dic[key][i]
                        pos2 = dic[key][j]

                        if pos1[1] <= pos2[1]:
                            newPos1 = (pos1[0] - abs(pos1[0] - pos2[0]), pos1[1] - abs(pos1[1] - pos2[1]))
                            newPos2 = (pos2[0] + abs(pos1[0] - pos2[0]), pos2[1] + abs(pos1[1] - pos2[1]))
                        else:
                            newPos1 = (pos1[0] - abs(pos1[0] - pos2[0]), pos1[1] + abs(pos1[1] - pos2[1]))
                            newPos2 = (pos2[0] + abs(pos1[0] - pos2[0]), pos2[1] - abs(pos1[1] - pos2[1]))

                        if newPos1[0] >= 0 and newPos1[0] < len(lines) and newPos1[1] >= 0 and newPos1[1] < len(lines[0]) and newPos1 not in antinodes:
                            antinodes.add(newPos1)
                        if newPos2[0] >= 0 and newPos2[0] < len(lines) and newPos2[1] >= 0 and newPos2[1] < len(lines[0]) and newPos2 not in antinodes:
                            antinodes.add(newPos2)
            
            cnt = len(antinodes)

        
        return cnt



    @staticmethod
    def __d8p2(fileName):
        """
        Read the file and return the result to the second part of the eighth day's problem
        """

        cnt = 0

        with open(fileName, 'r') as file:
            content = file.read()
            lines = content.split('\n')

            dic = {}
            antinodes = set()
            verticals = set()

            #print(len(lines), len(lines[0]))

            for i in range(len(lines)):
                for j in range(len(lines[i])):
                    if lines[i][j] != '.':
                        if not lines[i][j] in dic:
                            dic[lines[i][j]] = []
                        dic[lines[i][j]].append((i, j))
            
            for key in dic.keys():
                for i in range(len(dic[key])):
                    for j in range(i + 1, len(dic[key])):
                        pos1 = dic[key][i]
                        pos2 = dic[key][j]
                        
                        if pos1[1] == pos2[1]:
                            #print(pos1, pos2)
                            verticals.add((pos1[0]))
                        else:
                            a = (pos2[0] - pos1[0]) / (pos2[1] - pos1[1])
                            b = pos1[0] - a * pos1[1]
                            antinodes.add((a, b))


            
            mat = []
            for line in lines:
                mat.append(list(line))
                
            for i in range(len(mat)):
                pr = ''
                for j in range(len(mat[i])):
                    
                    ok = False

                    for f in antinodes:
                        a = f[0]
                        b = f[1]
                        if abs(a * j + b - i) < 1e-9:
                            ok = True
                            cnt += 1

                            if mat[i][j] == '.':
                                mat[i][j] = '#'

                            break
                    
                    if j in verticals and not ok:
                        cnt += 1

                        if mat[i][j] == '.':
                            mat[i][j] = '#'

                    pr += mat[i][j]
                #print(pr)

        
        return cnt



    @staticmethod
    def __d9p1(fileName):
        """
        Read the file and return the result to the first part of the ninth day's problem
        """

        sum = 0

        with open(fileName, 'r') as file:
            content = file.read()

            isSpace = False
            uncompressed = []
            curID = 0
            for ch in content:
                cnt = int(ch)
                if isSpace:
                    uncompressed.extend(['.'] * cnt)
                else:
                    uncompressed.extend([curID] * cnt)
                    curID += 1
                
                isSpace = not isSpace
            
            for i in range(len(uncompressed) - 1, -1, -1):
                if uncompressed[i] != '.':
                    for j in range(i):
                        if uncompressed[j] == '.':
                            uncompressed[j], uncompressed[i] = uncompressed[i], uncompressed[j]
            
            for i in range(len(uncompressed)):
                if uncompressed[i] != '.':
                    sum += i * uncompressed[i]
        
        return sum



    @staticmethod
    def __d9p2(fileName):
        """
        Read the file and return the result to the second part of the ninth day's problem
        """

        sum = 0

        with open(fileName, 'r') as file:
            content = file.read()

            isSpace = False
            uncompressed = []
            spaces = []
            files = []
            maxLen = 0
            curID = 0
            for ch in content:
                cnt = int(ch)
                if isSpace:
                    spaces.append([maxLen, cnt])
                else:
                    files.append([maxLen, cnt])
                    curID += 1
                
                maxLen += cnt
                isSpace = not isSpace
            
            for i in range(len(files) - 1, -1, -1):
                for j in range(len(spaces)):
                    if spaces[j][0] < files[i][0] and spaces[j][1] >= files[i][1]:
                        spaces[j][1] -= files[i][1]
                        files[i][0] = spaces[j][0]
                        spaces[j][0] += files[i][1]
                        break
            
            uncompressed = ['.'] * maxLen

            for i in range(len(files)):
                for j in range(files[i][1]):
                    uncompressed[files[i][0] + j] = i
            
            for i in range(len(uncompressed)):
                if uncompressed[i] != '.':
                    sum += i * uncompressed[i]
        
        return sum



    @staticmethod
    def __d10p1(fileName):
        """
        Read the file and return the result to the first part of the tenth day's problem
        """

        sum = 0
        with open(fileName, 'r') as file:
            content = file.read()
            lines = content.split('\n')

            mat = []
            zeroes = []

            for line in lines:
                v = []
                for ch in line:
                    v.append(int(ch))

                mat.append(v)

                for i, num in enumerate(mat[-1]):
                    if num == 0:
                        zeroes.append((len(mat) - 1, i))
            
            from collections import deque

            q = deque()

            dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            n, m = len(mat), len(mat[0])

            for zero in zeroes:
                q.append(zero)

                found = set()

                while len(q) > 0:
                    fr = q.popleft()

                    if mat[fr[0]][fr[1]] == 9:
                        if fr not in found:
                            found.add(fr)
                            sum += 1
                        continue
                    
                    for d in dir:
                        newFr = (fr[0] + d[0], fr[1] + d[1])

                        if newFr[0] >= 0 and newFr[0] < n and newFr[1] >= 0 and newFr[1] < m and mat[newFr[0]][newFr[1]] == mat[fr[0]][fr[1]] + 1:
                            q.append(newFr)
        
        return sum
    



    @staticmethod
    def __d10p2(fileName):
        """
        Read the file and return the result to the second part of the tenth day's problem
        """

        sum = 0
        with open(fileName, 'r') as file:
            content = file.read()
            lines = content.split('\n')

            mat = []
            zeroes = []

            for line in lines:
                v = []
                for ch in line:
                    v.append(int(ch))

                mat.append(v)

                for i, num in enumerate(mat[-1]):
                    if num == 0:
                        zeroes.append((len(mat) - 1, i))
            
            from collections import deque

            q = deque()

            dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            n, m = len(mat), len(mat[0])

            for zero in zeroes:
                q.append(zero)

                while len(q) > 0:
                    fr = q.popleft()

                    if mat[fr[0]][fr[1]] == 9:
                        sum += 1
                        continue
                    
                    for d in dir:
                        newFr = (fr[0] + d[0], fr[1] + d[1])

                        if newFr[0] >= 0 and newFr[0] < n and newFr[1] >= 0 and newFr[1] < m and mat[newFr[0]][newFr[1]] == mat[fr[0]][fr[1]] + 1:
                            q.append(newFr)
        
        return sum
                    
            

    
    @staticmethod
    def __d11p1(fileName):
        """
        Read the file and return the result to the first part of the eleventh day's problem
        """

        from collections import deque

        def solve(queue, solved, blink):
            if len(queue) == 0 or blink == 0:
                return 0
            
            fr = queue.popleft()

            if fr not in solved:
                solved[fr] = {}

            if blink == 1:
                solved[fr][blink] = 1

            if blink in solved[fr]:
                return solved[fr][blink]
                
            if fr == 0:
                queue.appendleft(1)
                solved[fr][blink] = solve(queue, solved, blink - 1)
            else:
                numCif = 0
                cn = fr
                while cn > 0:
                    numCif += 1
                    cn //= 10
                
                if numCif % 2 == 0:
                    # split in two
                    half = 10 ** (numCif // 2)
                    queue.appendleft(fr // half)
                    queue.appendleft(fr % half)
                    solved[fr][blink] = solve(queue, solved, blink - 1) + solve(queue, solved, blink - 1)
                else:
                    queue.appendleft(fr * 2024)
                    solved[fr][blink] = solve(queue, solved, blink - 1)

            return solved[fr][blink]

        cnt = 0

        with open(fileName, 'r') as file:
            nums = [int(x) for x in file.read().split()]

            blinks = 26

            solved = {}
            q = deque()

            for num in nums:
                q.append(num)
                cnt += solve(q, solved, blinks)
        
        return cnt



    @staticmethod
    def __d11p2(fileName):
        """
        Read the file and return the result to the second part of the eleventh day's problem
        """

        from collections import deque
        import sys

        sys.setrecursionlimit(1000000)

        def solve(queue, solved, blink):
            if len(queue) == 0 or blink == 0:
                return 0
            
            fr = queue.popleft()

            if fr not in solved:
                solved[fr] = {}

            if blink == 1:
                solved[fr][blink] = 1

            if blink in solved[fr]:
                return solved[fr][blink]
                
            if fr == 0:
                queue.appendleft(1)
                solved[fr][blink] = solve(queue, solved, blink - 1)
            else:
                numCif = 0
                cn = fr
                while cn > 0:
                    numCif += 1
                    cn //= 10
                
                if numCif % 2 == 0:
                    # split in two
                    half = 10 ** (numCif // 2)
                    queue.appendleft(fr // half)
                    queue.appendleft(fr % half)
                    solved[fr][blink] = solve(queue, solved, blink - 1) + solve(queue, solved, blink - 1)
                else:
                    queue.appendleft(fr * 2024)
                    solved[fr][blink] = solve(queue, solved, blink - 1)

            return solved[fr][blink]

        cnt = 0

        with open(fileName, 'r') as file:
            nums = [int(x) for x in file.read().split()]

            blinks = 76

            solved = {}
            q = deque()

            for num in nums:
                q.append(num)
                cnt += solve(q, solved, blinks)
        
        return cnt



    @staticmethod
    def __d12p1(fileName):
        """
        Read the file and return the result to the first part of the twelfth day's problem
        """

        def inbounds(x, y, n, m):
            return x >= 0 and x < n and y >= 0 and y < m

        def solve(x, y, n, m, mat, viz, dir):
            if not inbounds(x, y, n, m) or viz[x][y]:
                return (0, 0)
            
            viz[x][y] = True
            
            area = 0
            perimeter = 0

            for d in dir:
                if inbounds(x + d[0], y + d[1], n, m) and mat[x + d[0]][y + d[1]] == mat[x][y] and not viz[x + d[0]][y + d[1]]:
                    a, b = solve(x + d[0], y + d[1], n, m, mat, viz, dir)
                    area += a
                    perimeter += b
                elif not inbounds(x + d[0], y + d[1], n, m) or mat[x + d[0]][y + d[1]] != mat[x][y]:
                    perimeter += 1
            
            return (area + 1, perimeter)

        sum = 0

        with open(fileName, 'r') as file:
            content = file.read()
            
            mat = []
            viz = []
            dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]

            for line in content.split('\n'):
                mat.append(list(line))
                viz.append([False] * len(line))


            n = len(mat)
            m = len(mat[0])

            for i in range(n):
                for j in range(m):
                    if not viz[i][j]:
                        a, b = solve(i, j, n, m, mat, viz, dir)
                        sum += a * b

                        #print(mat[i][j], a, b)
        
        return sum
    


    @staticmethod
    def __d12p2(fileName):
        """
        Read the file and return the result to the second part of the twelfth day's problem
        """

        def inbounds(x, y, n, m):
            return x >= 0 and x < n and y >= 0 and y < m
        
        def countCorners(x, y, n, m, mat, viz, dir):
            # 16 possible states
            corners = 0
            neighbors = 0

            for d in dir:
                if inbounds(x + d[0], y + d[1], n, m) and mat[x + d[0]][y + d[1]] == mat[x][y]:
                    neighbors += 1

            # Case 1, no neighbors
            if neighbors == 0:
                corners += 4
            # Case 2, one neighbor
            elif neighbors == 1:
                corners += 2
            # Case 3, two neighbors
            elif neighbors == 2:
                # Case 3.1, neighbors are opposite
                if (inbounds(x + 1, y, n, m) and mat[x + 1][y] == mat[x][y]) and (inbounds(x - 1, y, n, m) and mat[x - 1][y] == mat[x][y]) or \
                    (inbounds(x, y + 1, n, m) and mat[x][y + 1] == mat[x][y]) and (inbounds(x, y - 1, n, m) and mat[x][y - 1] == mat[x][y]):
                    corners += 0
                # Case 3.2, neighbors are adjacent
                else:
                    corners += 1
                    hasInner = False
                    # Check if there is also a neighbor inside the 2 neighbors
                    for i in range(len(dir)):
                        if inbounds(x + dir[i][0], y + dir[i][1], n, m) and mat[x + dir[i][0]][y + dir[i][1]] == mat[x][y] and \
                            inbounds(x + dir[i - 1][0], y + dir[i - 1][1], n, m) and mat[x + dir[i - 1][0]][y + dir[i - 1][1]] == mat[x][y] and \
                            inbounds(x + dir[i - 1][0] + dir[i][0], y + dir[i - 1][1] + dir[i][1], n, m) and mat[x + dir[i - 1][0] + dir[i][0]][y + dir[i - 1][1] + dir[i][1]] == mat[x][y]:
                            hasInner = True
                            break
                    #print(x, y, hasInner)
                    if not hasInner:
                        corners += 1
            # Case 4, three neighbors or four neighbors
            else:
                inners = 0
                # Check how many inner neighbors there are
                for i in range(len(dir)):
                    if inbounds(x + dir[i][0], y + dir[i][1], n, m) and mat[x + dir[i][0]][y + dir[i][1]] == mat[x][y] and \
                        inbounds(x + dir[i - 1][0], y + dir[i - 1][1], n, m) and mat[x + dir[i - 1][0]][y + dir[i - 1][1]] == mat[x][y] and \
                        inbounds(x + dir[i - 1][0] + dir[i][0], y + dir[i - 1][1] + dir[i][1], n, m) and mat[x + dir[i - 1][0] + dir[i][0]][y + dir[i - 1][1] + dir[i][1]] == mat[x][y]:
                        inners += 1
                
                #print(x, y, inners, neighbors)

                if neighbors == 3:
                    corners += 2 - inners
                else:
                    corners += 4 - inners
            
            return corners



        def solve(x, y, n, m, mat, viz, dir):
            if not inbounds(x, y, n, m) or viz[x][y]:
                return (0, 0)
            
            viz[x][y] = True
            
            area = 0
            corners = 0

            for d in dir:
                if inbounds(x + d[0], y + d[1], n, m) and mat[x + d[0]][y + d[1]] == mat[x][y] and not viz[x + d[0]][y + d[1]]:
                    a, b = solve(x + d[0], y + d[1], n, m, mat, viz, dir)
                    area += a
                    corners += b
            
            corners += countCorners(x, y, n, m, mat, viz, dir)
            
            return (area + 1, corners)

        sum = 0

        with open(fileName, 'r') as file:
            content = file.read()
            
            mat = []
            viz = []
            dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]

            for line in content.split('\n'):
                mat.append(list(line))
                viz.append([False] * len(line))


            n = len(mat)
            m = len(mat[0])

            for i in range(n):
                for j in range(m):
                    if not viz[i][j]:
                        a, b = solve(i, j, n, m, mat, viz, dir)
                        sum += a * b

                        #print(mat[i][j], a, b)
        
        return sum



    @staticmethod
    def __d13p1(fileName):
        """
        Read the file and return the result to the first part of the thirteenth day's problem
        """

        sum = 0

        with open(fileName, 'r') as file:
            content = file.read()
            lineType = 0

            eqs = []
            currentEq = []

            for line in content.split('\n'):
                if lineType == 0 or lineType == 1:
                    tok = line.split()
                    currentEq.append((int(tok[2][2:-1]), int(tok[3][2:])))
                elif lineType == 2:
                    tok = line.split('=')
                    currentEq.append((int(tok[1][:-3]), int(tok[2])))
                    eqs.append(currentEq)
                    currentEq = []
                
                lineType = (lineType + 1) % 4
            
            for eq in eqs:
                minSol = -1
                for i in range(100):
                    for j in range(100):
                        if eq[0][0] * i + eq[1][0] * j == eq[2][0] and eq[0][1] * i + eq[1][1] * j == eq[2][1]:
                            #print('Found', i, j)
                            if minSol == -1 or minSol > 3 * i + j:
                                minSol = 3 * i + j
                if minSol != -1:
                    sum += minSol
        
        return sum
    


    @staticmethod
    def __d13p2(fileName):
        """
        Read the file and return the result to the second part of the thirteenth day's problem
        """

        def gcd(a, b):
            if b == 0:
                return a
            return gcd(b, a % b)

        sum = 0

        with open(fileName, 'r') as file:
            content = file.read()
            lineType = 0

            eqs = []
            currentEq = []

            for line in content.split('\n'):
                if lineType == 0 or lineType == 1:
                    tok = line.split()
                    currentEq.append((int(tok[2][2:-1]), int(tok[3][2:])))
                elif lineType == 2:
                    tok = line.split('=')
                    currentEq.append((int(tok[1][:-3]) + 10000000000000, int(tok[2]) + 10000000000000))
                    eqs.append(currentEq)
                    currentEq = []
                
                lineType = (lineType + 1) % 4
            
            for eq in eqs:
                # eq[0][0] * x + eq[1][0] * y = eq[2][0]
                # eq[0][1] * x + eq[1][1] * y = eq[2][1]

                xLCM = eq[0][0] * eq[0][1] // gcd(eq[0][0], eq[0][1])
                mult1X = xLCM // eq[0][0]
                mult2X = xLCM // eq[0][1]

                mult1Y = eq[1][0] * mult1X
                mult2Y = eq[1][1] * mult2X

                mult1Total = eq[2][0] * mult1X
                mult2Total = eq[2][1] * mult2X

                multTotalDiff = mult1Total - mult2Total
                multYDiff = mult1Y - mult2Y

                y = multTotalDiff // multYDiff

                totalForX = eq[2][0] - eq[1][0] * y
                x = totalForX // eq[0][0]

                if eq[0][0] * x + eq[1][0] * y == eq[2][0] and eq[0][1] * x + eq[1][1] * y == eq[2][1]:
                    sum += 3 * x + y
        
        return sum




    # Table of functions for each day and part
    __table = {
        1: {
            1: __d1p1,
            2: __d1p2
        },
        2: {
            1: __d2p1,
            2: __d2p2
        },
        3: {
            1: __d3p1,
            2: __d3p2
        },
        4: {
            1: __d4p1,
            2: __d4p2
        },
        5: {
            1: __d5p1,
            2: __d5p2
        },
        6: {
            1: __d6p1,
            2: __d6p2
        },
        7: {
            1: __d7p1,
            2: __d7p2
        },
        8: {
            1: __d8p1,
            2: __d8p2
        },
        9: {
            1: __d9p1,
            2: __d9p2
        },
        10: {
            1: __d10p1,
            2: __d10p2
        },
        11: {
            1: __d11p1,
            2: __d11p2
        },
        12: {
            1: __d12p1,
            2: __d12p2
        },
        13: {
            1: __d13p1,
            2: __d13p2
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
AdventOfCode.Solve(13, 2, "Inputs/Day13/p13.txt")