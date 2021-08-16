# Wi-FI Map

## Requirements

- pipenv version 2021.5.29

## Setup

Download vendors information

```
curl https://devtools360.com/en/macaddress/vendorMacs.xml\?download\=true > mac_vendors.xml
```

Run script:

```
pipenv run python3 main.py mac_vendors.xml airodump_out.csv
```
