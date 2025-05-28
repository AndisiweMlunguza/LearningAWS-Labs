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
