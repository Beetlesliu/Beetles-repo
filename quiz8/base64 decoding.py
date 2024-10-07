import base64
coded_string = "RVZBe1czMWMwbUVfVG9fekp1RVY0X1QzY2hAPz8/Pz99Ck1ENTo5NDY4NkM1N0U1MTIzNDkyOEIzNDQ5MjRGOTkyRDlDOQ=="
decoded_bytes = base64.b64decode(coded_string)
decoded_string = decoded_bytes.decode('utf-8')
flag, md5 = decoded_string.split('\n')
flag = flag.replace('?????', md5[-5:])
print(flag)
