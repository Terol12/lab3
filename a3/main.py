prev_reading = int(input("Введите предыдущее показание счетчика: "))
current_reading = int(input("Введите текущее показание счетчика: "))

if current_reading >= prev_reading:
    gas_volume = current_reading - prev_reading
else:
    gas_volume = (10000 - prev_reading) + current_reading

if gas_volume <= 300:
    total_cost = 21.0
elif gas_volume <= 600:
    total_cost = 21.0 + (gas_volume - 300) * 0.06
elif gas_volume <= 800:
    total_cost = 21.0 + 300 * 0.06 + (gas_volume - 600) * 0.04
else:
    total_cost = 21.0 + 300 * 0.06 + 200 * 0.04 + (gas_volume - 800) * 0.025

if gas_volume > 0:
    average_price_per_m3 = total_cost / gas_volume
else:
    average_price_per_m3 = 0
print(f"Предыдущее: {prev_reading} куб.м")
print(f"Текущее: {current_reading} куб.м")
print(f"Использовано: {gas_volume} куб.м")
print(f"К оплате: {total_cost:.2f}$")
print(f"Средняя цена м^3: {average_price_per_m3:.2f}$")