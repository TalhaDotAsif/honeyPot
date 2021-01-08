from socket import *

def main():
    ipadd="your ip"
    port="80"
    print("Honey Pot is active ........")

    try:
        get_socket_con = socket(AF_INET,SOCK_STREAM)
        get_socket_con.bind(ipadd,port)
        get_socket_con.listen(10)
        while True:
            client_con,client_addr = get_socket_con.accept()
            print("[+] Visitor found - [{}] ". format(client_addr[0]))
            client_con.send(b"<h1>You have been hacked</h1>")
            data = client_con.recv(1024)
            print(data.decode('UTF-8'))

    except error as identifier:
        print("[+] Unspecified error [{}]".format(identifier))
    except KeyboardInterrupt as ky:
        print("[-] Process stopped! ")
        get_socket_con.close()
    finally:
        get_socket_con.close()
    get_socket_con.close()
if __name__ == '__main__':
    main()
