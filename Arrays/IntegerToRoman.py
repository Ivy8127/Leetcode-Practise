class Solution:
    def intToRoman(self, num: int) -> str:
        symList = [["I",1],["IV",4 ],["V",5],["IX",9], ["X",10],["XL",40],["L",50],
                   ["XC",90],["C",100],["CD",400],["D",500],["CM",900],["M",1000]]
        
        #1500 / 1000  => 1 1500 MOD 1000 = 500 /500 = 1 500 mod 500 = 0 stop
        #"MD"
        #900 / 1000 => 0  900/900 = 1 900 mod 900 =0
        #"CM"
        res = ""
        for sym, val in reversed(symList):
            if num // val:
                count = num // val
                res += (count * sym)
                num = num % val
        return res