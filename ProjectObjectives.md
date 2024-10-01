
# Project Objectives - EcommLite

EcommLite is a minimal e-commerce platform built using microservices architecture. The main focus is to learn and implement end-to-end microservice architecture with event-driven methods. The project will be divided into two primary services:

## 1. User Management and Product Display Service (Django)
This service is responsible for user registration, login, and product catalog display. Key features:
- **User Registration and Authentication**: Minimal registration form with email and password.
- **User Login**: Basic login mechanism with session or token-based authentication.
- **Product Display**: A simple product listing page with product names, descriptions, and prices.

## 2. Payment Gateway Service (FastAPI)
This service handles payment activities using dummy data to mock real-world payment processes. Key features:
- **Payment Processing**: Minimal payment form that collects user payment details (mocked).
- **Encryption**: Basic encryption of sensitive payment information.
- **Event-Driven Payment Status Update**: Simulated event-driven mechanism to update order/payment status.

## Overall Architecture
- **Microservices Communication**: Services communicate via HTTP or an event-driven messaging system like RabbitMQ or Redis Pub/Sub.
- **Event-Driven Methods**: When a user makes a purchase, the payment service sends a payment update event to the user-management service.
- **Dockerized Setup**: Each service will be containerized using Docker to ensure easy deployment and scalability.

## Learning Objectives
1. **Microservices Architecture**: Implement a basic microservice-based e-commerce platform.
2. **Event-Driven Architecture**: Use an event-driven approach to simulate real-time communication between services.
3. **Minimal Features**: Ensure that all services are minimal yet functional to keep the learning curve focused.
