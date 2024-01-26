class fizz_Buzz:

    FIZZ = 3
    BUZZ = 5

    def fizzbuzz(self, n: int) -> list[str]: 

        

        output =[
            "FizzBuzz" if i % self.FIZZ == 0 and i % self.BUZZ == 0
            else "Fizz" if i % self.FIZZ == 0
            else "Buzz" if i % self.BUZZ == 0
            else str(i)
            for i in range(1, n + 1)
        ]
        return output

fizz_buzz_instance = fizz_Buzz()
results = fizz_buzz_instance.fizzbuzz(20)
print(results)
