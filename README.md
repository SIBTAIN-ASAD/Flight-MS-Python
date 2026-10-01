# Flight Booking Management System

A terminal-based Python application for managing flight customers, destinations, bookings, optional services, and membership discounts. Data is stored in plain-text, comma-separated files, so the project runs without a database or third-party packages.

## Features

- Create bookings for registered customers
- Register standard, member, and VIP customers
- Apply member and threshold-based VIP discounts
- Add destinations and track available seats
- Attach individual services or service bundles to a booking
- List customers, destinations, services, bundles, and bookings
- Report the most valuable customer and most popular destination
- Load a different set of data files from command-line arguments

## Requirements

- Python 3
- A terminal that supports interactive input

The application uses only the Python standard library.

## Run the sample application

Clone the repository and start the menu from its root directory:

```bash
git clone https://github.com/SIBTAIN-ASAD/Flight-MS-Python.git
cd Flight-MS-Python
python3 code.py
```

The included sample data is loaded from:

- `customers.txt`
- `destinations.txt`
- `services.txt`
- `bookings.txt`

Some menu actions append records to these files. If you want to preserve the sample data, work on copies and pass their paths explicitly:

```bash
mkdir -p /tmp/flight-ms-demo
cp customers.txt destinations.txt services.txt bookings.txt /tmp/flight-ms-demo/
python3 code.py \
  /tmp/flight-ms-demo/customers.txt \
  /tmp/flight-ms-demo/destinations.txt \
  /tmp/flight-ms-demo/services.txt \
  /tmp/flight-ms-demo/bookings.txt
```

The four file arguments must be supplied in this order: customers, destinations, services, and bookings. If no arguments are supplied, the files in the current directory are used.

## Menu

The interactive menu can:

1. Book a trip
2. Display customers
3. Display destinations
4. Add a customer
5. Add a destination
6. Display bookings
7. Display services and bundles
8. Display the most valuable customer
9. Display the most popular destination

Enter `q` to exit.

## Data model

The implementation is organized around a small set of classes in `code.py`:

| Class | Responsibility |
| --- | --- |
| `Customer`, `Member`, `VIPMember` | Customer identity, value, membership, and discount rules |
| `Destination` | Ticket price and available seats |
| `Service`, `Bundle` | Optional booking services |
| `Booking` | Customer, destination, service, discount, and date for one trip |
| `Records` | File loading, lookup, storage, and aggregate reports |
| `MenuDriverClass` | Interactive menu and booking workflow |

Customer IDs use `C`, `M`, or `V` prefixes for standard customers, members, and VIP members. Destination, service, and bundle IDs use `D`, `S`, and `B` prefixes respectively.

## Data files

Each record is comma-separated. For example:

```text
# customers.txt
C1, James, 0, 100
M3, Tom, 0.1, 500

# destinations.txt
D1, Sydney, 150, 30

# services.txt
S1, Internet, 0
B8, StarterMax, S1, S2, S3, S4

# bookings.txt
James, D1, 1, S1, 0, 12/12/2021 12:12:12
```

## Validation

Check that the source parses without running the interactive menu:

```bash
python3 -m py_compile code.py
```

## Project scope

This project was built as a programming-fundamentals exercise. It favors a single-file, object-oriented implementation and text-file persistence so the customer, booking, inheritance, and menu workflows remain easy to inspect.
