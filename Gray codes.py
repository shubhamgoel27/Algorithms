import sys 

greylen = int(sys.argv[1])
var_array = []

for num in range(greylen):
  temp_zer = []
  temp_one = []
  for ind in range(pow(2,num)):
    temp_zer.append(0)
    temp_one.append(1)
  var_array.append(temp_zer + temp_one)

for num in range(int(greylen)):
  cur_arr = var_array[len(var_array)-num-1]
  while len(cur_arr) 
