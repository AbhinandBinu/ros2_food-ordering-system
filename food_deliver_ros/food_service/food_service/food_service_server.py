# food_service_server.py

import rclpy
from rclpy.node import Node
from food_interfaces.srv import FoodOrder
import time


class FoodServiceServer(Node):

    def __init__(self):
        super().__init__('food_service_server')

        self.srv = self.create_service(
            FoodOrder,
            'order_food',
            self.handle_order
        )

        self.get_logger().info("🍽 Food Service Server is READY")


    def simulate_cooking(self, item, duration):
        """Simulate cooking with step-by-step logs"""
        for i in range(duration):
            self.get_logger().info(
                f"👨‍🍳 {item.capitalize()} cooking... {i+1}/{duration} sec"
            )
            time.sleep(1)


    def handle_order(self, request, response):
        item = request.item_name.strip().lower()

        self.get_logger().info(f"📥 Received Order: {item}")

        if item == "pizza":
            self.get_logger().info("🔥 Starting Pizza Preparation")
            self.simulate_cooking("pizza", 5)
            response.status = "🍕 Pizza is ready!"

        elif item == "burger":
            self.get_logger().info("🔥 Starting Burger Preparation")
            self.simulate_cooking("burger", 3)
            response.status = "🍔 Burger is ready!"

        else:
            self.get_logger().warn("❌ Item not available")
            response.status = "❌ Item not available"

        self.get_logger().info(f"✅ Order Completed: {item}\n")

        return response


def main():
    rclpy.init()
    node = FoodServiceServer()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info("🛑 Server stopped manually")

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
