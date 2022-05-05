class TrackOrders:
    # Aqui deve expor a quantidade de estoque
    orders = []

    def __init__(self):
        self.orders.clear()

    @classmethod
    def __len__(self):
        return len(self.orders)

    @classmethod
    def add_new_order(self, customer, order, day):
        new_order = [customer, order, day]
        self.orders.append(new_order)

    def get_most_ordered_dish_per_customer(self, customer):
        orders_array = [
            order[1] for order in self.orders if order[0] == customer
            ]
        orders_dict = {}
        for order in orders_array:
            if order in orders_dict:
                orders_dict[order] += 1
            else:
                orders_dict[order] = 1

        most_ordered = list(orders_dict.keys())[0]
        for item in orders_dict.keys():
            if orders_dict[item] > orders_dict[most_ordered]:
                most_ordered = item
        return most_ordered

    def get_never_ordered_per_customer(self, customer):
        plates = set()
        person_plates = set()
        for order in self.orders:
            plates.add(order[1])
            if order[0] == customer:
                person_plates.add(order[1])
        return plates-person_plates

    def get_days_never_visited_per_customer(self, customer):
        days = set()
        person_days = set()
        for order in self.orders:
            days.add(order[2])
            if order[0] == customer:
                person_days.add(order[2])
        return days-person_days

    def get_busiest_day(self):
        days_dict = {}
        for order in self.orders:
            if order[2] in days_dict:
                days_dict[order[2]] += 1
            else:
                days_dict[order[2]] = 1
        most_frequent = list(days_dict.keys())[0]
        for item in days_dict.keys():
            if days_dict[item] > days_dict[most_frequent]:
                most_frequent = item
        return most_frequent

    def get_least_busy_day(self):
        days_dict = {}
        for order in self.orders:
            if order[2] in days_dict:
                days_dict[order[2]] += 1
            else:
                days_dict[order[2]] = 1
        least_frequent = list(days_dict.keys())[0]
        for item in days_dict.keys():
            if days_dict[item] < days_dict[least_frequent]:
                least_frequent = item
        return least_frequent
