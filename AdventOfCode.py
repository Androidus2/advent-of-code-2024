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



    @staticmethod
    def __d14p1(fileName):
        """
        Read the file and return the result to the first part of the fourteenth day's problem
        """

        prod = 1

        with open(fileName, 'r') as file:
            content = file.read()

            robots = []

            for line in content.split('\n'):
                p,v = line.split()
                px,py = [int(x) for x in p.split('=')[1].split(',')]
                vx,vy = [int(x) for x in v.split('=')[1].split(',')]

                robots.append([px,py,vx,vy])

            m = 103 # 103
            n = 101 # 101
            iterations = 100

            for i in range(iterations):
                for r in robots:
                    r[0] = (r[0] + r[2] + n) % n
                    r[1] = (r[1] + r[3] + m) % m
                
            quadrants = [0] * 4

            for r in robots:
                if r[0] < n // 2 and r[1] < m // 2:
                    quadrants[0] += 1
                elif r[0] < n // 2 and r[1] > m // 2:
                    quadrants[1] += 1
                elif r[0] > n // 2 and r[1] < m // 2:
                    quadrants[2] += 1
                elif r[0] > n // 2 and r[1] > m // 2:
                    quadrants[3] += 1
            
            for q in quadrants:
                prod *= q
        
        return prod
    


    @staticmethod
    def __d14p2(fileName):
        """
        Read the file and return the result to the second part of the fourteenth day's problem
        """

        # The solution looks for the longest line of robots in the matrix

        def buildMatrix(robots, n, m):
            mat = [['.'] * m for i in range(n)]

            for r in robots:
                mat[r[0]][r[1]] = '#'
            
            return mat
        
        def longestLine(mat):
            longest = 0

            for i in range(len(mat)):
                cnt = 0
                for j in range(len(mat[i])):
                    if mat[i][j] == '#':
                        cnt += 1
                    else:
                        if cnt > longest:
                            longest = cnt
                        cnt = 0
                if cnt > longest:
                    longest = cnt
            
            # Check columns
            for j in range(len(mat[0])):
                cnt = 0
                for i in range(len(mat)):
                    if mat[i][j] == '#':
                        cnt += 1
                    else:
                        if cnt > longest:
                            longest = cnt
                        cnt = 0
                if cnt > longest:
                    longest = cnt
            
            return longest

        def printRobots(robots, n, m):
            mat = buildMatrix(robots, n, m)
            
            for line in mat:
                print(''.join(line))
            
            print()
            print()

        prod = 1

        with open(fileName, 'r') as file:
            content = file.read()

            robots = []

            for line in content.split('\n'):
                p,v = line.split()
                px,py = [int(x) for x in p.split('=')[1].split(',')]
                vx,vy = [int(x) for x in v.split('=')[1].split(',')]

                robots.append([px,py,vx,vy])

            m = 103 # 103
            n = 101 # 101
            iterations = 100000

            longest = 0
            longestIter = 0

            for i in range(iterations):
                for r in robots:
                    r[0] = (r[0] + r[2] + n) % n
                    r[1] = (r[1] + r[3] + m) % m
                
                mat = buildMatrix(robots, n, m)
                longestLineNow = longestLine(mat)

                if longestLineNow > longest:
                    longest = longestLineNow
                    longestIter = i
            
        
        return longestIter + 1



    @staticmethod
    def __d15p1(fileName):
        """
        Read the file and return the result to the first part of the fifteenth day's problem
        """

        def attemptToMove(robot, move, mp):
            dir = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}

            x = robot[0]
            y = robot[1]

            while True:
                x += dir[move][0]
                y += dir[move][1]

                if x < 0 or x >= len(mp) or y < 0 or y >= len(mp[0]):
                    break
                
                if mp[x][y] == '#':
                    return False
                
                if mp[x][y] == '.':
                    break
            
            return True

        def executeMove(robot, move, mp):
            dir = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}

            x = robot[0]
            y = robot[1]

            last = '@'
            mp[x][y] = '.'

            while True:
                x += dir[move][0]
                y += dir[move][1]

                if x < 0 or x >= len(mp) or y < 0 or y >= len(mp[0]):
                    break
                
                if mp[x][y] == '#':
                    break
                
                tmp = mp[x][y]
                mp[x][y] = last
                last = tmp

                if last == '.':
                    break
            
            robot[0] += dir[move][0]
            robot[1] += dir[move][1]
                


        sum = 0

        with open(fileName, 'r') as file:
            content = file.read()

            mp = []
            readingMap = True
            moves = []
            robot = []
            for i, line in enumerate(content.split('\n')):
                if line == '':
                    readingMap = False
                elif readingMap:
                    for j in range(len(line)):
                        if line[j] == '@':
                            robot = [i, j]
                    mp.append(list(line))
                else:
                    moves.extend(list(line))
            
            for move in moves:
                #print("Trying to move ", move)
                if attemptToMove(robot, move, mp):
                    executeMove(robot, move, mp)
                    #print('Success')
                
                #for i in range(len(mp)):
                    #print(''.join(mp[i]))
                #rint()
                #print()
            
            for i in range(len(mp)):
                #print(''.join(mp[i]))
                for j in range(len(mp[i])):
                    if mp[i][j] == 'O':
                        sum += 100 * i + j
        
        return sum
    


    @staticmethod
    def __d15p2(fileName):
        """
        Read the file and return the result to the second part of the fifteenth day's problem
        """

        import sys
        sys.setrecursionlimit(1000000)

        def attemptToMove(robot, move, mp):
            dir = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}

            x = robot[0]
            y = robot[1]

            x += dir[move][0]
            y += dir[move][1]
            
            if mp[x][y] == '#':
                return False
            
            if mp[x][y] == '[':
                return attemptToMove([x, y], move, mp) and (move == '>' or move == '<' or attemptToMove([x, y + 1], move, mp))
            elif mp[x][y] == ']':
                return attemptToMove([x, y], move, mp) and (move == '>' or move == '<' or attemptToMove([x, y - 1], move, mp))
            
            return True

        def executeMove(robot, move, mp):
            dir = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}

            x = robot[0]
            y = robot[1]

            last = mp[x][y]
            mp[x][y] = '.'
            
            x += dir[move][0]
            y += dir[move][1]

            if mp[x][y] == '[' and (move == '^' or move == 'v'):
                executeMove([x, y], move, mp)
                executeMove([x, y + 1], move, mp)
            elif mp[x][y] == ']' and (move == '^' or move == 'v'):
                executeMove([x, y], move, mp)
                executeMove([x, y - 1], move, mp)
            elif mp[x][y] == '[' or mp[x][y] == ']':
                executeMove([x, y], move, mp)
            
            mp[x][y] = last
            
            robot[0] += dir[move][0]
            robot[1] += dir[move][1]
                


        sum = 0

        with open(fileName, 'r') as file:
            content = file.read()

            mp = []
            readingMap = True
            moves = []
            robot = []
            for i, line in enumerate(content.split('\n')):
                if line == '':
                    readingMap = False
                elif readingMap:
                    mp.append([])
                    for j in range(len(line)):
                        if line[j] == '@':
                            robot = [i, j * 2]
                            mp[-1].extend(['@', '.'])
                        elif line[j] == '#':
                            mp[-1].extend(['#', '#'])
                        elif line[j] == 'O':
                            mp[-1].extend(['[', ']'])
                        else:
                            mp[-1].extend(['.', '.'])
                        
                else:
                    moves.extend(list(line))
            
            #for i in range(len(mp)):
                #print(''.join(mp[i]))
            
            for move in moves:
                #print("Trying to move ", move)
                if attemptToMove(robot, move, mp):
                    executeMove(robot, move, mp)
                    #print('Success')
                
                #for i in range(len(mp)):
                    #print(''.join(mp[i]))
                #print()
                #print()
            
            for i in range(len(mp)):
                #print(''.join(mp[i]))
                for j in range(len(mp[i])):
                    if mp[i][j] == '[':
                        sum += 100 * i + j
        
        return sum



    @staticmethod
    def __d16p1(fileName):
        """
        Read the file and return the result to the first part of the sixteenth day's problem
        """

        with open(fileName, 'r') as file:
            content = file.read()

            mat = []

            start = (-1, -1)
            end = (-1, -1)

            for line in content.split('\n'):
                mat.append(list(line))

                for i, ch in enumerate(line):
                    if ch == 'S':
                        start = (len(mat) - 1, i)
                    elif ch == 'E':
                        end = (len(mat) - 1, i)
            
            from collections import deque

            q = deque()

            dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]

            costs = [[[-1] * len(mat[0]) for i in range(len(mat))] for j in range(4)]

            q.append((start[0], start[1], 0, 0))

            while len(q) > 0:
                fr = q.popleft()
                #print(fr)
                
                if costs[fr[2]][fr[0]][fr[1]] == -1 or costs[fr[2]][fr[0]][fr[1]] > fr[3]:
                    costs[fr[2]][fr[0]][fr[1]] = fr[3]

                    for i, d in enumerate(dir):
                        if fr[2] == i:
                            newFr = (fr[0] + d[0], fr[1] + d[1], i, fr[3] + 1)
                        else:
                            newFr = (fr[0], fr[1], i, fr[3] + 1000)
                        
                        if newFr[0] >= 0 and newFr[0] < len(mat) and newFr[1] >= 0 and newFr[1] < len(mat[0]) and mat[newFr[0]][newFr[1]] != '#':
                            q.append(newFr)
            
            return min([costs[i][end[0]][end[1]] for i in range(4)])
        
    


    @staticmethod
    def __d16p2(fileName):
        """
        Read the file and return the result to the second part of the sixteenth day's problem
        """

        def isOnOptimalPath(fr, start, end, costs, mat, dir):
            # if we are out of bounds or we are on a wall, return False
            if fr[0] < 0 or fr[0] >= len(mat) or fr[1] < 0 or fr[1] >= len(mat[0]) or mat[fr[0]][fr[1]] == '#' or costs[fr[2]][fr[0]][fr[1]] < 0 or fr[3] < 0:
                return False
            
            if fr[3] == 0:
                if fr[0] == start[0] and fr[1] == start[1]:
                    mat[fr[0]][fr[1]] = 'O'
                    return True
                return False
            
            result = False
            
            for i, d in enumerate(dir):
                if fr[2] == i:
                    newFr = (fr[0] - d[0], fr[1] - d[1], i, fr[3] - 1)
                else:
                    newFr = (fr[0], fr[1], i, fr[3] - 1000)
                if costs[newFr[2]][newFr[0]][newFr[1]] <= fr[3]:
                    cmp = isOnOptimalPath(newFr, start, end, costs, mat, dir)
                    result = result or cmp


            if result:
                mat[fr[0]][fr[1]] = 'O'
            return result

        cnt = 0

        with open(fileName, 'r') as file:
            content = file.read()

            mat = []

            start = (-1, -1)
            end = (-1, -1)

            for line in content.split('\n'):
                mat.append(list(line))

                for i, ch in enumerate(line):
                    if ch == 'S':
                        start = (len(mat) - 1, i)
                    elif ch == 'E':
                        end = (len(mat) - 1, i)
            
            from collections import deque

            q = deque()

            dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]

            costs = [[[-1] * len(mat[0]) for i in range(len(mat))] for j in range(4)]

            q.append((start[0], start[1], 0, 0))

            while len(q) > 0:
                fr = q.popleft()
                #print(fr)
                
                if costs[fr[2]][fr[0]][fr[1]] == -1 or costs[fr[2]][fr[0]][fr[1]] > fr[3]:
                    costs[fr[2]][fr[0]][fr[1]] = fr[3]

                    for i, d in enumerate(dir):
                        if fr[2] == i:
                            newFr = (fr[0] + d[0], fr[1] + d[1], i, fr[3] + 1)
                        else:
                            newFr = (fr[0], fr[1], i, fr[3] + 1000)
                        
                        if newFr[0] >= 0 and newFr[0] < len(mat) and newFr[1] >= 0 and newFr[1] < len(mat[0]) and mat[newFr[0]][newFr[1]] != '#':
                            q.append(newFr)
            
            # reconstruct paths
            minn = min([costs[i][end[0]][end[1]] for i in range(4)])
                    

            for i in range(4):
                if costs[i][end[0]][end[1]] == minn:
                    isOnOptimalPath((end[0], end[1], i, minn), start, end, costs, mat, dir)
                
            for i in range(len(mat)):
                for j in range(len(mat[i])):
                    if mat[i][j] == 'O':
                        cnt += 1
            
        return cnt



    @staticmethod
    def __d17p1(fileName):
        """
        Read the file and return the result to the first part of the seventeenth day's problem
        """

        def comboOperand(combo, regA, regB, regC):
            if combo <= 3:
                return combo
            if combo == 4:
                return regA
            if combo == 5:
                return regB
            return regC

        ret = ""

        with open(fileName, 'r') as file:
            content = file.read()

            regA = 0
            regB = 0
            regC = 0
            ip = 0
            instructions = []

            for i, line in enumerate(content.split('\n')):
                if i == 0:
                    regA = int(line.split()[2])
                elif i == 1:
                    regB = int(line.split()[2])
                elif i == 2:
                    regC = int(line.split()[2])
                elif i == 4:
                    instructions = [int(x) for x in line.split()[1].split(',')]
            
            #print(regA, regB, regC, instructions)
            
            while ip + 1 < len(instructions):
                opcode = instructions[ip]
                operand = instructions[ip + 1]

                if opcode == 0:
                    regA = regA // (2 ** comboOperand(operand, regA, regB, regC))
                elif opcode == 1:
                    regB = regB ^ operand
                elif opcode == 2:
                    regB = comboOperand(operand, regA, regB, regC) % 8
                elif opcode == 3:
                    if regA != 0:
                        ip = operand
                        continue
                elif opcode == 4:
                    regB = regB ^ regC
                elif opcode == 5:
                    if len(ret) != 0:
                        ret += ','
                    #print(operand, regA, regB, regC)
                    ret += str(comboOperand(operand, regA, regB, regC) % 8)
                elif opcode == 6:
                    regB = regA // (2 ** comboOperand(operand, regA, regB, regC))
                else:
                    regC = regA // (2 ** comboOperand(operand, regA, regB, regC))
                
                ip += 2
        
        return ret



    @staticmethod
    def __d17p2(fileName):
        """
        Read the file and return the result to the second part of the seventeenth day's problem
        """

        solutions = []

        def solve(regA, instructions, ind):
            if ind < 0:
                solutions.append(regA)
                return True
            
            obj = instructions[ind]
            ok = False

            for add in range(8):
                newA = regA * 8 + add

                regB = add
                regB = regB ^ 2
                regC = (newA // (2 ** regB)) % 8
                regB = (regB ^ regC) % 8
                regB = (regB ^ 7) % 8

                if regB % 8 == obj:
                    if solve(newA, instructions, ind - 1):
                        ok = True
            return ok

        ret = 0

        with open(fileName, 'r') as file:
            content = file.read()

            regA = 0
            regB = 0
            regC = 0
            ip = 0
            instructions = []

            for i, line in enumerate(content.split('\n')):
                if i == 4:
                    resultToCheckFor = line.split()[1]
                    instructions = [int(x) for x in resultToCheckFor.split(',')]
            
            solve(0, instructions, len(instructions) - 1)

            ret = min(solutions)

        
        return ret




    @staticmethod
    def __d18p1(fileName):
        """
        Read the file and return the result to the first part of the eighteenth day's problem
        """

        lun = 0

        with open(fileName, 'r') as file:
            content = file.read()

            n = 71

            mat = [['.'] * n for i in range(n)]

            cnt = 0

            for line in content.split('\n'):
                cnt += 1
                a, b = [int(x) for x in line.split(',')]

                if cnt <= 1024:
                    mat[a][b] = '#'
            
            s = (0, 0)
            e = (n - 1, n - 1)

            dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]

            from collections import deque

            q = deque()

            q.append((s[0], s[1], 0))

            while len(q) > 0:
                fr = q.popleft()

                mat[fr[0]][fr[1]] = '#'

                if fr[0] == e[0] and fr[1] == e[1]:
                    lun = fr[2]
                    break
                
                for d in dir:
                    newFr = (fr[0] + d[0], fr[1] + d[1], fr[2] + 1)

                    if newFr[0] >= 0 and newFr[0] < n and newFr[1] >= 0 and newFr[1] < n and mat[newFr[0]][newFr[1]] == '.':
                        mat[newFr[0]][newFr[1]] = '#'
                        q.append(newFr)
        
        return lun
    




    @staticmethod
    def __d18p2(fileName):
        """
        Read the file and return the result to the second part of the eighteenth day's problem
        """

        lun = 0

        with open(fileName, 'r') as file:
            content = file.read()

            n = 71

            mat = [['.'] * n for i in range(n)]

            s = (0, 0)
            e = (n - 1, n - 1)

            dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]

            from collections import deque

            q = deque()

            for line in content.split('\n'):
                a, b = [int(x) for x in line.split(',')]

                for i in range(n):
                    for j in range(n):
                        if mat[i][j] == '!':
                            mat[i][j] = '.'
                
                mat[b][a] = '#'

                #for i in range(n):
                #    print(''.join(mat[i]))

                q.append((s[0], s[1], 0))

                ok = False

                while len(q) > 0:
                    fr = q.popleft()

                    if mat[fr[0]][fr[1]] == '.':
                        mat[fr[0]][fr[1]] = '!'

                    if fr[0] == e[0] and fr[1] == e[1]:
                        #print('Found ', a, b)
                        ok = True
                        break
                    
                    for d in dir:
                        newFr = (fr[0] + d[0], fr[1] + d[1], fr[2] + 1)

                        if newFr[0] >= 0 and newFr[0] < n and newFr[1] >= 0 and newFr[1] < n and mat[newFr[0]][newFr[1]] == '.':
                            mat[newFr[0]][newFr[1]] = '!'
                            q.append(newFr)
                
                if not ok:
                    lun = (a, b)
                    break
            
        
        return str(lun)[1:-1].split(', ')[0] + ',' + str(lun)[1:-1].split(', ')[1]




    @staticmethod
    def __d19p1(fileName):
        """
        Read the file and return the result to the first part of the nineteenth day's problem
        """

        def isValid(pat, found, patterns):
            if pat in found:
                return found[pat]

            if pat == '':
                return True
            
            ret = False

            for p in patterns:
                if pat.startswith(p):
                    cmp = isValid(pat[len(p):], found, patterns)
                    ret = ret or cmp
            
            found[pat] = ret
            return ret


        cnt = 0

        with open(fileName, 'r') as file:
            content = file.read()

            lines = content.split('\n')
            patterns = [pat for pat in lines[0].split(', ')]

            found = {}

            for i in range(2, len(lines)):
                if isValid(lines[i], found, patterns):
                    cnt += 1
        
        return cnt
    


    @staticmethod
    def __d19p2(fileName):
        """
        Read the file and return the result to the second part of the nineteenth day's problem
        """

        def isValid(pat, found, patterns):
            if pat in found:
                return found[pat]

            if pat == '':
                return 1
            
            ret = 0

            for p in patterns:
                if pat.startswith(p):
                    cmp = isValid(pat[len(p):], found, patterns)
                    ret = ret + cmp
            
            found[pat] = ret
            return ret


        cnt = 0

        with open(fileName, 'r') as file:
            content = file.read()

            lines = content.split('\n')
            patterns = [pat for pat in lines[0].split(', ')]

            found = {}

            for i in range(2, len(lines)):
                cnt += isValid(lines[i], found, patterns)
        
        return cnt
                



    @staticmethod
    def __d20p1(fileName):
        """
        Read the file and return the result to the first part of the twentieth day's problem
        """

        cnt = 0

        with open(fileName, 'r') as file:
            content = file.read()

            mat = []

            for line in content.split('\n'):
                mat.append(list(line))

                for i, ch in enumerate(line):
                    if ch == 'S':
                        start = (len(mat) - 1, i)
                        mat[len(mat) - 1][i] = 0
                    elif ch == 'E':
                        end = (len(mat) - 1, i)
                        mat[len(mat) - 1][i] = '.'
            
            from collections import deque

            q = deque()

            q.append((start[0], start[1], 0))

            ord = []

            dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]

            while len(q) > 0:
                fr = q.popleft()
                ord.append(fr)

                if fr[0] == end[0] and fr[1] == end[1]:
                    break
                
                for d in dir:
                    newFr = (fr[0] + d[0], fr[1] + d[1], fr[2] + 1)

                    if newFr[0] >= 0 and newFr[0] < len(mat) and newFr[1] >= 0 and newFr[1] < len(mat[0]) and mat[newFr[0]][newFr[1]] == '.':
                        mat[newFr[0]][newFr[1]] = fr[2] + 1
                        q.append(newFr)
            
            rez = {}
            
            for i in range(len(ord)):
                for j in range(len(dir)):
                    for k in range(j, len(dir)):
                        d1 = dir[j]
                        d2 = dir[k]
                        newPosition = (ord[i][0] + d1[0] + d2[0], ord[i][1] + d1[1] + d2[1])

                        if newPosition[0] >= 0 and newPosition[0] < len(mat) and newPosition[1] >= 0 and newPosition[1] < len(mat[0]):
                            if str(mat[newPosition[0]][newPosition[1]]).isdigit() and mat[newPosition[0]][newPosition[1]] >= ord[i][2]:
                                nm = mat[newPosition[0]][newPosition[1]] - ord[i][2] - 2
                                if nm not in rez:
                                    rez[nm] = 0
                                rez[nm] += 1
            
            #for i in range(len(mat)):
            #    print(''.join([str(x) for x in mat[i]]))

            for k in rez:

                if k >= 100:
                    #print(k, rez[k])
                    cnt += rez[k]
        
        return cnt
    



    @staticmethod
    def __d20p2(fileName):
        """
        Read the file and return the result to the second part of the twentieth day's problem
        """

        def inBounds(mat, x, y):
            return x >= 0 and x < len(mat) and y >= 0 and y < len(mat[0])
        
        def dist(x1, y1, x2, y2):
            return abs(x1 - x2) + abs(y1 - y2)

        def checkEnds(mat, startX, startY, rez):
            ext = 20

            for i in range(startX - ext, startX + ext + 1):
                for j in range(startY - ext, startY + ext + 1):
                    if dist(startX, startY, i, j) <= ext and inBounds(mat, i, j) and str(mat[i][j]).isdigit():
                        nm = mat[i][j] - mat[startX][startY] - dist(startX, startY, i, j)
                        if nm not in rez:
                            rez[nm] = 0
                        rez[nm] += 1


        cnt = 0

        with open(fileName, 'r') as file:
            content = file.read()

            mat = []

            for line in content.split('\n'):
                mat.append(list(line))

                for i, ch in enumerate(line):
                    if ch == 'S':
                        start = (len(mat) - 1, i)
                        mat[len(mat) - 1][i] = 0
                    elif ch == 'E':
                        end = (len(mat) - 1, i)
                        mat[len(mat) - 1][i] = '.'
            
            from collections import deque

            q = deque()

            q.append((start[0], start[1], 0))

            ord = []

            dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]

            while len(q) > 0:
                fr = q.popleft()
                ord.append(fr)

                if fr[0] == end[0] and fr[1] == end[1]:
                    break
                
                for d in dir:
                    newFr = (fr[0] + d[0], fr[1] + d[1], fr[2] + 1)

                    if newFr[0] >= 0 and newFr[0] < len(mat) and newFr[1] >= 0 and newFr[1] < len(mat[0]) and mat[newFr[0]][newFr[1]] == '.':
                        mat[newFr[0]][newFr[1]] = fr[2] + 1
                        q.append(newFr)
            
            rez = {}
            
            for i in range(len(ord)):
                checkEnds(mat, ord[i][0], ord[i][1], rez)
            
            #for i in range(len(mat)):
            #    print(''.join([str(x) for x in mat[i]]))

            for k in rez:

                if k >= 100:
                    #print(k, rez[k])
                    cnt += rez[k]
        
        return cnt




    @staticmethod
    def __d21p1(fileName):
        """
        Read the file and return the result to the first part of the twenty-first day's problem
        """

        def findPosition(mat, ch):
            for i in range(len(mat)):
                for j in range(len(mat[i])):
                    if mat[i][j] == ch:
                        return (i, j)
            return (-1, -1)

        def ok(mat, st, seq):
            for ch in seq:
                if mat[st[0]][st[1]] == ' ':
                    return False
                if ch == '^':
                    st = (st[0] - 1, st[1])
                elif ch == 'v':
                    st = (st[0] + 1, st[1])
                elif ch == '<':
                    st = (st[0], st[1] - 1)
                elif ch == '>':
                    st = (st[0], st[1] + 1)
                
                if st[0] < 0 or st[0] >= len(mat) or st[1] < 0 or st[1] >= len(mat[0]):
                    return False
            return True
            

        def generateMoves(position, objective, pad):
            objPos = findPosition(pad, objective)
            
            ret = ''

            if position[1] > objPos[1]:
                ret += '<' * (position[1] - objPos[1])
            
            if position[0] > objPos[0]:
                ret += '^' * (position[0] - objPos[0])
            if position[0] < objPos[0]:
                ret += 'v' * (objPos[0] - position[0])

            if position[1] < objPos[1]:
                ret += '>' * (objPos[1] - position[1])

            if not ok(pad, position, ret):
                ret = ''
                if position[1] < objPos[1]:
                    ret += '>' * (objPos[1] - position[1])

                if position[0] > objPos[0]:
                    ret += '^' * (position[0] - objPos[0])
                if position[0] < objPos[0]:
                    ret += 'v' * (objPos[0] - position[0])
                
                if position[1] > objPos[1]:
                    ret += '<' * (position[1] - objPos[1])

            
            return ret


        def solve(code, robots, keyPad, robotPad, maxRobots):
            if robots <= 0:
                return len(code)

            ret = 0

            posi = 3
            posj = 2

            if robots != maxRobots:
                posi = 0

            totalMoves = ''
            
            for ch in code:
                if robots == maxRobots:
                    moves = generateMoves((posi, posj), ch, keyPad)
                    posi, posj = findPosition(keyPad, ch)
                else:
                    moves = generateMoves((posi, posj), ch, robotPad)
                    posi, posj = findPosition(robotPad, ch)
                totalMoves += moves + 'A'
                ret += solve(moves + 'A', robots - 1, keyPad, robotPad, maxRobots)
            return ret

        ret = 0

        with open(fileName, 'r') as file:
            content = file.read()

            maxRobots = 3

            keyPad = ['789', '456', '123', ' 0A']
            robotPad = [' ^A', '<v>']

            for code in content.split('\n'):
                numericPart = 0

                for ch in code:
                    if ch >= '0' and ch <= '9':
                        numericPart = numericPart * 10 + int(ch)

                sv = solve(code, maxRobots, keyPad, robotPad, maxRobots)
                ret += sv * numericPart

        return ret
    


    @staticmethod
    def __d21p2(fileName):
        """
        Read the file and return the result to the second part of the twenty-first day's problem
        """

        from functools import cache

        @cache
        def findPosition(mat, ch):
            for i in range(len(mat)):
                for j in range(len(mat[i])):
                    if mat[i][j] == ch:
                        return (i, j)
            return (-1, -1)

        @cache
        def ok(mat, st, seq):
            for ch in seq:
                if mat[st[0]][st[1]] == ' ':
                    return False
                if ch == '^':
                    st = (st[0] - 1, st[1])
                elif ch == 'v':
                    st = (st[0] + 1, st[1])
                elif ch == '<':
                    st = (st[0], st[1] - 1)
                elif ch == '>':
                    st = (st[0], st[1] + 1)
                
                if st[0] < 0 or st[0] >= len(mat) or st[1] < 0 or st[1] >= len(mat[0]):
                    return False
            return True
            
        @cache
        def generateMoves(position, objective, pad):
            objPos = findPosition(pad, objective)
            
            ret = ''

            if position[1] > objPos[1]:
                ret += '<' * (position[1] - objPos[1])
            
            if position[0] > objPos[0]:
                ret += '^' * (position[0] - objPos[0])
            if position[0] < objPos[0]:
                ret += 'v' * (objPos[0] - position[0])

            if position[1] < objPos[1]:
                ret += '>' * (objPos[1] - position[1])

            if not ok(pad, position, ret):
                ret = ''
                if position[1] < objPos[1]:
                    ret += '>' * (objPos[1] - position[1])

                if position[0] > objPos[0]:
                    ret += '^' * (position[0] - objPos[0])
                if position[0] < objPos[0]:
                    ret += 'v' * (objPos[0] - position[0])
                
                if position[1] > objPos[1]:
                    ret += '<' * (position[1] - objPos[1])

            
            return ret

        @cache
        def solve(code, robots, keyPad, robotPad, maxRobots):
            if robots <= 0:
                return len(code)

            ret = 0

            posi = 3
            posj = 2

            if robots != maxRobots:
                posi = 0

            totalMoves = ''
            
            for ch in code:
                if robots == maxRobots:
                    moves = generateMoves((posi, posj), ch, keyPad)
                    posi, posj = findPosition(keyPad, ch)
                else:
                    moves = generateMoves((posi, posj), ch, robotPad)
                    posi, posj = findPosition(robotPad, ch)
                totalMoves += moves + 'A'
                ret += solve(moves + 'A', robots - 1, keyPad, robotPad, maxRobots)
            return ret

        ret = 0

        with open(fileName, 'r') as file:
            content = file.read()

            maxRobots = 26

            keyPad = ('789', '456', '123', ' 0A')
            robotPad = (' ^A', '<v>')

            for code in content.split('\n'):
                numericPart = 0

                for ch in code:
                    if ch >= '0' and ch <= '9':
                        numericPart = numericPart * 10 + int(ch)

                sv = solve(code, maxRobots, keyPad, robotPad, maxRobots)
                ret += sv * numericPart

        return ret



    @staticmethod
    def __d22p1(fileName):
        """
        Read the file and return the result to the first part of the twenty-second day's problem
        """

        def mix(a, b):
            return a ^ b

        def prune(a):
            return a % 16777216

        sum = 0

        with open(fileName, 'r') as file:
            content = file.read()

            iters = 2000

            for line in content.split('\n'):
                num = int(line)

                for i in range(iters):
                    num = mix(num, num * 64)
                    num = prune(num)

                    num = mix(num, num // 32)
                    num = prune(num)

                    num = mix(num, num * 2048)
                    num = prune(num)
                
                sum += num
        
        return sum
    




    @staticmethod
    def __d22p2(fileName):
        """
        Read the file and return the result to the second part of the twenty-second day's problem
        """

        def mix(a, b):
            return a ^ b

        def prune(a):
            return a % 16777216

        ret = 0

        with open(fileName, 'r') as file:
            content = file.read()

            iters = 2000

            totalBananas = {}

            for line in content.split('\n'):
                num = int(line)

                localBananas = {}
                lastDiff = (10, 10, 10, 10)

                for i in range(iters):
                    prev = num % 10
                    num = mix(num, num * 64)
                    num = prune(num)

                    num = mix(num, num // 32)
                    num = prune(num)

                    num = mix(num, num * 2048)
                    num = prune(num)

                    pri = num % 10

                    lastDiff = lastDiff[1:] + (pri - prev,)

                    if lastDiff not in localBananas:
                        localBananas[lastDiff] = pri
                
                for diff in localBananas:
                    if diff not in totalBananas:
                        totalBananas[diff] = 0
                    totalBananas[diff] += localBananas[diff]
                
            for diff in totalBananas:
                if totalBananas[diff] > ret:
                    ret = totalBananas[diff]
        
        return ret




    @staticmethod
    def __d23p1(fileName):
        """
        Read the file and return the result to the first part of the twenty-third day's problem
        """

        def solve(dep, maxDep, connections, curCom, computers, solutions):
            if dep == maxDep:
                tmp = curCom.copy()
                tmp.sort()
                solutions.add(tuple(tmp))
                return
            #print(dep, curCom)

            for i, com in enumerate(computers):
                ok = True

                for c in curCom:
                    if (com, c) not in connections:
                        #print(com, c, i)
                        ok = False
                        break
                        
                if ok:
                    curCom.append(com)
                    solve(dep + 1, maxDep, connections, curCom, computers, solutions)
                    curCom.pop()
            


        cnt = 0

        with open(fileName, 'r') as file:
            content = file.read()

            connections = []
            computers = []

            for line in content.split('\n'):
                c1, c2 = line.split('-')

                connections.append((c1, c2))
                connections.append((c2, c1))
                
                if c1 not in computers:
                    computers.append(c1)
                if c2 not in computers:
                    computers.append(c2)
            
            #print(computers)

            frcmp = list(computers)
            frcon = list(connections)

            solutions = set()

            #print(frcmp)
            #print(frcon)
            
            for i, c in enumerate(frcmp):
                if c[0] == 't':
                    #print('STARTING WITH ', c)
                    solve(1, 3, frcon, [c], frcmp, solutions)
            
            cnt = len(solutions)
            #print(solutions)
        
        return cnt
    


    @staticmethod
    def __d23p2(fileName):
        """
        Read the file and return the result to the second part of the twenty-third day's problem
        """
        
        with open(fileName, 'r') as file:
            content = file.read()

            connections = set()
            computers = set()

            for line in content.split('\n'):
                c1, c2 = line.split('-')
                
                connections.add((c1, c2))
                connections.add((c2, c1))

                computers.add(c1)
                computers.add(c2)
            
            nets = []

            for c in computers:
                nets.append(set([c]))
            
            for net in nets:
                for com in computers:
                    ok = True
                    for c in net:
                        if (com, c) not in connections:
                            ok = False
                            break
                    
                    if ok:
                        net.add(com)
            
            maxx = 0
            maxNet = 0

            for net in nets:
                if len(net) > maxx:
                    maxx = len(net)
                    maxNet = net
            
            maxNet = list(maxNet)
            maxNet.sort()
            
        return ','.join(maxNet)




    @staticmethod
    def __d24p1(fileName):
        """
        Read the file and return the result to the first part of the twenty-fourth day's problem
        """

        ret = 0

        with open(fileName, 'r') as file:
            content = file.read()

            mode = 0

            solved = {}

            from collections import deque

            unsolved = deque()

            for line in content.split('\n'):
                if line == '':
                    mode = 1
                    continue

                if mode == 0:
                    name, val = line.split(': ')
                    val = int(val)
                    solved[name] = val
                else:
                    name1, op, name2, _, res = line.split()
                    unsolved.append((name1, name2, op, res))
            
            #print(solved)
            #print(unsolved)
            
            while len(unsolved) > 0:
                fr = unsolved.popleft()

                if fr[0] in solved and fr[1] in solved:
                    res = 0
                    if fr[2] == 'AND':
                        res = solved[fr[0]] & solved[fr[1]]
                    elif fr[2] == 'OR':
                        res = solved[fr[0]] | solved[fr[1]]
                    else:
                        res = solved[fr[0]] ^ solved[fr[1]]
                    solved[fr[3]] = res
                else:
                    unsolved.append(fr)
            
            #print(solved)

            for name in solved:
                if name.startswith('z'):
                    zInd = int(name[1:])
                    ret += solved[name] << zInd
        
        return ret
    



    @staticmethod
    def __d24p2(fileName):
        """
        Read the file and return the result to the second part of the twenty-fourth day's problem
        """

        with open(fileName, 'r') as file:
            content = file.read()

            mode = 0
            errors = set()

            wires = []

            for line in content.split('\n'):
                if line == '':
                    mode = 1
                    continue

                if mode == 1:
                    name1, op, name2, _, res = line.split()
                    
                    if res.startswith('z') and res != 'z45' and op != 'XOR':
                        errors.add(res)
                    elif not res.startswith('z') and op == 'XOR' and not name1.startswith('x') and not name2.startswith('y') and not name2.startswith('x') and not name1.startswith('y'):
                        errors.add(res)
                    
                    wires.append((name1, name2, op, res))

            for wire in wires:
                if wire[0] == 'x00' or wire[1] == 'x00':
                    continue
                if wire[2] == 'XOR' and ((wire[0].startswith('x') and wire[1].startswith('y')) or (wire[0].startswith('y') and wire[1].startswith('x'))):
                    ok = False
                    for w in wires:
                        if (w[1] == wire[3] or w[0] == wire[3]) and w[2] == 'XOR':
                            ok = True
                            break
                    if not ok:
                        errors.add(wire[3])
                if wire[2] == 'AND':
                    ok = False
                    for w in wires:
                        if (w[1] == wire[3] or w[0] == wire[3]) and w[2] == 'OR':
                            ok = True
                            break
                    if not ok:
                        errors.add(wire[3])
            

            errList = list(errors)
            errList.sort()
        
        return ','.join(errList)




    @staticmethod
    def __d25p1(fileName):
        """
        Read the file and return the result to the first part of the twenty-fifth day's problem
        """

        cnt = 0

        with open(fileName, 'r') as file:
            content = file.read()

            locks = []
            keys = []

            readingNext = True
            isLock = False

            height = 0
            readingHeight = True

            for line in content.split('\n'):
                #print(line)
                if line == '':
                    readingNext = True
                    if readingHeight:
                        readingHeight = False
                    continue
                    
                if readingNext:
                    readingNext = False
                    if line == '.' * len(line):
                        isLock = False
                        keys.append([0] * len(line))
                    else:
                        isLock = True
                        locks.append([0] * len(line))
                
                if readingHeight:
                    height += 1

                if isLock:
                    for i, ch in enumerate(line):
                        if ch == '#':
                            locks[-1][i] += 1
                else:
                    for i, ch in enumerate(line):
                        if ch == '#':
                            keys[-1][i] += 1

            for lc in locks:
                for k in keys:
                    ok = True
                    for i in range(len(locks[0])):
                        if lc[i] + k[i] > height:
                            ok = False
                            break
                    
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
        },
        14: {
            1: __d14p1,
            2: __d14p2
        },
        15: {
            1: __d15p1,
            2: __d15p2
        },
        16: {
            1: __d16p1,
            2: __d16p2
        },
        17: {
            1: __d17p1,
            2: __d17p2
        },
        18: {
            1: __d18p1,
            2: __d18p2
        },
        19: {
            1: __d19p1,
            2: __d19p2
        },
        20: {
            1: __d20p1,
            2: __d20p2
        },
        21: {
            1: __d21p1,
            2: __d21p2
        },
        22: {
            1: __d22p1,
            2: __d22p2
        },
        23: {
            1: __d23p1,
            2: __d23p2
        },
        24: {
            1: __d24p1,
            2: __d24p2
        },
        25: {
            1: __d25p1
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
AdventOfCode.Solve(25, 1, "Inputs/Day25/p25.txt")