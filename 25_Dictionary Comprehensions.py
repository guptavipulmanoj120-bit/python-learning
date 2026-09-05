#Create a dictionary where Key → the number Value → the number multiplied by 10 Include only numbers greater than 3

numbers = [1, 2, 3, 4, 5, 6]

result = {number: number*10 for number in numbers if number > 3}

print(result)

#Create a dictionary for numbers = [5, 10, 15, 20]Where Key → number Value → "Big" if the number is >= 15 Otherwise → "Small"

numbers = [5, 10, 15, 20]

result = {number: "big" if number >= 15 else "small" for number in numbers}

print(result)

#Create a dictionary where Key → number Value → "Even" if even, otherwise "Odd" But include only numbers greater than 2

numbers = [1, 2, 3, 4, 5, 6]

result = {number: "even" if number % 2 == 0 else "odd" 
          for number in numbers
           if number > 2}

print(result)
