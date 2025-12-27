# GearGuard: The Ultimate Maintenance Tracker ⚙️🛡️

**GearGuard** is a robust Odoo module designed to streamline asset management and maintenance workflows. It provides a centralized dashboard for tracking equipment status, managing maintenance requests, and assigning tasks to technicians, ensuring your inventory is always operational.

---

## 📋 Table of Contents
* [About the Project](#about-the-project)
* [Key Features](#key-features)
* [Project Directory Structure](#project-directory-structure)
* [Prerequisites](#prerequisites)
* [Installation & Setup](#installation--setup)
* [Usage Guide](#usage-guide)
* [Screenshots](#screenshots)

---

## 📖 About the Project

GearGuard solves the chaos of unorganized maintenance logs. Instead of spreadsheets or sticky notes, GearGuard offers a structured system where:
* **Assets** (machinery, electronics, vehicles) are cataloged.
* **Maintenance Requests** are tracked from reporting to resolution.
* **Technicians** are assigned and managed efficiently.
* **Status Updates** happen in real-time, preventing operational downtime.

Built on the **Odoo 17** framework (compatible with v14+), it leverages Odoo's powerful ORM and Kanban views to deliver a modern, intuitive interface.

---

## ✨ Key Features

### 1. 📊 Interactive Dashboard
* **Kanban View:** Drag-and-drop maintenance requests across stages (New, In Progress, Completed).
* **Priority Tracking:** Visual indicators for High/Critical priority tasks.
* **Quick Overview:** See who is assigned to what task instantly.

### 2. 📦 Asset Inventory Management
* **Detailed Records:** Track Asset Name, ID Code, Category, Purchase Date, and Location.
* **Status Indicators:** Auto-tag assets as "Operational," "Under Maintenance," or "Retired."
* **History Log:** View the entire repair history of any specific asset linked directly to its profile.

### 3. 🛠️ Maintenance Workflow
* **Request System:** Employees can submit requests with issue descriptions and priority levels.
* **Assignment Logic:** Managers can assign specific technicians to requests.
* **Stage Automation:** Moving a request to "Completed" automatically updates the Asset status back to "Operational."
* **Chatter:** Built-in messaging and logging on every request (Odoo standard).

---

## 📂 Project Directory Structure

```text
custom_addons/
└── gear_guard/
    ├── __init__.py
    ├── __manifest__.py
    │
    ├── controllers/
    │   ├── __init__.py
    │   └── controllers.py
    │
    ├── demo/
    │   └── demo.xml
    │
    ├── models/
    │   ├── __init__.py
    │   ├── equipment.py
    │   ├── maintenance_request.py
    │   ├── team.py
    │   └── models.py
    │
    ├── security/
    │   └── ir.model.access.csv
    │
    ├── views/
    │   ├── equipment_views.xml
    │   ├── maintenance_request_views.xml
    │   ├── team_views.xml
    │   ├── menu.xml
    │   ├── views.xml
    │   └── templates.xml
    │
    └── __pycache__/


```
---

## ✅ Prerequisites

Before installing, ensure you have the following:

* **Odoo Installed:** Version 14, 15, 16, or 17 (Community or Enterprise).

* **Python 3.x:** (Standard with Odoo installation).

* **PostgreSQL:** Database server running.

---

## ⚙️ Installation & Setup

**Step 1: Clone or Download**
  
Download the gearguard folder and place it into your Odoo addons directory.

```
cd /path/to/your/odoo/addons
# If using git
git clone [https://github.com/yourusername/gearguard.git](https://github.com/yourusername/gearguard.git)

```
**Step 2: Update Odoo Configuration**

If you placed the folder in a custom directory, add that path to your odoo.conf file:

```
addons_path = /usr/lib/python3/dist-packages/odoo/addons,/path/to/your/custom/addons
```
**Step 3: Restart Odoo Server**

Restart the Odoo service to recognize the new module.

```
sudo service odoo restart
# Or if running manually
./odoo-bin -c odoo.conf
```
**Step 4: Install Module in Odoo**

* Log in to your Odoo database as Administrator.

* Enable Developer Mode (Settings > Scroll down > Activate the developer mode).

* Go to Apps in the main menu.

* Click Update Apps List in the top bar.

* Search for GearGuard.

* Click Activate / Install.


---

## 🚀 Usage Guide

**Add Assets:**

* Go to GearGuard > Assets.

* Click New to register a machine or tool.

**Create a Request:**

* Go to GearGuard > Dashboard.

* Click New to report an issue. Select the Asset and set Priority.

**Manage Workflow:**

* Drag the request card from New Request to In Progress when a technician starts working.

* Open the request to assign a specific Technician.

* Drag to Completed when done. This will automatically mark the asset as "Operational" again.

---

## Screenshots

* **Dashboard**

![Dashboard](https://github.com/user-attachments/assets/ba7e5650-4633-49ee-ab2d-c62fe75d6f93)


* **Equipments**

![Equipments](https://github.com/user-attachments/assets/0f9fe002-6db3-40e8-9744-31466cd59308)


* **Teams**

![Teams](https://github.com/user-attachments/assets/2690276c-295e-464b-ab54-678ce0ddfa4b)

* **Add new Team**

![Add new Team](https://github.com/user-attachments/assets/0fb935a1-d61b-4c4d-b7d5-e86a5573fbd8)

* **Add new Equipments**

![Add new Equipments](https://github.com/user-attachments/assets/36cecfff-e426-4b9a-ba30-09e73f76b843)

* **Add new maintenance request**

![Add new maintenance request](https://github.com/user-attachments/assets/e97539af-108c-40f8-9187-66e515bfb344)

---

## Team Members 

* Palak Goyal

* Mrunali Kamerikar

* Riddhima Taose

* Viral Agrawal 
