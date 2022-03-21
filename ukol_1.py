baliky = {
    "B541X": True,
    "B547X": False,
    "B251X": False,
    "B501X": True,
    "B947X": False,
}

balik = input("Zadejte cislo baliku:")
delivery = baliky[balik]
if delivery == True:
  print('Balik byl predan kuryrovi.')
else:
  print('Balik zatim nebyl predan kuryrovi.')
<<<<<<< HEAD






=======
>>>>>>> ba8802d664f9367d9c417407ad60b83e863d9ca0
