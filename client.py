import xmlrpc.client
proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")

num1=int(input("Enter num1: "))

num2=int(input("Enter num2: "))





print("factorial of num1 is : %s" % str(proxy.factorial_rpc(num1)))
print("factorial of num2 is : %s" % str(proxy.factorial_rpc(num2)))
