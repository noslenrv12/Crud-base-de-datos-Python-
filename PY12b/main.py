from service.customer_service import CustomerService

def main():
    customer_service = CustomerService()

    # Pedir los datos del cliente al usuario
    print('\nCRUD Insert Customer')
    customer_name = input("Ingrese el nombre del cliente: ")
    contact_name = input("Ingrese el nombre de contacto: ")
    address = input("Ingrese la dirección: ")
    city = input("Ingrese la ciudad: ")
    postal_code = input("Ingrese el código postal: ")
    country = input("Ingrese el país: ")

    # Crear un nuevo cliente
    customer_service.create_customer(
        customer_name=customer_name,
        contact_name=contact_name,
        address=address,
        city=city,
        postal_code=postal_code,
        country=country
    )
    print("Cliente creado.")

    # Leer un cliente
    try:
        print('\nCRUD Leer Customer')
        customer_id = int(input("Ingrese el ID del cliente que desea leer: "))
        customer = customer_service.get_customer(customer_id)
        if customer:
            print(f"Cliente recuperado: {customer.customer_name}, {customer.contact_name}, {customer.address}")
        else:
            print("Cliente no encontrado.")
    except ValueError:
        print("Por favor, ingrese un número válido para el ID del cliente.")

    # Actualizar un cliente
    try:
        print('\nCRUD Actualizar Customer')
        customer_id = int(input("Ingrese el ID del cliente que desea actualizar: "))
        customer_name = input("Ingrese el nuevo nombre del cliente: ")
        contact_name = input("Ingrese el nuevo nombre de contacto: ")
        address = input("Ingrese la nueva dirección: ")
        city = input("Ingrese la nueva ciudad: ")
        postal_code = input("Ingrese el nuevo código postal: ")
        country = input("Ingrese el nuevo país: ")

        customer_service.update_customer(
            customer_id=customer_id,
            customer_name=customer_name,
            contact_name=contact_name,
            address=address,
            city=city,
            postal_code=postal_code,
            country=country
        )
        print("Cliente actualizado.")
    except ValueError:
        print("Por favor, ingrese un número válido para el ID del cliente.")

    # Eliminar un cliente
    try:
        print('\nCRUD Eliminar Customer')
        customer_id = int(input("Ingrese el ID del cliente que desea eliminar: "))
        customer_service.delete_customer(customer_id=customer_id)
        print("Cliente eliminado.")
    except ValueError:
        print("Por favor, ingrese un número válido para el ID del cliente.")

if __name__ == "__main__":
    main()
