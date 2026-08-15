## DEVELOPMENT REPORT

## for

## Nintventario

Version 1.0 approved

Prepared by Andr´es Alfredo Cornejo Figueroa Jorde Daniel Mawyin Cabay Kevin Ariel Rold´an Pilozo Angel Alexander Tomal´a Moreno

Team 1

August 18, 2024

1

# Abstract

This document detailed the process undertaken to establish a necessary product for the company ”Pricotercorp S.A.,” a franchise specializing in video games, manga, and other pop culture items. One of the main issues the company faced was inventory management, which became cumbersome when adding, updating, and/or reviewing products. To address this, a proposal was presented to optimize these tasks. Additionally, a process to construct a website was initiated to facilitate remote product visualization for customers, aiming to increase the business’s clientele. The document also discussed the selection of appropriate tools to meet the functional and non-functional requirements of the system, encompassing both the mobile inventory module and the web module. The MoSCoW classification was used for functional requirements, and the Sommerville classification was applied for non-functional requirements. Testing was conducted to ensure system reliability and performance, and static analysis was performed to identify and rectify potential issues in the code. The main client for this project was Joffre Morales, owner of PRICOTERCORP S.A., a company with multiple points of sale in Guayas provinces, currently advertising through Instagram and Facebook. The proposed system was intended to streamline inventory management for employees and provide an enhanced online platform for customers to view and reserve products.

2

# Contents

1 Introduction 19

1. 1 Project context . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19

2 Relevant Architectural Decisions 20

2. 1 Teamwork Management Tool. . . . . . . . . . . . . . . . . . . . . . . . . 20

2. 2 Database. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21

2. 3 Web Frontend Framework. . . . . . . . . . . . . . . . . . . . . . . . . . . 22

2. 4 Web Backend Framework. . . . . . . . . . . . . . . . . . . . . . . . . . . 23

2. 5 Mobile Development Framework. . . . . . . . . . . . . . . . . . . . . . . 24

2. 6 Coding Standards / PMD Tool for Django . . . . . . . . . . . . . . . . . . 25

2. 7 Coding Standards Tool for Angular . . . . . . . . . . . . . . . . . . . . . . 26

2. 8 PMD Tool for Angular . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27

2. 9 Coding Standards / PMD Tool for Flutter . . . . . . . . . . . . . . . . . . 28

2. 10 Authentication and Access Control Framework. . . . . . . . . . . . . . . 29

2. 11 Continuous Integration Tool . . . . . . . . . . . . . . . . . . . . . . . . . . 30

2. 11.1 Mobile Module - Github Actions. . . . . . . . . . . . . . . . . . . 30

2. 11.2 Mobile Module - Github Actions. . . . . . . . . . . . . . . . . . . 32

2. 12 Testing Tools. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33

2. 12.1 Mobile Module. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33

2. 12.2 Web Module. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35

3 SCRUM Evidence 39

3. 1 Roles Definition . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 39

3. 1.1 Product Owner . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 39

3. 1.2 Scrum Master . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 39

3. 1.3 Development Team . . . . . . . . . . . . . . . . . . . . . . . . . . . 39

3. 2 Product Backlog. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40

3. 3 Sprint 1. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 42

3. 3.1 Sprint Backlog. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 42

3. 3.2 Sprint Review . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 43

3. 3.3 Sprint Retrospective. . . . . . . . . . . . . . . . . . . . . . . . . . 44

3. 3.4 Burndown Chart. . . . . . . . . . . . . . . . . . . . . . . . . . . . 45

3. 4 Sprint 2. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 46

3. 4.1 Sprint Backlog. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 46

3. 4.2 Sprint Review . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 47

3. 4.3 Sprint Retrospective. . . . . . . . . . . . . . . . . . . . . . . . . . 48

3. 4.4 Burndown Chart. . . . . . . . . . . . . . . . . . . . . . . . . . . . 49

3

3. 5 Sprint 3. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 50

3. 5.1 Sprint Backlog. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 50

3. 5.2 Sprint Review . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 51

3. 5.3 Sprint Retrospective. . . . . . . . . . . . . . . . . . . . . . . . . . 52

3. 5.4 Burndown Chart. . . . . . . . . . . . . . . . . . . . . . . . . . . . 53

3. 6 Sprint 4. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 54

3. 6.1 Sprint Backlog. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 54

3. 6.2 Sprint Review . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 55

3. 6.3 Sprint Retrospective. . . . . . . . . . . . . . . . . . . . . . . . . . 56

3. 6.4 Burndown Chart. . . . . . . . . . . . . . . . . . . . . . . . . . . . 57

4 Coding Standards Documentation 58

4. 1 Coding Standards - Mobile Module . . . . . . . . . . . . . . . . . . . . . . 58

4. 1.1 Naming Convention and Organization. . . . . . . . . . . . . . . . 58

4. 1.2 Formatting and Indentation . . . . . . . . . . . . . . . . . . . . . . 58

4. 1.3 Comments and Documentation. . . . . . . . . . . . . . . . . . . . 59

4. 1.4 Exception Handling / Logging. . . . . . . . . . . . . . . . . . . . 59

4. 1.5 Testing. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 60

4. 2 Coding Standards - Web Module. . . . . . . . . . . . . . . . . . . . . . . 61

4. 2.1 Backend . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 61

4. 2.2 Apply code standards - Backend. . . . . . . . . . . . . . . . . . . 63

4. 2.3 Frontend. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 65

4. 2.4 Apply code standards - Frontend . . . . . . . . . . . . . . . . . . . 67

5 Preemptive Error Detection 71

5. 1 Preemptive Error - Mobile Module. . . . . . . . . . . . . . . . . . . . . . 71

5. 1.1 Backend . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 71

5. 1.2 Frontend. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 72

5. 2 Preemptive Error - Web Module. . . . . . . . . . . . . . . . . . . . . . . 75

5. 2.1 Backend . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 75

5. 2.2 Frontend. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 75

6 Mobile Module Test Documentation 79

6. 1 Test plan. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 79

6. 2 Test case specification. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 84

6. 2.1 Unit Test Cases . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 84

6. 2.2 Acceptance Testing . . . . . . . . . . . . . . . . . . . . . . . . . . . 103

6. 3 Test data requirements . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 117

6. 4 Test environment requirements. . . . . . . . . . . . . . . . . . . . . . . . 117

6. 5 Test result . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 117

6. 6 Incident report. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 125

7 Web Module Test Documentation 127

7. 1 Test plan. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 127

4

7. 2 Test case specification. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 132

7. 2.1 Unit Test Cases: Frontend . . . . . . . . . . . . . . . . . . . . . . . 132

7. 2.2 Unit Test Cases: Backend Testing. . . . . . . . . . . . . . . . . . 174

7. 2.3 Acceptance Testing: Frontend . . . . . . . . . . . . . . . . . . . . . 195

7. 2.4 Acceptance Testing: Backend . . . . . . . . . . . . . . . . . . . . . 197

7. 3 Test Data Requirements . . . . . . . . . . . . . . . . . . . . . . . . . . . . 198

7. 4 Test Environment Requirements. . . . . . . . . . . . . . . . . . . . . . . 198

7. 5 Test result . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 198

7. 6 Incident report. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 205

8 Individual Contribution 210

9 Appendix 211

9. 1 Appendix A: GitHub Repositories. . . . . . . . . . . . . . . . . . . . . . 211

9. 2 Appendix B: Software Building. . . . . . . . . . . . . . . . . . . . . . . . 211

9. 3 Appendix C: Project Presentation Video . . . . . . . . . . . . . . . . . . . 211

9. 4 Appendix D: Client Acceptance Letters. . . . . . . . . . . . . . . . . . . 212

9. 4.1 Sprint 1 Acceptance Letter. . . . . . . . . . . . . . . . . . . . . . 212

9. 4.2 Sprint 2 Acceptance Letter. . . . . . . . . . . . . . . . . . . . . . 213

9. 4.3 Sprint 2 Acceptance Letter. . . . . . . . . . . . . . . . . . . . . . 214

9. 4.4 Sprint 4 Acceptance Letter. . . . . . . . . . . . . . . . . . . . . . 215

9. 5 Appendix E: System Deployment Guide WM. . . . . . . . . . . . . . . . 216

9. 5.1 Introduction. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 216

9. 5.2 System Requirements. . . . . . . . . . . . . . . . . . . . . . . . . 216

9. 5.3 Installation Steps . . . . . . . . . . . . . . . . . . . . . . . . . . . . 218

9. 6 Appendix F: Installation Guide MM. . . . . . . . . . . . . . . . . . . . . 227

9. 6.1 Introduction. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 227

9. 6.2 System Requirements. . . . . . . . . . . . . . . . . . . . . . . . . 227

9. 6.3 Download Instructions . . . . . . . . . . . . . . . . . . . . . . . . . 228

9. 6.4 Installation Instructions. . . . . . . . . . . . . . . . . . . . . . . . 228

9. 6.5 Verification of Installation . . . . . . . . . . . . . . . . . . . . . . . 229

9. 6.6 Troubleshooting. . . . . . . . . . . . . . . . . . . . . . . . . . . . 230

9. 6.7 Support. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 230

9. 7 Appendix G: User Manual . . . . . . . . . . . . . . . . . . . . . . . . . . . 231

9. 7.1 Web Manual. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 231

9. 7.2 Mobile Manual. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 301

9. 8 Appendix H: Asana activity schedule . . . . . . . . . . . . . . . . . . . . . 324

5

# List of Tables

2. 1 Comparison of Teamwork Management Tool . . . . . . . . . . . . . . . . . 20

2. 2 Comparison of Database . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21

2. 3 Options Considered for the Web Frontend Framework. . . . . . . . . . . 22

2. 4 Options Considered for the Web Backend Framework . . . . . . . . . . . . 23

2. 5 Comparison of Mobile Frameworks. . . . . . . . . . . . . . . . . . . . . . 24

2. 6 Comparison of Coding Standards Tool for Django . . . . . . . . . . . . . . 25

2. 7 Comparison of Coding Standards Tools for Angular . . . . . . . . . . . . . 26

2. 8 Comparison of PMD Tool for Angular. . . . . . . . . . . . . . . . . . . . 27

2. 9 Comparison of Coding Standards Tool for Flutter . . . . . . . . . . . . . . 28

2. 10 Comparison of Authentication and Access Control Options for Django. . 29

2. 11 Comparison of Unit Testing Tools for Mobile Module . . . . . . . . . . . . 33

2. 12 Comparison of Acceptance Testing Tools for Mobile Module . . . . . . . . 34

2. 13 Comparison of Unit Testing Tools for Angular . . . . . . . . . . . . . . . . 35

2. 14 Comparison of Acceptance Testing Tools for Angular . . . . . . . . . . . . 36

2. 15 Comparison of Unit Testing Tools for Django. . . . . . . . . . . . . . . . 37

2. 16 Comparison of Acceptance Testing Tools for Django. . . . . . . . . . . . 38

3. 1 Product Backlog. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 41

3. 2 Sprint Backlog - Sprint 1. . . . . . . . . . . . . . . . . . . . . . . . . . . 43

3. 3 Sprint Backlog - Sprint 2. . . . . . . . . . . . . . . . . . . . . . . . . . . 47

3. 4 Sprint Backlog - Sprint 3. . . . . . . . . . . . . . . . . . . . . . . . . . . 51

3. 5 Sprint Backlog - Sprint 4. . . . . . . . . . . . . . . . . . . . . . . . . . . 55

6. 1 Risk Analysis for Mobile Inventory Management Application. . . . . . . 82

6. 2 Test case to verify AppBar title on the home screen. . . . . . . . . . . . 84

6. 3 Test case to verify the welcome text on the home screen. . . . . . . . . . 84

6. 4 Test case to verify the creation of inventory. . . . . . . . . . . . . . . . . 84

6. 5 Test case to verify access to history . . . . . . . . . . . . . . . . . . . . . . 85

6. 6 Test case to verify access to settings. . . . . . . . . . . . . . . . . . . . . 85

6. 7 Test case to verify app exit functionality . . . . . . . . . . . . . . . . . . . 85

6. 8 Test case for Widget Initialization. . . . . . . . . . . . . . . . . . . . . . 86

6. 9 Test case for Loading State. . . . . . . . . . . . . . . . . . . . . . . . . . 86

6. 10 Test case for Error State . . . . . . . . . . . . . . . . . . . . . . . . . . . . 86

6. 11 Test case for ”No Products Found” message . . . . . . . . . . . . . . . . . 87

6. 12 Test case for Tab Selection. . . . . . . . . . . . . . . . . . . . . . . . . . 87

6. 13 Test case for Tab Bar Labels. . . . . . . . . . . . . . . . . . . . . . . . . 87

6. 14 Test case for Tab Bar Icons. . . . . . . . . . . . . . . . . . . . . . . . . . 88

6

6. 15 Test case for Page View. . . . . . . . . . . . . . . . . . . . . . . . . . . . 88

6. 16 Test case for Tab Bar Tap Animation. . . . . . . . . . . . . . . . . . . . 88

6. 17 Test case for initial date display in DateSelectorWidget. . . . . . . . . . 89

6. 18 Test case for date picker interaction in DateSelectorWidget. . . . . . . . 89

6. 19 Test case for date selection callback in DateSelectorWidget. . . . . . . . 89

6. 20 Test case for displaying sale spot locations on SaleSpotsPage. . . . . . . 90

6. 21 Test case for selecting a location and navigation in SaleSpotsPage . . . . . 90

6. 22 Test case for logging selected location in SaleSpotsPage in debug mode . . 90

6. 23 Test case for displaying InventoryDetails widget . . . . . . . . . . . . . . . 91

6. 24 Test case for saving a draft in InventoryDetails widget. . . . . . . . . . . 91

6. 25 Test case for Draft default values . . . . . . . . . . . . . . . . . . . . . . . 92

6. 26 Test case for Draft to JSON conversion. . . . . . . . . . . . . . . . . . . 92

6. 27 Test case for saving and loading a Draft from SharedPreferences. . . . . 92

6. 28 Test case for updating a Draft in SharedPreferences. . . . . . . . . . . . 93

6. 29 Test case for loading indicator in DraftsScreen. . . . . . . . . . . . . . . 94

6. 30 Test case for empty state in DraftsScreen. . . . . . . . . . . . . . . . . . 94

6. 31 Test case for displaying drafts list in DraftsScreen . . . . . . . . . . . . . . 94

6. 32 Test case for displaying product details in ProductDetails screen. . . . . 95

6. 33 Test case for initial stock value display in ProductDetails screen . . . . . . 95

6. 34 Test case for filtering product list by state in ProductsList screen . . . . . 96

6. 35 Test case for navigating to ProductDetails from product list in Product-

sList screen. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 96

6. 36 Test case for navigating to QR scanner from ProductsList screen. . . . . 97

6. 37 Test case for Product initialization. . . . . . . . . . . . . . . . . . . . . . 98

6. 38 Test case for Product JSON serialization . . . . . . . . . . . . . . . . . . . 98

6. 39 Test case for Product JSON deserialization. . . . . . . . . . . . . . . . . 99

6. 40 Test case for barcode detection in QRScannerWidget . . . . . . . . . . . . 100

6. 41 Test case for handling barcode not found in QRScannerWidget. . . . . . 100

6. 42 Test case for camera switching in QRScannerWidget. . . . . . . . . . . . 101

6. 43 Test case for displaying product counts in ReportScreen. . . . . . . . . . 102

6. 44 Test case for editing and displaying observations in ReportScreen . . . . . 102

6. 45 Test case for verifying SaleSptosPage display. . . . . . . . . . . . . . . . 103

6. 46 Test case for navigation to Home screen from SaleSptosPage . . . . . . . . 103

6. 47 Test case for navigation to Inventory Creation screen . . . . . . . . . . . . 103

6. 48 Test case for filter selection in Inventory Creation screen . . . . . . . . . . 104

6. 49 Test case for verifying stock update in Inventory Creation screen. . . . . 104

6. 50 Test case for verifying manager name update in Inventory Details screen . 104

6. 51 Test case for verifying draft save functionality in Inventory Details screen 105

6. 52 Details of the InventoryDetails Widget Test Failure.. . . . . . . . . . . . 125

6. 53 Details of the Report Screen Test Failure.. . . . . . . . . . . . . . . . . . 126

7. 1 Risk Analysis for Product Sales Website Project. . . . . . . . . . . . . . 131

7. 2 Test case to verify app component creation. . . . . . . . . . . . . . . . . 132

7. 3 Test case to verify navbar component rendering . . . . . . . . . . . . . . . 132

7

7. 4 Test case to verify conditional rendering of banner components. . . . . . 133

7. 5 Test case to verify footer component rendering. . . . . . . . . . . . . . . 133

7. 6 Test case to verify the creation of ‘FooterComponent‘. . . . . . . . . . . 133

7. 7 Test case to verify social media links in ‘FooterComponent‘. . . . . . . . 134

7. 8 Test case to verify the creation of ‘BannerComponent‘. . . . . . . . . . . 134

7. 9 Test case to verify the creation of ‘NavbarComponent‘. . . . . . . . . . . 134

7. 10 Test case to verify menu visibility toggle in ‘NavbarComponent‘ . . . . . . 135

7. 11 Test case to verify the creation of ‘AuthService‘ . . . . . . . . . . . . . . . 135

7. 12 Test case to verify user login in ‘AuthService‘. . . . . . . . . . . . . . . . 135

7. 13 Test case to verify user registration in ‘AuthService‘. . . . . . . . . . . . 136

7. 14 Test case to verify user logout in ‘AuthService‘. . . . . . . . . . . . . . . 136

7. 15 Test case to verify login status check in ‘AuthService‘. . . . . . . . . . . 136

7. 16 Test case to verify retrieval of user information in ‘AuthService‘ . . . . . . 137

7. 17 Test case to verify initial login status emission in ‘AuthService‘. . . . . . 137

7. 18 Test case to verify the creation of ‘CartService‘. . . . . . . . . . . . . . . 137

7. 19 Test case to verify adding a new item to the cart in ‘CartService‘ . . . . . 138

7. 20 Test case to verify updating the quantity of an existing item in ‘CartService‘138

7. 21 Test case to verify removing an item from the cart in ‘CartService‘. . . . 138

7. 22 Test case to verify resetting the cart in ‘CartService‘. . . . . . . . . . . . 139

7. 23 Test case to verify updating the total number of products in the cart in

‘CartService‘. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 139

7. 24 Test case to verify ‘ContactService‘ creation . . . . . . . . . . . . . . . . . 139

7. 25 Test case to verify contact email sending . . . . . . . . . . . . . . . . . . . 140

7. 26 Test case to verify register email sending . . . . . . . . . . . . . . . . . . . 140

7. 27 Test case to verify ‘ProductService‘ creation . . . . . . . . . . . . . . . . . 141

7. 28 Test case to verify retrieval of all products . . . . . . . . . . . . . . . . . . 141

7. 29 Test case to verify retrieval of filtered products. . . . . . . . . . . . . . . 141

7. 30 Test case to verify retrieval of newest products. . . . . . . . . . . . . . . 142

7. 31 Test case to verify retrieval of bestselling products. . . . . . . . . . . . . 142

7. 32 Test case to verify ‘OrderService‘ creation. . . . . . . . . . . . . . . . . . 142

7. 33 Test case to verify order creation. . . . . . . . . . . . . . . . . . . . . . . 143

7. 34 Test case to verify purchase history retrieval . . . . . . . . . . . . . . . . . 143

7. 35 Test case to verify ‘PaymentService‘ creation. . . . . . . . . . . . . . . . 144

7. 36 Test case to verify PayPal order creation . . . . . . . . . . . . . . . . . . . 144

7. 37 Test case to verify PayPal order capture . . . . . . . . . . . . . . . . . . . 145

7. 38 Test case to verify ‘WishlistService‘ creation . . . . . . . . . . . . . . . . . 145

7. 39 Test case to verify wishlist item retrieval . . . . . . . . . . . . . . . . . . . 145

7. 40 Test case to verify ‘ContactComponent‘ creation. . . . . . . . . . . . . . 146

7. 41 Test case to verify form submission in ‘ContactComponent‘. . . . . . . . 146

7. 42 Test case to verify ‘EmailChangeConfirmationComponent‘ creation . . . . 147

7. 43 Test case to verify alert initialization in ‘EmailChangeConfirmationCom-

ponent‘. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 147

7. 44 Test case to verify navigation to login in ‘EmailChangeConfirmationCom-

ponent‘. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 148

8

7. 45 Test case to verify ‘IndexComponent‘ creation . . . . . . . . . . . . . . . . 148

7. 46 Test case to verify carousel image display in ‘IndexComponent‘. . . . . . 149

7. 47 Test case to verify ‘nextSlide‘ method call in ‘IndexComponent‘ . . . . . . 149

7. 48 Test case to verify ‘prevSlide‘ method call in ‘IndexComponent‘ . . . . . . 149

7. 49 Test case to verify ‘LocalsComponent‘ creation. . . . . . . . . . . . . . . 150

7. 50 Test case to verify ‘nextSlide‘ method call in ‘LocalsComponent‘. . . . . 150

7. 51 Test case to verify ‘prevSlide‘ method call in ‘LocalsComponent‘. . . . . 150

7. 52 Test case to verify ‘LoginComponent‘ creation . . . . . . . . . . . . . . . . 151

7. 53 Test case to verify ‘AuthService‘ login method call in ‘LoginComponent‘ . 151

7. 54 Test case to verify navigation after login in ‘LoginComponent‘ . . . . . . . 151

7. 55 Test case to verify ‘PaymentGatewayComponent‘ creation . . . . . . . . . 152

7. 56 Test case to verify cart item display in ‘PaymentGatewayComponent‘. . 152

7. 57 Test case to verify cart subtotal calculation in ‘PaymentGatewayCompo-

nent‘ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 153

7. 58 Test case to verify cart item deletion in ‘PaymentGatewayComponent‘ . . 153

7. 59 Test case to verify ‘ProductSectionComponent‘ creation. . . . . . . . . . 154

7. 60 Test case to verify section initialization and user data fetching in ‘Prod-

uctSectionComponent‘ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 154

7. 61 Test case to verify product fetching based on section in ‘ProductSection-

Component‘ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 155

7. 62 Test case to verify sorting of products by price in ‘ProductSectionCom-

ponent‘. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 155

7. 63 Test case to verify adding a product to the wishlist in ‘ProductSection-

Component‘ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 156

7. 64 Test case to verify removing a product from the wishlist in ‘ProductSec-

tionComponent‘ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 156

7. 65 Test case to verify adding a product to the cart in ‘ProductSectionCom-

ponent‘. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 157

7. 66 Test case to verify navigation on search icon click in ‘ProductSectionCom-

ponent‘. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 157

7. 67 Test case to verify navigation on Enter key press in search in ‘Product-

SectionComponent‘ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 158

7. 68 Test case to verify wishlist addition or removal based on login status in

‘ProductSectionComponent‘ . . . . . . . . . . . . . . . . . . . . . . . . . . 158

7. 69 Test case to verify filtering of products by genre and platform in ‘Prod-

uctSectionComponent‘ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 159

7. 70 Test case to verify ‘RegisterComponent‘ creation. . . . . . . . . . . . . . 159

7. 71 Test case to verify registration form submission in ‘RegisterComponent‘. 160

7. 72 Test case to verify error handling when email already exists in ‘Register-

Component‘ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 161

7. 73 Test case to verify general error handling in ‘RegisterComponent‘ . . . . . 162

7. 74 Test case to verify form validation error handling in ‘RegisterComponent‘ 163

7. 75 Test case to verify navigation to login page in ‘RegisterComponent‘ . . . . 163

7. 76 Test case to verify ‘ResetPasswordComponent‘ creation. . . . . . . . . . 164

9

7. 77 Test case to verify route parameter initialization in ‘ResetPasswordCom-

ponent‘. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 164

7. 78 Test case to verify successful password reset in ‘ResetPasswordComponent‘165

7. 79 Test case to verify ‘ShoppingCartModalComponent‘ creation. . . . . . . 165

7. 80 Test case to verify products display in the cart. . . . . . . . . . . . . . . 166

7. 81 Test case to verify cart subtotal calculation. . . . . . . . . . . . . . . . . 166

7. 82 Test case to verify checkout button functionality. . . . . . . . . . . . . . 166

7. 83 Test case to verify underscore replacement in product names. . . . . . . 167

7. 84 Test case to verify product subtotal calculation. . . . . . . . . . . . . . . 167

7. 85 Test case to verify product IVA calculation. . . . . . . . . . . . . . . . . 167

7. 86 Test case to verify product total calculation . . . . . . . . . . . . . . . . . 168

7. 87 Test case to verify cart IVA calculation . . . . . . . . . . . . . . . . . . . . 168

7. 88 Test case to verify cart total calculation. . . . . . . . . . . . . . . . . . . 168

7. 89 Test case to verify product quantity update. . . . . . . . . . . . . . . . . 169

7. 90 Test case to verify product quantity increase . . . . . . . . . . . . . . . . . 169

7. 91 Test case to verify product quantity decrease. . . . . . . . . . . . . . . . 169

7. 92 Test case to verify cart item deletion . . . . . . . . . . . . . . . . . . . . . 170

7. 93 Test case to verify prevention of typing in quantity input. . . . . . . . . 170

7. 94 Test case to verify ‘UserDetailsComponent‘ creation. . . . . . . . . . . . 170

7. 95 Test case to verify navigation links in ‘UserDetailsComponent‘. . . . . . 171

7. 96 Test case to verify ‘UserAccountComponent‘ creation . . . . . . . . . . . . 171

7. 97 Test case to verify user information display in ‘UserAccountComponent‘. 171

7. 98 Test case to verify logout functionality in ‘UserAccountComponent‘ . . . . 172

7. 99 Test case to verify ‘UserPurchaseHistoryComponent‘ creation. . . . . . . 172

7. 100Test case to verify order list display in ‘UserPurchaseHistoryComponent‘ . 173

7. 101Test case to verify ‘WishlistModalComponent‘ creation . . . . . . . . . . . 173

7. 102Test case to verify wishlist product display in ‘WishlistModalComponent‘ 174

7. 103Test case to verify close button functionality in ‘WishlistModalComponent‘174

7. 104Test case to verify ‘User‘ model creation . . . . . . . . . . . . . . . . . . . 175

7. 105Test case to verify password hashing in ‘User‘ model. . . . . . . . . . . . 175

7. 106Test case to verify ‘Client‘ model creation. . . . . . . . . . . . . . . . . . 175

7. 107Test case to verify ‘Client‘ model relationship with ‘User‘. . . . . . . . . 176

7. 108Test case to verify ‘Category‘ model creation. . . . . . . . . . . . . . . . 176

7. 109Test case to verify uniqueness of ‘name‘ in ‘Category‘ model . . . . . . . . 176

7. 110Test case to verify ‘Product‘ model creation . . . . . . . . . . . . . . . . . 177

7. 111Test case to verify ‘Product‘ model relationship with ‘Category‘ . . . . . . 177

7. 112Test case to verify price in ‘Product‘ model. . . . . . . . . . . . . . . . . 177

7. 113Test case to verify ‘Order‘ model creation. . . . . . . . . . . . . . . . . . 178

7. 114Test case to verify ‘Order‘ model relationship with ‘Client‘ . . . . . . . . . 178

7. 115Test case to verify status in ‘Order‘ model . . . . . . . . . . . . . . . . . . 178

7. 116Test case to verify ‘OrderItem‘ model creation . . . . . . . . . . . . . . . . 179

7. 117Test case to verify ‘OrderItem‘ model relationships. . . . . . . . . . . . . 179

7. 118Test case to verify ‘WishlistItem‘ model creation. . . . . . . . . . . . . . 179

7. 119Test case to verify ‘WishlistItem‘ model relationships . . . . . . . . . . . . 180

10

7. 120Test case to verify uniqueness of ‘WishlistItem‘ model. . . . . . . . . . . 180

7. 121Test case to verify ‘UserSerializer‘ serialization. . . . . . . . . . . . . . . 181

7. 122Test case to verify ‘UserSerializer‘ update functionality . . . . . . . . . . . 181

7. 123Test case to verify ‘UserSerializer‘ email validation. . . . . . . . . . . . . 182

7. 124Test case to verify ‘ClientSerializer‘ serialization . . . . . . . . . . . . . . . 182

7. 125Test case to verify ‘ClientSerializer‘ update functionality . . . . . . . . . . 182

7. 126Test case to verify ‘CategorySerializer‘ serialization . . . . . . . . . . . . . 183

7. 127Test case to verify ‘CategorySerializer‘ update functionality. . . . . . . . 183

7. 128Test case to verify ‘CategorySerializer‘ name uniqueness validation. . . . 183

7. 129Test case to verify ‘ProductSerializer‘ serialization. . . . . . . . . . . . . 184

7. 130Test case to verify ‘ProductSerializer‘ update functionality . . . . . . . . . 184

7. 131Test case to verify ‘ProductSerializer‘ price validation. . . . . . . . . . . 184

7. 132Test case to verify ‘OrderItemSerializer‘ serialization. . . . . . . . . . . . 185

7. 133Test case to verify ‘OrderItemSerializer‘ update functionality. . . . . . . 185

7. 134Test case to verify ‘OrderItemSerializer‘ quantity validation. . . . . . . . 185

7. 135Test case to verify ‘OrderSerializer‘ serialization . . . . . . . . . . . . . . . 186

7. 136Test case to verify ‘OrderSerializer‘ creation functionality. . . . . . . . . 186

7. 137Test case to verify ‘OrderSerializer‘ quantity validation . . . . . . . . . . . 187

7. 138Test case to verify ‘WishlistItemSerializer‘ serialization . . . . . . . . . . . 187

7. 139Test case to verify ‘WishlistItemSerializer‘ update functionality. . . . . . 187

7. 140Test case to verify ‘WishlistItemSerializer‘ uniqueness validation. . . . . 188

7. 141Test case to verify retrieval of all products . . . . . . . . . . . . . . . . . . 188

7. 142Test case to verify retrieval of filtered products by price range . . . . . . . 188

7. 143Test case to verify sending of contact email. . . . . . . . . . . . . . . . . 189

7. 144Test case to verify sending of registration email . . . . . . . . . . . . . . . 189

7. 145Test case to verify successful login. . . . . . . . . . . . . . . . . . . . . . 189

7. 146Test case to verify login with invalid credentials . . . . . . . . . . . . . . . 190

7. 147Test case to verify successful user registration . . . . . . . . . . . . . . . . 190

7. 148Test case to verify registration with existing email. . . . . . . . . . . . . 190

7. 149Test case to verify successful user logout . . . . . . . . . . . . . . . . . . . 191

7. 150Test case to verify retrieval of a product by ID. . . . . . . . . . . . . . . 191

7. 151Test case to verify handling of non-existent product ID . . . . . . . . . . . 191

7. 152Test case to verify successful order creation. . . . . . . . . . . . . . . . . 192

7. 153Test case to verify handling of insufficient product quantity in order creation192

7. 154Test case to verify successful addition to wishlist. . . . . . . . . . . . . . 193

7. 155Test case to verify handling of already existing products in wishlist . . . . 193

7. 156Test case to verify successful removal from wishlist. . . . . . . . . . . . . 194

7. 157Test case to verify handling of non-existent products in wishlist . . . . . . 194

7. 158Test case to verify retrieval of user data. . . . . . . . . . . . . . . . . . . 194

7. 159Test case to verify retrieval of purchase history. . . . . . . . . . . . . . . 195

7. 160Details of the RegisterComponent Test Failure.. . . . . . . . . . . . . . . 205

7. 161Details of the ShoppingCartModalComponent Test Failure.. . . . . . . . 206

7. 162Details of the OrderSerializerTest Failure.. . . . . . . . . . . . . . . . . . 208

11

7. 163Details of the Filtered Product View Feature Failure. . . . . . . . . . . . . 209

12

# List of Figures

2. 1 CI Test for mobile module with Actions. . . . . . . . . . . . . . . . . . . . 30

2. 2 CI Build APK and Release for mobile module with Actions. . . . . . . . . 31

2. 3 CI Build APK and Release for mobile module with Actions. . . . . . . . . 32

3. 1 Sprint 1 Burndown Chart. . . . . . . . . . . . . . . . . . . . . . . . . . . 45

3. 2 Sprint 2 Burndown Chart. . . . . . . . . . . . . . . . . . . . . . . . . . . 49

3. 3 Sprint 3 Burndown Chart. . . . . . . . . . . . . . . . . . . . . . . . . . . 53

3. 4 Sprint 4 Burndown Chart. . . . . . . . . . . . . . . . . . . . . . . . . . . 57

4. 1 Configuration of Flake8 tool.. . . . . . . . . . . . . . . . . . . . . . . . . 63

4. 2 Flake8 tool execution result before correct the code.. . . . . . . . . . . . 64

4. 3 Flake8 tool execution result after correct the code.. . . . . . . . . . . . . 64

4. 4 Prettier configuration file.. . . . . . . . . . . . . . . . . . . . . . . . . . . 68

4. 5 Prettier ignore configuration file.. . . . . . . . . . . . . . . . . . . . . . . 69

4. 6 Prettier ignore configuration file.. . . . . . . . . . . . . . . . . . . . . . . 70

5. 1 Results of static testing mobile. . . . . . . . . . . . . . . . . . . . . . . . . 72

5. 2 All rules static testing for mobile app.. . . . . . . . . . . . . . . . . . . . 73

5. 3 Results of static testing mobile. . . . . . . . . . . . . . . . . . . . . . . . . 74

5. 4 Configuration of ESlint tool. . . . . . . . . . . . . . . . . . . . . . . . . . . 76

5. 5 ESlint tool execution result. . . . . . . . . . . . . . . . . . . . . . . . . . . 76

5. 6 ESlint tool execution after to correct the code.. . . . . . . . . . . . . . . 77

5. 7 Apex PMD tool execution.. . . . . . . . . . . . . . . . . . . . . . . . . . 78

6. 1 Risk Prioritization Matrix: High Impact and High Likelihood. . . . . . . 83

6. 2 Click on the ’Ceibos’ Local.. . . . . . . . . . . . . . . . . . . . . . . . . . 106

6. 3 Click on the ’Crear Inventario’ Button. . . . . . . . . . . . . . . . . . . . . 107

6. 4 Click on the ’Seleccionar Filtro’ option.. . . . . . . . . . . . . . . . . . . 108

6. 5 Click on the ’Todos’ option. . . . . . . . . . . . . . . . . . . . . . . . . . . 109

6. 6 Click on the ’Fifa 23’ product.. . . . . . . . . . . . . . . . . . . . . . . . 110

6. 7 Click on the ’Stock Actual’ field.. . . . . . . . . . . . . . . . . . . . . . . 111

6. 8 Put ’2’ in ’Stock Actual’ field. . . . . . . . . . . . . . . . . . . . . . . . . . 112

6. 9 Click on the ’Confirmar’ button.. . . . . . . . . . . . . . . . . . . . . . . 113

6. 10 Click on the ’Detalles’ tab.. . . . . . . . . . . . . . . . . . . . . . . . . . 114

6. 11 Write employee name ’Juan P´erez’. . . . . . . . . . . . . . . . . . . . . . . 115

6. 12 Click on the ’Guardar Borrador’ button. . . . . . . . . . . . . . . . . . . . 116

6. 13 Results of static testing mobile. . . . . . . . . . . . . . . . . . . . . . . . . 121

6. 14 Results of testing TabBar Screen. . . . . . . . . . . . . . . . . . . . . . . . 121

13

6. 15 Results of testing DateSelector Widget.. . . . . . . . . . . . . . . . . . . 122

6. 16 Results of testing Inventory Detail Screen. . . . . . . . . . . . . . . . . . . 122

6. 17 Results of testing SaleSpot Screen.. . . . . . . . . . . . . . . . . . . . . . 122

6. 18 Results of testing Draft Screen. . . . . . . . . . . . . . . . . . . . . . . . . 123

6. 19 Results of testing History Screen. . . . . . . . . . . . . . . . . . . . . . . . 123

6. 20 Results of testing Product Details Screen.. . . . . . . . . . . . . . . . . . 123

6. 21 Results of testing Product List Screen. . . . . . . . . . . . . . . . . . . . . 124

6. 22 Results of testing Product Class.. . . . . . . . . . . . . . . . . . . . . . . 124

6. 23 Results of testing qr widget. . . . . . . . . . . . . . . . . . . . . . . . . . . 124

6. 24 Results of testing Report Screen.. . . . . . . . . . . . . . . . . . . . . . . 125

7. 1 Risk Prioritization Matrix: High Impact and High Likelihood. . . . . . . 131

7. 2 Results of frontend testing . . . . . . . . . . . . . . . . . . . . . . . . . . . 200

7. 3 Results of frontend acceptance testing - Cart. . . . . . . . . . . . . . . . 201

7. 4 Results of frontend acceptance testing - Login . . . . . . . . . . . . . . . . 201

7. 5 Results of frontend acceptance testing - Product. . . . . . . . . . . . . . 202

7. 6 Results of frontend acceptance testing - Wishlist. . . . . . . . . . . . . . 202

7. 7 Results of backend testing - Cart. . . . . . . . . . . . . . . . . . . . . . . 204

7. 8 Results of backend acceptance testing - Cart. . . . . . . . . . . . . . . . 204

7. 9 RegisterComponent Test Failure. . . . . . . . . . . . . . . . . . . . . . . 206

7. 10 ShoppingCartModal Test Failure. . . . . . . . . . . . . . . . . . . . . . . 207

7. 11 OrderSerializerTes Test Failure. . . . . . . . . . . . . . . . . . . . . . . . 208

7. 12 Filtered Product View Feature Failure Failure . . . . . . . . . . . . . . . . 209

9. 1 Sprint 1 Acceptance Letter. . . . . . . . . . . . . . . . . . . . . . . . . . 212

9. 2 Sprint 1 Acceptance Letter. . . . . . . . . . . . . . . . . . . . . . . . . . 213

9. 3 Sprint 3 Acceptance Letter. . . . . . . . . . . . . . . . . . . . . . . . . . 214

9. 4 Sprint 4 Acceptance Letter. . . . . . . . . . . . . . . . . . . . . . . . . . 215

9. 5 Python –Version. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 216

9. 6 Angular and Node.js Version.. . . . . . . . . . . . . . . . . . . . . . . . . 217

9. 7 Git clone example.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 218

9. 8 Backend Path example.. . . . . . . . . . . . . . . . . . . . . . . . . . . . 218

9. 9 Pip List example. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 219

9. 10 Xampp configuration.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 220

9. 11 Go to PhpMyAdmin. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 221

9. 12 New Database.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 222

9. 13 Creation database example.. . . . . . . . . . . . . . . . . . . . . . . . . . 222

9. 14 Credential database example.. . . . . . . . . . . . . . . . . . . . . . . . . 223

9. 15 PhpMyAdmin page.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 224

9. 16 Select SQL option. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 225

9. 17 Category insert . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 225

9. 18 Product insert. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 226

9. 19 Frontend path example.. . . . . . . . . . . . . . . . . . . . . . . . . . . . 226

9. 20 Backend deploy . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 226

14

9. 21 Frontend deploy. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 227

9. 22 APK release in Github.. . . . . . . . . . . . . . . . . . . . . . . . . . . . 228

9. 23 Activate unknown sources. . . . . . . . . . . . . . . . . . . . . . . . . . . . 229

9. 24 App installed. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 230

9. 25 App icon.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 230

9. 26 Django administration panel . . . . . . . . . . . . . . . . . . . . . . . . . . 231

9. 27 Django administration panel - Loged . . . . . . . . . . . . . . . . . . . . . 232

9. 28 Go to Auth Section - Django. . . . . . . . . . . . . . . . . . . . . . . . . 233

9. 29 Auth Section Page - Django . . . . . . . . . . . . . . . . . . . . . . . . . . 233

9. 30 Go to Add Token - Django. . . . . . . . . . . . . . . . . . . . . . . . . . 234

9. 31 Add Token Page - Django. . . . . . . . . . . . . . . . . . . . . . . . . . . 234

9. 32 Go to Change Token - Django. . . . . . . . . . . . . . . . . . . . . . . . 234

9. 33 Change Token Page - Django. . . . . . . . . . . . . . . . . . . . . . . . . 235

9. 34 Go to Authentication and Authorization Section - Django. . . . . . . . . 235

9. 35 Authentication and Authorization Section - Django . . . . . . . . . . . . . 235

9. 36 Go to Add Group - Django. . . . . . . . . . . . . . . . . . . . . . . . . . 236

9. 37 Add Group Page - Django . . . . . . . . . . . . . . . . . . . . . . . . . . . 236

9. 38 Go to Change Group - Django. . . . . . . . . . . . . . . . . . . . . . . . 236

9. 39 Change Group Page - Django. . . . . . . . . . . . . . . . . . . . . . . . . 237

9. 40 Go to Custom User Management Section - Django. . . . . . . . . . . . . 237

9. 41 Custom User Management Section - Django . . . . . . . . . . . . . . . . . 237

9. 42 Go to Add user - Django . . . . . . . . . . . . . . . . . . . . . . . . . . . . 238

9. 43 Add User Page - Django . . . . . . . . . . . . . . . . . . . . . . . . . . . . 238

9. 44 Go to Change User - Django. . . . . . . . . . . . . . . . . . . . . . . . . 239

9. 45 Change Group User - Django. . . . . . . . . . . . . . . . . . . . . . . . . 239

9. 46 Recent Actions Section - Django. . . . . . . . . . . . . . . . . . . . . . . 239

9. 47 Home Page Web. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 240

9. 48 Navbar Icons. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 241

9. 49 Index page. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 242

9. 50 Dropdown of Products . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 244

9. 51 Local page . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 245

9. 52 Contact page. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 246

9. 53 Contact form. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 247

9. 54 Search function . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 247

9. 55 Best-Sellers block . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 248

9. 56 Best-Sellers page. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 249

9. 57 News-Products block . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 250

9. 58 News-Products page. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 251

9. 59 User icon. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 252

9. 60 Login from - Change to register form . . . . . . . . . . . . . . . . . . . . . 252

9. 61 Register form. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 253

9. 62 Email notification . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 253

9. 63 Register Email. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 254

9. 64 User icon. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 255

15

9. 65 Login form. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 255

9. 66 User icon. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 256

9. 67 User personal information page. . . . . . . . . . . . . . . . . . . . . . . . 256

9. 68 User icon. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 257

9. 69 Login page. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 257

9. 70 Email confirmation page . . . . . . . . . . . . . . . . . . . . . . . . . . . . 258

9. 71 Reset password email notification . . . . . . . . . . . . . . . . . . . . . . . 258

9. 72 Reset password email . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 259

9. 73 Reset password page. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 259

9. 74 Products dropdown . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 260

9. 75 Products page . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 260

9. 76 Wish-List icon. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 261

9. 77 Wish-List modal page. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 262

9. 78 Products dropdown . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 263

9. 79 Products page . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 263

9. 80 Shop-cart icon. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 264

9. 81 Shop-cart modal page. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 264

9. 82 Shop-cart modal page - Add quantity. . . . . . . . . . . . . . . . . . . . 265

9. 83 Shop-cart modal page - Reduce quantity . . . . . . . . . . . . . . . . . . . 266

9. 84 Shop-cart modal page - Eliminate product . . . . . . . . . . . . . . . . . . 266

9. 85 Alert - Elimination confirmation. . . . . . . . . . . . . . . . . . . . . . . 267

9. 86 Shop-cart modal page - Show all option. . . . . . . . . . . . . . . . . . . 267

9. 87 Shop-cart modal page - Finish buy option. . . . . . . . . . . . . . . . . . 268

9. 88 Payment page . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 269

9. 89 Shop-cart modal page - Eliminate product . . . . . . . . . . . . . . . . . . 270

9. 90 Alert - Elimination confirmation. . . . . . . . . . . . . . . . . . . . . . . 270

9. 91 Shop-cart modal page - Eliminate product . . . . . . . . . . . . . . . . . . 271

9. 92 Reserve buy email notification . . . . . . . . . . . . . . . . . . . . . . . . . 271

9. 93 Reserve buy email. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 272

9. 94 User icon. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 273

9. 95 User personal information page. . . . . . . . . . . . . . . . . . . . . . . . 273

9. 96 User buy history page. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 274

9. 97 User buy history page. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 274

9. 98 User buy history page - Order information . . . . . . . . . . . . . . . . . . 275

9. 99 Product section . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 276

9. 100Product section - Choose product . . . . . . . . . . . . . . . . . . . . . . . 277

9. 101Product detail. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 278

9. 102Product section - ordered by cheaper price . . . . . . . . . . . . . . . . . . 279

9. 103Product section - ordered by expensive price . . . . . . . . . . . . . . . . . 280

9. 104Product section - ordered by alphabetical A-Z . . . . . . . . . . . . . . . . 281

9. 105Product section - ordered by alphabetical Z-A . . . . . . . . . . . . . . . . 281

9. 106Product section - filtered by price . . . . . . . . . . . . . . . . . . . . . . . 282

9. 107Product section - filtered by video games . . . . . . . . . . . . . . . . . . . 283

9. 108Product section - filtered by funko pops. . . . . . . . . . . . . . . . . . . 284

16

9. 109Product section - filtered by console. . . . . . . . . . . . . . . . . . . . . 285

9. 110Product section - filtered by articles. . . . . . . . . . . . . . . . . . . . . 286

9. 111Product section - filtered by others . . . . . . . . . . . . . . . . . . . . . . 287

9. 112Video-games products section . . . . . . . . . . . . . . . . . . . . . . . . . 288

9. 113Funko-pop products section. . . . . . . . . . . . . . . . . . . . . . . . . . 289

9. 114Console products section . . . . . . . . . . . . . . . . . . . . . . . . . . . . 290

9. 115Article products section. . . . . . . . . . . . . . . . . . . . . . . . . . . . 291

9. 116Footer ubication. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 292

9. 117Terms and Conditions ubication. . . . . . . . . . . . . . . . . . . . . . . 293

9. 118Terms and Conditions page. . . . . . . . . . . . . . . . . . . . . . . . . . 294

9. 119About Us ubication. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 295

9. 120About Us page. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 296

9. 121Payment Methods ubication . . . . . . . . . . . . . . . . . . . . . . . . . . 297

9. 122Payment Methods page. . . . . . . . . . . . . . . . . . . . . . . . . . . . 298

9. 123Footer section - Facebook icon. . . . . . . . . . . . . . . . . . . . . . . . 299

9. 124Footer section - Instagram icon. . . . . . . . . . . . . . . . . . . . . . . . 300

9. 125Mobile App. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 301

9. 126Mobile App Login. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 302

9. 127Mobile App spots of sale . . . . . . . . . . . . . . . . . . . . . . . . . . . . 303

9. 128Mobile App home. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 304

9. 129Mobile App spots of sale . . . . . . . . . . . . . . . . . . . . . . . . . . . . 305

9. 130Mobile App Settings. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 306

9. 131Mobile App Create an Inventory. . . . . . . . . . . . . . . . . . . . . . . 307

9. 132Mobile App. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 308

9. 133Mobile App Draft of the Inventory. . . . . . . . . . . . . . . . . . . . . . 309

9. 134Mobile App Draft of the Inventory. . . . . . . . . . . . . . . . . . . . . . 310

9. 135Mobile App Inventory Details . . . . . . . . . . . . . . . . . . . . . . . . . 311

9. 136Mobile Draft Draft Inventory of a Spot of Sale. . . . . . . . . . . . . . . 312

9. 137Mobile App Draft Inventory of a Spot of Sale. . . . . . . . . . . . . . . . 313

9. 138Mobile App Elements of the Draft Inventory. . . . . . . . . . . . . . . . 314

9. 139Mobile App Create an Excel . . . . . . . . . . . . . . . . . . . . . . . . . . 315

9. 140Mobile App Create an Excel . . . . . . . . . . . . . . . . . . . . . . . . . . 316

9. 141Mobile App PDF Report. . . . . . . . . . . . . . . . . . . . . . . . . . . 317

9. 142Mobile App Last Report Generated . . . . . . . . . . . . . . . . . . . . . . 318

9. 143Mobile App Last Report Generated . . . . . . . . . . . . . . . . . . . . . . 319

9. 144Mobile App Last Inventory. . . . . . . . . . . . . . . . . . . . . . . . . . 320

9. 145Mobile App Last Inventory. . . . . . . . . . . . . . . . . . . . . . . . . . 321

9. 146Mobile App Product list. . . . . . . . . . . . . . . . . . . . . . . . . . . 322

9. 147Mobile App Product management. . . . . . . . . . . . . . . . . . . . . . 323

9. 148Asana activity schedule. . . . . . . . . . . . . . . . . . . . . . . . . . . . 324

17

# Revision History

Name Date Reason For Changes Version 1 25/06/2024 Nothing V1.0

18

# 1 Introduction

### 1.1 Project context

This project revolves around two primary components: a mobile application for inventory management and a web portal for customer interaction. The mobile application will enable the staff at ”Pricotercorp S.A.” to efficiently manage the inventory across all store locations. This includes functionalities for adding new products, updating existing product information, and conducting regular inventory reviews. By streamlining these tasks, the mobile application aims to reduce the time and effort required for effective inventory management.

The web portal, on the other hand, is designed to enhance the customer experience by providing an online platform where customers can browse and view available products. This portal will categorize products by city, allowing customers to see what is available at each store location. Additionally, detailed product information will be displayed, excluding the product codes to maintain privacy and security. Customers will have the capability to reserve products they are interested in, thereby facilitating a smoother purchase process.

Both components are crucial to addressing the existing challenges faced by ”Pricotercorp S.A.” in terms of inventory management and customer engagement. The integration of these systems is expected to improve operational efficiency and expand the company’s reach by attracting more customers through an enhanced online presence.

19

# 2 Relevant Architectural Decisions

In this section, we will document the key architectural decisions made during the project’s development, along with the reasons behind these decisions. This encompasses decisions ranging from the selection of collaborative tools to the choice of programming environments and frameworks for each section that the software covers.

### 2.1 Teamwork Management Tool

It was necessary to select an effective platform for task management, collaboration and project monitoring that would improve team organization in order to optimize communication and facilitate the assignment of responsibilities and thus avoid future problems around the assignment of tasks. To address this, we are considering the following teamwork management tools and their respective features:

Characteristic Asana Trello Jira

Ease of Use High High Medium Functionality Comprehensive Basic Comprehensive Integrations Extensive Limited Extensive Scalability High Medium High Support Good Good Excellent Price Various plans, incl. free Various plans, incl. free Paid, various plans

Table 2.1: Comparison of Teamwork Management Tool

Decision:

Asana

Justification:

It was decided to select Asana for its intuitive and friendly interface that makes it easy to create and assign tasks, manage projects through visual dashboards, and generate reports. Offering a wide range of functionality such as calendars, milestone tracking, integration with third-party tools, and its ability to scale with team needs make Asana an ideal choice for improving operational efficiency and collaboration within the project. To access the planning carried out in Asana for this software project, go to the section 9.8.

20

### 2.2 Database

There is a need to implement a robust relational database with wide adoption in the industry. To address this, we are considering the following databases and their respective features:

Characteristic MySQL PostgreSQL SQLite MongoDB

Database Type Relational Relational Relational NoSQL Transaction Support Yes Yes Yes No

Compatibility High High High Medium Scalability High High Low High (for NoSQL) Performance High High Medium High Documentation Extensive and detailed Extensive and detailed Good Good

Community Large Large Large Large Ease of Use Moderate Moderate High High

Table 2.2: Comparison of Database

Decision:

MySQL

Justification:

MySQL was selected for its robustness, widespread industry adoption, transaction support, and high compatibility with various technologies. In addition, the members of our development team are accustomed to this database management system, so we would reduce training and learning time for development in MySQL.

21

### 2.3 Web Frontend Framework

There is a need to choose a robust and scalable framework for developing Single Page Applications (SPAs). To address this, we are considering the following frameworks and their respective features:

Characteristic Angular React Vue.js

Language TypeScript JavaScript JavaScript Architecture MVC View library MVVM Corporate Support High (Google) High (Facebook) Medium Learning Curve Moderate Moderate Low Documentation Extensive and detailed Good Good Community Large Large Growing Performance High High High

Table 2.3: Options Considered for the Web Frontend Framework

Decision:

Angular

Justification:

Angular was chosen due to its robust ecosystem, corporate support from Google, and its ability to handle complex and scalable applications. Furthermore, our development team already has experience in building web applications with this framework, which will save us time in TypeScript training and navigating the Angular ecosystem.

22

### 2.4 Web Backend Framework

Need to select an efficient and secure backend framework for the rapid development of web applications, with the capacity to handle large volumes of data and offer a high level of security.To address this, we are considering the following frameworks and their respective features:

Characteristic Django Express.js Laravel Ruby on Rails

Language Python JavaScript PHP Ruby

MySQL 8.0 Connectivity Yes, additional libs Yes, npm MySQL lib Yes, .env config Yes, mysql12 gem

Scope Large-scale apps Lightweight apps & APIs Medium-sized web apps Startup, small web apps History Management Sessions or logging Routes, middleware, logging Logging system Logging system

Strengths Scalable, Built-in ORM, Admin interface

Lightweight, Flexible, Fast dev Elegant syntax, PHP ease Rapid dev, Convention over config Weaknesses Python may be slower Fewer built-in features Potential performance hit Response time may lag

Table 2.4: Options Considered for the Web Backend Framework

Decision:

Django

Justification:

Django was chosen for its low learning cost, robust MTV architecture, and its ability to handle secure and scalable web applications. The extensive documentation and the large community of developers are not an important factor since our development team lacks knowledge about the use of this bakeend framework. Additionally, its rich ecosystem of libraries and integration with popular technologies facilitate efficient development and deployment of complex web applications.

23

### 2.5 Mobile Development Framework

There is a need for a framework to develop efficient native mobile applications for iOS and Android with a code base that shares similarities between these mobile systems. To address this, we are considering the following frameworks and their respective features:

Characteristic Kotlin Flutter React Native Ionic

Learning Curve Low Moderate Moderate Moderate

MySQL 8.0 Connectivity Requires JDBC, Ktor REST APIs Axios for REST REST APIs

Scope Mobile, backend Mobile Mobile Mobile, web History Management Moderate Moderate High High

Strengths Java interoperability, modern syntax, security

Productivity, native UI, strong Google support

Community, multi-platform support

Web-friendly, acceptable performance Weaknesses Smaller community, compilation time

Development stage, resource usage

Performance issues, native plugins

Reliance on plugins, lower performance

Table 2.5: Comparison of Mobile Frameworks

Decision:

Flutter

Justification:

We decided to select Flutter for its high performance, corporate support from Google, and its ability to develop native applications for multiple platforms with a single code base, which would simplify the work done by the development team. Also, having a moderate learning curve, it will not take many resources to train those in charge of the mobile application on the operation of the essential and necessary features of Fluuter to carry out this software project.

24

### 2.6 Coding Standards / PMD Tool for Django

There is a need to implement consistent coding standards and improve code quality in our Django backend section of the web module to facilitate maintenance, reduce errors and improve code readability. To address this, we are considering the following frameworks and their respective features:

Characteristic Flake8 Pylint Black

Language Supported Python Python Python Coding Style PEP 8 PEP 8, PEP 257 Code formatter Ease of Use High Medium High Configurability High High Low Documentation Extensive and detailed Extensive and detailed Good

Integration with CI/CD Easy Easy Easy

Community Large Large Large Performance High Medium High

Table 2.6: Comparison of Coding Standards Tool for Django

Decision:

Flake8

Justification:

Flake8 was chosen for its ability to verify compliance with PEP 8 coding conventions, detect errors, and improve Python code quality effectively. Its easy configuration and ability to easily integrate with development environments ensure a smooth implementation. For a more detailed explanation of the choice of this Coding Standards tool for Django, go to the Figure 5.1.2.

25

### 2.7 Coding Standards Tool for Angular

There is a need to implement consistent coding standards to improve the quality of the code in our project in the web section with Angular and maintain consistency and facilitate collaboration between the development team members assigned to this module. To address this, we are considering the following coding standards tool for Angular and their respective features:

Characteristic ESLint TSLint Prettier

Language Supported JavaScript, Type- Script TypeScript JavaScript, Type- Script Coding Style Configurable Configurable Configurable Ease of Use High High High Configurability High High high Documentation Extensive and detailed Extensive and detailed Extensive and detailed Integration with CI/CD Easy Easy Easy

Community Large Medium Large Performance High High High

Table 2.7: Comparison of Coding Standards Tools for Angular

Decision:

Prettier

Justification:

Prettier was selected due to its ability to enforce a consistent coding style across the entire codebase automatically. Its opinionated nature removes the burden of configuration and debate over style preferences, allowing developers to focus more on coding rather than formatting. The tool’s extensive documentation, ease of use, and seamless integration with CI/CD pipelines make Prettier a powerful choice for improving code quality and ensuring a consistent development environment in Angular projects. For a more detailed explanation of the choice of this Coding Standards tool for Angular, go to the subsection 4.2.4.

26

### 2.8 PMD Tool for Angular

There is a need to implement consistent coding standards and static code analysis to enhance the quality of the code in our project and maintain a high level of consistency across different modules. This also facilitates collaboration between the development team members. To address this, we are considering the PMD tool for static code analysis and its respective features:

Characteristic ESLint TSLint Apex PMD

Language Supported JavaScript, Type- Script TypeScript JavaScript, Type- Script Coding Style Configurable Configurable Configurable Ease of Use High High Medium Configurability High High Medium Documentation Extensive and detailed Extensive and detailed Good

Integration with CI/CD Easy Easy Easy

Community Large Medium Medium Performance High High High

Table 2.8: Comparison of PMD Tool for Angular

Decision:

ESLint

Justification:

ESLint was selected due to its ability to verify and enforce custom coding rules, as well as style conventions and best practices in TypeScript. Its extensive configurability, support for plugins and the possibility of integrating with other libraries make ESLint a powerful tool to improve code quality, reduce errors, ensuring consistent and efficient development in Angular projects. For a more detailed explanation of the choice of this Coding Standards tool for Angular, go to the paragraph 5.2.1.

27

### 2.9 Coding Standards / PMD Tool for Flutter

Characteristic Dart Analyzer Flutter Analyzer Linter

Language Supported Dart Dart, Flutter Dart Coding Style PEP 8 PEP 8, Flutter Best Practices PEP 8

Ease of Use High Medium Medium Configurability High Medium High Documentation Extensive and detailed Extensive and detailed Extensive and detailed Integration with CI/CD Easy Easy Easy

Community Large Large Large Performance High Medium High

Table 2.9: Comparison of Coding Standards Tool for Flutter

Decision:

Dart Analyzer

Justification:

Dart Analyzer provides a high degree of configurability, enabling fine-tuning of analysis rules to meet the specific needs of a project. Also, is easy to use and configure, allowing for quick integration into both new and existing projects. Its simplicity makes it accessible to both novice and experienced developers. For a more detailed explanation of the choice of this Coding Standards tool for Angular, go to the subsection 5.1.2.

28

### 2.10 Authentication and Access Control Framework

For our web application, we are looking for an efficient and secure authentication framework that is capable of handling token-based authentication, guaranteeing secure access and providing an easy integration process with our selected backend, Django. To address this, we are considering the following options:

Characteristic Django Simple JWT DRF JWT Django OAuth Toolkit

Functionality JWT auth JWT auth OAuth2 auth Language Python Python Python Integration Django auth DRF Django, OAuth2 Token Types Access, Refresh Access, Refresh OAuth2 tokens Token Management Create, Verify, Refresh Create, Verify, Refresh Create, Verify, Refresh Security High, Customizable High OAuth2 standard

Docs and Community Extensive, Large Good, Active Extensive, Active

Strengths Simple, Secure, Scalable Easy, DRF support Comprehensive, Flexible Weaknesses Needs JWT knowledge Limited to DRF Complex setup

Table 2.10: Comparison of Authentication and Access Control Options for Django

Decision:

Django Simple JWT

Justification:

Django Simple JWT was chosen for its strong integration with the Django authentication system, its ability to handle secure token-based authentication, and support for access and refresh tokens. Its simplicity of setup, ability to customize token management features, comprehensive documentation provided, and community support make it easy to quickly develop and implement secure authentication mechanisms in our Django application.

29

### 2.11 Continuous Integration Tool

2. 11.1 Mobile Module - Github Actions

GitHub Actions was used as the primary tool for Continuous Integration (CI) in the project. This platform enabled the automation of the development process, ensuring that every change made to the source code passed through a set of predefined tests before being integrated into the main branch. Each time a commit was made to the repository, GitHub Actions automatically triggered a workflow that included the execution of unit and integration tests, helping to identify and fix issues early in the development cycle.

Figure 2.1: CI Test for mobile module with Actions.

In addition to the automatic execution of tests, GitHub Actions was configured to trigger the automatic generation of the APK file using a specific commit message. When the commit message contained a predefined keyword, such as ”[/build_apk]”, GitHub Actions detected it and executed the necessary commands to compile the project and generate the APK. This APK was then stored as a downloadable artifact directly from the GitHub interface.

30

Figure 2.2: CI Build APK and Release for mobile module with Actions.

This approach not only facilitated agile and collaborative development but also ensured high code quality and consistency in deliveries. By automating both testing and APK generation, the risk of human error was reduced, and the development process was accelerated, resulting in greater efficiency and productivity for the team.

31

2. 11.2 Mobile Module - Github Actions

In the development of the web module project using Angular for the frontend and Django for the backend, a Continuous Integration (CI) process was implemented using GitHub Actions. Below are the three main sections configured in the workflow:

- Running Angular Tests: Automatically runs unit and integration tests for the

Angular frontend with every push to the repository.

- Running Django Tests: Executes automated tests on the Django backend to

verify the integrity of models and server logic.

- Deployment to Firebase Hosting: After passing the tests, the frontend is

automatically deployed to Firebase Hosting.

These tasks are automatically performed whenever the code is updated in the repository, ensuring that the project remains stable and up-to-date at all times.

Figure 2.3: CI Build APK and Release for mobile module with Actions.

32

### 2.12 Testing Tools

2. 12.1 Mobile Module

Unit Testing tool

For unit testing in the mobile module developed with Flutter, we considered the following options:

Characteristic Flutter Test Mockito Bloc Test

Framework Integration Native Requires setup Requires setup Testing Paradigm Widget, Unit Mocking, Unit Blocspecific Ease of Use Simple Moderate Moderate Community Support Extensive Extensive Growing Documentation ComprehensiveGood Moderate Strengths Seamless, Fast Powerful Mocking Blocfocused Weaknesses Limited to Flutter Requires extra dependencies

Limited to Bloc pattern

Table 2.11: Comparison of Unit Testing Tools for Mobile Module

Decision:

Flutter Test

Justification:

Flutter Test was selected due to its seamless integration with the Flutter framework, which allows for efficient testing of both widget and unit tests. Its native support ensures faster test execution and simplifies the testing process, making it ideal for our needs. The extensive documentation and large community support further solidify it as the best choice for unit testing in our mobile module.

33

Acceptance Testing tool

For acceptance testing in the mobile module, the following options were evaluated:

Characteristic Flutter Integration Test Appium Espresso

Framework Integration Native Crossplatform Androidonly Ease of Setup Simple Complex Moderate Supported Platforms Flutter apps Multiple Android

Community Support Growing Extensive Extensive Documentation Good ComprehensiveGood Strengths Fast, Native Crossplatform Performance

Weaknesses Limited to Flutter Requires setup Androidonly

Table 2.12: Comparison of Acceptance Testing Tools for Mobile Module

Decision:

Flutter Integration Test

Justification:

Flutter Integration Test was chosen for its native support within the Flutter framework, offering a streamlined and efficient way to perform acceptance testing. Its simplicity in setup and execution, coupled with its ability to quickly integrate into our existing Flutter project, make it the optimal choice for acceptance testing in our mobile module.

34

2. 12.2 Web Module

Unit Testing tool Angular

For unit testing in the Angular web module, the following tools were considered:

Characteristic Karma - Jasmine Mocha - Chai Jest

Framework Integration Native Requires setup Requires setup

Testing Paradigm BDD, Unit BDD, Unit BDD, Unit Ease of Use Simple Moderate Simple Community Support Extensive Good Extensive Documentation Comprehensive Good Good Strengths Angularfocused Flexible Fast execution

Weaknesses Slower execution Complex setup Limited features

Table 2.13: Comparison of Unit Testing Tools for Angular

Decision:

Karma - Jasmine

Justification:

Karma - Jasmine was selected due to its deep integration with the Angular framework, making it the most suitable choice for unit testing. The simplicity in usage, coupled with extensive community support and comprehensive documentation, ensures that our unit testing needs are met efficiently.

35

Acceptance Testing tool Angular

For acceptance testing in the Angular module, we evaluated the following:

Characteristic Cypress - Cucumber Preprocessor

Protractor Nightwatch

Framework Integration Good Native Requires setup

BDD Support Strong Moderate Moderate Ease of Setup Simple Moderate Complex Community Support Growing Extensive Good Documentation Comprehensive Good Moderate Strengths BDD, Fast Angularnative Cross-browser

Weaknesses Learning curve Deprecation Requires extra setup

Table 2.14: Comparison of Acceptance Testing Tools for Angular

Decision:

Cypress - Cucumber Preprocessor

Justification:

Cypress with the Cucumber Preprocessor was chosen for its powerful BDD support, which aligns well with our acceptance testing requirements. The simplicity of setup and fast execution times, combined with a growing community and strong documentation, make it the ideal tool for our Angular web module.

36

Unit Testing tool Django

For unit testing in Django, we considered the following:

Characteristic django- TestCase Pytest- Django Nose2

Framework Integration Native Requires setup Requires setup

Testing Paradigm Unit, ORM Unit, ORM Unit, ORM Ease of Use Simple Simple Simple Community Support Extensive Extensive Good Documentation Comprehensive Good Moderate Strengths Django-specific Flexible Fast execution Weaknesses Limited features Requires plugins Limited support

Table 2.15: Comparison of Unit Testing Tools for Django

Decision:

django-TestCase

Justification:

django-TestCase was selected for its seamless integration with Django’s ORM, providing an out-of-the-box solution for unit testing. Its simplicity, combined with extensive community support and detailed documentation, makes it the most efficient choice for our Django module.

37

Acceptance Testing tool Django

For acceptance testing in Django, the following tools were evaluated:

Characteristic behave-django Selenium Robot Framework BDD Support Strong Limited Moderate Ease of Setup Simple Complex Moderate Framework Integration Good Requires setup Requires setup

Community Support Growing Extensive Good Documentation Good Good Good Strengths BDD, Django Cross-browser Versatile Weaknesses Limited to Django Complex setup Learning curve

Table 2.16: Comparison of Acceptance Testing Tools for Django

Decision:

behave-django

Justification:

behave-django was chosen due to its strong BDD support and smooth integration with Django. This tool allows for efficient acceptance testing that aligns with our project’s needs, supported by good documentation and an active community, making it the best choice for our Django web module.

38

# 3 SCRUM Evidence

### 3.1 Roles Definition

3. 1.1 Product Owner

JOFFRE MORALES MENDOZA was selected as the Product Owner due to his deep understanding of both customer requirements and the company, PRICOTERCORP S.A. He will be responsible for creating and managing the product backlog, maximizing its value, and guiding the team’s work. Additionally, he will make decisions on the functionalities to be implemented in each iteration.

3. 1.2 Scrum Master

CORNEJO FIGUEROA ANDRES ALFREDO was appointed as the Scrum Master because of his extensive knowledge and experience in the Scrum agile methodology. His main role will be to ensure that the Scrum team follows established principles and practices, assist the team in adopting and understanding Scrum, and remove obstacles. He will facilitate Scrum meetings and shield the team from external distractions.

3. 1.3 Development Team

Due to the team’s small size, all members will be responsible for project development: TOMALA MORENO ANGEL ALEXANDER, MAWYIN CABAY JORGE DANIEL, ROLDAN PILOZO KEVIN ARIEL, and CORNEJO FIGUEROA ANDRES ALFREDO. Their task will be to deliver product increments at the end of each sprint, turning backlog items into potentially shippable product increments.

39

### 3.2 Product Backlog

Functioning as a strategic roadmap, the Product Backlog not only aligns our team with stakeholder expectations but also facilitates adaptability to shifting market dynamics. In this concise exposition, we explore the integral role the Product Backlog plays in guiding our development.

ID Product Backlog Item Priority Initial Estimate of Effort (Hours) MM-01 Mobile M. As an inventory section employee, I want to improve stock management at Pricotercorp S.A. by being able to view the updated stock of products in each establishment, including information on items stored in the warehouse, to request what is needed in case of stockouts in a specific store.

1 24

MM-02 Mobile M. As an inventory area employee, I want the application to offer me the option to register a product using a code or QR that directly identifies the product to facilitate the registration of new products.

1 26

WM-01 Web M. As a user, I want each product to have a detailed description, including features, technical specifications, and relevant details to make an informed decision.

1 28

WM-02 Web M. As an administrator, I want the products shown to users to be directly related to those we have in the inventory to avoid inconsistencies when selling products.

1 22

MM-03 Mobile M. As a system administrator, I want any change in the quantity of products in the inventory to be automatically and instantly reflected on the web interface to provide a complete user experience.

2 9

MM-04 Mobile M. As a system administrator, I want to be able to manage who can access the action log history in the inventory to keep the registration system secure.

2 23

WM-03 Web M. As an administrator, I want to provide clear and easy-to-understand resources to help beginner users navigate the platform.

2 6

MM-05 Mobile M. As an administrator, I want the system to show me images and key features of each of the products available in the inventory to facilitate the review and efficient management of relevant product information.

3 16

40

MM-06 Mobile M. As a system administrator, I want the ability to export the history of actions taken in the inventory in a format that allows for review and external analysis for decision-making purposes.

3 15

WM-04 Web M. As a user, I want to experience a smooth purchasing process from product selection to transaction completion to avoid any complications during the payment process for one or more products.

3 25

WM-05 Web M. As a user, I want to manage my account efficiently and access personalized functions to improve my shopping experience.

3 48

MM-07 Mobile M. As an inventory area employee, I want autocomplete functionalities to expedite the process of registering new products.

4 20

MM-08 Mobile M. As a system administrator, I want a tool that allows me to easily search and filter the history of actions taken on inventory products to better identify changes made in the records.

4 26

MM-09 Mobile M. As a decision-making team member, I want the system to display the inventory flow, highlighting products with higher and lower movement frequency to facilitate decision-making by providing key information about product management.

4 22

WM-06 Web M. As a user, I want to filter among different products on the screen by categories and subcategories to have fewer elements on the screen.

4 12

WM-07 Web M. As a user, I want to search among all products by name, type, or brand to easily find a product. 4 20

Table 3.1: Product Backlog

41

### 3.3 Sprint 1

This sprint will focus on establishing the foundations of the inventory management system and enhancing the user experience on Pricotercorp S.A.’s mobile platform. Additionally, we will develop the initial views of the website, incorporating various key interfaces and functionalities for product display and search.

3. 3.1 Sprint Backlog

Sprint 1 Start Date: 05/20/2024 Final Date: 06/09/2024 Total Effort:68

ID Product Backlog Item Priority Sprint Task Volunteer Estimated Effort (Hours) MM- 01 Mobile M. As an inventory section employee, I want to improve stock management at Pricotercorp S.A. by being able to view the updated stock of products in each establishment, including information on items stored in the warehouse, to request what is needed in case of stockouts in a specific store.

1 Interface displaying different establishments Andr´es Cornejo 9

Implementation of Display Functionality Angel Tomal´a 7

WM- 01 Web M. As a user, I want each product to have a detailed description, including features, technical specifications, and relevant details to make an informed decision.

1 Design of the User Interface, main section, and the product section.

Kevin Roldan 15

MM- 05 Mobile M. As an administrator, I want the system to show me images and key features of each of the products available in the inventory

3 Interface displaying products with features and image integration

Andr´es Cornejo 7

WM- 07 Web M. As a user, I want to search among all products by name, type, or brand to easily find a product.

4 Query Management in the Backend connected to the database.

Kevin Rold´an 10

42

WM- 07 Web M. As a user, I want to search among all products by name, type, or brand to easily find a product.

4 Interface Design and Search Results Handling.

Jorge Mawyin 8

WM- 06 Web M. As a user, I want to filter among different products on the screen by categories and subcategories to have fewer elements on the screen.

4 Implementation of filtering functionality. Jorge Mawyin 12

Table 3.2: Sprint Backlog - Sprint 1

3. 3.2 Sprint Review

Date: June 09, 2024 Duration: 1 hour Assistants: Scrum Team (Developers, Scrum Master, Product Owner), normally employed in charge of inventory

Description of Meeting Objectives

This meeting aimed to present the first preview of the developed system, focusing mainly on the frontend section of both modules: the web module and the mobile module. We focused on validating with the stakeholder in charge of the inventory whether the layout of the content on the screen and the location of the various basic features of the mobile application were intuitive and met the established requirements. The same was done for the web section, ensuring that it aligned with the defined expectations and needs.

Stakeholder Feedback

- ”We consider that the layout of certain elements in the mobile version could be

optimized to improve the user experience since certain sections look very busy and are a little difficult to identify their function at a glance”

- ”Some elements of the mobile application could be rearranged to facilitate faster

access to the main functions.”

- ”The placement of key features in the web application meets our expectations and

the color distribution chosen to represent our business very well”

- ”We need to make sure the app is fully compatible with all major browsers.”

43

Decisions Made

- We will review the layout of items in the mobile application to enhance user-

friendliness.

- We will conduct additional tests to ensure that the website is error-free across

major browsers.

Sprint approval

To review the acceptance letter corresponding to sprint 1 you can go to the appendix subsection 9.4.1

3. 3.3 Sprint Retrospective

Date: June 09, 2024 Duration:35 min Assistants: Scrum Team (Developers, Scrum Master, Product Owner)

Sprint Successes

- We successfully completed all tasks assigned for this sprint without any complica-

tions regarding deadlines.

Sprint errors

- There were some communication issues that initially confused the team about the

tasks assigned to each member at the beginning of the sprint.

- Task allocation was uneven at times, leading to instances where development team

members had periods without assigned activities.

Identification of aspects to improve

- Improve communication among team members to prevent future issues affecting

product quality or delivery dates.

- Discuss how tasks are assigned at the beginning of each sprint and how to manage

periods when team members have significant downtime to avoid conflicts within the group.

44

3. 3.4 Burndown Chart

Figure 3.1: Sprint 1 Burndown Chart

45

### 3.4 Sprint 2

In Sprint 2, the team will focus on enhancing system security, improving user experience, and refining the functionality of the mobile application. For the website, the goals are to develop user account management and to implement the first part of the purchasing process, which includes the journey from product selection to the shopping cart.

3. 4.1 Sprint Backlog

Sprint 2 Start Date: 06/10/2024 Final Date: 06/30/2024 Total Effort:70

ID Product Backlog Item Priority Sprint Task Volunteer Estimated Effort (Hours)

MM- 04

Mobile M. As a system administrator, I want to be able to manage who can access the action log history in the inventory to keep the registration system secure.

2 Designing the Administration Interface for the Inventory System

Angel Tomal´a 8

Implement authentication system Angel Tomal´a 6

Access control and logging system for system access

Andr´es Cornejo 9

WM- 03 Web M. As an administrator, I want to provide clear and easy-to-understand resources to help beginner users navigate the platform.

2 Review of compliance with human-computer interaction criteria in the catalog and shopping section.

Jorge Mawyin 6

WM- 04 Web M. As a user, I want to experience a smooth purchasing process from product selection to transaction completion to avoid any complications during the payment process for one or more products.

3 Shopping Cart Functionality Kevin Rold´an 12

MM- 07

Mobile M. As an inventory area employee, I want auto-complete functionalities to expedite the process of registering new products.

4 Implementing logic for autocomplete Andr´es Cornejo 12

Interface for the new product registration section

Angel Tomal´a 8

46

WM- 05 Web M. As a user, I want to manage my account efficiently and access personalized functions to improve my shopping experience.

3 Designing the logging system and account management interface.

Jorge Mawyin 9

Table 3.3: Sprint Backlog - Sprint 2

3. 4.2 Sprint Review

Date: June 30, 2024 Duration: 25 min Assistants: Scrum Team (Developers, Scrum Master, Product Owner), Inventory Area Representative

Description of Meeting Objectives

This meeting aimed to review the progress and outcomes of Sprint 2, focusing on the enhancement of system security, improvements in user experience, and the refinement of mobile application functionality. The team also presented the development of user account management and the initial implementation of the purchasing process on the website. The key objectives were to validate the implementation of these features with stakeholders and gather feedback to ensure alignment with the project goals.

Stakeholder Feedback

- “The new admin interface for managing access to the inventory system’s action

log is well-organized, but additional instructions for first-time users might be necessary.”

- “The auto-complete feature in the mobile module significantly speeds up the prod-

uct registration process, which is a great improvement.”

- “The shopping cart functionality works smoothly; however, there were a few minor

issues managing the amount of product added.”

- “The user account management interface looks simple”

Decisions Made

- We will begin with the creation of the user manual since a direct guide in the app

would be counterproductive.

- Additional testing will be conducted on the shopping cart functionality to identify

and fix any bugs before the next sprint.

47

Sprint Approval

To review the acceptance letter corresponding to Sprint 2, you can go to the appendix subsection 9.4.2

3. 4.3 Sprint Retrospective

Date: June 30, 2024 Duration: 30 min Assistants: Scrum Team (Developers, Scrum Master, Product Owner)

Sprint Successes

- The team successfully implemented the auto-complete functionality in the mobile

module, which was well-received by the stakeholders.

- The initial phase of the purchasing process on the website was completed, enabling

a smooth transition from product selection to the shopping cart modal.

Sprint Errors

- There was a delay in the development of the authentication system for the mobile

module due to unforeseen technical challenges.

- The testing phase revealed some unexpected issues with the shopping cart func-

tionality that were not caught during initial development.

Identification of Aspects to Improve

- Increase the focus on early testing to catch potential issues before the final review.

48

3. 4.4 Burndown Chart

Figure 3.2: Sprint 2 Burndown Chart

49

### 3.5 Sprint 3

The goal of this sprint is to integrate new functionalities for both the mobile application and the website. We will focus on implementing technologies that simplify product registration and management, ensuring inventory information is accurate and up-todate. Additionally, we will enhance critical processes for the user experience, such as online payment management, and add personalization features to user accounts, allowing for better profile management and tracking of purchase history.

3. 5.1 Sprint Backlog

Sprint 3 Start Date: 07/01/2024 Final Date: 07/21/2024 Total Effort:77

ID Product Backlog Item Priority Sprint Task Volunteer Estimated Effort (Hours) MM- 02 Mobile M. As an inventory area employee, I want the application to offer me the option to register a product using a code or QR that directly identifies the product to facilitate the registration of new products.

1 Integration of the QR code scanner. Angel Tomal´a 10

Validation of the QR code and data storage. Andr´es Cornejo 6

WM- 02 Web M. As an administrator, I want the products shown to users to be directly related to those we have in the inventory to avoid inconsistencies when selling products.

1 Implement stock validations and display logic. Kevin Rold´an 10

WM- 04 Web M. As a user, I want to experience a smooth purchasing process from product selection to transaction completion to avoid any complications during the payment process for one or more products.

2 Implementation of payment gateway on the web

Kevin Rold´an 9

50

MM- 05 Mobile M. As an administrator, I want the system to show me images and key features of each of the products available in the inventory

3 Database query and presentation of key features

Kevin Rold´an 9

WM- 05 Web M. As a user, I want to manage my account efficiently and access personalized functions to improve my shopping experience.

3 Implementing the profile editing functionality.

Andr´es Cornejo 9

Implementing custom functions and recording purchase history.

Jorge Mawyin 10

Configuring email notification options. Jorge Mawyin 7

Implementing the wishlist feature. Angel Tomal´a 7

Table 3.4: Sprint Backlog - Sprint 3

3. 5.2 Sprint Review

Date: July 21, 2024 Duration: 35 min Assistants: Scrum Team (Developers, Scrum Master, Product Owner), Inventory Area Representative

Description of Meeting Objectives

The purpose of this meeting was to review the progress made during Sprint 3, which focused on integrating new functionalities for both the mobile application and the website. The primary goals were to simplify product registration and management processes, ensure inventory accuracy, and enhance user experience by implementing online payment management and personalization features in user accounts. The team presented these new features to the stakeholders to validate the implementation and gather feedback.

Stakeholder Feedback

- “The QR code scanner integration is a great addition, making product registration

much more efficient.”

- “The profile management enhancements, including purchase history tracking, are

useful, but there should be more detailed options for notifications.”

- “There were some issues with obtaining credentials for the payment gateway inte-

gration so this is expected to be addressed in the next sprint.”

51

Decisions Made

- The implementation of the payment gateway will be postponed until the next

sprint, changing the service used from Datafast to Paypal due to problems when integrating said gateway and at the request of the client. Responsibility will be taken to ensure that the payment gateway is thoroughly tested so that it works without problems.

Sprint Approval

To review the acceptance letter corresponding to Sprint 3, you can go to the appendix subsection 9.4.3.

3. 5.3 Sprint Retrospective

Date: July 21, 2024 Duration: 40 min Assistants: Scrum Team (Developers, Scrum Master, Product Owner)

Sprint Successes

- Successfully integrated the QR code scanner into the mobile application, stream-

lining the product registration process.

- Implemented stock validation and display logic on the website, which was well-

received by stakeholders.

- Added profile editing and purchase history tracking features, enhancing the user

experience on the website.

Sprint Errors

- The integration of the payment gateway encountered unforeseen issues, leading to

its delay and postponement to the next sprint.

- Some aspects of notification customization were not as detailed as expected by

stakeholders, requiring further refinement.

Identification of Aspects to Improve

- Increase focus on the testing and validation process for critical features like the

payment gateway to avoid delays in future sprints.

- Improve communication between developers and stakeholders during the design

phase to better align on expectations for new features.

52

3. 5.4 Burndown Chart

Figure 3.3: Sprint 3 Burndown Chart

53

### 3.6 Sprint 4

In this final sprint, the team will focus on integrating the latest key functionalities into the inventory system, with the primary task being the automatic synchronization of inventory changes with the web interface. Additionally, they will refine the sections dedicated to administrators that display the product flow within the inventory and streamline decision-making processes. This sprint aims to enhance inventory visibility and management, as well as provide advanced tools for informed decision-making.

3. 6.1 Sprint Backlog

Sprint 4 Start Date: 07/22/2024 Final Date: 08/11/2024 Total Effort: 72 hours

ID Product Backlog Item Priority Sprint Task Volunteer Estimated Effort (Hours) WM- 04 Web M. As a user, I want to experience a smooth purchasing process from product selection to transaction completion to avoid any complications during the payment process for one or more products.

3 Implementation of payment gateway on the web

Kevin Rold´an 9

MM- 08 Mobile M. As a system administrator, I want a tool that allows me to easily search and filter the history of actions taken on inventory products to better identify changes made in the records.

4 Implementation of Search and Filtering Functionality

Andr´es Cornejo 10

Roles and Permissions Management Angel Tomal´a 8

MM- 09 Mobile M. As a decision-making team member, I want the system to display the inventory flow, highlighting products with higher and lower movement frequency to facilitate decision-making by providing key information about product management.

4 Design of the User Interface section with exclusive access for administrators

Jorge Mawyin 10

54

MM- 06 Mobile M. As a system administrator, I want the ability to export the history of actions taken in the inventory in a format that allows for review and external analysis for decision-making purposes.

3 Implementation of the Exporter in multiple formats

Kevin Rold´an 8

User Interface and Access Control for Inventory Change History

Jorge Mawyin 7

Table 3.5: Sprint Backlog - Sprint 4

3. 6.2 Sprint Review

Date: August 11, 2024 Duration: 45 min Assistants: Scrum Team (Developers, Scrum Master, Product Owner), Inventory Area Representative

Description of Meeting Objectives

The goal of this meeting was to review the final sprint’s achievements, focusing on the integration of key functionalities into the inventory system. The primary task was the automatic synchronization of inventory changes with the web interface, along with the refinement of administrator sections that display product flow within the inventory. This sprint was aimed at enhancing inventory visibility, management, and decision-making capabilities. The team presented the completed features to stakeholders to confirm that the sprint objectives were met.

Stakeholder Feedback

- “The automatic synchronization with the Contifico system is functioning as ex-

pected.”

- “The new search and filtering tools make it much easier to track inventory changes,

which is a significant improvement.”

- “The payment gateway integration has been completed successfully, resolving the

issues from the previous sprint.”

- “Exporting inventory history in multiple formats is a useful feature, particularly

for external analysis and decision-making.”

Decisions Made

- The search and filtering tools will be further refined based on user feedback to

enhance usability.

55

- The team will monitor the performance of the automatic synchronization feature

in a live environment to ensure it functions as intended.

Sprint Approval

To review the acceptance letter corresponding to Sprint 4, you can go to the appendix subsection 9.4.4.

3. 6.3 Sprint Retrospective

Date: August 11, 2024 Duration: 35 min Assistants: Scrum Team (Developers, Scrum Master, Product Owner)

Sprint Successes

- Successfully implemented the automatic synchronization of inventory changes with

the Contifico system, providing real-time updates.

- Completed the payment gateway integration on the website, resolving previous

complications and ensuring a smooth purchasing process.

- Developed advanced tools for searching, filtering, and exporting inventory history,

which were well-received by stakeholders.

Sprint Errors

- Some initial challenges were encountered during the synchronization testing phase,

which required additional time to resolve.

- The user interface for inventory flow visualization required several iterations to

meet stakeholder expectations.

Identification of Aspects to Improve

v

- Improve initial testing procedures for synchronization features to catch potential

issues earlier in the sprint.

- Enhance collaboration between developers and stakeholders during the design

phase to reduce the number of iterations needed for user interface approval.

56

3. 6.4 Burndown Chart

Figure 3.4: Sprint 4 Burndown Chart

57

# 4 Coding Standards Documentation

Coding standards are sets of rules and conventions designed to guide the process of writing code in a software development project. These guidelines establish common practices that help improve the readability, consistency, and maintainability of the code.

### 4.1 Coding Standards - Mobile Module

4. 1.1 Naming Convention and Organization

Variables Use meaningful and descriptive names for variables, following Dart naming conventions like camelCase. Group related variables together within classes or functional components.

Classes Name classes using PascalCase, starting with a noun or noun phrase that describes the class’s purpose (e.g., UserProfile, HttpService). Consider organizing related classes into separate files or directories.

Widgets Name widgets using PascalCase, reflecting their role in the UI hierarchy (e.g., Home- Page, LoginForm). Organize widget files based on their location in the app’s navigation structure.

Functions/Methods Name functions and methods using camelCase, emphasizing action verbs or descriptive phrases (e.g., calculateTotal, fetchUserData). Keep related functions together within classes or functional components.

Directories Organize files into logical directories based on functionality or feature sets (e.g., screens/, models/, utils/). Keep the directory structure flat to avoid deep nesting.

4. 1.2 Formatting and Indentation

Indentation Style Use spaces for indentation with a standard width (typically 2 or 4 spaces). Ensure consistent indentation throughout the codebase.

58

Line Length Limit lines to a reasonable length (100 in this module) to enhance readability. Break long lines into multiple lines when necessary.

Brace Placement Place opening braces on the same line as control structures and function declarations. Use consistent brace placement for clarity.

4. 1.3 Comments and Documentation

Inline Comments Use comment sparingly to explain complex logic or clarify non-obvious code. Focus on explaining ”why” rather than ”what” if the code is self-explanatory.

Function/Method Comments Document functions and methods using Dartdoc comments, including descriptions, parameter types, and return types. Provide usage examples when appropriate.

Class Documentation Document classes with Dartdoc comments, describing their purpose, properties, and usage. Include relevant details about class behavior and relationships.

File-Level Documentation Provide an overview of the file’s contents and purpose in a comment at the top of the file. Summarize its role within the app and any important information about its contents.

File-Level Documentation Use tools like Dartdoc to generate API documentation from code annotations automatically.

4. 1.4 Exception Handling / Logging

Exception Types Define custom exceptions for specific error conditions if necessary, ensuring they provide meaningful information about the error. Use built-in exceptions for general error handling.

Error Messages Craft clear and informative error messages that help developers diagnose and troubleshoot issues. Include relevant context and information about the error’s cause.

Logging Levels Use logging libraries like logger to log messages at different levels (e.g., debug, info, warning, error). Adjust the log level based on the severity and importance of the message.

59

4. 1.5 Testing

Test File Naming Name test files using the same name as the file being tested, suffixed with test.dart (e.g., widget test.dart, api service test.dart).

Test Case Naming Name test cases descriptively to communicate their purpose and expected behavior (e.g., testSignInSuccess, testCalculateTotalWithDiscount).

Test Structure Organize tests into logical groups based on functionality or feature sets. Use setUp and tearDown methods to set up and tear down test environments as needed.

Assertions Write assertions to verify expected outcomes and behavior. Use expressive matchers provided by testing frameworks like flutter test to enhance readability and clarity.

60

### 4.2 Coding Standards - Web Module

4. 2.1 Backend

Below are the codes standard used in our project in the backend section. To learn more about the features used, visit the following link about python code standards.

Code Lay-out

Indentation Four spaces should be used per indentation level. Continuation lines should align wrapped elements either vertically using Python’s implicit line joining inside parentheses, brackets and braces, or using a hanging indent.

Tabs vs. Spaces Spaces should be the preferred indentation method.Tabs should be used solely to remain consistent with code that is already indented with tabs.

Maximum Line Length Avoid lines longer than 79 characters.

Blank Lines Surround top-level function and class definitions with two blank lines. Method definitions inside a class are surrounded by a single blank line.

Imports Imports should usually be on separate lines. Imports are always put at the top of the file, just after any module comments and docstrings, and before module globals and constants. Imports should be grouped in the following order:

1. Standard library imports.

2. Local application/library specific imports.

String quotes

In Python, single-quoted strings and double-quoted strings are the same, so we use bouth.

Whitespace in Expressions and Statements

Unnecessary white spaces will be avoided in the following situations:

- Immediately inside parentheses, brackets or braces.

- Between a trailing comma and a following close parenthesis.

61

- Immediately before a comma, semicolon, or colon.

- Immediately before the open parenthesis that starts the argument list of a function

call.

- Immediately before the open parenthesis that starts an indexing or slicing.

- More than one space around an assignment (or other) operator to align it with

another.

Comments

Block comments generally consist of one or more paragraphs built out of complete sentences, with each sentence ending in a period. The comments should be clear and easily to understand. Comments should be complete sentences. The first word should be capitalized, unless it is an identifier that begins with a lower case letter.

Inline comments An inline comment is a comment on the same line as a statement. Inline comments should be separated by at least two spaces from the statement. They should start with a # and a single space.

Naming conventions

The naming conventions of Python’s library are a bit of a mess, so we’ll never get this completely consistent – nevertheless, here are the currently recommended naming standards.

Classes Class names should be nouns and use with the first letter of each internal world capitalized convention. Try to keep the class names simple and descriptive.

Function and Variable Names Function names should be lowercase, with words separated by underscores as necessary to improve readability.

Method Names and Instance Variables Use the function naming rules: lowercase with words separated by underscores as necessary to improve readability.

62

4. 2.2 Apply code standards - Backend

Flake8 for Django Flake8 was chosen as the linter tool for the Django project due to its ability to combine multiple static analysis tools into one solution. Unlike other linter tools, Flake8 integrates Pyflakes, pycodestyle (formerly pep8), and McCabe, providing comprehensive coverage to detect errors and improve Python code quality.

Flake8 Configuration To configure Flake8 for an Django project, we create a file called (setup.cfg) at the root of the project and define the Flake8 rules according to our code standards.

Figure 4.1: Configuration of Flake8 tool.

This configuration is made with our coding standards.

- max-line-length = 79: This setting specifies the maximum allowed line length

in the code.

- exclude: This option specifies directories and files to exclude from Flake8’s linting

process. In our case we ignore the files that django created by himself and we don’t edit them like: ’app.py’, ’modules.py’, ’admind.py’, etc.

63

- per-file-ignores: This option allows for the specification of per-file exceptions

to certain Flake8 rules. In this case, we decided to ignore the ’models.py’ and ’urls.py’ profiles since some lines in those files generated a 501 error (line too long), but these lines could not be modified as they needed all the characters they have.

These Flake8 configurations are designed to enforce coding standards and best practices, promoting code readability, consistency, and maintainability throughout the project.

Flake8 tool execution result before correct the code

Figure 4.2: Flake8 tool execution result before correct the code.

Description of Errors: The most common code standard errors we found were:

- E261: This error indicates that there are at least two spaces before inline comment.

To resolve this error, we align the comment with the code.

- E501: This error indicates that a line is too long according to the configured

maximum line length. To fix this error, we considered breaking the line into multiple shorter lines.

- E302: This error indicates that there are too many blank lines after a function or

class definition. To resolve this error, we remove the extra blank lines to adhere to the project’s coding standards.

Flake8 tool execution result after correct the code

Figure 4.3: Flake8 tool execution result after correct the code.

64

4. 2.3 Frontend

Below are the code standards used in our project in the frontend section. To learn more about the features used, visit the following link about Angular Coding Style Guide and Best Practices.

Project Structure

Maintain a consistent folder structure to improve code organization and facilitate collaboration. Organize files logically, separating components, services, modules and other resources into dedicated directories. (e.g., src/app, src/assets, src/app/interfaces, src/app/pages, src/app/services).

Angular CLI Use the Angular CLI (Command Line Interface) for creating projects, generating components, services, modules, and more. The CLI enforces best practices, reduces human error, and provides a standardized approach to project setup.

Modular Architecture Adopt a modular approach by breaking your application into smaller, reusable modules. Each module should have a well-defined purpose and responsibility. This promotes code separation, re-usability, and easier maintenance.

Naming Conventions

Use a descriptive and consistent naming conventions for files, classes, variables, and functions. This improves the readability of the code and facilitates collaborative work.

Modules and Component Module and component names should be in PascalCase and end with Module. Example: UserProfileModule.

Services Service names should be in PascalCase and end with Service. Example: UserService.

Component Structure

Components should be organize with a consistent structure, including template, styles, and TypeScript file. This separation improves code readability and encourages the use of the Component-Driven Development approach.

File Naming

File names should be in kebab-case (lowercase with hyphens). Example: user-profile.component.ts.

65

Code Layout

Indentation Two spaces should be used per indentation level.

Maximum Line Length Avoid lines longer than 120 characters.

Blank Lines Separate related code blocks with a blank line to improve readability.

Component Structure

Template and Style Files Use separate HTML/CSS files for templates if they exceed 3 lines.

Inline Templates and Styles Allowed only for very simple components with few lines of HTML or CSS.

Imports

Imports should be grouped in the following order:

1. Angular imports (e.g., @angular/core).

2. External libraries.

3. Internal project modules.

String Quotes

Single quotes (’’) should be used for string literals.

Whitespace in Expressions and Statements

Unnecessary white spaces should be avoided in the following situations:

- Immediately inside parentheses, brackets, or braces.

- Between a trailing comma and a following close parenthesis.

- Immediately before a comma, semicolon, or colon.

66

Comments

Comments should be added when:

- The code is complex and may be hard to understand for someone who didn’t write

it.

- You’re using a non-obvious approach to solve a problem or a workaround for a

known issue.

Single-line Comments In JavaScript, single-line comments begin with two forward slashes //. They should be use for brief explanations.

Multi-line Comments Multi-line comments in JavaScript start with /* and end with */. They should be use for longer descriptions.

Angular’s Inline Template Comments In Angular, can use HTML comments (start with <!-- and end with -->) within component templates.

Comment Style Guidelines Comments should have this general style guidelines:

- Comment have to start with a capital letter.

- Use proper grammar and punctuation.

- Keep comments concise and to the point.

Version Control

Commit Messages Follow a clear convention for commit messages (e.g., Conventional Commits).

4. 2.4 Apply code standards - Frontend

Prettier Tool for angular We chose to use Prettier as our code standardization tool for our Angular project for several reasons. Firstly, Prettier ensures consistency in code formatting, making collaboration and code comprehension among team members easier. Additionally, by automating formatting according to predefined rules, it saves developers time and reduces style conflicts within the team. Its easy integration into the development workflow was also a significant factor in our decision.

67

Prettier configuration To configure Prettier for an Angular project, you create a file at the root of the project and define the Prettier rules according to your code standards.

Figure 4.4: Prettier configuration file.

This configuration is made with our coding standards.

- singleQuote: true: Ensures the use of single quotes for string literals, promoting

consistency in the code-base.

- semi: false: Disables the insertion of semicolons at the end of statements, reduc-

ing visual clutter and adhering to a common style preference.

- tabWidth: 2: Sets the width of each tab to 2 spaces, promoting readability and

consistency in indentation.

- printWidth: 120: Specifies the maximum line length before Prettier wraps the

code, improving readability and preventing horizontal scrolling.

- trailingComma: ”all”: Includes trailing commas in object literals and arrays,

making it easier to add or remove items without modifying adjacent lines.

- bracketSpacing: true: Enforces spacing within object literals, enhancing code

clarity and consistency.

68

- jsxBracketSameLine: false: Forces JSX closing brackets to be placed on a new

line, improving readability by separating tags from their content.

- htmlWhitespaceSensitivity: ”ignore”: Ignores white-space in HTML files,

ensuring consistent formatting regardless of white-space variations.

- endOfLine: ”lf”: Specifies LF (line feed) as the line ending character, ensuring

cross-platform compatibility.

- arrowParens: ”avoid”: Avoids unnecessary parentheses around single-parameter

arrow function arguments, improving code readability.

Files ignore Automatically generated files, which underwent no changes, were ignored.

Figure 4.5: Prettier ignore configuration file.

Prettier tool result Prettier applies the specified changes from the .prettierrc file to all files not listed in the .prettierignore file. To execute Prettier, the command (npm run format) is used.

69

Figure 4.6: Prettier ignore configuration file.

70

# 5 Preemptive Error Detection

### 5.1 Preemptive Error - Mobile Module

5. 1.1 Backend

Pylint for Python The tool for the static analysis of the mobile application backend was Pylint since it not only helps to detect errors, but its scope ranges from coding convention to detecting logical errors and improving code readability. In addition, it is one of the most used tools for static analysis for python development, so it allows you to establish any rule that is necessary.

Features and Typical Issues Detected:

- Comprehensive Code Analysis: Pylint performs a thorough analysis of your

Python code, checking for errors, enforcing coding standards, and detecting potential bugs.

- PEP 8 Compliance: Pylint helps ensure that your code adheres to the PEP 8

style guide, which is the de facto coding standard for Python.

- Detects Code Smells: Pylint identifies code smells like duplicate code, long

methods, and deeply nested loops, which can help you refactor and improve your code.

- Documentation and Support: Pylint has comprehensive documentation and

an active community, providing support and resources to help you get the most out of the tool.

Configuration The following rules represent various aspects of code styling, naming conventions, line length, incorrect imports, and other best practices by Pylint.

- W1514-unspecified-encoding This warning occurs when the open function is

used without explicitly specifying the encoding parameter. It’s recommended to specify an encoding to avoid potential issues with file reading/writing, especially when dealing with non-ASCII characters.

- W0105-pointless-string-statement This warning indicates that there is a string

statement that is not being used in any way. In Python, placing a string in the

71

middle of the code without assigning it to a variable or using it in any way is pointless and can be removed.

- C0114-missing-module-docstring This convention message indicates that the

module is missing a docstring at the top. A module docstring should describe the purpose and contents of the module.

- C0411-wrong-import-order This convention message indicates that the import

order is incorrect. According to PEP 8, imports should be grouped in the following order: standard library imports, related third-party imports, and local application/library-specific imports.

- C0301-line-too-long This convention message indicates that a line exceeds the

maximum allowed length. The default maximum length is 100 characters.

- C0103-invalid-name his convention message indicates that a variable, function,

or constant name does not conform to naming conventions. For example, constants should be in UPPER CASE, variables and functions should be in lower case with underscores, and classes should be in CapitalizedWords.

Tool Execution Results The errors found in the code written to date, according to the rules defined above, were as follows.

Figure 5.1: Results of static testing mobile.

After Pylint displays errors and violations of code standards based on the rules that were chosen, that code was corrected to enforce and maintain these standards.

5. 1.2 Frontend

Dart Analyzer for Flutter Using Dart Analyzer for static analysis offers several advantages over other tools. One of the main benefits is its deep integration with the Dart language itself.

72

Features and Typical Issues Detected:

- Code Quality and Standards Enforcement: Dart Analyzer helps ensure that

your code adheres to established coding standards and best practices.

- Improved Maintainability: Static analysis helps in maintaining a clean and

readable codebase.

- Integration with Development Tools: Dart Analyzer integrates seamlessly

with various development environments and CI/CD pipelines.

Configuration The following rules represent various aspects of code styling, naming conventions, line length, incorrect imports, and other best practices by Dart Analyzer.

- always declare return types: This rule enforces that all functions and meth-

ods must explicitly declare their return types. This improves code readability and helps avoid potential issues with type inference.

- prefer const constructors: This rule suggests using const constructors when-

ever possible. Using const constructors can improve performance by creating a compile-time constant and reducing the memory footprint.

- prefer final fields: This rule encourages marking fields as final if they are not

reassigned after their initial assignment. This ensures immutability and makes the code easier to understand and maintain.

Figure 5.2: All rules static testing for mobile app.

73

Tool Execution Results The errors found in the code written to date, according to the rules defined above, were as follows.

Figure 5.3: Results of static testing mobile.

After Dart Analyzer displays errors and violations of code standards based on the rules that were chosen, that code was corrected to enforce and maintain these standards.

74

### 5.2 Preemptive Error - Web Module

5. 2.1 Backend

Flake8 tool To ensure the quality and consistency of code in our Django project, we utilized Flake8. This tool combines several useful functionalities for static code analysis in Python, including error detection, compliance with coding standards, and identification of cyclomatic complexity. By integrating Flake8 into our workflow, we were able to detect and address issues from early stages of development, ensuring that our code is clean, readable, and easy to maintain. Therefore, Flake8 already covers code standards and PMD.

5. 2.2 Frontend

ESLint for Angular ESLint was selected for the Angular project due to its flexibility and extensibility. ES- Lint is a popular tool for analyzing JavaScript and TypeScript code and is particularly known for its ability to be customized through configurations and plugins. Compared to other tools like JSHint or JSLint, ESLint offers greater configurability and a wide range of rules that can be tailored to the specific needs of the project.

Features and Typical Issues Detected:

- Syntax Errors: ESLint can detect syntax errors in JavaScript/TypeScript code,

helping to prevent runtime errors.

- Best Practices: Ensures the code follows best development practices, such as

recommending the use of === instead of == to avoid comparison errors.

- Code Style Consistency: Enforces consistent coding style, such as the use of

single or double quotes, bracket placement, and semicolon usage.

- Complexity Issues: Similar to Flake8, ESLint can measure the cyclomatic com-

plexity of JavaScript/TypeScript code, identifying overly complex functions and suggesting refactorings.

- Usage of Variables and Functions: ESLint detects variables and functions that

are declared but not used, as well as variables used before being defined, helping to eliminate dead code and prevent errors.

Configuration In the ESLint configuration file (.eslintrc.json), the following settings have been specified to maintain code quality:

- "parser": This setting specifies the parser to be used by ESLint for TypeScript

files.

75

- "extends": This option extends the recommended configurations provided by

@typescript-eslint and @angular-eslint plugins.

- "rules": This section defines specific ESLint rules and their configurations.

Figure 5.4: Configuration of ESlint tool.

Tool Execution Results

Figure 5.5: ESlint tool execution result.

76

Description of Errors: The most common code standard errors we found were:

- @typescript-eslint/no-unused-vars: This error indicates that there are unused

variables in the TypeScript code. To resolve this error, we remove the unused variables.

- @typescript-eslint/no-explicit-any: This error indicates the use of the ‘any‘

type, which can lead to type safety issues in TypeScript. To fix this error, we avoid using the ‘any‘ type and use more specific interfaces.

- no-var: This error indicates the use of the ‘var‘ keyword to declare variables,

which is discouraged in modern JavaScript/TypeScript development. To resolve this error, use ‘const‘ instead of ‘var‘ to declare variables.

Tool execution after to correct the code

Figure 5.6: ESlint tool execution after to correct the code.

Apex PMD tool As another option, we decided to use Apex PMD in our project due to its ability to significantly improve code quality. Apex PMD is a static analysis tool that allows us to detect errors, bad practices, and vulnerabilities in our source code from the early stages of development.

77

Apex PMD tool execution

Figure 5.7: Apex PMD tool execution.

As we can see, after running Apex PMD on our project’s frontend, there were no corrections needed.

78

# 6 Mobile Module Test Documentation

### 6.1 Test plan

Test Plan for: Nintventario Inventory System (NIS) Context, Test Items & Scope This test plan outlines the testing strategy for the Inventory Management Application. The primary objective is to ensure that the application functions correctly across all supported devices and that it meets the requirements specified for inventory creation, management, and reporting. The test items include user authentication, inventory management features, reporting tools, and data synchronization mechanisms. The scope covers functional testing, UI testing, and integration testing. Team & Communication The testing team comprises developers, quality assurance engineers, and product managers. Communication channels include meetings, email updates, and issue tracking through a project management tool. Stakeholders Stakeholders include the project manager, development team, quality assurance team, and end users (inventory managers). They are responsible for defining the requirements, validating the test results, and ensuring that the application meets the business needs.

Risk Analysis:

ID Feature Risk Probability (1-10) Impact (1-10) Risk Number Mitigation Activities R1 Login Users may not be able to log in due to authentication failures or incorrect credentials.

6 8 48 Functional tests: Verify login process, including validation and error handling. R2 Select location for inventory

Users may select the wrong location for inventory, leading to incorrect stock updates.

5 7 35 UI tests: Ensure location selection is clear and errorfree.

79

R3 Create new inventories

Users might experience issues when creating new inventories due to form validation errors.

5 8 40 Functional tests: Verify inventory creation process, including validation and data handling. R4 Continue inventories via drafts

Drafts may not load correctly, causing users to lose progress in ongoing inventories.

6 7 42 Functional tests: Ensure that drafts can be saved and loaded reliably.

R5 Save drafts Drafts might not save properly, leading to loss of data or incomplete inventories.

7 7 49 Functional tests: Verify that drafts are saved correctly and can be accessed later. R6 Update product stock

Stock updates may fail or not synchronize properly, leading to discrepancies in inventory levels.

6 9 54 Integration tests: Ensure that stock updates are processed and synchronized correctly. R7 Search products The search functionality may return incorrect or no results, leading to inefficiencies in inventory management.

5 6 30 Functional tests: Validate search accuracy and performance.

R8 Filter by checked / unchecked

Users may be unable to filter products correctly by checked/unchecked status, leading to confusion and errors.

4 6 24 UI tests: Ensure filters work correctly and provide accurate results.

80

R9 Scan product by QR

The QR scanning feature may fail to recognize products, causing delays in inventory processing.

5 8 40 Functional tests: Verify QR scanning accuracy and speed.

R10 Generate an Excel file with updated products

The Excel generation feature may produce incorrect or incomplete data, affecting inventory records.

4 7 28 Functional tests: Ensure that Excel files are generated correctly with accurate data. R11 Generate a report in PDF format

PDF reports may not generate correctly or include all necessary information, leading to incomplete documentation.

3 6 18 Functional tests: Verify PDF generation accuracy and completeness.

R12 Write observations saved in drafts

Users may be unable to save observations in drafts, leading to incomplete or missing notes.

5 5 25 Functional tests: Ensure that observations can be saved and retrieved reliably in drafts. R13 Display product list

The product list may not display correctly, leading to missing or incorrect information.

4 7 28 UI tests: Ensure that the product list is displayed correctly with accurate details.

R14 Sort product list by checked / unchecked

The sorting functionality may not work correctly, leading to incorrect ordering of products.

4 6 24 Functional tests: Verify sorting accuracy by checked/unchecked status.

81

R15 Filter drafts by completed/uncompleted

Users may not be able to filter drafts correctly, causing confusion in managing inventory tasks.

5 6 30 Functional tests: Ensure draft filtering works accurately by completion status. R16 Mark drafts as completed

Users may be unable to mark drafts as completed, leading to incomplete task management.

5 5 25 Functional tests: Verify that drafts can be correctly marked as completed.

R17 Mark drafts as uncompleted

Users may be unable to revert drafts to uncompleted status, causing issues in inventory management.

4 5 20 Functional tests: Ensure that drafts can be correctly marked as uncompleted.

R18 Delete drafts Users may accidentally delete drafts or may be unable to delete them, leading to data loss or clutter.

6 6 36 Functional tests: Verify that drafts can be deleted correctly with proper confirmation.

R19 Modify inventory manager name

Users may be unable to update the name of the inventory manager, leading to incorrect records.

4 5 20 Functional tests: Ensure that the manager’s name can be updated correctly. R20 Modify inventory creation date

Users may be unable to change the inventory creation date, leading to inaccuracies in records.

3 5 15 Functional tests: Verify that the creation date of inventories can be updated correctly.

Table 6.1: Risk Analysis for Mobile Inventory Management Application

82

Risk Prioritization

Figure 6.1: Risk Prioritization Matrix: High Impact and High Likelihood

Test strategy:

The testing strategy for the Inventory Management Application is designed to mitigate the identified risks through a comprehensive set of testing activities. These activities include functional testing, UI testing and acceptance testing, each tailored to address specific risks associated with the features of the application

83

### 6.2 Test case specification

6. 2.1 Unit Test Cases

To perform and execute the tests on the mobile component, the flutter test library was used, which allowed the logic of these tests to be separated and executed all simultaneously. The library offers functionalities like widget testing, which allows developers to test individual widgets in isolation, ensuring they behave as expected under various scenarios.

Screen Home Tests

Test Case ID: TCMH1 Purpose: Verify the AppBar title on the home screen Priority: 3 Test Coverage Item: T1 Preconditions: The home screen is displayed. Inputs: Tap action. Expected Results: The AppBar title is ”HOME” with font size 40.

Table 6.2: Test case to verify AppBar title on the home screen

Test Case ID: TCMH2 Purpose: Verify the welcome text on the home screen Priority: 2 Test Coverage Item: T1 Preconditions: The home screen is displayed. Inputs: Tap action. Expected Results: The text is ”Welcome to ” followed by place.

Table 6.3: Test case to verify the welcome text on the home screen

Test Case ID: TCMH3.1 Purpose: Verify the creation of inventory Priority: 1 Test Coverage Item: T1 Preconditions: The home screen is displayed. Inputs: Tap action. Expected Results: MenuItem with icon edit document, label ”Create Inventory”. Postconditions: Go to TabBar.

Table 6.4: Test case to verify the creation of inventory

84

Test Case ID: TCMH3.2 Purpose: Verify access to history Priority: 2 Test Coverage Item: T1 Preconditions: The home screen is displayed. Inputs: Tap action. Expected Results: MenuItem with icon history, label ”History”. Postconditions: Go to History page.

Table 6.5: Test case to verify access to history

Test Case ID: TCMH3.3 Purpose: Verify access to settings Priority: 2 Test Coverage Item: T1 Preconditions: The home screen is displayed. Inputs: Tap action. Expected Results: MenuItem with icon settings, label ”Settings”. Postconditions: Go to Settings page.

Table 6.6: Test case to verify access to settings

Test Case ID: TCMH3.4 Purpose: Verify app exit functionality Priority: 1 Test Coverage Item: T1 Preconditions: The home screen is displayed. Inputs: Tap action. Expected Results: MenuItem with icon exit to app, label ”Exit”. Postconditions: Quit the app.

Table 6.7: Test case to verify app exit functionality

85

Screen TabBar Tests

Test Case ID: TCMTB1 Purpose: Verify the initialization of the CustomTabBar widget Priority: 3 Test Coverage Item: T2 (Widget Initialization) Preconditions: N/A Inputs: N/A Expected Results: CustomTabBar widget is rendered Postconditions: Initialization of widget

Table 6.8: Test case for Widget Initialization

Test Case ID: TCMTB2 Purpose: Verify the loading state when ’Crear Inventario’ is tapped Priority: 2 Test Coverage Item: T2 (Loading State) Preconditions: N/A Inputs: Tap on ’Crear Inventario’ Expected Results: Loading indicator is displayed Postconditions: Verify loading state

Table 6.9: Test case for Loading State

Test Case ID: TCMTB3 Purpose: Verify the error state of the CustomTabBar widget Priority: 2 Test Coverage Item: T2 (Error State) Preconditions: N/A Inputs: N/A Expected Results: Error message is displayed Postconditions: Verify error state

Table 6.10: Test case for Error State

86

Test Case ID: TCMTB4 Purpose: Verify display of ”No products found” message when no products are available Priority: 2 Test Coverage Item: T2 (No Products Found) Preconditions: N/A Inputs: N/A Expected Results: ”No products found” message is displayed Postconditions: Verify display of message

Table 6.11: Test case for ”No Products Found” message

Test Case ID: TCMTB5 Purpose: Verify tab selection functionality Priority: 1 Test Coverage Item: T2 (Tab Selection) Preconditions: Tap on different tabs Inputs: Tap on element Expected Results: Corresponding page is displayed Postconditions: Verify tab selection

Table 6.12: Test case for Tab Selection

Test Case ID: TCMTB6 Purpose: Verify that Tab bar labels match expected values Priority: 3 Test Coverage Item: T2 (Tab Bar Labels) Preconditions: N/A Inputs: N/A Expected Results: Tab bar labels match expected values Postconditions: Verify tab bar labels

Table 6.13: Test case for Tab Bar Labels

87

Test Case ID: TCMTB7 Purpose: Verify that Tab bar icons are rendered properly Priority: 2 Test Coverage Item: T2 (Tab Bar Icons) Preconditions: Enter in the widget Inputs: N/A Expected Results: Tab bar icons are rendered properly Postconditions: Verify tab bar icons

Table 6.14: Test case for Tab Bar Icons

Test Case ID: TCMTB8 Purpose: Verify that the correct page is displayed when swiping through the pages Priority: 1 Test Coverage Item: T2 (Page View) Preconditions: Swipe through the pages Inputs: N/A Expected Results: Correct page is displayed Postconditions: Verify page view

Table 6.15: Test case for Page View

Test Case ID: TCMTB9 Purpose: Verify that page transition animation occurs smoothly when tapping on different tabs Priority: 1 Test Coverage Item: T2 (Tab Bar Tap Animation) Preconditions: Tap on different tabs Inputs: N/A Expected Results: Page transition animation occurs smoothly Postconditions: Verify tap animation

Table 6.16: Test case for Tab Bar Tap Animation

88

Widget DateSelector Tests

Test Case ID: TCMDSW1 Purpose: Verify that the initial selected date is displayed correctly in the DateSelectorWidget Priority: 2 Test Coverage Item: T3 (Initial Date Display) Preconditions: N/A Inputs: N/A Expected Results: Today’s date is displayed Postconditions: Verify initial date display

Table 6.17: Test case for initial date display in DateSelectorWidget

Test Case ID: TCMDSW2 Purpose: Verify that the date picker dialog opens when tapping on the DateSelectorWidget Priority: 1 Test Coverage Item: T3 (Date Picker Interaction) Preconditions: N/A Inputs: Tap on widget Expected Results: Date picker dialog is displayed Postconditions: Verify date picker opens

Table 6.18: Test case for date picker interaction in DateSelectorWidget

Test Case ID: TCMDSW3 Purpose: Verify that the onDateSelected callback is called with the correct date when a date is selected Priority: 1 Test Coverage Item: T3 (Date Selection Callback) Preconditions: N/A Inputs: Select a date and tap ’OK’ Expected Results: onDateSelected is called with the picked date Postconditions: Verify callback is called with correct date

Table 6.19: Test case for date selection callback in DateSelectorWidget

89

SalesSpots Screen Tests

Test Case ID: TCMSS1 Purpose: Verify that all sale spot locations are displayed correctly on the SaleSpotsPage Priority: 2 Test Coverage Item: T4 (Locations Display) Preconditions: N/A Inputs: N/A Expected Results: All sale spot locations are displayed Postconditions: Verify locations display

Table 6.20: Test case for displaying sale spot locations on SaleSpotsPage

Test Case ID: TCMSS2 Purpose: Verify that tapping on a location updates the global variable ’local’ and navigates to the Home screen Priority: 1 Test Coverage Item: T4 (Location Selection) Preconditions: N/A Inputs: Tap on a location image Expected Results: Global variable ’local’ is updated and navigates to Home screen Postconditions: Verify location is selected and navigation occurs

Table 6.21: Test case for selecting a location and navigation in SaleSpotsPage

Test Case ID: TCMSS3 Purpose: Verify that the selected location is logged correctly in debug mode when tapped Priority: 2 Test Coverage Item: T4 (Location Logging in Debug Mode) Preconditions: Debug mode enabled Inputs: Tap on a location image Expected Results: Selected location is logged Postconditions: Verify log output

Table 6.22: Test case for logging selected location in SaleSpotsPage in debug mode

90

Inventory Details Tests

Test Case ID: TCINV1 Purpose: Verify that the InventoryDetails widget is displayed correctly with the correct ID, employee name, initial duration, and DateSelectorWidget Priority: 1 Test Coverage Item: T5 (Inventory Details Display) Preconditions: Globals: inventoryId = ’INV12345’, globalEmployeeName = ’John Doe’, globalDate = ’2024-08-10’ Inputs: N/A Expected Results: InventoryDetails screen is displayed correctly with the correct ID, employee name, initial duration, and DateSelector- Widget Postconditions: Verify correct display of AppBar title, Inventory ID, Employee name TextField, Duration TextField, DateSelector- Widget, and ’Guardar borrador’ button

Table 6.23: Test case for displaying InventoryDetails widget

Test Case ID: TCINV2 Purpose: Verify that entering an employee name and duration, then saving the draft, works correctly Priority: 1 Test Coverage Item: T5 (Saving Draft in Inventory Details) Preconditions: InventoryDetails screen displayed Inputs: Enter ’Jane Smith’ in Employee name TextField, Enter ’5’ in Duration TextField, Tap ’Guardar borrador’ button Expected Results: Draft is saved and SnackBar with ’Guardar borrador’ message is shown Postconditions: Verify that SnackBar appears with the correct message

Table 6.24: Test case for saving a draft in InventoryDetails widget

91

Draft Tests

Test Case ID: TCDFT1 Purpose: Verify that a Draft instance is created with default values when no parameters are provided Priority: 2 Test Coverage Item: T6 (Draft Default Values) Preconditions: SharedPreferences initialized Inputs: Create a new ‘Draft‘ instance without parameters Expected Results: Draft object is created with default values for ID, employee, duration, creationDate, state, products, and observations Postconditions: Verify that the Draft object has default values for each property

Table 6.25: Test case for Draft default values

Test Case ID: TCDFT2 Purpose: Verify that a Draft instance correctly converts to a JSON object Priority: 1 Test Coverage Item: T6 (Draft to JSON Conversion) Preconditions: N/A Inputs: Create a ‘Draft‘ instance with specific values, call ‘toJson()‘ method Expected Results: JSON object is created with the correct values from the Draft instance Postconditions: Verify the JSON object matches the expected values

Table 6.26: Test case for Draft to JSON conversion

Test Case ID: TCDFT3 Purpose: Verify that a Draft instance saves and loads correctly from SharedPreferences Priority: 1 Test Coverage Item: T6 (Draft Save and Load) Preconditions: SharedPreferences initialized Inputs: Create a ‘Draft‘ instance with specific values, call ‘save- Draft()‘ method, then load the drafts Expected Results: The saved Draft is correctly loaded from SharedPreferences Postconditions: Verify that the loaded Draft matches the saved values

Table 6.27: Test case for saving and loading a Draft from SharedPreferences

92

Test Case ID: TCDFT4 Purpose: Verify that a Draft instance updates an existing draft in SharedPreferences Priority: 1 Test Coverage Item: T6 (Draft Update in SharedPreferences) Preconditions: SharedPreferences initialized, an existing Draft with the same ID saved Inputs: Create a new ‘Draft‘ instance with the same ID but different values, call ‘saveDraft()‘ method Expected Results: The existing Draft in SharedPreferences is updated with the new values Postconditions: Verify that the updated Draft has the new values in Shared- Preferences

Table 6.28: Test case for updating a Draft in SharedPreferences

93

History Tests

Test Case ID: TCDS1 Purpose: Verify that DraftsScreen displays a loading indicator while drafts are loading Priority: 2 Test Coverage Item: T7 (Loading Indicator Display) Preconditions: SharedPreferences initialized Inputs: Launch ‘DraftsScreen‘ Expected Results: CircularProgressIndicator is displayed while drafts are loading Postconditions: Verify that the loading indicator is displayed

Table 6.29: Test case for loading indicator in DraftsScreen

Test Case ID: TCDS2 Purpose: Verify that DraftsScreen displays ”No drafts available” when no drafts exist Priority: 2 Test Coverage Item: T7 (Empty State Message) Preconditions: SharedPreferences initialized with no drafts Inputs: Launch ‘DraftsScreen‘, wait for loading to complete Expected Results: ”No hay borradores disponibles.” message is displayed Postconditions: Verify that the ”No drafts available” message is shown when no drafts exist

Table 6.30: Test case for empty state in DraftsScreen

Test Case ID: TCDS3 Purpose: Verify that DraftsScreen displays a list of drafts correctly Priority: 1 Test Coverage Item: T7 (Drafts List Display) Preconditions: SharedPreferences initialized with drafts Inputs: Create and save two Draft instances, then launch ‘DraftsScreen‘ Expected Results: A list of saved drafts is displayed on the screen Postconditions: Verify that the correct number of drafts are displayed with the correct details

Table 6.31: Test case for displaying drafts list in DraftsScreen

94

Product Details Tests

Test Case ID: TCPD1 Purpose: Verify that the ProductDetails screen displays the correct product details Priority: 1 Test Coverage Item: T8 (Product Details Display) Preconditions: A ‘Product‘ instance is created with specific values Inputs: Launch ‘ProductDetails‘ with the sample product Expected Results: Product details such as ID, name, stock anterior, and stock actual are displayed correctly on the screen Postconditions: Verify that all product details are correctly displayed

Table 6.32: Test case for displaying product details in ProductDetails screen

Test Case ID: TCPD2 Purpose: Verify that the initial stock value is set correctly in the TextField on the ProductDetails screen Priority: 2 Test Coverage Item: T8 (Initial Stock Value Display) Preconditions: A ‘Product‘ instance is created with specific stock values Inputs: Launch ‘ProductDetails‘ with the sample product Expected Results: The TextField for stock actual shows the correct initial value Postconditions: Verify that the TextField contains the correct initial stock value

Table 6.33: Test case for initial stock value display in ProductDetails screen

95

Product List Tests

Test Case ID: TCPL1 Purpose: Verify that the product list is correctly filtered by state (Checked / Unchecked) Priority: 1 Test Coverage Item: T9 (Product List Filtering) Preconditions: List of products with mixed states (Checked / Unchecked) Inputs: Select ”Checked” from the dropdown filter, then select ”Unchecked” Expected Results: Only products with the selected state are displayed in the list Postconditions: Verify that the product list shows only checked products when filtered by ”Checked” and only unchecked products when filtered by ”Unchecked”

Table 6.34: Test case for filtering product list by state in ProductsList screen

Test Case ID: TCPL2 Purpose: Verify that tapping on a product in the list navigates to the ProductDetails screen Priority: 2 Test Coverage Item: T9 (Product List Navigation) Preconditions: List of products displayed Inputs: Tap on a product in the list Expected Results: ProductDetails screen is displayed for the tapped product Postconditions: Verify that the ProductDetails screen is shown with the correct product details

Table 6.35: Test case for navigating to ProductDetails from product list in ProductsList screen

96

Test Case ID: TCPL3 Purpose: Verify that tapping on the floating action button navigates to the QR scanner Priority: 2 Test Coverage Item: T9 (QR Scanner Navigation) Preconditions: ProductsList screen displayed Inputs: Tap on the floating action button Expected Results: QRScannerWidget screen is displayed Postconditions: Verify that the QRScannerWidget is shown

Table 6.36: Test case for navigating to QR scanner from ProductsList screen

97

Product Tests

Test Case ID: TCPR1 Purpose: Verify that a Product instance is initialized with the correct values Priority: 1 Test Coverage Item: T10 (Product Initialization) Preconditions: N/A Inputs: Initialize a ‘Product‘ instance with specific values Expected Results: Product instance is created with the correct ID, name, stock- Anterior, stockActual, and state Postconditions: Verify that all properties of the Product instance match the expected values

Table 6.37: Test case for Product initialization

Test Case ID: TCPR2 Purpose: Verify that a Product instance is correctly serialized to JSON Priority: 2 Test Coverage Item: T10 (Product JSON Serialization) Preconditions: A ‘Product‘ instance is created Inputs: Convert the Product instance to JSON using ‘toJson()‘ method Expected Results: JSON object is created with the correct values from the Product instance Postconditions: Verify that the JSON object contains the correct values for each key

Table 6.38: Test case for Product JSON serialization

98

Test Case ID: TCPR3 Purpose: Verify that JSON data is correctly deserialized into a Product instance Priority: 2 Test Coverage Item: T10 (Product JSON Deserialization) Preconditions: Mock JSON data representing a ‘Product‘ Inputs: Deserialize the JSON data to a ‘Product‘ instance using ‘fromJson()‘ method Expected Results: Product instance is created with values matching the JSON data Postconditions: Verify that the Product instance contains the correct values as per the JSON data

Table 6.39: Test case for Product JSON deserialization

99

Qr Widget Tests

Test Case ID: TCQR1 Purpose: Verify that the QRScannerWidget detects a barcode and navigates to the correct ProductDetails screen Priority: 1 Test Coverage Item: T11 (Barcode Detection and Navigation) Preconditions: ‘QRScannerWidget‘ displayed, product with ID ’12345’ exists in ‘globalProducts‘ Inputs: Simulate barcode detection with ID ’12345’ Expected Results: Navigates to ‘ProductDetails‘ screen for the product with ID ’12345’ Postconditions: Verify that the ‘ProductDetails‘ screen is displayed with the correct product details

Table 6.40: Test case for barcode detection in QRScannerWidget

Test Case ID: TCQR2 Purpose: Verify that an error message is displayed when a scanned barcode is not found Priority: 2 Test Coverage Item: T11 (Barcode Not Found Handling) Preconditions: ‘QRScannerWidget‘ displayed, no product with ID ’67890’ in ‘globalProducts‘ Inputs: Simulate barcode detection with ID ’67890’ Expected Results: An ‘AlertDialog‘ is shown with the message ”Producto no encontrado” Postconditions: Verify that the ‘AlertDialog‘ is displayed with the correct error message

Table 6.41: Test case for handling barcode not found in QRScannerWidget

100

Test Case ID: TCQR3 Purpose: Verify that the camera switches correctly when the switch button is tapped in QRScannerWidget Priority: 2 Test Coverage Item: T11 (Camera Switching) Preconditions: ‘QRScannerWidget‘ displayed Inputs: Tap the camera switch button Expected Results: The camera is switched to the other camera Postconditions: Verify that the camera controller state changes after tapping the button

Table 6.42: Test case for camera switching in QRScannerWidget

101

Report Tests

Test Case ID: TCRS1 Purpose: Verify that the ReportScreen displays the correct number of checked and unchecked products Priority: 1 Test Coverage Item: T12 (Product Count Display) Preconditions: ‘globalProducts‘ list with both checked and unchecked products Inputs: Launch ‘ReportScreen‘ Expected Results: The number of checked and unchecked products are displayed correctly on the screen Postconditions: Verify that the text ”Productos checkeados” and ”Productos no-checkeados” is displayed with the correct count of products

Table 6.43: Test case for displaying product counts in ReportScreen

Test Case ID: TCRS2 Purpose: Verify that the ReportScreen allows editing of observations and displays the updated value correctly Priority: 2 Test Coverage Item: T12 (Observation Editing) Preconditions: ‘ReportScreen‘ displayed with an initial observation in ‘globalObservations‘ Inputs: Enter new text in the observation ‘TextFormField‘ Expected Results: The ‘globalObservations‘ variable is updated with the new value Postconditions: Verify that ‘globalObservations‘ reflects the updated observation text

Table 6.44: Test case for editing and displaying observations in ReportScreen

102

6. 2.2 Acceptance Testing

Test Case ID: TCSHP1 Purpose: Verify that SaleSptosPage displays correctly Priority: 1 Test Coverage Item: T13 (SaleSpotsPage Display) Preconditions: The app is launched Inputs: Launch SaleSptosPage Expected Results: SaleSptosPage is displayed Postconditions: Verify that the text ”Hola! Andr´es Cornejo” and a GridView are visible

Table 6.45: Test case for verifying SaleSptosPage display

Test Case ID: TCSHP2 Purpose: Verify navigation to Home screen when ”Ceibos” is selected Priority: 1 Test Coverage Item: T13 (Navigation to Home from SaleSpotsPage) Preconditions: SaleSptosPage is displayed Inputs: Tap on ”Ceibos” Expected Results: Home screen is displayed Postconditions: Verify that Home screen is displayed

Table 6.46: Test case for navigation to Home screen from SaleSptosPage

Test Case ID: TCSHP3 Purpose: Verify navigation to Inventory Creation screen Priority: 1 Test Coverage Item: T13 (Navigation to Inventory Creation) Preconditions: Home screen is displayed Inputs: Tap on ”Crear Inventario” Expected Results: Inventory creation screen is displayed Postconditions: Verify that ”Lista de productos” is displayed

Table 6.47: Test case for navigation to Inventory Creation screen

103

Test Case ID: TCSHP4 Purpose: Verify filter selection and display of filtered products Priority: 2 Test Coverage Item: T13 (Filter Selection in Inventory Creation) Preconditions: Inventory creation screen is displayed Inputs: Select ”Todos” filter Expected Results: Filter ”Todos” is selected Postconditions: Verify that ”Todos” filter is correctly applied

Table 6.48: Test case for filter selection in Inventory Creation screen

Test Case ID: TCSHP5 Purpose: Verify stock update for a product Priority: 1 Test Coverage Item: T13 (Stock Update in Inventory Creation) Preconditions: ”Todos” filter is selected in Inventory creation screen Inputs: Tap on ”(Ps5)Fifa 23”, update stock to 2, confirm Expected Results: Product stock is updated to 2 Postconditions: Verify that stock is updated to 2

Table 6.49: Test case for verifying stock update in Inventory Creation screen

Test Case ID: TCSHP6 Purpose: Verify inventory details and manager name update Priority: 2 Test Coverage Item: T13 (Manager Name Update in Inventory Details) Preconditions: Inventory details screen is displayed Inputs: Change manager name to ”Juan P´erez” Expected Results: Manager name is updated to ”Juan P´erez” Postconditions: Verify that the name ”Juan P´erez” is displayed

Table 6.50: Test case for verifying manager name update in Inventory Details screen

104

Test Case ID: TCSHP7 Purpose: Verify draft save functionality Priority: 1 Test Coverage Item: T13 (Draft Saving in Inventory Details) Preconditions: Inventory details screen is displayed with updated manager name Inputs: Tap on ”Guardar borrador” Expected Results: Draft is saved Postconditions: Verify that confirmation message ”¡Borrador guardado exitosamente!” is displayed

Table 6.51: Test case for verifying draft save functionality in Inventory Details screen

105

Flow of Acceptance Testing

Acceptance testing in Flutter is based on executing a series of steps automatically (the application runs on its own) according to the established instructions to validate that the application meets the requirements and works correctly from the perspective of the end user, covering complete flows of the application. The flow of the integration tests of the mobile module is as follows:

Figure 6.2: Click on the ’Ceibos’ Local.

106

Figure 6.3: Click on the ’Crear Inventario’ Button.

107

Figure 6.4: Click on the ’Seleccionar Filtro’ option.

108

Figure 6.5: Click on the ’Todos’ option.

109

Figure 6.6: Click on the ’Fifa 23’ product.

110

Figure 6.7: Click on the ’Stock Actual’ field.

111

Figure 6.8: Put ’2’ in ’Stock Actual’ field.

112

Figure 6.9: Click on the ’Confirmar’ button.

113

Figure 6.10: Click on the ’Detalles’ tab.

114

Figure 6.11: Write employee name ’Juan P´erez’.

115

Figure 6.12: Click on the ’Guardar Borrador’ button.

116

### 6.3 Test data requirements

For the testing of this application, a modified set of live data will be used. This data will include the necessary elements to perform comprehensive testing, ensuring that the application’s functionality is thoroughly validated. However, the data set must be carefully managed to exclude any critical customer information. To maintain the integrity and security of the testing process, all personal data will be obfuscated or scrambled before it is loaded into the testing environment.

Resetting the data after each test cycle is not required unless specified, and at the end of the testing phase, data will either be archived or disposed of according to the guidelines provided. The focus will be on ensuring that the test environment closely mirrors the production environment without compromising customer privacy.

### 6.4 Test environment requirements

The test environment for this project will be set up to closely mimic the production environment, ensuring that all functionalities are tested under conditions that closely resemble those that will be encountered by end-users. The environment will consist of a scalable cloud-based infrastructure that allows for automated scaling to handle varying loads during performance testing.

Configuration testing on this environment is limited, as it is intended to simulate the most common deployment configurations. However, edge cases involving different configurations will be handled in a separate test environment. Regular backups and environment resets will be scheduled to maintain consistency and allow for reliable test repetitions.

### 6.5 Test result

The following are the specific test results of customer-facing tests. The following documentation follows the structure: Number Test / Result of the Test/ Directory of the test / Description of the test

- Test 1: Passed (/home/runner/work/NintventarioApp-beta/NintventarioApp-beta/test/sale -

spots test.dart: Verify greeting text)

- Test 2: Passed (/home/runner/work/NintventarioApp-beta/NintventarioApp-beta/test/sale -

spots test.dart: Verify instruction text)

- Test 3: Passed (/home/runner/work/NintventarioApp-beta/NintventarioApp-beta/test/sale -

spots test.dart: Verify BottomAppBar elements)

117

- Test 4: Passed (/home/runner/work/NintventarioApp-beta/NintventarioApp-beta/test/qr -

scanner widget test.dart: QRScannerWidget Tests Barcode Detection)

- Test 5: Passed (/home/runner/work/NintventarioApp-beta/NintventarioApp-beta/test/qr -

scanner widget test.dart: QRScannerWidget Tests Barcode Not Found)

- Test 6: Passed (/home/runner/work/NintventarioApp-beta/NintventarioApp-beta/test/qr -

scanner widget test.dart: QRScannerWidget Tests Camera Switching)

- Test 7: Passed (/home/runner/work/NintventarioApp-beta/NintventarioApp-beta/test/details -

test.dart: InventoryDetails Widget Tests InventoryDetails displays correctly)

- Test 8: Passed (/home/runner/work/NintventarioApp-beta/NintventarioApp-beta/test/history -

test.dart: DraftsScreen should display a loading indicator while loading drafts)

- Test 9: Passed (/home/runner/work/NintventarioApp-beta/NintventarioApp-beta/test/history -

test.dart: DraftsScreen should display ”No drafts available” when no drafts exist)

- Test 10: Passed (/home/runner/work/NintventarioApp-beta/NintventarioApp-

beta/test/details test.dart: InventoryDetails Widget Tests InventoryDetails allows saving a draft)

- Test 11: Passed (/home/runner/work/NintventarioApp-beta/NintventarioApp-

beta/test/history test.dart: DraftsScreen should display a list of drafts)

- Test 12: Passed (/home/runner/work/NintventarioApp-beta/NintventarioApp-

beta/test/product test.dart: Product Class Tests Product Initialization)

- Test 13: Passed (/home/runner/work/NintventarioApp-beta/NintventarioApp-

beta/test/product test.dart: Product Class Tests JSON Serialization)

- Test 14: Passed (/home/runner/work/NintventarioApp-beta/NintventarioApp-

beta/test/product test.dart: Product Class Tests JSON Deserialization)

- Test 15: Passed (/home/runner/work/NintventarioApp-beta/NintventarioApp-

beta/test/draft test.dart: Draft should have default values when not provided)

- Test 16: Passed (/home/runner/work/NintventarioApp-beta/NintventarioApp-

beta/test/tab widget test.dart: CustomTabBar Widget Tests Widget Initialization Test)

- Test 17: Passed (/home/runner/work/NintventarioApp-beta/NintventarioApp-

beta/test/draft test.dart: Draft should correctly convert to JSON)

- Test 18: Passed (/home/runner/work/NintventarioApp-beta/NintventarioApp-

beta/test/draft test.dart: Draft should save and load correctly from SharedPreferences)

118

- Test 19: Passed (/home/runner/work/NintventarioApp-beta/NintventarioApp-

beta/test/draft test.dart: Draft should update an existing draft in SharedPreferences)

- Test 20: Passed (/home/runner/work/NintventarioApp-beta/NintventarioApp-

beta/test/tab widget test.dart: CustomTabBar Widget Tests Error State Test)

- Test 21: Passed (/home/runner/work/NintventarioApp-beta/NintventarioApp-

beta/test/tab widget test.dart: CustomTabBar Widget Tests No Products Found Test)

- Test 22: Passed (/home/runner/work/NintventarioApp-beta/NintventarioApp-

beta/test/tab widget test.dart: CustomTabBar Widget Tests Tab Selection Test)

- Test 23: Passed (/home/runner/work/NintventarioApp-beta/NintventarioApp-

beta/test/tab widget test.dart: CustomTabBar Widget Tests Tab Bar Labels Test)

- Test 24: Passed (/home/runner/work/NintventarioApp-beta/NintventarioApp-

beta/test/tab widget test.dart: CustomTabBar Widget Tests Tab Bar Icons Test)

- Test 25: Passed (/home/runner/work/NintventarioApp-beta/NintventarioApp-

beta/test/tab widget test.dart: CustomTabBar Widget Tests Page View Test)

- Test 26: Passed (/home/runner/work/NintventarioApp-beta/NintventarioApp-

beta/test/tab widget test.dart: CustomTabBar Widget Tests Tab Bar Tap Animation Test)

- Test 27: Passed (/home/runner/work/NintventarioApp-beta/NintventarioApp-

beta/test/product details test.dart: Displays correct product details)

- Test 28: Passed (/home/runner/work/NintventarioApp-beta/NintventarioApp-

beta/test/product details test.dart: Initial stock value is set correctly)

- Test 29: Passed (/home/runner/work/NintventarioApp-beta/NintventarioApp-

beta/test/date selector widget test.dart: DateSelectorWidget displays initial selected date)

- Test 30: Passed (/home/runner/work/NintventarioApp-beta/NintventarioApp-

beta/test/date selector widget test.dart: DateSelectorWidget opens date picker on tap)

- Test 31: Passed (/home/runner/work/NintventarioApp-beta/NintventarioApp-

beta/test/date selector widget test.dart: DateSelectorWidget calls onDateSelected with the picked date)

- Test 32: Passed (/home/runner/work/NintventarioApp-beta/NintventarioApp-

beta/test/home test.dart: Verify AppBar title)

119

- Test 33: Passed (/home/runner/work/NintventarioApp-beta/NintventarioApp-

beta/test/home test.dart: Verify menu items)

- Test 34: Passed (/home/runner/work/NintventarioApp-beta/NintventarioApp-

beta/test/product list test.dart: Filters product list by state)

- Test 35: Passed (/home/runner/work/NintventarioApp-beta/NintventarioApp-

beta/test/report test.dart: Report Screen should display correct number of checked and unchecked products)

- Test 36: Passed (/home/runner/work/NintventarioApp-beta/NintventarioApp-

beta/test/product list test.dart: Navigates to ProductDetails on product tap)

- Test 37: Passed (/home/runner/work/NintventarioApp-beta/NintventarioApp-

beta/test/report test.dart: Report Screen should allow observation editing and display updated value)

- Test 38: Passed (/home/runner/work/NintventarioApp-beta/NintventarioApp-

beta/test/product list test.dart: Floating action button navigates to QR scanner)

120

Results of test execution for Home Screen

Figure 6.13: Results of static testing mobile.

Results of test execution for TabBar Screen

Figure 6.14: Results of testing TabBar Screen.

Results of test execution for DateSelector

121

Figure 6.15: Results of testing DateSelector Widget.

Results of test execution for Inventory Details

Figure 6.16: Results of testing Inventory Detail Screen.

Results of test execution for SaleSpot

Figure 6.17: Results of testing SaleSpot Screen.

Results of test execution for Draft class

122

Figure 6.18: Results of testing Draft Screen.

Results of test execution for History screen

Figure 6.19: Results of testing History Screen.

Results of test execution for Product Details

Figure 6.20: Results of testing Product Details Screen.

Results of test execution for Product List

123

Figure 6.21: Results of testing Product List Screen.

Results of test execution for Product class

Figure 6.22: Results of testing Product Class.

Results of test execution for QR widget

Figure 6.23: Results of testing qr widget.

Results of test execution for Report Screen

124

Figure 6.24: Results of testing Report Screen.

### 6.6 Incident report

Number 1 Short Title InventoryDetails Widget Test Failure System NintventarioApp - Inventory Details Module System Version Beta Test ID TCINV1 Test Environment /home/runner/work/NintventarioApp-beta/NintventarioAppbeta/test/ Status Open Created by Angel Tomal´a Date & time: 01/08/2024 11:30 Observed by Angel Tomal´a Date & time: 01/08/2024 11:40 Details The test failed because the expected TextField widget with text ”0” was not found in the InventoryDetails widget. The test expected exactly one matching candidate but found none. Observed during Widget Testing

Severity High Priority 1 Risk The failure indicates a potential issue with the UI rendering or widget hierarchy in the InventoryDetails module, which could lead to a poor user experience or functional issues in production. Immediate investigation and resolution are recommended.

Table 6.52: Details of the InventoryDetails Widget Test Failure.

125

Number 2 Short Title Report Screen Test Failure System NintventarioApp - Report Module System Version Beta Test ID TCRS1 Test Environment /home/runner/work/NintventarioApp-beta/NintventarioAppbeta/test/ Status Open Created by Andr´es Cornejo Date & time: 01/08/2024 11:30 Observed by Andr´es Cornejo Date & time: 01/08/2024 11:40 Details The test failed because the expected text ”Productos no-checkeados:” was not found on the Report Screen. The test expected exactly one matching candidate but found none. Observed during Widget Testing

Severity Medium Priority 2 Risk The failure indicates a potential issue with the text rendering or widget hierarchy in the Report Screen, which could lead to inaccurate reporting or user confusion. Immediate investigation and resolution are recommended.

Table 6.53: Details of the Report Screen Test Failure.

The test management tool provides detailed records of test case execution, including timestamps, outcomes, and any issues encountered during testing. This tool is integrated with the automation framework, which automatically logs the results of each test run, including both passed and failed cases, and captures logs for further analysis.

126

# 7 Web Module Test Documentation

### 7.1 Test plan

Test Plan for:

Nintventario E-commerce Website

Context, test items scope:

This document outlines the test plan and strategies for the web module of the Ninventario project, developed using the Scrum framework. The scope of testing covers user interface (UI), functionality, performance and compatibility. Key test items include product browsing, search, user registration, shopping cart operations, payment processing, and order management, all of which will be tested iteratively during each sprint.

Team Communication:

The test team includes developers, and the Scrum Master, with the Product Owner providing ongoing input. Daily stand-ups, sprint planning, and sprint retrospectives will be used for communication and coordination.

Stakeholders:

Stakeholders include the Product Owner, Scrum Master and Development Team. The Product Owner ensures the e-commerce website aligns with business goals and provides feedback throughout each sprint. The Scrum Master facilitates the process, removing obstacles.

Risk Analysis:

ID Feature Risk Probability (1-10) Impact (1-10) Risk Number Mitigation Activities

127

R1 User Registration/Login

Users may be unable to register or log in due to validation errors or authentication failures.

7 8 56 Functional tests: Verify registration and login processes, including form validation and error handling. R2 Product Display Products may not display correctly, leading to missing or incorrect information.

6 8 48 UI tests: Ensure that all product details are correctly rendered on the frontend. R3 Wishlist Management

Users might lose wishlist items due to session expiration or incorrect database handling.

5 7 35 Functional tests: Verify that wishlist items are correctly added, removed, and persisted across sessions. R4 Shopping Cart Users may experience issues adding/removing products, or cart contents might not persist across sessions.

6 7 42 Functional tests: Verify correct shopping cart operations and persistence.

R5 Payment Processing Payments might fail due to errors in the PayPal integration or network issues.

5 9 45 Integration tests: Verify successful payment transactions and proper handling of failures. R6 Product Search The search functionality may return incorrect or no results due to indexing issues.

5 6 30 Functional tests: Validate the accuracy and relevance of search results.

128

R7 User Profile Management

Users may not be able to update their profiles due to form validation errors or backend issues.

3 8 24 Functional tests: Verify that users can update profile information correctly.

R8 Order Management Orders might not be processed correctly, leading to incorrect order statuses or missing orders.

6 9 54 Functional tests: Validate order creation, status updates, and tracking.

R9 Checkout Process Users may abandon purchases if the checkout process is too complicated or slow.

5 8 35 Usability tests: Ensure that the checkout process is smooth and intuitive. R10 Session Management

Users may be logged out unexpectedly due to session handling errors, leading to loss of cart contents or other data.

8 9 73 Security and functional tests: Verify session handling and data persistence across sessions.

R11 Data Security Sensitive user data may be exposed due to insecure data transmission or storage.

4 9 36 Security tests: Ensure that all data is encrypted and securely transmitted/stored. R12 API Rate Limiting High traffic might cause the API to throttle or deny requests, affecting user experience.

4 6 24 Load tests: Test the API under high traffic conditions to ensure proper rate limiting and response.

129

R13 Cross- Browser Compatibility

The application may not function consistently across different web browsers.

5 5 25 Cross-browser tests: Verify application performance across multiple browsers (e.g., Chrome, Firefox, Safari). R14 Mobile Responsiveness

The website may not display or function correctly on mobile devices.

6 6 36 Responsive design tests: Validate that the website is fully functional on mobile devices. R15 Form Validation Forms may accept invalid input or fail to validate correctly, leading to errors in user data submission.

4 8 32 Input validation tests: Ensure that all forms enforce proper validation rules. R16 Email Notifications Users may not receive confirmation emails or other notifications due to errors in the email system.

4 4 16 Functional tests: Verify that email notifications are sent and received correctly.

R17 Content Management

Admins might face difficulties in updating content due to UI or backend issues.

4 7 28 Functional tests: Ensure that content management features work as expected. R18 Load Time Performance

Pages might load slowly, leading to poor user experience and higher bounce rates.

5 4 20 Performance tests: Measure page load times and optimize resources. R19 Authorization Issues Unauthorized users may gain access to restricted features or data.

7 9 63 Security tests: Verify that all features enforce proper authorization checks.

130

Table 7.1: Risk Analysis for Product Sales Website Project

Risk Prioritization

Figure 7.1: Risk Prioritization Matrix: High Impact and High Likelihood

Test Strategy:

- Continuous Testing: Integrated into each sprint, with Product Owner involved

from planning to review.

- Test Case Creation: Developed during sprint planning and executed within the

sprint.

- Manual Automated Testing: Both approaches used for comprehensive cover-

age.

131

- CI/CD Integration: Automated tests run in the CI/CD pipeline for quick feed-

back.

### 7.2 Test case specification

7. 2.1 Unit Test Cases: Frontend

The frontend, in charge of the user interface and interactive experience, has been evaluated through user interface tests, which validate that all visual elements are presented and function as expected, and usability tests that ensure that navigation is intuitive and accessible to all users. For testing Angular applications specifically, we utilize Jasmine, a robust testing framework that allows us to perform unit tests efficiently and effectively.

Testing for the Main Component: AppComponent

Test Case ID: TCMC1 Purpose: Verify that the app component is created successfully Priority: 1 Test Coverage Item: App Initialization Preconditions: Angular application is running Inputs: N/A Expected Results: The app component should be truthy Postconditions: N/A

Table 7.2: Test case to verify app component creation

Test Case ID: TCMC2 Purpose: Verify that the navbar component is rendered Priority: 2 Test Coverage Item: Navbar Rendering Preconditions: The app component is initialized Inputs: N/A Expected Results: Navbar component should be present in the DOM Postconditions: N/A

Table 7.3: Test case to verify navbar component rendering

132

Test Case ID: TCMC3 Purpose: Verify conditional rendering of mid-banner or banner component Priority: 3 Test Coverage Item: Banner Component Rendering Preconditions: The app component is initialized Inputs: Set ‘isIndexPage‘ to true or false Expected Results: When ‘isIndexPage‘ is true, the banner component should be rendered, otherwise, the mid-banner component should be rendered Postconditions: N/A

Table 7.4: Test case to verify conditional rendering of banner components

Test Case ID: TCMC4 Purpose: Verify that the footer component is rendered Priority: 2 Test Coverage Item: Footer Rendering Preconditions: The app component is initialized Inputs: N/A Expected Results: Footer component should be present in the DOM Postconditions: N/A

Table 7.5: Test case to verify footer component rendering

Testing of Shared Components

Test Case ID: TCSC1 Purpose: Verify that the ‘FooterComponent‘ is created successfully Priority: 1 Test Coverage Item: Footer Component Initialization Preconditions: The Angular application is running and ‘FooterComponent‘ is included in the module Inputs: N/A Expected Results: The ‘FooterComponent‘ should be truthy Postconditions: N/A

Table 7.6: Test case to verify the creation of ‘FooterComponent‘

133

Test Case ID: TCSC2 Purpose: Verify that social media links are present in ‘FooterComponent‘ Priority: 2 Test Coverage Item: Footer Social Media Links Preconditions: The ‘FooterComponent‘ is initialized Inputs: N/A Expected Results: Social media links should be present in the ‘.social-icons a‘ selector Postconditions: N/A

Table 7.7: Test case to verify social media links in ‘FooterComponent‘

Test Case ID: TCSC3 Purpose: Verify that the ‘BannerComponent‘ is created successfully Priority: 1 Test Coverage Item: Banner Component Initialization Preconditions: The Angular application is running and ‘BannerComponent‘ is included in the module Inputs: N/A Expected Results: The ‘BannerComponent‘ should be truthy Postconditions: N/A

Table 7.8: Test case to verify the creation of ‘BannerComponent‘

Testing of NavbarComponent

Test Case ID: TCNC1 Purpose: Verify that the ‘NavbarComponent‘ is created successfully Priority: 1 Test Coverage Item: Navbar Component Initialization Preconditions: The Angular application is running and ‘NavbarComponent‘ is included in the module Inputs: N/A Expected Results: The ‘NavbarComponent‘ should be truthy Postconditions: N/A

Table 7.9: Test case to verify the creation of ‘NavbarComponent‘

134

Test Case ID: TCNC2 Purpose: Verify that the menu visibility toggles when ‘toggleMenu‘ is called Priority: 2 Test Coverage Item: Navbar Menu Toggle Preconditions: The ‘NavbarComponent‘ is initialized Inputs: Call ‘toggleMenu‘ method Expected Results: The ‘menuVisible‘ property should toggle between ‘true‘ and ‘false‘ Postconditions: N/A

Table 7.10: Test case to verify menu visibility toggle in ‘NavbarComponent‘

Testing of AuthService

Test Case ID: TCAS1 Purpose: Verify that the ‘AuthService‘ is created successfully Priority: 1 Test Coverage Item: AuthService Initialization Preconditions: The Angular application is running Inputs: N/A Expected Results: The ‘AuthService‘ should be truthy Postconditions: N/A

Table 7.11: Test case to verify the creation of ‘AuthService‘

Test Case ID: TCAS2 Purpose: Verify that the ‘login‘ method successfully logs in the user Priority: 1 Test Coverage Item: User Login Preconditions: The ‘AuthService‘ is initialized Inputs: Email: test@example.com, password:securepassword Expected Results: The user should be successfully logged in, receiving a valid ‘LoginResponse‘, and the ‘isLoggedInSubject‘ should be ‘true‘ Postconditions: N/A

Table 7.12: Test case to verify user login in ‘AuthService‘

135

Test Case ID: TCAS3 Purpose: Verify that the ‘register‘ method successfully registers the user Priority: 2 Test Coverage Item: User Registration Preconditions: The ‘AuthService‘ is initialized Inputs: Email: test@example.com, password:securepassword, first name: Kevin, last name: Villa Expected Results: The user should be successfully registered, receiving a valid ‘LoginResponse‘ Postconditions: N/A

Table 7.13: Test case to verify user registration in ‘AuthService‘

Test Case ID: TCAS4 Purpose: Verify that the ‘logout‘ method logs out the user and resets the cart Priority: 1 Test Coverage Item: User Logout Preconditions: The user is logged in and has an active cart Inputs: N/A Expected Results: The user should be logged out, the ‘accessToken‘ should be removed from localStorage, and the cart should be reset Postconditions: N/A

Table 7.14: Test case to verify user logout in ‘AuthService‘

Test Case ID: TCAS5 Purpose: Verify that ‘checkLoginStatus‘ returns the correct login status based on localStorage Priority: 2 Test Coverage Item: Login Status Check Preconditions: The ‘AuthService‘ is initialized Inputs: N/A Expected Results: The method should return ‘true‘ if the user is logged in and ‘false‘ if not Postconditions: N/A

Table 7.15: Test case to verify login status check in ‘AuthService‘

136

Test Case ID: TCAS6 Purpose: Verify that ‘getUserInfo‘ retrieves user information correctly Priority: 3 Test Coverage Item: Retrieve User Information Preconditions: The user is logged in and has a valid ‘accessToken‘ Inputs: N/A Expected Results: The method should return the user’s information Postconditions: N/A

Table 7.16: Test case to verify retrieval of user information in ‘AuthService‘

Test Case ID: TCAS7 Purpose: Verify that the correct initial login status is emitted based on localStorage Priority: 3 Test Coverage Item: Initial Login Status Emission Preconditions: The ‘AuthService‘ is initialized Inputs: N/A Expected Results: The login status should be correctly emitted based on whether ‘accessToken‘ is present in localStorage Postconditions: N/A

Table 7.17: Test case to verify initial login status emission in ‘AuthService‘

Testing of CartService

Test Case ID: TCCS1 Purpose: Verify that the ‘CartService‘ is created successfully Priority: 1 Test Coverage Item: CartService Initialization Preconditions: The Angular application is running Inputs: N/A Expected Results: The ‘CartService‘ should be truthy Postconditions: N/A

Table 7.18: Test case to verify the creation of ‘CartService‘

137

Test Case ID: TCCS2 Purpose: Verify that a new item is added to the cart Priority: 1 Test Coverage Item: Add to Cart Preconditions: The ‘CartService‘ is initialized Inputs: A ‘CartItem‘ object Expected Results: The item should be added to the ‘cartItems‘ array, and localStorage should be updated Postconditions: The cart should contain the new item

Table 7.19: Test case to verify adding a new item to the cart in ‘CartService‘

Test Case ID: TCCS3 Purpose: Verify that the quantity of an existing item in the cart is updated Priority: 2 Test Coverage Item: Update Item Quantity Preconditions: The item already exists in the cart Inputs: A ‘CartItem‘ object with the same ID as an existing item: 2 Expected Results: The quantity of the existing item should be updated, and localStorage should be updated Postconditions: The cart should reflect the updated quantity

Table 7.20: Test case to verify updating the quantity of an existing item in ‘CartService‘

Test Case ID: TCCS4 Purpose: Verify that an item is removed from the cart Priority: 1 Test Coverage Item: Remove from Cart Preconditions: The item exists in the cart Inputs: The ID of the item to remove: 1 Expected Results: The item should be removed from the ‘cartItems‘ array, and localStorage should be updated Postconditions: The cart should no longer contain the removed item

Table 7.21: Test case to verify removing an item from the cart in ‘CartService‘

138

Test Case ID: TCCS5 Purpose: Verify that the cart is reset Priority: 2 Test Coverage Item: Reset Cart Preconditions: The cart contains items Inputs: N/A Expected Results: The ‘cartItems‘ array should be empty, and localStorage should be updated accordingly Postconditions: The cart should be empty

Table 7.22: Test case to verify resetting the cart in ‘CartService‘

Test Case ID: TCCS6 Purpose: Verify that the total number of products in the cart is updated Priority: 2 Test Coverage Item: Update Total Products Preconditions: The cart contains items Inputs: A ‘CartItem‘ object with a specific quantity: cartquantity:23 Expected Results: The total number of products in the cart should reflect the sum of quantities of all items Postconditions: The total products count should be accurate

Table 7.23: Test case to verify updating the total number of products in the cart in ‘CartService‘

Testing of ContactService

Test Case ID: TCConS1 Purpose: Verify that the ‘ContactService‘ is created successfully Priority: 1 Test Coverage Item: Service Initialization Preconditions: Angular testing module is configured with ‘HttpClientTestingModule‘ and ‘ContactService‘ Inputs: N/A Expected Results: The ‘ContactService‘ instance should be truthy Postconditions: N/A

Table 7.24: Test case to verify ‘ContactService‘ creation

139

Test Case ID: TCConS2 Purpose: Verify that the contact email is sent successfully Priority: 2 Test Coverage Item: Email Sending Functionality Preconditions: The ‘ContactService‘ is initialized and the ‘HttpClientTestingModule‘ is injected Inputs: Mock contact data: {name: ’John Doe’, email: ’john.doe@example.com’, message: ’Hello!’} Expected Results: The contact email should be sent with a POST request to the correct URL, and the request body should match the mock data Postconditions: Ensure no outstanding HTTP requests remain

Table 7.25: Test case to verify contact email sending

Test Case ID: TCConS3 Purpose: Verify that the register email is sent successfully Priority: 2 Test Coverage Item: Email Sending Functionality Preconditions: The ‘ContactService‘ is initialized and the ‘HttpClientTestingModule‘ is injected Inputs: Mock register data: {name: ’Jane Doe’, email: ’jane.doe@example.com’} Expected Results: The register email should be sent with a POST request to the correct URL, and the request body should match the mock data Postconditions: Ensure no outstanding HTTP requests remain

Table 7.26: Test case to verify register email sending

140

Testing of ProductService

Test Case ID: TCPS1 Purpose: Verify that the ‘ProductService‘ is created successfully Priority: 1 Test Coverage Item: Service Initialization Preconditions: Angular testing module is configured with ‘HttpClientTestingModule‘ and ‘ProductService‘ Inputs: N/A Expected Results: The ‘ProductService‘ instance should be truthy Postconditions: N/A

Table 7.27: Test case to verify ‘ProductService‘ creation

Test Case ID: TCPS2 Purpose: Verify that all products are retrieved from the API via GET Priority: 2 Test Coverage Item: Product Retrieval Preconditions: The ‘ProductService‘ is initialized and the ‘HttpClientTestingModule‘ is injected. Inputs: N/A Expected Results: A GET request is sent to the correct URL, and the response should match the mock products data. Postconditions: Ensure no outstanding HTTP requests remain.

Table 7.28: Test case to verify retrieval of all products

Test Case ID: TCPS3 Purpose: Verify that filtered products are retrieved from the API via GET Priority: 2 Test Coverage Item: Filtered Product Retrieval Preconditions: The ‘ProductService‘ is initialized and the ‘HttpClientTestingModule‘ is injected. Inputs: Price range: 100-200, Product type: ’type’ Expected Results: A GET request is sent to the correct URL with the correct query parameters, and the response should match the mock filtered products data. Postconditions: Ensure no outstanding HTTP requests remain.

Table 7.29: Test case to verify retrieval of filtered products

141

Test Case ID: TCPS4 Purpose: Verify that the newest products are retrieved from the API via GET Priority: 2 Test Coverage Item: Newest Product Retrieval Preconditions: The ‘ProductService‘ is initialized and the ‘HttpClientTestingModule‘ is injected. Inputs: N/A Expected Results: A GET request is sent to the correct URL, and the response should match the mock newest products data. Postconditions: Ensure no outstanding HTTP requests remain.

Table 7.30: Test case to verify retrieval of newest products

Test Case ID: TCPS5 Purpose: Verify that the bestselling products are retrieved from the API via GET Priority: 2 Test Coverage Item: Bestselling Product Retrieval Preconditions: The ‘ProductService‘ is initialized and the ‘HttpClientTestingModule‘ is injected. Inputs: N/A Expected Results: A GET request is sent to the correct URL, and the response should match the mock bestselling products data. Postconditions: Ensure no outstanding HTTP requests remain.

Table 7.31: Test case to verify retrieval of bestselling products

Testing of OrderService

Test Case ID: TCOS1 Purpose: Verify that the ‘OrderService‘ is created successfully Priority: 1 Test Coverage Item: Service Initialization Preconditions: Angular testing module is configured with ‘HttpClientTestingModule‘ and ‘OrderService‘ Inputs: N/A Expected Results: The ‘OrderService‘ instance should be truthy Postconditions: N/A

Table 7.32: Test case to verify ‘OrderService‘ creation

142

Test Case ID: TCOS2 Purpose: Verify that a new order is created successfully Priority: 2 Test Coverage Item: Order Creation Functionality Preconditions: The ‘OrderService‘ is initialized and the ‘HttpClientTestingModule‘ is injected. A valid access token is stored in ‘localStorage‘. Inputs: Mock order data: {client: 1, total: 100, status: ’pending’, items: [{product: 1, quantity: 2}]} Expected Results: A POST request is sent to the correct URL with the correct request body and headers. The response should match the mock order response data. Postconditions: Ensure no outstanding HTTP requests remain. Local storage is cleared.

Table 7.33: Test case to verify order creation

Test Case ID: TCOS3 Purpose: Verify that the purchase history is retrieved successfully Priority: 2 Test Coverage Item: Purchase History Retrieval Preconditions: The ‘OrderService‘ is initialized and the ‘HttpClientTestingModule‘ is injected. A valid access token is stored in ‘localStorage‘. Inputs: N/A Expected Results: A GET request is sent to the correct URL with the correct headers. The response should match the mock purchase history data. Postconditions: Ensure no outstanding HTTP requests remain. Local storage is cleared.

Table 7.34: Test case to verify purchase history retrieval

143

Testing of PaymentService

Test Case ID: TCPayS1 Purpose: Verify that the ‘PaymentService‘ is created successfully Priority: 1 Test Coverage Item: Service Initialization Preconditions: Angular testing module is configured with ‘HttpClientTestingModule‘ and ‘PaymentService‘ Inputs: N/A Expected Results: The ‘PaymentService‘ instance should be truthy Postconditions: N/A

Table 7.35: Test case to verify ‘PaymentService‘ creation

Test Case ID: TCPayS2 Purpose: Verify that a new PayPal order is created successfully Priority: 2 Test Coverage Item: PayPal Order Creation Preconditions: The ‘PaymentService‘ is initialized and the ‘HttpClientTestingModule‘ is injected. Inputs: Mock cart item data: {id: 1, name: ’Product 1’, price: 100, maxQuantity: 10, quantityToBuy: 1, details: ’Details of product 1’, image: ’image1.jpg’} Expected Results: A POST request is sent to the correct URL with the correct request body. The response should match the mock PayPal order data. Postconditions: Ensure no outstanding HTTP requests remain.

Table 7.36: Test case to verify PayPal order creation

144

Test Case ID: TCPayS3 Purpose: Verify that a PayPal order is captured successfully Priority: 2 Test Coverage Item: PayPal Order Capture Preconditions: The ‘PaymentService‘ is initialized and the ‘HttpClientTestingModule‘ is injected. A valid order ID is available. Inputs: Order ID: ’ORDER-ID’ Expected Results: A POST request is sent to the correct URL with the correct order ID. The response should match the mock PayPal capture response data. Postconditions: Ensure no outstanding HTTP requests remain.

Table 7.37: Test case to verify PayPal order capture

Testing of WishlistService

Test Case ID: TCWS1 Purpose: Verify that the ‘WishlistService‘ is created successfully Priority: 1 Test Coverage Item: Service Initialization Preconditions: Angular testing module is configured with ‘HttpClientTestingModule‘ and ‘WishlistService‘ Inputs: N/A Expected Results: The ‘WishlistService‘ instance should be truthy Postconditions: N/A

Table 7.38: Test case to verify ‘WishlistService‘ creation

Test Case ID: TCWS2 Purpose: Verify that the wishlist items are fetched successfully from the API Priority: 2 Test Coverage Item: Wishlist Retrieval Preconditions: The ‘WishlistService‘ is initialized and the ‘HttpClientTestingModule‘ is injected. Inputs: N/A Expected Results: A GET request is sent to the correct URL, and the response should match the mock wishlist data. The length of the items array should be 1. Postconditions: Ensure no outstanding HTTP requests remain.

Table 7.39: Test case to verify wishlist item retrieval

145

Testing of ContactComponent

Test Case ID: TCCC1 Purpose: Verify that the ‘ContactComponent‘ is created successfully Priority: 1 Test Coverage Item: Component Initialization Preconditions: Angular testing module is configured with ‘FormsModule‘, ‘ContactComponent‘, and ‘HttpClientTestingModule‘ Inputs: N/A Expected Results: The ‘ContactComponent‘ instance should be truthy Postconditions: N/A

Table 7.40: Test case to verify ‘ContactComponent‘ creation

Test Case ID: TCCC2 Purpose: Verify that the form within ‘ContactComponent‘ is submitted correctly Priority: 2 Test Coverage Item: Form Submission Preconditions: The ‘ContactComponent‘ is initialized, and the form is present in the DOM Inputs: User interaction: click on the submit button Expected Results: The ‘onSubmit‘ method of the component should be called when the form is submitted Postconditions: N/A

Table 7.41: Test case to verify form submission in ‘ContactComponent‘

146

Testing of EmailChangeComponent

Test Case ID: TCECC1 Purpose: Verify that the ‘EmailChangeConfirmationComponent‘ is created successfully Priority: 1 Test Coverage Item: Component Initialization Preconditions: Angular testing module is configured with ‘FormsModule‘, ‘CommonModule‘, and necessary services mocked Inputs: N/A Expected Results: The ‘EmailChangeConfirmationComponent‘ instance should be truthy Postconditions: N/A

Table 7.42: Test case to verify ‘EmailChangeConfirmationComponent‘ creation

Test Case ID: TCECC2 Purpose: Verify that the alert properties are initialized correctly if an alert is active Priority: 2 Test Coverage Item: Alert Initialization Preconditions: The ‘EmailChangeConfirmationComponent‘ is initialized, and ‘AlertService‘ mock has ‘showAlert‘ set to true with predefined values Inputs: Mock Alert Data: {showAlert: true, alertTopic: ’Test Topic’, alertMessage: ’Test Message’, alertType: ’confirm’} Expected Results: The component’s alert properties should match the values from ‘AlertService‘, and ‘clearAlert‘ should be called Postconditions: N/A

Table 7.43: Test case to verify alert initialization in ‘EmailChangeConfirmationComponent‘

147

Test Case ID: TCECC3 Purpose: Verify that the component navigates to the login page when ‘navigateToLogin‘ is called Priority: 2 Test Coverage Item: Navigation Preconditions: The ‘EmailChangeConfirmationComponent‘ is initialized, and the ‘Router‘ service is mocked Inputs: Method call: ‘component.navigateToLogin()‘ Expected Results: The ‘Router.navigateByUrl‘ method should be called with the argument ‘’/login’‘ Postconditions: N/A

Table 7.44: Test case to verify navigation to login in ‘EmailChangeConfirmationComponent‘

Testing of IndexComponent

Test Case ID: TCIC1 Purpose: Verify that the ‘IndexComponent‘ is created successfully Priority: 1 Test Coverage Item: Component Initialization Preconditions: Angular testing module is configured with ‘FormsModule‘, ‘HttpClientTestingModule‘, y el componente ‘IndexComponent‘ Inputs: N/A Expected Results: The ‘IndexComponent‘ instance should be truthy Postconditions: N/A

Table 7.45: Test case to verify ‘IndexComponent‘ creation

148

Test Case ID: TCIC2 Purpose: Verify that the carousel displays the correct number of images Priority: 2 Test Coverage Item: Carousel Display Preconditions: The ‘IndexComponent‘ is initialized and the ‘images‘ array is set Inputs: Set ‘component.images‘ to [’image1.png’, ’image2.png’] Expected Results: The DOM should contain two elements with the class ‘carousel-item‘ Postconditions: N/A

Table 7.46: Test case to verify carousel image display in ‘IndexComponent‘

Test Case ID: TCIC3 Purpose: Verify that the ‘nextSlide‘ method is called when the next button is clicked Priority: 2 Test Coverage Item: Carousel Navigation Preconditions: The ‘IndexComponent‘ is initialized and the carousel is displayed Inputs: User interaction: click on the ‘.next‘ button Expected Results: The ‘nextSlide‘ method of the component should be called Postconditions: N/A

Table 7.47: Test case to verify ‘nextSlide‘ method call in ‘IndexComponent‘

Test Case ID: TCIC4 Purpose: Verify that the ‘prevSlide‘ method is called when the previous button is clicked Priority: 2 Test Coverage Item: Carousel Navigation Preconditions: The ‘IndexComponent‘ is initialized and the carousel is displayed Inputs: User interaction: click on the ‘.prev‘ button Expected Results: The ‘prevSlide‘ method of the component should be called Postconditions: N/A

Table 7.48: Test case to verify ‘prevSlide‘ method call in ‘IndexComponent‘

149

Testing of LocalsComponent

Test Case ID: TCLC1 Purpose: Verify that the ‘LocalsComponent‘ is created successfully Priority: 1 Test Coverage Item: Component Initialization Preconditions: Angular testing module is configured with the ‘LocalsComponent‘ Inputs: N/A Expected Results: The ‘LocalsComponent‘ instance should be truthy Postconditions: N/A

Table 7.49: Test case to verify ‘LocalsComponent‘ creation

Test Case ID: TCLC2 Purpose: Verify that the ‘nextSlide‘ method is called when the next button is clicked Priority: 2 Test Coverage Item: Carousel Navigation Preconditions: The ‘LocalsComponent‘ is initialized Inputs: User interaction: click on the ‘.next‘ button Expected Results: The ‘nextSlide‘ method of the component should be called Postconditions: N/A

Table 7.50: Test case to verify ‘nextSlide‘ method call in ‘LocalsComponent‘

Test Case ID: TCLC3 Purpose: Verify that the ‘prevSlide‘ method is called when the previous button is clicked Priority: 2 Test Coverage Item: Carousel Navigation Preconditions: The ‘LocalsComponent‘ is initialized Inputs: User interaction: click on the ‘.prev‘ button Expected Results: The ‘prevSlide‘ method of the component should be called Postconditions: N/A

Table 7.51: Test case to verify ‘prevSlide‘ method call in ‘LocalsComponent‘

150

Testing of LoginComponent

Test Case ID: TCLogC1 Purpose: Verify that the ‘LoginComponent‘ is created successfully Priority: 1 Test Coverage Item: Component Initialization Preconditions: Angular testing module is configured with ‘FormsModule‘, ‘LoginComponent‘, and the necessary services mocked Inputs: N/A Expected Results: The ‘LoginComponent‘ instance should be truthy Postconditions: N/A

Table 7.52: Test case to verify ‘LoginComponent‘ creation

Test Case ID: TCLogC2 Purpose: Verify that the ‘AuthService‘ login method is called with the correct credentials when the form is submitted Priority: 2 Test Coverage Item: Form Submission Preconditions: The ‘LoginComponent‘ is initialized, and the ‘AuthService‘ mock is provided Inputs: User credentials: email: ’user@example.com’, password: ’password’ Expected Results: The ‘AuthService.login‘ method should be called with the provided email and password Postconditions: N/A

Table 7.53: Test case to verify ‘AuthService‘ login method call in ‘LoginComponent‘

Test Case ID: TCLogC3 Purpose: Verify that the user is navigated to the home page after a successful login Priority: 2 Test Coverage Item: Navigation after Login Preconditions: The ‘LoginComponent‘ is initialized, and the ‘AuthService‘ mock returns a successful login Inputs: Form submission Expected Results: The ‘Router.navigateByUrl‘ method should be called with the argument ‘’/’‘ to navigate to the home page Postconditions: N/A

Table 7.54: Test case to verify navigation after login in ‘LoginComponent‘

151

Testing of PaymentGatewayComponent

Test Case ID: TCPGC1 Purpose: Verify that the ‘PaymentGatewayComponent‘ is created successfully Priority: 1 Test Coverage Item: Component Initialization Preconditions: Angular testing module is configured with necessary dependencies and mocks Inputs: N/A Expected Results: The ‘PaymentGatewayComponent‘ instance should be truthy Postconditions: N/A

Table 7.55: Test case to verify ‘PaymentGatewayComponent‘ creation

Test Case ID: TCPGC2 Purpose: Verify that products in the cart are displayed correctly Priority: 2 Test Coverage Item: Cart Display Functionality Preconditions: ‘PaymentGatewayComponent‘ is initialized with mock cart items Inputs:

- Cart items:

– { id: 1, name: ’Product 1’, image: ’image1.jpg’, quantityToBuy: 1, price: 100, maxQuantity: 10, details: ’Details of product 1’}

Expected Results: The cart item should be displayed in the DOM with the correct details Postconditions: N/A

Table 7.56: Test case to verify cart item display in ‘PaymentGatewayComponent‘

152

Test Case ID: TCPGC3 Purpose: Verify that the cart subtotal is calculated correctly Priority: 2 Test Coverage Item: Cart Calculation Functionality Preconditions: ‘PaymentGatewayComponent‘ is initialized with mock cart items Inputs:

- Cart items:

– { id: 1, name: ’Product 1’, image: ’image1.jpg’, quantityToBuy: 1, price: 100, maxQuantity: 10, details: ’Details of product 1’}

– { id: 2, name: ’Product 2’, image: ’image2.jpg’, quantityToBuy: 2, price: 50, maxQuantity: 5, details: ’Details of product 2’}

Expected Results: The cart subtotal should be calculated as 200 Postconditions: N/A

Table 7.57: Test case to verify cart subtotal calculation in ‘PaymentGatewayComponent‘

Test Case ID: TCPGC4 Purpose: Verify that the deleteCartItem method is called when the delete button is clicked Priority: 2 Test Coverage Item: Cart Item Deletion Functionality Preconditions: ‘PaymentGatewayComponent‘ is initialized with mock cart items Inputs:

- Cart items:

– { id: 1, name: ’Product 1’, image: ’image1.jpg’, quantityToBuy: 1, price: 100, maxQuantity: 10, details: ’Details of product 1’}

Expected Results: The ‘deleteCartItem‘ method should be called with the correct item ID when the delete button is clicked Postconditions: N/A

Table 7.58: Test case to verify cart item deletion in ‘PaymentGatewayComponent‘

153

Testing of ProductSectionComponent

Test Case ID: TCPSC1 Purpose: Verify that the ‘ProductSectionComponent‘ is created successfully Priority: 1 Test Coverage Item: Component Initialization Preconditions: Angular testing module is configured with necessary dependencies and mocks Inputs: N/A Expected Results: The ‘ProductSectionComponent‘ instance should be truthy Postconditions: N/A

Table 7.59: Test case to verify ‘ProductSectionComponent‘ creation

Test Case ID: TCPSC2 Purpose: Verify initialization of section and fetching of user info and wishlist if logged in Priority: 2 Test Coverage Item: Component Initialization Preconditions: ‘ProductSectionComponent‘ is initialized and the user is logged in Inputs: N/A Expected Results:

- Section should be initialized to ’videojuegos’

- ‘authServiceMock.checkLoginStatus‘ should be called

- ‘authServiceMock.getUserInfo‘ should be called

- ‘wishlistServiceMock.getWishlist‘ should be called

Postconditions: N/A

Table 7.60: Test case to verify section initialization and user data fetching in ‘Product- SectionComponent‘

154

Test Case ID: TCPSC3 Purpose: Verify fetching of products based on section Priority: 2 Test Coverage Item: Product Fetching Functionality Preconditions: ‘ProductSectionComponent‘ is initialized Inputs:

- Min Price: ‘component.minPrice‘

- Max Price: ‘component.maxPrice‘

- Category: ‘component.category‘

Expected Results: ‘productServiceMock.getFilteredProducts‘ should be called with the correct parameters Postconditions: N/A

Table 7.61: Test case to verify product fetching based on section in ‘ProductSection- Component‘

Test Case ID: TCPSC4 Purpose: Verify sorting of products by price in ascending order Priority: 2 Test Coverage Item: Product Sorting Functionality Preconditions: ‘ProductSectionComponent‘ is initialized with a list of products Inputs:

- Products:

– { id: 1, name: ’Product 1’, price: 100}

– { id: 2, name: ’Product 2’, price: 50}

Expected Results: Products should be sorted by price in ascending order Postconditions: N/A

Table 7.62: Test case to verify sorting of products by price in ‘ProductSectionComponent‘

155

Test Case ID: TCPSC5 Purpose: Verify adding a product to the wishlist Priority: 2 Test Coverage Item: Wishlist Functionality Preconditions: ‘ProductSectionComponent‘ is initialized Inputs:

- Product: { id: 1, name: ’Product 1’}

Expected Results: ‘wishlistServiceMock.addToWishlist‘ should be called with the correct product ID Postconditions: N/A

Table 7.63: Test case to verify adding a product to the wishlist in ‘ProductSectionComponent‘

Test Case ID: TCPSC6 Purpose: Verify removing a product from the wishlist Priority: 2 Test Coverage Item: Wishlist Functionality Preconditions: ‘ProductSectionComponent‘ is initialized with a product in the wishlist Inputs:

- Product: { id: 1, name: ’Product 1’}

Expected Results: ‘wishlistServiceMock.removeFromWishlist‘ should be called with the correct product ID Postconditions: N/A

Table 7.64: Test case to verify removing a product from the wishlist in ‘ProductSection- Component‘

156

Test Case ID: TCPSC7 Purpose: Verify adding a product to the cart Priority: 2 Test Coverage Item: Cart Functionality Preconditions: ‘ProductSectionComponent‘ is initialized Inputs:

- Product: { id: 1, name: ’Product 1’, price: 100, quan-

tity: 10, details: ”, image: ”}

- Event: Mouse click event

Expected Results: ‘cartServiceMock.addToCart‘ should be called with the correct product details Postconditions: N/A

Table 7.65: Test case to verify adding a product to the cart in ‘ProductSectionComponent‘

Test Case ID: TCPSC8 Purpose: Verify navigation when the search icon is clicked Priority: 2 Test Coverage Item: Navigation Functionality Preconditions: ‘ProductSectionComponent‘ is initialized with a search term Inputs:

- Search term: ’search term’

Expected Results: ‘routerMock.navigate‘ should be called with the correct query parameters Postconditions: N/A

Table 7.66: Test case to verify navigation on search icon click in ‘ProductSectionComponent‘

157

Test Case ID: TCPSC9 Purpose: Verify navigation when the Enter key is pressed in search Priority: 2 Test Coverage Item: Navigation Functionality Preconditions: ‘ProductSectionComponent‘ is initialized with a search term Inputs:

- Search term: ’search term’

- Event: Keyboard event (Enter key press)

Expected Results: ‘routerMock.navigate‘ should be called with the correct query parameters Postconditions: N/A

Table 7.67: Test case to verify navigation on Enter key press in search in ‘ProductSectionComponent‘

Test Case ID: TCPSC10 Purpose: Verify wishlist addition or removal based on login status Priority: 2 Test Coverage Item: Wishlist Functionality Preconditions: ‘ProductSectionComponent‘ is initialized, and user is logged in Inputs:

- Product: { id: 1, name: ’Product 1’}

- Event: Mouse click event

Expected Results:

- If the product is not in the wishlist, it should be added.

- If the product is in the wishlist, it should be removed.

Postconditions: N/A

Table 7.68: Test case to verify wishlist addition or removal based on login status in ‘ProductSectionComponent‘

158

Test Case ID: TCPSC11 Purpose: Verify filtering of products by genre and platform Priority: 2 Test Coverage Item: Product Filtering Functionality Preconditions: ‘ProductSectionComponent‘ is initialized Inputs:

- Platform: ’PS5’

- Genre: ’Acci´on’

Expected Results:

- The selected platform should be set to ’PS5’

- The selected genre should be set to ’Acci´on’

- ‘component.getFilteredData‘ should be called

Postconditions: N/A

Table 7.69: Test case to verify filtering of products by genre and platform in ‘Product- SectionComponent‘

Testing of RegisterComponent

Test Case ID: TCRC1 Purpose: Verify that the ‘RegisterComponent‘ is created successfully Priority: 1 Test Coverage Item: Component Initialization Preconditions: Angular testing module is configured with necessary dependencies and mocks Inputs: N/A Expected Results: The ‘RegisterComponent‘ instance should be truthy Postconditions: N/A

Table 7.70: Test case to verify ‘RegisterComponent‘ creation

159

Test Case ID: TCRC2 Purpose: Verify that the ‘AuthService.register‘ method is called when the form is submitted Priority: 2 Test Coverage Item: Registration Functionality Preconditions: ‘RegisterComponent‘ is initialized and form is filled with valid data Inputs:

- First Name: ’John’

- Last Name: ’Doe’

- Email: ’user@example.com’

- Password: ’password123’

Expected Results: ‘AuthService.register‘ should be called with the correct parameters Postconditions: N/A

Table 7.71: Test case to verify registration form submission in ‘RegisterComponent‘

160

Test Case ID: TCRC3 Purpose: Verify that an error message is shown if the email already exists Priority: 2 Test Coverage Item: Error Handling Preconditions: ‘RegisterComponent‘ is initialized, and form is filled with data Inputs:

- First Name: ’John’

- Last Name: ’Doe’

- Email: ’user@example.com’

- Password: ’password123’

Expected Results:

- ‘AuthService.register‘ should return an error indicat-

ing email already exists

- Component should display an alert with the message

’El correo ya est´a registrado.’

Postconditions: N/A

Table 7.72: Test case to verify error handling when email already exists in ‘RegisterComponent‘

161

Test Case ID: TCRC4 Purpose: Verify that a general error message is shown on registration failure Priority: 2 Test Coverage Item: Error Handling Preconditions: ‘RegisterComponent‘ is initialized, and form is filled with data Inputs:

- First Name: ’John’

- Last Name: ’Doe’

- Email: ’user@example.com’

- Password: ’password123’

Expected Results:

- ‘AuthService.register‘ should return a general error

- Component should display an alert with the message

’Ocurri´o un error durante el registro.’

Postconditions: N/A

Table 7.73: Test case to verify general error handling in ‘RegisterComponent‘

162

Test Case ID: TCRC5 Purpose: Verify that a validation error message is shown if the form is invalid Priority: 2 Test Coverage Item: Form Validation Preconditions: ‘RegisterComponent‘ is initialized, and form is filled with invalid data Inputs:

- First Name: ”

- Last Name: ”

- Email: ’invalid-email’

- Password: ’123’

Expected Results: Component should display an alert with the message ’Porfavor rellena todos los campos.’ Postconditions: N/A

Table 7.74: Test case to verify form validation error handling in ‘RegisterComponent‘

Test Case ID: TCRC6 Purpose: Verify that the component navigates to the login page when ‘navigateToLogin‘ is called Priority: 2 Test Coverage Item: Navigation Functionality Preconditions: ‘RegisterComponent‘ is initialized Inputs: N/A Expected Results: ‘routerMock.navigateByUrl‘ should be called with ’/login’ Postconditions: N/A

Table 7.75: Test case to verify navigation to login page in ‘RegisterComponent‘

163

Testing of ResetPasswordComponent

Test Case ID: TCRPC1 Purpose: Verify that the ‘ResetPasswordComponent‘ is created successfully Priority: 1 Test Coverage Item: Component Initialization Preconditions: Angular testing module is configured with necessary dependencies and mocks Inputs: N/A Expected Results: The ‘ResetPasswordComponent‘ instance should be truthy Postconditions: N/A

Table 7.76: Test case to verify ‘ResetPasswordComponent‘ creation

Test Case ID: TCRPC2 Purpose: Verify that the ‘uid‘ and ‘token‘ are initialized from route params Priority: 2 Test Coverage Item: Route Parameter Initialization Preconditions: ‘ResetPasswordComponent‘ is initialized and ‘ngOnInit‘ is called Inputs: Mock route parameters: {uid: ’test-uid’, token: ’testtoken’} Expected Results: The ‘uid‘ and ‘token‘ properties of the component should be initialized with the values from the route params Postconditions: N/A

Table 7.77: Test case to verify route parameter initialization in ‘ResetPasswordComponent‘

164

Test Case ID: TCRPC3 Purpose: Verify that an alert is shown and navigation occurs on successful password reset Priority: 2 Test Coverage Item: Password Reset Functionality Preconditions: The form is filled with valid password and confirmPassword values Inputs:

- Password: ’ValidPassword’

- Confirm Password: ’ValidPassword’

Expected Results:

- ‘AuthService.resetPassword‘ should be called and re-

turn a success response.

- An alert should be set with the message ’Contrase˜na

restablecida con ´exito.’

- The user should be navigated to the login page.

Postconditions: Ensure no outstanding operations remain

Table 7.78: Test case to verify successful password reset in ‘ResetPasswordComponent‘

Testing of ShoppingCartModalComponent

Test Case ID: TCSCM1 Purpose: Verify that the ‘ShoppingCartModalComponent‘ is created successfully Priority: 1 Test Coverage Item: Component Initialization Preconditions: Angular testing module is configured with ‘ShoppingCart- ModalComponent‘ and ‘HttpClientTestingModule‘ Inputs: N/A Expected Results: The ‘ShoppingCartModalComponent‘ instance should be truthy Postconditions: N/A

Table 7.79: Test case to verify ‘ShoppingCartModalComponent‘ creation

165

Test Case ID: TCSCM2 Purpose: Verify that products are displayed in the cart Priority: 2 Test Coverage Item: Cart Display Functionality Preconditions: Mock cart items are stored in ‘localStorage‘ Inputs: Mock cart items: {id: 1, name: ’Product 1’, image: ’image1.jpg’, quantityToBuy: 1, price: 100, maxQuantity: 10, details: ’Details of product 1’} Expected Results: The cart items should be rendered in the DOM Postconditions: N/A

Table 7.80: Test case to verify products display in the cart

Test Case ID: TCSCM3 Purpose: Verify that the cart subtotal is calculated correctly Priority: 2 Test Coverage Item: Cart Calculation Functionality Preconditions: Mock cart items are stored in ‘localStorage‘ Inputs: Mock cart items: {id: 1, name: ’Product 1’, image: ’image1.jpg’, quantityToBuy: 1, price: 100, maxQuantity: 10, details: ’Details of product 1’}, {id: 2, name: ’Product 2’, image: ’image2.jpg’, quantityToBuy: 2, price: 50, maxQuantity: 5, details: ’Details of product 2’} Expected Results: The cart subtotal should be 200 Postconditions: N/A

Table 7.81: Test case to verify cart subtotal calculation

Test Case ID: TCSCM4 Purpose: Verify that ‘goToCheckout‘ is called when the checkout button is clicked Priority: 2 Test Coverage Item: Checkout Navigation Preconditions: The checkout button is rendered in the DOM Inputs: Click event on the checkout button Expected Results: The ‘goToCheckout‘ method should be called Postconditions: N/A

Table 7.82: Test case to verify checkout button functionality

166

Test Case ID: TCSCM5 Purpose: Verify that underscores are replaced with spaces in product names Priority: 3 Test Coverage Item: String Formatting Functionality Preconditions: The ‘ShoppingCartModalComponent‘ is initialized Inputs: ’Product Name With Underscores’ Expected Results: The output should be ’Product Name With Underscores’ Postconditions: N/A

Table 7.83: Test case to verify underscore replacement in product names

Test Case ID: TCSCM6 Purpose: Verify that the correct subtotal is calculated for a product Priority: 2 Test Coverage Item: Product Subtotal Calculation Preconditions: Mock cart items are stored in ‘localStorage‘ Inputs: Mock cart item: {id: 1, name: ’Product 1’, image: ’image1.jpg’, quantityToBuy: 2, price: 50, maxQuantity: 10, details: ’Details of product 1’} Expected Results: The product subtotal should be 100 Postconditions: N/A

Table 7.84: Test case to verify product subtotal calculation

Test Case ID: TCSCM7 Purpose: Verify that the correct IVA is calculated for a product Priority: 2 Test Coverage Item: Product IVA Calculation Preconditions: Mock cart items are stored in ‘localStorage‘ Inputs: Mock cart item: {id: 1, name: ’Product 1’, image: ’image1.jpg’, quantityToBuy: 2, price: 50, maxQuantity: 10, details: ’Details of product 1’} Expected Results: The product IVA should be 12 Postconditions: N/A

Table 7.85: Test case to verify product IVA calculation

167

Test Case ID: TCSCM8 Purpose: Verify that the correct total is calculated for a product Priority: 2 Test Coverage Item: Product Total Calculation Preconditions: Mock cart items are stored in ‘localStorage‘ Inputs: Mock cart item: {id: 1, name: ’Product 1’, image: ’image1.jpg’, quantityToBuy: 2, price: 50, maxQuantity: 10, details: ’Details of product 1’} Expected Results: The product total should be 112 Postconditions: N/A

Table 7.86: Test case to verify product total calculation

Test Case ID: TCSCM9 Purpose: Verify that the correct IVA is calculated for the entire cart Priority: 2 Test Coverage Item: Cart IVA Calculation Preconditions: Mock cart items are stored in ‘localStorage‘ Inputs: Mock cart items: {id: 1, name: ’Product 1’, image: ’image1.jpg’, quantityToBuy: 1, price: 100, maxQuantity: 10, details: ’Details of product 1’}, {id: 2, name: ’Product 2’, image: ’image2.jpg’, quantityToBuy: 2, price: 50, maxQuantity: 5, details: ’Details of product 2’} Expected Results: The cart IVA should be 24 Postconditions: N/A

Table 7.87: Test case to verify cart IVA calculation

Test Case ID: TCSCM10 Purpose: Verify that the correct total is calculated for the entire cart Priority: 2 Test Coverage Item: Cart Total Calculation Preconditions: Mock cart items are stored in ‘localStorage‘ Inputs: Mock cart items: {id: 1, name: ’Product 1’, image: ’image1.jpg’, quantityToBuy: 1, price: 100, maxQuantity: 10, details: ’Details of product 1’}, {id: 2, name: ’Product 2’, image: ’image2.jpg’, quantityToBuy: 2, price: 50, maxQuantity: 5, details: ’Details of product 2’} Expected Results: The cart total should be 224 Postconditions: N/A

Table 7.88: Test case to verify cart total calculation

168

Test Case ID: TCSCM11 Purpose: Verify that the quantity of a product is updated correctly Priority: 2 Test Coverage Item: Quantity Update Functionality Preconditions: Mock cart items are stored in ‘localStorage‘ Inputs: Event with input value ’5’, product ID: 1 Expected Results: The quantity of the product should be updated to 5 Postconditions: N/A

Table 7.89: Test case to verify product quantity update

Test Case ID: TCSCM12 Purpose: Verify that the quantity of a product increases correctly Priority: 2 Test Coverage Item: Quantity Increase Functionality Preconditions: Mock cart items are stored in ‘localStorage‘ Inputs: Product ID: 1 Expected Results: The quantity of the product should increase by 1 Postconditions: N/A

Table 7.90: Test case to verify product quantity increase

Test Case ID: TCSCM13 Purpose: Verify that the quantity of a product decreases correctly Priority: 2 Test Coverage Item: Quantity Decrease Functionality Preconditions: Mock cart items are stored in ‘localStorage‘ Inputs: Product ID: 1 Expected Results: The quantity of the product should decrease by 1 Postconditions: N/A

Table 7.91: Test case to verify product quantity decrease

169

Test Case ID: TCSCM14 Purpose: Verify that a product is deleted from the cart Priority: 2 Test Coverage Item: Cart Item Deletion Preconditions: Mock cart items are stored in ‘localStorage‘, user confirms deletion Inputs: Product ID: 1 Expected Results: The product should be removed from the cart Postconditions: N/A

Table 7.92: Test case to verify cart item deletion

Test Case ID: TCSCM15 Purpose: Verify that typing in quantity input is prevented Priority: 2 Test Coverage Item: Input Typing Prevention Preconditions: The ‘ShoppingCartModalComponent‘ is initialized Inputs: KeyboardEvent for typing ’a’ Expected Results: The default action of typing should be prevented Postconditions: N/A

Table 7.93: Test case to verify prevention of typing in quantity input

Testing of UserDetailsComponent

Test Case ID: TCUDC1 Purpose: Verify that the ‘UserDetailsComponent‘ is created successfully Priority: 1 Test Coverage Item: Component Initialization Preconditions: Angular testing module is configured with ‘UserDetailsComponent‘, ‘RouterTestingModule‘, and ‘HttpClientTesting- Module‘ Inputs: N/A Expected Results: The ‘UserDetailsComponent‘ instance should be truthy Postconditions: N/A

Table 7.94: Test case to verify ‘UserDetailsComponent‘ creation

170

Test Case ID: TCUDC2 Purpose: Verify that the component has links to user account and purchase history Priority: 2 Test Coverage Item: Navigation Links Preconditions: The ‘UserDetailsComponent‘ is rendered Inputs: N/A Expected Results: The component should have two links: one to ‘/userDetails/userAccount‘ and another to ‘/userDetails/userPurchase- History‘ Postconditions: N/A

Table 7.95: Test case to verify navigation links in ‘UserDetailsComponent‘

Testing of UserAccountComponent

Test Case ID: TCUAC1 Purpose: Verify that the ‘UserAccountComponent‘ is created successfully Priority: 1 Test Coverage Item: Component Initialization Preconditions: Angular testing module is configured with ‘UserAccount- Component‘ and ‘HttpClientTestingModule‘ Inputs: N/A Expected Results: The ‘UserAccountComponent‘ instance should be truthy Postconditions: N/A

Table 7.96: Test case to verify ‘UserAccountComponent‘ creation

Test Case ID: TCUAC2 Purpose: Verify that user information is displayed correctly Priority: 2 Test Coverage Item: User Information Display Preconditions: The ‘UserAccountComponent‘ is rendered with mock user data Inputs: Mock user data: {id: 1, first name: ’John’, last name: ’Doe’, email: ’john.doe@example.com’} Expected Results: The first name, last name, and email fields should display the correct values Postconditions: N/A

Table 7.97: Test case to verify user information display in ‘UserAccountComponent‘

171

Test Case ID: TCUAC3 Purpose: Verify that the ‘logout‘ method is called when the logout button is clicked Priority: 2 Test Coverage Item: Logout Functionality Preconditions: The ‘UserAccountComponent‘ is rendered Inputs: Click event on the logout button Expected Results: The ‘logout‘ method should be called Postconditions: N/A

Table 7.98: Test case to verify logout functionality in ‘UserAccountComponent‘

Testing of UserPurchaseHistoryComponent

Test Case ID: TCUPH1 Purpose: Verify that the ‘UserPurchaseHistoryComponent‘ is created successfully Priority: 1 Test Coverage Item: Component Initialization Preconditions: Angular testing module is configured with ‘UserPurchase- HistoryComponent‘ and ‘HttpClientTestingModule‘ Inputs: N/A Expected Results: The ‘UserPurchaseHistoryComponent‘ instance should be truthy Postconditions: N/A

Table 7.99: Test case to verify ‘UserPurchaseHistoryComponent‘ creation

172

Test Case ID: TCUPH2 Purpose: Verify that the order list is displayed correctly Priority: 2 Test Coverage Item: Order List Display Preconditions: The ‘UserPurchaseHistoryComponent‘ is rendered with mock orders and products data Inputs:

- Mock orders:

– {id: 1, client: 123, total: 100, status: ’completed’, date created: ’2024-01-01’, date update: ’2024-01-02’, items: [{product: 1, quantity: 2}]}

- Mock products:

– {id: 1, name: ’Product 1’, image: ’product.jpg’, description: ’Product Description’, details: ’Details’, local: ’Store’, price: 50}

Expected Results: The order list should be rendered in the DOM with the corresponding product details Postconditions: N/A

Table 7.100: Test case to verify order list display in ‘UserPurchaseHistoryComponent‘

Testing of WishlistModalComponent

Test Case ID: TCWM1 Purpose: Verify that the ‘WishlistModalComponent‘ is created successfully Priority: 1 Test Coverage Item: Component Initialization Preconditions: Angular testing module is configured with ‘WishlistModal- Component‘ and ‘HttpClientTestingModule‘ Inputs: N/A Expected Results: The ‘WishlistModalComponent‘ instance should be truthy Postconditions: N/A

Table 7.101: Test case to verify ‘WishlistModalComponent‘ creation

173

Test Case ID: TCWM2 Purpose: Verify that products in the wishlist are displayed correctly Priority: 2 Test Coverage Item: Wishlist Display Functionality Preconditions: The ‘WishlistModalComponent‘ is rendered with mock wishlist data Inputs:

- Mock wishlist data:

– {id: 1, name: ’Product 1’, description: ’Description’, price: 100, image: ’image1.jpg’, added at: ’2024-08-01T00:00:00Z’}

Expected Results: The wishlist products should be rendered in the DOM with the correct details Postconditions: N/A

Table 7.102: Test case to verify wishlist product display in ‘WishlistModalComponent‘

Test Case ID: TCWM3 Purpose: Verify that the ‘onClose‘ method is called when the close button is clicked Priority: 2 Test Coverage Item: Close Button Functionality Preconditions: The ‘WishlistModalComponent‘ is rendered Inputs: Click event on the close button Expected Results: The ‘onClose‘ method should be called Postconditions: N/A

Table 7.103: Test case to verify close button functionality in ‘WishlistModalComponent‘

7. 2.2 Unit Test Cases: Backend Testing

The backend, responsible for business logic and data management, has been subjected to a series of unit tests that verify the correct functioning of individual components and the correct functioning of system models and views. For our Django-based backend, we employ Django’s built-in testing tools, including pytest, for comprehensive testing of our API endpoints and business logic. Furthermore, we leverage Django’s factory libraries to create mock data that simulate our database models, ensuring thorough testing of our application’s behavior under various scenarios.

174

Client Model Test Cases

Test Case ID: TCCM1 Purpose: Verify that a ‘User‘ instance is created successfully Priority: 1 Test Coverage Item: User Model Creation Preconditions: N/A Inputs: Use ‘UserFactory()‘ to create a user Expected Results: A ‘User‘ instance should be created, and its string representation should match its email Postconditions: N/A

Table 7.104: Test case to verify ‘User‘ model creation

Test Case ID: TCCM2 Purpose: Verify that the ‘User‘ model’s password is hashed correctly Priority: 1 Test Coverage Item: User Password Hashing Preconditions: N/A Inputs: Use ‘UserFactory(password=’mysecret’)‘ to create a user with a raw password Expected Results: The stored password should be hashed, and ‘check password‘ should return true for the original password Postconditions: N/A

Table 7.105: Test case to verify password hashing in ‘User‘ model

Test Case ID: TCCM3 Purpose: Verify that a ‘Client‘ instance is created successfully Priority: 1 Test Coverage Item: Client Model Creation Preconditions: N/A Inputs: Use ‘ClientFactory()‘ to create a client Expected Results: A ‘Client‘ instance should be created, and its string representation should match its ‘dni‘ Postconditions: N/A

Table 7.106: Test case to verify ‘Client‘ model creation

175

Test Case ID: TCCM4 Purpose: Verify the relationship between ‘Client‘ and ‘User‘ models Priority: 2 Test Coverage Item: Client-User Relationship Preconditions: A ‘Client‘ instance exists Inputs: Use ‘ClientFactory()‘ to create a client Expected Results: The ‘user‘ attribute of the ‘Client‘ instance should be an instance of ‘User‘ Postconditions: N/A

Table 7.107: Test case to verify ‘Client‘ model relationship with ‘User‘

Test Case ID: TCCM5 Purpose: Verify that a ‘Category‘ instance is created successfully Priority: 1 Test Coverage Item: Category Model Creation Preconditions: N/A Inputs: Use ‘CategoryFactory()‘ to create a category Expected Results: A ‘Category‘ instance should be created, and its string representation should match its ‘name‘ Postconditions: N/A

Table 7.108: Test case to verify ‘Category‘ model creation

Test Case ID: TCCM6 Purpose: Verify the uniqueness constraint on the ‘name‘ field in ‘Category‘ model Priority: 2 Test Coverage Item: Category Name Uniqueness Preconditions: A ‘Category‘ instance with ‘name=’Electronics’‘ exists Inputs: Use ‘CategoryFactory(name=’Electronics’)‘ to create a category with the same name Expected Results: An exception should be raised due to the uniqueness constraint Postconditions: N/A

Table 7.109: Test case to verify uniqueness of ‘name‘ in ‘Category‘ model

176

Test Case ID: TCCM7 Purpose: Verify that a ‘Product‘ instance is created successfully Priority: 1 Test Coverage Item: Product Model Creation Preconditions: N/A Inputs: Use ‘ProductFactory()‘ to create a product Expected Results: A ‘Product‘ instance should be created, and its string representation should match its ‘name‘ Postconditions: N/A

Table 7.110: Test case to verify ‘Product‘ model creation

Test Case ID: TCCM8 Purpose: Verify the relationship between ‘Product‘ and ‘Category‘ models Priority: 2 Test Coverage Item: Product-Category Relationship Preconditions: A ‘Product‘ instance exists Inputs: Use ‘ProductFactory()‘ to create a product Expected Results: The ‘category‘ attribute of the ‘Product‘ instance should be an instance of ‘Category‘ Postconditions: N/A

Table 7.111: Test case to verify ‘Product‘ model relationship with ‘Category‘

Test Case ID: TCCM9 Purpose: Verify the price field in ‘Product‘ model Priority: 2 Test Coverage Item: Product Price Preconditions: N/A Inputs: Use ‘ProductFactory(price=100.00)‘ to create a product Expected Results: The ‘price‘ attribute of the ‘Product‘ instance should match the input value Postconditions: N/A

Table 7.112: Test case to verify price in ‘Product‘ model

177

Test Case ID: TCCM10 Purpose: Verify that an ‘Order‘ instance is created successfully Priority: 1 Test Coverage Item: Order Model Creation Preconditions: N/A Inputs: Use ‘OrderFactory()‘ to create an order Expected Results: An ‘Order‘ instance should be created Postconditions: N/A

Table 7.113: Test case to verify ‘Order‘ model creation

Test Case ID: TCCM11 Purpose: Verify the relationship between ‘Order‘ and ‘Client‘ models Priority: 2 Test Coverage Item: Order-Client Relationship Preconditions: An ‘Order‘ instance exists Inputs: Use ‘OrderFactory()‘ to create an order Expected Results: The ‘client‘ attribute of the ‘Order‘ instance should be an instance of ‘Client‘ Postconditions: N/A

Table 7.114: Test case to verify ‘Order‘ model relationship with ‘Client‘

Test Case ID: TCCM12 Purpose: Verify the status field in ‘Order‘ model Priority: 2 Test Coverage Item: Order Status Preconditions: N/A Inputs: Use ‘OrderFactory(status=’Pending’)‘ to create an order Expected Results: The ‘status‘ attribute of the ‘Order‘ instance should match the input value Postconditions: N/A

Table 7.115: Test case to verify status in ‘Order‘ model

178

Test Case ID: TCCM13 Purpose: Verify that an ‘OrderItem‘ instance is created successfully Priority: 1 Test Coverage Item: OrderItem Model Creation Preconditions: N/A Inputs: Use ‘OrderItemFactory()‘ to create an order item Expected Results: An ‘OrderItem‘ instance should be created Postconditions: N/A

Table 7.116: Test case to verify ‘OrderItem‘ model creation

Test Case ID: TCCM14 Purpose: Verify the relationships between ‘OrderItem‘, ‘Order‘, and ‘Product‘ models Priority: 2 Test Coverage Item: OrderItem Relationships Preconditions: An ‘OrderItem‘ instance exists Inputs: Use ‘OrderItemFactory()‘ to create an order item Expected Results: The ‘order‘ attribute should be an instance of ‘Order‘, and the ‘product‘ attribute should be an instance of ‘Product‘ Postconditions: N/A

Table 7.117: Test case to verify ‘OrderItem‘ model relationships

Test Case ID: TCCM15 Purpose: Verify that a ‘WishlistItem‘ instance is created successfully Priority: 1 Test Coverage Item: WishlistItem Model Creation Preconditions: N/A Inputs: Use ‘WishlistItemFactory()‘ to create a wishlist item Expected Results: A ‘WishlistItem‘ instance should be created Postconditions: N/A

Table 7.118: Test case to verify ‘WishlistItem‘ model creation

179

Test Case ID: TCCM16 Purpose: Verify the relationships between ‘WishlistItem‘, ‘User‘, and ‘Product‘ models Priority: 2 Test Coverage Item: WishlistItem Relationships Preconditions: A ‘WishlistItem‘ instance exists Inputs: Use ‘WishlistItemFactory()‘ to create a wishlist item Expected Results: The ‘user‘ attribute should be an instance of ‘User‘, and the ‘product‘ attribute should be an instance of ‘Product‘ Postconditions: N/A

Table 7.119: Test case to verify ‘WishlistItem‘ model relationships

Test Case ID: TCCM17 Purpose: Verify the uniqueness constraint on the combination of ‘user‘ and ‘product‘ in ‘WishlistItem‘ model Priority: 2 Test Coverage Item: WishlistItem Uniqueness Preconditions: A ‘WishlistItem‘ instance with a specific ‘user‘ and ‘product‘ exists Inputs: Use ‘WishlistItemFactory(user=existing user, product=existing product)‘ to create another wishlist item with the same ‘user‘ and ‘product‘ Expected Results: An exception should be raised due to the uniqueness constraint Postconditions: N/A

Table 7.120: Test case to verify uniqueness of ‘WishlistItem‘ model

180

Test cases for Serializer validation

Test Case ID: TCSV1 Purpose: Verify that the ‘UserSerializer‘ serializes the ‘User‘ model correctly Priority: 1 Test Coverage Item: User Serialization Preconditions: A ‘User‘ instance exists Inputs: Serialize a ‘User‘ instance using ‘UserSerializer‘ Expected Results: The serialized data should contain the correct fields: ‘id‘, ‘email‘, ‘first name‘, ‘last name‘, ‘password‘, ‘last login‘, ‘is active‘, ‘date joined‘, ‘is staff‘, ‘groups‘, ‘is superuser‘, ‘user permissions‘ Postconditions: N/A

Table 7.121: Test case to verify ‘UserSerializer‘ serialization

Test Case ID: TCSV2 Purpose: Verify that the ‘UserSerializer‘ updates a ‘User‘ instance correctly Priority: 1 Test Coverage Item: User Update Preconditions: A ‘User‘ instance exists Inputs: Update the ‘User‘ instance’s ‘first name‘ field using ‘UserSerializer‘ Expected Results: The ‘first name‘ field should be updated to the new value Postconditions: N/A

Table 7.122: Test case to verify ‘UserSerializer‘ update functionality

181

Test Case ID: TCSV3 Purpose: Verify that the ‘UserSerializer‘ handles invalid email addresses correctly Priority: 2 Test Coverage Item: User Validation Preconditions: A ‘User‘ instance exists Inputs: Try to update the ‘User‘ instance’s ‘email‘ field to an invalid email using ‘UserSerializer‘ Expected Results: The serializer should be invalid and should contain an error message for the ‘email‘ field Postconditions: N/A

Table 7.123: Test case to verify ‘UserSerializer‘ email validation

Test Case ID: TCSV4 Purpose: Verify that the ‘ClientSerializer‘ serializes the ‘Client‘ model correctly Priority: 1 Test Coverage Item: Client Serialization Preconditions: A ‘Client‘ instance exists Inputs: Serialize a ‘Client‘ instance using ‘ClientSerializer‘ Expected Results: The serialized data should contain the correct fields: ‘id‘, ‘dni‘, ‘user‘, ‘direction‘, ‘cellphone‘, ‘city‘ Postconditions: N/A

Table 7.124: Test case to verify ‘ClientSerializer‘ serialization

Test Case ID: TCSV5 Purpose: Verify that the ‘ClientSerializer‘ updates a ‘Client‘ instance correctly Priority: 1 Test Coverage Item: Client Update Preconditions: A ‘Client‘ instance exists Inputs: Update the ‘Client‘ instance’s ‘city‘ field using ‘ClientSerializer‘ Expected Results: The ‘city‘ field should be updated to the new value Postconditions: N/A

Table 7.125: Test case to verify ‘ClientSerializer‘ update functionality

182

Test Case ID: TCSV6 Purpose: Verify that the ‘CategorySerializer‘ serializes the ‘Category‘ model correctly Priority: 1 Test Coverage Item: Category Serialization Preconditions: A ‘Category‘ instance exists Inputs: Serialize a ‘Category‘ instance using ‘CategorySerializer‘ Expected Results: The serialized data should contain the correct fields: ‘id‘, ‘name‘, ‘description‘ Postconditions: N/A

Table 7.126: Test case to verify ‘CategorySerializer‘ serialization

Test Case ID: TCSV7 Purpose: Verify that the ‘CategorySerializer‘ updates a ‘Category‘ instance correctly Priority: 1 Test Coverage Item: Category Update Preconditions: A ‘Category‘ instance exists Inputs: Update the ‘Category‘ instance’s ‘description‘ field using ‘CategorySerializer‘ Expected Results: The ‘description‘ field should be updated to the new value Postconditions: N/A

Table 7.127: Test case to verify ‘CategorySerializer‘ update functionality

Test Case ID: TCSV8 Purpose: Verify that the ‘CategorySerializer‘ handles duplicate category names correctly Priority: 2 Test Coverage Item: Category Name Uniqueness Preconditions: A ‘Category‘ instance with ‘name=’UniqueName’‘ exists Inputs: Try to update another ‘Category‘ instance’s ‘name‘ field to ‘UniqueName‘ using ‘CategorySerializer‘ Expected Results: The serializer should be invalid and should contain an error message for the ‘name‘ field Postconditions: N/A

Table 7.128: Test case to verify ‘CategorySerializer‘ name uniqueness validation

183

Test Case ID: TCSV9 Purpose: Verify that the ‘ProductSerializer‘ serializes the ‘Product‘ model correctly Priority: 1 Test Coverage Item: Product Serialization Preconditions: A ‘Product‘ instance exists Inputs: Serialize a ‘Product‘ instance using ‘ProductSerializer‘ Expected Results: The serialized data should contain the correct fields: ‘id‘, ‘name‘, ‘description‘, ‘price‘, ‘quantity‘, ‘category‘, ‘date added‘, ‘local‘, ‘image‘, ‘details‘ Postconditions: N/A

Table 7.129: Test case to verify ‘ProductSerializer‘ serialization

Test Case ID: TCSV10 Purpose: Verify that the ‘ProductSerializer‘ updates a ‘Product‘ instance correctly Priority: 1 Test Coverage Item: Product Update Preconditions: A ‘Product‘ instance exists Inputs: Update the ‘Product‘ instance’s ‘price‘ field using ‘Product- Serializer‘ Expected Results: The ‘price‘ field should be updated to the new value Postconditions: N/A

Table 7.130: Test case to verify ‘ProductSerializer‘ update functionality

Test Case ID: TCSV11 Purpose: Verify that the ‘ProductSerializer‘ handles invalid price values correctly Priority: 2 Test Coverage Item: Product Price Validation Preconditions: A ‘Product‘ instance exists Inputs: Try to update the ‘Product‘ instance’s ‘price‘ field to an invalid value using ‘ProductSerializer‘ Expected Results: The serializer should be invalid and should contain an error message for the ‘price‘ field Postconditions: N/A

Table 7.131: Test case to verify ‘ProductSerializer‘ price validation

184

Test Case ID: TCSV12 Purpose: Verify that the ‘OrderItemSerializer‘ serializes the ‘OrderItem‘ model correctly Priority: 1 Test Coverage Item: OrderItem Serialization Preconditions: An ‘OrderItem‘ instance exists Inputs: Serialize an ‘OrderItem‘ instance using ‘OrderItemSerializer‘ Expected Results: The serialized data should contain the correct fields: ‘product‘, ‘quantity‘ Postconditions: N/A

Table 7.132: Test case to verify ‘OrderItemSerializer‘ serialization

Test Case ID: TCSV13 Purpose: Verify that the ‘OrderItemSerializer‘ updates an ‘OrderItem‘ instance correctly Priority: 1 Test Coverage Item: OrderItem Update Preconditions: An ‘OrderItem‘ instance exists Inputs: Update the ‘OrderItem‘ instance’s ‘quantity‘ field using ‘OrderItemSerializer‘ Expected Results: The ‘quantity‘ field should be updated to the new value Postconditions: N/A

Table 7.133: Test case to verify ‘OrderItemSerializer‘ update functionality

Test Case ID: TCSV14 Purpose: Verify that the ‘OrderItemSerializer‘ handles invalid quantity values correctly Priority: 2 Test Coverage Item: OrderItem Quantity Validation Preconditions: An ‘OrderItem‘ instance exists Inputs: Try to update the ‘OrderItem‘ instance’s ‘quantity‘ field to an invalid value using ‘OrderItemSerializer‘ Expected Results: The serializer should be invalid and should contain an error message for the ‘quantity‘ field Postconditions: N/A

Table 7.134: Test case to verify ‘OrderItemSerializer‘ quantity validation

185

Test Case ID: TCSV15 Purpose: Verify that the ‘OrderSerializer‘ serializes the ‘Order‘ model correctly Priority: 1 Test Coverage Item: Order Serialization Preconditions: An ‘Order‘ instance with an ‘OrderItem‘ exists Inputs: Serialize an ‘Order‘ instance using ‘OrderSerializer‘ Expected Results: The serialized data should contain the correct fields: ‘id‘, ‘client‘, ‘total‘, ‘status‘, ‘date created‘, ‘date update‘, ‘items‘, and the ‘items‘ field should contain the correct product and quantity Postconditions: N/A

Table 7.135: Test case to verify ‘OrderSerializer‘ serialization

Test Case ID: TCSV16 Purpose: Verify that the ‘OrderSerializer‘ creates an ‘Order‘ instance correctly Priority: 1 Test Coverage Item: Order Creation Preconditions: A ‘Client‘ and a ‘Product‘ with sufficient quantity exist Inputs: Create an ‘Order‘ with an item using ‘OrderSerializer‘ and the provided data: {’client’: client.id, ’total’: ’100.00’, ’status’: 2, ’items’: [’product’: product.id, ’quantity’: 2]} Expected Results: The ‘Order‘ instance should be created, and the ‘Product‘ quantity should be updated correctly Postconditions: The ‘Product‘ instance’s quantity should be reduced accordingly

Table 7.136: Test case to verify ‘OrderSerializer‘ creation functionality

186

Test Case ID: TCSV17 Purpose: Verify that the ‘OrderSerializer‘ handles insufficient product quantity correctly Priority: 2 Test Coverage Item: Order Quantity Validation Preconditions: A ‘Client‘ and a ‘Product‘ with insufficient quantity exist Inputs: Try to create an ‘Order‘ with an item using ‘OrderSerializer‘ and the provided data: {’client’: client.id, ’total’: ’100.00’, ’status’: 3, ’items’: [’product’: product.id, ’quantity’: 2]} Expected Results: The serializer should be invalid and should raise a ‘ValidationError‘ Postconditions: N/A

Table 7.137: Test case to verify ‘OrderSerializer‘ quantity validation

Test Case ID: TCSV18 Purpose: Verify that the ‘WishlistItemSerializer‘ serializes the ‘WishlistItem‘ model correctly Priority: 1 Test Coverage Item: WishlistItem Serialization Preconditions: A ‘WishlistItem‘ instance exists Inputs: Serialize a ‘WishlistItem‘ instance using ‘WishlistItemSerializer‘ Expected Results: The serialized data should contain the correct fields: ‘id‘, ‘user‘, ‘product‘, ‘added at‘ Postconditions: N/A

Table 7.138: Test case to verify ‘WishlistItemSerializer‘ serialization

Test Case ID: TCSV19 Purpose: Verify that the ‘WishlistItemSerializer‘ updates a ‘WishlistItem‘ instance correctly Priority: 1 Test Coverage Item: WishlistItem Update Preconditions: A ‘WishlistItem‘ instance exists Inputs: Update the ‘WishlistItem‘ instance’s ‘product‘ field using ‘WishlistItemSerializer‘ Expected Results: The ‘product‘ field should be updated to the new value Postconditions: N/A

Table 7.139: Test case to verify ‘WishlistItemSerializer‘ update functionality

187

Test Case ID: TCSV20 Purpose: Verify that the ‘WishlistItemSerializer‘ handles duplicate wishlist items correctly Priority: 2 Test Coverage Item: WishlistItem Uniqueness Validation Preconditions: A ‘WishlistItem‘ instance with a specific ‘user‘ and ‘product‘ exists Inputs: Try to create another ‘WishlistItem‘ with the same ‘user‘ and ‘product‘ using ‘WishlistItemSerializer‘ Expected Results: The serializer should be invalid and should contain a ‘non field errors‘ entry in the errors Postconditions: N/A

Table 7.140: Test case to verify ‘WishlistItemSerializer‘ uniqueness validation

Test cases for API endpoints

Test Case ID: TCE2E1 Purpose: Verify that the view returns all products correctly Priority: 1 Test Coverage Item: Product View - Get All Products Preconditions: At least one product exists in the database Inputs: Send a GET request to the ‘get all products‘ endpoint Expected Results: The response status should be 200, and the product names should be included in the response data Postconditions: N/A

Table 7.141: Test case to verify retrieval of all products

Test Case ID: TCE2E2 Purpose: Verify that the view returns products filtered by price range correctly Priority: 1 Test Coverage Item: Product View - Filtered Products Preconditions: Products exist in the database with varying prices Inputs: Send a GET request to the ‘get-filtered-products‘ endpoint with ‘price min‘ and ‘price max‘ parameters Expected Results: The response status should be 200, and the returned products should be within the specified price range Postconditions: N/A

Table 7.142: Test case to verify retrieval of filtered products by price range

188

Test Case ID: TCE2E3 Purpose: Verify that the view sends a contact email successfully Priority: 1 Test Coverage Item: Email View - Send Contact Email Preconditions: N/A Inputs: Send a POST request to the ‘send contact email‘ endpoint with the contact details Expected Results: The response status should be 200, and a success message should be included in the response Postconditions: N/A

Table 7.143: Test case to verify sending of contact email

Test Case ID: TCE2E4 Purpose: Verify that the view sends a registration email successfully Priority: 1 Test Coverage Item: Email View - Send Registration Email Preconditions: N/A Inputs: Send a POST request to the ‘send register email‘ endpoint with the registration details Expected Results: The response status should be 200, and a success message should be included in the response Postconditions: N/A

Table 7.144: Test case to verify sending of registration email

Test Case ID: TCE2E5 Purpose: Verify that the login view authenticates a user with valid credentials Priority: 1 Test Coverage Item: Auth View - Login Preconditions: A ‘User‘ instance exists with valid credentials Inputs: Send a POST request to the ‘login‘ endpoint with valid credentials Expected Results: The response status should be 200, and an access token should be included in the response Postconditions: N/A

Table 7.145: Test case to verify successful login

189

Test Case ID: TCE2E6 Purpose: Verify that the login view returns an error with invalid credentials Priority: 1 Test Coverage Item: Auth View - Login Preconditions: A ‘User‘ instance exists with valid credentials Inputs: Send a POST request to the ‘login‘ endpoint with invalid credentials Expected Results: The response status should be 400, and an error message should be included in the response Postconditions: N/A

Table 7.146: Test case to verify login with invalid credentials

Test Case ID: TCE2E7 Purpose: Verify that the registration view registers a new user successfully Priority: 1 Test Coverage Item: Auth View - Register Preconditions: N/A Inputs: Send a POST request to the ‘register‘ endpoint with valid registration data Expected Results: The response status should be 200, and an access token should be included in the response Postconditions: A new ‘User‘ instance should be created in the database

Table 7.147: Test case to verify successful user registration

Test Case ID: TCE2E8 Purpose: Verify that the registration view returns an error when using an existing email Priority: 2 Test Coverage Item: Auth View - Register Preconditions: A ‘User‘ instance with the provided email already exists Inputs: Send a POST request to the ‘register‘ endpoint with an existing email Expected Results: The response status should be 400, and an error message should be included in the response Postconditions: N/A

Table 7.148: Test case to verify registration with existing email

190

Test Case ID: TCE2E9 Purpose: Verify that the logout view logs out a user successfully Priority: 1 Test Coverage Item: Auth View - Logout Preconditions: A user is authenticated Inputs: Send a POST request to the ‘logout view‘ endpoint Expected Results: The response status should be 200, and a success message should be included in the response Postconditions: The user’s session should be terminated

Table 7.149: Test case to verify successful user logout

Test Case ID: TCE2E10 Purpose: Verify that the view returns the correct product by ID Priority: 1 Test Coverage Item: Product Detail View - Get Product by ID Preconditions: A ‘Product‘ instance with a specific ID exists Inputs: Send a GET request to the ‘get product by id‘ endpoint with the product ID Expected Results: The response status should be 200, and the product details should match the expected values Postconditions: N/A

Table 7.150: Test case to verify retrieval of a product by ID

Test Case ID: TCE2E11 Purpose: Verify that the view returns an error when the product ID is not found Priority: 2 Test Coverage Item: Product Detail View - Get Product by ID Preconditions: A ‘Product‘ instance with the provided ID does not exist Inputs: Send a GET request to the ‘get product by id‘ endpoint with a non-existent product ID Expected Results: The response status should be 404, and an error message should be included in the response Postconditions: N/A

Table 7.151: Test case to verify handling of non-existent product ID

191

Test Case ID: TCE2E12 Purpose: Verify that the order creation view creates an order successfully Priority: 1 Test Coverage Item: Order View - Create Order Preconditions: A ‘Client‘ instance and a ‘Product‘ instance with sufficient quantity exist Inputs: Send a POST request to the ‘create order‘ endpoint with valid order data Expected Results: The response status should be 201, and the order details should match the expected values Postconditions: A new ‘Order‘ instance should be created in the database

Table 7.152: Test case to verify successful order creation

Test Case ID: TCE2E13 Purpose: Verify that the order creation view handles insufficient product quantity correctly Priority: 2 Test Coverage Item: Order View - Create Order Preconditions: A ‘Client‘ instance and a ‘Product‘ instance with insufficient quantity exist Inputs: Send a POST request to the ‘create order‘ endpoint with order data requesting more product than is available Expected Results: The response status should be 400, and an error message should be included in the response Postconditions: N/A

Table 7.153: Test case to verify handling of insufficient product quantity in order creation

192

Test Case ID: TCE2E14 Purpose: Verify that the wishlist view adds a product to the wishlist successfully Priority: 1 Test Coverage Item: Wishlist View - Add to Wishlist Preconditions: A ‘Product‘ instance and an authenticated ‘User‘ instance exist Inputs: Send a POST request to the ‘add to wishlist‘ endpoint with the product ID Expected Results: The response status should be 201, and a success message should be included in the response Postconditions: The ‘Product‘ should be added to the user’s wishlist

Table 7.154: Test case to verify successful addition to wishlist

Test Case ID: TCE2E15 Purpose: Verify that the wishlist view handles already existing products in the wishlist correctly Priority: 2 Test Coverage Item: Wishlist View - Add to Wishlist Preconditions: A ‘WishlistItem‘ instance with the same ‘Product‘ and ‘User‘ already exists Inputs: Send a POST request to the ‘add to wishlist‘ endpoint with the product ID Expected Results: The response status should be 200, and an appropriate message should be included in the response Postconditions: The wishlist should remain unchanged

Table 7.155: Test case to verify handling of already existing products in wishlist

193

Test Case ID: TCE2E16 Purpose: Verify that the wishlist view removes a product from the wishlist successfully Priority: 1 Test Coverage Item: Wishlist View - Remove from Wishlist Preconditions: A ‘WishlistItem‘ instance with the specified product and user exists Inputs: Send a POST request to the ‘remove from wishlist‘ endpoint with the product ID Expected Results: The response status should be 200, and a success message should be included in the response Postconditions: The ‘Product‘ should be removed from the user’s wishlist

Table 7.156: Test case to verify successful removal from wishlist

Test Case ID: TCE2E17 Purpose: Verify that the wishlist view handles non-existent products in the wishlist correctly Priority: 2 Test Coverage Item: Wishlist View - Remove from Wishlist Preconditions: The ‘Product‘ does not exist in the user’s wishlist Inputs: Send a POST request to the ‘remove from wishlist‘ endpoint with a non-existent product ID Expected Results: The response status should be 404, and an appropriate error message should be included in the response Postconditions: N/A

Table 7.157: Test case to verify handling of non-existent products in wishlist

Test Case ID: TCE2E18 Purpose: Verify that the user data view returns the correct user data Priority: 1 Test Coverage Item: User Data View - Get User Data Preconditions: An authenticated ‘User‘ instance exists Inputs: Send a GET request to the ‘get-user-data‘ endpoint Expected Results: The response status should be 200, and the user data should match the expected values Postconditions: N/A

Table 7.158: Test case to verify retrieval of user data

194

Test Case ID: TCE2E19 Purpose: Verify that the purchase history view returns the correct purchase history for the user Priority: 1 Test Coverage Item: Purchase History View - Get Purchase History Preconditions: An authenticated ‘User‘ instance with at least one order exists Inputs: Send a GET request to the ‘purchase-history‘ endpoint Expected Results: The response status should be 200, and the purchase history should match the expected values Postconditions: N/A

Table 7.159: Test case to verify retrieval of purchase history

7. 2.3 Acceptance Testing: Frontend

Cypress was used as the primary tool for acceptance testing due to its strong end-to-end testing capabilities. To improve the testing process, the Cypress-Cucumber-Preprocessor plugin was integrated, which allows the implementation of BDD (Behavior Driven Development) principles. This combination gave us a powerful and flexible testing environment, which allowed the writing of clear, human-readable test scenarios in Gherkin syntax, while maintaining the efficiency and speed of Cypress in executing the tests.

The structure of the features used is presented below.

Feature: Cart

Scenario: Add product to cart and checkout Given I am on the product details page When I add the product to the cart And I proceed to checkout Then I should be redirected to the login page if I am not logged in

Scenario: User go to checkout Given I am logged in And I have products in my cart When I proceed to checkout Then I should see the paypal boton And I should see the products to buy

Feature: User Authentication

Scenario: User registers an account

195

Given I visit the registration page When I fill in the registration form with valid details And I submit the registration form Then I should see a success message And I should be able to log in with my new credentials

Scenario: User logs in with valid credentials Given I visit the login page When I enter valid credentials And I submit the login form Then I should be redirected to the homepage And I should see my user profile in the navbar

Scenario: User cannot log in with invalid credentials Given I visit the login page When I enter invalid credentials And I submit the login form Then I should see an error message

Feature: Product Listing

Scenario: View all available products Given I visit the homepage When I navigate to the products section Then I should see a list of all available products And each product should have a title, image, and price

Scenario: View product details Given I am on the products page When I click on a product Then I should see the modal product details page And I should see detailed information about the product And I should see an option to add the product to the wishlist or cart

Feature: Wishlist Management

Scenario: Add a product to the wishlist Given I am logged in And I am on the product details page When I click the "Add to Wishlist" button Then I should see a confirmation message And the product should be added to my wishlist

196

Scenario: View wishlist Given I am logged in When I navigate to my wishlist page Then I should see all the products I have added to my wishlist

7. 2.4 Acceptance Testing: Backend

For the backend of the project, Behave-Django was used as the main tool for acceptance testing, taking advantage of its integration with the Django framework. This tool allowed the implementation of behavior-driven development (BDD) by allowing test scenarios to be written in Gherkin syntax.

The structure of the features used is presented below.

Feature: Contact Us Form

Scenario: Send a contact email When I send a contact email with subject "Inquiry" and message "I need help with my o Then I should receive a "200" status And I should see a confirmation message "Correo enviado exitosamente"

Feature: Error Handling and Validation

Scenario: Attempt to create an order with insufficient product quantity Given a product exists with a quantity of "1" When I attempt to create an order with a quantity of "2" for that product Then I should receive a "400" status And I should see an error message "Insufficient quantity"

Scenario: Attempt to view a product that does not exist When I attempt to view the product with ID "9999" Then I should receive a "404" status And I should see an error message "Product not found"

Scenario: Attempt to register with an already taken email Given a user already exists with the email "existinguser@example.com" When I attempt to register with the email "existinguser@example.com" Then I should receive a "400" status And I should see an error message "Email already exists"

197

Feature: Filtered Product View

Scenario: View filtered products by category Given a category named "Electronics" exists And a product exists with name "Smartphone" in the "Electronics" category When I view products filtered by the "Electronics" category Then I should see the product "Smartphone"

### 7.3 Test Data Requirements

A subset of anonymized production data will be used for testing, excluding sensitive customer information such as credit card details, addresses, or phone numbers. The test team and stakeholders will ensure that the data is “cleaned” and anonymized before use. PayPal’s sandbox mode will be utilized for payment testing, with test accounts configured to simulate various payment scenarios. Test data will be refreshed and validated at the start of each sprint to align with the features being developed and tested.

### 7.4 Test Environment Requirements

The test environment will replicate the production environment, configured with secure logins and restricted access to test data. PayPal’s sandbox mode will be integrated into the test environment to facilitate secure and realistic payment processing tests. Functional and performance testing, including payment workflows, will be carried out in this environment during each sprint to support ongoing development and testing activities.

### 7.5 Test result

Test Results: Front end

The following are the specific test results for the web module frontend of the Ninventario project, documented at the end of the final sprint. All tests passed successfully:

- Test TCUPHC1:Passed

- Test TCUPHC2:Passed

- Test TCOS1:Passed

- Test TCOS2:Passed

- Test TCOS3:Passed

- Test TCPayS1:Passed

- Test TCPayS2:Passed

- Test TCPayS3:Passed

- Test TCSC2:Passed

- Test TCSC1:Passed

- Test TCSC3:Passed

- Test TCWS1:Passed

- Test TCWS2:Passed

- Test TCPS1:Passed

- Test TCPS2:Passed

- Test TCPS3:Passed

- Test TCPS4:Passed

- Test TCPS5:Passed

198

- Test TCAS1:Passed

- Test TCAS2:Passed

- Test TCAS3:Passed

- Test TCAS4:Passed

- Test TCAS5:Passed

- Test TCAS6:Passed

- Test TCAS7:Passed

- Test TCAS8:Passed

- Test TCCC1:Passed

- Test TCCC2:Passed

- Test TCECC1:Passed

- Test TCECC2:Passed

- Test TCECC3:Passed

- Test TCIC1:Passed

- Test TCIC2:Passed

- Test TCIC3:Passed

- Test TCIC4:Passed

- Test TCRPC1:Passed

- Test TCRPC2:Passed

- Test TCRPC3:Passed

- Test TCNC1:Passed

- Test TCNC2:Passed

- Test TCLC1:Passed

- Test TCLC2:Passed

- Test TCLC3:Passed

- Test TCMC1:Passed

- Test TCMC2:Passed

- Test TCMC3:Passed

- Test TCMC4:Passed

- Test TCPGC1:Passed

- Test TCPGC2:Passed

- Test TCPGC3:Passed

- Test TCPGC4:Passed

- Test TCUDC1:Passed

- Test TCUDC2:Passed

- Test TCRC1:Passed

- Test TCRC2:Passed

- Test TCRC3:Passed

- Test TCRC4:Passed

- Test TCRC5:Passed

- Test TCRC6:Passed

- Test TCPSC1:Passed

- Test TCPSC2:Passed

- Test TCPSC3:Passed

- Test TCPSC4:Passed

- Test TCPSC5:Passed

- Test TCPSC6:Passed

- Test TCPSC7:Passed

- Test TCPSC8:Passed

- Test TCPSC9:Passed

- Test TCPSC10:Passed

- Test TCPSC11:Passed

- Test TCConS1:Passed

- Test TCConS2:Passed

- Test TCConS3:Passed

- Test TCSCM1:Passed

- Test TCSCM2:Passed

- Test TCSCM3:Passed

- Test TCSCM4:Passed

- Test TCSCM5:Passed

- Test TCSCM6:Passed

- Test TCSCM7:Passed

- Test TCSCM8:Passed

- Test TCSCM9:Passed

- Test TCSCM10:Passed

- Test TCSCM11:Passed

- Test TCSCM12:Passed

- Test TCSCM13:Passed

- Test TCSCM14:Passed

- Test TCSCM15:Passed

- Test TCLogC1:Passed

- Test TCLogC2:Passed

- Test TCLogC3:Passed

- Test TCWM1:Passed

- Test TCWM2:Passed

- Test TCWM3:Passed

- Test TCCS1:Passed

- Test TCCS2:Passed

- Test TCCS3:Passed

- Test TCCS4:Passed

- Test TCCS5:Passed

- Test TCCS6:Passed

- Test TCUAC1:Passed

- Test TCUAC2:Passed

- Test TCUAC3:Passed

199

The detailed results, including any logs or data captured during these tests, can be reviewed in the test management system.

Figure 7.2: Results of frontend testing

200

Acceptance Testing Results

Figure 7.3: Results of frontend acceptance testing - Cart

Figure 7.4: Results of frontend acceptance testing - Login

201

Figure 7.5: Results of frontend acceptance testing - Product

Figure 7.6: Results of frontend acceptance testing - Wishlist

Test Results: Back end

The following are the specific test results for the web module backend of the Ninventario project, documented at the end of the final sprint. All tests passed successfully:

202

- Test TCCM1:Passed

- Test TCCM2:Passed

- Test TCCM3:Passed

- Test TCCM4:Passed

- Test TCCM5:Passed

- Test TCCM6:Passed

- Test TCCM7:Passed

- Test TCCM8:Passed

- Test TCCM9:Passed

- Test TCCM10:Passed

- Test TCCM11:Passed

- Test TCCM12:Passed

- Test TCCM13:Passed

- Test TCCM14:Passed

- Test TCCM15:Passed

- Test TCCM16:Passed

- Test TCCM17:Passed

- Test TCSV1:Passed

- Test TCSV2:Passed

- Test TCSV3:Passed

- Test TCSV4:Passed

- Test TCSV5:Passed

- Test TCSV6:Passed

- Test TCSV7:Passed

- Test TCSV8:Passed

- Test TCSV9:Passed

- Test TCSV10:Passed

- Test TCSV11:Passed

- Test TCSV12:Passed

- Test TCSV13:Passed

- Test TCSV14:Passed

- Test TCSV15:Passed

- Test TCSV16:Passed

- Test TCSV17:Passed

- Test TCSV18:Passed

- Test TCSV19:Passed

- Test TCSV20:Passed

- Test TCE2E1:Passed

- Test TCE2E2:Passed

- Test TCE2E3:Passed

- Test TCE2E4:Passed

- Test TCE2E5:Passed

- Test TCE2E6:Passed

- Test TCE2E7:Passed

- Test TCE2E8:Passed

- Test TCE2E9:Passed

- Test TCE2E10:Passed

- Test TCE2E11:Passed

- Test TCE2E12:Passed

- Test TCE2E13:Passed

- Test TCE2E14:Passed

- Test TCE2E15:Passed

- Test TCE2E16:Passed

- Test TCE2E17:Passed

- Test TCE2E18:Passed

- Test TCE2E19:Passed

203

Figure 7.7: Results of backend testing - Cart

Acceptance Testing Results

Figure 7.8: Results of backend acceptance testing - Cart

204

### 7.6 Incident report

RegisterComponent Test Failure

Number 3 Short Title RegisterComponent Test Failure System User Registration Module System Version Beta Test ID TCREG1 Test Environment /src/app/pages/register/register.component.ts

Status Open Created by Kevin Roldan Pilozo Date & time: 10/08/2024 Observed by Kevin Roldan Pilozo Date & time: 11/08/2024 Details The test failed because the ‘router.navigate‘ method is not a function, causing a TypeError during the execution of the ‘RegisterComponent‘ onSubmit method. This indicates that the router instance may not be properly initialized or mocked in the testing environment. Observed during Unit Testing

Severity High Priority 1 Risk The failure indicates a critical issue with the user registration process, which could prevent users from successfully navigating through the application after registration. This needs immediate attention to ensure the functionality of the registration flow.

Table 7.160: Details of the RegisterComponent Test Failure.

205

Figure 7.9: RegisterComponent Test Failure

ShoppingCartModal Test Failure

Number 4 Short Title ShoppingCartModalComponent Test Failure System Shopping Cart Module System Version Beta Test ID TCSC1 Test Environment /src/app/pages/shopping-cart-modal/shopping-cartmodal.component.spec.ts Status Open Created by Kevin Rold´an Pilozo Date & time: 10/08/2024 Observed by Kevin Rold´an Pilozo Date & time: 11/08/2024 Details The test failed because the ShoppingCartModalComponent did not delete a product from the cart as expected. The test expected the value 2 to be 1, indicating a mismatch in the number of items or the state of the cart after attempting to delete an item. Observed during Unit Testing

Severity High Priority 1 Risk This issue suggests that the shopping cart may not correctly handle item deletions, leading to a potential accumulation of unwanted items in the cart. This could result in a negative user experience and incorrect order processing if not addressed promptly.

Table 7.161: Details of the ShoppingCartModalComponent Test Failure.

206

Figure 7.10: ShoppingCartModal Test Failure

207

OrderSerializer Test Failure

Number 5 Short Title OrderSerializerTest Failure System Order Processing Module System Version Beta Test ID TCORD2 Test Environment /backend/tests/test serializers.py

Status Open Created by Kevin Rold´an Pilozo Date & time: 11/08/2024 Observed by Kevin Rold´an Pilozo Date & time: 12/08/2024 Details The test ‘test order create insufficient quantity‘ failed because the assertion that the serializer should be invalid when an order is created with insufficient quantity returned ‘True‘ instead of ‘False‘. This indicates that the serializer is not correctly validating the quantity constraints as expected. Observed during Unit Testing

Severity High Priority 1 Risk This issue may allow orders to be processed with insufficient quantities, leading to potential fulfillment issues and customer dissatisfaction. Immediate resolution is necessary to ensure the integrity of the order creation process.

Table 7.162: Details of the OrderSerializerTest Failure.

Figure 7.11: OrderSerializerTes Test Failure

208

Filtered Product View Feature Failure.

Number 6 Short Title Filtered Product View Feature Failure System Product Filtering Module System Version Beta Test ID TCFPV1 Test Environment /tests/acceptance/features/productfiltering feature.feature

Status Open Created by Kevin Rold´an Pilozo Date & time: 11/08/2024 Observed by Kevin Rold´an Pilozo Date & time: 12/08/2024 Details The acceptance test for viewing filtered products by category failed. The test expected to find a product named ”Smartphone” under the ”Electronics” category after applying the filter, but the product was not found. The test verifies that products are correctly displayed when a filter is applied, but the expected product was missing from the filtered results. Observed during Acceptance Testing

Severity Medium Priority 2 Risk This issue may lead to incorrect product listings when users filter products by category, affecting the usability of the product filtering feature. It is important to resolve this issue to ensure accurate and expected behavior in product searches.

Table 7.163: Details of the Filtered Product View Feature Failure.

Figure 7.12: Filtered Product View Feature Failure Failure

209

# 8 Individual Contribution

Name Sections Andr´es Cornejo Abstract, Mobile Development Framework, Coding Standards-Mobile Module, User Manual-Mobile Module, Test Cases-Mobile Module, Deployment Mobile Guide Jorge Mawyin Coding Standars and Coding Standards/PMD for Web Module (Backend-Frontend), Preemptive Error Detection-Mobile Module, Instalation Guide, Web Module Deployment and Appendix G: User Manual - Web Manual Kevin Rold´an SCRUM Evidence,Relevant Architectural Decisions, Web Module Test Documentation Angel Tomal´a Project Context, Coding Standards/PMD for Flutter, Preemptive Error Detection-Mobile Module, Test Cases-Mobile Module, Installation Guide, Software Building - Mobile Apk

210

# 9 Appendix

### 9.1 Appendix A: GitHub Repositories

You can find the repository of this Requirements here: https://github.com/Nintventario-Team/ Requeriments_PRICOTERCORP.git.

You can find the repository of Mobile Module here: https://github.com/Nintventario-Team/ NintventarioApp-beta.git

You can find the repository of Web Module here: https://github.com/Nintventario-Team/ Nintventario-beta

You can find the repository of Communication Report here: https://github.com/ Nintventario-Team/T1.git

### 9.2 Appendix B: Software Building

Mobile APK The mobile app was released on 06/22/2024 as an Alpha version (pre-release) with the Github Actions automation tool and the APK executable can be found at the following link: https://github.com/Nintventario-Team/NintventarioApp-beta/releases/tag/v2

Web Page The website (front and back end) was deployed on 06/22/2024. The backend was deployed with pythonanywhere. https://nintventario.pythonanywhere.com/admin/

The frontend was deployed with firebase. https://nintventario.firebaseapp.com/

### 9.3 Appendix C: Project Presentation Video

To access the project presentation video, which shows a demonstration (in English) of our software system showing the software components in execution and their compliance with the functional and non-functional requirements, access the following link. Also, there is the link of the presentation in PPT for the Project Presentation Video: Presentation.

211

### 9.4 Appendix D: Client Acceptance Letters

9. 4.1 Sprint 1 Acceptance Letter

Figure 9.1: Sprint 1 Acceptance Letter

212

9. 4.2 Sprint 2 Acceptance Letter

Figure 9.2: Sprint 1 Acceptance Letter

213

9. 4.3 Sprint 2 Acceptance Letter

Figure 9.3: Sprint 3 Acceptance Letter

214

9. 4.4 Sprint 4 Acceptance Letter

Figure 9.4: Sprint 4 Acceptance Letter

215

### 9.5 Appendix E: System Deployment Guide WM

9. 5.1 Introduction

The Nintendo website is designed to display and pre-order products online. This guide will walk you through the installation process on Windows 10/11 systems. Please follow the steps carefully to ensure a successful installation.

9. 5.2 System Requirements

Before installing the web, please ensure that your computer meets the following minimum requirements:

Software Requirements:

- Operative system: Windows 10/11.

- Python: Version 3.12.3 or higher.

Make sure you have Python 3.12.3 installed on your system. You can verify it by using the following command: (python –version).

Figure 9.5: Python –Version.

If you don’t have it, or don’t have the correct version, you can download it from the official Python website https://www.python.org/downloads/.

- Node: Version 20.14 or higher.

- Angular CLI: Version 18.0 or higher.

If you don’t have it yet, install Angular CLI globally by running (npm install

- g @angular/cli) in your CMD.

216

Figure 9.6: Angular and Node.js Version.

- XAMPP: Download and install XAMPP from the official XAMPP website https:

//www.apachefriends.org/index.html.

- Disk Space: Make sure you have at least 1 GB of free disk space for the project

and dependencies.

- Version control: Git - Latest stable version.

- Package management: Pip - To handle Python dependencies.

- Virtual Environment (Python): venv or virtualenv to isolate dependencies.

- Version control: Git - Latest stable version.

- Browser: Opera GX, Microsoft Edge, Google Chrome (Dor testing and develop-

ment).

- Others: Visual studio Code for code development and Postman for API Tests.

217

Hardware Requirements:

- CPU: Intel Core i5 (quad-core) or higher / AMD Ryzen 5 or higher

- RAM: It is recommended to have at least 8 GB of RAM. 16 GB recommended.

- Storage: It is recommended to have at least 10 GB of free space.

Network Requirements:

- Internet Connection: Stable internet connection of 10 Mbps or higher.

An internet connection is required to install Python and Node.js dependencies, as well as to download Angular libraries, packages and Xaamp.

9. 5.3 Installation Steps

1. Clone the repository

- Clone the repository https://github.com/Nintventario-Team/Nintventario-beta.

git to your local machine using the following command git clone LINK in CMD.

Figure 9.7: Git clone example.

2. Set up the virtual environment

- Once the repository is cloned, access to the backend directory as follows cd

Nintventario-beta/backend.

Figure 9.8: Backend Path example.

- In the backend folder, create a Python virtual environment by executing:

– On Windows: python -m venv environmentName. Then activate the virtual environment by running ”./environmentName/Scripts/activate”.

218

– On Linux/macOS: source environmentName/bin/activate.

3. Install Django dependencies

- Once you are in the virtual environment, install the requirements.txt file by

running: pip install -r requirements.txt.

- Then, check if you have the following packages by running the command pip

list.

Figure 9.9: Pip List example.

4. Configure the database

- Start XAMPP and make sure the MySQL and Apache servers are running.

219

Figure 9.10: Xampp configuration.

- Go to your browser and put http://localhost/phpmyadmin/ in the search

bar

220

Figure 9.11: Go to PhpMyAdmin.

- Then, create a new database for your project from phpMyAdmin.

221

Figure 9.12: New Database.

Figure 9.13: Creation database example.

5. Configure the Django backend

- Go to the settings.py file in the backend/backend nintventario configu-

222

ration folder.

- Configure the connection to the MySQL database you just created with your

credentials.

Engine: django.db.backends.mysql

Name: Here go the database name that recently create database nintventario

User: For default is root

Password: For default don’t have a password

Host: localhost

Port: Default port is 3306, you can check this in Xampp control panel

Figure 9.14: Credential database example.

- Access to the backend directory as follows cd Nintventario-beta/backend

and activate the virtualvenv by./env/Scripts/activate.

- Perform migrations as running python manage.py makemigrations fol-

lowed by python manage.py migrate.

6. Insert data into MySQL

- Once migrations are executed. In the browser, go to http://localhost/phpmyadmin/

and enter to the database you created database nintventario.

223

Figure 9.15: PhpMyAdmin page.

- Go to the custom user category table, and in the SQL section, execute the

category inserts found in the database nintventario.sql file.

224

Figure 9.16: Select SQL option

Figure 9.17: Category insert

- Repeat the same process for the custom user product table.

225

Figure 9.18: Product insert

7. Configure the Angular frontend

- In another command line, navigate to the Angular frontend folder as follow

cd Nintventario-beta/frontend.

Figure 9.19: Frontend path example.

- Install dependencies by running npm install.

8. Deploy the website locally

- Access to the backend directory as follows cd Nintventario-beta/backend

and activate the virtualvenv by./env/Scripts/activate and run python manage.py runserver to start the Django server.

Figure 9.20: Backend deploy

- In another command line, navigate to the Angular frontend folder as follow

cd Nintventario-beta/frontend and run ng serve -o to start the Angular development server.

226

Figure 9.21: Frontend deploy

- Now you should be able to access the web catalog from your browser by

visiting http://localhost:4200.

### 9.6 Appendix F: Installation Guide MM

9. 6.1 Introduction

The Nintventario app is designed to help users manage their inventories efficiently. This guide will walk you through the installation process on Android devices. Please follow the steps carefully to ensure a successful installation.

9. 6.2 System Requirements

Before installing the app, please ensure that your device meets the following minimum requirements:

- Platform: Android

- Supported Hardware Architectures: x64, Arm32, Arm64

- Supported Android Versions: Android 5.0 (Lollipop, API level 21) to Android

14 (API level 34)

- Storage: 1 GB of available space

- Memory: 2 GB RAM

- Unsupported Android Versions: Android 4.4 (KitKat, API level 20) and ear-

lier

To check your Android version and hardware architecture, follow these steps:

227

1. Go to Settings on your Android device.

2. Scroll down and select About Phone or About Device.

3. Look for Android Version to see your current version.

4. To check your device’s hardware architecture, you may need to install a third-party

app like CPU-Z from the Google Play Store.

9. 6.3 Download Instructions

1. Access the Nintventario app’s release page by visiting the following link: https://

github.com/Nintventario-Team/NintventarioApp-beta/releases/tag/v1.0

2. Click on the Nintventario.apk file to start the download.

3. If you are downloading through a browser on your phone, an alert will appear

indicating that downloading an app from external sources may be harmful. Select Download anyway.

Figure 9.22: APK release in Github.

9. 6.4 Installation Instructions

1. Locate the downloaded Nintventario.apk file in your device’s Downloads folder.

2. Tap on the file to begin the installation process.

3. If prompted, you may need to enable the option to install from Unknown Sources:

- Go to Settings → Security → Install unknown apps.

- Select the app (e.g., your browser) that you used to download the APK.

- Toggle the switch to allow Install unknown apps.

228

Figure 9.23: Activate unknown sources.

9. 6.5 Verification of Installation

1. After installation, check for the Nintventario app icon on your home screen or

app drawer.

2. Tap the icon to open the app.

3. Upon first launch, you may be prompted to grant permissions. Ensure you grant

the necessary permissions for the app to function correctly.

229

Figure 9.24: App installed.

Figure 9.25: App icon.

9. 6.6 Troubleshooting

If you encounter any issues during the installation, here are some common problems and their solutions:

- Problem: Installation fails or the app crashes upon opening.

– Solution: Ensure your device meets the minimum system requirements. Try restarting your device and reinstalling the app.

- Problem: The app icon does not appear after installation.

– Solution: Check if the installation was completed successfully. If not, download and install the APK again.

- Problem: The app requests additional permissions that you are unsure about.

– Solution: Review the permissions carefully and allow those that are essential for the app to operate.

9. 6.7 Support

If you continue to experience issues or have questions, please contact our support team at nintventario@gmail.com for further assistance.

230

### 9.7 Appendix G: User Manual

9. 7.1 Web Manual

User Guide for Using the Django Deployed System in PythonAnywhere

First open your web browser and enter the URL of the Django administration panel through the following link: https://nintventario.pythonanywhere.com/admin/. Once there, you will have the following view:

Figure 9.26: Django administration panel

On the login page, enter your superuser credentials (username and password) that were configured during the initial Django installation. These credentials, at the moment, are the following:

user: adminNintventario@hotmail.com password: admin

Click ”Login” to access the administration panel.

231

Figure 9.27: Django administration panel - Loged

232

Once you’re logged in, you’ll see the following sections in your Django admin panel:

Auth Token In this section we can manage the system tokens

Figure 9.28: Go to Auth Section - Django

Figure 9.29: Auth Section Page - Django

Add: Allows you to create new authentication tokens. These tokens are used to authenticate users to your APIs. To add a token, select ”Add” under the ”Tokens” section, complete the required fields, and save the new token.

233

Figure 9.30: Go to Add Token - Django

Figure 9.31: Add Token Page - Django

Change: View and modify existing authentication tokens. To modify a token, select ”Change” under the ”Tokens” section, browse through the list of tokens, select the one you want to modify, make the necessary changes, and save.

Figure 9.32: Go to Change Token - Django

234

Figure 9.33: Change Token Page - Django

Authentication and Authorization In this section you can interact with the various types of authorization groups in the backend

Figure 9.34: Go to Authentication and Authorization Section - Django

Figure 9.35: Authentication and Authorization Section - Django

235

Add: Allows you to create new user groups. Groups are a way to organize users and assign permissions together. To add a group, select ”Add” under the ”Groups” section, fill out the necessary fields, such as the group name and associated permissions, then save.

Figure 9.36: Go to Add Group - Django

Figure 9.37: Add Group Page - Django

Change: Allows you to view and modify existing user groups. To modify a group, select ”Change” under the ”Groups” section, select the group you want to modify, make the necessary changes, and save.

Figure 9.38: Go to Change Group - Django

236

Figure 9.39: Change Group Page - Django

Custom User Management Here we manage what corresponds to the users that our website will have.

Figure 9.40: Go to Custom User Management Section - Django

Figure 9.41: Custom User Management Section - Django

Add: Allows you to create new users in the system. Here you can define details such

237

as username, password, and assign specific permissions. To add a user, select ”Add” under the ”Users” section, complete the required fields such as username, password, and other user profile details, assign specific permissions as necessary, and save.

Figure 9.42: Go to Add user - Django

Figure 9.43: Add User Page - Django

Change: Allows you to view and modify existing users. To modify a user, select ”Change” under the ”Users” section, find the user you want to modify, make any necessary changes to the profile details or permissions, and save.

238

Figure 9.44: Go to Change User - Django

Figure 9.45: Change Group User - Django

Recent Actions Displays a log of recent actions taken by the currently logged in user. This may include actions such as creating or modifying objects within the administration panel. It is useful for tracking changes and managing your activity within the system.

Figure 9.46: Recent Actions Section - Django

239

User Guide for Navigating and Using the Website

First open your web browser and enter the URL of the web page displayed in Firebase which is the following:

https://nintventario.firebaseapp.com

Once the page loads, users will be on the main interface of our application. Below you will see how to use the functionalities of the website:

Page Navigation Use the navigation menu, located at the top, on the main page to explore different parts of the application.

Figure 9.47: Home Page Web

240

Figure 9.48: Navbar Icons

”Inicio” Here you will find the first visual impression of the website where there is a carousel with promotional banners about the store, below the banner there is a search bar that searches through all the available products and finally there is the featured products section where by clicking on the box on the left you will see the best selling products and the box on the right the most recent products.

241

Figure 9.49: Index page

Productos Being on the products option we will find a drop-down list of the general product categories with their subcategories as follows:

- “Videojuegos”: It is a general category that when pressed directs you to the

video game products section. Its subcategories are: – “Nintendo 3DS”: Link showing video game products for Nintendo 3DS. – “Nintendo Wii”: Link showing video game products for Nintendo Wii. – ”Nintendo Switch”: Link showing video game products for Nintendo Switch. – ”PS1”: Link showing video game products for Playstation 1. – ”PS2”: Link showing video game products for Playstation 2. – ”PS3”: Link showing video game products for Playstation 3. – ”PS4”: Link showing video game products for Playstation 4.

242

– ”PS5”: Link showing video game products for Playstation 5. – ”Xbox One”: Link showing video game products for Xbox one. – ”Xbox 360”: Link showing video game products for Xbox 360.

- “Funko-Pops”: It is a general category that when pressed directs you to the

funko-pops products section. Its subcategories are: – “Heroes”: Link showing funko-pops products from DC comics, their comics, movies and series. – “Marvel”: Link showing funko-pops products from Marvel, their comics, movies and series. – ”Comics”: Link showing funko-pops products from the rest of the comics. – ”Animacion”: Link showing funko-pops products containing animated characters, classic drawings and anime in general. – ”Disney”: Link showing funko-pops products that groups all Disney animated series and movies. – ”Television”: Link showing funko-pops products that groups the main television series. – ”Movies”: Link showing Funko-Pops products that develop all the characters from the best Pop Culture movies.

- ”Consolas”: It is a general category that when pressed directs you to the console

products section. Its subcategories are: – ”Nintendo Switch”: Link showing Nintendo Switch 5 consoles. – ”PS5”: Link showing Playstation 5 consoles.

- ”Art´ıculos”: It is a general category that when pressed directs you to the section

of products that are articles. Its subcategories are: – ”Cables”: Link showing the types of cables offered by the website. – ”Cargadores”: Link showing the types of chargers offered by the website. – “Nintendo 3DS”: Link showing the types of Nintendo 3DS items. – “Nintendo Wii”: Link showing the types of Nintendo Wii items. – ”Nintendo Switch”: Link showing the types of Nintendo Switch items. – ”PS1”: Link showing the types of Playstation 1 items. – ”PS2”: Link showing the types of Playstation 2 items. – ”PS3”: Link showing the types of Playstation 3 items. – ”PS4”: Link showing the types of Playstation 4 items. – ”PS5”: Link showing the types of Playstation 5 items. – ”Tazas”: Link showing the types of cups offered by the website.

243

- ”Otros”: It is a general category that, when pressed, directs you to the section

with the rest of the products offered on the page. Its subcategories are:

Figure 9.50: Dropdown of Products

Steps to go to local page

Step 1: Select local category in the navbar.

244

Figure 9.51: Local page

This section contains information on all available ”Mundo M´agico del Nintendo” stores throughout the country. The name of the shopping center where it is located, the address of the shopping center and the opening hours are indicated.

Steps to go to contact page

Step 1: Select contact category in the navbar.

245

Figure 9.52: Contact page

This section contains the contact information for customer service. It contains the phone numbers for each location and the company’s general email address. It also includes a form so that the customer can contact us for any additional information, questions, suggestions, etc.

Steps to send an email from the contact’s section

Step 1: Enter to contact page.

246

Figure 9.53: Contact form

Steps to search product in the page

Step 1: Go to “Inicio” from https://nintventario.firebaseapp.com

Figure 9.54: Search function

247

Steps to see the best sellers products

Step 1: Go to “Inicio” from https://nintventario.firebaseapp.com

Figure 9.55: Best-Sellers block

248

Figure 9.56: Best-Sellers page

Steps to see the news products

Step 1: Go to “Inicio” from https://nintventario.firebaseapp.com

249

Figure 9.57: News-Products block

250

Figure 9.58: News-Products page

Steps to register in the page

Step 1: Go to the user icon ubicated in the navbar.

251

Figure 9.59: User icon

Figure 9.60: Login from - Change to register form

Step 2: Complete the fields to create your account.

252

Figure 9.61: Register form

Step 3: Check your email for the welcome notification.

Figure 9.62: Email notification

253

Figure 9.63: Register Email

Steps to login in the page

Step 1: You must be registered (Go to that step).

Step 2: Go to the user icon ubicated in the navbar.

254

Figure 9.64: User icon

Figure 9.65: Login form

255

Steps to see the user data

Step 1: You must have login (Go to that step).

Step 2: Go to the user icon ubicated in the navbar.

Figure 9.66: User icon

Figure 9.67: User personal information page

Steps to see the user dataSteps to recover the password

Step 1: You must have an account (Go to that step).

256

Step 2: Go to the user icon ubicated in the navbar.

Figure 9.68: User icon

Figure 9.69: Login page

Step 3: Complete the email field.

257

Figure 9.70: Email confirmation page

Step 4: Go to the email that put in the previous step.

Figure 9.71: Reset password email notification

258

Figure 9.72: Reset password email

Step 5: Complete the fields to change the password.

Figure 9.73: Reset password page

Steps to add a product to the wishlist

Step 1: You must be login (Go to that step).

Step 2: Go to any products section that wish.

259

Figure 9.74: Products dropdown

Step 3: Select the products that want to add in the wishlist.

Figure 9.75: Products page

260

Steps to see the products that are in the wishlist

Step 1: You must be login (Go to that step).

Step 2: Go to the heart icon ubicated in the navbar.

Figure 9.76: Wish-List icon

261

Figure 9.77: Wish-List modal page

Steps to add a product to the shop cart

Step 1: Go to any products section that wish.

262

Figure 9.78: Products dropdown

Step 2: Go to any products section that wish.

Figure 9.79: Products page

263

Steps to see the products that are in the shop cart

Step 1: Go to the shop cart icon ubicated in the navbar.

Figure 9.80: Shop-cart icon

Figure 9.81: Shop-cart modal page

264

Steps to add quantity to the products in the shop cart

Step 1: Open the shop cart (Go to that step).

Step 2: Choose the product of the shop cart that want increase the quantity.

Figure 9.82: Shop-cart modal page - Add quantity

Steps to reduce quantity to the products in the shop cart

Step 1: Open the shop cart (Go to that step).

Step 2: Choose the product of the shop cart that want reduce the quantity.

265

Figure 9.83: Shop-cart modal page - Reduce quantity

Steps to eliminate products from the shop cart

Step 1: Open the shop cart (Go to that step).

Step 2: Choose the product to eliminated.

Figure 9.84: Shop-cart modal page - Eliminate product

266

Step 3: Confirm the product elimination.

Figure 9.85: Alert - Elimination confirmation

Steps to see all products in the shop cart

Step 1: Open the shop cart (Go to that step).

Step 2: Choose the “Mostrar todo” text option.

Figure 9.86: Shop-cart modal page - Show all option

267

Steps to go to the payment page

Step 1: Open the shop cart (Go to that step).

Step 2: Press “Finalizar Compra”.

Figure 9.87: Shop-cart modal page - Finish buy option

268

Figure 9.88: Payment page

Steps to eliminate product from the payment page

Step 1: Go to the payment page (Go to that step).

Step 2: Choose the product from the payment page to eliminate.

269

Figure 9.89: Shop-cart modal page - Eliminate product

Step 3: Confirm the product elimination.

Figure 9.90: Alert - Elimination confirmation

Steps to reserve products

Step 1: Go to the payment page (Go to that step).

Step 2: Select local and payment method.

270

Figure 9.91: Shop-cart modal page - Eliminate product

Step 3: Check your email for the reserve confirmation message.

Figure 9.92: Reserve buy email notification

271

Figure 9.93: Reserve buy email

Steps to see buy history

Step 1: You must have login (Go to that step).

Step 2: Go to the user icon ubicated in the navbar.

272

Figure 9.94: User icon

Figure 9.95: User personal information page

273

Figure 9.96: User buy history page

Steps to see the information of each buy history

Step 1: You must go to the buy history page (Go to that step).

Step 2: Select the order to see the information.

Figure 9.97: User buy history page

274

Figure 9.98: User buy history page - Order information

Steps to see all the products

Step 1: You must go to products section.

275

Figure 9.99: Product section

Steps to see details of a product

Step 1: You must go to products section (Go to that step).

Step 2: Select product.

276

Figure 9.100: Product section - Choose product

277

Figure 9.101: Product detail

Steps to order products by cheaper price

Step 1: You must go to products section (Go to that step).

Step 2: Select cheaper order option.

278

Figure 9.102: Product section - ordered by cheaper price

Steps to order products by expensive price

Step 1: You must go to products section (Go to that step).

Step 2: Select expensive order option.

279

Figure 9.103: Product section - ordered by expensive price

Steps to sort products in alphabetical order A-Z

Step 1: You must go to products section (Go to that step).

Step 2: Select the alphabetical order A-Z option

280

Figure 9.104: Product section - ordered by alphabetical A-Z

Steps to sort products in alphabetical order Z-A

Step 1: You must go to products section (Go to that step).

Step 2: Select the alphabetical order Z-A option.

Figure 9.105: Product section - ordered by alphabetical Z-A

281

Steps to filters any products by price

Step 1: You must go to products section (Go to that step).

Step 2: Select a price filter option.

Figure 9.106: Product section - filtered by price

Steps to filter products by video games

Step 1: You must go to products section (Go to that step).

Step 2: Select video games option in products filter.

282

Figure 9.107: Product section - filtered by video games

Steps to filter products by funko pops

Step 1: You must go to products section (Go to that step).

Step 2: Select funko-pops option in products filter.

283

Figure 9.108: Product section - filtered by funko pops

Steps to filter products by consoles

Step 1: You must go to products section (Go to that step).

Step 2: Select console option in products filter.

284

Figure 9.109: Product section - filtered by console

Steps to filter products by articles

Step 1: You must go to products section (Go to that step).

Step 2: Select articles option in products filter.

285

Figure 9.110: Product section - filtered by articles

Steps to filter products by others

Step 1: You must go to products section (Go to that step).

Step 2: Select others option in products filter.

286

Figure 9.111: Product section - filtered by others

Steps to filter video games by gender or platform

Step 1: You must go to video games products section (Go to that step).

Step 2: Choose the gender or platform filter option.

287

Figure 9.112: Video-games products section

Steps to filter funko pops by category

Step 1: You must go to funko pops products section (Go to that step).

Step 2: Choose the category filter option.

288

Figure 9.113: Funko-pop products section

Steps to filter console by platform

Step 1: You must go to console products section (Go to that step).

Step 2: Choose the platform filter option.

289

Figure 9.114: Console products section

Steps to filter articles by category

Step 1: You must go to articles products section (Go to that step).

Step 2: Choose the category filter option.

290

Figure 9.115: Article products section

Steps to see the footer in every page

Step 1: You must go to the bottom of any screen to find the footer.

291

Figure 9.116: Footer ubication

Steps to see Term and conditions page

Step 1: You must go to footer section (Go to that step).

Step 2: Go to term and conditions option.

292

Figure 9.117: Terms and Conditions ubication

293

Figure 9.118: Terms and Conditions page

This section of the web, accessible from any page via the footer link or the navigation bar, details the rules and policies that govern the use of the site.

- Last Update: The date of the last modification of the terms will always be

displayed, ensuring that users are informed of any recent changes.

- Modifications: It is important for users to periodically review this section, as

the terms may change at any time. Modifications are effective immediately after being posted.

- Website Usage: It specifies that the site must be used only for legal purposes

and in accordance with applicable laws.

- Products and Pricing: This section describes the policies on product availability

and possible price changes.

- Purchases and Payments: Users must provide accurate information when mak-

ing purchases, and rights are reserved regarding order acceptance.

- Intellectual Property: All content on the website is protected under intellectual

property laws.

- Contact Information: Contact details are provided for resolving questions or

issues related to the terms and conditions.

294

For more information or to read the full terms, you can visit the ”Terms and Conditions” section on the website.

Steps to see about page

Step 1: You must go to footer section (Go to that step).

Step 2: Go to about us option.

Figure 9.119: About Us ubication

295

Figure 9.120: About Us page

This section of the web, accessible from any page via the footer link or the navigation bar, details the rules and policies that govern the use of the site.

- Our Story: We are passionate about gaming and geek culture, offering a carefully

curated selection of the latest releases, rare items, and unique products that capture the essence of your favorite franchises.

- Our Mission: Our goal is to bring the magic of the Nintendo world to your hands

with quality and authenticity in every product we offer.

- Connect with Us: Stay connected by exploring our catalog, joining our commu-

nity on social media, and staying updated on our latest news and offers.

For more information, you can visit the ”About Us” section on our website.

Steps to see payment methods page

Step 1: You must go to footer section (Go to that step).

Step 2: Go to payment method option.

296

Figure 9.121: Payment Methods ubication

297

Figure 9.122: Payment Methods page

This section provides an overview of the payment options available in Magical World of Nintendo to make your purchase as smooth as possible.

- Online Payments with Credit Cards: We accept Visa, Mastercard, and Amer-

ican Express credit cards, both domestic and international. Your card will be charged at the time of purchase.

- Online Payments with Debit Cards: We accept Visa, Mastercard, and Amer-

ican Express debit cards, both domestic and international. The charge will be made directly at the time of purchase.

- Online Payments with PayPal: PayPal is a secure and easy way to pay, allow-

ing you to link your account to your credit card, debit card, or bank account. It provides an additional layer of security as your financial information is not shared during transactions.

For more information, you can visit the ”Payment Method” section on our website.

298

Steps to go to facebook page

Step 1: You must go to footer section (Go to that step).

Step 2: Go to facebook page.

Figure 9.123: Footer section - Facebook icon

Steps to go to Instagram page

Step 1: You must go to footer section (Go to that step).

Step 2: Go to Instagram page.

299

Figure 9.124: Footer section - Instagram icon

300

9. 7.2 Mobile Manual

User Manual for Sistem Nintventario Version 1.0

Steps to Access the Home Screen

Figure 9.125: Mobile App

301

Figure 9.126: Mobile App Login

302

Figure 9.127: Mobile App spots of sale

After the step 3 the home is going to be displayed in the following way:

303

Figure 9.128: Mobile App home

304

Steps to Change the Spot of Sale

Figure 9.129: Mobile App spots of sale

305

Figure 9.130: Mobile App Settings

Note: If you want to log out from the system instead of changing the spot of sale, select the Cerrar Sesi´on button, and the system will automatically close your session.

306

Steps to Create an Inventory

Figure 9.131: Mobile App Create an Inventory

IMPORTANT: The application will create the inventory automatically, considering the spot of sale and the time you are working. The screen will display the same list of products as in Contifico. Values of the objects in the list of the inventory: The value of each item is going to appear below the Title of the product, and each product is going to be separated by a line.

307

Figure 9.132: Mobile App

- ID: The barcode of the product.

- Stock Anterior: The stock that should be in the spot of sale at that moment, as

shown in Contifico.

- Stock Actual: The stock at the spot of sale during the inventory.

- Estado: Indicates if the product has already been checked during the inventory.

308

Steps to Save a Draft of the Inventory

Figure 9.133: Mobile App Draft of the Inventory

309

Figure 9.134: Mobile App Draft of the Inventory

310

After you press, the button is going to display the screen:

Figure 9.135: Mobile App Inventory Details

311

Steps to Access a Draft Inventory of a Spot of Sale

Figure 9.136: Mobile Draft Draft Inventory of a Spot of Sale

312

Figure 9.137: Mobile App Draft Inventory of a Spot of Sale

313

Elements of the Draft Inventory

Figure 9.138: Mobile App Elements of the Draft Inventory

- Delete: You can delete a draft by pressing this button.

- Set as Complete: You can set the state of a draft as complete by pressing this

button.

- ID: Unique ID of the draft inventory.

- Encargado: Name of the person who created the inventory.

- Duraci´on: Number of days the inventory took.

- Fecha: Day of creation of the inventory.

- Observaciones: The observations found during the inventory.

314

Steps to Complete an Inventory and Create an Excel of the Inventory

Figure 9.139: Mobile App Create an Excel

315

Figure 9.140: Mobile App Create an Excel

316

Steps to Generate a PDF Report of an Inventory

Figure 9.141: Mobile App PDF Report

The result will be a PDF with all the products that do not match the actual stock and the previous stock.

317

Steps to See the Last Report Generated

Figure 9.142: Mobile App Last Report Generated

318

Figure 9.143: Mobile App Last Report Generated

IMPORTANT: The server hosting the copies of previous reports tends to delete these copies after a period. For greater security, it is recommended to download them to your electronic device.

319

Steps to Work on the Last Inventory You Were Working On

Figure 9.144: Mobile App Last Inventory

320

Figure 9.145: Mobile App Last Inventory

321

Steps to update the quantity of a product.

Figure 9.146: Mobile App Product list

322

Figure 9.147: Mobile App Product management

323

### 9.8 Appendix H: Asana activity schedule

We have sent an invitation to our Software Engineering 2 professor to join our group’s Asana project. This will allow the professor to review the project’s structure and monitor our progress. By joining, the professor can provide feedback and ensure that we are on the right track with our project management and organization.

Figure 9.148: Asana activity schedule

324