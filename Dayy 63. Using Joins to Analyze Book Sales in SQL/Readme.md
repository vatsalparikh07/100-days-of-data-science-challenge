# Day 63. 100 Days of Data Science Challenge - 04/04/2025

# Gravity Books: Using Joins to Analyze Book Sales in SQL

This project uses SQL joins to extract deep insights from a fictional bookstore database, "Gravity Books." By linking multiple tables—including customer data, order records, and order history—it’s possible to understand customer behavior, track order progress, and identify trends in book sales and returns.

---

## Overview

The goal of this project is to demonstrate how multiple SQL joins can reveal insights that are hidden when looking at isolated tables. This is achieved by:

- **Exploring the Database Structure:** Understanding how the tables interrelate.
- **Analyzing Order Histories:** Tracking the status evolution of orders.
- **Identifying Key Customer Behaviors:** Determining which customers frequently return orders.
- **Profiling Order Statuses:** Mapping status codes from the order history with meaningful descriptions from the lookup tables.

*By Vatsal Parikh*

---

## Database Structure and Relationships

The Gravity Books database is designed to mimic a real-world bookstore environment. Its main components include:

- **customer:** Contains details like `customer_id`, `first_name`, `last_name`, and `email`.
- **cust_order:** Logs all orders made by customers.
- **order_history:** Records every status change an order goes through (e.g., order received, delivered, returned).
- **order_status:** Maps numerical `status_id` values to descriptive status strings (e.g., Order Received, Delivered, Returned).
- **address_status:** Explains the state of shipping addresses.

### Visual Representation

![Database Structure](https://cdn.mathpix.com/cropped/2025_04_05_ab204f5cc1cdd0c16c88g-2.jpg?height=946&width=1706&top_left_y=155&top_left_x=181)

This diagram illustrates the core relationships:
- `customer` → `cust_order`
- `cust_order` → `order_history`
- `order_history` ↔ `order_status`
- Additional context is provided via the `address_status` table.

---

## SQL Analysis Methodology

### 1. Exploring the Customer Data

The first step involved a simple query to inspect customer data:
```SELECT * FROM customer LIMIT 10;```


This confirmed the structure of the customer information, featuring key fields like `customer_id`, `first_name`, `last_name`, and `email`.

### 2. Understanding Order Statuses

Before joining tables, it’s essential to understand the different order statuses. A quick lookup of the `order_status` table provides clarity on the meaning of each status ID:

```SELECT * FROM order_status;```

_Status codes:_
- `1`: Order Received
- `2`: Pending Delivery
- `3`: Delivery In Progress
- `4`: Delivered
- `5`: Cancelled
- `6`: Returned

### 3. Investigating Order History

The `order_history` table is the heartbeat of order tracking:
- Multiple entries per `order_id` capture the evolution of an order’s status.
- Special focus is given to entries where `status_id = 6` (indicating orders that were returned).

### 4. Joining Tables to Unveil Customer Behavior

#### Basic Join: Linking Orders with Order Histories

To analyze how orders progress, we join `cust_order` with `order_history`:

```
SELECT *
FROM cust_order
JOIN order_history ON order_history.order_id = cust_order.order_id
WHERE cust_order.order_id = 4412;
```


This join verifies that each order from `cust_order` is accompanied by its historical status changes.

#### Aggregating Returned Orders per Customer

One key analytic focuses on seeing which customers have a propensity to return orders. The query below aggregates returned orders and orders customers from most to least returns:

```
SELECT cust_order.customer_id, COUNT(order_history.order_id) AS returned_orders
FROM cust_order
JOIN order_history ON order_history.order_id = cust_order.order_id
WHERE order_history.status_id = 6
GROUP BY cust_order.customer_id
ORDER BY returned_orders DESC;
```

#### Extending the Join with Customer Data

To generate customer profiles for those with multiple returns, we extend the join to include details from the `customer` table:

```
SELECT customer.first_name, customer.last_name, customer.email,
cust_order.customer_id, COUNT(order_history.order_id) AS returned_orders
FROM cust_order
JOIN order_history ON order_history.order_id = cust_order.order_id
LEFT JOIN customer ON customer.customer_id = cust_order.customer_id
WHERE order_history.status_id = 6
GROUP BY cust_order.customer_id, customer.first_name, customer.last_name, customer.email
HAVING COUNT(order_history.order_id) > 1
ORDER BY returned_orders DESC;
```


### Visual Output: Customer Return Profile

![Customer Return Analysis](https://cdn.mathpix.com/cropped/2025_04_05_ab204f5cc1cdd0c16c88g-5.jpg?height=798&width=1440&top_left_y=492&top_left_x=157)

The image above showcases a summarized view of customers who often return orders—an essential insight for understanding and potentially addressing recurring issues.

---

## Key Insights

- **Interconnected Data:** The effective use of joins reveals a rich, interconnected narrative of customer behavior and order progression.
- **Customer Patterns:** A small subset of customers is returning multiple orders, indicating potential areas for further investigation, such as product quality or customer service issues.
- **Database Design:** The thoughtful organization of tables—linking customer, order, and status data—enables a seamless process to track order evolution and identify anomalies.
- **Business Applications:** Insights from these queries can inform decision-making processes to improve customer satisfaction and reduce returns.

---

## Conclusion

This project demonstrates the power of SQL joins for unlocking hidden insights in a relational database. By linking customers to their orders and tracking each order’s history, we gain a comprehensive view of the customer journey and order performance within the fictional Gravity Books database. These insights can help improve operational strategies, streamline workflows, and ultimately enhance the customer experience.
