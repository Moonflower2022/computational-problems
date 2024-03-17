import random

class BeerDistributionGame:
    def __init__(self, initial_inventory, num_rounds, num_sims, strategy, strategy_name):
        self.num_sims = num_sims
        self.initial_inventory = initial_inventory
        self.customer_demand = random.randint(0, 8)
        self.retailer_inventory = initial_inventory
        self.wholesaler_inventory = initial_inventory
        self.distributor_inventory = initial_inventory
        self.factory_inventory = initial_inventory
        self.order_delay = 2
        self.orders = [4, 4, 4, 4]
        self.num_rounds = num_rounds
        self.strategy = strategy
        self.strategy_name = strategy_name
        self.results = []

    def place_orders(self, strategy):
        new_orders = self.orders.copy()
        new_orders.append(strategy(self))  # Update the orders
        if len(new_orders) > self.order_delay:
            new_orders.pop(0)  # Remove the oldest order
        return new_orders

    def fulfill_orders(self):
    # Reduce inventory based on orders and increase inventory based on oldest order
        new_inventories = self.inventories.copy()
        updated_orders = []
        for i in range(4):
            new_inventories[i] -= self.orders[i]
            if len(self.orders) > self.order_delay:
                new_inventories[i] += self.orders[i - self.order_delay]
            updated_orders.append(new_inventories[i])
        return updated_orders

    def simulate_game(self):
        # Reset inventories, orders, and customer demand for each game
        self.inventories = [self.initial_inventory] * 4
        updated_orders = [0] * 4
        self.customer_demand = random.randint(0, 8)
        for _ in range(self.num_rounds):
            updated_orders = self.place_orders(self.strategy)
            updated_orders = self.fulfill_orders()
            self.results.append(self.calculate_cost())
        return updated_orders

    def calculate_cost(self):
        # Calculate the total cost in one line
        total_cost = sum(max(0, inventory - self.customer_demand)/2 + max(0, self.customer_demand - inventory) for inventory in self.inventories)
        return total_cost

    def play_game(self):
        results = []
        for _ in range(self.num_sims):  # Run the simulation 100 times
            self.orders = self.simulate_game()
            results.append(self.results)
        self.display_results()
        print()

    def display_results(self):
        total_cost = sum(self.results)
        average_cost = total_cost / self.num_sims  # Calculate the average of the 100 results
        print(f"Average total cost for {self.strategy_name}: {average_cost}")
        average_cost_per_round = average_cost / self.num_rounds
        print(f"Average cost per round for {self.strategy_name}: {average_cost_per_round:.2f}")

def random_strategy(game):
        return random.randint(0, game.initial_inventory)

def fixed_order_strategy(game):
    return 10  # Fixed order quantity

def fixed_order_with_forecast_strategy(game):
    return max(0, game.customer_demand - 2)  # Order quantity based on forecast

def demand_matching_strategy(game):
    return game.customer_demand  # Order quantity matches customer demand

def mitigating_bullwhip_strategy(game):
    if game.customer_demand > game.retailer_inventory + game.order_delay:
        return game.customer_demand
    else:
        return 0

if __name__ == "__main__":
    rounds = 30  # Number of rounds to simulate
    sims = 1000 # Number of simulations to average over
    initial_inventory = 12  
    strategy_names = ["Random", "Fixed Order", "Fixed Order with Demand Forecast", "Demand-Matching", "Mitigating Bullwhip"]
    strategies = [
            random_strategy,
            fixed_order_strategy,
            fixed_order_with_forecast_strategy,
            demand_matching_strategy,
            mitigating_bullwhip_strategy
    ]
    games = []
    for i in range(5):
        games.append(BeerDistributionGame(initial_inventory, rounds, sims, strategies[i], strategy_names[i]))
    for i in range(5):
        games[i].play_game()