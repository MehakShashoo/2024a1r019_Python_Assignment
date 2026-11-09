#  Smart Parcel Dispatch and Delivery Tracker

A console-based parcel management application developed using **Python** as part of a five-milestone programming assignment.

##  About the Project

This application helps manage parcel dispatch operations by accepting parcel details, calculating delivery charges, estimating delivery time, and maintaining dispatch records.

##  Features

- Manage multiple parcel details.
- Calculate delivery charges based on weight and distance.
- Support Standard and Express delivery services.
- Classify parcels by weight.
- Estimate delivery time.
- Generate dispatch summaries and sort parcels by distance.
- Save and display records using file handling.
- Handle errors using exception handling.

##  Technologies Used

- Python 3
- Visual Studio Code
- Python Standard Library (`math`)

## 📂 Project Structure

```text
Smart_Parcel_Dispatch_Tracker/
│
├── main.py
├── delivery_utils.py
├── parcel_records.txt
└── README.md
```

| File | Description |
|---|---|
| `main.py` | Main application containing classes and program execution. |
| `delivery_utils.py` | Contains reusable functions and file operations. |
| `parcel_records.txt` | Stores completed parcel records. |


**4.** Enter parcel details and type `DONE` as the Parcel ID to finish dispatch.

## 📚 Python Concepts Used

- Data types and operators
- Lists and dictionaries
- Loops and conditional statements
- Functions and lambda expressions
- Classes, inheritance and polymorphism
- Modules and imports
- File handling and exception handling

## ⚠️ Exception Handling

| Exception | Purpose |
|---|---|
| `ValueError` | Handles invalid numeric input. |
| `KeyError` | Handles unavailable delivery services. |
| `FileNotFoundError` | Handles a missing parcel records file. |

## 🎯 Conclusion

This project demonstrates the practical application of Python programming concepts to develop a structured parcel dispatch management system.

---

**Developed as part of a Python Programming Assignment.**
