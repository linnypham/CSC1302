def computeMSE(observed, predicted):
    #TODO 1: Complete this function
    n = len(observed)
    mse = sum((obs - pred) ** 2 for obs, pred in zip(observed, predicted)) / n
    return mse

def computeRMSE(observed, predicted):
    #TODO 2: Complete this function
    mse = computeMSE(observed, predicted)
    rmse = mse ** 0.5
    return rmse

def computeMAE(observed, predicted):
    # TODO 3: Complete this function
    n = len(observed)
    mae = sum(abs(obs - pred) for obs, pred in zip(observed, predicted)) / n
    return mae

'''
TODO 4: Write driver code that calls the above methods and prints
the MSE, RMSE, and MAE for the following input. (Round
off the results to two decimal places)
    observed = 4,5,12,5,7
    predicted = 5,5,11,4,5
'''
#Driver code

observed = [4,5,12,5,7]
predicted = [5,5,11,4,5]

mse = computeMSE(observed,predicted)
rmse = computeRMSE(observed,predicted)
mae = computeMAE(observed,predicted)

print(f"MSE = {mse:.2f}")
print(f"RMSE = {rmse:.2f}")
print(f"MAE = {mae:.2f}")