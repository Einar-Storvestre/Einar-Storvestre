
def setning_dikter(setning):
  sporreord = ("hva","hordan","hvem","hvorfor")
  store_bokstaver = setning.capitalize()
  if setning.startswith(sporreord):
    return "{}?".format(store_bokstaver)
  else:
    return "{}.".format(store_bokstaver)

resultater =[]
while True:
  bruker_innput = input("Si noe: ")
  if bruker_innput =="\end":
    break
  else:
    resultater.append(setning_dikter(bruker_innput))

print(" ".join(resultater))












