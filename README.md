
This project was part of my cloud learning journey a hands-on exercise deploying a dynamic PHP café website on an AWS EC2 instance using the LAMP stack. The goal? Enable customers to place online orders from a custom-built web app hosted in the cloud.

## 🚀 What I Did

### 🛠️ Setup & Deployment

- **Launched an EC2 instance** with Amazon Linux and connected via the Cloud9 IDE.
- **Analyzed the LAMP stack environment**, confirming Apache, PHP, and MariaDB were working properly.
- **Installed a dynamic PHP web application** using Secrets Manager for database credentials.
- **Tested and troubleshot** the application until it was fully functional.
- **Created a custom AMI** of the configured instance.
- **Launched a second EC2 instance** in another region to simulate production and development environments.
- Now... **customers can place online orders through the café website! 🍽️**

### 🌍 Multi-Region Architecture

- Used a custom Amazon Machine Image (AMI) to **clone the setup** into a new region.
- Created separate **development and production environments** using EC2.

