At first I wasn't sure exactly how to get the data using the testing environment


I then realized we were using a string object that contained multiple lines. Therefore the data wasn't provided as separate input but needed to be parsed by the code_here function first. I achieved separating the input data and placing it into two separate variables using the split() library function and passing in new line as a parameter. 


I recognized the problem to be similiar to two sum early on. 


At first I attempted to implement a brute force solution but was facing error messages regarding my input. I realized that I still needed to convert the list data to integers. This is where I struggled solving the problem. At first I tried list comprehension to convert to integers but ran into a problem. I was separating by character. This caused an invalid literal for int() with base 10 exception. Once I realized this I used the list map function to convert my already parsed list of strings into a list of integers aka the input array. 


From there my brute force solution started working. However I sill needed to return pairs. Next I created a list before the loop that held the stored pairs Unfortunately I was not able to finish my solution within the given time returning the appropriate output. You can however see the printed message for "found a sum" when a correct pair is found. The solution identifies if a list pair was not found by checking if the list_pairs variable is empty. 


If I had realized my integer issue earlier I would have been able to finish my solution returning the pairs as a string object with each pair on a separate line and properly sorted in ascending order. I would most likely use the library function.Sort().


My brute force solution runs at O(n2) time complexity and O(!) space complexity. 


If I had to implement a proper solution I would have used Hash Map (Two Pass) which would run O(n) for both time and space complexity. 


I am still new to learning leet code style code assessments. Thank you for the opportunity. I will continue to study and improve my code assessment skills. Please keep me in mind for future opportunities.