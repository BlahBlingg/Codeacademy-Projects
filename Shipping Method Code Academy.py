def ground_shipping(weight):
  if weight <= 2.0:
    return (weight * 1.5 + 20)
  if weight > 2.0 and weight <= 6.0:
    return (weight * 3 + 20)
  if weight > 6.0 and weight <= 10.0:
    return (weight * 4 + 20)
  if weight > 10.0:
    return (weight * 4.75 + 20)
print(ground_shipping(8.4))
premium_shipping = 125.00
def drone_shipping(weight):
  if weight <= 2.0:
    return (weight * 4.5)
  if weight > 2.0 and weight <= 6.0:
    return (weight * 9)
  if weight > 6.0 and weight <= 10.0:
    return (weight * 12)
  if weight > 10:
    return (weight * 14.25)
print(drone_shipping(1.5))
def cheapest_method(weight):
  if ground_shipping(weight) < drone_shipping(weight) and ground_shipping(weight) < premium_shipping:
    return ("Ground shipping is the cheapest shipping method. The cost to ship your package is " + str(ground_shipping(weight)))
  if drone_shipping(weight) < ground_shipping(weight) and drone_shipping(weight) < premium_shipping : 
    return ("Drone shipping is the cheapest shipping method. The cost to ship your package is " + str(drone_shipping(weight)))
  if premium_shipping < ground_shipping(weight) and premium_shipping < drone_shipping(weight):
    return ("Premium shipping is the cheapest shipping method. The cost of shipping is $125.00")
print(cheapest_method(4.8))
print(cheapest_method(41.5))
