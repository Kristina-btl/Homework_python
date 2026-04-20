from Address import Address
from Mailing import Mailing 


from_address = Address ("123456", "Minsk", "Pushkina",  "10" , "8")
to_address = Address ("654321", "Moscow", "Lenina",  "40" , "50")

mailing = Mailing (to_address=to_address, from_address=from_address, track= "NSKF02uNd", cost = "555.3")



print (f"Отправление {mailing.track} из {from_address} в {to_address}. Стоимостью {mailing.cost} рублей" )