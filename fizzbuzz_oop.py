class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        """ This method generates numbers according to the FizzBuzz game.

        Args:
            n (int): The number to stop counting at (i.e 1-20, 20 being the nth number).

        Returns:
            list[str]: The method retuns a List of numbers in the form of stings.
        """
        
        arr = list()
        for i in range(1, n + 1):
            if i%3 == 0 and i%5 == 0:
                i = "FizzBuzz"
                arr.append(i)

            elif i%3 == 0:
                i = "Fizz"
                arr.append(i)
            
            elif  i%5 == 0:
                i = "Buzz"
                arr.append(i)
            
            else:
                arr.append(str(i))

        return (arr)

fizzBuzz_inst = Solution()

fb_result = fizzBuzz_inst.fizzBuzz(20)
print(fb_result)
