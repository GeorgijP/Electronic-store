from utils.utils import Phone

item = Phone("SamsundDuo", 60_000, 4, 2)


print(item.quantity_sim)

item.quantity_sim = 100

print(item.quantity_sim)