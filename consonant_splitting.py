
class ConsonantSplitter:
    def syllabicate(self, word:str) -> list[str]:
        clumps = self.clumpify(word)
        shared = self.dispute(clumps)

        lx, rx = 0, len(clumps)-1

        while lx < rx:
            self.resolve(clumps, shared, lx)

            if len(clumps) % 2 and (lx == rx-1):
                break

            self.resolve(clumps, shared, rx-1)
            lx += 1
            rx -= 1

        if (len(clumps) > 1) and (clumps[-1] == 'e'):
            clumps.pop()
            clumps[-1] += 'e'

        return clumps


    def clumpify(self, word:str) -> list[str]:
        vowels = set('aeiouy')
        clumps, ix = [], 0
        consonants = ''

        for ch in word:
            if ch in vowels:
                if not clumps:
                    clumps.append(consonants + ch)
                else:
                    if consonants:
                        sc = self.digraph_split(consonants)
                        clumps.append(sc[1] + ch)
                        clumps[ix] += sc[0]
                        ix += 1
                    else:
                        clumps[ix] += ch
                consonants = ''
            else:
                consonants += ch
        
        if clumps and consonants:
            clumps[-1] += consonants

        elif consonants:
            clumps.append(consonants)
            
        return clumps
    

    def dispute(self, clumps:list[str]) -> list[int]:
        shared = []

        for i in range(max := len(clumps)):
            shared.insert(i, 0)

            if (i > 0) and (clumps[i-1][-1] == clumps[i][0]):
                shared[i] += 1
            
            if (i < max-1) and (clumps[i][-1] == clumps[i+1][0]):
                shared[i] += 1

        return shared


    def resolve(self, clumps:list[str], shared:list[int], ix:int):
        jx = ix+1
        dx = len(clumps[ix]) - len(clumps[jx])

        if shared[ix] and shared[jx]:
            if dx < 0:
                clumps[ix] = clumps[ix][:-1]
                shared[jx] -= 1

            elif dx > 0:
                clumps[jx] = clumps[jx][1:]
                shared[ix] -= 1

            elif shared[ix] > shared[jx]:
                clumps[ix] = clumps[ix][:-1]
                shared[jx] -= 1
            
            else:
                clumps[jx] = clumps[jx][1:]
                shared[ix] -= 1


    def dup_split(self, s:str) -> tuple[str, str]:
        return (s[:(mid := len(s) // 2) + (len(s) % 2)], s[mid:])


    def digraph_split(self, s:str) -> tuple[str, str]:
        pre_digs = {'bl', 'br', 'ch', 'cl', 'cr', 'dr', 'fl', 'fr', 'gl', 'gr', 'kn', 'ph', 'pl', 'pr', 'st', 'str', 'sw', 'th', 'tr', 'wh', 'wr'}
        pos_digs = {'ch', 'ck', 'dge', 'ly', 'mp', 'nd', 'ng', 'ph', 'sh', 'ss', 'st', 'th', 'tch'}

        for i in range(min(4, len(s) + 1), 1, -1):
            if s[:i] in pos_digs:
                return (s[:i], s[i:])
            
            if s[-i:] in pre_digs:
                return (s[:-i], s[-i:])
            
        return self.dup_split(s)
