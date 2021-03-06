Parts Implemented by Muhammed Raşit EROL
========================================

In this section, there are three main page that are firm
pages, driver pages and vehicle pages. Furthermore, other
components are listed in this section.

Firm Pages
------------------

Firms are another user type and they have home page for operations on related tables which are vehicles and drivers.
Also, adding expeditions is performed from firm home page.

Firm Home Page
^^^^^^^^^^^^^^^^

In this page, firms can see its information and several operations
can be performed. This page is kind of user page. However, with the firm
home page, related expedition operations are performed easily.

You can see the firm home page below.

.. figure:: images/member2/homepage.PNG
     :scale: 75 %
     :alt: Home Page for Firm

     Figure 1 - Home Page for Firm


Signup Page
^^^^^^^^^^^^

The firms are added to system with the firm signup page.
Because they are another type of users.


You have to give all of the requested information in the signup page of firms.
These information will be hold in firms table.
Firm name, firm password, firm email and phone fields are necessary.
Password is stored after hashing in database.
Furthermore, city comes from city table. There is CAPTCHA control.
Also,firms have logo and images (can be multiple)
Submission is checked with js and validation is checked with that.

You can see the signup page of firms below.

.. figure:: images/member2/signup.png
     :scale: 75 %
     :alt: Signup for Firm

     Figure 2 - Signup for Firm


Login page
^^^^^^^^^^^

The firms are logged in to system with the firm login page.
It is required that firm user have to be logged in successfully.
If you try to access a page that requires an authorization without being logged in,
system redirects you to the login page with error.

You can see the login page of firms below.

.. figure:: images/member2/login.PNG
     :scale: 75 %
     :alt: Login for Firm

     Figure 3 - Login for Firm

Edit Firm Page
^^^^^^^^^^^^^^^^

It is possible to edit the firms information using firm edit page.
The preview part contains database information.
Hence, firm can see its old information.

You can see the firm edit page of firms below.

.. figure:: images/member2/edit.PNG
     :scale: 75 %
     :alt: Edit Firm Page

     Figure 4 - Edit Firm Page


Firms List Page
^^^^^^^^^^^^^^^^^

It is possible to list all firms in the system. However, only admin can see all firms.
In this page, deletion operation is possible for admin. Furthermore, all attributes can
be seen in this page.

You can see the firm list page of firms below.


.. figure:: images/member2/firm_list.PNG
     :scale: 75 %
     :alt: Firm List Page

     Figure 5 - Firm List Page


Driver Pages
------------------

Driver are members of the firms. Hence, a firm can have driver. It is possible to
add, list, delete and edit drivers for firms.

Driver Add Page
^^^^^^^^^^^^^^^^^

A firm can add driver to the system with the driver add page.

.. figure:: images/member2/add_driver.PNG
     :scale: 75 %
     :alt: Add Driver Page

     Figure 6 - Add Driver Page


Driver List Page
^^^^^^^^^^^^^^^^^

A firm can list drivers of its with the driver list page.
In this page, it is possible to delete and edit the drivers.
Deletion is performed immediately and editing is performed in
driver edit page.

.. figure:: images/member2/driver_list.PNG
     :scale: 75 %
     :alt: Driver List Page

     Figure 7 - Driver List Page


Driver Edit page
^^^^^^^^^^^^^^^^^

In this page, a firm can edit its driver's information.

.. figure:: images/member2/edit_driver.PNG
     :scale: 75 %
     :alt: Driver Edit Page

     Figure 8 - Driver Edit Page

Vehicle Pages
------------------

Vehicles are members of the firms. Hence, a firm can have vehicle. It is possible to
add, list, delete and edit vehicles for firms.

Vehicle Add Page
^^^^^^^^^^^^^^^^^

A firm can add vehicle to the system with the vehicle add page.

.. figure:: images/member2/add_vehicle.PNG
     :scale: 75 %
     :alt: Add Vehicle Page

     Figure 9 - Add Vehicle Page


Vehicle List Page
^^^^^^^^^^^^^^^^^

A firm can list vehicles of its with the vehicle list page.
In this page, it is possible to delete and edit the vehicles.
Deletion is performed immediately and editing is performed in
vehicle edit page.

.. figure:: images/member2/vehicle_list.PNG
     :scale: 75 %
     :alt: Vehicle List Page

     Figure 10 - Vehicle List Page


Vehicle Edit page
^^^^^^^^^^^^^^^^^

In this page, a firm can edit its vehicle's information.

.. figure:: images/member2/edit_vehicle.PNG
     :scale: 75 %
     :alt: Edit Vehicle Page

     Figure 11 - Edit Vehicle Page





