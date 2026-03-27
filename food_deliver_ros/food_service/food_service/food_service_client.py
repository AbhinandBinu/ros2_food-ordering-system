# food_service_client.py

import rclpy
from rclpy.node import Node
from food_interfaces.srv import FoodOrder


class FoodServiceClient(Node):

    def __init__(self):
        super().__init__('food_service_client')

        self.client = self.create_client(FoodOrder, 'order_food')

        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info("⏳ Waiting for food service...")

        self.get_logger().info("✅ Connected to Food Service")


    def send_request(self, item):
        request = FoodOrder.Request()
        request.item_name = item
        return self.client.call_async(request)


def main():
    rclpy.init()
    node = FoodServiceClient()

    while True:
        print("\n📋 MENU: pizza | burger")
        item = input("Enter item (or 'exit'): ").strip()

        if item == "exit":
            print("👋 Exiting...")
            break

        future = node.send_request(item)

        node.get_logger().info("📡 Sending request...")

        rclpy.spin_until_future_complete(node, future)

        if future.result() is not None:
            print(f"🤖 Response: {future.result().status}")
        else:
            print("⚠ Service call failed")

    rclpy.shutdown()
