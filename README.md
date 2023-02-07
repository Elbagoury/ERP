## Enterprise Resource Planning System (ERP)
Enterprise Resource Planning (ERP) is a type of software used by a business to plan and manage daily activities such as supply chain, accounting and sales, also it can be used to automate and simplify individual activities across the business.

This project was built with the latest software technologies using Python & Javascript, and was built on the basis of extensive scientific research as it was part of a Mohamed Elbagoury master's degree.

## Installation
### Python
ERP requires Python 3.8 or later to run. Use your package manager to download and install Python 3 on your machine if it is not already done

```sh
python3 --version
```
```sh
pip3 --version
```
### PostgreSQL
ERP  uses PostgreSQL as database management system. Use your package manager to download and install PostgreSQL (supported version: 11.0 and later).
On Debian/Unbuntu, it can be achieved by executing the following:
```sh
sudo apt install postgresql postgresql-client
```
By default, the only user is postgres but ERP forbids connecting as postgres, so you need to create a new PostgreSQL user:
```sh
 sudo -u postgres createuser -s erp
```
### ERP Code
Copy the ERP code to your machine by executing the following:

```sh
 git clone git@github.com:Elbagoury/ERP.git
```

### Dependencies
For libraries using native code, it is necessary to install development tools and native dependencies before the Python dependencies of ERP. They are available in -dev or -devel packages for Python, PostgreSQL, libxml2, libxslt1, libevent, libsasl2 and libldap2.
On Debian/Unbuntu, the following command should install all the required libraries:
```sh
  sudo apt install python3-dev libxml2-dev libxslt1-dev libldap2-dev libsasl2-dev \
    libtiff5-dev libjpeg8-dev libopenjp2-7-dev zlib1g-dev libfreetype6-dev \
    liblcms2-dev libwebp-dev libharfbuzz-dev libfribidi-dev libxcb1-dev libpq-dev
```
ERP  dependencies are listed in the [requirements.txt](requirements.txt)

```sh
 pip3 install -r requirements.txt
```
### Running ERP
Once all dependencies are set up, ERP can be launched by running [erp-bin](erp-bin), the command-line interface of the server.

```sh
 ./erp-bin
```
## License

GNU/General Public License (see [license.txt](license.txt))

The ERP code is licensed as GNU General Public License (v3) and the Documentation is licensed as Creative Commons (CC-BY-SA-3.0) and the copyright is owned by Mohamed Elbagoury and Contributors.

By contributing to ERP, you agree that your contributions will be licensed under its GNU General Public License (v3).

