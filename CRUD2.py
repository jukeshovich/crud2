class Car:
    def __init__(self, id, make, model, year):
        self.id = id
        self.make = make
        self.model = model
        self.year = year

def create_car(cars):
    id = int(input("Введите ID машины: "))
    make = input("Введите марку машины: ")
    model = input("Введите модель машины: ")
    year = int(input("Введите год выпуска: "))
    car = Car(id, make, model, year)
    cars.append(car)
    print("Машина успешно добавлена!")

def read_car(cars, car_id):
    for car in cars:
        if car.id == car_id:
            return car
    return None

def update_car(cars, car_id):
    car = read_car(cars, car_id)
    if car:
        print(f"Нынешняя инфа о машине: ID={car.id}, Марка={car.make}, Модель={car.model}, Год={car.year}")
        make = input("Введите марку машины: ")
        model = input("Введите марку машины: ")
        year = input("Введите год машины: ")

        if make:
            car.make = make
        if model:
            car.model = model
        if year:
            car.year = int(year)

        print("Машина успешно обновлена!")
    else:
        print("Машина не найдена")

def delete_car(cars, car_id):
    car = read_car(cars, car_id)
    if car:
        cars.remove(car)
        print("Машина успешно удалена!")
    else:
        print("Машина не найдена")

if __name__ == "__main__":
    car_database = []

    while True:
        print("\nМеню:")
        print("1. Create Car")
        print("2. Read Car")
        print("3. Update Car")
        print("4. Delete Car")
        print("5. Exit")
        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == '1':
            create_car(car_database)
        elif choice == '2':
            car_id = int(input("Enter car ID to read: "))
            car = read_car(car_database, car_id)
            if car:
                print(f"Car found: ID={car.id}, Make={car.make}, Model={car.model}, Year={car.year}")
            else:
                print("Car not found")
        elif choice == '3':
            car_id = int(input("Enter car ID to update: "))
            update_car(car_database, car_id)
        elif choice == '4':
            car_id = int(input("Enter car ID to delete: "))
            delete_car(car_database, car_id)
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select a valid option.")
