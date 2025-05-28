# ☁️ AWS Cloud Café Deployment Project

This project was part of my cloud learning journey — a hands-on exercise deploying a dynamic PHP café website on an AWS EC2 instance using the LAMP stack. The goal? Enable customers to place online orders from a custom-built web app hosted in the cloud.

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

## 🧪 Common Errors & What I Learned

I ran into quite a few roadblocks that turned into valuable lessons:

| ❌ Error Message | 💡 What Fixed It |
|------------------|------------------|
| `ERROR 2002: Can't connect to local MySQL server through socket` | MySQL wasn't running — started the service using `sudo systemctl start mariadb`. |
| `Access denied for user 'root'@'localhost'` | Adjusted user privileges using `ALTER USER` and verified the plugin method. |
| `ERROR 1698: Access denied for user 'admin'@'localhost'` | Ensured the admin user existed, updated the password, and assigned proper plugins. |
| HTTP 500 - Internal Server Error | Found via logs (`/var/log/php-fpm/www-error.log`) that missing DB credentials were causing the crash. |
| PHP error: `Access denied for user ''@'localhost'` | Credentials were not loading because the EC2 instance had **no IAM role** attached. |

**Biggest Lesson**: Sometimes the fastest fix is a fresh start. I wiped the instance, reinstalled everything from scratch, and made sure to **attach an IAM role with Secrets Manager permissions** right away.

## 🔐 Security & Best Practices

- Used **AWS Secrets Manager** to store sensitive values like DB credentials.
- Applied **least privilege IAM policies** and only allowed necessary services access to secrets.

## 📚 Key Concepts Practiced

- EC2 provisioning & SSH/IDE access
- LAMP stack validation
- Dynamic web app deployment with PHP & MariaDB
- IAM role attachment & permission troubleshooting
- Secrets Manager integration in PHP
- AMI creation & multi-region deployment
- Basic front-end editing & PHP debugging

## 📸 Screenshots
[image](https://github.com/user-attachments/assets/6310ce91-97b4-49cd-ab9f-f132c346a698)

## 📌 Tech Stack

- Amazon EC2
- Amazon Linux 2
- Apache
- PHP 7+
- MariaDB
- AWS Secrets Manager
- Cloud9 IDE
- Custom AMI
- IAM Roles

### 🧑‍💻 Still learning. Still building.
