from ldap3 import Server, Connection, LDAPException, AUTH_SIMPLE
from customers.models import Customer

class ActiveDirectoryAuthentication:
    def authenticate(self, username, password):
        # build a client
        if '@dylan.be' in username:
            server = Server('10.3.50.160', port=636)  # define an unsecure LDAP server, requesting info on DSE and schema
            try:
                connection = Connection(server, user=username, password=password, auto_bind=True, authentication=AUTH_SIMPLE)
            except LDAPException:
                return None
            if connection.result != None:
                try:
                    customer = Customer.objects.get(email=username)
                except Customer.DoesNotExist:
                    customer = Customer.objects.create_user(email=username, password=password, first=username, last=username, birth=None, address=username, special=None, used=None, ad=True)
                connection.unbind()
                return customer
            else:
                return None
        else:
            return None

    def get_user(self, user_id):
        try:
            return Customer.objects.get(pk=user_id)
        except Customer.DoesNotExist:
            return None