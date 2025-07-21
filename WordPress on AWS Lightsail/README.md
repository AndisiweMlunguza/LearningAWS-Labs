**WordPress on AWS Lightsail**

This project demonstrates the deployment of a fully functional **WordPress blog** on **AWS Lightsail**, providing an affordable, beginner-friendly, and scalable hosting solution for personal or small business websites.

**Project Overview**

**Goal:** Deploy a WordPress blog using AWS Lightsail and make it publicly accessible via a static IP and custom domain (optional).

**Platform Used:**  
- [AWS Lightsail](https://aws.amazon.com/lightsail/) – simplified cloud platform by AWS

**Key Features**

-  One-click deployment of WordPress instance on AWS Lightsail
-  Configured static IP address for stable public access
-  Performed basic WordPress setup (themes, plugins, security)
-  Regular snapshot backups configured

## Technologies & Services Used

| Service/Tool     | Purpose                        |
|------------------|--------------------------------|
| AWS Lightsail     | VPS hosting with WordPress blueprint |
| WordPress         | CMS for blog publishing       |
| SSH (via terminal) | Server configuration and SSL setup |
---

## Steps Performed

1. **Created Lightsail Instance**
   - Selected WordPress blueprint
   - Chose instance size and region

2. **Connected via SSH**
   - Logged in using Lightsail browser-based SSH
   - Retrieved WordPress admin password

3. **Assigned Static IP**
   - Attached to the instance for permanent public access

4. **Customized WordPress**
   - Chose theme, installed essential plugins (e.g., security, SEO)
   - Set up pages, categories, and menus

5. **Created Snapshot**
   - Enabled automatic backups for disaster recovery

---

## Screenshots

> _(Add screenshots here if available: WordPress dashboard, Lightsail console, domain in browser with HTTPS)_

---

## Lessons Learned

- Basic VPS management and SSH usage
- Understanding WordPress hosting architecture
- Configuring SSL and domain mapping- I learnt about this step but did not configure SSL and domain mapping, still exploring free options to do so.
- Importance of backups and snapshots
- How to troubleshoot WordPress login and permission issues

---

## Useful Commands

```bash
# Access Bitnami application credentials (optional)
cat /home/bitnami/bitnami_application_password

