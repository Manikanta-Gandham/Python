def numberToWords( num):
        """
        :type num: int
        :rtype: str
        """
        tens=["Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]
        ones=["One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
        if num==0:
            return "Zero"
        ret=""
        if num//1000000000!=0:
            ret += numberToWords(num//1000000000)+" Billion "
            num%=1000000000
        if num//1000000!=0:
            ret += numberToWords(num//1000000)+" Million "
            num%=1000000
        if num//1000!=0:
            ret += numberToWords(num//1000)+" Thousand "
            num%=1000
        if num//100!=0:
            ret += numberToWords(num//100)+" Hundred "
            num%=100
        if num>=20 and num//10!=0:
            ret += tens[num//10-2]+" "
            num%=10
        if num!=0:
            ret += ones[num-1]
        return ret.strip()

print(numberToWords(123456789))