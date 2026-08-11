## **DEVELOPMENT REPORT** 

## **for** 

## **Nintventario** 

## **Version 1.0 approved** 

**Prepared by Andr´es Alfredo Cornejo Figueroa Jorde Daniel Mawyin Cabay Kevin Ariel Rold´an Pilozo Angel Alexander Tomal´a Moreno** 

**Team 1** 

**June 26, 2024** 

1 

## **Abstract** 

This document detailed the process undertaken to establish a necessary product for the company ”Pricotercorp S.A.,” a franchise specializing in video games, manga, and other pop culture items. One of the main issues the company faced was inventory management, which became cumbersome when adding, updating, and/or reviewing products. To address this, a proposal was presented to optimize these tasks. Additionally, a process to construct a website was initiated to facilitate remote product visualization for customers, aiming to increase the business’s clientele. The document also discussed the selection of appropriate tools to meet the functional and non-functional requirements of the system, encompassing both the mobile inventory module and the web module. The MoSCoW classification was used for functional requirements, and the Sommerville classification was applied for non-functional requirements. Testing was conducted to ensure system reliability and performance, and static analysis was performed to identify and rectify potential issues in the code. The main client for this project was Joffre Morales, owner of PRICOTERCORP S.A., a company with multiple points of sale in Guayas provinces, currently advertising through Instagram and Facebook. The proposed system was intended to streamline inventory management for employees and provide an enhanced online platform for customers to view and reserve products. 

2 

## **Contents** 

|**1**|**Introduction**|**Introduction**|**10**|
|---|---|---|---|
||1.1|Project context . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|10|
|**2**|**Relevant Architectural Decisions**||**11**|
||2.1|Teamwork Management Tool<br>. . . . . . . . . . . . . . . . . . . . . . . . .|11|
||2.2|Database<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|12|
||2.3|Web Frontend Framework . . . . . . . . . . . . . . . . . . . . . . . . . . .|13|
||2.4|Web Backend Framework<br>. . . . . . . . . . . . . . . . . . . . . . . . . . .|14|
||2.5|Authentication and Access Control Framework<br>. . . . . . . . . . . . . . .|15|
||2.6|Mobile Development Framework<br>. . . . . . . . . . . . . . . . . . . . . . .|16|
||2.7|Coding Standards / PMD Tool for Django . . . . . . . . . . . . . . . . . .|17|
||2.8|Coding Standards Tool for Angular . . . . . . . . . . . . . . . . . . . . . .|18|
||2.9|PMD Tool for Angular . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|19|
||2.10|Coding Standards / PMD Tool for Flutter . . . . . . . . . . . . . . . . . .|20|
|**3**|**SCRUM Evidence**||**21**|
||3.1|Roles Defnition . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|21|
|||3.1.1<br>Product Owner . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|21|
|||3.1.2<br>Scrum Master . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|21|
|||3.1.3<br>Development Team . . . . . . . . . . . . . . . . . . . . . . . . . . .|21|
||3.2|Product Backlog<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|22|
||3.3|Sprint 1 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|24|
|||3.3.1<br>Sprint Backlog . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|24|
|||3.3.2<br>Sprint Review . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|25|
|||3.3.3<br>Sprint Retrospective . . . . . . . . . . . . . . . . . . . . . . . . . .|26|
||3.4|Sprint 2 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|27|
|||3.4.1<br>Sprint Backlog . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|27|
|||3.4.2<br>Sprint Review . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|28|
|||3.4.3<br>Sprint Retrospective . . . . . . . . . . . . . . . . . . . . . . . . . .|28|
||3.5|Sprint 3 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|29|
|||3.5.1<br>Sprint Backlog . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|29|
|||3.5.2<br>Sprint Review . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|30|
|||3.5.3<br>Sprint Retrospective . . . . . . . . . . . . . . . . . . . . . . . . . .|30|
||3.6|Sprint 4 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|31|
|||3.6.1<br>Sprint Backlog . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|31|
|||3.6.2<br>Sprint Review . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|32|
|||3.6.3<br>Sprint Retrospective . . . . . . . . . . . . . . . . . . . . . . . . . .|32|



3 

|**4**|**Coding Standards Documentation**|**Coding Standards Documentation**|**Coding Standards Documentation**|||**33**|
|---|---|---|---|---|---|---|
||4.1|Coding|Standards - Mobile Module . .||. . . . . . . . . . . . . . . . . . . .|33|
|||4.1.1|Naming Convention and Organization . . . . . . . . . . . . . . . .|||33|
|||4.1.2|Formatting and Indentation . .||. . . . . . . . . . . . . . . . . . . .|33|
|||4.1.3|Comments and Documentation||. . . . . . . . . . . . . . . . . . . .|34|
|||4.1.4|Exception Handling / Logging||. . . . . . . . . . . . . . . . . . . .|34|
|||4.1.5|Testing<br>. . . . . . . . . .|. . .|. . . . . . . . . . . . . . . . . . . .|35|
||4.2|Coding|Standards - Web Module|. . .|. . . . . . . . . . . . . . . . . . . .|36|
|||4.2.1|Backend . . . . . . . . . .|. . .|. . . . . . . . . . . . . . . . . . . .|36|
|||4.2.2|Apply code standards - Backend||. . . . . . . . . . . . . . . . . . .|38|
|||4.2.3|Frontend<br>. . . . . . . . .|. . .|. . . . . . . . . . . . . . . . . . . .|40|
|||4.2.4|Apply code standards - Frontend . . . . . . . . . . . . . . . . . . .|||42|
|**5**|**Preemptive **||**Error Detection**|||**46**|
||5.1|Preemptive Error - Mobile Module . .|||. . . . . . . . . . . . . . . . . . . .|46|
|||5.1.1|Backend . . . . . . . . . .|. . .|. . . . . . . . . . . . . . . . . . . .|46|
|||5.1.2|Frontend<br>. . . . . . . . .|. . .|. . . . . . . . . . . . . . . . . . . .|47|
||5.2|Preemptive Error - Web Module||. . .|. . . . . . . . . . . . . . . . . . . .|50|
|||5.2.1|Backend . . . . . . . . . .|. . .|. . . . . . . . . . . . . . . . . . . .|50|
|||5.2.2|Frontend<br>. . . . . . . . .|. . .|. . . . . . . . . . . . . . . . . . . .|50|
|**6**|**Test **|**Cases**||||**54**|
||6.1|Test Cases - Mobile Module . . .||. . .|. . . . . . . . . . . . . . . . . . . .|54|
|||6.1.1|Screen Home Tests . . . .|. . .|. . . . . . . . . . . . . . . . . . . .|54|
|||6.1.2|Screen TabBar Tests . . .|. . .|. . . . . . . . . . . . . . . . . . . .|56|
|||6.1.3|Widget DateSelector Tests|. .|. . . . . . . . . . . . . . . . . . . .|58|
|||6.1.4|SalesSpots Screen Tests .|. . .|. . . . . . . . . . . . . . . . . . . .|59|
||6.2|Test Cases - Web Module . . . .||. . .|. . . . . . . . . . . . . . . . . . . .|60|
|||6.2.1|Frontend Testing . . . . .|. . .|. . . . . . . . . . . . . . . . . . . .|60|
|||6.2.2|Backend Testing<br>. . . . .|. . .|. . . . . . . . . . . . . . . . . . . .|72|
|**7**|**Individual Contribution**|||||**77**|
|**8**|**Appendix**|||||**78**|
||8.1|Appendix A: GitHub Repositories||. .|. . . . . . . . . . . . . . . . . . . .|78|
||8.2|Appendix B: Software Building .||. . .|. . . . . . . . . . . . . . . . . . . .|78|
||8.3|Appendix C: Project Presentation||Video . . . . . . . . . . . . . . . . . . .||78|
||8.4|Appendix D: Client Acceptance Letters|||. . . . . . . . . . . . . . . . . . .|79|
|||8.4.1|Sprint 1 Acceptance Letter|. .|. . . . . . . . . . . . . . . . . . . .|79|
||8.5|Appendix E: System Deployment Guide WM . . . . . . . . . . . . . . . .||||80|
||8.6|Appendix F: Installation Guide MM .|||. . . . . . . . . . . . . . . . . . . .|84|
||8.7|Appendix G: User Manual . . . .||. . .|. . . . . . . . . . . . . . . . . . . .|86|
|||8.7.1|Web Manual<br>. . . . . . .|. . .|. . . . . . . . . . . . . . . . . . . .|86|
|||8.7.2|Mobile Manual . . . . . .|. . .|. . . . . . . . . . . . . . . . . . . .|102|



4 

- 8.8 Appendix H: Asana activity schedule . . . . . . . . . . . . . . . . . . . . . 118 

5 

## **List of Tables** 

|2.1|Comparison of Teamwork Management Tool . . . . . . . . . . . . . . . . .|Comparison of Teamwork Management Tool . . . . . . . . . . . . . . . . .|11|
|---|---|---|---|
|2.2|Comparison of Database . . . . . . . . .|. . . . . . . . . . . . . . . . . . .|12|
|2.3|Options Considered for the Web Frontend Framework<br>. . . . . . . . . . .||13|
|2.4|Options Considered for the Web Backend|Framework . . . . . . . . . . . .|14|
|2.5|Comparison of Authentication and Access Control Options for Django . .||15|
|2.6|Comparison of Mobile Frameworks . . .|. . . . . . . . . . . . . . . . . . .|16|
|2.7|Comparison of Coding Standards Tool for Django . . . . . . . . . . . . . .||17|
|2.8|Comparison of Coding Standards Tools for Angular . . . . . . . . . . . . .||18|
|2.9|Comparison of PMD Tool for Angular .|. . . . . . . . . . . . . . . . . . .|19|
|2.10|Comparison of Coding Standards Tool for Flutter . . . . . . . . . . . . . .||20|
|3.1|Product Backlog<br>. . . . . . . . . . . . .|. . . . . . . . . . . . . . . . . . .|23|
|3.2|Sprint Backlog - Sprint 1<br>. . . . . . . .|. . . . . . . . . . . . . . . . . . .|25|
|3.3|Sprint Backlog - Sprint 2<br>. . . . . . . .|. . . . . . . . . . . . . . . . . . .|28|
|3.4|Sprint Backlog - Sprint 3<br>. . . . . . . .|. . . . . . . . . . . . . . . . . . .|30|
|3.5|Sprint Backlog - Sprint 4<br>. . . . . . . .|. . . . . . . . . . . . . . . . . . .|32|
|6.1|Test cases to verify AppBar title, welcome text, and menu items<br>. . . . .||54|
|6.2|Test cases for various functionalities<br>. .|. . . . . . . . . . . . . . . . . . .|56|
|6.3|Test cases for DateSelectorWidget functionalities . . . . . . . . . . . . . .||58|
|6.4|Test cases for SaleSptosPage functionalities . . . . . . . . . . . . . . . . .||59|
|6.5|Test cases for `AppComponent`<br>. . . . . .|. . . . . . . . . . . . . . . . . . .|60|
|6.6|Test cases for Shared Components<br>. . .|. . . . . . . . . . . . . . . . . . .|61|
|6.7|Test cases for Shared Components: NavbarComponent Case . . . . . . . .||61|
|6.8|Test cases for AuthService . . . . . . . .|. . . . . . . . . . . . . . . . . . .|62|
|6.9|Test cases for ProductService . . . . . .|. . . . . . . . . . . . . . . . . . .|63|
|6.10|Test cases for NewsService . . . . . . . .|. . . . . . . . . . . . . . . . . . .|64|
|6.11|Test cases for UserDetailsComponent . .|. . . . . . . . . . . . . . . . . . .|65|
|6.12|Test cases for ShoppingCartComponent|. . . . . . . . . . . . . . . . . . .|66|
|6.13|Test cases for RegisterComponent<br>. . .|. . . . . . . . . . . . . . . . . . .|67|
|6.14|Test cases for ProductSectionComponent|. . . . . . . . . . . . . . . . . .|68|
|6.15|Test cases for LoginComponent . . . . .|. . . . . . . . . . . . . . . . . . .|69|
|6.16|Test Cases for IndexComponent . . . . .|. . . . . . . . . . . . . . . . . . .|69|
|6.17|Test cases for BlogComponent . . . . . .|. . . . . . . . . . . . . . . . . . .|70|
|6.18|Test cases for Client model<br>. . . . . . .|. . . . . . . . . . . . . . . . . . .|73|
|6.19|Test cases for Serializer validation<br>. . .|. . . . . . . . . . . . . . . . . . .|75|
|6.20|Test cases for API endpoints<br>. . . . . .|. . . . . . . . . . . . . . . . . . .|76|



6 

## **List of Figures** 

|4.1|Confguration of Flake8 tool.<br>. . . . . . . . . . . . . . . . . . . . . . . . .|38|
|---|---|---|
|4.2|Flake8 tool execution result before correct the code.<br>. . . . . . . . . . . .|39|
|4.3|Flake8 tool execution after correct the code. . . . . . . . . . . . . . . . . .|39|
|4.4|Prettier confguration fle. . . . . . . . . . . . . . . . . . . . . . . . . . . .|43|
|4.5|Prettier ignore confguration fle. . . . . . . . . . . . . . . . . . . . . . . .|44|
|4.6|Prettier ignore confguration fle. . . . . . . . . . . . . . . . . . . . . . . .|45|
|5.1|Results of static testing mobile. . . . . . . . . . . . . . . . . . . . . . . . .|47|
|5.2|All rules static testing for mobile app. . . . . . . . . . . . . . . . . . . . .|48|
|5.3|Results of static testing mobile. . . . . . . . . . . . . . . . . . . . . . . . .|49|
|5.4|Confguration of ESlint tool. . . . . . . . . . . . . . . . . . . . . . . . . . .|51|
|5.5|ESlint tool execution result. . . . . . . . . . . . . . . . . . . . . . . . . . .|51|
|5.6|ESlint tool execution after to correct the code.<br>. . . . . . . . . . . . . . .|52|
|5.7|Apex PMD tool execution.<br>. . . . . . . . . . . . . . . . . . . . . . . . . .|53|
|6.1|Results of static testing mobile. . . . . . . . . . . . . . . . . . . . . . . . .|55|
|6.2|Results of testing TabBar Screen. . . . . . . . . . . . . . . . . . . . . . . .|57|
|6.3|Results of testing DateSelector Widget.<br>. . . . . . . . . . . . . . . . . . .|58|
|6.4|Results of testing SaleSpot Screen. . . . . . . . . . . . . . . . . . . . . . .|59|
|6.5|Results of testing Web Frontend. . . . . . . . . . . . . . . . . . . . . . . .|71|
|6.6|Results of testing Web Backend.<br>. . . . . . . . . . . . . . . . . . . . . . .|76|
|8.1|Sprint 1 Acceptance Letter<br>. . . . . . . . . . . . . . . . . . . . . . . . . .|79|
|8.2|Python –Version. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|80|
|8.3|Backend Path example.<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . .|81|
|8.4|Pip List example. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|81|
|8.5|Xampp confguration.<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . .|82|
|8.6|Creation database example. . . . . . . . . . . . . . . . . . . . . . . . . . .|82|
|8.7|Credential database example. . . . . . . . . . . . . . . . . . . . . . . . . .|83|
|8.8|Frontend path example. . . . . . . . . . . . . . . . . . . . . . . . . . . . .|83|
|8.9|APK release in Github.<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . .|84|
|8.10|Activate unknown sources. . . . . . . . . . . . . . . . . . . . . . . . . . . .|85|
|8.11|App installed. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|85|
|8.12|App. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|85|
|8.13|Django administration panel . . . . . . . . . . . . . . . . . . . . . . . . . .|86|
|8.14|Django administration panel - Loged . . . . . . . . . . . . . . . . . . . . .|87|
|8.15|Auth Section - Django . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|88|
|8.16|Add Token - Django . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|88|



7 

|8.17|Change Token - Django|. . . .|. . . . . . . . . . . . . . . . . . . . . . . .|89|
|---|---|---|---|---|
|8.18|Authentication and Authorization Section - Django<br>. . . . . . . . . . . .|||89|
|8.19|Add Group - Django<br>.|. . . .|. . . . . . . . . . . . . . . . . . . . . . . .|90|
|8.20|Change Group - Django|. . . .|. . . . . . . . . . . . . . . . . . . . . . . .|90|
|8.21|Custom User Management Section - Django<br>. . . . . . . . . . . . . . . .|||91|
|8.22|Add User - Django . . .|. . . .|. . . . . . . . . . . . . . . . . . . . . . . .|91|
|8.23|Change User - Django .|. . . .|. . . . . . . . . . . . . . . . . . . . . . . .|92|
|8.24|Recent Actions Section - Django||. . . . . . . . . . . . . . . . . . . . . . .|93|
|8.25|Home Page Web<br>. . . .|. . . .|. . . . . . . . . . . . . . . . . . . . . . . .|94|
|8.26|Best selling products . .|. . . .|. . . . . . . . . . . . . . . . . . . . . . . .|95|
|8.27|Product Details Display|. . . .|. . . . . . . . . . . . . . . . . . . . . . . .|95|
|8.28|Dropdown of Categoriesy|. . .|. . . . . . . . . . . . . . . . . . . . . . . .|96|
|8.29|Example of Categoriesy Section||. . . . . . . . . . . . . . . . . . . . . . . .|97|
|8.30|Blog Section . . . . . . .|. . . .|. . . . . . . . . . . . . . . . . . . . . . . .|97|
|8.31|Login Section . . . . . .|. . . .|. . . . . . . . . . . . . . . . . . . . . . . .|98|
|8.32|Login Demonstration . .|. . . .|. . . . . . . . . . . . . . . . . . . . . . . .|99|
|8.33|User Profle . . . . . . .|. . . .|. . . . . . . . . . . . . . . . . . . . . . . .|99|
|8.34|Registration Section<br>. .|. . . .|. . . . . . . . . . . . . . . . . . . . . . . .|100|
|8.35|Shopping Cart Section .|. . . .|. . . . . . . . . . . . . . . . . . . . . . . .|100|
|8.36|Search Bar<br>. . . . . . .|. . . .|. . . . . . . . . . . . . . . . . . . . . . . .|101|
|8.37|Search Result Example .|. . . .|. . . . . . . . . . . . . . . . . . . . . . . .|101|
|8.38|Mobile App . . . . . . .|. . . .|. . . . . . . . . . . . . . . . . . . . . . . .|102|
|8.39|Mobile Login . . . . . .|. . . .|. . . . . . . . . . . . . . . . . . . . . . . .|103|
|8.40|Sale Spot<br>. . . . . . . .|. . . .|. . . . . . . . . . . . . . . . . . . . . . . .|104|
|8.41|Home picture . . . . . .|. . . .|. . . . . . . . . . . . . . . . . . . . . . . .|105|
|8.42|Home picture Crear inventario||. . . . . . . . . . . . . . . . . . . . . . . .|106|
|8.43|Inventory List . . . . . .|. . . .|. . . . . . . . . . . . . . . . . . . . . . . .|107|
|8.44|Inventory seek option<br>.|. . . .|. . . . . . . . . . . . . . . . . . . . . . . .|108|
|8.45|Object view . . . . . . .|. . . .|. . . . . . . . . . . . . . . . . . . . . . . .|109|
|8.46|Details view . . . . . . .|. . . .|. . . . . . . . . . . . . . . . . . . . . . . .|110|
|8.47|Mobile App Details view|. . . .|. . . . . . . . . . . . . . . . . . . . . . . .|110|
|8.48|Mobile App Report view|. . . .|. . . . . . . . . . . . . . . . . . . . . . . .|111|
|8.49|Mobile App History selection .||. . . . . . . . . . . . . . . . . . . . . . . .|112|
|8.50|Mobile App History view|. . .|. . . . . . . . . . . . . . . . . . . . . . . .|113|
|8.51|Mobile App settings selection .||. . . . . . . . . . . . . . . . . . . . . . . .|114|
|8.52|Mobile App settings view|. . .|. . . . . . . . . . . . . . . . . . . . . . . .|115|
|8.53|Mobile App settings developers||. . . . . . . . . . . . . . . . . . . . . . . .|116|
|8.54|Mobile App logout view|. . . .|. . . . . . . . . . . . . . . . . . . . . . . .|117|
|8.55|Asana activity schedule|. . . .|. . . . . . . . . . . . . . . . . . . . . . . .|118|



8 

## **Revision History** 

|Name|Date|Reason For Changes|Version|
|---|---|---|---|
|1|25/06/2024|Nothing|V1.0|



9 

## **1 Introduction** 

## **1.1 Project context** 

This project revolves around two primary components: a mobile application for inventory management and a web portal for customer interaction. The mobile application will enable the staff at ”Pricotercorp S.A.” to efficiently manage the inventory across all store locations. This includes functionalities for adding new products, updating existing product information, and conducting regular inventory reviews. By streamlining these tasks, the mobile application aims to reduce the time and effort required for effective inventory management. 

The web portal, on the other hand, is designed to enhance the customer experience by providing an online platform where customers can browse and view available products. This portal will categorize products by city, allowing customers to see what is available at each store location. Additionally, detailed product information will be displayed, excluding the product codes to maintain privacy and security. Customers will have the capability to reserve products they are interested in, thereby facilitating a smoother purchase process. 

Both components are crucial to addressing the existing challenges faced by ”Pricotercorp S.A.” in terms of inventory management and customer engagement. The integration of these systems is expected to improve operational efficiency and expand the company’s reach by attracting more customers through an enhanced online presence. 

10 

## **2 Relevant Architectural Decisions** 

In this section, we will document the key architectural decisions made during the project’s development, along with the reasons behind these decisions. This encompasses decisions ranging from the selection of collaborative tools to the choice of programming environments and frameworks for each section that the software covers. 

## **2.1 Teamwork Management Tool** 

It was necessary to select an effective platform for task management, collaboration and project monitoring that would improve team organization in order to optimize communication and facilitate the assignment of responsibilities and thus avoid future problems around the assignment of tasks. To address this, we are considering the following teamwork management tools and their respective features: 

|**Characteristic**|**Asana**|**Trello**|**Jira**|
|---|---|---|---|
|**Ease of Use**|High|High|Medium|
|**Functionality**|Comprehensive|Basic|Comprehensive|
|**Integrations**|Extensive|Limited|Extensive|
|**Scalability**|High|Medium|High|
|**Support**|Good|Good|Excellent|
|**Price**|Various<br>plans,<br>incl. free|Various<br>plans,<br>incl. free|Paid,<br>various<br>plans|



Table 2.1: Comparison of Teamwork Management Tool 

## **Decision:** 

Asana 

## **Justification:** 

It was decided to select Asana for its intuitive and friendly interface that makes it easy to create and assign tasks, manage projects through visual dashboards, and generate reports. Offering a wide range of functionality such as calendars, milestone tracking, integration with third-party tools, and its ability to scale with team needs make Asana an ideal choice for improving operational efficiency and collaboration within the project. To access the planning carried out in Asana for this software project, go to the section 8.8. 

11 

## **2.2 Database** 

There is a need to implement a robust relational database with wide adoption in the industry. To address this, we are considering the following databases and their respective features: 

|features:|||||
|---|---|---|---|---|
|**Characteristic**|**MySQL**|**PostgreSQL**|**SQLite**|**MongoDB**|
|**Database Type**|Relational|Relational|Relational|NoSQL|
|**Transaction**<br>**Support**|Yes|Yes|Yes|No|
|**Compatibility**|High|High|High|Medium|
|**Scalability**|High|High|Low|High(for NoSQL)|
|**Performance**|High|High|Medium|High|
|**Documentation**|Extensive and de-<br>tailed|Extensive and de-<br>tailed|Good|Good|
|**Community**|Large|Large|Large|Large|
|**Ease of Use**|Moderate|Moderate|High|High|



Table 2.2: Comparison of Database 

## **Decision:** 

MySQL 

## **Justification:** 

MySQL was selected for its robustness, widespread industry adoption, transaction support, and high compatibility with various technologies. In addition, the members of our development team are accustomed to this database management system, so we would reduce training and learning time for development in MySQL. 

12 

## **2.3 Web Frontend Framework** 

There is a need to choose a robust and scalable framework for developing Single Page Applications (SPAs). To address this, we are considering the following frameworks and their respective features: 

|**Characteristic**<br>**Angular**<br>**React**<br>**Vue.js**|**Characteristic**<br>**Angular**<br>**React**<br>**Vue.js**|**Characteristic**<br>**Angular**<br>**React**<br>**Vue.js**|**Characteristic**<br>**Angular**<br>**React**<br>**Vue.js**|
|---|---|---|---|
|**Language**|TypeScript|JavaScript|JavaScript|
|**Architecture**|MVC|View library|MVVM|
|**Corporate Support**|High (Google)|High (Facebook)|Medium|
|**Learning Curve**|Moderate|Moderate|Low|
|**Documentation**|Extensive and detailed|Good|Good|
|**Community**|Large|Large|Growing|
|**Performance**|High|High|High|



Table 2.3: Options Considered for the Web Frontend Framework 

## **Decision:** 

Angular 

## **Justification:** 

Angular was chosen due to its robust ecosystem, corporate support from Google, and its ability to handle complex and scalable applications. Furthermore, our development team already has experience in building web applications with this framework, which will save us time in TypeScript training and navigating the Angular ecosystem. 

13 

## **2.4 Web Backend Framework** 

Need to select an efficient and secure backend framework for the rapid development of web applications, with the capacity to handle large volumes of data and offer a high level of security.To address this, we are considering the following frameworks and their respective features: 

|**Characteristic**|**Django**|**Express.js**|**Laravel**|**Ruby on Rails**|
|---|---|---|---|---|
|**Language**|Python|JavaScript|PHP|Ruby|
|**MySQL**<br>**8.0**<br>**Connectivity**|Yes,<br>additional<br>libs|Yes, npm MySQL<br>lib|Yes, .env confg|Yes, mysql12 gem|
|**Scope**|Large-scale apps|Lightweight apps<br>& APIs|Medium-sized<br>web apps|Startup,<br>small<br>web apps|
|**History**<br>**Man-**<br>**agement**|Sessions<br>or<br>log-<br>ging|Routes,<br>middle-<br>ware, logging|Logging system|Logging system|
|**Strengths**|Scalable, Built-in<br>ORM, Admin in-<br>terface|Lightweight,<br>Flexible, Fast dev|Elegant<br>syntax,<br>PHP ease|Rapid dev, Con-<br>vention over con-<br>fg|
|**Weaknesses**|Python<br>may<br>be<br>slower|Fewer built-in fea-<br>tures|Potential<br>perfor-<br>mance hit|Response<br>time<br>may lag|



Table 2.4: Options Considered for the Web Backend Framework 

## **Decision:** 

Django 

## **Justification:** 

Django was chosen for its low learning cost, robust MTV architecture, and its ability to handle secure and scalable web applications. The extensive documentation and the large community of developers are not an important factor since our development team lacks knowledge about the use of this bakeend framework. Additionally, its rich ecosystem of libraries and integration with popular technologies facilitate efficient development and deployment of complex web applications. 

14 

## **2.5 Authentication and Access Control Framework** 

For our web application, we are looking for an efficient and secure authentication framework that is capable of handling token-based authentication, guaranteeing secure access and providing an easy integration process with our selected backend, Django. To address this, we are considering the following options: 

|**Characteristic**|**Django**<br>**Simple**<br>**JWT**|**DRF JWT**|**Django OAuth**<br>**Toolkit**|
|---|---|---|---|
|**Functionality**|JWT auth|JWT auth|OAuth2 auth|
|**Language**|Python|Python|Python|
|**Integration**|Django auth|DRF|Django, OAuth2|
|**Token Types**|Access, Refresh|Access, Refresh|OAuth2 tokens|
|**Token Management**|Create,<br>Verify,<br>Refresh|Create,<br>Verify,<br>Refresh|Create,<br>Verify,<br>Refresh|
|**Security**|High,<br>Customiz-<br>able|High|OAuth2 standard|
|**Docs**<br>**and**<br>**Commu-**<br>**nity**|Extensive, Large|Good, Active|Extensive, Active|
|**Strengths**|Simple,<br>Secure,<br>Scalable|Easy, DRF sup-<br>port|Comprehensive,<br>Flexible|
|**Weaknesses**|Needs<br>JWT<br>knowledge|Limited to DRF|Complex setup|



Table 2.5: Comparison of Authentication and Access Control Options for Django 

## **Decision:** 

Django Simple JWT 

## **Justification:** 

Django Simple JWT was chosen for its strong integration with the Django authentication system, its ability to handle secure token-based authentication, and support for access and refresh tokens. Its simplicity of setup, ability to customize token management features, comprehensive documentation provided, and community support make it easy to quickly develop and implement secure authentication mechanisms in our Django application. 

15 

## **2.6 Mobile Development Framework** 

There is a need for a framework to develop efficient native mobile applications for iOS and Android with a code base that shares similarities between these mobile systems. To address this, we are considering the following frameworks and their respective features: 

|**Characteristic**|**Kotlin**|**Flutter**|**React Native**|**Ionic**|
|---|---|---|---|---|
|**Learning Curve**|Low|Moderate|Moderate|Moderate|
|**MySQL**<br>**8.0**<br>**Connectivity**|Requires<br>JDBC,<br>Ktor|REST APIs|Axios for REST|REST APIs|
|**Scope**|Mobile, backend|Mobile|Mobile|Mobile, web|
|**History**<br>**Man-**<br>**agement**|Moderate|Moderate|High|High|
|**Strengths**|Java<br>interoper-<br>ability,<br>modern<br>syntax, security|Productivity, na-<br>tive<br>UI,<br>strong<br>Google support|Community,<br>multi-platform<br>support|Web-friendly,<br>acceptable<br>per-<br>formance|
|**Weaknesses**|Smaller<br>commu-<br>nity, compilation<br>time|Development<br>stage,<br>resource<br>usage|Performance<br>issues,<br>native<br>plugins|Reliance on plug-<br>ins, lower perfor-<br>mance|



Table 2.6: Comparison of Mobile Frameworks 

## **Decision:** 

Flutter 

## **Justification:** 

We decided to select Flutter for its high performance, corporate support from Google, and its ability to develop native applications for multiple platforms with a single code base, which would simplify the work done by the development team. Also, having a moderate learning curve, it will not take many resources to train those in charge of the mobile application on the operation of the essential and necessary features of Fluuter to carry out this software project. 

16 

## **2.7 Coding Standards / PMD Tool for Django** 

There is a need to implement consistent coding standards and improve code quality in our Django backend section of the web module to facilitate maintenance, reduce errors and improve code readability. To address this, we are considering the following frameworks and their respective features: 

|**Characteristic**|**Flake8**|**Pylint**|**Black**|
|---|---|---|---|
|**Language Supported**|Python|Python|Python|
|**Coding Style**|PEP 8|PEP 8, PEP 257|Code formatter|
|**Ease of Use**|High|Medium|High|
|**Confgurability**|High|High|Low|
|**Documentation**|Extensive and de-<br>tailed|Extensive and de-<br>tailed|Good|
|**Integration**<br>**with**<br>**CI/CD**|Easy|Easy|Easy|
|**Community**|Large|Large|Large|
|**Performance**|High|Medium|High|



Table 2.7: Comparison of Coding Standards Tool for Django 

## **Decision:** 

Flake8 

## **Justification:** 

Flake8 was chosen for its ability to verify compliance with PEP 8 coding conventions, detect errors, and improve Python code quality effectively. Its easy configuration and ability to easily integrate with development environments ensure a smooth implementation. For a more detailed explanation of the choice of this Coding Standards tool for Django, go to the Figure 5.1.2. 

17 

## **2.8 Coding Standards Tool for Angular** 

There is a need to implement consistent coding standards to improve the quality of the code in our project in the web section with Angular and maintain consistency and facilitate collaboration between the development team members assigned to this module. To address this, we are considering the following coding standards tool for Angular and their respective features: 

|**Characteristic**|**ESLint**|**TSLint**|**Prettier**|
|---|---|---|---|
|**Language Supported**|JavaScript, Type-<br>Script|TypeScript|JavaScript, Type-<br>Script|
|**Coding Style**|Confgurable|Confgurable|Confgurable|
|**Ease of Use**|High|High|High|
|**Confgurability**|High|High|high|
|**Documentation**|Extensive and de-<br>tailed|Extensive and de-<br>tailed|Extensive and de-<br>tailed|
|**Integration**<br>**with**<br>**CI/CD**|Easy|Easy|Easy|
|**Community**|Large|Medium|Large|
|**Performance**|High|High|High|



Table 2.8: Comparison of Coding Standards Tools for Angular 

## **Decision:** 

Prettier 

## **Justification:** 

Prettier was selected due to its ability to enforce a consistent coding style across the entire codebase automatically. Its opinionated nature removes the burden of configuration and debate over style preferences, allowing developers to focus more on coding rather than formatting. The tool’s extensive documentation, ease of use, and seamless integration with CI/CD pipelines make Prettier a powerful choice for improving code quality and ensuring a consistent development environment in Angular projects. For a more detailed explanation of the choice of this Coding Standards tool for Angular, go to the subsection 4.2.4. 

18 

## **2.9 PMD Tool for Angular** 

There is a need to implement consistent coding standards and static code analysis to enhance the quality of the code in our project and maintain a high level of consistency across different modules. This also facilitates collaboration between the development team members. To address this, we are considering the PMD tool for static code analysis and its respective features: 

|**Characteristic**|**ESLint**|**TSLint**|**Apex PMD**|
|---|---|---|---|
|**Language Supported**|JavaScript, Type-<br>Script|TypeScript|JavaScript, Type-<br>Script|
|**Coding Style**|Confgurable|Confgurable|Confgurable|
|**Ease of Use**|High|High|Medium|
|**Confgurability**|High|High|Medium|
|**Documentation**|Extensive and de-<br>tailed|Extensive and de-<br>tailed|Good|
|**Integration**<br>**with**<br>**CI/CD**|Easy|Easy|Easy|
|**Community**|Large|Medium|Medium|
|**Performance**|High|High|High|



Table 2.9: Comparison of PMD Tool for Angular 

## **Decision:** 

ESLint 

## **Justification:** 

ESLint was selected due to its ability to verify and enforce custom coding rules, as well as style conventions and best practices in TypeScript. Its extensive configurability, support for plugins and the possibility of integrating with other libraries make ESLint a powerful tool to improve code quality, reduce errors, ensuring consistent and efficient development in Angular projects. For a more detailed explanation of the choice of this Coding Standards tool for Angular, go to the paragraph 5.2.1. 

19 

## **2.10 Coding Standards / PMD Tool for Flutter** 

|**Characteristic**|**Dart Analyzer**|**Flutter**<br>**Ana-**<br>**lyzer**|**Linter**|
|---|---|---|---|
|**Language Supported**|Dart|Dart, Flutter|Dart|
|**Coding Style**|PEP 8|PEP<br>8,<br>Flutter<br>Best Practices|PEP 8|
|**Ease of Use**|High|Medium|Medium|
|**Confgurability**|High|Medium|High|
|**Documentation**|Extensive and de-<br>tailed|Extensive and de-<br>tailed|Extensive and de-<br>tailed|
|**Integration**<br>**with**<br>**CI/CD**|Easy|Easy|Easy|
|**Community**|Large|Large|Large|
|**Performance**|High|Medium|High|



Table 2.10: Comparison of Coding Standards Tool for Flutter 

## **Decision:** 

Dart Analyzer 

## **Justification:** 

Dart Analyzer provides a high degree of configurability, enabling fine-tuning of analysis rules to meet the specific needs of a project. Also, is easy to use and configure, allowing for quick integration into both new and existing projects. Its simplicity makes it accessible to both novice and experienced developers. For a more detailed explanation of the choice of this Coding Standards tool for Angular, go to the subsection 5.1.2. 

20 

## **3 SCRUM Evidence** 

## **3.1 Roles Definition** 

## **3.1.1 Product Owner** 

JOFFRE MORALES MENDOZA was selected as the Product Owner due to his deep understanding of both customer requirements and the company, PRICOTERCORP S.A. He will be responsible for creating and managing the product backlog, maximizing its value, and guiding the team’s work. Additionally, he will make decisions on the functionalities to be implemented in each iteration. 

## **3.1.2 Scrum Master** 

CORNEJO FIGUEROA ANDRES ALFREDO was appointed as the Scrum Master because of his extensive knowledge and experience in the Scrum agile methodology. His main role will be to ensure that the Scrum team follows established principles and practices, assist the team in adopting and understanding Scrum, and remove obstacles. He will facilitate Scrum meetings and shield the team from external distractions. 

## **3.1.3 Development Team** 

Due to the team’s small size, all members will be responsible for project development: TOMALA MORENO ANGEL ALEXANDER, MAWYIN CABAY JORGE DANIEL, ROLDAN PILOZO KEVIN ARIEL, and CORNEJO FIGUEROA ANDRES ALFREDO. Their task will be to deliver product increments at the end of each sprint, turning backlog items into potentially shippable product increments. 

21 

## **3.2 Product Backlog** 

Functioning as a strategic roadmap, the Product Backlog not only aligns our team with stakeholder expectations but also facilitates adaptability to shifting market dynamics. In this concise exposition, we explore the integral role the Product Backlog plays in guiding our development. 

|**ID**|**Product Backlog Item**|**Priority**|**Initial**<br>**Esti-**<br>**mate of Ef-**<br>**fort (Hours)**|
|---|---|---|---|
|**MM-01**|**Mobile M.**As an inventory section employee, I want to im-<br>prove stock management at Pricotercorp S.A. by being able<br>to view the updated stock of products in each establishment,<br>including information on items stored in the warehouse, to<br>request what is needed in case of stockouts in a specifc store.|1|24|
|**MM-02**|**Mobile M.** As an inventory area employee, I want the ap-<br>plication to ofer me the option to register a product using a<br>code or QR that directly identifes the product to facilitate<br>the registration of new products.|1|26|
|**WM-01**|**Web M.** As a user, I want each product to have a detailed<br>description, including features, technical specifcations, and<br>relevant details to make an informed decision.|1|28|
|**WM-02**|**Web M.**As an administrator, I want the products shown to<br>users to be directly related to those we have in the inventory<br>to avoid inconsistencies when selling products.|1|22|
|**MM-03**|**Mobile M.**As a system administrator, I want any change in<br>the quantity of products in the inventory to be automatically<br>and instantly refected on the web interface to provide a<br>complete user experience.|2|9|
|**MM-04**|**Mobile M.** As a system administrator, I want to be able<br>to manage who can access the action log history in the in-<br>ventory to keep the registration system secure.|2|23|
|**WM-03**|**Web M.** As an administrator, I want to provide clear and<br>easy-to-understand resources to help beginner users navigate<br>the platform.|2|6|
|**MM-05**|**Mobile M.**As an administrator, I want the system to show<br>me images and key features of each of the products available<br>in the inventory to facilitate the review and efcient man-<br>agement of relevant product information.|3|16|



22 

|**MM-06**|**Mobile M.** As a system administrator, I want the ability<br>to export the history of actions taken in the inventory in<br>a format that allows for review and external analysis for<br>decision-making purposes.|3|15|
|---|---|---|---|
|**WM-04**|**Web M.**As a user, I want to experience a smooth purchas-<br>ing process from product selection to transaction completion<br>to avoid any complications during the payment process for<br>one or more products.|3|25|
|**WM-05**|**Web M.**As a user, I want to manage my account efciently<br>and access personalized functions to improve my shopping<br>experience.|3|48|
|**MM-07**|**Mobile M.** As an inventory area employee, I want auto-<br>complete functionalities to expedite the process of register-<br>ing new products.|4|20|
|**MM-08**|**Mobile M.** As a system administrator, I want a tool that<br>allows me to easily search and flter the history of actions<br>taken on inventory products to better identify changes made<br>in the records.|4|26|
|**MM-09**|**Mobile M.** As a decision-making team member, I want<br>the system to display the inventory fow, highlighting prod-<br>ucts with higher and lower movement frequency to facilitate<br>decision-making by providing key information about prod-<br>uct management.|4|22|
|**WM-06**|**Web M.**As a user, I want to flter among diferent products<br>on the screen by categories and subcategories to have fewer<br>elements on the screen.|4|12|
|**WM-07**|**Web M.** As a user, I want to search among all products by<br>name, type, or brand to easily fnd a product.|4|20|



Table 3.1: Product Backlog 

23 

## **3.3 Sprint 1** 

This sprint will focus on establishing the foundations of the inventory management system and enhancing the user experience on Pricotercorp S.A.’s mobile platform. Additionally, we will develop the initial views of the website, incorporating various key interfaces and functionalities for product display and search. 

## **3.3.1 Sprint Backlog** 

|**Sprint 1**|**Sprint 1**|**Sprint 1**|**Sprint 1**|**Sprint 1**|**Sprint 1**|
|---|---|---|---|---|---|
|**Start Date:**<br>05/20/2024||**Final Date:** 06/09/2024||**Total Efort:**68||
|||||||
|**ID**|**Product Backlog Item**|**Priority**|**Sprint Task**|**Volunteer**|**Estimated**<br>**Efort**<br>**(Hours)**|
|**MM-**<br>**01**|**Mobile M.** As an inventory<br>section employee, I want to<br>improve stock management<br>at Pricotercorp S.A. by being<br>able to view the updated<br>stock of products in each<br>establishment, including<br>information on items stored<br>in the warehouse, to request<br>what is needed in case of<br>stockouts in a specifc store.|1|Interface displaying dif-<br>ferent establishments|Andr´es<br>Cornejo|9|
||||Implementation of Dis-<br>play Functionality|Angel<br>Tomal´a|7|
|**WM-**<br>**01**|**Web M.** As a user, I want<br>each product to have a de-<br>tailed description, including<br>features, technical specifca-<br>tions, and relevant details to<br>make an informed decision.|1|Design of the User In-<br>terface,<br>main<br>section,<br>and the product section.|Kevin<br>Roldan|15|
|**MM-**<br>**05**|**Mobile M.** As an adminis-<br>trator, I want the system to<br>show me images and key fea-<br>tures of each of the products<br>available in the inventory|3|Interface<br>displaying<br>products with features<br>and image integration|Andr´es<br>Cornejo|7|
|**WM-**<br>**07**|**Web M.** As a user, I want to<br>search among all products by<br>name, type, or brand to easily<br>fnd a product.|4|Query Management in<br>the Backend connected<br>to the database.|Kevin<br>Rold´an|10|



24 

|**WM-**<br>**07**|**Web M.** As a user, I want to<br>search among all products by<br>name, type, or brand to easily<br>fnd a product.|4|Interface<br>Design<br>and<br>Search<br>Results<br>Han-<br>dling.|Jorge<br>Mawyin|8|
|---|---|---|---|---|---|
|**WM-**<br>**06**|**Web M.** As a user, I want<br>to flter among diferent prod-<br>ucts on the screen by cat-<br>egories and subcategories to<br>have fewer elements on the<br>screen.|4|Implementation of fl-<br>tering functionality.|Jorge<br>Mawyin|12|



Table 3.2: Sprint Backlog - Sprint 1 

## **3.3.2 Sprint Review** 

**Date:** June 09, 2024 **Duration:** 1 hour 

**Assistants:** Scrum Team (Developers, Scrum Master, Product Owner), normally employed in charge of inventory 

## **Description of Meeting Objectives** 

This meeting aimed to present the first preview of the developed system, focusing mainly on the frontend section of both modules: the web module and the mobile module. We focused on validating with the stakeholder in charge of the inventory whether the layout of the content on the screen and the location of the various basic features of the mobile application were intuitive and met the established requirements. The same was done for the web section, ensuring that it aligned with the defined expectations and needs. 

## **Stakeholder Feedback** 

- ”We consider that the layout of certain elements in the mobile version could be optimized to improve the user experience since certain sections look very busy and are a little difficult to identify their function at a glance” 

- ”Some elements of the mobile application could be rearranged to facilitate faster access to the main functions.” 

- ”The placement of key features in the web application meets our expectations and the color distribution chosen to represent our business very well” 

- ”We need to make sure the app is fully compatible with all major browsers.” 

25 

## **Decisions Made** 

- We will review the layout of items in the mobile application to enhance userfriendliness. 

- We will conduct additional tests to ensure that the website is error-free across major browsers. 

## **Sprint approval** 

To review the acceptance letter corresponding to sprint 1 you can go to the appendix subsection 8.4.1 

## **3.3.3 Sprint Retrospective** 

**Date:** June 09, 2024 

**Duration:** 1 hour 

**Assistants:** Scrum Team (Developers, Scrum Master, Product Owner) 

## **Sprint Successes** 

- We successfully completed all tasks assigned for this sprint without any complications regarding deadlines. 

## **Sprint errors** 

- There were some communication issues that initially confused the team about the tasks assigned to each member at the beginning of the sprint. 

- Task allocation was uneven at times, leading to instances where development team members had periods without assigned activities. 

## **Identification of aspects to improve** 

- Improve communication among team members to prevent future issues affecting product quality or delivery dates. 

- Discuss how tasks are assigned at the beginning of each sprint and how to manage periods when team members have significant downtime to avoid conflicts within the group. 

26 

## **3.4 Sprint 2** 

In Sprint 2, the team will focus on enhancing system security, improving user experience, and refining the functionality of the mobile application. For the website, the goals are to develop user account management and to implement the first part of the purchasing process, which includes the journey from product selection to the shopping cart. 

## **3.4.1 Sprint Backlog** 

|**Sprint 2**|**Sprint 2**|**Sprint 2**|**Sprint 2**|**Sprint 2**|**Sprint 2**|
|---|---|---|---|---|---|
|**Start Date:**<br>06/10/2024||**Final Date:** 06/30/2024||**Total Efort:**70||
|||||||
|**ID**|**Product Backlog Item**|**Priority**|**Sprint Task**|**Volunteer**|**Estimated**<br>**Efort**<br>**(Hours)**|
|**MM-**<br>**04**|**Mobile M.** As a system<br>administrator, I want to be<br>able to manage who can<br>access the action log history<br>in the inventory to keep the<br>registration system secure.|2|Designing the Adminis-<br>tration Interface for the<br>Inventory System|Angel<br>Tomal´a|8|
||||Implement<br>authentica-<br>tion system|Angel<br>Tomal´a|6|
||||Access control and log-<br>ging system for system<br>access|Andr´es<br>Cornejo|9|
|**WM-**<br>**03**|**Web M.** As an administra-<br>tor, I want to provide clear<br>and<br>easy-to-understand<br>re-<br>sources to help beginner users<br>navigate the platform.|2|Review<br>of<br>compliance<br>with<br>human-computer<br>interaction<br>criteria<br>in<br>the catalog and shop-<br>ping section.|Jorge<br>Mawyin|6|
|**WM-**<br>**04**|**Web M.** As a user, I want<br>to experience a smooth pur-<br>chasing process from product<br>selection to transaction com-<br>pletion to avoid any complica-<br>tions during the payment pro-<br>cess for one or moreproducts.|3|Shopping<br>Cart<br>Func-<br>tionality|Kevin<br>Rold´an|12|
|**MM-**<br>**07**|**Mobile M.** As an inventory<br>area employee, I want<br>auto-complete functionalities<br>to expedite the process of<br>registering new products.|4|Implementing logic for<br>autocomplete|Andr´es<br>Cornejo|12|
||||Interface for the new<br>product<br>registration<br>section|Angel<br>Tomal´a|8|



27 

|**WM-**<br>**05**|**Web M.** As a user, I want to<br>manage my account efciently<br>and access personalized func-<br>tions to improve my shopping<br>experience.|3|Designing<br>the<br>logging<br>system<br>and<br>account<br>management interface.|Jorge<br>Mawyin|9|
|---|---|---|---|---|---|



Table 3.3: Sprint Backlog - Sprint 2 

## **3.4.2 Sprint Review** 

This section cannot be filled out at this time because Sprint 2 is still in process. Once the sprint has concluded, the results of the Sprint Review will be documented, including demonstrations of completed work and feedback received from stakeholders. 

## **3.4.3 Sprint Retrospective** 

The Sprint Retrospective for Sprint 2 has not happened yet, as the sprint is currently in progress. This section will be completed after the completion of the sprint, with a summary of discussions about what worked well, what can be improved, and next steps. 

28 

## **3.5 Sprint 3** 

The goal of this sprint is to integrate new functionalities for both the mobile application and the website. We will focus on implementing technologies that simplify product registration and management, ensuring inventory information is accurate and up-todate. Additionally, we will enhance critical processes for the user experience, such as online payment management, and add personalization features to user accounts, allowing for better profile management and tracking of purchase history. 

## **3.5.1 Sprint Backlog** 

|**Sprint 3**|**Sprint 3**|**Sprint 3**|**Sprint 3**|**Sprint 3**|**Sprint 3**|
|---|---|---|---|---|---|
|**Start Date:**<br>07/01/2024||**Final Date:** 07/21/2024||**Total Efort:**77||
|||||||
|**ID**|**Product Backlog Item**|**Priority**|**Sprint Task**|**Volunteer**|**Estimated**<br>**Efort**<br>**(Hours)**|
|**MM-**<br>**02**|**Mobile M.** As an inventory<br>area employee, I want the<br>application to ofer me the<br>option to register a product<br>using a code or QR that<br>directly identifes the product<br>to facilitate the registration<br>of new products.|1|Integration of the QR<br>code scanner.|Angel<br>Tomal´a|10|
||||Validation of the QR<br>code and data storage.|Andr´es<br>Cornejo|6|
|**WM-**<br>**02**|**Web**<br>**M.**<br>As<br>an<br>adminis-<br>trator, I want the products<br>shown to users to be directly<br>related to those we have in<br>the inventory to avoid incon-<br>sistencies when selling prod-<br>ucts.|1|Implement stock valida-<br>tions and display logic.|Kevin<br>Rold´an|10|
|**WM-**<br>**04**|**Web M.** As a user, I want<br>to experience a smooth pur-<br>chasing process from product<br>selection to transaction com-<br>pletion to avoid any complica-<br>tions during the payment pro-<br>cess for one or moreproducts.|3|Implementation of pay-<br>ment gateway on the<br>web|Kevin<br>Rold´an|9|



29 

|**MM-**<br>**05**|**Mobile M.** As an adminis-<br>trator, I want the system to<br>show me images and key fea-<br>tures of each of the products<br>available in the inventory|3|Database<br>query<br>and<br>presentation<br>of<br>key<br>features|Kevin<br>Rold´an|9|
|---|---|---|---|---|---|
|**WM-**<br>**05**|**Web M.** As a user, I want to<br>manage my account<br>efciently and access<br>personalized functions to<br>improve my shopping<br>experience.|3|Implementing the pro-<br>fle editing functional-<br>ity.|Andr´es<br>Cornejo|9|
||||Implementing<br>custom<br>functions and recording<br>purchase history.|Jorge<br>Mawyin|10|
||||Confguring custom no-<br>tifcation options.|Jorge<br>Mawyin|7|
||||Implementing the wish-<br>list feature.|Angel<br>Tomal´a|7|



Table 3.4: Sprint Backlog - Sprint 3 

## **3.5.2 Sprint Review** 

This section cannot be completed yet, as we have not reached Sprint 3. The Sprint Review is planned and will be documented once the sprint is completed, detailing the results and feedback obtained. 

## **3.5.3 Sprint Retrospective** 

We have not yet reached the Sprint Retrospective for Sprint 3. This section will be filled out after the conclusion of the sprint, including an analysis of the lessons learned and improvement opportunities identified. 

30 

## **3.6 Sprint 4** 

In this final sprint, the team will focus on integrating the latest key functionalities into the inventory system, with the primary task being the automatic synchronization of inventory changes with the web interface. Additionally, they will refine the sections dedicated to administrators that display the product flow within the inventory and streamline decision-making processes. This sprint aims to enhance inventory visibility and management, as well as provide advanced tools for informed decision-making. 

## **3.6.1 Sprint Backlog** 

|**Sprint 4**|**Sprint 4**|**Sprint 4**|**Sprint 4**|**Sprint 4**|**Sprint 4**|
|---|---|---|---|---|---|
|**Start Date:**<br>07/22/2024||**Final Date:** 08/11/2024||**Total Efort:**72||
|||||||
|**ID**|**Product Backlog Item**|**Priority**|**Sprint Task**|**Volunteer**|**Estimated**<br>**Efort**<br>**(Hours)**|
|**MM-**<br>**03**|**Mobile**<br>**M.**<br>As<br>a<br>system<br>administrator,<br>I<br>want<br>any<br>change<br>in<br>the<br>quantity<br>of<br>products<br>in<br>the<br>inventory<br>to be automatically and in-<br>stantly refected on the web<br>interface to provide a com-<br>plete user experience.|2|Integration of the web-<br>site with the inventory<br>system|Andr´es<br>Cornejo|9|
|**MM-**<br>**08**|**Mobile M.** As a system<br>administrator, I want a tool<br>that allows me to easily<br>search and flter the history<br>of actions taken on inventory<br>products to better identify<br>changes made in the records.|4|Implementation<br>of<br>Search<br>and<br>Filtering<br>Functionality|Andr´es<br>Cornejo|10|
||||Implementation of the<br>Inventory Action Log|Angel<br>Tomal´a|8|
||||Roles and Permissions<br>Management|Angel<br>Tomal´a|8|
|**MM-**<br>**09**|**Mobile M.** As a<br>decision-making team<br>member, I want the system<br>to display the inventory fow,<br>highlighting products with<br>higher and lower movement<br>frequency to facilitate<br>decision-making by providing<br>key information about<br>product management.|4|Design of the User In-<br>terface section with ex-<br>clusive access for ad-<br>ministrators.|Jorge<br>Mawyin|10|
||||Utilize inventory change<br>logs to identify product<br>fow and store them in a<br>section for future refer-<br>ence.|Kevin<br>Rold´an|12|



31 

|**MM-**<br>**06**|**Mobile M.** As a system<br>administrator, I want the<br>ability to export the history<br>of actions taken in the<br>inventory in a format that<br>allows for review and<br>external analysis for<br>decision-making purposes.|3|Implementation of the<br>Exporter<br>in<br>multiple<br>formats|Kevin<br>Rold´an|8|
|---|---|---|---|---|---|
||||User Interface and Ac-<br>cess Control for Inven-<br>tory Change History|Jorge<br>Mawyin|7|



Table 3.5: Sprint Backlog - Sprint 4 

## **3.6.2 Sprint Review** 

The Sprint Review for Sprint 4 cannot be filled out at this time, as this sprint is planned but has not yet started. Once the sprint is completed, the results and feedback from the review will be documented. 

## **3.6.3 Sprint Retrospective** 

We haven’t reached Sprint 4 yet, so this section will be completed after its completion. A summary of the Sprint Retrospective will be included, addressing what has been learned and proposed improvements for future sprints. 

32 

## **4 Coding Standards Documentation** 

Coding standards are sets of rules and conventions designed to guide the process of writing code in a software development project. These guidelines establish common practices that help improve the readability, consistency, and maintainability of the code. 

## **4.1 Coding Standards - Mobile Module** 

## **4.1.1 Naming Convention and Organization** 

## **Variables** 

Use meaningful and descriptive names for variables, following Dart naming conventions like camelCase. Group related variables together within classes or functional components. 

## **Classes** 

Name classes using PascalCase, starting with a noun or noun phrase that describes the class’s purpose (e.g., UserProfile, HttpService). Consider organizing related classes into separate files or directories. 

## **Widgets** 

Name widgets using PascalCase, reflecting their role in the UI hierarchy (e.g., HomePage, LoginForm). Organize widget files based on their location in the app’s navigation structure. 

## **Functions/Methods** 

Name functions and methods using camelCase, emphasizing action verbs or descriptive phrases (e.g., calculateTotal, fetchUserData). Keep related functions together within classes or functional components. 

## **Directories** 

Organize files into logical directories based on functionality or feature sets (e.g., screens/, models/, utils/). Keep the directory structure flat to avoid deep nesting. 

## **4.1.2 Formatting and Indentation** 

## **Indentation Style** 

Use spaces for indentation with a standard width (typically 2 or 4 spaces). Ensure consistent indentation throughout the codebase. 

33 

## **Line Length** 

Limit lines to a reasonable length (100 in this module) to enhance readability. Break long lines into multiple lines when necessary. 

## **Brace Placement** 

Place opening braces on the same line as control structures and function declarations. Use consistent brace placement for clarity. 

## **4.1.3 Comments and Documentation** 

## **Inline Comments** 

Use comment sparingly to explain complex logic or clarify non-obvious code. Focus on explaining ”why” rather than ”what” if the code is self-explanatory. 

## **Function/Method Comments** 

Document functions and methods using Dartdoc comments, including descriptions, parameter types, and return types. Provide usage examples when appropriate. 

## **Class Documentation** 

Document classes with Dartdoc comments, describing their purpose, properties, and usage. Include relevant details about class behavior and relationships. 

## **File-Level Documentation** 

Provide an overview of the file’s contents and purpose in a comment at the top of the file. Summarize its role within the app and any important information about its contents. 

## **File-Level Documentation** 

Use tools like Dartdoc to generate API documentation from code annotations automatically. 

## **4.1.4 Exception Handling / Logging** 

## **Exception Types** 

Define custom exceptions for specific error conditions if necessary, ensuring they provide meaningful information about the error. Use built-in exceptions for general error handling. 

## **Error Messages** 

Craft clear and informative error messages that help developers diagnose and troubleshoot issues. Include relevant context and information about the error’s cause. 

## **Logging Levels** 

Use logging libraries like logger to log messages at different levels (e.g., debug, info, warning, error). Adjust the log level based on the severity and importance of the message. 

34 

## **4.1.5 Testing** 

## **Test File Naming** 

Name test files using the same name as the file being tested, suffixed with ~~t~~ est.dart (e.g., widget test.dart, api ~~s~~ ervice ~~t~~ est.dart). 

## **Test Case Naming** 

Name test cases descriptively to communicate their purpose and expected behavior (e.g., testSignInSuccess, testCalculateTotalWithDiscount). 

## **Test Structure** 

Organize tests into logical groups based on functionality or feature sets. Use setUp and tearDown methods to set up and tear down test environments as needed. 

## **Assertions** 

Write assertions to verify expected outcomes and behavior. Use expressive matchers provided by testing frameworks like flutter ~~t~~ est to enhance readability and clarity. 

35 

## **4.2 Coding Standards - Web Module** 

## **4.2.1 Backend** 

Below are the codes standard used in our project in the backend section. To learn more about the features used, visit the following link about python code standards. 

## **Code Lay-out** 

## **Indentation** 

Four spaces should be used per indentation level. Continuation lines should align wrapped elements either vertically using Python’s implicit line joining inside parentheses, brackets and braces, or using a hanging indent. 

## **Tabs vs. Spaces** 

Spaces should be the preferred indentation method.Tabs should be used solely to remain consistent with code that is already indented with tabs. 

## **Maximum Line Length** 

Avoid lines longer than 79 characters. 

## **Blank Lines** 

Surround top-level function and class definitions with two blank lines. Method definitions inside a class are surrounded by a single blank line. 

## **Imports** 

Imports should usually be on separate lines. 

Imports are always put at the top of the file, just after any module comments and docstrings, and before module globals and constants. 

Imports should be grouped in the following order: 

1. Standard library imports. 

2. Local application/library specific imports. 

## **String quotes** 

In Python, single-quoted strings and double-quoted strings are the same, so we use bouth. 

## **Whitespace in Expressions and Statements** 

Unnecessary white spaces will be avoided in the following situations: 

- Immediately inside parentheses, brackets or braces. 

- Between a trailing comma and a following close parenthesis. 

36 

- Immediately before a comma, semicolon, or colon. 

- Immediately before the open parenthesis that starts the argument list of a function call. 

- Immediately before the open parenthesis that starts an indexing or slicing. 

- More than one space around an assignment (or other) operator to align it with another. 

## **Comments** 

Block comments generally consist of one or more paragraphs built out of complete sentences, with each sentence ending in a period. The comments should be clear and easily to understand. 

Comments should be complete sentences. The first word should be capitalized, unless it is an identifier that begins with a lower case letter. 

## **Inline comments** 

An inline comment is a comment on the same line as a statement. Inline comments should be separated by at least two spaces from the statement. They should start with a # and a single space. 

## **Naming conventions** 

The naming conventions of Python’s library are a bit of a mess, so we’ll never get this completely consistent – nevertheless, here are the currently recommended naming standards. 

## **Classes** 

Class names should be nouns and use with the first letter of each internal world capitalized convention. Try to keep the class names simple and descriptive. 

## **Function and Variable Names** 

Function names should be lowercase, with words separated by underscores as necessary to improve readability. 

## **Method Names and Instance Variables** 

Use the function naming rules: lowercase with words separated by underscores as necessary to improve readability. 

37 

## **4.2.2 Apply code standards - Backend** 

## **Flake8 for Django** 

Flake8 was chosen as the linter tool for the Django project due to its ability to combine multiple static analysis tools into one solution. Unlike other linter tools, Flake8 integrates Pyflakes, pycodestyle (formerly pep8), and McCabe, providing comprehensive coverage to detect errors and improve Python code quality. 

## **Flake8 Configuration** 

To configure Flake8 for an Django project, we create a file called ( `setup.cfg` ) at the root of the project and define the Flake8 rules according to our code standards. 

Figure 4.1: Configuration of Flake8 tool. 

This configuration is made with our coding standards. 

- `max-line-length = 79` : This setting specifies the maximum allowed line length in the code. 

- `exclude` : This option specifies directories and files to exclude from Flake8’s linting process. In our case we ignore the files that django created by himself and we don’t edit them like: ’app.py’, ’modules.py’, ’admind.py’, etc. 

38 

- `per-file-ignores` : This option allows for the specification of per-file exceptions to certain Flake8 rules. In this case, we decided to ignore the ’models.py’ and ’urls.py’ profiles since some lines in those files generated a 501 error (line too long), but these lines could not be modified as they needed all the characters they have. 

These Flake8 configurations are designed to enforce coding standards and best practices, promoting code readability, consistency, and maintainability throughout the project. 

## **Flake8 tool execution result before correct the code** 

Figure 4.2: Flake8 tool execution result before correct the code. 

**Description of Errors:** The most common code standard errors we found were: 

- **E261** : This error indicates that there are at least two spaces before inline comment. To resolve this error, we align the comment with the code. 

- **E501** : This error indicates that a line is too long according to the configured maximum line length. To fix this error, we considered breaking the line into multiple shorter lines. 

- **E302** : This error indicates that there are too many blank lines after a function or class definition. To resolve this error, we remove the extra blank lines to adhere to the project’s coding standards. 

## **Flake8 tool execution result after correct the code** 

Figure 4.3: Flake8 tool execution after correct the code. 

39 

## **4.2.3 Frontend** 

Below are the code standards used in our project in the frontend section. To learn more about the features used, visit the following link about Angular Coding Style Guide and Best Practices. 

## **Project Structure** 

Maintain a consistent folder structure to improve code organization and facilitate collaboration. Organize files logically, separating components, services, modules and other resources into dedicated directories. (e.g., `src/app` , `src/assets` , `src/app/interfaces` , `src/app/pages` , `src/app/services` ). 

## **Angular CLI** 

Use the Angular CLI (Command Line Interface) for creating projects, generating components, services, modules, and more. The CLI enforces best practices, reduces human error, and provides a standardized approach to project setup. 

## **Modular Architecture** 

Adopt a modular approach by breaking your application into smaller, reusable modules. Each module should have a well-defined purpose and responsibility. This promotes code separation, re-usability, and easier maintenance. 

## **Naming Conventions** 

Use a descriptive and consistent naming conventions for files, classes, variables, and functions. This improves the readability of the code and facilitates collaborative work. 

## **Modules and Component** 

Module and component names should be in PascalCase and end with `Module` . Example: `UserProfileModule` . 

## **Services** 

Service names should be in PascalCase and end with `Service` . Example: `UserService` . 

## **Component Structure** 

Components should be organize with a consistent structure, including template, styles, and TypeScript file. This separation improves code readability and encourages the use of the Component-Driven Development approach. 

## **File Naming** 

File names should be in kebab-case (lowercase with hyphens). Example: `user-profile.component.ts` . 

40 

## **Code Layout** 

## **Indentation** 

Two spaces should be used per indentation level. 

## **Maximum Line Length** 

Avoid lines longer than 120 characters. 

## **Blank Lines** 

Separate related code blocks with a blank line to improve readability. 

## **Component Structure** 

## **Template and Style Files** 

Use separate HTML/CSS files for templates if they exceed 3 lines. 

## **Inline Templates and Styles** 

Allowed only for very simple components with few lines of HTML or CSS. 

## **Imports** 

Imports should be grouped in the following order: 

1. Angular imports (e.g., `@angular/core` ). 

2. External libraries. 

3. Internal project modules. 

## **String Quotes** 

Single quotes ( `’’` ) should be used for string literals. 

## **Whitespace in Expressions and Statements** 

Unnecessary white spaces should be avoided in the following situations: 

- Immediately inside parentheses, brackets, or braces. 

- Between a trailing comma and a following close parenthesis. 

- Immediately before a comma, semicolon, or colon. 

41 

## **Comments** 

Comments should be added when: 

- The code is complex and may be hard to understand for someone who didn’t write it. 

- You’re using a non-obvious approach to solve a problem or a workaround for a known issue. 

## **Single-line Comments** 

In JavaScript, single-line comments begin with two forward slashes //. They should be use for brief explanations. 

## **Multi-line Comments** 

Multi-line comments in JavaScript start with /* and end with */. They should be use for longer descriptions. 

## **Angular’s Inline Template Comments** 

In Angular, can use HTML comments (start with _<_ `!--` and end with `--` _>_ ) within component templates. 

## **Comment Style Guidelines** 

Comments should have this general style guidelines: 

- Comment have to start with a capital letter. 

- Use proper grammar and punctuation. 

- Keep comments concise and to the point. 

## **Version Control** 

## **Commit Messages** 

Follow a clear convention for commit messages (e.g., `Conventional Commits` ). 

## **4.2.4 Apply code standards - Frontend** 

## **Prettier Tool for angular** 

We chose to use Prettier as our code standardization tool for our Angular project for several reasons. Firstly, Prettier ensures consistency in code formatting, making collaboration and code comprehension among team members easier. Additionally, by automating formatting according to predefined rules, it saves developers time and reduces style conflicts within the team. Its easy integration into the development workflow was also a significant factor in our decision. 

42 

## **Prettier configuration** 

To configure Prettier for an Angular project, you create a file at the root of the project and define the Prettier rules according to your code standards. 

Figure 4.4: Prettier configuration file. 

This configuration is made with our coding standards. 

- **singleQuote: true:** Ensures the use of single quotes for string literals, promoting consistency in the code-base. 

- **semi: false:** Disables the insertion of semicolons at the end of statements, reducing visual clutter and adhering to a common style preference. 

- **tabWidth: 2:** Sets the width of each tab to 2 spaces, promoting readability and consistency in indentation. 

- **printWidth: 120:** Specifies the maximum line length before Prettier wraps the code, improving readability and preventing horizontal scrolling. 

- **trailingComma: ”all”:** Includes trailing commas in object literals and arrays, making it easier to add or remove items without modifying adjacent lines. 

- **bracketSpacing: true:** Enforces spacing within object literals, enhancing code clarity and consistency. 

43 

- **jsxBracketSameLine: false:** Forces JSX closing brackets to be placed on a new line, improving readability by separating tags from their content. 

- **htmlWhitespaceSensitivity: ”ignore”:** Ignores white-space in HTML files, ensuring consistent formatting regardless of white-space variations. 

- **endOfLine: ”lf”:** Specifies LF (line feed) as the line ending character, ensuring cross-platform compatibility. 

- **arrowParens: ”avoid”:** Avoids unnecessary parentheses around single-parameter arrow function arguments, improving code readability. 

## **Files ignore** 

Automatically generated files, which underwent no changes, were ignored. 

Figure 4.5: Prettier ignore configuration file. 

## **Prettier tool result** 

Prettier applies the specified changes from the .prettierrc file to all files not listed in the .prettierignore file. To execute Prettier, the command (npm run format) is used. 

44 

Figure 4.6: Prettier ignore configuration file. 

45 

## **5 Preemptive Error Detection** 

## **5.1 Preemptive Error - Mobile Module** 

## **5.1.1 Backend** 

## **Pylint for Python** 

The tool for the static analysis of the mobile application backend was Pylint since it not only helps to detect errors, but its scope ranges from coding convention to detecting logical errors and improving code readability. In addition, it is one of the most used tools for static analysis for python development, so it allows you to establish any rule that is necessary. 

## **Features and Typical Issues Detected:** 

- **Comprehensive Code Analysis:** Pylint performs a thorough analysis of your Python code, checking for errors, enforcing coding standards, and detecting potential bugs. 

- **PEP 8 Compliance:** Pylint helps ensure that your code adheres to the PEP 8 style guide, which is the de facto coding standard for Python. 

- **Detects Code Smells:** Pylint identifies code smells like duplicate code, long methods, and deeply nested loops, which can help you refactor and improve your code. 

- **Documentation and Support:** Pylint has comprehensive documentation and an active community, providing support and resources to help you get the most out of the tool. 

## **Configuration** 

The following rules represent various aspects of code styling, naming conventions, line length, incorrect imports, and other best practices by Pylint. 

- **W1514-unspecified-encoding** This warning occurs when the open function is used without explicitly specifying the encoding parameter. It’s recommended to specify an encoding to avoid potential issues with file reading/writing, especially when dealing with non-ASCII characters. 

- **W0105-pointless-string-statement** This warning indicates that there is a string statement that is not being used in any way. In Python, placing a string in the 

46 

middle of the code without assigning it to a variable or using it in any way is pointless and can be removed. 

- **C0114-missing-module-docstring** This convention message indicates that the module is missing a docstring at the top. A module docstring should describe the purpose and contents of the module. 

- **C0411-wrong-import-order** This convention message indicates that the import order is incorrect. According to PEP 8, imports should be grouped in the following order: standard library imports, related third-party imports, and local application/library-specific imports. 

- **C0301-line-too-long** This convention message indicates that a line exceeds the maximum allowed length. The default maximum length is 100 characters. 

- **C0103-invalid-name** his convention message indicates that a variable, function, or constant name does not conform to naming conventions. For example, constants should be in UPPER CASE, variables and functions should be in lower ~~c~~ ase ~~w~~ ith ~~-~~ underscores, and classes should be in CapitalizedWords. 

## **Tool Execution Results** 

The errors found in the code written to date, according to the rules defined above, were as follows. 

Figure 5.1: Results of static testing mobile. 

After Pylint displays errors and violations of code standards based on the rules that were chosen, that code was corrected to enforce and maintain these standards. 

## **5.1.2 Frontend** 

## **Dart Analyzer for Flutter** 

Using Dart Analyzer for static analysis offers several advantages over other tools. One of the main benefits is its deep integration with the Dart language itself. 

47 

**Features and Typical Issues Detected:** 

- **Code Quality and Standards Enforcement:** Dart Analyzer helps ensure that your code adheres to established coding standards and best practices. 

- **Improved Maintainability:** Static analysis helps in maintaining a clean and readable codebase. 

- **Integration with Development Tools:** Dart Analyzer integrates seamlessly with various development environments and CI/CD pipelines. 

## **Configuration** 

The following rules represent various aspects of code styling, naming conventions, line length, incorrect imports, and other best practices by Dart Analyzer. 

- **always** ~~**d**~~ **eclare return types:** This rule enforces that all functions and methods must explicitly declare their return types. This improves code readability and helps avoid potential issues with type inference. 

- **prefer** ~~**c**~~ **onst** ~~**c**~~ **onstructors:** This rule suggests using const constructors whenever possible. Using const constructors can improve performance by creating a compile-time constant and reducing the memory footprint. 

- **prefer** ~~**f**~~ **inal** ~~**f**~~ **ields:** This rule encourages marking fields as final if they are not reassigned after their initial assignment. This ensures immutability and makes the code easier to understand and maintain. 

Figure 5.2: All rules static testing for mobile app. 

48 

## **Tool Execution Results** 

The errors found in the code written to date, according to the rules defined above, were as follows. 

Figure 5.3: Results of static testing mobile. 

After Dart Analyzer displays errors and violations of code standards based on the rules that were chosen, that code was corrected to enforce and maintain these standards. 

49 

## **5.2 Preemptive Error - Web Module** 

## **5.2.1 Backend** 

## **Flake8 tool** 

To ensure the quality and consistency of code in our Django project, we utilized Flake8. This tool combines several useful functionalities for static code analysis in Python, including error detection, compliance with coding standards, and identification of cyclomatic complexity. By integrating Flake8 into our workflow, we were able to detect and address issues from early stages of development, ensuring that our code is clean, readable, and easy to maintain. Therefore, Flake8 already covers code standards and PMD. 

## **5.2.2 Frontend** 

## **ESLint for Angular** 

ESLint was selected for the Angular project due to its flexibility and extensibility. ESLint is a popular tool for analyzing JavaScript and TypeScript code and is particularly known for its ability to be customized through configurations and plugins. Compared to other tools like JSHint or JSLint, ESLint offers greater configurability and a wide range of rules that can be tailored to the specific needs of the project. 

## **Features and Typical Issues Detected:** 

- **Syntax Errors:** ESLint can detect syntax errors in JavaScript/TypeScript code, helping to prevent runtime errors. 

- **Best Practices:** Ensures the code follows best development practices, such as recommending the use of `===` instead of `==` to avoid comparison errors. 

- **Code Style Consistency:** Enforces consistent coding style, such as the use of single or double quotes, bracket placement, and semicolon usage. 

- **Complexity Issues:** Similar to Flake8, ESLint can measure the cyclomatic complexity of JavaScript/TypeScript code, identifying overly complex functions and suggesting refactorings. 

- **Usage of Variables and Functions:** ESLint detects variables and functions that are declared but not used, as well as variables used before being defined, helping to eliminate dead code and prevent errors. 

## **Configuration** 

In the ESLint configuration file ( `.eslintrc.json` ), the following settings have been specified to maintain code quality: 

- `"parser"` : This setting specifies the parser to be used by ESLint for TypeScript files. 

50 

- `"extends"` : This option extends the recommended configurations provided by `@typescript-eslint` and `@angular-eslint` plugins. 

- `"rules"` : This section defines specific ESLint rules and their configurations. 

Figure 5.4: Configuration of ESlint tool. 

## **Tool Execution Results** 

Figure 5.5: ESlint tool execution result. 

51 

## **Description of Errors:** 

The most common code standard errors we found were: 

- **@typescript-eslint/no-unused-vars** : This error indicates that there are unused variables in the TypeScript code. To resolve this error, we remove the unused variables. 

- **@typescript-eslint/no-explicit-any** : This error indicates the use of the ‘any‘ type, which can lead to type safety issues in TypeScript. To fix this error, we avoid using the ‘any‘ type and use more specific interfaces. 

- **no-var** : This error indicates the use of the ‘var‘ keyword to declare variables, which is discouraged in modern JavaScript/TypeScript development. To resolve this error, use ‘const‘ instead of ‘var‘ to declare variables. 

## **Tool execution after to correct the code** 

Figure 5.6: ESlint tool execution after to correct the code. 

## **Apex PMD tool** 

As another option, we decided to use Apex PMD in our project due to its ability to significantly improve code quality. Apex PMD is a static analysis tool that allows us to detect errors, bad practices, and vulnerabilities in our source code from the early stages of development. 

## **Apex PMD tool execution** 

52 

Figure 5.7: Apex PMD tool execution. 

As we can see, after running Apex PMD on our project’s frontend, there were no corrections needed. 

53 

## **6 Test Cases** 

## **6.1 Test Cases - Mobile Module** 

To perform and execute the tests on the mobile component, the flutter ~~t~~ est library was used, which allowed the logic of these tests to be separated and executed all simultaneously. The library offers functionalities like widget testing, which allows developers to test individual widgets in isolation, ensuring they behave as expected under various scenarios. 

## **6.1.1 Screen Home Tests** 

|**ID**|**Description**|**Preconditions**|**Input**|**Expected Out-**<br>**put**|**Postconditions**|
|---|---|---|---|---|---|
|TCMH1|Verify App-<br>Bar title|Home screen is<br>displayed|Tap action|AppBar<br>title<br>is<br>”HOME”<br>with<br>font size 40|None|
|TCMH2|Verify<br>wel-<br>come text|Home screen is<br>displayed|Tap action|Text is ”Welcome<br>to ” followed by<br>~~-~~<br>place|None|
|TCMH3.1|Verify<br>cre-<br>ation of in-<br>ventory|Home screen is<br>displayed|Tap action|MenuItem<br>with<br>icon<br>edit<br>~~d~~oc-<br>ument,<br>label<br>”Create<br>Inven-<br>tory”|Go to TabBar|
|TCMH3.2|Verify<br>ac-<br>cess<br>to<br>history|Home screen is<br>displayed|Tap action|MenuItem<br>with<br>icon history, label<br>”History”|Go<br>to<br>History<br>page|
|TCMH3.3|Verify<br>ac-<br>cess<br>to<br>settings|Home screen is<br>displayed|Tap action|MenuItem<br>with<br>icon<br>settings,<br>label ”Settings”|Go<br>to<br>Settings<br>page|
|TCMH3.4|Verify<br>app<br>exit<br>func-<br>tionality|Home screen is<br>displayed|Tap action|MenuItem<br>with<br>icon<br>exit<br>~~t~~o<br>~~a~~pp,<br>label ”Exit”|Quit the app|



Table 6.1: Test cases to verify AppBar title, welcome text, and menu items 

54 

## **Results of test execution for Home Screen** 

Figure 6.1: Results of static testing mobile. 

55 

## **6.1.2 Screen TabBar Tests** 

|**ID**|**Description**|**Preconditions**|**Input**|**E. Output**|**Postconditions**|
|---|---|---|---|---|---|
|TCMTB1|Widget<br>ini-<br>tialization|N/A|N/A|CustomTabBar<br>widget is ren-<br>dered|Initialization<br>of<br>widget|
|TCMTB2|Loading<br>state|N/A|Tap on ’Crear<br>Inventario’|Loading indica-<br>tor is displayed|Verify<br>loading<br>state|
|TCMTB3|Error state|N/A|N/A|Error<br>message<br>is displayed|Verify error state|
|TCMTB4|No products<br>found|N/A|N/A|”No<br>products<br>found” message<br>is displayed|Verify display of<br>message|
|TCMTB5|Tab selection|Tap on difer-<br>ent tabs|Tap on element|Corresponding<br>page<br>is<br>dis-<br>played|Verify tab selec-<br>tion|
|TCMTB6|Tab bar la-<br>bels|N/A|N/A|Tab bar labels<br>match expected<br>values|Verify tab bar la-<br>bels|
|TCMTB7|Tab<br>bar<br>icons|N/A|Enter<br>in<br>the<br>widget|Tab bar icons<br>are<br>rendered<br>properly|Verify<br>tab<br>bar<br>icons|
|TCMTB8|Page view|Swipe through<br>the pages|N/A|Correct page is<br>displayed|Verify page view|
|TCMTB9|Tab bar tap<br>animation|Tap on difer-<br>ent tabs|N/A|Page transition<br>animation<br>oc-<br>curs smoothly|Verify tap anima-<br>tion|



Table 6.2: Test cases for various functionalities 

56 

## **Results of test execution for TabBar Screen** 

Figure 6.2: Results of testing TabBar Screen. 

57 

## **6.1.3 Widget DateSelector Tests** 

|**ID**|**Description**|**Preconditions**|**Input**|**E. Output**|**Postconditions**|
|---|---|---|---|---|---|
|TCMDSW1|TCMDSW1<br>Display<br>ini-<br>tial<br>selected<br>date|N/A|N/A|Today’s date is<br>displayed|Verify initial date<br>display|
|TCMDSW2|TCMDSW2<br>Open<br>date<br>picker on tap|N/A|Tap on widget|Date<br>picker<br>dialog<br>is<br>dis-<br>played|Verify date picker<br>opens|
|TCMDSW3|TCMDSW3<br>Call<br>on-<br>DateSelected<br>with<br>picked<br>date|N/A|Select<br>a<br>date<br>and tap ’OK’|onDateSelected<br>is<br>called<br>with<br>the picked date|Verify callback is<br>called<br>with<br>cor-<br>rect date|



Table 6.3: Test cases for DateSelectorWidget functionalities 

## **Results of test execution for DateSelector** 

Figure 6.3: Results of testing DateSelector Widget. 

58 

## **6.1.4 SalesSpots Screen Tests** 

|**ID**|**Description**|**Preconditions**|**Input**|**E. Output**|**Postconditions**|
|---|---|---|---|---|---|
|TCMSS1|Display<br>ini-<br>tial locations|N/A|N/A|All sale spot lo-<br>cations are dis-<br>played|Verify<br>locations<br>display|
|TCMSS2|Tap on a lo-<br>cation|N/A|Tap on a loca-<br>tion image|Global variable<br>’local’<br>is<br>up-<br>dated and nav-<br>igates to Home<br>screen|Verify location is<br>selected and nav-<br>igation occurs|
|TCMSS3|Log selected<br>location<br>in<br>debug mode|Debug<br>mode<br>enabled|Tap on a loca-<br>tion image|Selected<br>loca-<br>tion is logged|Verify log output|



Table 6.4: Test cases for SaleSptosPage functionalities 

## **Results of test execution for SaleSpot** 

Figure 6.4: Results of testing SaleSpot Screen. 

59 

## **6.2 Test Cases - Web Module** 

This section describes the test cases used to ensure the quality and functionality of the web module of this software project, both in its backend and in its frontend. The main objective of testing is to identify and correct errors, verify compliance with requirements and ensure an optimal user experience. 

## **6.2.1 Frontend Testing** 

The frontend, in charge of the user interface and interactive experience, has been evaluated through user interface tests, which validate that all visual elements are presented and function as expected, and usability tests that ensure that navigation is intuitive and accessible to all users. For testing Angular applications specifically, we utilize Jasmine, a robust testing framework that allows us to perform unit tests efficiently and effectively. 

## **Testing for the Main Component: AppComponent** 

|**ID**|**Description**|**Preconditions**|**Input**|**E. Output**|**Postconditions**|
|---|---|---|---|---|---|
|TCWF01|Create<br>the<br>component|Test<br>module<br>confguration<br>completed|None|The<br>compo-<br>nent<br>should<br>be successfully<br>created|The<br>`AppComponent`<br>is<br>initialized<br>and<br>available for other<br>tests|
|TCWF02|Verify<br>`isIndexPage`<br>for the root<br>URL|The component<br>is created and<br>`router` is avail-<br>able|Navigate to the<br>URL `’/’`|`isIndexPage`<br>should be `true`|The<br>component<br>state refects that<br>it is on the home<br>page|



Table 6.5: Test cases for `AppComponent` 

## **Testing of Shared Components** 

|**ID**|**Description**|**Preconditions**|**Input**|**E. Output**|**Postconditions**|
|---|---|---|---|---|---|
|TCWF03|Create<br>MidBanner-<br>Component|Test<br>module<br>confguration<br>completed|None|The<br>compo-<br>nent<br>should<br>be successfully<br>created|The<br>MidBanner-<br>Component<br>is<br>initialized<br>and<br>available for other<br>tests|
|TCWF04|Create<br>FooterCom-<br>ponent|Test<br>module<br>confguration<br>completed|None|The<br>compo-<br>nent<br>should<br>be successfully<br>created|The<br>FooterCom-<br>ponent is initial-<br>ized and available<br>for other tests|



60 

|TCWF05|Create<br>BannerCom-<br>ponent|Test<br>module<br>confguration<br>completed|None|The<br>compo-<br>nent<br>should<br>be successfully<br>created|The BannerCom-<br>ponent is initial-<br>ized and available<br>for other tests|
|---|---|---|---|---|---|



Table 6.6: Test cases for Shared Components 

## **Testing of NavbarComponent** 

|**ID**|**Description**|**Preconditions**|**Input**|**E. Output**|**Postconditions**|
|---|---|---|---|---|---|
|TCWF06|Create<br>NavbarCom-<br>ponent|Test<br>module<br>confguration<br>completed|None|The<br>compo-<br>nent<br>should<br>be successfully<br>created|The<br>`NavbarComponent`<br>is initialized and<br>available for other<br>tests|
|TCWF07|Navigate<br>to<br>login page|The component<br>is created and<br>router is avail-<br>able|Call<br>compo-<br>nent.navigate<br>ToLogin()|router.navigate<br>ByUrl<br>should<br>be called with<br>’/login’|The router navi-<br>gates to the login<br>page|
|TCWF08|Toggle<br>search<br>bar<br>visibility|The component<br>is created|Call<br>compo-<br>nent.toggle<br>SearchBar()<br>twice|isSearch<br>BarVisible<br>should be tog-<br>gled from false<br>to<br>true<br>and<br>back to false|The<br>search<br>bar<br>visibility state is<br>correctly toggled|
|TCWF09|Search prod-<br>uct on Enter<br>key press|The component<br>is created and<br>input value is<br>set|Simulate<br>En-<br>ter<br>key<br>press<br>with<br>compo-<br>nent.search<br>Product(event)|router.navigate<br>should<br>be<br>called<br>with<br>[’/todos’]<br>and<br>queryParams<br>containing<br>trimmed input<br>value|The router nav-<br>igates<br>to<br>the<br>search<br>results<br>page with correct<br>query parameters|



Table 6.7: Test cases for Shared Components: NavbarComponent Case 

61 

## **Testing of AuthService** 

|**ID**|**Description**|**Preconditions**|**Input**|**E. Output**|**Postconditions**|
|---|---|---|---|---|---|
|TCWF10|Create Auth-<br>Service|Test<br>module<br>confguration<br>completed|None|The<br>service<br>should<br>be<br>successfully<br>created|The AuthService<br>is initialized and<br>available for other<br>tests|
|TCWF11|Login user|The service is<br>created|Call<br>ser-<br>vice.login(email,<br>password)|The<br>response<br>should<br>match<br>mockLoginRe-<br>sponse|The service sends<br>a POST request<br>to loginUrl with<br>correct<br>body<br>and receives the<br>mockLoginRe-<br>sponse|
|TCWF12|Register user|The service is<br>created|Call<br>service.<br>register(email,<br>password,<br>frst<br>~~n~~ame,<br>last<br>~~n~~ame)|The<br>response<br>should<br>match<br>mockRegister-<br>Response|The service sends<br>a POST request<br>to<br>registerUrl<br>with correct body<br>and receives the<br>mockRegisterRe-<br>sponse|
|TCWF13|Logout user|The service is<br>created|Call<br>ser-<br>vice.logout()|The<br>response<br>should<br>be<br>truthy|The service sends<br>a POST request<br>to logoutUrl and<br>receives an empty<br>response|
|TCWF14|Check<br>login<br>status|The service is<br>created|localStorage<br>contains<br>ac-<br>cessToken|The<br>function<br>should<br>return<br>true|The service cor-<br>rectly verifes the<br>presence<br>of<br>ac-<br>cessToken in lo-<br>calStorage|
|TCWF15|Get user info|The service is<br>created|Call<br>service.<br>getUserInfo()|The<br>response<br>should<br>match<br>mockUser|The service sends<br>a GET request to<br>userInfoUrl<br>with<br>Authorization<br>header<br>and<br>re-<br>ceives mockUser|



Table 6.8: Test cases for AuthService 

62 

## **Testing of ProductService** 

|**ID**|**Description**|**Preconditions**|**Input**|**E. Output**|**Postconditions**|
|---|---|---|---|---|---|
|TCWF16|Create Prod-<br>uctService|Test<br>module<br>confguration<br>completed|None|The<br>service<br>should<br>be<br>successfully<br>created|The<br>ProductSer-<br>vice is initialized<br>and available for<br>other tests|
|TCWF17|Retrieve<br>all<br>products<br>from API via<br>GET|The service is<br>created|Call<br>service.<br>getAllProd-<br>ucts()|The<br>response<br>should<br>match<br>mockProducts|The service sends<br>a GET request to<br>the products end-<br>point and receives<br>mockProducts|
|TCWF18|Retrieve<br>fltered prod-<br>ucts<br>from<br>API<br>via<br>GET|The service is<br>created|Call<br>service.<br>getFiltered-<br>Products(100,<br>200, ’type’)|The<br>response<br>should<br>match<br>mockFiltered-<br>Products|The<br>service<br>sends<br>a<br>GET<br>request<br>to<br>the<br>flteredProducts<br>endpoint<br>with<br>correct<br>query<br>parameters<br>and<br>receives mockFil-<br>teredProducts|
|TCWF19|Retrieve<br>newest prod-<br>ucts<br>from<br>API<br>via<br>GET|The service is<br>created|Call<br>service.<br>getNewest-<br>Products()|The<br>response<br>should<br>match<br>mockNewest-<br>Products|The<br>service<br>sends<br>a<br>GET<br>request<br>to<br>the<br>newest-products<br>endpoint<br>and<br>receives<br>mock-<br>NewestProducts|
|TCWF20|Retrieve<br>bestselling<br>products<br>from API via<br>GET|The service is<br>created|Call<br>service.<br>getBestselling-<br>Products()|The<br>response<br>should<br>match<br>mockBest-<br>sellingProducts|The service sends<br>a GET request to<br>the<br>bestselling-<br>products<br>end-<br>point and receives<br>mockBestselling-<br>Products|



Table 6.9: Test cases for ProductService 

63 

## **Testing of NewsService** 

|**ID**|**Description**|**Preconditions**|**Input**|**E. Output**|**Postconditions**|
|---|---|---|---|---|---|
|TCWF21|Create<br>NewsService|Test<br>module<br>confguration<br>completed|None|The<br>service<br>should<br>be<br>successfully<br>created|The NewsService<br>is initialized and<br>available for other<br>tests|
|TCWF22|Return<br>cor-<br>rect news list|The service is<br>created|Call<br>service.<br>updateNews()|The<br>returned<br>news list should<br>have a length<br>greater than 0<br>and match the<br>service’s notice<br>property|The<br>service<br>returns<br>a<br>non-<br>empty list of news<br>items<br>matching<br>the notice prop-<br>erty|



Table 6.10: Test cases for NewsService 

## **Testing of UserDetailsComponent** 

|**ID**|**Description**|**Preconditions**|**Input**|**E. Output**|**Postconditions**|
|---|---|---|---|---|---|
|TCWF23|Create<br>UserDe-<br>tailsCompo-<br>nent|Test<br>module<br>confguration<br>completed|None|The<br>compo-<br>nent<br>should<br>be successfully<br>created|The<br>UserDe-<br>tailsComponent<br>is initialized and<br>available for other<br>tests|
|TCWF24|Set<br>userInfo<br>if user is au-<br>thenticated|The component<br>is created and<br>user is authen-<br>ticated|Call<br>fx-<br>ture.<br>de-<br>tectChanges()|The<br>userInfo<br>should<br>be<br>set<br>with mockUser<br>data|The<br>component<br>retrieves<br>and<br>sets the userInfo<br>property<br>with<br>mockUser|
|TCWF25|Log<br>error<br>if<br>user<br>info<br>cannot<br>be<br>fetched|The component<br>is created, user<br>is<br>authenti-<br>cated but user<br>info fetch fails|Call<br>fx-<br>ture.<br>de-<br>tectChanges()|An error should<br>be<br>logged<br>to<br>the<br>console<br>with the mes-<br>sage ’User info<br>fetch error’|The<br>component<br>logs<br>an<br>error<br>when<br>user<br>info<br>fetch fails|
|TCWF26|Log error if<br>user<br>is<br>not<br>authenti-<br>cated|The component<br>is created but<br>user is not au-<br>thenticated|Call<br>fx-<br>ture.<br>de-<br>tectChanges()|An error should<br>be<br>logged<br>to<br>the<br>console<br>with the mes-<br>sage ’User not<br>authenticated’|The<br>component<br>logs<br>an<br>error<br>when user is not<br>authenticated|



64 

|TCWF27|Logout<br>and<br>navigate<br>to<br>home|The component<br>is created|Call<br>compo-<br>nent. logout()|The<br>compo-<br>nent<br>should<br>call<br>authSer-<br>vice.logout()<br>and navigate to<br>home|The<br>component<br>logs out the user<br>and navigates to<br>the home page|
|---|---|---|---|---|---|



Table 6.11: Test cases for UserDetailsComponent 

## **Testing of ShoppingCartComponent** 

|**ID**|**Description**|**Preconditions**|**Input**|**E. Output**|**Postconditions**|
|---|---|---|---|---|---|
|TCWF28|Create Shop-<br>pingCart-<br>Component|Test<br>module<br>confguration<br>completed|None|The<br>compo-<br>nent<br>should<br>be successfully<br>created|The<br>Shopping-<br>CartComponent<br>is initialized and<br>available for other<br>tests|
|TCWF29|Load<br>prod-<br>ucts<br>from<br>localStorage<br>on init|The component<br>is created,<br>lo-<br>calStorage<br>has<br>cart items|Call<br>fx-<br>ture.<br>de-<br>tectChanges()|The<br>product-<br>shop<br>should<br>be<br>set<br>with<br>items<br>from<br>localStorage,<br>isCartEmpty<br>should be false|The<br>component<br>loads cart items<br>from localStorage<br>into productshop|
|TCWF30|Calculate<br>subtotal<br>correctly|The component<br>is created and<br>productshop<br>has items|Call<br>compo-<br>nent.<br>get-<br>Subtotal(1)|The<br>subto-<br>tal<br>should<br>be<br>calculated<br>correctly|The<br>component<br>calculates<br>the<br>subtotal of items<br>in the cart|
|TCWF31|Calculate<br>IVA<br>cor-<br>rectly|The component<br>is created and<br>productshop<br>has items|Call<br>com-<br>ponent.<br>getIVA(1)|The IVA should<br>be<br>calculated<br>correctly|The<br>component<br>calculates<br>the<br>IVA of items in<br>the cart|
|TCWF32|Calculate to-<br>tal correctly|The component<br>is created and<br>productshop<br>has items|Call<br>compo-<br>nent.<br>getTo-<br>tal(1)|The<br>total<br>should<br>be<br>calculated<br>correctly|The<br>component<br>calculates<br>the<br>total cost of items<br>in the cart|
|TCWF33|Update<br>quantity<br>correctly|The component<br>is created and<br>productshop<br>has items|Call<br>compo-<br>nent.<br>up-<br>dateQuan-<br>tity(event,<br>1)<br>with<br>a<br>new<br>quantity|The<br>quantity-<br>ToBuy<br>should<br>be updated cor-<br>rectly in prod-<br>uctshop|The<br>component<br>updates the quan-<br>tityToBuy of an<br>item in the cart|



65 

|TCWF34|Navigate<br>to<br>checkout|The component<br>is created and<br>productshop<br>has items|Call<br>compo-<br>nent.<br>go-<br>ToCheckout()|localStorage.<br>setItem should<br>be called with<br>updated<br>cart,<br>and<br>router<br>should<br>navi-<br>gate to ’/caja’|The<br>component<br>saves<br>the<br>cart<br>to<br>localStorage<br>and navigates to<br>checkout|
|---|---|---|---|---|---|
|TCWF35|Go back to<br>previous<br>lo-<br>cation|The component<br>is created and<br>productshop<br>has items|Call<br>compo-<br>nent. keepBuy-<br>ing()|localStorage.<br>setItem should<br>be<br>called<br>with<br>updated<br>cart,<br>and<br>lo-<br>cation.back<br>should<br>be<br>called|The<br>component<br>saves the cart to<br>localStorage<br>and<br>navigates back|
|TCWF36|Prevent typ-<br>ing|The component<br>is created|Call<br>compo-<br>nent.<br>prevent-<br>Typing(event)<br>with<br>a<br>Key-<br>boardEvent|event. prevent-<br>Default should<br>be called|The<br>component<br>prevents<br>typing<br>in a certain input<br>feld|



Table 6.12: Test cases for ShoppingCartComponent 

## **Testing of RegisterComponent** 

|**ID**|**Description**|**Preconditions**|**Input**|**E. Output**|**Postconditions**|
|---|---|---|---|---|---|
|TCWF37|Create<br>Register-<br>Component|Test<br>module<br>confguration<br>completed|None|The<br>compo-<br>nent<br>should<br>be successfully<br>created|The<br>Register-<br>Component<br>is<br>initialized<br>and<br>available for other<br>tests|
|TCWF38|Register suc-<br>cessfully|The<br>compo-<br>nent is created,<br>AuthService is<br>mocked|Fill registration<br>form felds, call<br>component.<br>onSubmit()|Router<br>should<br>navigate<br>to<br>’/’, console.log<br>should<br>display<br>’Registration<br>successful’<br>with<br>response,<br>errorMessage<br>should<br>be<br>empty|The<br>component<br>registers<br>a<br>user<br>successfully|



66 

|TCWF39|Handle regis-<br>tration error|The<br>compo-<br>nent is created,<br>AuthService is<br>mocked|Fill<br>registra-<br>tion form felds<br>with<br>existing<br>email,<br>call<br>component.<br>onSubmit()|Router<br>should<br>not<br>navigate,<br>console.error<br>should<br>display<br>’Registration<br>error’<br>with<br>error<br>object,<br>errorMessage<br>should<br>con-<br>tain the error<br>message|The<br>component<br>handles<br>regis-<br>tration<br>error<br>appropriately|
|---|---|---|---|---|---|
|Table 6.13: Test cases for RegisterComponent<br>**Testing of ProductSectionComponent**||||||
|**ID**|**Description**|**Preconditions**|**Input**|**Expected**<br>**Output**|**Postconditions**|
|TCWF40|Create Prod-<br>uctSection-<br>Component|Test<br>module<br>confguration<br>completed|None|The<br>compo-<br>nent<br>should<br>be successfully<br>created|The ProductSec-<br>tionComponent<br>is initialized and<br>available for other<br>tests|
|TCWF41|Initialize<br>with<br>sec-<br>tion ”todos”<br>and<br>fetch<br>products|The<br>compo-<br>nent is created,<br>ProductService<br>is mocked|None|Component<br>should<br>have<br>section<br>”to-<br>dos”,<br>to-<br>talProducts<br>should<br>match<br>mockProducts,<br>data should be<br>initialized with<br>mockProducts|The<br>component<br>initializes<br>with<br>correct<br>section<br>and fetches prod-<br>ucts accordingly|
|TCWF42|Filter<br>prod-<br>ucts<br>by<br>search string|Component<br>is<br>created,<br>data<br>initialized with<br>mockProducts|Search<br>string<br>”product 1”|data<br>should<br>contain<br>only<br>products<br>matching<br>the<br>search string|The<br>component<br>flters<br>products<br>correctly<br>based<br>on<br>the<br>search<br>string|



67 

|TCWF43|Update price<br>range<br>and<br>fetch fltered<br>products|Component<br>is<br>created,<br>ProductService<br>is<br>mocked,<br>minPrice<br>and<br>maxPrice<br>are<br>set|Call<br>getFil-<br>teredProd-<br>ucts()|data<br>should<br>contain<br>prod-<br>ucts<br>fltered<br>by price range<br>defned<br>by<br>minPrice<br>and<br>maxPrice|The<br>component<br>fetches<br>fltered<br>products<br>based<br>on updated price<br>range|
|---|---|---|---|---|---|
|TCWF44|Sort<br>prod-<br>ucts<br>in<br>descending<br>order<br>by<br>price|Component<br>is<br>created,<br>data<br>initialized with<br>mockProducts|Sort<br>order<br>”desc”|data should be<br>sorted<br>in<br>de-<br>scending order<br>by price|The<br>component<br>sorts<br>products<br>correctly<br>based<br>on<br>the<br>specifed<br>order|
|TCWF45|Add product<br>to cart|Component<br>is<br>created,<br>se-<br>lectedProduct<br>is<br>set<br>with<br>mockProduct|Call<br>compo-<br>nent.<br>add-<br>Cart();|localStorage<br>should contain<br>the<br>added<br>product in cart<br>format|The<br>component<br>adds the selected<br>product<br>to<br>the<br>cart<br>stored<br>in<br>localStorage|



Table 6.14: Test cases for ProductSectionComponent 

## **Testing of LoginComponent** 

|**ID**|**Description**|**Preconditions**|**Input**|**Expected**<br>**Output**|**Postconditions**|
|---|---|---|---|---|---|
|TCWF46|Create<br>LoginCom-<br>ponent|Test<br>module<br>confguration<br>completed|None|The<br>compo-<br>nent<br>should<br>be successfully<br>created|The<br>Login-<br>Component<br>is<br>initialized<br>and<br>available for other<br>tests|
|TCWF47|Navigate<br>to<br>register page|The component<br>is created|Click<br>on<br>the<br>register button|Should<br>navi-<br>gate to ’/regis-<br>ter’|The<br>component<br>navigates to the<br>register<br>page<br>when requested|
|TCWF48|Login<br>suc-<br>cessfully|The<br>compo-<br>nent is created,<br>AuthService is<br>mocked|Valid email and<br>password|localStorage<br>should contain<br>access<br>token,<br>should navigate<br>to ’/’|The<br>component<br>logs<br>in<br>suc-<br>cessfully<br>and<br>navigates to the<br>home page|



68 

|TCWF49|Handle login<br>error|The<br>compo-<br>nent is created,<br>AuthService is<br>mocked|Invalid email or<br>password|errorMessage<br>should<br>be<br>displayed,<br>error<br>should<br>be<br>logged<br>to<br>console|The<br>component<br>handles<br>login<br>errors correctly|
|---|---|---|---|---|---|
|TCWF50|Not navigate<br>on login er-<br>ror|The<br>compo-<br>nent is created,<br>AuthService is<br>mocked|Invalid email or<br>password|Should<br>not<br>navigate<br>any-<br>where|The<br>component<br>does not navigate<br>on login error|



Table 6.15: Test cases for LoginComponent 

## **Testing of IndexComponent** 

|**ID**|**Description**|**Preconditions**|**Input**|**Expected**<br>**Output**|**Postconditions**|
|---|---|---|---|---|---|
|TCWF51|Create<br>IndexCom-<br>ponent|Test<br>mod-<br>ule<br>setup<br>is<br>completed|None|Component<br>should<br>be<br>created<br>suc-<br>cessfully|IndexComponent<br>initializes<br>and<br>is<br>available<br>for<br>further testing|
|TCWF52|Open<br>and<br>close product<br>details|Component<br>is<br>created|Call<br>compo-<br>nent.<br>open-<br>Details (mock-<br>Product)|Should display<br>product details<br>and then close<br>them properly|Component han-<br>dles product de-<br>tail<br>display<br>and<br>hiding correctly|
|TCWF53|Add product<br>to cart|Component<br>is<br>created,<br>simu-<br>lated<br>selected<br>product|Call<br>compo-<br>nent.<br>add-<br>Cart();|Should<br>store<br>selected<br>prod-<br>uct<br>in<br>cart<br>correctly<br>in<br>localStorage|Component han-<br>dles adding prod-<br>ucts to cart cor-<br>rectly|



Table 6.16: Test Cases for IndexComponent 

69 

## **Testing of BlogComponent** 

|**ID**|**Description**|**Preconditions**|**Input**|**E. Output**|**Postconditions**|
|---|---|---|---|---|---|
|TCWF54|Create Blog-<br>Component|Test<br>module<br>confguration<br>completed|None|The<br>compo-<br>nent<br>should<br>be successfully<br>created|The BlogCompo-<br>nent is initialized<br>and available for<br>other tests|
|TCWF55|Fetch<br>news<br>from<br>NewsService<br>on initializa-<br>tion|The<br>compo-<br>nent is created<br>and<br>NewsSer-<br>vice<br>mock<br>is<br>provided|Call<br>compo-<br>nent.ngOnInit()|component.notic<br>should<br>equal<br>the mock news<br>data|e<br>The<br>compo-<br>nent fetches and<br>displays<br>news<br>correctly<br>from<br>NewsService|



Table 6.17: Test cases for BlogComponent 

## **Results of testing Web Frontend** 

70 

Figure 6.5: Results of testing Web Frontend. 

71 

## **6.2.2 Backend Testing** 

The backend, responsible for business logic and data management, has been subjected to a series of unit tests that verify the correct functioning of individual components and the correct functioning of system models and views. For our Django-based backend, we employ Django’s built-in testing tools, including pytest, for comprehensive testing of our API endpoints and business logic. Furthermore, we leverage Django’s factory libraries to create mock data that simulate our database models, ensuring thorough testing of our application’s behavior under various scenarios. 

## **Client Model Test Cases** 

|**ID**|**Description**|**Preconditions**|**Input**|**Expected**<br>**Output**|**Postconditions**|
|---|---|---|---|---|---|
|TCWB01|Test user cre-<br>ation|-|UserFactory.<br>create()|User.objects.<br>count() is 1|Successfully<br>cre-<br>ates a user|
|TCWB02|Test<br>user<br>string repre-<br>sentation|-|str(self.user)|str(self.user)<br>matches<br>self.user.email|Correctly displays<br>user’s<br>email<br>as<br>string representa-<br>tion|
|TCWB03|Test<br>client<br>creation|-|ClientFactory.<br>create()|Client.objects.<br>count() is 1|Successfully<br>cre-<br>ates a client|
|TCWB04|Test<br>client<br>relations|Client instance<br>exists|self.client.user.<br>clients.count()|self.client.user.<br>clients.count()<br>is 1|Client is correctly<br>related to its user|
|TCWB05|Test<br>max<br>length felds<br>for client|-|Client.objects.<br>create()|IntegrityError<br>raised<br>for<br>overly<br>long<br>felds|Prevents creation<br>of<br>client<br>with<br>excessively<br>long<br>felds|
|TCWB06|Test<br>client<br>DNI unique-<br>ness|ClientFactory.<br>create()|ClientFactory.<br>create(dni<br>`=`<br>client1.dni)|IntegrityError<br>raised<br>for<br>duplicate DNI|Ensures<br>unique-<br>ness<br>of<br>client’s<br>DNI|
|TCWB07|Test<br>cate-<br>gorycreation|-|CategoryFactory<br>create()|.<br>Category.objects<br>count() is 1|.<br>Successfully<br>cre-<br>ates a category|
|TCWB08|Test<br>unique<br>category<br>name|-|CategoryFactory<br>create()|.<br>IntegrityError<br>raised<br>for<br>duplicate<br>category name|Ensures<br>unique-<br>ness of category<br>name|
|TCWB09|Test product<br>creation|-|ProductFactory.<br>create()|Product.objects.<br>count() is 1|Successfully<br>cre-<br>ates a product|



72 

|TCWB10|Test product<br>relations|Product<br>in-<br>stance exists|self.product.<br>cate-<br>gory.products.<br>count()|self.product.<br>cate-<br>gory.products.<br>count() is 1|Product<br>is<br>cor-<br>rectly related to<br>its category|
|---|---|---|---|---|---|
|TCWB11|Test<br>order<br>creation|-|OrderFactory.<br>create()|Order.objects.<br>count() is 1|Successfully<br>cre-<br>ates an order|
|TCWB12|Test<br>order<br>relations|Order instance<br>exists|self.order.<br>client.orders.<br>count()|self.order.<br>client.orders.<br>count() is 1|Order is correctly<br>related<br>to<br>its<br>client|
|TCWB13|Test required<br>felds for or-<br>der|-|Order.objects.<br>create()|IntegrityError<br>raised<br>for<br>missing client|Prevents creation<br>of order without a<br>client|
|TCWB14|Test<br>order<br>item creation|-|OrderItem Fac-<br>tory. create()|OrderItem. ob-<br>jects. count() is<br>1|Successfully<br>cre-<br>ates an order item|
|TCWB15|Test<br>or-<br>der<br>item<br>relations|OrderItem<br>in-<br>stance exists|self.order<br>~~i~~tem.<br>order.items.<br>count()<br>and<br>self.order<br>~~-~~<br>item.<br>product.<br>order<br>~~i~~tems.<br>count()|Counts are 1|Order<br>item<br>is<br>correctly<br>related<br>to its order and<br>product|
|TCWB16|Test<br>or-<br>der<br>item<br>quantity|-|self.order<br>~~i~~tem.<br>quantity `>` 0|self.order<br>~~i~~tem.<br>quantity<br>is<br>greater than 0|Order item quan-<br>tity is valid|



Table 6.18: Test cases for Client model 

## **Test cases for Serializer validation** 

|**ID**|**Description**|**Preconditions**|**Input**|**Expected**<br>**Output**|**Postconditions**|
|---|---|---|---|---|---|
|TCWB17|Test UserSe-<br>rializer valid|-|UserFactory.<br>build()|serializer.is<br>~~-~~<br>valid() is True|UserSerializer<br>correctly<br>vali-<br>dates user data|
|TCWB18|Test UserSe-<br>rializer<br>required<br>felds|-|[ ]|serializer.<br>is<br>~~-~~<br>valid() is False,<br>’email’<br>and<br>’password’<br>in<br>serializer.errors|UserSerializer<br>correctly<br>iden-<br>tifes<br>missing<br>required felds|



73 

|TCWB19|Test<br>ClientSe-<br>rializer valid|User<br>instance<br>exists|ClientFactory.<br>build(),<br>User-<br>Factory.<br>cre-<br>ate()|serializer.<br>is<br>~~-~~<br>valid() is True|ClientSerializer<br>correctly<br>vali-<br>dates client data<br>with<br>associated<br>user|
|---|---|---|---|---|---|
|TCWB20|Test<br>ClientSe-<br>rializer<br>required<br>felds|-|[ ]|serializer.<br>is<br>~~v~~alid()<br>is<br>False,<br>’dni’,<br>’direction’,<br>’cellphone’,<br>’city’ in serial-<br>izer.errors|ClientSerializer<br>correctly<br>iden-<br>tifes<br>missing<br>required felds|
|TCWB21|Test Catego-<br>rySerializer<br>valid|-|CategoryFactory<br>build()|.<br>serializer.<br>is<br>~~-~~<br>valid() is True|CategorySerializer<br>correctly<br>vali-<br>dates<br>category<br>data|
|TCWB22|Test Catego-<br>rySerializer<br>required<br>felds|-|[ ]|serializer.<br>is<br>~~v~~alid()<br>is<br>False,<br>’name’,<br>’description’<br>in<br>serializer.<br>errors|CategorySerializer<br>correctly<br>iden-<br>tifes<br>missing<br>required felds|
|TCWB23|Test<br>Prod-<br>uctSerializer<br>valid|-|ProductFactory.<br>build()|serializer.<br>is<br>~~-~~<br>valid() is True|ProductSerializer<br>correctly<br>vali-<br>dates<br>product<br>data|
|TCWB24|Test<br>Prod-<br>uctSerializer<br>required<br>felds|-|[ ]|serializer.is<br>~~-~~<br>valid() is False,<br>’name’,<br>’de-<br>scription’,<br>’price’,<br>’quan-<br>tity’ in serial-<br>izer. errors|ProductSerializer<br>correctly<br>iden-<br>tifes<br>missing<br>required felds|
|TCWB25|Test<br>Order-<br>Serializer<br>valid|Client instance<br>exists|OrderFactory.<br>build(), Client-<br>Factory.<br>cre-<br>ate()|serializer.<br>is<br>~~-~~<br>valid() is True|OrderSerializer<br>correctly<br>vali-<br>dates order data<br>with<br>associated<br>client|



74 

|TCWB26|Test<br>Order-<br>Serializer re-<br>quired felds|-|[ ]|serializer.<br>is<br>~~-~~<br>valid() is False,<br>’client’,<br>’total’<br>in serializer. er-<br>rors|OrderSerializer<br>correctly<br>iden-<br>tifes<br>missing<br>required felds|
|---|---|---|---|---|---|
|TCWB27|Test<br>Or-<br>derItem-<br>Serializer<br>valid|Order instance<br>exists|OrderItem Fac-<br>tory.<br>build(),<br>OrderFactory.<br>create()|serializer.<br>is<br>~~-~~<br>valid() is True|OrderItemSerialize<br>correctly<br>val-<br>idates<br>order<br>item<br>data<br>with<br>associated order|
|TCWB28|Test<br>Or-<br>derItem-<br>Serializer<br>required<br>felds|-|[ ]|serializer.<br>is<br>~~-~~<br>valid() is False,<br>’order’,<br>’quan-<br>tity’ in serial-<br>izer. errors|OrderItemSerialize<br>correctly<br>iden-<br>tifes<br>missing<br>required felds|



Table 6.19: Test cases for Serializer validation 

## **Test cases for API endpoints** 

|**ID**|**Description**|**Preconditions**|**Input**|**Expected**<br>**Output**|**Postconditions**|
|---|---|---|---|---|---|
|TCWB29|Test get all<br>products|-|Product.objects.<br>create()|List of all prod-<br>ucts|Successfully<br>retrieves<br>all<br>products|
|TCWB30|Test<br>get<br>fltered<br>products|-|Product.objects.<br>create()|Filtered list of<br>products|Successfully<br>fl-<br>ters<br>products<br>based on parame-<br>ters|
|TCWB31|Test register<br>view|-|’email’:<br>’test@example.<br>com’,<br>’pass-<br>word’:<br>’test-<br>password’,<br>’frst<br>~~n~~ame’:<br>’John’,<br>’last<br>~~-~~<br>name’: ’Doe’|’refresh’,<br>’access’<br>in<br>response.json()|Successfully regis-<br>ters a new user|
|TCWB32|Test<br>login<br>view|User.objects.<br>create<br>~~u~~ser()|’email’:<br>’test@example.<br>com’,<br>’pass-<br>word’:<br>’test-<br>password’|’refresh’,<br>’access’<br>in<br>response.json()|Successfully<br>logs<br>in existing user|



75 

|TCWB33|Test<br>logout<br>view|User.objects.<br>create<br>~~u~~ser(),<br>self.client.login()|-|’message’:<br>’Logout<br>suc-<br>cessful’<br>in<br>response.json()|Successfully<br>logs<br>out<br>a<br>logged-in<br>user|
|---|---|---|---|---|---|
|TCWB34|Test<br>newest<br>products|Order.objects.<br>create()|Product.objects.<br>create()|List of newest<br>products|Successfully<br>re-<br>trieves<br>newest<br>products|
|TCWB35|Test<br>best-<br>selling<br>products|Order.objects.<br>create(), Prod-<br>uct.objects.<br>create()|Product.order<br>~~-~~<br>items. create()|List<br>of<br>best-<br>selling<br>prod-<br>ucts|Successfully<br>re-<br>trieves bestselling<br>products|
|TCWB36|Test get user<br>data|User.objects.<br>create<br>~~u~~ser()|HTTP<br>~~A~~U-<br>THORIZA-<br>TION:<br>Bearer<br>access<br>~~t~~oken|User<br>data<br>(email,<br>first<br>~~-~~<br>name,<br>last<br>~~-~~<br>name)|Successfully<br>retrieves<br>user<br>data|



Table 6.20: Test cases for API endpoints 

## **Results of testing Web Backend** 

Figure 6.6: Results of testing Web Backend. 

76 

## **7 Individual Contribution** 

|**Name**|**Sections**|
|---|---|
|**Andr´es**<br>**Cornejo**|Abstract, Mobile Development Framework, Coding Standards-Mobile<br>Module, User Manual-Mobile Module, Test Cases-Mobile Module,<br>Deployment Mobile Guide|
|**Jorge Mawyin**|Coding Standars and Coding Standards/PMD for Web Module<br>(Backend-Frontend), Preemptive Error Detection-Mobile Module, In-<br>stalation Guide, Web Module Deployment.|
|**Kevin Rold´an**|SCRUM Evidence,Relevant Architectural Decisions,Test Cases - Web<br>Module and Appendix G: User Manual - Web Manual|
|**Angel Tomal´a**|Project Context, Coding Standards/PMD for Flutter, Preemptive<br>Error Detection-Mobile Module, Test Cases-Mobile Module, Instal-<br>lation Guide, Software Building - Mobile Apk|



77 

## **8 Appendix** 

## **8.1 Appendix A: GitHub Repositories** 

You can find the repository of this Requirements here: `https://github.com/Nintventario-Team/ Requeriments_PRICOTERCORP.git` . 

You can find the repository of Mobile Module here: `https://github.com/Nintventario-Team/ NintventarioApp-beta.git` 

You can find the repository of Web Module here: `https://github.com/Nintventario-Team/ Nintventario-betat` 

You can find the repository of Communication Report here: `https://github.com/ Nintventario-Team/T1.git` 

## **8.2 Appendix B: Software Building** 

## **Mobile APK** 

The mobile app was released on 06/22/2024 as an Alpha version (pre-release) with the Github Actions automation tool and the APK executable can be found at the following link: 

```
https://github.com/Nintventario-Team/NintventarioApp-beta/releases/tag/v2
```

## **Web Page** 

The website (front and back end) was deployed on 06/22/2024. The backend was deployed with pythonanywhere. `https://jorgemawyin.pythonanywhere.com/admin/` 

The frontend was deployed with firebase. `https://nintventario.web.app/` 

## **8.3 Appendix C: Project Presentation Video** 

To access the project presentation video, which shows a demonstration (in English) of our software system showing the software components in execution and their compliance with the functional and non-functional requirements, access the following link. Also, there is the link of the presentation in PPT for the Project Presentation Video: Presentation. 

78 

## **8.4 Appendix D: Client Acceptance Letters** 

## **8.4.1 Sprint 1 Acceptance Letter** 

Figure 8.1: Sprint 1 Acceptance Letter 

79 

## **8.5 Appendix E: System Deployment Guide WM** 

- **Requirements:** 

## **Software Requirements:** 

- Python: Make sure you have Python installed on your system. You can verify it by using the following command: (python –version). 

Figure 8.2: Python –Version. 

If you don’t have it, you can download it from the official Python website (https://www.python.org/downloads/). 

- Angular CLI: If you don’t have it yet, install Angular CLI globally by running (npm install -g @angular/cli) in your terminal. 

- Disk Space: Make sure you have at least 1 GB of free disk space for the project and dependencies. 

## **Hardware Requirements:** 

- CPU: A processor of at least 1 GHz is recommended. 

- RAM: It is recommended to have at least 4 GB of RAM. 

- XAMPP: Download and install XAMPP from the official XAMPP website (https://www.apachefriends.org/index.html). 

## **Network Requirements:** 

   - Internet Connection: An internet connection is required to install Python and Node.js dependencies, as well as to download Angular libraries and packages. 

- **Installation Steps:** 

   1. Clone the repository: 

      - Clone the repository (https://github.com/Nintventario-Team/Nintventariobeta.git) to your local machine using the following command (git clone LINK) in CMD. 

   2. Set up the virtual environment: 

80 

- Once the repository is cloned, access it as follows (cd Nintventario-beta/backend). 

Figure 8.3: Backend Path example. 

   - Once in the backend folder, create a Python virtual environment by executing: 

      - ∗ On Windows: (python -m venv environmentName). Then activate the virtual environment by running ( ”./env/Scripts/activate”). 

      - ∗ On Linux/macOS: (source environmentName/bin/activate). 

3. Install Django dependencies: 

   - Once you are in the virtual environment, install the requirements.txt file by running: (pip install -r requirements.txt). 

   - Then, check if you have the following packages by running the command (pip list). 

Figure 8.4: Pip List example. 

4. Configure the database: 

81 

- Start XAMPP and make sure the MySQL and Apache servers are running. 

Figure 8.5: Xampp configuration. 

- Then, create a new database for your project from phpMyAdmin. 

Figure 8.6: Creation database example. 

5. Configure the Django backend: 

   - Go to the settings.py file in the backend/backend ~~n~~ intventario configuration folder. 

   - Configure the connection to the MySQL database you just created with the credentials. 

82 

Figure 8.7: Credential database example. 

   - Perform migrations by running (python manage.py makemigrations) followed by (python manage.py migrate) in CMD. 

6. Insert data into MySQL: 

   - Once migrations are executed. In the browser, go to (http://localhost/phpmyadmin/) and enter the database you created, go to the ’custom ~~u~~ ser ~~c~~ ategory’ table, and in the SQL section, execute the category inserts found in the database ~~n~~ intventario.sql file. 

   - Repeat the same process for the ’custom ~~u~~ ser ~~p~~ roduct’ table. 

7. Configure the Angular frontend: 

   - In another command line, navigate to the Angular frontend folder. 

Figure 8.8: Frontend path example. 

   - Install dependencies by running (npm install). 

8. Configure the Angular frontend: 

   - In the virtual environment terminal, run (python manage.py runserver) to start the Django server. 

   - In the other terminal, navigate to the frontend folder and run (ng serve -o) to start the Angular development server. 

83 

- Now you should be able to access the web catalog from your browser by visiting http://localhost:4200. 

## **8.6 Appendix F: Installation Guide MM** 

To install the Nintventario app, first of all you must go to the link below and click on the Nintventario.apk file. You don’t need to have a github account to access the file. `https: //github.com/Nintventario-Team/NintventarioApp-beta/releases/tag/v0.1` 

Figure 8.9: APK release in Github. 

If downloaded through a browser on your phone, an alert will appear indicating that downloading an app by external means is dangerous with the message ”The app could be harmful”. Select the ”Download anyway” option and don’t worry that the app does not contain any harmful software, it is simply an alert that comes by default when downloading applications outside of conventional stores. 

Once the apk file is downloaded, you have to locate it and open it to start the installation. In some cases it will be necessary to activate the ”unknown sources” option to allow the installation. 

84 

Figure 8.10: Activate unknown sources. 

Once the app is installed, you just have to look for the icon and open the application. 

Figure 8.11: App installed. 

Figure 8.12: App. 

85 

## **8.7 Appendix G: User Manual** 

## **8.7.1 Web Manual** 

## **User Guide for Using the Django Deployed System in PythonAnywhere** 

First open your web browser and enter the URL of the Django administration panel through the following link: `https://jorgemawyin.pythonanywhere.com/admin/` . Once there, you will have the following view: 

Figure 8.13: Django administration panel 

On the login page, enter your superuser credentials (username and password) that were configured during the initial Django installation. These credentials, at the moment, are the following: 

**user:** adminNintventario@hotmail.com 

**password:** admind 

Click ”Login” to access the administration panel. 

86 

Figure 8.14: Django administration panel - Loged 

87 

Once you’re logged in, you’ll see the following sections in your Django admin panel: 

**Auth Token** In this section we can manage the system tokens 

Figure 8.15: Auth Section - Django 

Add: Allows you to create new authentication tokens. These tokens are used to authenticate users to your APIs. To add a token, select ”Add” under the ”Tokens” section, complete the required fields, and save the new token. 

Figure 8.16: Add Token - Django 

Change: View and modify existing authentication tokens. To modify a token, select ”Change” under the ”Tokens” section, browse through the list of tokens, select the one you want to modify, make the necessary changes, and save. 

88 

Figure 8.17: Change Token - Django 

## **Authentication and Authorization** 

In this section you can interact with the various types of authorization groups in the backend 

Figure 8.18: Authentication and Authorization Section - Django 

Add: Allows you to create new user groups. Groups are a way to organize users and assign permissions together. To add a group, select ”Add” under the ”Groups” section, fill out the necessary fields, such as the group name and associated permissions, then save. 

89 

Figure 8.19: Add Group - Django 

Change: Allows you to view and modify existing user groups. To modify a group, select ”Change” under the ”Groups” section, select the group you want to modify, make the necessary changes, and save. 

Figure 8.20: Change Group - Django 

## **Custom User Management** 

Here we manage what corresponds to the users that our website will have. 

90 

Figure 8.21: Custom User Management Section - Django 

Add: Allows you to create new users in the system. Here you can define details such as username, password, and assign specific permissions. To add a user, select ”Add” under the ”Users” section, complete the required fields such as username, password, and other user profile details, assign specific permissions as necessary, and save. 

Figure 8.22: Add User - Django 

Change: Allows you to view and modify existing users. To modify a user, select ”Change” under the ”Users” section, find the user you want to modify, make any necessary changes to the profile details or permissions, and save. 

91 

Figure 8.23: Change User - Django 

## **Recent Actions** 

Displays a log of recent actions taken by the currently logged in user. This may include actions such as creating or modifying objects within the administration panel. It is useful for tracking changes and managing your activity within the system. 

92 

Figure 8.24: Recent Actions Section - Django 

93 

## **User Guide for Navigating and Using the Website** 

First open your web browser and enter the URL of the web page displayed in Firebase which is the following: 

`https://nintventario.web.app` 

Once the page loads, users will be on the main interface of our application. Below you will see how to use the basic functionalities of the website: 

## **Page Navigation** 

Use the navigation menu, located at the top, on the main page to explore different parts of the application. The sections available to browse are: ”Inicio”, ”Categorias”, Blog, login and search cart. There is also the ”Contacto” section that is not yet implemented for the delivery of this report: 

Figure 8.25: Home Page Web 

## **”Inicio”** 

Here you will find the first visual impression of the website where there is a banner and below are the products that are in greatest demand among customers accompanied by miniatures of the products with direct links to add them to the cart. The latest products added to our inventory are also presented: 

94 

Figure 8.26: Best selling products 

Figure 8.27: Product Details Display 

## **Categorias** 

Being on this category we will find a Dropdown of Categories where we will have: 

95 

- ”TODOS”: A link that directs to a page where all available products are displayed without filtering by specific category. 

- ”VIDEO JUEGOS”: Link that shows products that are video games. 

- FUNKO POPS: Page dedicated to products from the Funko Pops category. 

- CONSOLAS: Video game console products, including latest generation consoles and previous models. 

- ”COLECCIONABLES”: Section that contains collectible products such as figures, limited editions, or items of interest to collectors. 

- ”ACCESORIOS” : Products related to accessories for video games or other electronic products are shown here. 

Figure 8.28: Dropdown of Categoriesy 

96 

Figure 8.29: Example of Categoriesy Section 

## **Blog** 

Space where articles, news, product reviews, and relevant content for users are published. Each blog post includes images and detailed text: 

Figure 8.30: Blog Section 

97 

## **Login** 

You enter here by clicking on the person icon in the navigation bar. It will redirect us to the login section where the login form will be found for registered users to access their personal accounts: 

Figure 8.31: Login Section 

When you log in, the user is redirected to the main window and clicking the person icon again in the navigation bar will display the user’s profile data: 

98 

Figure 8.32: Login Demonstration 

Figure 8.33: User Profile 

If you do not have an account, you can click the Register button so that new users can create accounts on your website: 

99 

Figure 8.34: Registration Section 

## **Shopping Cart** 

This section is accessed by clicking on the cart icon in the navigation bar. Here users can see the products they have selected to purchase. At the moment, only the storage of products and the change in purchase quantities corresponding to the maximum in inventory is implemented: 

Figure 8.35: Shopping Cart Section 

100 

## **Search bar** 

Clicking on the magnifying glass icon in the navigation bar will display a bar where users can write the name of any product they are looking for and upon clicking ENTER the user will be redirected to the ’All’ category section where the products will be displayed. that match the search performed: 

Figure 8.36: Search Bar 

Figure 8.37: Search Result Example 

101 

## **8.7.2 Mobile Manual** 

## **User Guide for Navigating in the Mobile App** 

Once we have the mobile app on our device, we should get in it. 

Figure 8.38: Mobile App 

## **Login** 

The first screen that is going to appear when you open the mobile app is the login. Now in development, we have two buttons. The first login is going to be an authentication that is going to let you in only if you have the credentials of a PRICOTERCORP’s employee. The other button is going to let you in without any credentials, so in this case we use the Bypass Login (the button is only there until the development stage is finished) 

102 

Figure 8.39: Mobile Login 

## **Sale Spots screen** 

After we login, the app is going to display a list of the sale spots of the company PRICOTERCORP S.A. in this case we can select any commercial center that we are interested in. 

103 

Figure 8.40: Sale Spot 

**Home screen** 

Once we have selected a sale spot, we are going to be directed to the “home page” this screen displays four options. 

104 

Figure 8.41: Home picture 

## **Create inventory** 

If we select the option “Crear inventario” the app is going to display the list of products with its properties (“ID”, “Anterior Stock”, “Actual Stock” , “Estado”) of the unfinished inventory that the user was working on. 

105 

Figure 8.42: Home picture Crear inventario 

106 

Figure 8.43: Inventory List 

Here are some important points to take into mind. The first element of this page is going to be the search bar, in this tool we can put as an input the name, ID or state of a product and automatically is displaying the related product with the input. As you can see in the next picture: 

107 

Figure 8.44: Inventory seek option 

By selecting confirm you are going to return to the list of products in the inventory applying the changes. 

The other part to take in mind are the products that appear in this list, by selecting one of them just pressing on them. The app is going to display the following widget In the real environment, the main goal of the user is going to change the “current Stock” with the total number of products that are in the local, so, in this widget is possible to do that just introducing the number. An also, in the same way you can modify the others properties. 

108 

Figure 8.45: Object view 

## **Inventory Details screen** 

While working on the inventory, you can save drafts to work later. To do this we have to select the option “Detalles” in the bottom bar. After selecting that option, the following screen is going to appear: 

109 

Figure 8.46: Details view 

Here are the details of the inventory, the ID of the inventory, the name of the person that created the inventory. The inventory duration based on the lapse of time between the creation date and the current date. If everything is okay push the “SAVE DRAFT” button, you should see the following message in the bottom of the screen. 

Figure 8.47: Mobile App Details view 

**Inventory Report screen** Once the inventory is finished, we should go to option “Reporte” in the bottom bar of the screen. After selecting that the next screen is going to be displayed: 

110 

Figure 8.48: Mobile App Report view 

Here are going to appear the “inconsistence” of the inventory, this is going to be helpful to track the advance of the items already checked on the inventory. Once the user feels ready to declare an inventory as finished. We only are going to push the button “FINALIZE” and the app is going to eport a report.docx with all the issues. 

## **Inventory History screen** 

In other part, if in the home. We select the option “Historial” the App is going to display a list of the previous inventories with its state (finished or working) 

111 

Figure 8.49: Mobile App History selection 

112 

Figure 8.50: Mobile App History view 

## **Inventory settings screen** 

In other part, if in the home. We select the option “Ajustes” the App is going to display the following settings: the notification, account settings, and the version of the app. 

113 

Figure 8.51: Mobile App settings selection 

114 

Figure 8.52: Mobile App settings view 

The selection of the option “About” is going to show the information of the App and its developers. 

115 

Figure 8.53: Mobile App settings developers 

## **Inventory Log out screen** 

Finally, the option “salir” is going to close the app. 

116 

Figure 8.54: Mobile App logout view 

117 

## **8.8 Appendix H: Asana activity schedule** 

We have sent an invitation to our Software Engineering 2 professor to join our group’s Asana project. This will allow the professor to review the project’s structure and monitor our progress. By joining, the professor can provide feedback and ensure that we are on the right track with our project management and organization. 

Figure 8.55: Asana activity schedule 

118 

