import numpy as np

def calculate(list):
  matrix = np.array(list)

  if len(list) < 9:
    raise ValueError("List must contain nine numbers.")

  matrix = matrix.reshape((3, 3))
  print(matrix)

  #determine mean then convert arrays to lists
  mean_flat = np.mean(matrix)
  mean_a1 = np.mean(matrix, axis=0)
  mean_a2 = np.mean(matrix, axis=1)
  mean_a1 = mean_a1.tolist()
  mean_a2 = mean_a2.tolist()
  
  #determine variance then convert arrays to lists
  var_flat = np.var(matrix)
  var_a1 = np.var(matrix, axis=0)
  var_a2 = np.var(matrix, axis=1)
  var_a1 = var_a1.tolist()
  var_a2 = var_a2.tolist()

  #determine standard deviation then convert arrays to lists
  std_flat = np.std(matrix)
  std_a1 = np.std(matrix, axis=0)
  std_a2 = np.std(matrix, axis=1)
  std_a1 = std_a1.tolist()
  std_a2 = std_a2.tolist()

  #determine max then convert arrays to lists
  max_flat = np.max(matrix)
  max_a1 = np.max(matrix, axis=0)
  max_a2 = np.max(matrix, axis=1)
  max_a1 = max_a1.tolist()
  max_a2 = max_a2.tolist()

  #determine min then convert arrays to lists
  min_flat = np.min(matrix)
  min_a1 = np.min(matrix, axis=0)
  min_a2 = np.min(matrix, axis=1)
  min_a1 = min_a1.tolist()
  min_a2 = min_a2.tolist()

  #determine sum then convert arrays to lists
  sum_flat = np.sum(matrix)
  sum_a1 = np.sum(matrix, axis=0)
  sum_a2 = np.sum(matrix, axis=1)
  sum_a1 = sum_a1.tolist()
  sum_a2 = sum_a2.tolist()


  calculations = {}
  calculations['mean'] = [mean_a1, mean_a2, mean_flat]
  calculations['variance'] = [var_a1, var_a2, var_flat]
  calculations['standard deviation'] = [std_a1, std_a2, std_flat]
  calculations['max'] = [max_a1, max_a2, max_flat]
  calculations['min'] = [min_a1, min_a2, min_flat]
  calculations['sum'] = [sum_a1, sum_a2, sum_flat]

  print(calculations)

  return calculations


