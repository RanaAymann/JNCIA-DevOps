from jnpr.junos import Device

dev = Device(host="10.1.1.1", user="lab", password="lab123")
dev.open()
print(dev.facts)
dev.close()

# collect junos facts

