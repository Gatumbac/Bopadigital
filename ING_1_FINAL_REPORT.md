#### BOPACORP S.A. Final Project Specification Document 

##### by 

##### Grupo 2 BOPADIGITAL 

###### PROJECT PRESENTED TO ESCUELA SUPERIOR POLITÉCNICA DEL LITORAL 

GUAYAQUIL, JANUARY 12, 2026 

###### ESCUELA SUPERIOR POLITÉCNICA DEL LITORAL ESPOL 

Grupo 2 BOPADIGITAL, 2026 

This Creative Commons license allows readers to download this work and share it with others as long as the author is credited. The content of this work cannot be modified in any way or used commercially. 

###### **TEAM MEMBERS** 

THIS PROJECT HAS BEEN DEVELOPED 

BY THE FOLLOWING GROUP OF STUDENTS 

Shirley Aragon Facultad de Ingenieria en Electricidad y Computación 

Nahim Díaz 

Facultad de Ingenieria en Electricidad y Computación 

Salvador Muñoz 

Facultad de Ingenieria en Electricidad y Computación 

Gabriel Tumbaco 

Facultad de Ingenieria en Electricidad y Computación 

Anthony Navarrete Facultad de Ingenieria en Electricidad y Computación 

###### **TABLE OF CONTENTS** 

Page 

|CHA|PTER 1<br>RISK MANAGEMENT, SPRINT BACKLOGS, AND PROJECT<br>SCHEDULING .................................................................1|
|---|---|
|1.1|Risk Management .........................................................................1<br>|
||1.1.1<br>Identifed Risks for the BOPADIGITAL Project ..............................1|
|1.2|Product backlog .......................................................................... 4|
|1.3|Sprint Backlog ........................................................................... 11|
||1.3.1<br>Sprint 1: Foundation, Auth & Public Web (Weeks 1–4) .................... 11|
||1.3.2<br>Sprint 2: CRM Core & Geolocation (Weeks 5–8) .......................... 12|
|1.4|Scheduling ............................................................................... 14|
|CHA|PTER 2<br>STATIC SYSTEM MODELING AND ARCHITECTURAL DESIGN .... 16|
|2.1|Use Case Diagram ...................................................................... 18|
|2.2|Use Case Documentation ............................................................... 21|
|2.3|Class Diagrams .......................................................................... 92|
|2.4|Object Diagrams .......................................................................102|
|2.5|Components Diagram ..................................................................108|
|2.6|Deployment Diagram ..................................................................110|
|CHA|PTER 3<br>SYSTEM BEHAVIORAL MODELING ....................................112|
|3.1|Activity Diagrams .....................................................................113|
|3.2|Sequence Diagrams ....................................................................118|
|3.3|Collaboration–Communication Diagrams ............................................ 151|
|3.4|State Diagrams .........................................................................155|
|CHA|PTER 4<br>INDIVIDUAL CONTRIBUTIONS .........................................159|
|CHA|PTER 5<br>AUTHORSHIP DECLARATION ..........................................160|
|APPE|NDIX I<br>PROTOTYPE ................................................................ 161|
|APPE|NDIX II<br>CLIENT ACCEPTANCE LETTER .........................................209|
|APPE|NDIX III REQUIREMENTS SPECIFICATION DOCUMENT ..................... 211|



###### **LIST OF TABLES** 

|||Page|
|---|---|---|
|Table 1.1|Risk Probability Classifcation ...........................................|......1|
|Table 1.2|Identifed Risks and Mitigation Strategies for the BOPADIGITAL<br>Project .....................................................................|..... 3|
|Table 1.3|Product Backlog for the BOPADIGITAL Project .......................|.... 10|
|Table 1.4|Sprint 1 Backlog — Foundation, Authentication and Public Web .....|.... 11|
|Table 1.5|Sprint 2 Backlog — CRM Core, Geolocation, and Business Logic ...|.... 13|
|Table 1.6|Project Scheduling and Critical Path Overview .........................|.... 15|
|Table 2.1|Use Case Documentation - Contact an Advisor from the Catalog .....|.... 22|
|Table 2.2|Use Case Documentation - View Job Vacancies ........................|.... 24|
|Table 2.3|Use Case Documentation - Apply for a Job Vacancy ...................|.... 25|
|Table 2.4|Use Case Documentation - Access Control Panel with Credentials ....|.... 27|
|Table 2.5|Use Case Documentation - Manage Product Catalog ...................|.... 29|
|Table 2.6|Use Case Documentation - Register New Client ........................|.... 31|
|Table 2.7|Use Case Documentation - Update Existing Client .....................|.... 33|
|Table 2.8|Use Case Documentation -Edit Negotiations ...........................|.... 35|
|Table 2.9|Use Case Documentation - Register Visit ...............................|.... 37|
|Table 2.10|Use Case Documentation - View Visit History .........................|.... 39|
|Table 2.11|Use Case Documentation - Update negotiation status ..................|.... 41|
|Table 2.12|Use Case Documentation - Assign client to advisor ....................|.... 43|
|Table 2.13|Use Case Documentation - Unassign or remove client from an advisor|... 45|
|Table 2.14|Use Case Documentation - Disable closed negotiations ................|.... 47|
|Table 2.15|Use Case Documentation - View recent advisor activity ...............|.... 49|



III 

|Table 2.16|Use Case Documentation - View costs per advisor ......................... 51|
|---|---|
|Table 2.17|Use Case Documentation - Get progress report ............................. 53|
|Table 2.18|Use Case Documentation - Compare Metrics Between Advisors .......... 54|
|Table 2.19|Use Case Documentation - View Advisor Metrics .......................... 57|
|Table 2.20|Use Case Documentation - Filter Reports ................................... 60|
|Table 2.21|Use Case Documentation - Generate Sales and Closing Reports .......... 63|
|Table 2.22|Use Case Documentation - Filter Client Lists by Metrics .................. 66|
|Table 2.23|Use Case Documentation - Reject Matrices ................................ 69|
|Table 2.24|Use Case Documentation - Review Operator Availability .................. 71|
|Table 2.25|Use Case Documentation - Check Matrix Approval Status ................ 74|
|Table 2.26|Use Case Documentation - Consult Clients and Their Documentation<br>Status .......................................................................... 76|
|Table 2.27|Use Case Documentation - Download Documentation ..................... 78|
|Table 2.28|Use Case Documentation - Tag Documentation ............................ 80|
|Table 2.29|Use Case Documentation - Review Documentation Uploaded to Profle .. 82|
|Table 2.30|Use Case Documentation - Add Client Documentation .................... 84|
|Table 2.31|Use Case Documentation - Review and Approve New Matrices ........... 86|
|Table 2.32|Use Case Documentation - Request Supervisor Approval .................. 88|
|Table 2.33|Use Case Documentation - Create Ofer Matrix for Specifc Clients ...... 90|
|Table 4.1|Individual Contributions of the Project .....................................159|



###### **LIST OF FIGURES** 

|||Page|
|---|---|---|
|Figure 1.1|Activity on Arrow Diagram .........................................|........ 15|
|Figure 2.1|BOPADIGITAL Use Case Diagram Part 1 .........................|........ 18|
|Figure 2.2|BOPADIGITAL Use Case Diagram Part 2 .........................|........ 20|
|Figure 2.3|BOPADIGITAL Class Diagram Overview .........................|........ 93|
|Figure 2.4|BOPADIGITAL Auth Module Class Diagram .....................|........ 94|
|Figure 2.5|BOPADIGITAL CoreUsers Module Class Diagram ...............|........ 95|
|Figure 2.6|BOPADIGITAL CRM Module Class Diagram ....................|........ 96|
|Figure 2.7|BOPADIGITAL Documents Module Class Diagram ..............|........ 97|
|Figure 2.8|BOPADIGITAL Employability Module Class Diagram ...........|........ 98|
|Figure 2.9|BOPADIGITAL OferMatrices Module Class Diagram ...........|........ 99|
|Figure 2.10|BOPADIGITAL Reports Module Class Diagram ..................|.......100|
|Figure 2.11|BOPADIGITAL ServiceCatalogCMS Module Class Diagram ...|....... 101|
|Figure 2.12|BOPADIGITAL CRM Object Diagram Overview .................|.......103|
|Figure 2.13|BOPADIGITAL OferMatrix Object Diagram Overview .........|.......104|
|Figure 2.14|BOPADIGITAL Catalog Object Diagram Overview ..............|.......105|
|Figure 2.15|BOPADIGITAL Auth Object Diagram Overview .................|.......106|
|Figure 2.16|BOPADIGITAL Documents Object Diagram Overview ..........|.......107|
|Figure 2.17|BOPADIGITAL Components Object Diagram ....................|.......109|
|Figure 2.18|BOPADIGITAL Deployment Diagram .............................|....... 111|
|Figure 3.1|BOPADIGITAL Activity Diagram – Negotiation Life Cycle .....|.......113|
|Figure 3.2|BOPADIGITAL Activity Diagram – Ofer Matrices ..............|.......114|
|Figure 3.3|BOPADIGITAL Activity Diagram – Visit Management ..........|.......115|



V 

|Figure 3.4|BOPADIGITAL Activity Diagram – Auth ................................116|
|---|---|
|Figure 3.5|BOPADIGITAL Activity Diagram – Document Management ...........117|
|Figure 3.6|BOPADIGITAL Sequence Diagram - registerVisit ......................119|
|Figure 3.7|BOPADIGITAL Sequence Diagram - reviewVisit .......................120|
|Figure 3.8|BOPADIGITAL Sequence Diagram - updateNegotiationStatus ......... 121|
|Figure 3.9|BOPADIGITAL Sequence Diagram - checkVisitHistory ................122|
|Figure 3.10|BOPADIGITAL Sequence Diagram - deactivateClient ..................123|
|Figure 3.11|BOPADIGITAL Sequence Diagram - createOferMatrix ................124|
|Figure 3.12|BOPADIGITAL Sequence Diagram - addItemToMatrix<br>................125|
|Figure 3.13|BOPADIGITAL Sequence Diagram - recalculateTotals .................126|
|Figure 3.14|BOPADIGITAL Sequence Diagram - saveDraft .........................127|
|Figure 3.15|BOPADIGITAL Sequence Diagram - sendToSupervisor ................128|
|Figure 3.16|BOPADIGITAL Sequence Diagram - Login .............................129|
|Figure 3.17|BOPADIGITAL Sequence Diagram - listPendingMatrices ..............130|
|Figure 3.18|BOPADIGITAL Sequence Diagram - approveMatrix<br>................... 131|
|Figure 3.19|BOPADIGITAL Sequence Diagram - rejectMatrix ......................132|
|Figure 3.20|BOPADIGITAL Sequence Diagram - uploadDocument .................133|
|Figure 3.21|BOPADIGITAL Sequence Diagram - approveDocument<br>...............134|
|Figure 3.22|BOPADIGITAL Sequence Diagram - rejectDocument ..................135|
|Figure 3.23|BOPADIGITAL Sequence Diagram - downloadDocument<br>.............136|
|Figure 3.24|BOPADIGITAL Sequence Diagram - searchCatalog ....................137|
|Figure 3.25|BOPADIGITAL Sequence Diagram - flterCatalog ......................138|
|Figure 3.26|BOPADIGITAL Sequence Diagram - createCatalogItem<br>...............139|
|Figure 3.27|BOPADIGITAL Sequence Diagram – checkPermission .................140|



VI 

|Figure 3.28|BOPADIGITAL Sequence Diagram – editWebContents<br>................ 141|
|---|---|
|Figure 3.29|BOPADIGITAL Sequence Diagram – generateReport<br>..................142|
|Figure 3.30|BOPADIGITAL Sequence Diagram – exportReport .....................143|
|Figure 3.31|BOPADIGITAL Sequence Diagram – activeVacancies ..................144|
|Figure 3.32|BOPADIGITAL Sequence Diagram – applyToVacancy .................145|
|Figure 3.33|BOPADIGITAL Sequence Diagram – evaluateApplication .............146|
|Figure 3.34|BOPADIGITAL Sequence Diagram – submitApplication ...............147|
|Figure 3.35|BOPADIGITAL Sequence Diagram – registrateClient<br>..................148|
|Figure 3.36|BOPADIGITAL Sequence Diagram – assignClient ......................149|
|Figure 3.37|BOPADIGITAL Sequence Diagram – scheduleVisit<br>....................150|
|Figure 3.38|BOPADIGITAL Communication Diagram – Auth .......................152|
|Figure 3.39|BOPADIGITAL Communication Diagram – Approve Ofer Matrix ....153|
|Figure 3.40|BOPADIGITAL Communication Diagram – uploadDocument .........154|
|Figure 3.41|BOPADIGITAL State Diagram – Negotiation ............................155|
|Figure 3.42|BOPADIGITAL State Diagram – Ofer Matrix ...........................156|
|Figure 3.43|BOPADIGITAL State Diagram – Negotiation Document ................157|
|Figure 3.44|BOPADIGITAL State Diagram – Job Application .......................158|
|Figure I-1|BOPADIGITAL Prototype - Main view of the Sales Dashboard<br>displaying the Kanban board with customer distribution by stages. ..... 161|
|Figure I-2|BOPADIGITAL Prototype - Visualization of the ability to move clients<br>across stages within the Kanban board. ................................... 161|
|Figure I-3|BOPADIGITAL Prototype - Detailed view of the client , showing<br>contact information, interaction history, and visit planning panel. ......162|
|Figure I-4|BOPADIGITAL Prototype - “Edit Client” modal window allowing the<br>modifcation of tax information (RUC, Legal Name) and contact details. 162|



VII 

- Figure I-5 BOPADIGITAL Prototype - System notification displayed in the .....163 

- upper-right corner confirming the successful update of client data. 

- Figure I-6 BOPADIGITAL Prototype - “My Performance” screen displaying key KPI cards and the monthly revenue goal progress bar. ...................163 

- Figure I-7 BOPADIGITAL Prototype - Graphical analysis section within “My Performance”, detailing the client pipeline by stage and sales distribution by service. .....................................................164 

- Figure I-8 BOPADIGITAL Prototype - “Weekly Activity” area chart and ......164 

- commercial efficiency metrics (Average per Sale and Visit Rate). 

- Figure I-9 BOPADIGITAL Prototype - “Client Management” module presenting the complete tabular listing of the client portfolio with a global search bar. ..........................................................................165 

- Figure I-10 BOPADIGITAL Prototype - Demonstration of the client list filtering functionality, isolating only those in the “Negotiation” stage. ...........165 

- Figure I-11 BOPADIGITAL Prototype - “Add New Client” modal form for registering new prospects, capturing tax data (RUC), contact information, and initial stage. ..............................................166 

- Figure I-12 BOPADIGITAL Prototype - “Visit Calendar” module (January 2026 view) with status summary (Completed vs. Overdue) and monthly schedule visualization. .....................................................166 

- Figure I-13 BOPADIGITAL Prototype - Client management panel: visit history displayed on the left and mandatory document upload section on the right. ........................................................................167 

- Figure I-14 BOPADIGITAL Prototype - Calendar navigation to future months (February 2026), enabling long-term visit planning and scheduling. ....167 

- Figure I-15 BOPADIGITAL Advisor - "Offer Matrices" dashboard managing commercial proposals, displaying status counters (Drafts, Pending, Approved) and a list of client proposals with subsidy details. ...........168 

- Figure I-16 BOPADIGITAL Advisor - "New Offer Matrix" modal allowing the creation of a commercial proposal by selecting a client, adding products, and uploading necessary attachments. ....................................168 

VIII 

|Figure I-17|BOPADIGITAL Advisor - "Edit Ofer Matrix" interface for modifying<br>specifc line items within a proposal, such as adjusting quantities, unit<br>prices, and adding item-specifc notes. ....................................169|
|---|---|
|Figure I-18|BOPADIGITAL Advisor - Detailed view of an "Approved" Ofer<br>Matrix, highlighting the automatic subsidy calculation, fnal total, and<br>supervisor approval comments. ............................................169|
|Figure I-19|BOPADIGITAL CMS - Product and Services Catalog dashboard<br>displaying inventory statistics (Total, Active, Discontinued) and the<br>product grid. ................................................................170|
|Figure I-20|BOPADIGITAL CMS - Catalog fltering functionality, demonstrating<br>the isolation of products within the "Telephony" category. ..............170|
|Figure I-21|BOPADIGITAL CMS - Catalog view fltered by "Discontinued" status,<br>highlighting legacy services with distinct visual tags. ................... 171|
|Figure I-22|BOPADIGITAL CMS - Search bar functionality enabling quick<br>retrieval of specifc services (e.g., "Internet Fibra Óptica") by name. ... 171|
|Figure I-23|BOPADIGITAL CMS - "New Product" modal interface allowing<br>administrators to register new services with defned categories, pricing,<br>and status. ..................................................................172|
|Figure I-24|BOPADIGITAL CMS - "Edit Product" modal for modifying existing<br>service details, including descriptions, pricing attributes, and image<br>URLs. .......................................................................172|
|Figure I-25|BOPADIGITAL CMS - Security confrmation dialog ensuring<br>administrative verifcation before permanently removing a product<br>from the catalog. ...........................................................173|
|Figure I-26|BOPADIGITAL CMS - Web Content Editor dashboard used to manage<br>public-facing website elements, showing content status and preview<br>cards. ........................................................................173|
|Figure I-27|BOPADIGITAL CMS - Section fltering mechanism in the Web<br>Content Editor, allowing focused management of specifc page areas<br>(e.g., Main Banner). ........................................................174|
|Figure I-28|BOPADIGITAL CMS - Content modifcation modal for updating<br>website assets, including visibility toggles, display order, titles, and<br>subtitles. ....................................................................174|



IX 

|Figure I-29|BOPADIGITAL Admin - General Metrics Dashboard providing a<br>consolidated view of commercial performance, including sales totals,<br>conversion rates, and active team members. ..............................175|
|---|---|
|Figure I-30|BOPADIGITAL Admin - "Top Performers" section ranking sales<br>advisors based on closed sales value and visit volume. ..................175|
|Figure I-31|BOPADIGITAL Admin - Notifcation dropdown displaying real-time<br>alerts regarding document approvals and rejections for specifc clients. 176|
|Figure I-32|BOPADIGITAL Admin - System feedback (toast notifcation)<br>confrming that all alerts have been marked as read. .....................176|
|Figure I-33|BOPADIGITAL Admin - System feedback confrming the successful<br>deletion of notifcations from the user’s history. ..........................177|
|Figure I-34|BOPADIGITAL Admin - "Advisor Management" screen showing the<br>team roster, status indicators, and alerts for pending document reviews. 177|
|Figure I-35|BOPADIGITAL Admin - "New Advisor" modal form used to register<br>a new sales representative in the system. ..................................178|
|Figure I-36|BOPADIGITAL Admin - List view demonstrating the fltering<br>capability to isolate "Inactive" advisors. ..................................178|
|Figure I-37|BOPADIGITAL Admin - Advisor Profle Modal: "Change History"<br>tab tracking specifc actions and updates made by the advisor. ..........179|
|Figure I-38|BOPADIGITAL Admin - Advisor Profle Modal: "Assigned Clients"<br>tab displaying the advisor’s current portfolio and account status. .......179|
|Figure I-39|BOPADIGITAL Admin - Advisor Profle Modal: "Documents" tab<br>summarizing the approval status of fles uploaded by the advisor. ......180|
|Figure I-40|BOPADIGITAL Admin - Advisor Profle Modal: "Performance<br>Metrics" tab showing KPIs like total invoicing and sales conversion<br>rates. ........................................................................180|
|Figure I-41|BOPADIGITAL Admin - Advisor Profle Modal: "Recent Activities"<br>timeline logging the advisor’s latest interactions and system events. .... 181|
|Figure I-42|BOPADIGITAL Admin - "Contact Management" screen showing the<br>"Unassigned Contacts" tab, a pool of leads waiting for distribution. .... 181|
|Figure I-43|BOPADIGITAL Admin - Unassigned contacts fltered by the<br>"Prospecting" stage to prioritize early-stage lead distribution. ...........182|



X 

|Figure I-44|BOPADIGITAL Admin - Bulk selection of unassigned contacts to be<br>transferred to a specifc advisor (e.g., Patricia Vargas). ..................182|
|---|---|
|Figure I-45|BOPADIGITAL Admin - Toast notifcation confrming the successful<br>assignment of selected contacts to the target advisor. ....................183|
|Figure I-46|BOPADIGITAL Admin - "Assigned Contacts" tab displaying the<br>master list of clients that are currently managed by an advisor. ..........183|
|Figure I-47|BOPADIGITAL Admin - "Add New Client" modal allowing<br>administrators to manually inject new leads into the system. ............184|
|Figure I-48|BOPADIGITAL Admin - "Document Management" module for<br>centralized bulk processing (approve/reject) of client documentation. ..184|
|Figure I-49|BOPADIGITAL Admin - Document fltering functionality, showing<br>the list fltered by "Pending" status to prioritize urgent reviews. .........185|
|Figure I-50|BOPADIGITAL Admin - Selection mechanism allowing administrators<br>to choose specifc documents (or all) to perform bulk actions like<br>approval or rejection. .......................................................185|
|Figure I-51|BOPADIGITAL Admin - "Reject Document" modal requiring the<br>administrator to provide a mandatory reason for the rejection before<br>processing. ..................................................................186|
|Figure I-52|BOPADIGITAL Admin - System notifcation confrming the initiation<br>of a secure bulk download for the selected client documentation. .......186|
|Figure I-53|BOPADIGITAL Admin - "Commercial Performance Reports"<br>dashboard ofering a high-level overview of sales productivity and<br>team metrics. ...............................................................187|
|Figure I-54|BOPADIGITAL Admin - Advanced reporting flters applied to analyze<br>a specifc advisor’s performance (e.g., Roberto Mendoza) over the last<br>semester. ....................................................................187|
|Figure I-55|BOPADIGITAL Admin - "Export Report" function allowing data to<br>be generated and downloaded as a PDF fle for external presentation. ..188|
|Figure I-56|BOPADIGITAL Admin - "Recent Activity" audit log tracking system-<br>wide events such as closed sales, document uploads, and login sessions. 188|
|Figure I-57|BOPADIGITAL Admin - "Document Confguration" panel used to<br>defne mandatory or optional fle requirements for diferent sales stages. 189|



XI 

|Figure I-58|BOPADIGITAL Admin - "Edit Document Type" modal allowing<br>adjustments to validation rules, such as making a document mandatory<br>for all services. .............................................................189|
|---|---|
|Figure I-59|BOPADIGITAL Admin - "Delete Document Type" confrmation<br>modal ensuring the administrator intends to permanently remove a<br>confguration (e.g., "RUC") from the system. .............................190|
|Figure I-60|BOPADIGITAL Admin - "Add New Document Type" form allowing<br>the defnition of new mandatory or optional requirements, specifying<br>applicable sales stages and service scope. ................................190|
|Figure I-61|BOPADIGITAL Admin - "Sales Closings Report" dashboard providing<br>detailed transaction analysis, including total revenue, sales count, and<br>visual breakdowns by service type and geographic zone. ................ 191|
|Figure I-62|BOPADIGITAL Admin - Sales Report demonstrating fltering<br>capabilities, isolating performance data for a specifc advisor (e.g.,<br>Roberto Mendoza) over the "Last Semester" period. ..................... 191|
|Figure I-63|BOPADIGITAL Admin - "Export Report" functionality showing<br>system feedback (modal alert) confrming the generation of a PDF fle<br>containing the current sales data visualization. ...........................192|
|Figure I-64|BOPACORP Mobile App - Authentication and Main Dashboard views. 194|
|Figure I-65|BOPACORP Mobile App - Activity tracking and creation workfow. ...195|
|Figure I-66|BOPACORP Mobile App - Detailed activity logging and client portfolio<br>navigation. ..................................................................196|
|Figure I-67|BOPACORP Mobile App - Client administration and registration<br>interface. ....................................................................197|
|Figure I-68|BOPACORP Mobile App - Final step of the new client registration<br>process. .....................................................................198|
|Figure I-69|BOPACORP Mobile App - Comprehensive client profle and history<br>view. ........................................................................199|
|Figure I-70|BOPACORP Mobile App - Operational lists for daily task and portfolio<br>management. ...............................................................200|
|Figure I-71|BOPACORP Mobile App - User profle and application settings. ....... 201|
|Figure I-72|BOPACORP Mobile App - Administrative control panel and statistics. 202|



XII 

- Figure I-73 BOPACORP Mobile App - Advanced system management and user administration. .............................................................203 

- Figure I-74 BOPACORP Mobile App - Administrative tools for user onboarding and service catalog maintenance. .........................................204 

- Figure I-75 BOPACORP Website - Homepage featuring the main value proposition, navigation menu, and quick access to services and company information. ................................................................205 

- Figure I-76 BOPACORP Website - "About Us" section detailing the company’s history, mission, and vision statements to establish corporate identity. .205 

- Figure I-77 BOPACORP Website - complete Service Catalog displaying available .....206 

- corporate plans with filtering options by category, zone, and price. 

- Figure I-78 BOPACORP Website - Service Detail Modal for "Plan Corporativo ...206 

- 100", showing specific costs, coverage zones, and included benefits. 

- Figure I-79 BOPACORP Website - Search results view demonstrating active filters (Cloud, Digital Services, National Coverage) applied to the catalog. ...207 

- Figure I-80 BOPACORP Website - "Work with Us" (Careers) page highlighting ......................207 

- employee benefits and listing current job openings. 

- Figure I-81 BOPACORP Website - Job Application Modal allowing candidates to ....208 

- submit personal details and upload their CV for a specific position. 

- Figure I-82 BOPACORP Website - Success confirmation modal providing feedback to the user that their job application has been successfully sent. ........208 

###### **LIST OF ABBREVIATIONS** 

BOPACORP S.A. Telecommunications company and main client of the project 

BOPADIGITAL Digital platform developed for BOPACORP S.A. 

B2B Business-to-Business (commercial model between companies) CMS Content Management System – module for website content administration CRM Customer Relationship Management – module for managing business clients and negotiations DOC Document Management Module EMP Employability / Application Module MAT Offer Matrix Module REP Reporting Module SUP Supervision and Approvals Module CAT Catalog and Website Module SEG Basic Security Module NOT Notifications Module GPS Global Positioning System UI User Interface UX User Experience JWT JSON Web Token (authentication mechanism) TLS Transport Layer Security (encryption protocol for HTTPS) PDF Portable Document Format 

XIV 

KPI Key Performance Indicator RUC Unique Taxpayer Registry ID Identifier (unique reference or key) 

###### **LIST OF SYMBOLS AND UNITS OF MEASUREMENTS** 

% Percentage (used in performance indicators such as availability or success rate) 

s Seconds (used for system response times, e.g., 3 s) 

MB Megabytes (used for file upload size limits, e.g., 50 MB) 

h Hours (used for availability and operational timeframes) 

###### **CHAPTER 1** 

###### **RISK MANAGEMENT, SPRINT BACKLOGS, AND PROJECT SCHEDULING** 

###### **1.1 Risk Management** 

In this section, we identify, quantify, and classify the various risks that may arise during the software development process of _BOPADIGITAL_ . Additionally, a detailed assessment of the likelihood of occurrence, the potential impact of each risk, and the corresponding protocols to be followed in the event that they materialize is provided. 

|**Description**|**Probability Range**|
|---|---|
|Not Probable: The event is highly unlikely to occur.|0% – 20%|
|Low Probability: The event is unlikely but possible.|21% – 40%|
|Moderate Probability: The event has an even chance|41% – 60%|
|of occurring.||
|High Probability: The event is likely to occur.|61% – 80%|
|Very High Probability: The event is almost certain<br>to occur.|81% – 100%|



Table 1.1 Risk Probability Classification 

###### **1.1.1 Identified Risks for the BOPADIGITAL Project** 

The following table outlines the risks identified for the _BOPADIGITAL_ project, specifically associated with its functional modules (CRM, MAT, DOC, SUP) and operational environment. 

2 

|**ID**|**Risk Name**|**Risk Description**|**Probability**|**Impact**|**Action Protocol**|
|---|---|---|---|---|---|
|001|Field<br>Connectivity<br>Failures|Sales advisors may lose<br>network<br>connectivity<br>when<br>uploading<br>visits<br>or documents in remote<br>areas.|Very High|Critical|Implement<br>a<br>robust<br>_ofine-frst_<br>architecture<br>that<br>stores<br>data<br>locally<br>and<br>synchronizes<br>automatically<br>once<br>connectivity<br>is<br>restored.|
|002|Geolocation<br>Inaccuracy|Visit records depend on<br>accurate GPS coordinates,<br>which may vary across<br>devices or environments.|High|High|Apply<br>tolerance<br>thresholds for location<br>validation and allow<br>supervised<br>manual<br>correction with system<br>justifcation when GPS<br>data is unreliable.|
|003|Subsidy<br>Calculation<br>Complexity<br>(MAT)|Business<br>rules<br>for<br>automatic<br>ofer<br>and<br>subsidy calculations may<br>be<br>misinterpreted<br>or<br>incorrectly implemented.|Moderate|High|Validate<br>calculation<br>formulas with fnancial<br>stakeholders<br>before<br>development<br>and<br>implement exhaustive<br>unit<br>tests<br>for<br>the<br>calculation engine.|



3 

_Table continued from previous page_ 

|**ID**|**Risk Name**|**Risk Description**|**Probability**|**Impact**|**Action Protocol**|
|---|---|---|---|---|---|
|004|Sales<br>Staf<br>Resistance<br>to<br>Change|Users<br>accustomed<br>to<br>manual processes may<br>resist adopting the mobile<br>application.|High|Moderate|Design<br>an<br>intuitive<br>UX/UI and implement<br>a training plan focused<br>on<br>demonstrating<br>productivity<br>and<br>administrative<br>workload reduction.|
|005|Storage Overload<br>(DOC Module)|Massive<br>uploads<br>of<br>contract images and legal<br>documents may exceed<br>the<br>projected<br>storage<br>capacity.|Low|High|Enable<br>client-side<br>image<br>compression<br>and<br>use<br>scalable<br>storage services with<br>defned<br>retention<br>policies.|
|006|Approval<br>Role<br>and Permission<br>Changes|The approval hierarchy<br>(Advisor →Supervisor<br>→Manager) may change<br>during development or<br>operation.|Moderate|Moderate|Develop<br>a<br>fexible,<br>database-driven RBAC<br>system that supports<br>dynamic confguration<br>without<br>hardcoded<br>logic.|



Table 1.2 Identified Risks and Mitigation Strategies for the BOPADIGITAL Project 

4 

###### **1.2 Product backlog** 

|**ID**|**Priority**|**Dependencies**|**Backlog Item Description**|**Estimation**<br>**(hours)**|
|---|---|---|---|---|
|PB1|0|None|Research and Environment: Investigation<br>of the architecture (Docker, Node.js, React).<br>Confguration of the Git repository, branch<br>strategy, and CICD pipeline basics. Includes<br>creation of the initial "Hello World" to verify<br>connectivity.|6|
|PB2|0|PB1|Database Architecture: Design the complete<br>database schema (PostgreSQL) including<br>tables for Users, Clients, Matrices, Subsidies,<br>and Visits. Generation of the ER Diagram<br>and initial migration scripts.|6|
|PB3|0|PB1|Cloud Storage Setup:<br>Confguration of<br>the fle storage service (e.g., AWS S3 or<br>local server storage) to handle PDF and<br>image uploads securely.<br>Includes access<br>key generation.|4|
|PB4|0|PB1|Backend Foundation: Setup of the Express.js<br>server, error handling middleware, CORS<br>confguration, and connection pooling for<br>the database.|4|
|PB5|1|PB2, PB4|Authentication<br>Logic<br>(Backend):<br>Implementation<br>of<br>JWT<br>(JSON<br>Web<br>Token) strategy, password hashing (Bcrypt),<br>and login/register endpoints.|8|



5 

###### _Table continued from previous page_ 

|**ID**|**Priority**|**Dependencies**|**Backlog Item Description**|**Estimation**<br>**(hours)**|
|---|---|---|---|---|
|PB6|1|PB5|As a System Admin, I want to create<br>user accounts with specifc roles (Advisor,<br>Supervisor, Manager) so that I can control<br>who accesses the platform.|6|
|PB7|1|PB5|As a Sales Advisor, I want to log in to the<br>Web Portal using my credentials so that I<br>can access my dashboard securely.|4|
|PB8|1|PB5|As a Sales Advisor, I want to log in to the<br>Mobile App using my credentials so that I<br>can work from the feld.|6|
|PB9|2|PB7|As a User, I want to reset my password via<br>email verifcation in case I forget it, ensuring<br>I can recover access to my account.|8|
|PB10|2|PB1|Landing Page Structure: Implementation<br>of the main public website layout (Header,<br>Footer, Navigation) using React.|6|
|PB11|2|PB10|As a Visitor, I want to view the "About Us"<br>and "Contact" sections on the public site so<br>that I can learn about BOPACORP.|4|
|PB12|2|PB2, PB10|As a Visitor, I want to browse the Service<br>Catalog by categories so that I can easily<br>fnd the services I need.|8|
|PB13|2|PB12|As a Visitor, I want to search for specifc<br>services in the catalog using keywords so<br>that I can fnd information faster.|4|



6 

###### _Table continued from previous page_ 

|**ID**|**Priority**|**Dependencies**|**Backlog Item Description**|**Estimation**<br>**(hours)**|
|---|---|---|---|---|
|PB14|3|PB10|As an Applicant, I want to fll out a "Work<br>with Us" form on the public site so that I can<br>apply for a job.|6|
|PB15|3|PB3, PB14|As an Applicant, I want to upload my CV<br>(PDF) through the form so that HR can<br>review my profle.|6|
|PB16|1|PB2, PB4|Client Management API: Development of<br>backend endpoints (GET, POST, PUT,<br>DELETE) for the Clients and Prospects<br>table.|6|
|PB17|1|PB7, PB16|As a Sales Advisor, I want to register a new<br>Client on the Web Dashboard, entering their<br>RUC, name, and address.|6|
|PB18|1|PB8, PB16|As a Sales Advisor, I want to register a new<br>Client from the Mobile App, so that I can<br>add prospects while in the feld.|8|
|PB19|1|PB17|As a Sales Advisor, I want to edit client<br>information on the Web to correct errors or<br>update contact details.|4|
|PB20|1|PB16|As a Sales Advisor, I want to flter my client<br>list by status (Active/Inactive) or name, so I<br>can fnd specifc accounts quickly.|4|
|PB21|1|PB2|Geolocation Service: Implementation of the<br>backend logic to store and query geospatial<br>data (Latitude/Longitude) for visit records.|6|



7 

###### _Table continued from previous page_ 

|**ID**|**Priority**|**Dependencies**|**Backlog Item Description**|**Estimation**<br>**(hours)**|
|---|---|---|---|---|
|PB22|1|PB8, PB21|As a Sales Advisor, I want to view a map on<br>the Mobile App showing my current location<br>to verify my GPS is working.|6|
|PB23|1|PB22|As a Sales Advisor, I want to "Check-In"<br>at a client’s location using the Mobile App<br>so that my visit start time and location are<br>recorded.|8|
|PB24|1|PB23|As a Sales Advisor, I want to "Check-Out"<br>adding a summary note of the visit so that<br>the interaction is fully documented.|6|
|PB25|1|PB24|As a Supervisor, I want to view the history of<br>visits for my team on a map or list to monitor<br>feld compliance.|6|
|PB26|1|PB2|Matrix Calculation Engine: Implementation<br>of the backend logic to calculate base prices,<br>apply subsidies, and compute taxes.|10|
|PB27|1|PB7, PB26|As a Sales Advisor, I want to create a new<br>"Ofer Matrix" on the Web, selecting a client<br>to start the quoting process.|4|
|PB28|1|PB27|As a Sales Advisor, I want to add multiple<br>services/products to the matrix so that I can<br>build a comprehensive ofer.|6|
|PB29|1|PB26, PB28|As a Sales Advisor, I want the system to<br>automatically calculate the total cost and<br>applicable subsidies as I add items.|8|



8 

###### _Table continued from previous page_ 

|**ID**|**Priority**|**Dependencies**|**Backlog Item Description**|**Estimation**<br>**(hours)**|
|---|---|---|---|---|
|PB30|2|PB29|As a Sales Advisor, I want to save the Matrix<br>as a "Draft" so that I can continue working<br>on it later without losing progress.|4|
|PB31|2|PB29|As a Sales Advisor, I want to generate a PDF<br>preview of the ofer so that I can show it to<br>the client for immediate review.|8|
|PB32|2|PB31|As a Sales Advisor, I want to email the PDF<br>ofer directly to the client from the system<br>to speed up communication.|4|
|PB33|2|PB3|Document Management API: Backend setup<br>to handle multipart form data for uploading<br>legal documents linked to a Matrix.|6|
|PB34|2|PB33|As a Sales Advisor, I want to upload the<br>Client’s RUC and ID scans to the specifc<br>Ofer Matrix to fulfll legal requirements.|6|
|PB35|2|PB34|As a Sales Advisor, I want to validate that<br>the uploaded fles are readable and within<br>the size limit before saving.|4|
|PB36|2|PB30, PB34|As a Sales Advisor, I want to submit a<br>completed Matrix for approval, changing<br>its status to "Pending".|2|
|PB37|2|PB36|As a Supervisor, I want to receive a<br>notifcation (in-app or email) when an<br>advisor submits a matrix for approval.|4|



9 

###### _Table continued from previous page_ 

|**ID**|**Priority**|**Dependencies**|**Backlog Item Description**|**Estimation**<br>**(hours)**|
|---|---|---|---|---|
|PB38|2|PB37|As a Supervisor, I want to view a "Pending<br>Approvals" inbox so that I can see which<br>ofers require my attention.|4|
|PB39|2|PB38|As a Supervisor, I want to view the details<br>and documents of a pending Matrix to decide<br>whether to approve it.|4|
|PB40|2|PB39|As a Supervisor, I want to Approve a matrix<br>so that the sale can be fnalized and sent to<br>billing.|2|
|PB41|2|PB39|As a Supervisor, I want to Reject a matrix<br>with a mandatory comment explaining the<br>reason for rejection.|4|
|PB42|3|PB2|Reporting Queries: Optimization of SQL<br>queries to aggregate sales data by month,<br>advisor, and region.|6|
|PB43|3|PB42|As a General Manager, I want to view a<br>dashboard with a bar chart showing "Sales<br>vs Targets" for the current month.|8|
|PB44|3|PB43|As a General Manager, I want to export<br>the monthly sales report to an Excel fle for<br>further analysis.|6|
|PB45|0|All|Integration Testing: Execution of end-to-end<br>tests covering the fow from Client Creation<br>-> Visit -> Matrix -> Approval.|16|



10 

_Table continued from previous page_ 

|**ID**|**Priority**|**Dependencies**|**Backlog Item Description**|**Estimation**<br>**(hours)**|
|---|---|---|---|---|
|PB46|0|All|Production Deployment: Confguration of<br>the production server, environment variables,|8|
||||and fnal deployment of Web and Mobile<br>builds.||



Table 1.3 Product Backlog for the BOPADIGITAL Project 

11 

###### **1.3 Sprint Backlog** 

###### **1.3.1 Sprint 1: Foundation, Auth & Public Web (Weeks 1–4)** 

**Goal:** Establish the technical architecture, security layer, and the public-facing ecosystem (Web & Employability). 

|**Product Backlog**|**User Story / Description**|**Tasks**|**Assigned To**|
|---|---|---|---|
|**Item**||||
|PB1<br>–<br>PB4|Technical setup of the core|•<br>Repository<br>and<br>Docker|Gabriel Tumbaco|
|(Infrastructure)|infrastructure<br>including<br>containers, database, cloud<br>storage,<br>and<br>backend<br>services.|environment setup<br>•<br>Database schema creation<br>•<br>S3 bucket confguration<br>•<br>Express.js base confguration|Nahim Díaz|
|PB5 – PB9 (Auth|Implementation<br>of|•<br>Login<br>and<br>registration|Anthony|
|& Roles)|authentication<br>and<br>authorization<br>using<br>JWT and role-based access<br>control.|endpoints<br>•<br>Defnition of Admin, Advisor,<br>and User roles<br>•<br>Password recovery logic|Navarrete<br>Salvador Muñoz|
|PB10<br>–<br>PB13<br>(Public Web)|Development of the public-<br>facing website including<br>landing page and service<br>catalog.|•<br>React layout (Header and<br>Footer)<br>•<br>Dynamic service catalog<br>•<br>Search functionality|Gabriel Tumbaco<br>Shirley Aragon|
|PB14<br>–<br>PB15|Implementation<br>of<br>the|•<br>“Work with Us” form|Shirley Aragon|
|(Employability)|employability module for<br>applicant registration and<br>CV submission.|•<br>CV fle validation<br>•<br>Secure CV storage||



Table 1.4 Sprint 1 Backlog — Foundation, Authentication and Public Web 

12 

###### **1.3.2 Sprint 2: CRM Core & Geolocation (Weeks 5–8)** 

**Goal:** Enable the management of the client portfolio and tracking of field operations (Visits). 

|**Product Backlog**|**User Story / Description**|**Tasks**|**Assigned To**|
|---|---|---|---|
|**Item**||||
|PB16<br>–<br>PB20|Client CRUD operations|•<br>Client API (PostgreSQL)|Salvador Muñoz|
|(Client Mgmt)|and fltering for efective<br>portfolio management.|•<br>Web<br>forms<br>for<br>client<br>management<br>•<br>Mobile “Add Client” view<br>•<br>Search and status flters|Nahim Díaz<br>Anthony<br>Navarrete|
|PB21<br>–<br>PB22|Backend<br>geolocation|•<br>Spatial data setup (PostGIS /|Anthony|
|(Geo Services)|services and mobile map<br>visualization.|Geometry)<br>•<br>Mobile map integration|Navarrete<br>Shirley Aragon|
|PB23<br>–<br>PB25|Visit<br>tracking<br>through|•<br>Visit timer logic|Anthony|
|(Visit Logic)|check-in<br>and<br>check-out<br>processes.|•<br>Coordinate capture on check-<br>in<br>•<br>Supervisor visit map view|Navarrete<br>Nahim Díaz|
|PB26, PB29 (Calc<br>Engine)|Implementation of pricing,<br>subsidy,<br>and calculation<br>logic.|•<br>Subsidy calculation algorithm<br>•<br>Total cost computation|Shirley Aragon<br>Salvador Muñoz|
|PB27<br>–<br>PB28<br>(Matrix UI)|User interface for building<br>ofer matrices.|•<br>Product/service selection UI<br>•<br>Cart state management|Gabriel Tumbaco<br>Salvador Muñoz|
|PB30 (Drafts)|Save partially completed<br>matrices<br>for<br>later<br>continuation.|•<br>“Save as Draft” functionality|Salvador Muñoz|



13 

|**Product Backlog**<br>**Item**|**User Story / Description**|**Tasks**|**Assigned To**|
|---|---|---|---|
|PB31<br>–<br>PB32<br>(PDF & Email)|Generation and delivery of<br>ofer documents.|•<br>PDF library integration (e.g.,<br>PDFKit)<br>•<br>Email service confguration<br>(SMTP)|Nahim Díaz<br>Gabriel Tumbaco|
|PB33<br>–<br>PB35|Legal document upload and|•<br>Multipart upload API|Shirley Aragon|
|(Doc Upload)|validation.|•<br>ID / RUC scanning UI<br>•<br>File validation|Anthony<br>Navarrete|
|PB36<br>–<br>PB41|Supervisor<br>approval|•<br>State machine (Pending →|Anthony|
|(Approvals)|workfow for ofer matrices.|Approved / Rejected)<br>•<br>Notifcation system<br>•<br>Approval inbox UI|Navarrete<br>Salvador Muñoz|
|PB42<br>–<br>PB44<br>(Reporting)|Business<br>intelligence<br>dashboards<br>and<br>report<br>exports.|•<br>Aggregation queries (sales by<br>month)<br>•<br>Chart components (Recharts)<br>•<br>Excel export logic|Shirley Aragon<br>Nahim Díaz|
|PB45 (QA)|End-to-end validation of the<br>system.|•<br>Integration testing (Cypress /<br>Selenium)<br>•<br>Bug fxing sprint|All<br>Team<br>Members|
|PB46 (Deploy)|Final<br>production<br>deployment<br>and<br>documentation.|•<br>Server confguration<br>•<br>Domain setup and SSL<br>•<br>Final user manual|Nahim Díaz<br>Gabriel Tumbaco|



Table 1.5 Sprint 2 Backlog — CRM Core, Geolocation, and Business Logic 

14 

###### **1.4 Scheduling** 

|**ID**|**Description**|**Details**|**Product Backlog**<br>**Items**|**Hours**|**Earlies**<br>**Start**|**t**<br>**Latest**<br>**Finish**|**Float**|
|---|---|---|---|---|---|---|---|
|A|System<br>Foundation<br>& DB|Docker<br>setup,<br>PostgreSQL<br>schema,<br>and<br>backend<br>base<br>architecture.|PB1, PB2, PB3,<br>PB4|20|0|20|0|
|B|Auth & Security<br>Core|JWT, roles, and<br>user management<br>implementation.|PB5, PB6, PB7,<br>PB8, PB9|32|20|52|0|
|C|Public Ecosystem|Landing<br>page,<br>catalog,<br>and<br>employability<br>modules.|PB10–PB15|34|20|192|138|
|D|CRM<br>&<br>Field<br>Operations|Client<br>management,<br>geolocation, and<br>visit tracking.|PB16–PB25|60|52|112|0|
|E|Matrix<br>Calculation<br>Engine|Pricing, subsidies,<br>PDF<br>generation,<br>and drafts.|PB26–PB32|44|112|156|0|
|F|Docs & Approval<br>Workfow|Legal<br>docs,<br>validation,<br>and<br>approval<br>processes.|PB33–PB41|36|156|192|0|





<!-- Start of picture text -->
qsYy AGO) (3)1222 B(32) ( |=ol ) D(60) of E(44) Gq e F(36) qo[192/<br>(<{g G44) qeBy<br>eeT) arliest event time<br>LEY? Latest event time<br><!-- End of picture text -->

###### **CHAPTER 2** 

**STATIC SYSTEM MODELING AND ARCHITECTURAL DESIGN** 

17 

# ~~|~~ 



19 

Figure 2.1 BOPADIGITAL Use Case Diagram Part 1 



<!-- Start of picture text -->
Offer Matrix Management<br>Crear matrices para clientes específicos<br>CRM Operadora <<Include>><br>Filtrar listas de cliente segun metricas Consultar estado de aprobación de matrices Solicitar aprobación de supervisor<br>Revisar disponibilidad de operadora<br>Rechazar matrices<br>Supervisor Inmediato Visualizar y aprobar nuevas matrices <<Extend>><br>extension points<br>Rechazar matrices<br>Reporting, Performance & Analysis System Asesor Comercial<br>Document Management System<br>Filtrar reportes <<Extend>> Generar reportes de ventas y cierre extension points Filtrar reportes Añadir documentación de clienteEtiquetar documentación extension points <<Extend>><br><<Include>> Etiquetar documentación<br>Generar reportes en PDF o Excel Revisar documentación subida a perfil<br>extension points<br><<Include>> Administradores Descargar documentación <<Extend>><br>Comparar metricas entre asesores <<Extend>> Visualizar métricas de asesores extension points <<Include>> Descargar documentación<br>Comparar metricas entre asesores<br>Consultar clientes y su estado de<br>documentación Powered By�Visual Paradigm Community Edition<br><!-- End of picture text -->



Figure 2.2 BOPADIGITAL Use Case Diagram Part 2 

21 

**2.2 Use Case Documentation** 

22 

|**Name of Use Case:**<br>Co|ntact an Advisor fromthe Catalog|
|---|---|
|**Created By:**<br>BO|PADIGITAL<br>**Last Updated By:**<br>BOPADIGITAL|
|**Date Created:**<br>21|/12/25<br>**Last Revision**<br>**Date:**<br>11/01/2026|
|<br>**Description:**<br>|The Business Client browses the service catalog and requests to be contacted<br>by a sales advisor in order to start a negotiation about a product or service of<br>interest.<br>|
|**Actors: **|Business Client|
|**Preconditions:**|1. The public website must be accessible.<br>2. The service catalog must contain available products/services.<br>3. The contactform must befunctional.|
|**Postconditions:**|1. A contact request is registered in the system.<br>2. The business client receives an on-screen confirmation message.<br>3. The assigned advisor receives anotificationoftherequest.|
|**Flow:**|1. The Business Client accesses the BOPACORP public website.<br>2. The System displays the service catalog organized by categories<br>(Voice, Connectivity, Digital Services).<br>3. The Business Client navigates through the available categories.<br>4. The Business Client selects a specific service to view details.<br>5. The System displays service information including costs, benefits, and<br>usage conditions.<br>6. The Business Client clicks the “Contact Advisor” button.<br>7. The System displays a contact form requesting: Company Name, Tax<br>ID (RUC), Contact Name, Email, Phone Number.<br>8. The Business Client completes all form fields.<br>9. The Business Client clicks “Submit Request”.<br>10. The System validates the entered information.<br>11. The System creates a contact request record in the database.<br>12. The System displays a confirmation message: “We will contact you<br>shortly.”|
|**Alternative Flows:**|_10a. Validation fails_<br>1. The System displays specific error messages indicating missing or<br>invalid fields.<br>2. The Business Client corrects the information.<br>3. The flow returns to step 9.|
|**Exceptions:**|_2. Catalog unavailable or empty_<br>1. The System displays:_“Service catalog temporarily unavailable._<br>_Please try again later.”_<br>2. The use case ends.<br>_11. Contact request cannot be created_<br>1. The System displays:_“Your request could not be processed. Please_<br>_try again.”_<br>2. The use case ends.|



Table 2.1 Use Case Documentation - Contact an Advisor from the Catalog 

23 

**Requirements:** RF-CAT-004:  The system shall allow the business client to contact a sales advisor to initiate a negotiation regarding selected catalog items 

Table 2.1 (continued) 

24 

|**Name of Use Case:**<br>Vi|ew Job Vacancies|
|---|---|
|**Created By:**<br>BO|PADIGITAL<br>**Last Updated By:**<br>BOPADIGITAL|
|**Date Created:**<br>21|/12/25<br>**Last Revision**<br>**Date:**<br>11/01/2026|
|<br>**Description:**|The Candidate reviews the list of active job opportunities published by<br>BOPACORPto examinerequirements, job descriptions, and closing dates.|
|**Actors: **|SalesAdvisorCandidate|
|**Preconditions:**|1. The employability module must be active on the website.<br>2. The job database must be accessible.<br>3. Atleast one active job vacancymust exist.|
|**Postconditions:**|1. The candidate views detailedinformationofthe selected vacancy.|
|**Flow:**|1. The Candidate accesses the “Work With Us” section on the<br>BOPACORP website.<br>2. The System retrieves available vacancies from the database.<br>3. The System displays a list including Job Title, City, and Publication<br>Date.<br>4. The Candidate reviews the vacancy list.<br>5. The Candidate selects a specific vacancy.<br>6. The System displays full vacancy details including job description,<br>academicrequirements, years ofexperience, andresponsibilities.|
|**Alternative Flows:**|_2a. No active vacancies found_<br>1. The System displays:_“There are currently no open job_<br>_opportunities.”_<br>2. The System suggests subscribing to vacancy notifications.<br>3. The use case ends.|
|**Exceptions:**|_2. Database unavailable_<br>1. The System displays:_“Service temporarily unavailable. Please try_<br>_again later.”_<br>2. The System logs the error.<br>3. The use case ends.|
|**Requirements:**|RF-EMP-001:  The system shall allow the sales advisor candidate to view<br>available vacancies, displaying the position title, description, requirements,<br>andpublication date.|



Table 2.2 Use Case Documentation - View Job Vacancies 

25 

|**Name of Use Case:**<br>Ap|plyfora Job Vacancy|
|---|---|
|**Created By:**<br>BO|PADIGITAL<br>**Last Updated By:**<br>BOPADIGITAL|
|**Date Created:**<br>21|/12/25<br>**Last Revision**<br>**Date:**<br>11/01/2026|
|<br>**Description:**|The Candidate submits a formal job application by completing an application<br>formand uploading arésuméin PDF format.|
|**Actors: **|SalesAdvisorCandidate|
|**Preconditions:**|1. The candidate has viewed the vacancy details (UC-02).<br>2. The application system is operational.<br>3. Therésuméis availablein PDF format (max50MB).|
|**Postconditions:**|1. The job application is stored in the system.<br>2. The résumé file is stored and linked to the application.<br>3. The candidatereceives confirmationonscreenand by email.|
|**Flow:**|1. The Candidate is viewing the details of a job vacancy of interest.<br>2. The Candidate clicks the “Apply” button on the specific vacancy.<br>3. The System displays the application form requesting: Full Name,<br>National ID Number, Email, Phone Number, Address.<br>4. The Candidate completes all form fields with personal information.<br>5. The System requests uploading the résumé in PDF format with a<br>maximum size of 50MB.<br>6. The Candidate selects and uploads the résumé file from the device.<br>7. The System validates the file format and size.<br>8. The System validates that all required fields are complete and correct.<br>9. The Candidate clicks “Submit Application.”<br>10. The System stores the application in the database.<br>11. The System stores the résumé file.<br>12. The System sends a confirmation email to the provided address.<br>13. The System displays the success message: “Your application has been<br>successfully submitted.”|
|**Alternative Flows:**|_7a. If the file is not PDF:_<br>1. The System rejects the file and displays:_“Only PDF files are_<br>_allowed.”_<br>2. The flow returns to step 5.<br>_7b. If the file exceeds 50MB:_<br>1. The System rejects the file and displays:_“The file size must not exceed_<br>_50MB.”_<br>2. The flow returns to step 5.<br>_8a. If field validation fails:_<br>1. The System displays specific error messages for each invalid or<br>missing field.<br>2. The Candidate corrects the errors according to the instructions.<br>3. The flow returns to step 9.|



Table 2.3 Use Case Documentation - Apply for a Job Vacancy 

26 

|**Exceptions:**|_10. If application storage fails:_|
|---|---|
||1. The System displays the message:_“The application could not be_<br>_processed. Please try again.”_<br>2. The System logs the error for administrator review.<br>3. The use case ends.|
|**Requirements:**|RF-EMP-002,RF-EMP-003,RF-EMP-004,RF-EMP-005|



Table 2.3 (continued) 

27 

|**Name of Use Case:**<br>Ac|cess Control PanelwithCredentials|
|---|---|
|**Created By:**<br>BO|PADIGITAL<br>**Last Updated By:**<br>BOPADIGITAL|
|**Date Created:**<br>21<br>|/12/25<br>**Last Revision**<br>**Date:**<br>11/01/2026|
|**Description:**|The Web Administrator authenticates into the system using valid user<br>credentials (username and password) in order to access the Content<br>Management System(CMS) administrative controlpanel.|
|**Actors: **|WebAdministrator|
|**Preconditions:**|1. The administrator must have valid credentials previously registered in<br>the system.<br>2. The authentication service must be operational.<br>3. The administratoraccountmust be active.|
|**Postconditions:**|1. The administrator successfully gains access to the CMS<br>administration panel.<br>2. A user session is created with a valid JWT token.<br>3. The access event is recorded in the system log with date, time, and<br>user information.|
|**Flow:**|1. The Web Administrator navigates to the administrative login URL.<br>2. The System displays the login form with the following fields:<br>Username/Email and Password.<br>3. The Web Administrator enters their username or email.<br>4. The Web Administrator enters their password.<br>5. The Web Administrator clicks the “Log In” button.<br>6. The System validates the credentials against the users database.<br>7. The System verifies that the administrator account is active.<br>8. The System verifies the administrator role permissions.<br>9. The System generates a JWT token containing the user ID, role, and<br>expiration time.<br>10. The System creates a secure user session storing the token.<br>11. The System records the successful access event including timestamp<br>and IP address.<br>12. The System redirects the administratorto themainCMS dashboard.|
|**Alternative Flows:**|_6a. Invalid credentials (incorrect username or password)_<br>1. The System increments the failed login attempt counter for the<br>account.<br>2. The System displays the error message: “Invalid username or<br>password.”<br>3. The System allows the administrator to retry the login process.<br>4. The flow returns to step 2 of the main flow.<br>_6b. Three consecutive failed login attempts_<br>1. The System temporarily locks the account for 15 minutes.<br>2. The<br>System<br>displays<br>the<br>message:<br>“Account locked due to multiple failed login attempts. Please try again<br>in 15minutes.”|



Table 2.4 Use Case Documentation - Access Control Panel with Credentials 

28 

|3. The System sends a security alert email to the administrator.<br>4. The use case ends.<br>_7a. Inactive or disabled account_<br>1. The<br>System<br>displays<br>the<br>message:<br>“Your account is disabled. Please contact the system administrator.”<br>2. The use case ends.|
|---|
|**Exceptions:**_6. Authentication service unavailable_|
|1. The<br>System<br>displays<br>the<br>message:<br>**“**Authentication service temporarily unavailable. Please try again<br>later.”<br>2. The System logs the error for technical review.<br>3. The use case ends.<br>_9. JWT token generation failure_<br>1. The System logs the internal error.|
|**2. **The<br>System<br>displays<br>the<br>message:<br>“Login error. Please try again.”<br>3. The use case ends.|
|**Requirements:**RF-SEG-001:  The system shall require authentication using a valid<br>username and password to allow access to the internal application.<br>RF-CMS-001: The system shall allow the web administrator to access the<br>content management panel using credential-based authentication (username<br>and password).|



Table 2.4 (continued) 

29 

|**Name of Use Case:**<br>M|anageProduct Catalog|
|---|---|
|**Created By:**<br>BO|PADIGITAL<br>**Last Updated By:**<br>BOPADIGITAL|
|**Date Created:**<br>21|/12/25<br>**Last Revision**<br>**Date:**<br>11/01/2026|
|<br>**Description:**|The Web Administrator can create, edit, and delete products and services<br>within the public catalog of the BOPACORP website in order to keep service<br>informationupdated and availableforbusiness clients.|
|**Actors: **|WebAdministrator.|
|**Preconditions:**|1. The administrator must be authenticated in the system (Use Case 04).<br>2. The CMS module must be accessible.<br>3. The administrator musthave catalogmanagement permissions.|
|**Postconditions:**|1. All changes made are saved in the database.<br>2. Changes are immediately reflected in the public service catalog.<br>3. The system logs the operationwithuser, date, and actionperformed.|
|**Flow:**|1. The Web Administrator accesses the “Product Catalog” section within<br>the CMS panel.<br>2. The System retrieves and displays the current list of existing products<br>and services including: Name, Category, Price, and Status<br>(Active/Inactive).<br>3. The Web Administrator reviews the list of products.<br>4. The Web Administrator selects one available action: Register new<br>product, Edit existing product, or Delete product.<br>5. The System executes the corresponding flow based on the selected<br>action.<br>6. The System confirms the operation performed.<br>7. The Systemupdates the public catalogin realtime.|
|**Alternative Flows:**|_4a. Register new product_<br>1. The System displays a creation form with the following fields: Name,<br>Description, Category (Voice / Connectivity / Digital), Price, Benefits,<br>and Terms of Use.<br>2. The Web Administrator completes all required fields.<br>3. The Web Administrator optionally uploads a representative product<br>image.<br>4. The Web Administrator clicks “Save Product.”<br>5. The System validates that all mandatory fields are completed.<br>6. The System validates price format and numeric fields.<br>7. The System creates a new product record in the database.<br>8. The flow continues at step 6 of the main flow.<br>_4b. Edit existing product_<br>1. The System displays a pre-filled edit form with the current product<br>data.<br>2. The Web Administrator modifies the desired fields.<br>3. The Web Administrator clicks “Save Changes.”<br>4. The System validates the modified data.<br>5. The System updates the product record in the database.<br>6. The System logs themodificationwithdate, time, and user.|



Table 2.5 Use Case Documentation - Manage Product Catalog 

30 

|7. The flow continues at step 6 of the main flow.<br>_4c. Delete product_<br> <br> <br> <br> <br>|
|---|
|1. The<br>System<br>displays<br>a<br>confirmation<br>dialog:<br>“Are you sure you want to delete this product? This action cannot be<br>undone.”<br>2. The Web Administrator confirms the deletion.<br>3. The System verifies that the product is not referenced in active<br>negotiations.<br>4. The System removes the product from the active catalog.<br>5. The flow continues at step 6 of the main flow.|
|**Exceptions:**_5._Validation error (4a or 4b):<br>1. The System displays specific validation error messages.<br>2. The Web Administrator corrects the indicated errors.<br>3. The flow returns to the corresponding alternative flow step.<br>_3._Product referenced in active negotiations (4c):|
|1. The<br>System<br>displays<br>the<br>warning:<br>“This product cannot be deleted because it is used in active<br>negotiations.”<br>2. The System suggests disabling the product instead of deleting it.<br>3. Theflowreturns to step4ofthemain flow.|
|**Requirements:**RF-CMS-003:  The system shall allow the web administrator to create new<br>products and services within the catalog<br>RF-CMS-004:  The system shall allow the web administrator to update the<br>information of existing products and services in the catalog<br>RF-CMS-005:  The system shall allow the web administrator to delete<br>products and services from the catalog.|



Table 2.5 (continued) 

31 

|**Name of Use Case:**<br>Re|gisterNew Client|
|---|---|
|**Created By:**<br>BO|PADIGITAL<br>**Last Updated By:**<br>BOPADIGITAL|
|**Date Created:**<br>21|/12/25<br>**Last Revision**<br>**Date:**<br>11/01/2026|
|<br>**Description:**<br>|The Sales Advisor or Immediate Supervisor creates a new business client<br>recordinthe CRMsystem including allcommercialand contactinformation.<br>|
|**Actors: **|SalesAdvisor,Immediate Supervisor|
|**Preconditions:**|1. The user must be authenticated with the appropriate role.<br>2. The CRM module must be accessible.<br>3. The user musthave permissionto create clients.|
|**Postconditions:**|1. A new client record is created in the CRM database.<br>2. The client becomes available to be assigned to sales advisors.<br>3. Aunique clientID is generated by the system.|
|**Flow:**|1. The User navigates to the “Clients” section within the CRM module.<br>2. The User clicks the “Add New Client” button.<br>3. The System displays the client registration form with mandatory<br>fields.<br>4. The User enters the following information: Client RUC, Business<br>Name or Trade Name, Number of Active Services, Current Monthly<br>Billing, Contact Person Name, Contact Phone Number, Contact<br>Email, and Company Address.<br>5. The System validates the RUC format in real time.<br>6. The System verifies that the RUC does not already exist in the<br>database.<br>7. The User clicks “Save Client.”<br>8. The System validates that all mandatory fields are completed.<br>9. The System validates email and phone formats.<br>10. The System creates the client record in the database.<br>11. The System generates and assigns a unique client ID.<br>12. The Systemdisplays a successmessageincluding the clientID.|
|**Alternative Flows:**|_6a. RUC already exists_|
||1. The<br>System<br>displays<br>the<br>message:<br>“A client with this RUC already exists.”<br>2. The System displays a “View Existing Client” button.<br>3. The User may cancel or modify the entered RUC.<br>4. The use case ends if the user cancels.<br>_8a. Missing required fields_<br>1. The System highlights missing fields.<br>2. The<br>System<br>displays<br>the<br>message:<br>“Please complete all required fields.”<br>3. The User completes the missing information.<br>4. The flow returns to step 7.<br>_9a. Invalid email or phone format_<br>1. The Systemdisplays specific validation messages.|



Table 2.6 Use Case Documentation - Register New Client 

32 

|2. The User corrects the data.<br>3. The flow returns to step 7.|
|---|
|**Exceptions:**_10._  _Database failure_|
|1. The<br>System<br>displays<br>the<br>message:<br>“The client could not be created. Please try again.”<br>2. The System logs the error.<br>3. The entered data remains in the form.<br>4. The use case ends.|
|**Requirements:**RF-CRM-001:   The system shall allow the sales advisor to fill out a client<br>registration form including the company’s RUC (tax ID), business name,<br>number of active services,and current monthlybilling.|



Table 2.6 (continued) 

33 

|**Name of Use Case:**<br>Up|dateExisting Client|
|---|---|
|**Created By:**<br>BO|PADIGITAL<br>**Last Updated By:**<br>BOPADIGITAL|
|**Date Created:**<br>21|/12/25<br>**Last Revision**<br>**Date:**<br>11/01/2026|
|<br>**Description:**|The Sales Advisor or Immediate Supervisor updates contact, commercial, or<br>administrative information of an existing business client to keep records<br>current.|
|**Actors: **|SalesAdvisor,Immediate Supervisor|
|**Preconditions:**|1. The user must be authenticated in the system.<br>2. The client record must exist in the database.<br>3. Sales Advisors can only update clients assigned to them.<br>4. Immediate Supervisors canupdate any client withintheirteam.|
|**Postconditions:**|1. Client information is updated in the database.<br>2. The change history is recorded with date, time, and user.<br>3. The updates areimmediately visibleinthe client profile.|
|**Flow:**|4. The User accesses the CRM module.<br>5. The User searches for a client using RUC or Business Name.<br>6. The System displays a list of matching clients.<br>7. The User selects the client to update.<br>8. The System verifies the user’s permissions.<br>9. The System displays the client details form with current information.<br>10. The User modifies the desired fields.<br>11. The User clicks “Save Changes.”<br>12. The System validates the modified data.<br>13. The System updates the client record in the database.<br>14. The System records the change in the audit history.<br>15. The Systemdisplays a confirmation message.|
|**Alternative Flows:**|_5a. Unauthorized access_<br>1. The<br>System<br>displays:<br>“Access denied. This client is not assigned to you.”<br>2. The User is redirected to their assigned client list.<br>3. The use case ends.<br>_9a. Validation failure_<br>1. The System displays specific error messages.<br>2. The User corrects the errors.<br>3. The flow returns to step 8.|
|**Exceptions:**|_3._ _Search returns no results_<br>1. The<br>System<br>displays:<br>“No clients found with the given criteria.”<br>2. The User may modify the search or cancel.<br>_10. Database update failure_|



Table 2.7 Use Case Documentation - Update Existing Client 

34 

|1. The<br>System<br>displays:<br>“Changes could not be saved. Please try again.”<br>2. The System logs the error.<br>3. The use case ends if the user cancels.|
|---|
|**Requirements:**RF-CRM-002:   The system shall allow the sales advisor to update the<br>information of assigned business clients.|



Table 2.7 (continued) 

35 

|**Name of Use Case:**<br>Ed|it Negotiations|
|---|---|
|**Created By:**<br>BO|PADIGITAL<br>**Last Updated By:**<br>BOPADIGITAL|
|**Date Created:**<br>21|/12/25<br>**Last Revision**<br>**Date:**<br>11/01/2026|
|<br>**Description:**|The Sales Advisor modifies the details and observations of an ongoing<br>negotiation with an assigned business client in order to keep the commercial<br>progress updated.|
|**Actors: **|SalesAdvisor|
|**Preconditions:**|1. The sales advisor must be authenticated in the system.<br>2. The negotiation must exist in the system and be in active status.<br>3. The associated client must be assigned to the sales advisor.<br>4. Thenegotiation mustnot beinclosed orcanceled status.|
|**Postconditions:**|1. The negotiation details are updated in the database.<br>2. The changes are recorded in the negotiation history with a timestamp.<br>3. Thelastmodificationdate ofthenegotiation is updated.|
|**Flow:**|1. The Sales Advisor accesses the client profile within the CRM module.<br>2. The Sales Advisor navigates to the client’s negotiations section.<br>3. The System displays the active negotiations associated with the client<br>and their current status.<br>4. The Sales Advisor selects the specific negotiation to edit.<br>5. The Sales Advisor clicks the “Edit Negotiation” button.<br>6. The System displays the edit form with modifiable fields including:<br>Progress observations, Estimated closing date, and additional notes.<br>7. The Sales Advisor modifies the required fields.<br>8. The Sales Advisor clicks “Save Changes.”<br>9. The System validates that the entered data is correct (for example, a<br>valid future date).<br>10. The System updates the negotiation record in the database.<br>11. The System records the change in the negotiation history with<br>timestamp and user.<br>12. The System displays a confirmation message indicating that the<br>negotiationwas successfully updated.|
|**Alternative Flows:**|_9a._ _If data validation fails:_<br>1. The System displays specific error messages (for example: “The<br>closing date must be a future date”).<br>2. The Sales Advisor corrects the indicated errors.<br>3. The flow returns to step 8.|
|**Exceptions:**|_4. If the negotiation is in closed or canceled status:_<br>1. The System displays the message “Closed or canceled negotiations<br>cannot be edited.”<br>2. The System disables the edit option.<br>3. The use case ends.<br>_5._ _If the advisor attempts to edit a negotiation belonging to another advisor:_|



Table 2.8 Use Case Documentation -Edit Negotiations 

36 

||1. The System displays the message “Access denied. This negotiation<br>belongs to another advisor.”<br>2. The use case ends.<br>_10._ _If the database update fails:_<br>1. The System displays the message “Error saving changes. Please try<br>again.”<br>2. The System logs the error.<br>3. The use case ends.|
|---|---|
|**Requirements:**|RF-MAT-001:  The system shall allow the sales advisor to create a new offer<br>matrix associated with a business client and an ongoing negotiation.<br>RF-MAT-003:  The system shall automatically calculate the applicable<br>subsidy range based on client billing and the number of proposed services,<br>displayingthe total estimated benefit amount.|



Table 2.8 (continued) 

37 

|**Name of Use Case:**<br>Re|gisterVisit|
|---|---|
|**Created By:**<br>BO|PADIGITAL<br>**Last Updated By:**<br>BOPADIGITAL|
|**Date Created:**<br>21|/12/25<br>**Last Revision**<br>**Date:**<br>11/01/2026|
|<br>**Description:**|The Sales Advisor registers an in-person visit carried out with a business<br>client, including automatic GPS location, date, time, visit type, and meeting<br>observations.|
|**Actors: **|SalesAdvisor|
|**Preconditions:**|1. The advisor must be authenticated in the mobile application.<br>2. GPS functionality must be available and enabled on the mobile device.<br>3. The client must be assigned to the sales advisor.<br>4. Theremust be anactivenegotiationwiththe client.|
|**Postconditions:**|1. A visit record is created in the database with precise GPS coordinates.<br>2. The visit is automatically added to the client’s visit history.<br>3. The immediate supervisor can view and verify the registered visit.<br>4. The client’slast contact dateis updated.|
|**Flow:**|1. The Sales Advisor opens the BOPADIGITAL mobile application.<br>2. The Sales Advisor navigates to the profile of the client being visited.<br>3. The Sales Advisor clicks the “Register Visit” button.<br>4. The System requests location permissions if they are not enabled.<br>5. The System automatically captures the device’s GPS coordinates<br>including latitude, longitude, and accuracy.<br>6. The System displays the visit registration form pre-filled with current<br>date, current time, and captured GPS location.<br>7. The Sales Advisor selects the visit type from a dropdown list: Initial<br>Visit, Follow-up, Negotiation, Closing, or Post-Sale.<br>8. The Sales Advisor enters detailed observations and notes about the<br>visit.<br>9. The Sales Advisor clicks “Save Visit.”<br>10. The System validates that all required fields are completed.<br>11. The System creates a visit record linked to the client and the active<br>negotiation.<br>12. The System stores the GPS coordinates for later verification.<br>13. The System displays a confirmation message including the registered<br>GPS coordinates.|
|**Alternative Flows:**|_5a. If GPS is not available or the signal is weak:_<br>1. The System displays a warning message indicating that GPS is not<br>available.<br>2. The Sales Advisor can choose to wait for GPS signal, continue without<br>location, or cancel the registration.<br>3. If continuing without GPS, the flow proceeds without GPS data.<br>4. The visit is marked as “Unverified GPS.”<br>_10a. If validation fails:_<br>1. The System displays error messages indicating missing fields.<br>2. The SalesAdvisorcompletes therequiredinformation.|



Table 2.9 Use Case Documentation - Register Visit 

38 

||3. The flow returns to step 9.|
|---|---|
|**Exceptions:**|_4._ _If the user has denied location permissions:_<br>1. The System displays a message indicating that location permission is<br>required.<br>2. The System offers to open the device permission settings.<br>3. If permissions are not granted, the use case ends.<br>_11._ _If saving fails due to connectivity issues:_<br>1. The System displays an error message indicating connection issues.<br>2. The System temporarily stores the visit data locally.<br>3. The System synchronizes the data automatically once connectivity is<br>restored.|
|**Requirements:**|RF-CRM-005:   The system shall allow the sales advisor to register a new<br>client visit by entering date, time, observations, and GPS location<br>automaticallyobtained from their mobile device.|



Table 2.9 (continued) 

39 

|**Name of Use Case:**<br>Vi|ew VisitHistory|
|---|---|
|**Created By:**<br>BO|PADIGITAL<br>**Last Updated By:**<br>BOPADIGITAL|
|**Date Created:**<br>21|/12/25<br>**Last Revision**<br>**Date:**<br>11/01/2026|
|<br>**Description:**<br>|The Sales Advisor or Immediate Supervisor reviews the complete and<br>chronological history of all visits made to a specific business client for follow-<br>up analysis.<br>|
|**Actors: **|SalesAdvisor,Immediate Supervisor|
|**Preconditions:**|1. The user must be authenticated in the system.<br>2. The client record must exist in the database.<br>3. Sales Advisors can only view visits of their assigned clients.<br>4. Supervisors canview visits ofallclientsintheirteam.|
|**Postconditions:**|1. The visit history is displayed in descending chronological order.<br>2. The usercanviewfulldetails ofeach individualvisit|
|**Flow:**|1. The User accesses the client profile within the CRM module.<br>2. The User clicks the “Visit History” tab.<br>3. The System retrieves all visits associated with the client.<br>4. The System sorts visits by date and time in descending order.<br>5. The System displays a list of visits including date, time, visit type,<br>advisor, summarized observations, GPS location link, and verification<br>status.<br>6. The User selects a specific visit to view detailed information.<br>7. The System displays the full visit details including complete<br>observations and an interactive GPSmap.|
|**Alternative Flows:**|_3a. If no visits exist:_<br>1. The System displays a message indicating that no visits have been<br>registered.<br>2. If the user is an advisor, the system displays an option to register the<br>first visit.<br>_5a. If filters are applied:_<br>1. The System allows filtering by date range, visit type, and advisor.<br>2. The System updates the displayed list based on the selected filters.|
|**Exceptions:**|_3._ _If the database query fails:_<br>1. The System displays an error message: "The visit history could not be<br>loaded. Please try again".<br>2. The System logs the error for technical review.<br>3. The use case ends.<br>_7._ _If GPS coordinates are not available for the selected visit:_<br>1. The System displays the remaining visit information.|



Table 2.10 Use Case Documentation - View Visit History 

40 

|2. Instead of the map, the System displays: "GPS location not available<br>for this visit".|
|---|
|**Requirements:**RF-CRM-007:   The system shall allow the sales advisor to view a history of<br>visits made to their assigned business clients|



Table 2.10 (continued) 

41 

|**Name of Use Case:**<br>Up|datenegotiationstatus|
|---|---|
|**Created By:**<br>BO|PADIGITAL<br>**Last Updated By:**<br>BOPADIGITAL|
|**Date Created:**<br>21|/12/25<br>**Last Revision**<br>11/01/2026|
||**Date:**|
|<br>**Description:**|The Sales Advisor changes the current status of a negotiation to reflect the<br>progressinthe sales process according to the advancement withthe client.|
|**Actors: **|SalesAdvisor.|
|**Preconditions:**|1. The advisor must be authenticated in the system.<br>2. The negotiation must exist and be active in the system.<br>3. The client must be assigned to the sales advisor.<br>4. Thenew statusmust be valid according to the systemstatusflow|
|**Postconditions:**|1. The negotiation status is updated in the database.<br>2. The status change is recorded in the negotiation history with a<br>timestamp.<br>3. Appropriate workflows or notifications are triggered according to the<br>new status.|
||4. The advisor’smetrics are automatically updated.|
|**Flow:**|1. The Sales Advisor accesses the negotiation detail page of the client.<br>2. The System prominently displays the current status of the negotiation.<br>3. The Advisor clicks the “Update Status” button.<br>4. The System displays a dialog with the next available statuses<br>according to the flow: Prospecting, Initial Contact, Active<br>Negotiation, Closing, Post-Sale.<br>5. The Advisor selects the desired new status.<br>6. The System displays an optional text field to add notes about the status<br>change.<br>7. The Advisor optionally enters explanatory notes about the change.<br>8. The Advisor clicks “Confirm Change”.<br>9. The System validates that the status transition is allowed (critical<br>stages cannot be skipped).<br>10. The System updates the negotiation status in the database.<br>11. The System records the change in the history with: Previous status,<br>New status, User, Date and time, Entered notes.<br>12. The System executes specific actions according to the new status (e.g.,<br>notify the Immediate Supervisor if it moves to Closing).<br>13. The System displays a confirmation message: “The negotiation status<br>has been updated to [new status]”.|
|**Alternative Flows:**|<br>_9a. If the status transition is invalid (e.g., attempting to skip from Prospecting_<br>_directly to Closing):_<br>1. The System displays a warning message: “Invalid status transition.<br>You must go through the intermediate stages”.<br>2. The System displays the next valid status.<br>3. The flow returns to step 4.<br>_12a. If the new status is “Closing”:_<br>1. The System sends an automatic notification to the Immediate<br>Supervisor.|



Table 2.11 Use Case Documentation - Update negotiation status 

42 

||2. The System requests additional information required for closing<br>(estimated amount, probable date).<br>3. The flow continues normally.|
|---|---|
|**Exceptions:**|_10._ _If the database update fails:_<br>1. The System displays an error message: “The status could not be<br>updated. Please try again”.<br>2. The System logs the error.<br>3. The negotiation status remains unchanged.<br>4. The use case ends.<br>_1._ _If the negotiation is closed or canceled:_<br>1. The System does not display the “Update Status” button.<br>2. The System displays an informational message: “This negotiation is<br>closed and cannot be modified”.<br>3. The use case ends.|
|**Requirements:**|RF-CRM-008:   The system shall allow the sales advisor to update the<br>negotiation status with an assigned business client.|



Table 2.11 (continued) 

43 

|**Name of Use Case:**<br>As|signclient to advisor|
|---|---|
|**Created By:**<br>BO|PADIGITAL<br>**Last Updated By:**<br>BOPADIGITAL|
|**Date Created:**<br>21|/12/25<br>**Last Revision**<br>**Date:**<br>11/01/2026|
|<br>**Description:**|The Immediate Supervisor assigns a business client to a specific sales advisor<br>from their team so that the advisor can start or continue the commercial<br>negotiationprocess.|
|**Actors: **|Immediate Supervisor.|
|**Preconditions:**|1. The supervisor must be authenticated in the system.<br>2. The client must exist in the database.<br>3. The destination sales advisor must be active and belong to the<br>supervisor’s team.<br>4. The clientmay be unassigned oralready assigned to anotheradvisor.|
|**Postconditions:**|1. The client is assigned to the selected sales advisor.<br>2. The advisor can now view and manage the client in their portfolio.<br>3. The assignment is recorded in the system with date, time, and the<br>supervisor who performed the assignment.<br>4. The advisor receives anotificationofthenew assignment.|
|**Flow:**|1. The Immediate Supervisor navigates to the “Client Management”<br>section in the CRM module.<br>2. The Supervisor searches for the client to assign by RUC or Business<br>Name.<br>3. The System displays the search results with basic client information.<br>4. The Supervisor selects the specific client.<br>5. The System displays the client details and the current assignment<br>status.<br>6. The Supervisor clicks the “Assign to Advisor” or “Reassign” button.<br>7. The System displays a list of available sales advisors in the<br>supervisor’s team with: Full name, Sales zone, Current number of<br>assigned clients, Current workload.<br>8. The Supervisor selects the destination sales advisor from the list.<br>9. The Supervisor optionally enters notes about the reason for the<br>assignment.<br>10. The Supervisor clicks “Confirm Assignment”.<br>11. The System validates that the client is not already assigned to the same<br>advisor.<br>12. The System creates or updates the assignment relationship in the<br>database.<br>13. The System records the assignment in the audit log.<br>14. The System sends a notification to the sales advisor about the newly<br>assigned client.<br>15. The System displays a confirmation message: “[Client] has been<br>successfully assigned to [Advisor]”.|
|**Alternative Flows:**|_11a._ _If the client is already assigned to the selected advisor:_|



Table 2.12 Use Case Documentation - Assign client to advisor 

44 

||1. The System displays an alert: “This client is already assigned to<br>[Advisor Name]”.<br>2. The System asks whether the supervisor wants to change the<br>assignment to another advisor.<br>3. If the supervisor confirms, the flow returns to step 7.<br>4. If the supervisor cancels, the use case ends.<br>_6a._ _If the client is already assigned to another advisor:_<br>5. The System displays information about the current advisor.<br>6. The System displays a warning: “This client is currently assigned to<br>[Name]. Do you want to reassign?”.<br>7. The Supervisor may: Continue with the reassignment, View the client<br>history before deciding, or Cancel.<br>8. If the Supervisor continues, the flow proceeds normally from step 7.|
|---|---|
|**Exceptions:**|_12. If the assignment operation fails in the database:_<br>1. The System displays an error message: “The assignment could not be<br>completed. Please try again”.<br>2. The System logs the error for technical review.<br>3. The assignment is not performed.<br>4. The use case ends.<br>_14._ _If sending the notification to the advisor fails:_<br>1. The System completes the assignment anyway.<br>2. The System records that the notification failed.<br>3. The Systemwillattempt toresend thenotification later.|
|**Requirements:**|RF-CRM-012:   The system shall allow the immediate supervisor to assign<br>business clients to sales advisors to initiate negotiations.|



Table 2.12 (continued) 

45 

|**Name of Use Case:**<br>Un|assignor remove clientfromanadvisor|
|---|---|
|**Created By:**<br>BO|PADIGITAL<br>**Last Updated By:**<br>BOPADIGITAL|
|**Date Created:**<br>21<br>|/12/25<br>**Last Revision**<br>**Date:**<br>11/01/2026|
|**Description:**|The Immediate Supervisor removes the assignment relationship between a<br>business client and a sales advisor, freeing the client for potential<br>reassignment orarchiving.|
|**Actors: **|Immediate Supervisor|
|**Preconditions:**|1. The supervisor must be authenticated in the system.<br>2. The client must currently be assigned to a sales advisor.<br>3. The advisor and the client must belong to the supervisor’s<br>team/portfolio.|
|**Postconditions:**|1. The assignment relationship is removed from the database.<br>2. The client becomes available to be reassigned to another advisor.<br>3. The sales advisor no longer has access to modify that client.<br>4. The unassignmentisrecordedinthe audithistory with reasonand user.|
|**Flow:**|1. The Immediate Supervisor accesses the team management module in<br>the CRM.<br>2. The Supervisor views the list of sales advisors on their team.<br>3. The Supervisor selects a specific advisor to view their client portfolio.<br>4. The System displays all clients currently assigned to that advisor.<br>5. The Supervisor selects the client to be unassigned.<br>6. The Supervisor clicks the “Remove Assignment” or “Unassign<br>Client” button.<br>7. The System displays a confirmation dialog with a warning: “Are you<br>sure you want to unassign this client from [Advisor Name]?”.<br>8. The System displays a mandatory field requesting the reason for the<br>unassignment.<br>9. The Supervisor enters the reason explaining the cause (e.g., “Territory<br>change”, “Workload reassignment”, “Inactive client”).<br>10. The Supervisor clicks “Confirm Unassignment”.<br>11. The System checks whether the client has active negotiations in<br>progress.<br>12. The System removes the assignment relationship from the database.<br>13. The System records the unassignment in the audit history with: User<br>who performed the action, Date and time, Unassigned client, Advisor<br>from whom the client was unassigned, Provided reason.<br>14. The System displays a confirmation message: “The client has been<br>successfully unassigned from [Advisor]”.|
|**Alternative Flows:**|_10a. If the Supervisor cancels the operation:_<br>1. The System closes the confirmation dialog without making changes.<br>2. The assignment remains intact.<br>3. The use case ends.<br>_8a. If the Supervisor does not provide a reason:_<br>1. The System displays an error: “The unassignment reason is<br>mandatory”.|



Table 2.13 Use Case Documentation - Unassign or remove client from an advisor 

46 

||2. The System does not allow continuation until a reason is entered.<br>3. The flow remains at step 9|
|---|---|
|**Exceptions:**|_11. If the client has active negotiations in a critical state (e.g., imminent_<br>_Closing):_<br>1. The System displays a warning: “WARNING: This client has active<br>negotiations in Closing state. Do you want to proceed anyway?”.<br>2. The System displays details of the active negotiations.<br>3. The Supervisor may: Confirm and proceed with the unassignment, or<br>Cancel to review the negotiations first.<br>4. If the Supervisor confirms, the flow continues at step 12.<br>5. If the Supervisor cancels, the use case ends.<br>_12._ _If the database operation fails:_<br>1. The System displays an error message: “The unassignment could not<br>be completed. Please try again”.<br>2. The System logs the error.<br>3. The assignment remains unchanged.<br>4. The use case ends.|
|**Requirements:**|RF-CRM-014:   The system shall allow the immediate supervisor to remove<br>business clients from a sales advisor’sportfolio.|



Table 2.13 (continued) 

47 

|**Name of Use Case:**<br>Di|sable closednegotiations|
|---|---|
|**Created By:**<br>BO|PADIGITAL<br>**Last Updated By:**<br>BOPADIGITAL|
|**Date Created:**<br>21|/12/25<br>**Last Revision**<br>**Date:**<br>11/01/2026|
|<br>**Description:**|The Immediate Supervisor marks negotiations that have been completed<br>(successful or canceled) as closed and inactive to prevent further<br>modifications and preserve theintegrity of historicaldata.|
|**Actors: **|Immediate Supervisor.|
|**Preconditions:**|1. The supervisor must be authenticated in the system.<br>2. The negotiation must be in a final state: Post-Sale (successfully<br>completed) or Canceled.<br>3. Thenegotiation must belong to a client withinthe supervisor’s team.|
|**Postconditions:**|1. The negotiation is marked as closed/inactive in the database.<br>2. No further modifications or status changes are allowed on the<br>negotiation.<br>3. The negotiation data is preserved intact for historical reports and<br>auditing.<br>4. Historical metrics andreportsinclude thisnegotiation.|
|**Flow:**|1. The Immediate Supervisor navigates to the “Negotiations” section in<br>the CRM module.<br>2. The Supervisor applies a filter to view negotiations in “Post-Sale” or<br>“Canceled” status.<br>3. The System displays the list of completed negotiations that are still<br>marked as active.<br>4. The Supervisor reviews the list and selects the negotiation(s) to<br>permanently close.<br>5. The Supervisor may select multiple negotiations using checkboxes.<br>6. The Supervisor clicks the “Close Selected Negotiations” button.<br>7. The System displays a confirmation dialog listing the negotiations to<br>be closed: Associated client, Final status, Responsible advisor,<br>Completion date.<br>8. The System warns: “Closed negotiations cannot be modified later”.<br>9. The Supervisor reviews the information and clicks “Confirm<br>Closure”.<br>10. The System sets the isActive flag to false for each selected negotiation.<br>11. The System records the closure in the audit log with: User who closed,<br>Closure date and time, IDs of closed negotiations.<br>12. The System displays a confirmation message: “[N] negotiation(s)<br>have been successfully closed”.|
|**Alternative Flows:**|_9a. If the Supervisor cancels the operation:_<br>1. The System closes the dialog without applying changes.<br>2. All negotiations remain active.<br>3. The use case ends.<br>_4a. If the Supervisor wants to view details before closing:_<br>1. The Supervisor clicks on a specific negotiation.<br>2. The Systemdisplays the detailed view withthe completehistory.|



Table 2.14 Use Case Documentation - Disable closed negotiations 

48 

||3. The Supervisor reviews the full information.<br>4. The Supervisor returns to the list.<br>5. The flow continues at step 4.|
|---|---|
|**Exceptions:**|_3.  If there are no negotiations in final status available for closure:_<br>1. The System displays the message: “There are no completed<br>negotiations pending closure”.<br>2. The use case ends.<br>_4._ _If a selected negotiation is not in a valid final status:_<br>1. The System displays a warning: “Only negotiations in Post-Sale or<br>Canceled status can be closed”.<br>2. The System automatically unselects negotiations with invalid status.<br>3. The System displays which negotiations were unselected and why.<br>4. The flow continues with the remaining valid negotiations.<br>_10._ _If the database update operation fails:_<br>1. The System displays an error: “The negotiations could not be closed.<br>Please try again”.<br>2. The System logs the error.<br>3. The negotiations remain active.<br>4. The use case ends.|
|**Requirements:**|RF-CRM-011:  The system shall allow the immediate supervisor to<br>deactivate business clients when necessary.|



Table 2.14 (continued) 

49 

|**Name of Use Case:**<br>Vi|ewrecent advisoractivity|
|---|---|
|**Created By:**<br>BO|PADIGITAL<br>**Last Updated By:**<br>BOPADIGITAL|
|**Date Created:**<br>21|/12/25<br>**Last Revision**<br>**Date:**<br>11/01/2026|
|<br>**Description:**|The Immediate Supervisor reviews a feed of recent activities performed by<br>the sales advisors on their team in order to monitor productivity, follow-up,<br>and compliance withdefined processes.|
|**Actors: **|Immediate Supervisor.|
|**Preconditions:**|1. The supervisor must be authenticated in the system.<br>2. The supervisor must have at least one sales advisor assigned to their<br>team.<br>3. Theremust be activityrecordedinthe systemby the advisors.|
|**Postconditions:**|1. A chronological feed of recent team activity is displayed.<br>2. The supervisor can identify work patterns and areas requiring<br>attention.|
|**Flow:**|1. The Immediate Supervisor navigates to the “Team Activity” section<br>on the dashboard.<br>2. The System queries the recent activities of all supervised advisors.<br>3. The System displays an activity feed in descending chronological<br>order (most recent first) with: Activity type (Visit registration, Client<br>update, Negotiation status change, Document upload, Offer matrix<br>submission), Advisor who performed the action, Associated client,<br>Exact date and time, Brief summary of the action.<br>4. The Supervisor may apply filters to refine the view: Filter by specific<br>advisor or view all, Filter by date range (today, last week, last month,<br>custom), Filter by specific activity type.<br>5. The Supervisor selects a specific activity to view full details.<br>6. The System displays the detailed activity view including: All relevant<br>action data, Client and negotiation context, Links to directly access the<br>relatedrecord.|
|**Alternative Flows:**|_2a. If there is no recent activity recorded:_<br>1. The System displays an informational message: “There is no recent<br>activity to display for the selected period”.<br>2. The System suggests expanding the date range.<br>3. The use case ends if the supervisor does not modify filters.<br>_4a. If the Supervisor applies filters:_<br>1. The System updates the feed displaying only activities that match the<br>criteria.<br>2. The System displays a counter: “Displaying [N] activities”.<br>3. The flow continues at step 4 with the filtered results.<br>_5a. If the Supervisor wants to export the activity report:_<br>1. The Supervisor clicks “Export Activity”.<br>2. TheSystemgenerates an Excel filewith all displayed activities.|



Table 2.15 Use Case Documentation - View recent advisor activity 

50 

||3. The flow continues normally.|
|---|---|
|**Exceptions:**|_2._ _If the activity feed query fails:_|
||1. The System displays an error message: “The activity feed could not be<br>loaded. Please try again”.<br>2. The System logs the error for technical review.<br>3. The use case ends.|
||_6._ _If the related record has been deleted:_<br>1. The System displays the available activity information.<br>2. The System indicates: “The associated record is no longer available”.<br>3. Links tonon-existentrecords arenot enabled.|
|**Requirements:**|RF-CRM-015:   The system shall allow the immediate supervisor to view the<br>recent activityof all companysales advisors.|



Table 2.15 (continued) 

51 

|**Name of Use Case:**<br>Vi|ew costs peradvisor|
|---|---|
|**Created By:**<br>BO|PADIGITAL<br>**Last Updated By:**<br>BOPADIGITAL|
|**Date Created:**<br>21|/12/25<br>**Last Revision**<br>**Date:**<br>11/01/2026|
|<br>**Description:**|The Immediate Supervisor or Manager reviews cost and sales performance<br>metricsforeachadvisorontheirteam.|
|**Actors: **|Immediate Supervisor,Manager|
|**Preconditions:**|1. The user must be authenticated with the appropriate role.<br>2. Sales data must be available in the system.|
|**Postconditions:**|1. Cost and performance metrics per advisor are displayed.|
|**Flow:**|2. The User navigates to the “Advisor Metrics” section.<br>3. The System displays a list of advisors with key metrics: Total sales<br>amount, Number of closures, Average deal value, Earned commission,<br>Sales by service category.<br>4. The User can sort by any metric column.<br>5. The User selects a specific advisor to view a detailed breakdown.<br>6. The System displays a detailed cost analysis: Monthly trend chart,<br>Revenue by service type, Customeracquisitioncost, Conversion rates.|
|**Alternative Flows:**|_2a. If no data is available for the selected period:_<br>1. The System displays: “No sales data available for the selected period”.<br>2. The use case ends.|
|**Exceptions:**|_2. If metric calculation fails:_<br>1. The System displays: “Metrics could not be calculated. Please try<br>again”.<br>2. The use case ends.|
|**Requirements:**|RF-CRM-017:  The system shall allow management to view the total billed<br>amount per advisor, along with the total number of services sold and the<br>average revenueper service.|



Table 2.16 Use Case Documentation - View costs per advisor 

52 

|**Name of Use Case:**<br>Ge|t salesreport|
|---|---|
|**Created By:**<br>BO|PADIGITAL<br>**Last Updated By:**<br>BOPADIGITAL|
|**Date Created:**<br>21|/12/25<br>**Last Revision**<br>**Date:**<br>11/01/2026|
|<br>**Description:**|The Immediate Supervisor or Manager views a commercial progress report<br>that shows negotiation progress, completed visits, and client statuses in order<br>to evaluate goalcompliance.|
|**Actors: **|Manager,Immediate Supervisor.|
|**Preconditions:**|1. The user must be authenticated.<br>2. Sales data must exist in the system.|
|**Postconditions:**|1. The sales report is generated and displayed.<br>2. Thereport canbe exportedforexternaluse.|
|**Flow:**|1. The User navigates to the “Reports” section.<br>2. The User selects the “Sales Report” option.<br>3. The System displays the report configuration form: Date range,<br>Advisor filter (all/specific), Service category filter, Grouping option<br>(by advisor/by month/by service).<br>4. The User configures the desired parameters.<br>5. The User clicks “Generate Report”.<br>6. The System queries sales data based on the parameters.<br>7. The System calculates aggregated metrics: Total sales value, Number<br>of closed deals, Average deal size, Top-performing advisors, Best-<br>selling services.<br>8. The System displays the report with charts and tables.<br>9. The User may export thereportin PDFor Excel format.|
|**Alternative Flows:**|_6a. If no data matches the selected criteria:_<br>1. The System displays: “No sales data found for the selected criteria”.<br>2. The User may modify parameters and retry.|
|**Exceptions:**|_6. If a query timeout occurs:_<br>1. The System displays: “Report generation is taking longer than<br>expected. Please try a smaller date range”.<br>2. The use case ends.|
|**Requirements:**|RF-REP-001: The system shall allow the manager to generate commercial<br>performance reports by advisor, month, or period to evaluate team<br>productivity.<br>RF-REP-006:  The system shall allow the manager to export generated<br>reports in PDF or Excel format for analysis orpresentation|



Table 2.16 (continued) 

53 

|**Name of Use Case:**<br>Ge|t progressreport|
|---|---|
|**Created By:**<br>BO|PADIGITAL<br>**Last Updated By:**<br>BOPADIGITAL|
|**Date Created:**<br>21|/12/25<br>**Last Revision**<br>11/01/2026|
||**Date:**|
|<br>**Description:**|The Immediate Supervisor or Manager generates reports showing the progress<br>of the negotiation pipeline and advisor performance against defined<br>objectives.|
|**Actors: **|Immediate Supervisor,Manager|
|**Preconditions:**|1. The user must be authenticated.<br>2. Negotiation and target data must exist.|
|**Postconditions:**|1. The progress report is generated showing current status versus<br>objectives.<br>2. Thereport canbe exported.|
|**Flow:**|1. The User navigates to the “Reports” section.<br>2. The User selects the “Progress Report” option.<br>3. The System displays the configuration form: Date range, Advisor<br>filter, Include comparison against objectives.<br>4. The User configures the parameters.<br>5. The User clicks “Generate Report”.<br>6. The System queries negotiation pipeline data.<br>7. The System calculates metrics: Negotiations by stage<br>(Prospecting/Active/Closing/Closed), Conversion rates, Average<br>time per stage, Objective compliance percentage, Projected<br>versus actual performance.<br>8. The System displays the report with pipeline funnel visualization.<br>9. The User may export thereportin PDFor Excel format.|
|**Alternative Flows:**|_6a. If there are no active negotiations:_<br>1. The System displays: “No negotiations were found for the selected<br>period”.<br>2. The use case ends.|
|**Exceptions:**|_6. If calculation fails:_<br>1. The System displays: “The progress report could not be generated.<br>Please try again”.<br>2. The use case ends.|
|**Requirements:**|RF-CRM-019: The system shall allow management to view, for each<br>advisor,the number of business clients in each sales funnel stage.|



Table 2.17 Use Case Documentation - Get progress report 

54 

|**Name of Use Case:**|CompareMetricsBetween Advisors|
|---|---|
|**Created By:**|BOPADIGITAL<br>**Last Updated By:**<br>BOPADIGITAL|
|**Date Created:**|21/12/25<br>**Last**<br>**Revision**<br>**Date:**<br>11/01/2026|
|**Description:**|The Immediate Supervisor or Manager performs side-by-side comparison of<br>performance metrics between multiple sales advisors to identify best<br>practices, performance gaps, and make informed decisions about coaching,<br>recognition, or resource allocation.|
|**Actors:**|Immediate Supervisor|
|**Preconditions:**|1. The user must be authenticated with the appropriate role.<br>2. At least two sales advisors must exist in the system.<br>3. Performance data must be available for the advisors being compared.<br>4.ForSupervisors, allcompared advisorsmust beintheirteam.|
|**Postconditions:**|1. A comparative analysis of selected advisors is displayed.<br>2. Performance gaps and leaders are clearly identified.<br>3. The comparison can be saved or exported for review.<br>4.Managementhasinsightsfordecision-making.|
|**Flow:**|1. The User accesses the "Team Performance" section in the CRM module.<br>2. The System displays the list of all advisors in the user's scope.<br>3. The User selects multiple advisors for comparison using checkboxes<br>(minimum two, maximum five).<br>4. The User clicks "Compare Selected Advisors".<br>5. The System displays a period selector: Current month (default), Last month,<br>Last quarter, Year to date, Custom range.<br>6. The User selects the time for comparison.<br>7. The System queries performance data for all selected advisors for the<br>specified period.<br>8. The System calculates comparison metrics for each advisor: Revenue<br>generated, Number of deals closed, Average deal size, Number of active<br>clients, Client visits performed, Negotiations in pipeline, Closing rate (%),<br>Average time to close, Proposals submitted, Approval rate (%),<br>Documentation completion rate.<br>9. The System displays the comparison dashboard organized in sections:<br>Summary Comparison Table: Advisors as columns, Key metrics as rows,<br>Numeric values with color coding (green for above average, red for below).<br>Visual Comparisons: Grouped bar charts for revenue and deals, Line graphs<br>for trends over time, Radar charts for multi-dimensional comparison, Pie<br>charts for market share/contribution. Performance Rankings: Overall<br>performance score, Individual metric rankings, Percentile position within<br>team. Gap Analysis: Identifies largest performance differences, Highlights<br>strengths and weaknesses, Shows distance from team average or top<br>performer.<br>10. The System color-codes each metric: Green for top performers (top 25%),<br>Yellow for average performers (middle 50%), Red for below average (bottom<br>25%).<br>11. The User reviews the comparison visualizations.<br>12. The User can interact with charts and tables: Hover for detailed values,<br>click to drill down into specific data, Toggle metrics on/off, Sort by any<br>column.|



Table 2.18 Use Case Documentation - Compare Metrics Between Advisors 

55 

|**Alternative Flows:**|**12a. User adjusts comparison parameters:**<br>1. The User clicks "Adjust Comparison".<br>2. The System allows modifying: Selected advisors (add/remove), Time<br>period, Metrics to compare (select/deselect specific metrics).<br>3. The User makes changes.<br>4. The System recalculates and updates the comparison.<br>5. The flow returns to step 11.<br>**12b. User views detailed breakdown for specific metric:**<br>1. The User clicks on a specific metric in the comparison.<br>2. The System displays a detailed view for that metric only: Individual values<br>for each advisor, Statistical analysis (mean, median, standard deviation),<br>Distribution chart, Historical trend for each advisor, Target vs. actual<br>comparison.<br>3. The User can return to the full comparison.<br>**12c. User identifies and analyzes performance gap:**<br>1. The User clicks on a significant performance gap indicator.<br>2. The System displays gap analysis: Top performer's approach and activities,<br>Lower performer's activities, Specific recommendations, Best practices from<br>top performer, Suggested coaching focus areas.<br>3. The User can export the gap analysis.<br>**11a. User exports comparison report:**<br>1. The User clicks "Export Comparison".<br>2. The System displays export options: Format (PDF/Excel/PowerPoint),<br>Include all metrics or selected only, Include charts and visualizations, Add<br>executive summary.<br>3. The User configures export options.<br>4. The System generates a comprehensive comparison report with: Cover<br>page, Executive summary, Detailed comparison tables, All visualizations,<br>Insights, and recommendations.<br>5. The System initiates the download.<br>**12d. User saves comparison for later:**<br>1. The User clicks "Save Comparison".<br>2. The System prompts for a name and optional description.<br>3. The User provides comparison details.<br>4. The System saves the comparison configuration and current results.<br>5. The System displays: "Comparison saved. Access it from 'My Saved<br>Comparisons'."<br>**11b. User shares comparison with others:**<br>1. The User clicks "Share Comparison".<br>2. The System displays sharing options: Share link (view-only), Send via<br>email, Schedule recurring email.<br>3. The User selects recipients.<br>4. The System generates a shareable link or sends the report.<br>5. The System logs the sharing action.|
|---|---|



Table 2.18 (continued) 

56 

|**Exceptions:**|**7. Performance data unavailable for some advisors:**<br>1. The System displays a warning: "Limited data available for [Advisor<br>Name]. Comparison may be incomplete."<br>2. The System displays available data with indicators for missing metrics.<br>3. The System includes a note in the comparison.<br>4. The User can proceed with partial comparison or exclude the advisor.<br>**9. Calculation error during comparison:**<br>1. The System displays: "An error occurred while calculating comparison<br>metrics."<br>2. The System displays successfully calculated metrics with a warning.<br>3. The System logs the error with details.<br>4.The Usercan retry|
|---|---|



Table 2.18 (continued) 

57 

|**Name of Use Case:**|ViewAdvisor Metrics|
|---|---|
|**Created By:**|BOPADIGITAL<br>**Last Updated By:**<br>BOPADIGITAL|
|**Date Created:**|21/12/25<br>**Last**<br>**Revision**<br>**Date:**<br>11/01/2026|
|**Description:**|The Immediate Supervisor or Manager views detailed performance metrics<br>for individual sales advisors to evaluate productivity, identify top performers,<br>and detect areasneedingimprovement orsupport.|
|**Actors:**|SalesAdvisor,Immediate Supervisor|
|**Preconditions:**|1. The user must be authenticated with the appropriate role.<br>2. Sales advisor accounts must exist in the system.<br>3. Performance data must be available in the database.<br>4. For Supervisors, they can only view metrics for advisors in their team.<br>5.Managers canviewmetricsforalladvisors.|
|**Postconditions:**|1. Comprehensive advisor performance metrics are displayed.<br>2. The user can identify performance trends and patterns.<br>3. Metric viewing is logged for audit purposes.<br>|
||4.Performance comparisons canbemade betweenadvisors.|
|**Flow:**|1. The User accesses the "Team Performance" or "Advisor Metrics" section.<br>2. The System displays a list of advisors within the user's scope with summary<br>metrics: Advisor name and photo, Current clients assigned, Active<br>negotiations, Closed deals (current month), Total revenue (current month),<br>Performance rating indicator.<br>3. The User can sort the list by any metric column.<br>4. The User selects a specific advisor to view detailed metrics.<br>5. The System displays comprehensive advisor performance data organized<br>in sections: Overview Section: Advisor profile information, Team/territory<br>assignment, Hire date and tenure, Current performance rating. Activity<br>Metrics: Total clients assigned, New clients added (period), Client visits<br>registered, Last visit date, Average visits per client. Pipeline Metrics: Total<br>active negotiations, Negotiations by stage (count and percentage), Average<br>negotiation duration, Stage conversion rates, Stalled negotiations (no activity<br>> 30 days). Revenue Metrics: Total closed deals (period), Total revenue<br>generated (period), Average deal size, Largest deal closed, Revenue by<br>service category, Year-to-date revenue. Productivity Metrics: Closing rate<br>(%), Average time to close, Proposals submitted, Proposals approved,<br>Proposals rejected, Documentation completion rate. Comparative Metrics:<br>Performance vs. team average, Performance vs. personal targets, Ranking<br>within team, Trend indicators (improving/declining).<br>6. The System includes visual indicators: Color-coded performance ratings,<br>Trend arrows (up/down/stable), Progress bars for targets, Sparklines for<br>trends.<br>7. The User can select different time periods: Current month, Last month, Last<br>quarter, Last year, Custom date range.<br>8. The System updates all metrics for the selected period.<br>9. The User can view detailed drill-downs: Click on any metric to see<br>underlying transactions, View individual client details, Review specific<br>negotiations.|



Table 2.19 Use Case Documentation - View Advisor Metrics 

58 

|**Alternative Flows:**|**9a. User views advisor activity timeline:**<br>1. The User clicks "Activity Timeline".<br>2. The System displays a chronological view of all advisor activities: Client<br>registrations, Visits registered, Matrix submissions, Approvals received, Deal<br>closures, Documentation uploads.<br>3. Each activity is timestamped and includes details.<br>4. The User can filter by activity type.<br>**9b. User compares multiple advisors:**<br>1. The User returns to the advisor list.<br>2. The User selects multiple advisors using checkboxes (2-5 advisors).<br>3. The User clicks "Compare Selected".<br>4. The System displays a side-by-side comparison dashboard: Key metrics in<br>comparison table, Stacked bar charts for visual comparison, Performance<br>ranking, Strengths, and weaknesses analysis.<br>5. The System highlights significant differences.<br>**9c. User exports advisor metrics:**<br>1. The User clicks "Export Metrics".<br>2. The System displays export options: Format (Excel/PDF), Include charts<br>(yes/no), Include all advisors or current selection, Time period to include.<br>3. The User configures export options.<br>4. The System generates the export file.<br>5. The System initiates the download.<br>**5a. User views advisor's client portfolio:**<br>1. The User clicks "View Clients" in the advisor profile.<br>2. The System displays all clients assigned to the advisor with: Client name<br>and RUC, Current monthly billing, Negotiation status, Last contact date,<br>Documentation status.<br>3. The User can click on any client to view full details.<br>**6a. Performance alerts displayed:**<br>1. The System automatically identifies and displays alerts: "Below target for<br>2 consecutive months", "No client visits in last 14 days", "3 negotiations<br>stalled over 60 days", "Documentation completion below 50%".<br>2. Each alert includes a severity level (Info/Warning/Critical).<br>3.The Usercanclickonalertsfor recommendations.|
|---|---|
|**Exceptions:**|**5. Advisor metrics cannot be loaded:**<br>1. The System displays: "Unable to load advisor metrics. Please try again."<br>2. The System logs the error.<br>3. The summary metrics remain visible.<br>4. The use case ends.<br>**8. Time period query timeout:**<br>1. The System displays: "Loading metrics for the selected period is taking too<br>long. Try a shorter time range."<br>2. The System displays cached or summary data if available.<br>3. The User can select a different period.|



Table 2.19 (continued) 

59 

||**2. No advisors in user's scope:**<br>1. The System displays: "No sales advisors are currently assigned to your<br>team."<br>2. For Supervisors, suggests contacting management.<br>3.The use case ends.|
|---|---|
|**Requirements:**|**RF-CRM-017:**The system shall allow management to view the total billed<br>amount per advisor, along with the total number of services sold and the<br>average revenue per service.<br>**RF-CRM-019:**The system shall allow management to view, for each advisor,<br>the number of business clients in each sales funnel stage.<br>**RF-REP-007:**The system shall display individual advisor performance<br>metrics including deals closed, revenue, and conversion rates.|



Table 2.19 (continued) 

60 

|**Name of Use Case:**|Filter Reports|
|---|---|
|**Created By:**|BOPADIGITAL<br>**Last Updated By:**<br>BOPADIGITAL|
|**Date Created:**|21/12/25<br>**Last**<br>**Revision**<br>**Date:**<br>11/01/2026|
|**Description:**|The Immediate Supervisor or Manager applies filters to generated reports to<br>focus on specific segments, time periods, or metrics, enabling detailed<br>analysis ofaspects ofsales performance.|
|**Actors:**|Immediate Supervisor,Immediate Supervisor|
|**Preconditions:**|1. The user must be authenticated with the appropriate role.<br>2. A report must have been generated (sales, progress, or performance report).<br>3.Thereportmust contain filterable data.|
|**Postconditions:**|1. The report view is updated to show only filtered data.<br>2. Filter settings are temporarily saved for the current session.<br>3. Filtered data can be exported separately.<br>4. Charts and visualizations are updated toreflectfiltered data.|
|**Flow:**|1. The User is viewing a generated report (sales, progress, or performance).<br>2. The User clicks "Filter Report" or the filter icon in the report interface.<br>3. The System displays available filter options based on report type: Time<br>Period Filters: Specific months, Quarters, Date ranges. Advisor Filters:<br>Individual advisors, Teams, Performance levels (Top/Average/Below<br>Average). Service Category Filters: Voice, Connectivity, Digital Services,<br>Specific services. Client Segment Filters: By industry, By company size, By<br>billing range. Performance Filters: Above/below target, Conversion rate<br>ranges, Deal size ranges. Status Filters: Negotiation stages, Documentation<br>status, Approval status.<br>4. The User selects one or multiple filter criteria.<br>5. The User specifies filter values or ranges as appropriate.<br>6. The User can combine filters using AND/OR logic operators.<br>7. The User clicks "Apply Filters".<br>8. The System validates the filter criteria.<br>9. The System recalculates metrics based on filtered data.<br>10. The System updates all visualizations (charts, graphs, tables).<br>11. The System displays the filtered report with: Updated summary statistics<br>reflecting only filtered data, Refreshed charts and graphs, Indicator showing<br>active filters, Number of records displayed vs. total available.<br>12. The System displays an active filter summary: "Showing [N] of [Total]<br>records Filters: [list of active filters]".<br>13. The User can review the filtered report.<br>14.The Usercanaddmorefilters,removefilters, orclearall filters.|
|**Alternative Flows:**|**14a. User clears all filters:**<br>1. The User clicks "Clear All Filters".<br>2. The System removes all active filters.<br>3. The System restores the report to show all data.<br>4. The System recalculates metrics with complete dataset.<br>5. The flow returns to step 11 with full data.<br>**14b. User saves filter configuration:**<br>1. The User clicks "Save Filter Configuration".<br>2. The System displays a dialog to name the filter.<br>3. The User enters a descriptive name.|



Table 2.20 Use Case Documentation - Filter Reports 

61 

||4. The System saves the filter configuration.<br>5. The System displays: "Filter configuration saved. You can load it from 'My<br>Saved Filters'."<br>**9a. Filtered data results in empty set:**<br>1. The System displays: "No data matches your filter criteria."<br>2. The System shows which filters eliminated all data.<br>3. The System suggests: "Try removing or adjusting some filters."<br>4. The User can modify filters or clear them.<br>**14c. User exports filtered report:**<br>1. The User clicks "Export Filtered Data".<br>2. The System displays export options (Excel/PDF).<br>3. The User selects format.<br>4. The System generates export with only filtered data.<br>5. The export includes a note indicating active filters.<br>6. The System initiates the download.<br>**11a. User compares filtered vs. unfiltered data:**<br>1. The User clicks "Compare with Total".<br>2. The System displays side-by-side comparison: Filtered data metrics, Total<br>data metrics, Percentage difference.<br>3. The System highlights significant variances.<br>4. The User can return to filtered view.<br>**6a. User creates complex filter logic:**<br>1. The User clicks "Advanced Filter Logic".<br>2. The System displays a filter builder interface.<br>3. The User creates nested conditions with AND/OR operators.<br>4. The System validates the logic.<br>5.Theflow continues at step 7.|
|---|---|
|**Exceptions:**|**9. Filter recalculation fails:**<br>1. The System displays: "Unable to apply filters. Please try again."<br>2. The System logs the error.<br>3. The report remains in its previous state.<br>4. The use case ends.<br>**8. Invalid filter criteria:**<br>1. The System displays: "Invalid filter values. Please check your inputs."<br>2. The System highlights invalid fields.<br>3. The User corrects the values.<br>4. The flow returns to step 7.<br>**10. Chart rendering fails with filtered data:**<br>1. The System displays the filtered data in table format.<br>2. The System shows a message: "Charts temporarily unavailable. Displaying<br>data in table format."<br>3. The System logs the rendering error.<br>4.The usercanstillworkwith thefiltered data.|



Table 2.20 (continued) 

62 

|**Requirements:**|**RF-REP-004:**The system shall allow filtering reports by multiple criteria<br>such as date range, advisor, and service type.|
|---|---|
||**RF-REP-005:**The system shall update report visualizations dynamically<br>when filters are applied.|



Table 2.20 (continued) 

63 

|**Name of Use Case:**<br>|Generate Sales and ClosingReports<br> <br>|
|---|---|
|**Created By:**|BOPADIGITAL<br>**Last Updated By:**<br>BOPADIGITAL|
|**Date Created:**|21/12/25<br>**Last**<br>**Revision**<br>**Date:**<br>11/01/2026|
|**Description:**|The Immediate Supervisor or Manager generates comprehensive sales reports<br>showing closed deals, revenue, and performance metrics for a specified time<br>period to evaluate commercialsuccess and advisorproductivity.|
|**Actors:**|Immediate Supervisor,Administrator|
|**Preconditions:**|1. The user must be authenticated with the appropriate role.<br>2. Sales and negotiation data must exist in the system.<br>3. At least one closed negotiation must exist in the database.<br>4.Thereportingmodulemust be operational.|
|**Postconditions:**|1. A sales and closing report is generated and displayed.<br>2. The report can be exported in PDF or Excel format.<br>3. Report generation is logged in the system.<br>4.Managementhas visibilityinto sales performance.|
|**Flow:**|1. The User accesses the "Reports" section in the CRM module.<br>2. The User selects "Sales and Closing Report".<br>3. The System displays the report configuration form with parameters: Date<br>Range: Start date (required), End date (required), Quick select options (This<br>Month, Last Month, This Quarter, Last Quarter, This Year, Custom).<br>Grouping Options: By Advisor, By Service Category, By Month, By Client<br>Segment. Advisor Filter: All advisors (for Manager), My team (for<br>Supervisor), Specific advisor(s). Service Category Filter: All categories,<br>Voice, Connectivity, Digital Services. Metrics to Include (checkboxes): Total<br>closed deals, Total revenue, Average deal size, Revenue by service type, Top<br>performing advisors, Conversion rates, Deal closure time.<br>4. The User configures the desired report parameters.<br>5. The User selects which metrics to include in the report.<br>6. The User clicks "Generate Report".<br>7. The System validates that the date range is valid and not excessive.<br>8. The System displays a progress indicator: "Generating report...".<br>9. The System queries the database for closed negotiations within the<br>specified parameters.<br>10. The System calculates all selected metrics: Total number of closed deals,<br>Total revenue generated, Average revenue per deal, Revenue breakdown by<br>service category, Individual advisor performance, Month-over-month trends,<br>Conversion rate (closed vs. total negotiations).<br>11. The System generates visualizations: Bar charts for revenue by advisor,<br>Pie charts for revenue by service category, Line graphs for trends over time,<br>Performance comparison tables.<br>12. The System displays the complete report with: Executive Summary: Key<br>highlights, Overall performance metrics, Period-over-period comparison.<br>Detailed Tables: Individual deal listings, Advisor performance breakdown,<br>Service category analysis. Visual Charts and Graphs: Interactive<br>visualizations, Trend analysis, Comparative metrics.<br>13. The User reviews the report.<br>14. The User can interact with charts (hover for details, click to drill down).|



Table 2.21 Use Case Documentation - Generate Sales and Closing Reports 

64 

|**Alternative Flows:**|**13a. User exports report to Excel:**<br>1. The User clicks "Export to Excel".<br>2. The System generates an Excel workbook with multiple sheets: Summary<br>sheet, Detailed data sheet, Advisor breakdown sheet, Service category sheet,<br>Raw data sheet.<br>3. The System includes charts and formatting.<br>4. The System initiates the download.<br>5. The System logs the export action.<br>**13b. User exports report to PDF:**<br>1. The User clicks "Export to PDF".<br>2. The System generates a formatted PDF document with: Cover page with<br>report title and parameters, Executive summary page, Detailed analysis with<br>charts, Appendix with data tables.<br>3. The System initiates the download.<br>4. The System logs the export action.<br>**14a. User drills down into specific data:**<br>1. The User clicks on a specific chart element (e.g., a bar for an advisor).<br>2. The System displays a detailed view of that specific segment.<br>3. The System shows individual deals comprising that data point.<br>4. The User can return to the full report view.<br>**7a. Date range exceeds system limits:**<br>1. The System displays: "Date range is too large. Please select a range of 2<br>years or less."<br>2. The System highlights the date range fields.<br>3. The User adjusts the date range.<br>4. The flow returns to step 6.<br>**9a. No closed deals in the selected period:**<br>1. The System displays: "No closed deals found for the selected period and<br>filters."<br>2. The System suggests: "Try selecting a different date range or adjusting<br>filters."<br>3. The System shows the nearest periods with available data.<br>4. The User can modify parameters or cancel.<br>**12a. User schedules recurring report:**<br>1. The User clicks "Schedule Report".<br>2.<br>The<br>System<br>displays<br>scheduling<br>options:<br>Frequency<br>(Daily/Weekly/Monthly/Quarterly), Recipients (email addresses), Format<br>(PDF/Excel), Delivery time.<br>3. The User configures the schedule.<br>4. The System saves the scheduled report configuration.<br>5. The System will automatically generate and email the report.|
|---|---|
|**Exceptions:**|**9. Database query fails:**<br>1. The System displays: "Unable to retrieve sales data. Please try again."<br>2. The System logs the error with query details.<br>3.The use case ends.|



Table 2.21 (continued) 

65 

||**10. Calculation error:**<br>1. The System displays: "An error occurred while calculating metrics. Please<br>contact support."<br>2. The System logs the error with partial results.<br>3. The System displays any successfully calculated metrics with a warning.<br>4. The use case ends.<br>**9. Query timeout due to large dataset:**<br>1. The System displays: "Report generation is taking longer than expected.<br>Try a smaller date range or fewer metrics."<br>2. The System cancels the query.<br>3.The use case ends.|
|---|---|
|**Requirements:**|**RF-REP-001:**The system shall allow the manager to generate commercial<br>performance reports by advisor, month, or period to evaluate team<br>productivity.<br>**RF-REP-003:**The system shall include metrics such as total deals closed,<br>revenue generated, and average deal size.<br>**RF-REP-006:**The system shall allow the manager to export generated reports<br>in PDF or Excel format for analysis or presentation.|



Table 2.21 (continued) 

66 

|**Name of Use Case:**|FilterClientLists byMetrics|
|---|---|
|**Created By:**|BOPADIGITAL<br>**Last Updated By:**<br>BOPADIGITAL|
|**Date Created:**|21/12/25<br>**Last**<br>**Revision**<br>**Date:**<br>11/01/2026|
|**Description:**|The Sales Advisor, Immediate Supervisor, or Manager applies advanced<br>filters to client lists based on various metrics and criteria to identify specific<br>client segments, prioritize actions, and analyze the client portfolio.|
|**Actors:**|SalesAdvisor,Immediate Supervisor,Administrator|
|**Preconditions:**|1. The user must be authenticated in the system.<br>2. Client records must exist in the database.<br>3. The CRM module must be accessible.<br>4. For Sales Advisors, they can only filter their assigned clients.<br>5.ForSupervisors andManagers, they can filterallclientsintheirscope.|
|**Postconditions:**|1. A filtered list of clients is displayed according to the selected criteria.<br>2. The filter configuration can be saved for future use.<br>3.Filter results canbe exportedforexternalanalysis.|
|**Flow:**|1. The User accesses the "Clients" section in the CRM module.<br>2. The System displays the complete client list with basic information.<br>3. The User clicks "Advanced Filters" or the filter icon.<br>4. The System displays the filter panel with available filter categories: Client<br>Information Filters: Business Name, RUC, Industry Sector, Company Size.<br>Commercial Metrics Filters: Current Monthly Billing (range), Number of<br>Active Services (range), Total Contract Value (range), Customer Lifetime<br>Value.<br>Negotiation<br>Status<br>Filters:<br>Negotiation<br>Stage<br>(Prospecting/Active/Closing/Post-Sale), Last Contact Date (date range), Days<br>Without Contact, Assigned Advisor. Performance Filters: Documentation<br>Status (Complete/Incomplete), Payment Status (Current/Overdue), Risk<br>Level (Low/Medium/High). Geographic Filters: City, Province, Coverage<br>Zone.<br>5. The User selects one or multiple filter criteria.<br>6. For numeric or date ranges, the User specifies minimum and maximum<br>values.<br>7. For categorical filters, the User selects from dropdown options or<br>checkboxes.<br>8. The User can combine multiple filters using AND/OR logic.<br>9. The User clicks "Apply Filters".<br>10. The System validates the filter criteria.<br>11. The System queries the database with the applied filters.<br>12. The System displays the filtered client list showing: Number of clients<br>matching criteria, Client details matching all filters, Summary statistics for<br>the filtered set.<br>13. The User can further refine filters or clear them.<br>14. The User can save the filter configuration by clicking "Save Filter".<br>15. The System prompts for a filter name.<br>16. The User provides a descriptive name for the filter.<br>17. The System saves the filter configuration for future use.|



Table 2.22 Use Case Documentation - Filter Client Lists by Metrics 

67 

|**Alternative Flows:**|**14a. User loads a saved filter:**<br>1. The User clicks "Load Saved Filter".<br>2. The System displays a list of previously saved filters with: Filter name,<br>Creation date, Filter criteria summary.<br>3. The User selects a saved filter.<br>4. The System applies the saved filter configuration.<br>5. The flow continues at step 11.<br>**13a. User exports filtered results:**<br>1. The User clicks "Export Results".<br>2. The System displays export options: Format (Excel/CSV/PDF), Include<br>columns (customizable), Include summary statistics.<br>3. The User selects export preferences.<br>4. The System generates the export file.<br>5. The System initiates the download.<br>6. The System logs the export action.<br>**12a. No clients match the filter criteria:**<br>1. The System displays: "No clients match your filter criteria."<br>2. The System suggests: "Try adjusting your filters or clearing some criteria."<br>3. The System shows how many clients were excluded by each filter.<br>4. The User can modify filters or clear them.<br>**8a. User creates complex filter logic:**<br>1. The User clicks "Advanced Logic".<br>2. The System displays a query builder interface.<br>3. The User creates complex conditions: (Billing > $1000 AND Services >=<br>3) OR (Stage = Closing).<br>4. The System validates the logic syntax.<br>5. The flow continues at step 9.<br>**12b. User sorts filtered results:**<br>1. The User clicks a column header to sort.<br>2. The System re-orders the filtered list by that column.<br>3. The User can toggle between ascending and descending order.<br>4.The sort preferenceismaintained during the session.|
|---|---|
|**Exceptions:**|**11. Database query timeout:**<br>1. The System displays: "Filter query is taking too long. Try using fewer<br>criteria or narrower ranges."<br>2. The System logs the timeout.<br>3. The user can simplify filters and retry.<br>4. The use case ends if the user cancels.<br>**11. Database query fails:**<br>1. The System displays: "Unable to apply filters. Please try again."<br>2. The System logs the error.<br>3. The previous unfiltered list remains displayed.<br>4. The use case ends.|



Table 2.22 (continued) 

68 

||**17. Filter save fails:**<br>1. The System displays: "Filter could not be saved. Please try again."<br>2. The System logs the error.<br>3. The filter remains applied but is not saved.<br>4.The usercan retry saving.|
|---|---|
|**Requirements:**|**RF-CRM-009:**The system shall allow filtering clients by multiple criteria<br>including billing, services, status, and advisor.<br>**RF-CRM-018:**The system shall provide advanced search and filtering<br>capabilities for client lists.<br>**RF-REP-002:**The system shall allow users to create custom filters and save<br>them for future use.|



Table 2.22 (continued) 

69 

|**Name of Use Case:**|RejectMatrices|
|---|---|
|**Created By:**|BOPADIGITAL<br>**Last Updated By:**<br>BOPADIGITAL|
|**Date Created:**|21/12/25<br>**Last**<br>**Revision**<br>**Date:**<br>11/01/2026|
|**Description:**<br>|The Immediate Supervisor rejects an offer matrix submitted by a sales advisor<br>when it does not comply with commercial policies, contains errors, or is not<br>viableforthe business, providing detailedreasonsfortherejection.<br>|
|**Actors:**|Immediate Supervisor|
|**Preconditions:**|1. The supervisor must be authenticated in the system.<br>2. The offer matrix must exist and be in "Pending Approval" status.<br>3. The matrix must belong to an advisor in the supervisor's team.<br>4.The supervisor musthaverejectionpermissions.|
|**Postconditions:**|1. The matrix status is updated to "Rejected".<br>2. The rejection reason is stored in the database.<br>3. The sales advisor receives a notification with rejection details.<br>4. The matrix cannot be presented to the client without revision.<br>5.Therejection isrecordedinthe auditlog.|
|**Flow:**<br>**Alternative Flows:**|1. The Immediate Supervisor accesses the "Matrix Approvals" section.<br>2. The System displays the list of matrices pending approval.<br>3. The Supervisor selects a specific matrix to review.<br>4. The System displays the complete matrix details including services,<br>pricing, subsidies, and client information.<br>5. The Supervisor reviews the matrix and identifies issues or non-compliance.<br>6. The Supervisor clicks the "Reject Matrix" button.<br>7. The System displays a rejection dialog with: Mandatory text field for<br>rejection reason, Checklist of common rejection reasons (optional): "Exceeds<br>discount limits", "Services not available in area", "Incorrect subsidy<br>calculation", "Missing required information", "Does not meet company<br>policies", "Pricing errors", Additional comments field (optional).<br>8. The Supervisor selects applicable reasons from the checklist or enters a<br>custom reason.<br>9. The Supervisor provides detailed comments explaining the rejection and<br>what needs to be corrected.<br>10. The Supervisor clicks "Confirm Rejection".<br>11. The System validates that a rejection reason has been provided.<br>12. The System updates the matrix status to "Rejected".<br>13. The System records the rejection details in the database including:<br>Supervisor ID, Rejection timestamp, Selected rejection reasons, Detailed<br>comments, Previous matrix status.<br>14. The System creates an entry in the matrix history log.<br>15. The System sends a notification to the sales advisor including: Matrix ID<br>and client name, Rejection reasons, Supervisor comments, Guidance on next<br>steps.<br>16. The System sends an email notification to the advisor.<br>17. The System displays a confirmation message: "Matrix rejected. The<br>advisor has been notified."<br>**8a. Supervisor requests information instead of rejecting:**|



Table 2.23 Use Case Documentation - Reject Matrices 

70 

||1. The Supervisor clicks "Request Information" instead of "Reject".<br>2. The System displays a form to specify what information is needed.<br>3. The Supervisor enters the information request.<br>4. The System updates the matrix status to "Information Requested".<br>5. The System notifies the advisor.<br>6. The use case ends with matrix in "Information Requested" status.<br>**11a. No rejection reason provided:**<br>1. The System displays a validation error: "Rejection reason is mandatory.<br>Please provide a detailed explanation."<br>2. The System highlights the empty reason field.<br>3. The System prevents proceeding until a reason is entered.<br>4. The flow returns to step 9.<br>**10a. Supervisor cancels rejection:**<br>1. The Supervisor clicks "Cancel" on the rejection dialog.<br>2. The System closes the dialog without making changes.<br>3. The matrix status remains "Pending Approval".<br>4.The use case ends.|
|---|---|
|**Exceptions:**|**12. Database update fails:**<br>1. The System displays: "The rejection could not be processed. Please try<br>again."<br>2. The System logs the error with full details.<br>3. The matrix status remains unchanged.<br>4. The rejection reason is not saved.<br>5. The use case ends.<br>**15. Notification service fails:**<br>1. The System completes the rejection anyway.<br>2. The System logs that the notification failed.<br>3. The System queues the notification for retry.<br>4. The System displays a warning: "Matrix rejected, but advisor notification<br>may be delayed."<br>**16. Email delivery fails:**<br>1. The System completes the rejection and in-app notification.<br>2. The System logs the email failure.<br>3. The System will retry email delivery later.<br>4. The rejection is still valid.|
|**Requirements:**|**RF-MAT-004:**The system shall allow the immediate supervisor to approve<br>or reject offer matrices submitted by advisors.<br>**RF-MAT-005:**The system shall require supervisors to provide rejection<br>reasons when rejecting matrices.<br>**RF-CRM-013:**The system shall allow the immediate supervisor to review<br>and approve commercial proposals generated by advisors.|



Table 2.23 (continued) 

71 

|**Name of Use Case:**|Review Operator Availability|
|---|---|
|**Created By:**|BOPADIGITAL<br>**Last Updated By:**<br>BOPADIGITAL|
|**Date Created:**|21/12/25<br>**Last**<br>**Revision**<br>**Date:**<br>11/01/2026|
|**Description:**|The Sales Advisor or Coordinator verifies service availability with the<br>telecommunications operator (Telefónica Movistar) for a specific geographic<br>locationbefore creating anoffer matrixoractivating services.|
|**Actors:**|SalesAdvisor,Administrator, Carrier(external)|
|**Preconditions:**|1. The user must be authenticated in the system.<br>2. The client must have a registered address or geographic location.<br>3. The operator's API or verification system must be accessible.<br>4.Internet connectivitymust be available.|
|**Postconditions:**|1. Service availability information is retrieved and displayed.<br>2. The availability check is logged with timestamp and result.<br>3. The user knows which services can be offered to the client.<br>4. Unavailable services areidentified with reasons.|
|**Flow:**|1. The User accesses the client profile in the CRM module.<br>2. The User navigates to the "Service Availability" section or initiates matrix<br>creation.<br>3. The System displays the client's registered address and geographic<br>coordinates (if available).<br>4. The User clicks "Check Operator Availability".<br>5. The System validates that the client has a complete address registered.<br>6. The System displays a loading indicator: "Checking service availability<br>with operator..."<br>7. The System sends a request to the operator's API with: Client address,<br>Geographic coordinates, Requested service types (Voice, Connectivity,<br>Digital Services).<br>8. The Operator System processes the request and returns availability data.<br>9. The System receives the response and processes the information.<br>10. The System displays service availability results organized by category:<br>Available<br>Services<br>(green<br>indicator):<br>Service<br>name,<br>Maximum<br>capacity/speed, Estimated installation time. Partially Available Services<br>(yellow indicator): Service name, Limitations or conditions, Alternative<br>options. Unavailable Services (red indicator): Service name, Reason for<br>unavailability, Estimated availability date (if known).<br>11. The User reviews the availability information.<br>12. The System logs the availability check with: User ID, Client ID, Check<br>timestamp, Services queried, Results summary.<br>13.Ifyou create amatrix, only available services canbe selected.|
|**Alternative Flows:**|**5a. Client address incomplete:**<br>1. The System displays: "Client address is incomplete. Please update the client<br>address before checking availability."<br>2. The System provides a link to edit client information.<br>3. The User can either: Update the address and retry, Cancel the availability<br>check.<br>4. The use case ends if canceled.|



Table 2.24 Use Case Documentation - Review Operator Availability 

72 

||**8a. Operator API is unavailable:**<br>1. The System displays: "Unable to connect to operator system. Using cached<br>data (last updated: [date])."<br>2. The System displays the most recent availability data from cache.<br>3. The System displays a warning: "This information may be outdated. Please<br>try again later for current availability."<br>4. The flow continues at step 10 with cached data.<br>**8b. Operator returns partial response:**<br>1. The System displays the available information.<br>2. The System shows a warning for services without information:<br>"Availability unknown contact operator directly."<br>3. The flow continues at step 11.<br>**10a. User requests detailed coverage map:**<br>1. The User clicks "View Coverage Map".<br>2. The System displays an interactive map showing: Client location, Service<br>coverage areas by type, Network infrastructure details, Signal strength<br>indicators.<br>3. The User can zoom and pan to explore coverage.<br>4. The User closes the map to return to the results.<br>**13a. User saves availability report:**<br>1. The User clicks "Save Availability Report".<br>2. The System generates a PDF report with all availability information.<br>3. The System attaches the report to the client's documents.<br>4.The Systemdisplays:"Availabilityreport saved to client documents."|
|---|---|
|**Exceptions:**|**8. Operator API timeout:**<br>1. The System displays: "The operator system is taking too long to respond.<br>Please try again in a few minutes."<br>2. The System logs the timeout error.<br>3. The availability check is marked as failed.<br>4. The use case ends.<br>**8. Operator returns error:**<br>1. The System displays: "The operator system returned an error: [error<br>message]. Please contact support if this persists."<br>2. The System logs the full error details.<br>3. The use case ends.<br>**9. Invalid response format:**<br>1. The System displays: "Received invalid data from operator system. Please<br>try again or contact support."<br>2. The System logs the response for technical analysis.<br>3. The use case ends.<br>**5. No client address registered:**<br>1. The System displays: "Cannot check availability without a client address."<br>2. The System displays a form to enter the client address.<br>3.The User mustenter theaddress before proceeding.|



Table 2.24 (continued) 

73 

|**Requirements:**|**RF-MAT-008:**The system shall verify service availability with the operator<br>before allowing matrix creation.<br>**RF-SRV-001:**The system shall integrate with operator APIs to check real-<br>time service availability.<br>**RF-SRV-002:**The system shall display service coverage information for<br>client locations.|
|---|---|



Table 2.24 (continued) 

74 

|**Name of Use Case:**|Check Matrix ApprovalStatus|
|---|---|
|**Created By:**|BOPADIGITAL<br>**Last Updated By:**<br>BOPADIGITAL|
|**Date Created:**|21/12/25<br>**Last**<br>**Revision**<br>**Date:**<br>11/01/2026|
|**Description:**|The Sales Advisor consults the current approval status of offer matrices<br>submitted to the immediate supervisor to know whether they can proceed with<br>client presentationor need to adjust.|
|**Actors:**|SalesAdvisor|
|**Preconditions:**|1. The advisor must be authenticated in the system.<br>2. At least one offer matrix must have been created and submitted for<br>approval.<br>3.Thematrix must be associated witha client assigned to the advisor.|
|**Postconditions:**|1. The advisor is informed of the current matrix status.<br>2. If rejected, the advisor can view the rejection reasons.<br>3.The status consultation isloggedfortracking purposes.|
|**Flow:**|1. The Sales Advisor accesses the CRM module.<br>2. The Advisor navigates to "My Matrices" or accesses a specific client's<br>negotiation.<br>3. The System displays all matrices created by the advisor with the following<br>information: Matrix ID, Client Name, Creation Date, Submission Date,<br>Current Status, Last Update Date, Reviewing Supervisor.<br>4. The System displays matrices with status indicators: "Draft" (gray),<br>"Pending Approval" (yellow), "Approved" (green), "Rejected" (red),<br>"Information Requested" (orange).<br>5. The Advisor can filter matrices by: Status, Client, Date range, Negotiation.<br>6. The Advisor selects a specific matrix to view detailed status.<br>7. The System displays the matrix status details including: Current status with<br>timestamp, Status history timeline showing all status changes, Supervisor<br>comments (if any), Approval/rejection date (if applicable), Rejection reasons<br>(if rejected), Requested information (if information requested).<br>8. If the status is "Approved", the System displays: "This matrix has been<br>approved. You may proceed to present it to the client."<br>9. If the status is "Rejected", the System displays: "This matrix was rejected.<br>Please review the comments and create a new matrix addressing the<br>concerns."<br>10. If the status is "Information Requested", the System displays: "Additional<br>information is required. Please respond to the supervisor's request."<br>11. The Advisor can take appropriate action based on the status: View<br>supervisor comments, Create a revised matrix, Respond to information<br>requests,Download approvedmatrix forclient presentation.|
|**Alternative Flows:**|**5a. Advisor filters by pending status:**<br>1. The Advisor selects "Pending Approval" filter.<br>2. The System displays only matrices awaiting supervisor review.<br>3. The System sorts by submission date (oldest first).<br>4. The System displays: "You have [N] matrices pending approval."<br>5. The flow continues at step 6.<br>**10a. Advisor responds to information request:**<br>1. The Advisor clicks "Respond to Request".<br>2. The System displays a form to provide the requested information.|



Table 2.25 Use Case Documentation - Check Matrix Approval Status 

75 

||3. The Advisor enters the additional information or clarifications.<br>4. The Advisor optionally attaches supporting documents.<br>5. The Advisor clicks "Submit Response".<br>6. The System updates the matrix status to "Pending Approval" with new<br>information.<br>7. The System notifies the supervisor of the response.<br>8. The System displays: "Response submitted successfully."<br>**9a. Advisor creates revised matrix after rejection:**<br>1. The Advisor clicks "Create Revised Matrix" from the rejected matrix<br>details.<br>2. The System creates a new matrix duplicating the original data.<br>3. The System adds a reference to the rejected matrix.<br>4. The System displays the rejection comments prominently.<br>5. The Advisor makes necessary adjustments.<br>6. The flow continues with matrix creation process.<br>**11a. Advisor downloads approved matrix:**<br>1. The Advisor clicks "Download Matrix" on an approved matrix.<br>2. The System generates a PDF document with: Matrix details, All services<br>and pricing, Applied subsidies, Approval information, Terms and conditions.<br>3. The System downloads the formatted matrix.<br>4.The System logs the download action.|
|---|---|
|**Exceptions:**|**3. No matrices found:**<br>1. The System displays: "You have not created any offer matrices yet."<br>2. The System displays a "Create New Matrix" button.<br>3. The use case ends.<br>**7. Matrix details cannot be loaded:**<br>1. The System displays: "Matrix details are temporarily unavailable. Please<br>try again."<br>2. The System logs the error.<br>3. The use case ends.<br>**2. Database connection fails:**<br>1. The System displays: "Unable to retrieve matrix information. Please check<br>your connection and try again."<br>2. The System logs the error.<br>3. The use case ends.|
|**Requirements:**|**RF-MAT-006:**The system shall allow sales advisors to view the approval<br>status of their submitted matrices.<br>**RF-MAT-007:**The system shall display supervisor comments and rejection<br>reasons for matrices.|



Table 2.25 (continued) 

76 

|**Name of Use Case:**|Consult Clients andTheir DocumentationStatus|
|---|---|
|**Created By:**|BOPADIGITAL<br>**Last Updated By:**<br>BOPADIGITAL|
|**Date Created:**|21/12/25<br>**Last**<br>**Revision**<br>**Date:**<br>11/01/2026|
|**Description:**|The Immediate Supervisor or Coordinator views a comprehensive list of<br>clients with their documentation status to identify pending documentation and<br>trackwhichadvisor isresponsibleforeachclient.|
|**Actors:**|Immediate Supervisor,Administrator|
|**Preconditions:**|1. The user must be authenticated with the appropriate role.<br>2. Client records must exist in the database.<br>3.The documentmanagementmodulemust be operational.|
|**Postconditions:**|1. The user has visibility of all clients and their documentation status.<br>2. The user can identify clients with incomplete documentation.<br>3.The usercantrack responsible advisorsfor follow-up.|
|**Flow:**|1. The User accesses the "Documentation Management" section in the CRM<br>module.<br>2. The User selects "Client Documentation Status" from the menu.<br>3. The System queries all clients within the user's scope (team for supervisors,<br>all for coordinators).<br>4. The System displays a table with the following columns: Client Name,<br>RUC<br>(Tax<br>ID),<br>Assigned<br>Advisor,<br>Documentation<br>Status<br>(Complete/Incomplete/Pending Review), Required Documents (X of Y<br>completed), Optional Documents (count), Last Document Upload Date,<br>Status Indicator (color-coded).<br>5. The System uses color coding: Green for "Complete", Yellow for "In<br>Progress", Red for "Missing Critical Documents".<br>6. The User reviews the list to identify clients requiring attention.<br>7. The User can sort the list by any column (client name, status, advisor, date).<br>8.<br>The<br>User<br>can<br>apply<br>filters:<br>Documentation<br>status<br>(Complete/Incomplete/Pending), Assigned advisor, Date range for last<br>upload, Specific missing documents.<br>9. The User selects a specific client to view detailed documentation status.<br>10. The System displays the client's complete documentation dashboard<br>showing: Checklist of required documents with status, List of optional<br>documents uploaded, Document history timeline, Responsible advisor contact<br>information, Action buttons (Notify Advisor, View Documents, Download<br>All).<br>11. The User can take action: Notify the advisor about pending documents,<br>View ordownload specific documents,Markdocumentationasreviewed.|
|**Alternative Flows:**|**8a. User filters by incomplete documentation:**<br>1. The User selects "Incomplete" from the status filter.<br>2. The System displays only clients with missing required documents.<br>3. The System sorts by urgency (oldest pending first).<br>4. The flow continues at step 9.<br>**8b. User filters by specific advisor:**<br>1. The User selects an advisor from the dropdown filter.<br>2. The System displays only clients assigned to that advisor.<br>3. The System displays advisor performance metrics: Total clients, Clients<br>with complete documentation (%), Average documentation completion time.|



Table 2.26 Use Case Documentation - Consult Clients and Their Documentation Status 

77 

||4. The flow continues at step 9.<br>**11a. User notifies advisor about pending documents:**<br>1. The User clicks "Notify Advisor" for a specific client.<br>2. The System displays a notification dialog with: List of missing documents<br>(pre-selected), Optional message field, Notification urgency level<br>(Normal/Urgent).<br>3. The User adds a custom message if needed.<br>4. The User clicks "Send Notification".<br>5. The System sends an email and in-app notification to the advisor.<br>6. The System records the notification in the client history.<br>7. The System displays: "Advisor notified successfully."<br>**11b. User exports documentation status report:**<br>1. The User clicks "Export Report".<br>2. The System displays export options: Excel or PDF format, Include only<br>filtered results or all clients, Include detailed document checklist.<br>3. The User selects preferences and clicks "Generate Report".<br>4. The System generates the report file.<br>5. The System initiates download of the report.|
|---|---|
|**Exceptions:**|**3. Database query fails:**<br>1. The System displays: "Unable to load client documentation status. Please<br>try again."<br>2. The System logs the error for technical review.<br>3. The use case ends.<br>**10. Client details cannot be loaded:**<br>1. The System displays: "Client documentation details are temporarily<br>unavailable."<br>2. The System displays basic client information available in cache.<br>3. The User can retry or return to the list.<br>**4. No clients found:**<br>1. The System displays: "No clients found within your scope."<br>2.The use case ends.|
|**Requirements:**|**RF-DOC-004:**<br>The<br>system<br>shall<br>display<br>documentation<br>status<br>(complete/pending/missing) for each client.<br>**RF-CRM-016:**The system shall allow coordinators to verify pending<br>documentation and track which advisor is responsible.<br>**RF-CRM-010:**The system shall allow the immediate supervisor to view all<br>business clients assigned to their team.|



Table 2.26 (continued) 

78 

|**Name of Use Case:**<br>|DownloadDocumentation<br> <br>|
|---|---|
|**Created By:**|BOPADIGITAL<br>**Last Updated By:**<br>BOPADIGITAL|
|**Date Created:**|21/12/25<br>**Last**<br>**Revision**<br>**Date:**<br>11/01/2026|
|**Description:**|Authorized users download client documentation from the system for review,<br>processing, orexternalsubmissionto the operator.<br>|
|**Actors:**|SalesAdvisor,Immediate Supervisor,Administrator|
|**Preconditions:**|The user must be authenticated in the system.<br>2. The document must exist in the system.<br>3. The user must have permission to access the client's documents.<br>4.ForSalesAdvisors, the clientmust be assigned to themorbeintheirteam.|
|**Postconditions:**|1. The document file is downloaded to the user's device.<br>2. The download action is logged in the system audit trail.<br>3.Document access statistics are updated.|
|**Flow:**|1. The User accesses the client profile in the CRM module.<br>2. The User navigates to the "Documents" tab.<br>3. The System displays all documents associated with the client including:<br>Document name, Document type, Upload date, File size, uploaded by, Tags.<br>4. The User can optionally filter documents by: Document type, Date range,<br>Tags, Advisor who uploaded.<br>5. The User locates the desired document.<br>6. The User clicks the "Download" button or download icon next to the<br>document.<br>7. The System verifies the user has permission to access the document.<br>8. The System retrieves the document file from secure storage.<br>9. The System initiates the file download to the user's device.<br>10. The System logs the download action including: User ID, Document ID,<br>Client ID, Download timestamp, User's IP address.<br>11. The System increments the document's download counter.<br>12. The download completes successfully.<br>13. The System displays a brief confirmation: "Document downloaded<br>successfully."|
|**Alternative Flows:**|**6a. User previews document before downloading:**<br>1. The User clicks "Preview" instead of "Download".<br>2. The System displays the document in a preview window (for supported<br>formats).<br>3. The User reviews the document.<br>4. The User clicks "Download" from the preview window.<br>5. The flow continues at step 7.<br>**6b. User downloads multiple documents:**<br>1. The User selects multiple documents using checkboxes.<br>2. The User clicks "Download Selected" or "Download All".<br>3. The System creates a ZIP archive containing all selected documents.<br>4. The System names the archive: "[Client Name]__Documents__[Date].zip".<br>5. The flow continues at step 7 with the ZIP file.|



Table 2.27 Use Case Documentation - Download Documentation 

79 

||**4a. User applies filters:**<br>1. The System updates the document list based on filter criteria.<br>2. The System displays: "Showing [N] documents matching your filters."<br>3. The flow continues at step 5 with filtered results.|
|---|---|
|**Exceptions:**|**7. Permission denied:**<br>1. The System displays: "Access denied. You do not have permission to<br>download this document."<br>2. The System logs the unauthorized access attempt.<br>3. The use case ends.<br>**8. Document file not found:**<br>1. The System displays: "Document file is missing or has been deleted. Please<br>contact support."<br>2. The System logs the error with document ID and storage location.<br>3. The System notifies the system administrator.<br>4. The use case ends.<br>**9. Download interrupted:**<br>1. The System detects the connection failure.<br>2. The System attempts to resume the download if the browser supports it.<br>3. If resume fails, the System displays: "Download interrupted. Please try<br>again."<br>4. The partial download action is still logged.<br>5. The use case ends.<br>**3. No documents available:**<br>1. The System displays: "No documents have been uploaded for this client<br>yet."<br>2. If the user is an advisor, the System displays an "Upload Document" button.<br>3.The use case ends.|
|**Requirements:**|**RF-DOC-006:**The system shall allow authorized users to download client<br>documentation.<br>**RF-DOC-007:**The system shall log all documents and download actions for<br>audit purposes.|



Table 2.27 (continued) 

80 

|**Name of Use Case:**|TagDocumentation|
|---|---|
|**Created By:**|BOPADIGITAL<br>**Last Updated By:**<br>BOPADIGITAL|
|**Date Created:**|21/12/25<br>**Last**<br>**Revision**<br>**Date:**<br>11/01/2026|
|**Description:**|The Sales Advisor or Coordinator adds or modifies tags to uploaded<br>documents to improve organization, searchability, and categorization within<br>the documentmanagement system.<br>|
|**Actors:**|SalesAdvisor,Administrators|
|**Preconditions:**|1. The user must be authenticated in the system.<br>2. At least one document must be uploaded to a client profile.<br>3. The user must have permission to manage documentation.<br>4.ForSalesAdvisors, the clientmust be assigned to them.|
|**Postconditions:**|1. Document tags are updated in the database.<br>2. The tag modification is recorded in the document history.<br>3. Document searchability is improved based on new tags.<br>4.The tagging action islogged withuser IDand timestamp.|
|**Flow:**|1. The User accesses the client profile in the CRM module.<br>2. The User navigates to the "Documents" tab.<br>3. The System displays all documents uploaded for the client with their<br>current tags.<br>4. The User selects a specific document to tag.<br>5. The User clicks "Edit Tags" or the tag icon.<br>6. The System displays the tag management interface showing: Current tags<br>(removable), Suggested tags based on document type, Custom tag input field,<br>Recently used tags.<br>7. The User can perform any of the following actions: Add new tags by typing<br>and pressing Enter, Select from suggested tags, Remove existing tags by<br>clicking the X icon, Add multiple tags separated by commas.<br>8. The System validates tag format (alphanumeric, max 50 characters per tag).<br>9. The System prevents duplicate tags.<br>10. The User clicks "Save Tags".<br>11. The System updates the document record with the new tag set.<br>12. The System records the tag modification in the document history with:<br>User ID, Previous tags, New tags, Timestamp.<br>13. The System updates the document search index.<br>14. The System displays a confirmation message: "Tags updated<br>successfully."|
|**Alternative Flows:**|**6a. Document has no tags:**<br>1. The System displays: "No tags currently assigned. Add tags to improve<br>document organization."<br>2. The System suggests tags based on document type and client category.<br>3. The flow continues at step 7.<br>**8a. Invalid tag format:**<br>1. The System displays a validation error: "Tag '[tag name]' is invalid. Tags<br>must be alphanumeric and under 50 characters."<br>2. The System highlights the invalid tag.<br>3. The User corrects the tag.<br>4. The flow returns to step 8.|



Table 2.28 Use Case Documentation - Tag Documentation 

81 

||**9a. Duplicate tag detected:**<br>1. The System silently prevents adding the duplicate tag.<br>2. The System displays a brief notification: "Duplicate tag ignored."<br>3. The flow continues normally.<br>**7a. User applies bulk tags to multiple documents:**<br>1. The User selects multiple documents using checkboxes.<br>2. The User clicks "Bulk Tag".<br>3. The System displays a tag input for multiple documents.<br>4. The User enters tags to apply to all selected documents.<br>5. The System applies tags to all selected documents.<br>6.Theflow continues at step11 foreachdocument.|
|---|---|
|**Exceptions:**|**11. Database update fails:**<br>1. The System displays: "Tags could not be saved. Please try again."<br>2. The System logs the error.<br>3. The previous tags remain unchanged.<br>4. The use case ends.|
||**13. Search index update fails:**<br>1. The System completes the tag update anyway.<br>2. The System logs the indexing error.<br>3. The System schedules a reindex operation.<br>4.The tags are saved butmaynot beimmediately searchable.|
|**Requirements:**|**RF-DOC-002:**The system shall automatically tag uploaded documents based<br>on document type.<br>**RF-DOC-005:**The system shall allow users to add custom tags to documents<br>for improved organization.|



Table 2.28 (continued) 

82 

|**Name of Use Case:**<br>|ReviewDocumentationUploaded toProfile<br> <br>|
|---|---|
|**Created By:**|BOPADIGITAL<br>**Last Updated By:**<br>BOPADIGITAL|
|**Date Created:**|21/12/25<br>**Last**<br>**Revision**<br>**Date:**<br>11/01/2026|
|**Description:**|The Immediate Supervisor or Coordinator reviews all documentation<br>uploaded by sales advisors to client profiles to verify completeness and<br>compliance before service activation.<br>|
|**Actors:**|Immediate Supervisor,Administrator|
|**Preconditions:**|1. The user must be authenticated with the appropriate role.<br>2. The client profile must exist in the database.<br>3. At least one document must have been uploaded to the client profile.<br>4.The user musthave permissiontoreview documentation.|
|**Postconditions:**|1. The user has reviewed the client's documentation status.<br>2. Document review actions are logged in the system.<br>3.The usercan identifymissing or incomplete documentation.|
|**Flow:**|1. The User accesses the "Document Management" section in the CRM<br>module.<br>2. The User searches for a client by RUC or Business Name.<br>3. The System displays search results with basic client information.<br>4. The User selects the specific client.<br>5. The System displays the client's document dashboard showing: Required<br>documents checklist with status (Complete/Pending/Missing), Optional<br>documents list, Total number of uploaded documents, Last document upload<br>date and user.<br>6. The User reviews the documentation status summary.<br>7. The User clicks on a specific document category to view details.<br>8. The System displays a list of all documents in that category including:<br>Document name, Upload date, Uploaded by (advisor name), File size, Tags,<br>Status (Pending Review/Approved/Rejected).<br>9. The User selects a specific document to view.<br>10. The System displays the document preview or download option.<br>11. The User reviews the document content.<br>12. The User may mark the document as "Reviewed", "Approved", or<br>"Requires Correction".<br>13. If marking as "Requires Correction", the System requests a comment<br>explaining the issue.<br>14. The System records the review action with user ID and timestamp.<br>15. The System updates the document status.<br>16. If all required documents are approved, the System updates the client<br>status to"DocumentationComplete".|
|**Alternative Flows:**|**6a. Missing required documents:**<br>1. The System highlights missing required documents in red.<br>2. The System displays: "Missing required documents: [list of documents]."<br>3. The User may click "Notify Advisor" to send a reminder.<br>4. The System sends a notification to the responsible advisor.<br>5. The flow continues at step 7.|



Table 2.29 Use Case Documentation - Review Documentation Uploaded to Profile 

83 

||**12a. User requests document re-upload:**<br>1. The User clicks "Request Re-upload".<br>2. The System displays a text field for specifying the reason.<br>3. The User enters the reason.<br>4. The System marks the document as "Rejected Re-upload Required".<br>5. The System sends a notification to the advisor who uploaded it.<br>6. The flow continues at step 14.<br>**10a. Document preview not available:**<br>1. The System displays: "Preview not available for this file type."<br>2. The System offers a "Download" button instead.<br>3.Theflow continues at step11.|
|---|---|
|**Exceptions:**|**2. Search returns no results:**<br>1. The System displays: "No clients found with the given criteria."<br>2. The User may modify search parameters or cancel.<br>3. The use case ends if canceled.<br>**8. Document retrieval fails:**<br>1. The System displays: "Unable to load documents at this time. Please try<br>again."<br>2. The System logs the error for technical review.<br>3. The use case ends.<br>**10. Document file not found in storage:**<br>1. The System displays: "Document file is missing or corrupted. Please<br>contact support."<br>2. The System logs the error with document ID.<br>3.The Usercansee documentmetadata but cannot view content.|
|**Requirements:**|**RF-DOC-003:**The system shall allow supervisors and coordinators to review<br>documentation uploaded to client profiles.<br>**RF-DOC-004:**<br>The<br>system<br>shall<br>display<br>documentation<br>status<br>(complete/pending/missing) for each client.<br>**RF-CRM-016:**The system shall allow coordinators to verify pending<br>documentation and track which advisor is responsible.|



Table 2.29 (continued) 

84 

|**Name of Use Case:**|Add ClientDocumentation|
|---|---|
|**Created By:**|BOPADIGITAL<br>**Last Updated By:**<br>BOPADIGITAL|
|**Date Created:**|21/12/25<br>**Last**<br>**Revision**<br>**Date:**<br>11/01/2026|
|**Description:**<br>|The Sales Advisor uploads required and optional documents to the client's<br>profile to support thenegotiationand service activationprocess.<br>|
|**Actors:**|SalesAdvisor|
|**Preconditions:**|1. The advisor must be authenticated in the system.<br>2. The client must exist in the database and be assigned to the advisor.<br>3. The document management module must be operational.<br>4. Documents must be in supported formats (PDF, JPG, PNG, DOCX).<br>5.Document sizemustnot exceed 50MBper file.|
|**Postconditions:**|1. The document is stored in the system linked to the client profile.<br>2. The document receives automatic tags based on content type.<br>3. The upload event is recorded in the client history.<br>4. The document becomes visible to authorized users.<br>5.Pending documentationcounters are updated.|
|**Flow:**|1. The Sales Advisor accesses the client profile in the CRM module.<br>2. The Advisor navigates to the "Documents" tab.<br>3. The System displays the current documentation list and pending<br>requirements.<br>4. The Advisor clicks "Upload New Document".<br>5. The System displays the document upload form with fields: Document type<br>(dropdown), Description (optional), Tags (optional), File selector.<br>6. The Advisor selects the document type from available options: RUC (Tax<br>ID), Constitutional document, Legal representative ID, Power of attorney,<br>Proof of address, Other.<br>7. The Advisor optionally enters a description.<br>8. The Advisor clicks "Select File" and chooses the document from their<br>device.<br>9. The System validates the file format.<br>10. The System validates the file size.<br>11. The Advisor reviews the selected file information.<br>12. The Advisor clicks "Upload Document".<br>13. The System uploads the file to secure storage.<br>14. The System automatically generates tags based on document type.<br>15. The System creates a document record in the database linked to the client.<br>16. The System records metadata: Upload date and time, Uploading user, File<br>name and size, Document type.<br>17. The System updates pending documentation status.<br>18. The System displays a success message: "Document uploaded<br>successfully."|
|**Alternative Flows:**|**9a. Invalid file format:**<br>1. The System rejects the file and displays: "Invalid file format. Accepted<br>formats are: PDF, JPG, PNG, DOCX."<br>2. The flow returns to step 8.<br>**10a. File size exceeds limit:**<br>1. The System rejects the file and displays: "File size exceeds the 50MB limit.<br>Please compress the file or upload a smaller version."|



Table 2.30 Use Case Documentation - Add Client Documentation 

85 

||2. The flow returns to step 8.<br>**14a. Advisor adds custom tags:**<br>1. The Advisor clicks "Add Custom Tag".<br>2. The System displays a text field.<br>3. The Advisor enters custom tags separated by commas.<br>4. The System validates and adds the tags.<br>5.Theflow continues at step15.|
|---|---|
|**Exceptions:**|**13. Upload fails due to connectivity issues:**<br>1. The System displays: "Upload failed due to connection issues. Please check<br>your internet connection and try again."<br>2. The System logs the error.<br>3. The selected file remains in the form for retry.<br>4. The use case ends.<br>**15. Database record creation fails:**<br>1. The System displays: "The document was uploaded but could not be<br>registered. Please contact support."<br>2. The System logs the error with file reference.<br>3. The uploaded file is quarantined for manual recovery.<br>4.The use case ends.|
|**Requirements:**|**RF-DOC-001:**The system shall allow sales advisors to upload client<br>documentation to support negotiations.<br>**RF-DOC-002:**The system shall automatically tag uploaded documents based<br>on document type.|



Table 2.30 (continued) 

86 

|**Name of Use Case:**|Review andApprove NewMatrices|
|---|---|
|**Created By:**|BOPADIGITAL<br>**Last Updated By:**<br>BOPADIGITAL|
|**Date Created:**|21/12/25<br>**Last**<br>**Revision**<br>**Date:**<br>11/01/2026|
|**Description:**<br>|The Immediate Supervisor reviews offer matrices submitted by sales advisors<br>and approves or rejects thembased oncommercialpolicies and businessrules.<br>|
|**Actors:**|Immediate Supervisor|
|**Preconditions:**|1. The supervisor must be authenticated in the system.<br>2. At least one offer matrix must be in "Pending Approval" status.<br>3. The matrix must belong to an advisor in the supervisor's team.<br>4.The supervisor musthave approvalpermissions.|
|**Postconditions:**|1. The matrix status is updated to "Approved" or "Rejected".<br>2. The sales advisor receives a notification of the decision.<br>3. The approval or rejection is recorded in the audit log.<br>|
||4.Ifapproved, thematrixbecomes available to present to the client.|
|**Flow:**|1. The Immediate Supervisor accesses the "Matrix Approvals" section in the<br>CRM module.<br>2. The System displays a list of pending matrices including: Client name,<br>Sales advisor, Creation date, Total value, Subsidy amount, Current status.<br>3. The Supervisor reviews the list of pending approvals.<br>4. The Supervisor selects a specific matrix to review.<br>5. The System displays the complete matrix details including: Selected<br>services and quantities, Individual and total prices, Applied subsidies and<br>calculations, Client information and current billing, Advisor observations.<br>6. The Supervisor reviews the commercial viability of the offer.<br>7. The Supervisor verifies compliance with company policies.<br>8. The Supervisor clicks either "Approve Matrix" or "Reject Matrix".<br>9. If rejecting, the System displays a mandatory field requesting motive.<br>10. The Supervisor enters comments explaining the decision.<br>11. The Supervisor clicks "Confirm Decision".<br>12. The System validates that comments are provided if rejecting.<br>13. The System updates the matrix status accordingly.<br>14. The System records the decision in the audit log with: Supervisor ID,<br>Decision (Approved/Rejected), Timestamp, Comments.<br>15. The System sends a notification to the sales advisor.<br>16.<br>The<br>System<br>displays<br>a<br>confirmation<br>message:<br>"Matrix<br>[Approved/Rejected] successfully."|
|**Alternative Flows:**|**8a. Supervisor needs more information:**<br>1. The Supervisor clicks "Request Additional Information".<br>2. The System displays a text field for the information request.<br>3. The Supervisor enters the required information details.<br>4. The System updates the matrix status to "Information Requested".<br>5. The System sends a notification to the advisor.<br>6. The use case ends.<br>**12a. Missing rejection comments:**<br>1. The System displays: "Rejection reason is mandatory. Please provide<br>comments."<br>2. The System does not allow proceeding until comments are entered.<br>3. The flow returns to step 10.|



Table 2.31 Use Case Documentation - Review and Approve New Matrices 

87 

|**Exceptions:**|**13. Status update fails:**<br>1. The System displays: "The decision could not be processed. Please try<br>again."<br>2. The System logs the error.<br>3. The matrix status remains unchanged.<br>4. The use case ends.<br>**2. No pending matrices:**<br>1. The System displays: "There are no matrices pending approval at this time."<br>2.The use case ends.|
|---|---|
|**Requirements:**|**RF-MAT-004:**The system shall allow the immediate supervisor to approve<br>or reject offer matrices submitted by advisors.<br>**RF-CRM-013:**The system shall allow the immediate supervisor to review<br>and approve commercial proposals generated by advisors.|



Table 2.31 (continued) 

88 

|**Name of Use Case:**|Request Supervisor Approval|
|---|---|
|**Created By:**|BOPADIGITAL<br>**Last Updated By:**<br>BOPADIGITAL|
|**Date Created:**|21/12/25<br>**Last**<br>**Revision**<br>**Date:**<br>11/01/2026|
|**Description:**<br>|The Sales Advisor submits an offer matrix for review and approval by the<br>immediate supervisorbefore presentingit to the client.<br>|
|**Actors:**|SalesAdvisor|
|**Preconditions:**|1. The advisor must be authenticated in the system.<br>2. An offer matrix must exist and be in "Draft" or "Pending Approval" status.<br>3. The matrix must be complete with all required information.<br>4.The advisor musthave permissiontorequest approval.|
|**Postconditions:**|1. The matrix status changes to "Pending Approval".<br>2. The immediate supervisor receives a notification.<br>3. The matrix becomes visible in the supervisor's approval queue.<br>4.Therequestislogged withtimestamp and advisor information.|
|**Flow:**|1. The Sales Advisor accesses the client's negotiation details.<br>2. The Advisor navigates to the "Offer Matrices" section.<br>3. The System displays all matrices associated with the negotiation and their<br>current status.<br>4. The Advisor selects a matrix in "Draft" status.<br>5. The Advisor reviews the matrix details.<br>6. The Advisor clicks "Request Approval".<br>7. The System displays a confirmation dialog: "Are you sure you want to<br>submit this matrix for supervisor approval?".<br>8. The Advisor confirms the submission.<br>9. The System validates that the matrix is complete.<br>10. The System updates the matrix status to "Pending Approval".<br>11. The System records the approval request with date, time, and advisor ID.<br>12. The System sends a notification to the immediate supervisor.<br>13. The System sends a notification email to the supervisor.<br>14. The System displays a confirmation message: "Approval request<br>submitted successfully.Yoursupervisorwill review thematrixshortly."|
|**Alternative Flows:**|**9a. Matrix incomplete:**<br>1. The System displays: "The matrix cannot be submitted. Please complete<br>all required fields: [list of missing fields]."<br>2. The Advisor clicks "Edit Matrix" to complete the information.<br>3. The use case ends.<br>**8a. Advisor cancels:**<br>1. The System closes the confirmation dialog.<br>2. The matrix status remains unchanged.<br>3. The use case ends.|
|**Exceptions:**|**10. Status update fails:**<br>1. The System displays: "The approval request could not be processed. Please<br>try again."<br>2. The System logs the error.<br>3. The matrix status remains unchanged.<br>4.The use case ends.|



Table 2.32 Use Case Documentation - Request Supervisor Approval 

89 

||**12. Notification service unavailable:**<br>1. The System completes the status update anyway.<br>2. The System logs that the notification failed.<br>3. The System will attempt to resend the notification later.<br>4. The System displays a warning: "Approval requested, but supervisor<br>notification may be delayed."|
|---|---|
|**Requirements:**|**RF-MAT-002:**The system shall allow the sales advisor to submit offer<br>matricesforsupervisorapproval.|



Table 2.32 (continued) 

90 

|**Name of Use Case:**<br>Create Offer Matrix forSpecific Clients|
|---|
|**Created By:**<br>BOPADIGITAL<br>**Last Updated By:**<br>BOPADIGITAL|
|**Date Created:**<br>21/12/25<br>**Last**<br>**Revision**<br>11/01/2026|
|**Date:**|
|**Description:**<br>The Sales Advisor creates a new offer matrix for a specific business client,<br>defining the proposed services, quantities, and calculating the applicable<br>subsidies based on the client's billing and service portfolio.<br><br>|
|**Actors:**<br>SalesAdvisor|
|**Preconditions:**<br>1. The advisor must be authenticated in the system.<br>2. The client must be registered and assigned to the advisor.<br>3. There must be an active negotiation with the client.<br>4.The service catalogmust be accessible.|
|**Postconditions:**<br>1. A new offer matrix is created and stored in the database.<br>2. The matrix is linked to the client and the active negotiation.<br>3. The subsidy amount is automatically calculated based on business rules.<br>4. The matrix enters "Pending Approval" status.<br>5.Theimmediate supervisor receives anotificationofthenewmatrix.|
|**Flow:**<br>1. The Sales Advisor accesses the client profile in the CRM module.<br>2. The Advisor navigates to the "Negotiations" section of the client.<br>3. The Advisor selects an active negotiation.<br>4. The Advisor clicks the "Create Offer Matrix" button.<br>5. The System displays the matrix creation form with available services<br>organized by category (Voice, Connectivity, Digital Services).<br>6. The Advisor selects the services to include in the offer.<br>7. The Advisor specifies the quantity for each selected service.<br>8. The System validates service availability with the operator.<br>9. The System automatically retrieves the client's current monthly billing.<br>10. The System automatically retrieves the client's number of active services.<br>11. The System calculates the applicable subsidy range based on: Client's<br>current billing amount, Number of services currently contracted, Number of<br>new services proposed in the matrix.<br>12. The System displays the total estimated benefit amount.<br>13. The Advisor adds observations or special notes about the offer.<br>14. The Advisor clicks "Save Matrix".<br>15. The System validates that all required fields are completed.<br>16. The System creates the matrix record in the database with status "Pending<br>Approval".<br>17. The System links the matrix to the client and negotiation.<br>18. The System sends a notification to the immediate supervisor for approval.<br>19. The System displays a confirmation message: "Offer matrix created<br> ’"|
|successfully.Awaiting supervisors approval.|
|**Alternative Flows:**<br>**8a. Service unavailable with operator**<br>1. The System displays a warning message: "The service [Service Name] is<br>not available in the client's geographic area."<br>2. The System removes the unavailable service from the selection.<br>3. The Advisor may select alternative services.<br>4. The flow returns to step 7.|



Table 2.33 Use Case Documentation - Create Offer Matrix for Specific Clients 

91 

||**15a. Validation fails**<br>1. The System displays specific error messages indicating missing or invalid<br>fields.<br>2. The Advisor completes or corrects the required information.<br>3.Theflowreturns to step14.|
|---|---|
|**Exceptions:**|**8. Operator availability check fails:**<br>1. The System displays: "Cannot verify service availability at this time. Please<br>try again later."<br>2. The System logs the error.<br>3. The use case ends.<br>**16. Matrix creation fails:**<br>1. The System displays: "The offer matrix could not be created. Please try<br>again."<br>2. The System logs the error for administrator review.<br>3. The entered data remains in the form.<br>4.The use case ends.|
|**Requirements:**|**RF-MAT-001:**The system shall allow the sales advisor to create a new offer<br>matrix associated with a business client and an ongoing negotiation.<br>**RF-MAT-003:**The system shall automatically calculate the applicable<br>subsidyrange based onclient billing and thenumberofproposed services,|



Table 2.33 (continued) 

92 

**2.3 Class Diagrams** 



<!-- Start of picture text -->
rrr ee ee ee ee ------------------+--+ ey<br>1'<br>'<br>'<br>1<br>'<br>'<br>1<br>Jp > '<br>1<br>'<br>------------S I<br>KE rrr cane 1<br>'<br>Po 1<br>' '<br>i<br>1 mot 1<br>1 I '<br>1 1 '<br>11 ' T T A ''<br>1 ' 1 ' 1 '<br>1 t 1 1 1 1<br>1 ' ' ' 1 '<br>! 1 1 1 1 '<br>1 '' a , 1 1<br>1 1 '<br>1 ' '<br><- -1 '1 ' '<br>'<br>' 1<br>' '<br>'' Ip ------------- 1'<br>'1' '<br>''1' K<----51 ''<br>' 1 '<br>Il' 11 ''<br>i Oeli ercctccrcrcte _ ''<br>iuraul 11 '1 '<br>Tvl tl 1 1 '<br>1 ! '<br>' 1 1<br>1 1 1<br>1 ! '<br>1 1 1<br>i f I<----------4<br>K-77 77 1 1'<br>1<br>1<br>1<br>1<br>1<br>t--------<br>jigm Community Edition<br><!-- End of picture text -->



<!-- Start of picture text -->
Auth<br>BcryptHasher<br>+generateHash(password : String) : String<br>has -hasher : PasswordHasher AuthService has +verifyPassword(plainPassword : String, hashPassword : String) : boolean<br>PostgresUserRepository<br>-users : UserRepository<br>+findByEmail(email : String) : SystemUser -tokenService : TokenService 1 -hasher<br>+login(email : String, plainPassword : String) : String <<Interface>><br>+checkPermission(token : String, resource : String, action : String) : boolean PasswordHasher<br>1<br>-users +generateHash(password : String) : String<br><<Interface>> +verifyPassword(plainPassword : String, hashPassword : String) : boolean<br>UserRepository<br>+findByEmail(email : String) : SystemUser has<br>1 -tokenService<br><<Interface>> JwtTokenService<br>TokenService +generateToken(user : SystemUser) : String<br>+generateToken(user : SystemUser) : String +validateToken(token : String) : boolean<br>+validateToken(token : String) : boolean +getUserFromToken(token : String) : SystemUser<br>+getUserFromToken(token : String) : SystemUser<br>SystemUser<br>-email : String<br>-passwordHash : String<br>-isActive : boolean Role Permission<br>-createdAt : LocalDateTime has -role -name : String has -permissions -name : String<br>-lastConnection : LocalDateTime-employee : Employee 1 -description : String-permissions : Permission[] * -resourceCode : String-action : String<br>-role : Role +addPermission(permission : Permission) : boolean +checkMatch(resource : String, action : String) : boolean<br>+verifyActive() : boolean +hasPermission(resource : String, action : String) : boolean<br>+addRole(role : Role) : boolean<br>+hasPermission(resource : String, action : String) : boolean<br>Powered By�Visual Paradigm Community Edition<br><!-- End of picture text -->



Figure 2.4 BOPADIGITAL Auth Module Class Diagram 



<!-- Start of picture text -->
CoreUsers<br>Visit<br>Executive ImmediateSupervisor<br>(CRM)<br>-managementRegion : String -salesZone : String<br>-objectives : SalesObjective[] -subordinates : SalesAdvisor[]<br>+defineStrategicObjetctive(objective : SalesObjective) : void +addAdvisorToTeam(advisor : SalesAdvisor) : void OfferMatrix<br>+managesZone(zone : String) : boolean +reviewOfferMatrix(matrix : OfferMatrix, isApproved : boolean, reason : String) : void (OfferMatrices)<br>+generateReport(facade : ReportFacade, filter : ReportFilter) : CommercialPerformanceReport +assignClientToAdvisor(client : BusinessClient, advisor : SalesAdvisor) : void<br>+exportReportToPdf(report : Report) : void +deactivateClient(client : BusinessClient) : void<br>+getPendingMatrices() : List<OfferMatrix><br>-manager 1 +approveMatrix(matrix : OfferMatrix) : void BusinessClient<br>+rejectMatrix(matrix : OfferMatrix, reason : String) : void<br>defines +reviewVisit(visit : Visit, comments : String) : void -supervisors (CRM)<br>* -objectives ReportFacade (Reports) +getSubordinates() : List<SalesAdvisor> * has<br>SalesObjective *<br>(Reports) -subordinates GPSCoordinates<br>SalesAdvisor (CRM)<br>-commissionRate : double<br>-salesZone : String VisitType<br>-monthlySalesTarget : BigDecimal (CRM)<br>Employee -accumulativeSales : BigDecimal<br>SystemUser 1 has -employee -employeeCode : String -totalSalesMonth : int<br>(Auth) -credentials 1 -firstName : String -currentMonthBilling : BigDecimal<br>-secondName : String -createdMatrices : OfferMatrix[]<br>-lastName : String -supervisors : ImmediateSupervisor[]<br>-secondLastName : String -clients : BusinessClient[]<br>-credentials : SystemUser -negotiationHistory : Negotiation[]<br>+getFullName() : String -visitHistory : Visit[]<br>+getEmail() : String +createOffer(negotiation : Negotiation) : OfferMatrix<br>+registerClient(rucValue : String, businessName : String, contactName : String) : BusinessClient<br>+addClient(client : BusinessClient) : void<br>+removeClient(client : BusinessClient) : void<br>+registerVisitResult(visit : Visit, gps : GPSCoordinates, observations : String) : void<br>+advanceNegotiation(negotiation : Negotiation) : void<br>WebAdministrator +getClientVisitHistory(client : BusinessClient) : List<Visit><br>+createCatalogItem(facade : CMSFacade, categoryName : String, item : CatalogItem) : boolean +startNegotiation(client : BusinessClient) : Negotiation<br>+editCompanyContent(facade : CMSFacade, key : String, newContent : String) : boolean +getMatricesPendingApproval() : List<OfferMatrix><br>+evaluateApplication(application : JobApplication, isApproved : boolean) : void +uploadDocumentToNegotiation(negotiation : Negotiation, file : File, docType : DocumentType) : NegotiationDocument<br>+scheduleVisit(client : BusinessClient, type : VisitType, notes : String, date : Date) : Visit<br>Negotiation<br>(CRM)<br>Coordinator<br>VacancyFacade (Employability) (ServiceCatalogCMS) CMSFacade -department : String NegotiationDocument<br>-vacancies : JobVacancy[] -serviceCatalog : Catalog +reviewDocument(document : NegotiationDocument, isApproved : boolean, reason : String) : void (Documents)<br>I f C I f +authorizeServiceActivation(negotiation : Negotiation) : void<br>+downloadDocument(document : NegotiationDocument) : File<br>Powered By�Visual Paradigm Community Edition<br><!-- End of picture text -->



Figure 2.5 BOPADIGITAL CoreUsers Module Class Diagram 



<!-- Start of picture text -->
CRM<br>BusinessClient<br>-activeServicesCount : int<br>-currentMonthlyBilling : BigDecimal OfferMatrix<br>-isActive : boolean (OfferMatrices) DocumentType<br>-address : String-contactName : String-contactPhone : String has -ruc -value : String+isValid() : boolean RUC -matrices * has -mandatoryDocuments -name : String-description : String(Documents)<br>-contactEmail : String-seller : SalesAdvisor 1 +RUC(value : String) has * -isMandatory : boolean<br>-visitLog : Visit[] 1 -negotiation -type 1<br>-ruc : RUC has<br>-negotiationHistory : Negotiation[]-businessName : String 1 -negotiationHistory -startDate : Date Negotiation<br>+deactivate() : void -client has * -estimatedClosedDate : Date-observations : String NegotiationDocument<br>+assignToAdvisor(advisor : SalesAdvisor) : void+unassignAdvisor() : void+addVisitToLog(visit : Visit) : void -isActive : boolean-client : BusinessClient-advisor : SalesAdvisor -negotiation1 has -documents* (Documents)<br>+addNegotiation(negotiation : Negotiation) : void -state : NegotiationState CanceledState<br>+isActive() : boolean+searchCatalog(catalog : Catalog, keyword : String) : List<CatalogComponent>+filterServices(catalog : Catalog, criteria : CatalogFilterCriteria) : List<CatalogComponent> -visits : Visit[]-documents : NegotiationDocument[]-matrices : OfferMatrix[] -name : String-description : String NegotiationState +handleNextStage() : void+handleCancellation() : void<br>-client 1 -clients * -mandatoryDocuments : DocumentType[] 1 has 1 #context : Negotiation PostSaleState<br>hasAssigned +changeState(newState : NegotiationState) : void+getCurrentState() : NegotiationState #context -state +handleNextStage() : void +handleCancellation() : void +handleNextStage() : void<br>1 -seller +proceedToNextState() : void +registerVisit(visit : Visit) : void<br>SalesAdvisor (CoreUsers) -advisor11 has-negotiationHistory* +cancel() : void+addVisitReport(visit : Visit) : void+addDocument(doc : NegotiationDocument) : void+addMatrix(matrix : OfferMatrix) : void +attachDocument(doc : NegotiationDocument) : void+generateOffer(matrix : OfferMatrix) : void +handleNextStage() : void ClosingState<br>-advisor +isActive() : boolean<br>+hasApprovedMatrix() : boolean ProspectingState ActiveNegotiationState<br>makes -negotiation 1 +handleNextStage() : void +handleNextStage() : void<br>DocumentUploadService VisitType<br>(Documents) has -code : String InitialContactState<br>receives -visitHistory * * -visits has 1 -name : String +handleNextStage() : void<br>-description : String<br>Visit<br>-date : Date -type<br>-visitLog -observations : String<br>* -isVerified : boolean-supervisorComment : String -latitude : double GPSCoordinates<br>-negotiation : Negotiation<br>-longitude : double<br>-verifiedBy : ImmediateSupervisor<br>-advisor : SalesAdvisor -coordinates -accuracy : double<br>-timestamp : Date<br>-type : VisitType-coordinates : GPSCoordinates has 1 +getMapsLink() : String<br>-client : BusinessClient +GPSCoordinates(latitude : double, longitude : double, accuracy : double)<br>+calculateDistance(targetLat : double, targetLon : double) : double<br>+markAsRejected(supervisor : ImmediateSupervisor, reason : String) : void -verifiedBy<br>+calculateDistanceToClientOffice() : double<br>+registerCheckIn(gps : GPSCoordinates, observations : String) : void 1 ImmediateSupervisor<br>+markAsVerified(supervisor : ImmediateSupervisor, comment : String) : void supervises (CoreUsers)<br>+isVerified() : boolean<br>Powered By�Visual Paradigm Community Edition<br><!-- End of picture text -->



Figure 2.6 BOPADIGITAL CRM Module Class Diagram 



<!-- Start of picture text -->
Documents<br>S3EmcryptedStorage BaseDocument DocumentNegotiationState RejectedState<br>+uploadFile(file : File, destinationFolder : String) : String -filename : String -name : String<br>+downloadFile(storagePath : String) : File -fileExtension : String -description : String<br>-extractFilename(path : String) : String -fileSizeMb : double #context : NegotiationDocument AcceptedState<br>-storagePath : String<br>-uploadDate : LocalDateTime +approve(coordinator : Coordinator) : void<br><<Interface>> -mimeType : String +replaceFile(newFilePath : String, newSize : double) : void PendingApprovalState Coordinator<br>FileStorageService -extractExtension(name : String) : String +reject(coordinator : Coordinator, reason : String) : void (CoreUsers)<br>+downloadFile(storagePath : String) : File+uploadFile(file : File, destinationFolder : String) : String +getAllowedExtensions() : String[] +validateFormat() : void -state 1 -reviewedBy 1<br>-storageService 1 +updateFileInfo(newFilePath : String, newSize : double) : void#setFilename(filename : String) : void 1 #contexthas reviews<br>#setStoragePath(path : String) : void<br>has NegotiationDocument<br>-reviewDate : Date<br>-coordinatorMessage : String<br>DocumentUploadService -negotiation : Negotiation<br>-storageService : FileStorageService CandidateResume MatrixAttachment -type : DocumentType<br>-instance : DocumentUploadService -candidate : SalesAdvisorCandidate -description : String -state : DocumentNegotiationState<br>-documentFactory : DocumentFactory +getAllowedExtensions() : String[] -matrix : OfferMatrix -reviewedBy : Coordinator<br>-DocumentUploadService() +getAllowedExtensions() : String[] +changeState(newState : DocumentNegotiationState) : void<br>+uploadFile(file : File, destinationFolder : String) : BaseDocument +approveDocument(coordinator : Coordinator) : void<br>+setFactory(factory : DocumentFactory) : void +rejectDocument(coordinator : Coordinator, reason : String) : void<br>has -instance 1 +reuploadFile(newPath : String, newSize : double) : void<br>has DocumentConfig +NegotiationDocument(negotiation : Negotiation, type : DocumentType, filename : String, storagePath : String)<br>+withMandatory(isMandatory : boolean) : DocumentConfig +getRecipientEmail() : String<br>1 -documentFactory +withCoordinatorMessage(message : String) : DocumentConfig +getNotificationMessage() : String<br>DocumentFactory +withDocumentType(type : DocumentType) : DocumentConfig +getNotificationTitle() : String<br>+createDocument(config : DocumentConfig) : BaseDocument +withMimeType(mimeType : String) : DocumentConfig +getAllowedExtensions() : String[]<br>+processDocument(config : DocumentConfig) : BaseDocument +withDescription(description : String) : DocumentConfig<br>+DocumentConfig(filename : String, storagePath : String)<br>+withReviewDate(reviewDate : Date) : DocumentConfig<br>+withNegotiation(negotiation : Negotiation) : DocumentConfig ObserverPattern<br>CandidateResumeFactory NegotiationDocumentFactory has<br>has<br><<Interface>><br>MatrixAttachmentFactory 1 -type 1 -type NotifiableEntity (Employability) Publisher<br>DocumentType (Employability) -subscribers : Subscriber[]<br>-name : String +getRecipientEmail() : String<br>-description : String +getNotificationMessage() : String +subscribe(observer : Subscriber) : void<br>-isMandatory : boolean +getNotificationTitle() : String +unsubscribe(observer : Subscriber) : void<br>+notifySubscribers() : void<br>+Publisher()<br>Powered By�Visual Paradigm Community Edition<br><!-- End of picture text -->



Figure 2.7 BOPADIGITAL Documents Module Class Diagram 



<!-- Start of picture text -->
Employability<br>JobApplication InternNotificationService<br>JobVacancy<br>-title : String-description : String-requirements : String[]-publicatioDate : LocalDateTime-closingDate : LocalDateTime 1vacancyhas applications* -applicationDate : LocalDateTime-coverLetter : String-isReviewed : boolean-reviewNotes : String-reviewDate : String-candidate : SalesAdvisorCandidate +getRecipientEmail() : String+getNotificationMessage() : String+getNotificationTitle() : String NotifiableEntity <<Interface>> +update(context : NotifiableEntity) : void+sendPushNotification(title : String, body : String) : void<br>-requiredDocuments : String[]-isActive : boolean -currentState : ApplicationState-attachedResume : CandidateResume<br>-isPublished : boolean-applications : JobApplication[]+closeVacancy() : void+isActive() : boolean -vacancy : JobVacancy+changeState(newState : ApplicationState) : void+submit() : void+evaluateApplication(isApproved : boolean) : void -subscribers : Subscriber[]+subscribe(observer : Subscriber) : void Publisher -subscribershas * +update(context : NotifiableEntity) : void <<Interface>> Subscriber<br>+isExpired() : boolean +JobApplication(candidate : SalesAdvisorCandidate, vacancy : JobVacancy) +unsubscribe(observer : Subscriber) : void<br>+isPublished() : boolean +attachResume(resume : CandidateResume) : void +notifySubscribers() : void<br>+updateVacancy(title : String, closingDate : LocalDateTime) : boolean+addApplication(application : JobApplication) : void hasAttached +getRecipientEmail() : String+getNotificationMessage() : String +Publisher() EmailService<br>-vacancies * +getNotificationTitle() : String-applications * #context 1 +update(context : NotifiableEntity) : void+sendEmail(to : String, subject : String, body : String) : void<br>manages<br>apply has<br>1 -attachedResume 1<br>VacancyFacade ApplicationState<br>-vacancies : JobVacancy[]+getActiveVacancies() : List<JobVacancy>+createJobVacancy(vacancy : JobVacancy) : boolean CandidateResume * (Documents) SalesAdvisorCandidate 1 -candidate -currentState -name : String-description : String#context : JobApplication<br>+updateJobVacancy(vacancy : JobVacancy) : boolean -resumeHistory -name : String +submitApplication() : void<br>+deleteJobVacancy(vacancy : JobVacancy) : boolean -lastname : String +evaluate(isApproved : boolean) : void<br>+publishJobVacancy(vacancy : JobVacancy) : boolean -email : String<br>+unpublishJobVacancy(vacancy : JobVacancy) : boolean -phone : String<br>-address : String<br>-applicationCount : int<br>has -applications : JobApplication[]<br>-resumeHistory : CandidateResume[]<br>-candidate +getApplications() : JobApplication[]<br>1 +getLatestResume() : CandidateResume+applyToVacancy(vacancy : JobVacancy, resumeFile : File) : JobApplication DraftState PendingState AcceptedState RejectedState<br>DocumentUploadService +uploadResume(file : File) : CandidateResume<br>(Documents) +viewActiveVacancies(facade : VacancyFacade) : List<JobVacancy><br>Powered By�Visual Paradigm Community Edition<br><!-- End of picture text -->



Figure 2.8 BOPADIGITAL Employability Module Class Diagram 

|OfferMatrices|
|---|
|lltttlMtiVl  BiDil litCtBilli  BiDil iCt  BiDil  BiDil<br>**StandardSubsidyStrategy**|
|+cacuae(oaarxaue : gecma, cenurrenng : gecma, servceoun : gecma) : gecma|
|<<Interface>><br>**SubsidyCalculationStrategy**<br>-calculateBillingFactor(billing : BigDecimal) : BigDecimal<br>-calculateServiceFactor(services : BigDecimal) : BigDecimal<br>**SalesAdvisor**<br>(CoreUsers)<br>-creator<br>1|
|_+calculate(totalMatrixValue : BigDecimal, clientCurrentBilling : BigDecimal, serviceCount : BigDecimal) : BigDecimal_<br>creates|
|<br>**_MatrixState_**<br>**DocumentUploadService**<br>(Documents)<br>-subsidyStrategy<br>1<br>-createdMatrices<br>*<br>has|
|-name : String<br> <br>|
|<br>**OfferMatrix**<br>-description : String<br>OffMi<br>-state<br>1<br>has|
|-creationDate : Date<br>#context : eratrx<br>**MatrixAttachment**<br>#context<br>1|
|-observations : String<br>-totalAmount : BigDecimal<br> <br>+editDetails() : void<br>+sendForApproval() : void<br> <br>(Documents)|
|-calculatedSubsidy : BigDecimal<br>-isApproved : boolean<br> <br>+approve(supervisor : ImmediateSupervisor) : void<br>+reject(supervisor : ImmediateSupervisor, reason : String) : void<br>-attachments<br>*|
|-approvalDate : Date<br>-supervisorMessage : String<br><br>-matrix<br>1<br>has|
|-negotiation : Negotiation<br>**DraftMatrixState**<br><br> <br>**RejectedMatrixState**<br><br>|
|-state : MatrixState<br>+editDetails() : void<br>**ApprovedMatrixState**<br>+editDetails() : void<br><<Interface>><br>|
|-subsidyStrategy : SubsidyCalculationStrategy<br> <br> <br>**NotifiableEntity**|
|<br>-items : MatrixLineItem[]<br>+sendForApproval() : void<br> <br>(Employability)|
|-approvedBy : ImmediateSupervisor<br>**PendingApprovalState**<br>_+getRecipientEmail() : String_<br>|
|-creator : SalesAdvisor<br><br>_+getNotificationMessage() : String_|
|<br>-attachments : MatrixAttachment[]<br> <br>+approve(supervisor : ImmediateSupervisor) : void<br>+reject(supervisor : ImmediateSupervisor, reason : String) : void<br> <br>_+getNotificationTitle() : String_|
|+changeState(newState : MatrixState) : void<br>+getCurrentState() : MatrixState<br>**_Publisher_**<br><br><br>*<br>has|
|+sendToSupervisor() : void<br>**MatrixLineItem**<br>(Employability)<br>1<br>|
|+approve(supervisor : ImmediateSupervisor) : void<br>-quantity : int<br>-subscribers : Subscriber[]<br>-matrix<br>-items|
|+reject(supervisor : ImmediateSupervisor, reason : String) : void<br> <br>-unitPrice : BigDecimal<br> <br>+subscribe(observer : Subscriber) : void<br>|
|+recalculateTotals() : void<br> <br>-total : BigDecimal<br> <br>+unsubscribe(observer : Subscriber) : void|
|+addAttachment(attachment : MatrixAttachment) : void<br> <br>-matrix : OfferMatrix<br>|
|+OfferMatrix(negotiation : Negotiation, creator : SalesAdvisor)<br> <br>-item : CatalogItem|
|+addItem(catalogItem : CatalogItem, quantity : int, customPrice : BigDecimal) : boolean<br>+calculateTotal() : BigDecimal|
|+saveDraft(observations : String) : void<br> <br> <br>+MatrixLineItem(matrix : OfferMatrix, item : CatalogItem, quantity : int, customPrice : BigDecimal)|
|+hasItems() : boolean|
|+getRecipientEmail() : String<br>+getNotificationMessage() : String<br> <br>**ImmediateSupervisor**<br>(CoreUsers)<br>-item<br>1<br>1<br>has|
|+getNotificationTitle() : String<br>i|
|**CatalogItem**<br>(ServiceCatalogCMS)<br>-approvedBy<br>supervses<br>Powered ByVisual Paradigm Community Edition|



Figure 2.9 BOPADIGITAL OfferMatrices Module Class Diagram 



<!-- Start of picture text -->
Reports<br>PDFExporter<br>+export(report : Report) : File Report -generatedBy Employee<br>-generateFilename(title : String) : String -title : String generates 1 (CoreUsers)<br>-writeMetricsToPdf(file : File, metrics : List<PerformanceMetric>) : void -generationDate : LocalDateTime<br>-exporter : ReportExporter<br>1 has -generatedBy : Employee-metrics : PerformanceMetric[] -report1 has * -metrics PerformanceMetric<br>+export(report : Report) : File ExcelExporter ReportExporter <<Interface>> -exporter -visualizations : ReportChart[]+addMetric(metric : PerformanceMetric) : void -metricName : String-value : double<br>+export(report : Report) : File +operation() : void -unit : String<br>+Report(generatedBy : Employee, title : String) -report : Report<br>+addVisualization(chart : ReportChart) : void +validateData() : boolean<br>+getMetrics() : List<PerformanceMetric> +PerformanceMetric(metricName : String, value : double, unit : String)<br>+exportData(exporter : ReportExporter) : File<br>+setExporter(exporter : ReportExporter) : void<br>+getTitle() : String -report has -visualizations ReportChart<br>+getGenerationDate() : LocalDateTime+getGeneratedBy() 1 * -title : String<br>-description : String<br>-labels : String[]<br>OperationalReport -values : double[]<br>CommercialPerformanceReport<br>-benchmarkObjective : SalesObjective -report : Report<br>AdvisorDashboard -analyzedAdvisors : SalesAdvisor[] -type : ChartType<br>+OperationalReport(supervisor : ImmediateSupervisor) -marketInsights : List<String><br>has +addMarketInsight(insight : String) : void +addDataPoint(label : String, value : double) : void<br>has +CommercialPerformanceReport(manager : Executive)<br>1 -benchmarkObjective has +addAnalyzedAdvisor(advisor : SalesAdvisor) : void+getAnalyzedAdvisors() : List<SalesAdvisor> has<br>-targetSalesAmount : BigDecimal SalesObjective 1 SalesAdvisor -advisor * -analyzedAdvisors Executive ChartType 1 -type<br>-targetClosedDeals : int (CoreUsers) (CoreUsers) -name : String<br>-periodStart : Date -description : String<br>-periodEnd : Date<br>-manager : Executive<br>+calculateSalesCompletionPercentage(actualValue : BigDecimal) : BigDecimal ReportFilter<br>ReportFacade -startDate : Date<br>+generateManagerReport(manager : Executive, filter : ReportFilter) : CommercialPerformanceReport -endDate : Date<br>+generateSupervisorReport(supervisor : ImmediateSupervisor, filter : ReportFilter) : OperationalReport -zone : String<br>-serviceType : Category<br>+validateDates() : boolean<br>Category 1 has +ReportFilter(startDate : Date, endDate : Date)<br>+matchesDate(dateToCheck : Date) : boolean<br>(ServiceCatalogCMS) -serviceType +withZone(zone : String) : ReportFilter<br>+withServiceType(type : Category) : ReportFilter<br>Powered By�Visual Paradigm Community Edition<br><!-- End of picture text -->



Figure 2.10 BOPADIGITAL Reports Module Class Diagram 



<!-- Start of picture text -->
ServiceCatalogCMS<br>Category<br>-children : CatalogComponent[]<br>Catalog -categories CatalogComponent +add(component : CatalogComponent) : boolean<br>-categories : CatalogComponent[]+filter(criteria : CatalogFilterCriteria) : List<CatalogComponent> has * -name : String-description : String +remove(component : CatalogComponent) : boolean+getItems() : List<CatalogComponent><br>+search(keyword : String) : List<CatalogComponent>+addItem(component : CatalogComponent) : boolean +getDetails() : String +getPrice() : BigDecimal * owns +Category()+search(keyword : String) : List<CatalogComponent><br>+removeItem(component : CatalogComponent) : boolean +search(keyword : String) : List<CatalogComponent> -children +filter(criteria : CatalogFilterCriteria) : List<CatalogComponent><br>+getCategory(categoryName : String) : CatalogComponent +filter(criteria : CatalogFilterCriteria) : List<CatalogComponent> +getPrice() : BigDecimal<br>+Catalog()<br>+getAllCategories() : List<CatalogComponent> has<br>1 -serviceCatalog<br>CatalogFilterCriteria CatalogItem * -benefits<br>-searchTerm : String -price : BigDecimal -conditions<br><<Interface>> <<Interface>><br>-minPrice : BigDecimal-maxPrice : BigDecimal -conditions : Condition[]-benefits : Benefit[] has * Condition Benefit<br>-coverage : String +isMatch(criteria : CatalogFilterCriteria) : boolean +getDetails() : void +getDetails() : void<br>-categoryName : String +filter(criteria : CatalogFilterCriteria) : List<CatalogComponent><br>+CatalogFilterCriteria() +addCondition(condition) : void<br>manages +withSearchTerm(term : String) : CatalogFilterCriteria +addBenefit(benefit) : void<br>+withPriceRange(min : BigDecimal, max : BigDecimal) : CatalogFilterCriteria<br>+withCategory(category : String) : CatalogFilterCriteria<br>ElectiveBenefit<br>LegalCondition<br>+getDetails() : void<br>+getDetails() : void<br>VoiceService ConectivityService DigitalService TemporalBenefit<br>-gigasTotal : int -bandWidth : double -provider : String AgeCondition +getDetails() : void<br>-minutes : int +getDetails() : void<br>-sms : int<br>CMSFacade<br>-serviceCatalog : Catalog<br>-companyInfo : CompanyInfo CompanyInfo ContentBlock<br>+updateCatalogComponent(item : CatalogComponent) : boolean -contents : ContentBlock[] -key : String ContentType<br>+deleteCatalogComponent(item : CatalogComponent) : boolean+editWebsiteContent(content : ContentBlock) : boolean+editCompanyInfo(key : String, content : String) : boolean -companyInfo +getMission() : ContentBlock+getVision() : ContentBlock -contents -content : String-type : ContentType has -type1 -code : String-name : String<br>+CMSFacade() manages 1 +getHistory() : ContentBlock+getValues() : ContentBlock has * +updateContent(newContent : String) : boolean+ContentBlock(key : String, type : ContentType) -description : String<br>+addRootCategory(category : Category) : boolean<br>+CompanyInfo()<br>+addItemToCategory(categoryName : String, item : CatalogItem) : boolean<br>-findByKey(key : String) : ContentBlock<br>+browseCategories() : List<CatalogComponent><br>+updateInfo(key : String, content : String) : void<br>+filterServices(criteria : CatalogFilterCriteria) : List<CatalogComponent><br>Powered By�Visual Paradigm Community Edition<br><!-- End of picture text -->



Figure 2.11 BOPADIGITAL ServiceCatalogCMS Module Class Diagram 

102 

**2.4 Object Diagrams** 



<!-- Start of picture text -->
1_CRM<br>ruc1 : RUC<br>advisor1 : SalesAdvisor client1 : BusinessClient<br>value = 0991234567001<br>employeeCode = SA-2024-011 businessName = TechSolutions S.A.<br>firstName = Juan contactName = Carlos Mendoza<br>lastName = Perez contactPhone = 0991234567<br>salesZone = Guayaquil Norte contactEmail = cmendoza@espol.edu.ec<br>commissionRate = 0.05 address = Av. Francisco de Orellana<br>thl S l T t 15000 00 isActive = true<br>activeServicesCount = 0<br>visit1 : Visit<br>date = 2025-10-10<br>observations = Primera visita - presentacion de servicios<br>isVerified = true<br>supervisorComment = Visita verificada correctamente<br>gps1 : GPSCoordinates<br>latitude = -2.1894<br>longitude = -79.8891<br>accuracy = 5.0<br>timestamp = 2025-10-10 10:30:00<br>activeStatus : ActiveNegotiationState<br>neg1 : Negotiation<br>name = ACTIVE<br>startDate = 2025-10-10<br>estimatedClosedDate = 2025-12-15<br>observations = Cliente interesado en plan corporativo<br>isActive = true<br>Powered By�Visual Paradigm Community Edition<br><!-- End of picture text -->



Figure 2.12 BOPADIGITAL CRM Object Diagram Overview 

2_OfferMatrix 



<!-- Start of picture text -->
strategy1 : StandardSubsidyStrategy<br>service2 : CatalogItem item2 : MatrixLineItem matrix1 : OfferMatrix advisor1 : SalesAdvisor<br>name = Internet Fibra 100Mbps quantity = 2 creationDate = 2025-01-15<br>description = Fibra optica empresarial unitPrice = 125.00 observations = Oferta plan corporativo employeeCode = SA-2024-011firstName = Juan<br>price = 125.00 total = 250.00 totalAmount = 850.00 lastName = Perez<br>calculatedSubsidy = 85.00<br>salesZone = Guayaquil Norte<br>isApproved = false commissionRate = 0.05<br>service1 : CatalogItem item1 : MatrixLineItem approvalDate = null thl S l T t 15000 00<br>name = Plan Voz Corporativo 500 quantity = 5<br>description = 500 min nacionales unitPrice = 120.00<br>price = 120.00 total = 600.00<br>neg1 : Negotiation<br>pendingStatus : PendingApprovalState<br>startDate = 2025-10-10<br>name = PENDING<br>estimatedClosedDate = 2025-12-15<br>observations = Cliente interesado en plan corporativo<br>isActive = true<br>Powered By�Visual Paradigm Community Edition<br><!-- End of picture text -->



Figure 2.13 BOPADIGITAL OfferMatrix Object Diagram Overview 



<!-- Start of picture text -->
3_Catalog<br>catalog1 : Catalog<br>voiceCat : Category internetCat : Category digitalCat : Category<br>name = Servicios de Voz name = Conectividad name = Servicios Digitales<br>description = Planes de telefonía móvil description = Internet y fibra óptica description = Apps y plataformas<br>voicePlan1 : VoiceService voicePlan2 : VoiceService<br>conectivity1 : ConectivityService conectivity2 : ConectivityService digital1 : DigitalService<br>name = Plan Voz 500 name = Plan Voz 1000<br>description = 500 min nacionales description = 1000 min + roaming name = Fibra 100mbps name = Fibra 300mbps name = Cloud Storage 1 TB<br>price = 25.00 price = 45.00 description = Internet Empresarial description = Alta velocidad description = Almacenamiento nube<br>minutes = 500 minutes = 1000 price = 89.00 price = 129.00 price = 15.00<br>sms = 100 sms = 100 bandWidth = 100.00 bandWidth = 300.0 provider = Movistar Cloud<br>gigasTotal = 5 gigasTotal = 5<br>3FreeMonths : TemporalBenefit includedRouter : ElectiveBenefit<br>Powered By�Visual Paradigm Community Edition<br><!-- End of picture text -->



Figure 2.14 BOPADIGITAL Catalog Object Diagram Overview 



<!-- Start of picture text -->
4_Auth<br>users : hasher :<br>PostgresUserRepository BcryptHasher<br>authService : tokenService :<br>AuthService JwtTokenService<br>perm1 : Permission<br>name = Gestionar clientes<br>action = manage<br>user1 : SystemUser resourceCode = clients<br>email = jperez@bopacorp.ec advisorRole : Role<br>passwordHash = $2a$10$N9qo8uLO...<br>name = SALES_ADVISOR<br>isActive = true perm2 : Permission<br>description = Asesor Comercial de Bopacorp<br>createdAt = 2024-06-15 08:00:00<br>lastConnection = 2025-12-15 09:30:00 name = Crear negociaciones<br>action = create<br>resourceCode = negotiations<br>perm3 : Permission<br>advisor1 : SalesAdvisor<br>name = Registrar Visitas<br>employeeCode = SA-2024-011 action = create<br>firstName = Juan<br>resourceCode = visits<br>lastName = Perez<br>salesZone = Guayaquil Norte<br>commissionRate = 0.05<br>monthlySalesTarget = 15000.00<br>Powered By�Visual Paradigm Community Edition<br><!-- End of picture text -->



Figure 2.15 BOPADIGITAL Auth Object Diagram Overview 

5_Documents 



<!-- Start of picture text -->
advisor1 : SalesAdvisor<br>neg1 : Negotiation<br>employeeCode = SA-2024-011<br>firstName = Juan startDate = 2025-10-10<br>lastName = Perez estimatedClosedDate = 2025-12-15 config1 : DocumentConfig<br>salesZone = Guayaquil Norte observations = Cliente interesado en plan corporativo<br>commissionRate = 0.05 isActive = true filename = contrato_empresarial.pdf<br>storagePath = s3://bopa-docs/neg-2025-001/<br>monthlySalesTarget = 15000.00<br>mimeType = application/pdf<br>isMandatory = true<br>description = contrato de servicios<br>coord1 : Coordinator doc1 : NegotiationDocument<br>employeeCode = CORD-001 filename = contrato_empresarial.pdf<br>firstName = Maria fileExtension = pdf<br>lastName = González fileSizeMb = 1.8<br>department = Documentacion storagePath = s3://bopa-docs/neg-2025-001/<br>uploadDate = 2025-01-15 10:30:00<br>reviewDate = null<br>coordinatorMessage = null<br>factory1 :<br>NegotiationDocumentFactory<br>rejectedState : pendingState : acceptedState :<br>RejectedState PendingApprovalState AcceptedState<br>Powered By�Visual Paradigm Community Edition<br><!-- End of picture text -->



Figure 2.16 BOPADIGITAL Documents Object Diagram Overview 

108 

**2.5 Components Diagram** 



110 

**2.6 Deployment Diagram** 



<!-- Start of picture text -->
<<component>><br>Client Layer<br>Web Browser Mobile App<br>(iOS/Android)<br>HTTPS HTTPS<br><<component>><br>DMZ<br>Load Balancer<br>nginx<br>Firewall<br><<component>> <<artifact>><br>Application Server External Services<br><<artifact>> Web Server Carrier API Activation<br>Database Server (Apache/nginx) Service<br>API Calls<br>Database Postgres SQL / MySQL SQL<br>Notifications SMTP (Email Services)<br>Application Server<br>Cache (Node.js/Java)<br>Cache Redils<br><<artifact>><br>CMS Module <<artifact>> <<artifact>><br>Reporting Module Search Engine <<component>><br>File Storage<br><<artifact>> <<artifact>> Store/Retrieve File Server<br>CRM Module Document Management Document Storage<br>Powered By�Visual Paradigm Community Edition<br><!-- End of picture text -->

Figure 2.18 BOPADIGITAL Deployment Diagram 

**CHAPTER 3 SYSTEM BEHAVIORAL MODELING** 

113 

###### **3.1 Activity Diagrams** 



<!-- Start of picture text -->
act [1_NegotiationLifeCycle]<br>Negotiation<br>Register Client<br>[no]<br>Valid RUC?<br>[yes]<br>Assign client to advisor<br>Create Negotiation<br>Set state: Prospecting<br>Schedule and make visit<br>Registrate check-in GPS<br>[yes]<br>[no]<br>Visit was verified by supervisor?<br>Advance Status Repeat Visit<br>[no] Cancel negotiation?<br>[yes]<br>Set state: Canceled<br>[yes]<br>State !- PostSale?<br>[no]<br>State: PostSale<br>Negotiation Completed<br>Powered By�Visual Paradigm Community Edition<br><!-- End of picture text -->



Figure 3.1 BOPADIGITAL Activity Diagram – Negotiation Life Cycle 

114 



<!-- Start of picture text -->
act [2_OfferMatrices]<br>Create Offer Matrix<br>Set State: Draft<br>Add line items (services from catalog)<br>Calculate Subsidy<br>[yes]<br>Save draft<br>More items?<br>[no]<br>[no]<br>Has items?<br>[yes]<br>Send for approval<br>Set state: PendingApproval<br>Supervisor reviews matrix<br>[yes] [no]<br>Approved?<br>Set state: Approved Set state: Rejected<br>Notify Advisor Notify advisor with reason<br>[no] [yes]<br>Powered By�Visual Paradigm Community EditionEdit and retry?<br><!-- End of picture text -->



Figure 3.2 BOPADIGITAL Activity Diagram – Offer Matrices 



<!-- Start of picture text -->
Po)<br>’<br>\<br>v<br>y<br>V V<br>Co) Co)<br>v<br>Co)<br><!-- End of picture text -->





<!-- Start of picture text -->
|)<br>—<br>cD<br>——_} ep<br>— é<br>—<br>c> a<br>= ep<br>=<br><!-- End of picture text -->





<!-- Start of picture text -->
Po<br>=<br>Process \<br>a<br>v<br>Cc) By Visual Paradigm Community Edition ><br><!-- End of picture text -->



118 

**3.2 Sequence Diagrams** 



<!-- Start of picture text -->
|||<br>| | |<br>|||<br>|||<br>||<br>!||<br>||<br>||<br>'|<br>|<br>Sn |<br>|<br>| |<br>||<br>||<br>||<br>||<br>||<br>||<br>TT TT | |<br>| |<br>|||<br>|||<br>||<br>||<br>||<br>€---------------- | |<br>| |<br>|||<br>|||<br>|<br>|<br>|<br>|<br>|<br>| ||<br>|<br>|<br>1|<br>II|<br>|| |<br>@< ---------- | | |<br>| | |<br>||||<br>1<br>I | Powered By Visual Paradigm Comntunity Edition<br><!-- End of picture text -->



<!-- Start of picture text -->
sd [11_reviewVisit]<br>: ImmediateSupervisor visit : Visit coordinates : GPSCoordinates<br>1: reviewVisit(visit : Visit, comments : String) : void<br>1.1: calculateDistanceToClientOffice() : double<br>1.1.1: getLatitude() : double<br>1.1.2: visitLat<br>1.1.3: getLongitude() : double<br>1.1.4: visitLon<br>1.1.5: calculateDistance(targetLat : double = visitLat, targetLon : double = visitLon) : double<br>1.1.6: distance<br>1.2: distance<br>alt<br>[distance <= maxAllowedDistance]<br>1.3: markAsVerified(supervisor : ImmediateSupervisor = this, comment : String = comments) : void<br>1.4:<br>[else]<br>1.5: markAsRejected(supervisor : ImmediateSupervisor = this, reason : String = comments) : void<br>1.6:<br>1.7:<br>Powered By�Visual Paradigm Community Edition<br><!-- End of picture text -->



Figure 3.7 BOPADIGITAL Sequence Diagram - reviewVisit 



<!-- Start of picture text -->
sd [12_updateNegotiationStatus]<br>: SalesAdvisor negotiation : Negotiation currentState : ActiveNegotiationState<br>1: advanceNegotiation(negotiation : Negotiation) : void<br>1.1: proceedToNextState() : void<br>1.1.1: handleNextStage() : void 2: getContext() : Negotiation<br>1.1.1.1: negotiation<br>1.1.1.2: hasApprovedMatrix() : boolean<br>1.1.1.3: hasApproved<br>opt<br>[hasApproved]<br>1.1.1.4: <<create>> newtState : ClosingState<br>1.1.1.4: changeState(newState : NegotiationState) : void<br>1.1.1.5:<br>1.1.1.6:<br>1.1.1.6.1:<br>1.1.1.6.1.1:<br>Powered By�Visual Paradigm Community Edition<br><!-- End of picture text -->



Figure 3.8 BOPADIGITAL Sequence Diagram - updateNegotiationStatus 



<!-- Start of picture text -->
I|<br>| |<br>||<br>||<br>|<br>1|<br>I<br>|<br>ee |<br>|<br>II<br>I<br>i1 ||<br>| |<br>I I<br>|<br>|<br>7, ! | |!<br>| | |<br>II | II<br>a | I<br>I | |<br>| | |<br>, |<br>|<br>I<br>I<br>|<br>[ |<br>|<br>I<br>LT<br>| | |<br>| | |<br>| | |<br>@<--------- I| | |<br>|<br>| | Powered!ByI Visual Paradigm Community Edition<br><!-- End of picture text -->



<!-- Start of picture text -->
||<br>| |<br>||<br>||<br>||<br>|<br>|<br>|<br>4|||<br>||<br>| |<br>=, | |<br>||<br>||<br>|<br>|<br>|<br>|<br>|<br>le! ||<br>|<br>a |<br>| |<br><|I<br>|<br>|<br>le! ||<br>|<br>|<br>| <amII|<br>|<br>|<br>|<br>|<br>oH |<br>|<br>||<br>||<br>||<br>I|<br>|<br>4|<br>| |<br>||<br>||<br>|<br>||<br>@<------------ |||<br>| | Powered By Visual Paradigm ¢ommunity Edition<br><!-- End of picture text -->



<!-- Start of picture text -->
|||<br>| | |<br>|||<br>|| |<br>| | |<br>-ou-- LL} | |I |<br>|| |<br>|||<br>T|I|||<br>|<br>| |I |<br>||<br>. | |<br>|T|<br>|| |<br>|||<br>|| |<br>||<br>||<br>||<br>|| as<br>||<br>|| |<br>| | |<br>Qt bn nbn nn nnn nnn nnn<br>| | |<br>||I|<br>@<--------- || | | |<br>| || || I| Powered By Visual Paradigm Community| Edition<br><!-- End of picture text -->



<!-- Start of picture text -->
I<br>I<br>I<br>I<br>|<br>aaaaanna |I<br>|<br>I<br>|<br>| 0<br>a, II<br>|<br>I<br>I<br>¢ |I<br>|<br>I<br>| |<br>I<br>|<br>bo |<br>@< ---------- | ||<br>:<br>| Powered By Visual Paradigm Community Edition<br><!-- End of picture text -->





<!-- Start of picture text -->
sd [17_recalculateTotals]<br>: OfferMatrix item : MatrixLineItem itemsTotal : BigDecimal negotiation : Negotiation client : BusinessClient subsidyStrategy : SubsidyCalculationStrategy<br>1: recalculateTotals() : void<br>loop<br>[for each this.items]<br>1.1: calculateTotal() : BigDecimal<br>1.2: itemTotal<br>1.3: add(itemTotal)<br>1.4:<br>1.5: setTotalAmount(totalAmount : BigDecimal = itemsTotal) : void<br>1.6:<br>2: getClient() : BusinessClient<br>2.1: client<br>3: getCurrentMonthlyBilling() : BigDecimal<br>3.1: clientBilling<br>4: getActiveServicesCount() : int<br>4.1: servicesCount<br>5: <<create>> servicesBD : BigDecimal<br>6: calculate(totalMatrixValue : BigDecimal = this.totalAmount, clientCurrentBilling : BigDecimal = clientBilling, serviceCount : BigDecimal = servicesBD) : BigDecimal<br>6.1: subsidy<br>7: setCalculatedSubsidy(calculatedSubsidy : BigDecimal = subsidy) : void<br>7.1:<br>8:<br>Powered By�Visual Paradigm Community Edition<br><!-- End of picture text -->



Figure 3.13 BOPADIGITAL Sequence Diagram - recalculateTotals 



<!-- Start of picture text -->
|<br>|<br>|<br>|<br>|<br>|<br>|<br>|7|<br><|<br>|<br>i<br>~]<br>< |<br>@<--------- | |||<br>| Powered By Visual Paradigm Community Edition<br><!-- End of picture text -->





<!-- Start of picture text -->
|<br>I<br>|<br>|<br>I<br>!<br>| ~I<br>I<<br>StatePattern (see Class Diagram) IN<br>|<br>|<br>|<br>|<br>— eee i<br>|<br>|<br>|<br>|<br>|<br>eee ||<br>|<br>|<br>|<br>|<br>|<br>oH |<br>@<---------- |<br>!<br>I1 |1 Powered By Visual Paradigm Community Edition<br><!-- End of picture text -->





<!-- Start of picture text -->
||||<br>| | | |<br>||||<br>| | |<br>'|||<br>|| |<br>| | |<br><a |‘||IIII<br>|||<br>||<br>a||||<br>|i i}<br>|<br>ee LEE | |I|<br>|I<br>|' |<br>SO OSG<br>I I I]<br>||||<br>|<br>@<--------- | | I| I|<br>|| | |<br>| | | ! Powered By Visual Paradigm bommunity Edition<br><!-- End of picture text -->



<!-- Start of picture text -->
sd [20_listPendingMatrices]<br>: ImmediateSupervisor advisor : SalesAdvisor matrix : OfferMatrix<br>1: getPendingMatrices() : List<OfferMatrix><br>1.1: <<create>> pendingMatrices :<br>ArrayList<OfferMatrix><br>1.2: getSubordinates() : List<SalesAdvisor><br>1.3: subordinates<br>loop<br>[for each subordinates]<br>2: getMatricesPendingApproval() : List<OfferMatrix><br>2.1: <<create>> pendingMatrices :<br>ArrayList<OfferMatrix><br>loop<br>[for each this.createdMatrices]<br>2.2: getCurrentState() : MatrixState<br>2.3: currentState<br>opt<br>[isPending]<br>2.4: add(matrix)<br>2.5:<br>2.6: advisorMatrices<br>3: addAll(advisorMatrices)<br>4: pendingMatrices<br>Powered By�Visual Paradigm Community Edition<br><!-- End of picture text -->



Figure 3.17 BOPADIGITAL Sequence Diagram - listPendingMatrices 



<!-- Start of picture text -->
sd [21_approveMatrix]<br>: ImmediateSupervisor matrix : OfferMatrix currentState : PendingApprovalState<br>1: approveMatrix(matrix : OfferMatrix) : void<br>1.1: getCurrentState() : MatrixState<br>1.2: currentState<br>1.3: approve(supervisor : ImmediateSupervisor = this) : void{}<br>1.3.1: getContext() : OfferMatrix<br>1.3.2: matrix<br>2: approve(supervisor : ImmediateSupervisor = supervisor) : void<br>2.1: <<create>> this.approvalDate : Date<br>2.2: <<create>> approvedState : ApprovedMatrixState<br>2.3: changeState(newState : MatrixState = approvedState) : void<br>2.4:<br>3: notifySubscribers() : void<br>3.1:<br>3.2:<br>1.4:<br>1.5:<br>Powered By�Visual Paradigm Community Edition<br><!-- End of picture text -->



Figure 3.18 BOPADIGITAL Sequence Diagram - approveMatrix 



<!-- Start of picture text -->
sd [22_rejectMatrix]<br>: ImmediateSupervisor matrix : OfferMatrix currentState : PendingApprovalState<br>1: rejectMatrix(matrix : OfferMatrix, reason : String) : void<br>1.1: getCurrentState() : MatrixState<br>1.2: currentState<br>1.3: reject(supervisor : ImmediateSupervisor = this, reason : String = reason) : void<br>1.3.1: getContext() : OfferMatrix<br>1.3.2: matrix<br>2: reject(supervisor : ImmediateSupervisor = supervisor, reason : String = reason) : void<br>2.1: <<create>> rejectedState : RejectedMatrixState<br>2.2: changeState(newState : MatrixState = rejectedState) : void<br>2.3:<br>3: notifySubscribers() : void<br>3.1:<br>3.2:<br>1.4:<br>1.5:<br>Powered By�Visual Paradigm Community Edition<br><!-- End of picture text -->



Figure 3.19 BOPADIGITAL Sequence Diagram - rejectMatrix 



<!-- Start of picture text -->
sd [23_uploadDocument]<br>: SalesAdvisor negotiation : Negotiation file : File<br>1: uploadDocumentToNegotiation(negotiation : Negotiation, file : File, docType : DocumentType) : NegotiationDocument<br>1.1: <<create>> storage : S3EmcryptedStorage<br>1.2: hashCode()<br>1.3: hashCode<br>1.4: uploadFile(file : File = file, destinationFolder : String = destinationFolder) : String<br>1.5: storagePath<br>1.6: getName()<br>1.7: fileName<br>1.8: <<create>> config : DocumentConfig<br>1.9: withDocumentType(type : DocumentType = docType) : DocumentConfig<br>1.10:<br>1.11: withNegotiation(negotiation : Negotiation = negotiation) : DocumentConfig<br>1.12:<br>1.13: <<create>> factory : NegotiationDocumentFactory<br>1.14: processDocument(config : DocumentConfig = config) : BaseDocument<br>1.15: doc<br>1.16: addDocument(doc : NegotiationDocument = document) : void<br>1.17:<br>Powered By�Visual Paradigm Community Edition<br><!-- End of picture text -->



Figure 3.20 BOPADIGITAL Sequence Diagram - uploadDocument 



<!-- Start of picture text -->
sd [24_approveDocument]<br>: Coordinator document : NegotiationDocument currentState : PendingApprovalState<br>1: reviewDocument(document : NegotiationDocument, isApproved : boolean, reason : String) : void<br>1.1: getState() : DocumentNegotiationState<br>alt<br>[isApproved]<br>1.2: approve(coordinator : Coordinator = this) : void<br>1.2.1: getContext() : NegotiationDocument<br>1.2.2: document<br>2: approveDocument(coordinator : Coordinator = coordinator) : void<br>2.1: <<create>> acceptedState : AcceptedState<br>2.2: changeState(newState : DocumentNegotiationState = acceptedState) : void<br>2.3:<br>2.4:<br>1.3:<br>[else] 1.4: reject(coordinator : Coordinator = this, reason : String = reason) : void<br>1.5:<br>1.6:<br>Powered By�Visual Paradigm Community Edition<br><!-- End of picture text -->



Figure 3.21 BOPADIGITAL Sequence Diagram - approveDocument 



<!-- Start of picture text -->
sd [25_rejectDocument]<br>: Coordinator document : NegotiationDocument currentState : PendingApprovalState<br>1: reviewDocument(document : NegotiationDocument, isApproved : boolean, reason : String) : void<br>1.1: getState() : DocumentNegotiationState<br>1.2: currentState<br>alt<br>[isApproved]<br>1.3: approve(coordinator : Coordinator = this) : void<br>1.4:<br>[else]<br>1.5: reject(coordinator : Coordinator = this, reason : String = reason) : void<br>1.5.1: getContext() : NegotiationDocument<br>1.5.2: document<br>2: rejectDocument(coordinator : Coordinator = coordinator, reason : String = reason) : void<br>2.1: rejectedState : RejectedState<br>2.2: changeState(newState : DocumentNegotiationState = rejectedState) : void<br>2.3:<br>3: emailService : EmailService<br>4: update(context : NotifiableEntity = this) : void<br>4.1:<br>4.2:<br>1.6:<br>1.7:<br>Powered By�Visual Paradigm Community Edition<br><!-- End of picture text -->



Figure 3.22 BOPADIGITAL Sequence Diagram - rejectDocument 



<!-- Start of picture text -->
|<br>|<br>|<br>|<br>|<br>!<br>|<br>woe eee eee -----p------------3<br>|<br>I |<br>|<br>|<br>|<br>|<br>|<br>|<br>|<br>|<br>|<br>| “I<br>| <I<br>|<br>! -------------------<br>|<br>|| as<br>|<br><r asian nnn |<br>||<br>|| |<br>@<--------- | | |<br>| |<br>|.|<br>: I Powered By Visual Paradigm Community Edition<br><!-- End of picture text -->



<!-- Start of picture text -->
||<br>|<br>CompositePattern IN |<br>(see Class Diagram) |<br>|<br>|<br>|<br>|<br>|<br>@j-----------S |<br>|<br>{ !|<br>||<br>I|<br>'|<br>Pa |||<br>| |<br>— | |<br>| I |<br><||<br>||<br>|) | |<br>!|<br>|<br>He ee<br>||<br>||<br>||<br>|<br>|<br>i|<br>||<br>||<br>| |<br>OT | |<br>I |<br>e<< — || || ||<br>|||<br>II | Powered By Visual Paradigm) Community Edition<br><!-- End of picture text -->





<!-- Start of picture text -->
sd [28_filterCatalog]<br>: BusinessClient catalog : Catalog category : CatalogComponent<br>1: filterServices(catalog : Catalog, criteria : CatalogFilterCriteria) : List<CatalogComponent><br>1.1: filter(criteria : CatalogFilterCriteria = criteria) : List<CatalogComponent><br>1.1.1: <<create>><br>results : ArrayList<CatalogComponent><br>1.1.2: getAllCategories() : List<CatalogComponent><br>1.1.3: categories<br>loop<br>[for each categories]<br>2: filter(criteria : CatalogFilterCriteria = criteria) : List<CatalogComponent><br>2.1: categoryResults<br>3: addAll(categoryResults)<br>3.1:<br>1.2: results<br>1.3: results<br>Powered By�Visual Paradigm Community Edition<br><!-- End of picture text -->



Figure 3.25 BOPADIGITAL Sequence Diagram - filterCatalog 



<!-- Start of picture text -->
sd [29_createCatalogItem]<br>: WebAdministrator facade : CMSFacade serviceCatalog : Catalog category : Category category : CatalogComponent name : String<br>1: createCatalogItem(facade : CMSFacade, categoryName : String, item : CatalogItem) : boolean<br>1.1: addItemToCategory(categoryName : String = categoryName, item : CatalogItem = item) : boolean<br>1.1.1: getCategory(categoryName : String = categoryName) : CatalogComponent<br>loop<br>[for each this.categories]<br>1.1.1.1: getName() : String<br>1.1.1.2: name<br>1.1.1.3: equals(categoryName)<br>1.1.1.4: matches<br>1.1.2: category<br>1.1.3: add(component : CatalogComponent = item) : boolean<br>1.1.4: wasAdded<br>1.2: wasAdded<br>1.3: wasAdded<br>Powered By�Visual Paradigm Community Edition<br><!-- End of picture text -->



Figure 3.26 BOPADIGITAL Sequence Diagram - createCatalogItem 



<!-- Start of picture text -->
||<br>||<br>||<br>||<br>|<br>\|<br>|<br>|<br>| |<br>||<br>||<br>a '<br>|<br>|<br>4<br>| |<br>|<br>a FG|<br>||<br>||<br>| |<br>@<--------- !<br>|||<br>I<br>| Powered By Visual Paradigm Comrhunity Edition<br><!-- End of picture text -->



<!-- Start of picture text -->
sd [30_editWebContents]<br>: WebAdministrator facade : CMSFacade companyInfo : CompanyInfo block : ContentBlock<br>1: editCompanyContent(facade : CMSFacade, key : String, newContent : String) : boolean<br>1.1: editCompanyInfo(key : String = key, content : String = newContent) : boolean<br>1.1.1: updateInfo(key : String = key, content : String = content) : void<br>1.1.1.1: findByKey(key : String = key) : ContentBlock<br>opt<br>[block != null]<br>1.1.1.2: updateContent(newContent : String = content) : boolean<br>1.1.1.3: wasUpdated<br>1.1.2:<br>1.2: wasEdited<br>1.3: wasEdited<br>Powered By�Visual Paradigm Community Edition<br><!-- End of picture text -->



Figure 3.28 BOPADIGITAL Sequence Diagram – editWebContents 



<!-- Start of picture text -->
sd [31_generateReport]<br>: Executive facade : ReportFacade filter : ReportFilter<br>1: generateReport(facade : ReportFacade, filter : ReportFilter) : CommercialPerformanceReport<br>1.1: generateManagerReport(manager : Executive = this, filter : ReportFilter = filter) : CommercialPerformanceReport<br>1.1.1: validateDates() : boolean<br>1.1.2: validFilters<br>opt<br>[validFilter]<br>1.1.3: <<create>> report : CommercialPerformanceReport<br>1.1.4: <<create>> salesMetric : PerformanceMetric<br>1.1.5: addMetric(metric : PerformanceMetric = salesMetric) : void<br>1.1.6:<br>1.1.7: <<create>> conversionMetric : PerformanceMetric<br>1.1.8: addMetric(metric : PerformanceMetric = conversionMetric) : void<br>1.1.9:<br>1.1.10: addMarketInsight(insight : String = "Analisis del periodo") : void<br>1.1.11:<br>1.2: report<br>1.3: report<br>Powered By�Visual Paradigm Community Edition<br><!-- End of picture text -->



Figure 3.29 BOPADIGITAL Sequence Diagram – generateReport 



<!-- Start of picture text -->
sd [32_exportReport]<br>: Executive report : Report currentExporter : PDFExporter<br>1: exportReportToPdf(report : Report) : void<br>1.1: <<create>> pdfExporter : PDFExporter<br>1.2: exportData(exporter : ReportExporter = pdfExporter) : File<br>1.2.1: setExporter(exporter : ReportExporter = exporter) : void<br>1.2.2: export(report : Report = this) : File<br>1.2.2.1: getTitle() : String<br>1.2.2.2: title<br>1.2.2.3: generateFilename(title : String = title) : String<br>1.2.2.4: filename<br>2: <<create>> pdfFile : File<br>3: getMetrics() : List<PerformanceMetric><br>3.1: metrics<br>4:<br>5: pdfFile<br>1.3: exportedFile<br>1.4:<br>Powered By�Visual Paradigm Community Edition<br><!-- End of picture text -->



Figure 3.30 BOPADIGITAL Sequence Diagram – exportReport 



<!-- Start of picture text -->
I<br>|<br>|<br>|<br>|<br>---------> |<br>| I<br>| | ||<br>7, | |<br>||<br>|<br>|<br>ee<br>|<br>I<br>nn<br>a, I<br>|<br>|<br>I<br>|<br>|<br>|<br>p I |<br>LT<br>|I<br>|<br>||<br>@<---------- |||<br>| | I<br>| : Powered By Visual Paradigm!Community Edition<br><!-- End of picture text -->



<!-- Start of picture text -->
I<br>I<br>|<br>I<br>I<br>|<br>I<br>sovees f !<br>I<br>|I<br>|I<br>| |<br>77 |<br>—I|<br>| I<br>|I<br>1|<br>I<br>I<br>I<br>ee ee |<br>|<br>I<br>|<br>nn<br>|<br>!<br>I<br>|<br>@<------------ a |<br>!<br>I1 | Powered By Visual Paradigm CommunityI Edition<br><!-- End of picture text -->



<!-- Start of picture text -->
sd [5_evaluateApplication]<br>: JobApplication currentState : PendingState subscriber : Subscriber<br>1: evaluateApplication(isApproved : boolean) : void<br>1.1: evaluate(isApproved : boolean = isApproved) : void<br>alt<br>[isApproved] 1.1.1: <<create>> nextState : AcceptedState<br>[else]<br>1.1.2: <<create>> nextState : RejectedState<br>1.1.3: changeState(newState : ApplicationState = nextState) : void<br>1.1.4:<br>1.1.5:<br>1.1.5.1:<br>loop<br>[for each subscribers]<br>1.1.5.1.1: update(context : NotifiableEntity = (NotifiableEntity) this) : void<br>1.1.5.2:<br>1.1.5.3:<br>Powered By�Visual Paradigm Community Edition<br><!-- End of picture text -->



Figure 3.33 BOPADIGITAL Sequence Diagram – evaluateApplication 



<!-- Start of picture text -->
| | |<br>|<br>|| StatePattern (see Class Diagram)7 N |I<br>||<br>l|<br>I<br>I<br>I<br>-------------- I<br>|<br>{| |!<br>| I<br>||<br>||<br>||<br>---- | |<br>||<br>||<br>eee | |<br>| |<br>||I<br>|| I<br>| | ObserverPattern (see IN<br>| | [Class Diagram) |<br>pp Ee<br>_||I<br>—|||<br>|| I<br>@<---------- | | |I<br>|| |<br>||I<br>|| |<br>| | | Powered By Visual Paradigm Colnmunity Edition<br><!-- End of picture text -->



<!-- Start of picture text -->
I<br>| |<br>i, | |<br>I<br>I<br>|<br>caaaeneneeen I teeeees  Dn<br>I<br>I<br>|<br>|<br>I<br>|<br>—-------------+------------5><br>I<br>a<br>I<br>|<br>| |<br>|I<br>@< --------- !|| |<br>I: |<br>Powered By Visual Paradigm Community Edition<br><!-- End of picture text -->



<!-- Start of picture text -->
|l|<br>| | |<br>|||<br>| | |<br>|||<br>|!|<br>||<br>||<br>||<br>a, | | | |<br>|| |<br>|l|<br>|||<br>||<br>||<br>'|<br>|<br>|<br>|<br>|||<br>|<br>||<br>| |<br>4||||<br>|||<br>|||<br>|<br>||<br>:l|<br>||<br>||<br>!|<br>|<br>ee<br>|<br>| |<br>| |<br>4 ||!|<br>I||<br>|| |<br>@<------------ \\ | | |<br>| |<br>|: |: |: P owered By Visual Paradigm CommunityI Edition<br><!-- End of picture text -->



<!-- Start of picture text -->
|||<br>| | |<br>|||<br>|| |<br>| | |<br>-----------> | | |<br>|| |<br>|||<br>T|||||<br>|<br>L | ||<br>rs | |<br>|1I|||<br>||<br>|<br>||<br>||<br>|||<br>|| |<br>||<br>||<br>||A<br>||<br>|||<br>|| |<br>| | |<br>Go pn en bn<br>| | |<br>||||<br>| | |<br>@<---------- | | | |<br>| |l || || Powered By Visual Paradigm Community| Edition<br><!-- End of picture text -->



151 

**3.3 Collaboration–Communication Diagrams** 



<!-- Start of picture text -->
><br>eee +<br>A ne<br>, Lo<br>| Powered By Visual Paradigm Community Edition<br><!-- End of picture text -->





<!-- Start of picture text -->
La LE > |<br>4 |v<br>A<br>| Lk  Edition<br><!-- End of picture text -->





<!-- Start of picture text -->
Upload Negotiation Document IN<br>in<br>[ Powered By Visual Paradigm Community Edition<br><!-- End of picture text -->





<!-- Start of picture text -->
Negotiation States IN<br><!-- End of picture text -->





<!-- Start of picture text -->
Powered By Visual Paradigm Community Edition?<br><!-- End of picture text -->



<!-- Start of picture text -->
OfferMatrix States IX |<br>Powered By Visual Paradigm Community Edition<br><!-- End of picture text -->





<!-- Start of picture text -->
NegotiationDocument States IN<br>| Powered By Visual Paradigm Community Edition<br><!-- End of picture text -->





<!-- Start of picture text -->
JobApplication AN<br>States<br>NBs Paradigm Community Edition<br><!-- End of picture text -->



###### **CHAPTER 4 INDIVIDUAL CONTRIBUTIONS** 

|**Name**|**Contributions**|
|---|---|
|Aragon Intriago Shirley|Documentation of sprint backlogs and project schedule,|
|Yamel|development of activity diagrams for system processes,<br>and support in the modeling of collaboration and state<br>diagrams.|
|Diaz<br>Osorio<br>Fernando|Identifcation and documentation of project risks,|
|Nahim|participation in sprint planning activities,<br>and<br>contribution to the defnition and documentation of<br>use case diagrams.|
|Muñoz Sanchez Salvador<br>Gabriel|Design and documentation of class diagrams aligned<br>with SOLID principles, modeling of object diagrams<br>for key system aspects, and contribution to the system<br>component and deployment diagrams.|
|Navarrete Castillo Anthony|Development of the system prototype, modeling of|
|Josue|sequence diagrams for transactional algorithms, and<br>participation in the documentation of system behavior<br>diagrams.|
|Tumbaco Santana Gabriel<br>Alejandro|Integration and consistency of project documentation,<br>coordination of static and behavioral UML modeling<br>(use case, component, deployment, and activity<br>diagrams), and consolidation of the system prototype.|
|Table 4.1|Individual Contributions of the Project|



###### **CHAPTER 5 AUTHORSHIP DECLARATION** 

We, the undersigned members of the **BOPADIGITAL** development team, hereby declare that the present document titled **“BOPACORP S.A. Requirements Specification Document”** has been entirely prepared by us as part of the course **Software Engineering I** at the **Escuela** 

###### **Superior Politécnica del Litoral (ESPOL)** . 

We affirm that all sections, analyses, and specifications contained in this document represent our own work and understanding, based on information gathered from the client and the 

methodologies applied during the software requirements engineering process. 

No part of this document has been copied, plagiarized, or taken from other sources without proper acknowledgment. Any external reference used has been duly cited in the bibliography according to academic integrity standards. 

Each member of the team assumes full responsibility for the authenticity, accuracy, and originality of the content herein. 

**Digital Confirmation:** All members of the team confirm authorship through their electronic submission of this document. 

###### **Team Members:** 

Aragon Intriago Shirley Yamel 

Diaz Osorio Fernando Nahim Muñoz Sanchez Salvador Gabriel Navarrete Castillo Anthony Josue Tumbaco Santana Gabriel Alejandro 



<!-- Start of picture text -->
ESOS—_ Dashboard de Ventas a<br>Vista general del pipeline de ventas<br> kdmin ave Prospeccion 6 Negociacion 1 Cierre 1 Po:<br>$ 2.500 / mes $ 3.800 / mes $4<br>28 Dashboard Maria Fernandez >o ; ; .<br>Tech Innovators SRL Carlos Rodriguez o José Gutiérrez > oO A<br>Q Mi Desemper @ 20987654321 Inversiones Andinas SAC Constructora Moderna D<br>@ 20123456789 EIRL a<br>“eee<br>om22. Mis Co itactos Ricardo.  Gdmez7 > o $ $2.500 ii /mes~ 4<br>Comercial Los Andes SAC Internet Corporativo Telefonia $ $3,800 / me<br>rean) Repositorio7 umentode Sofia Paredes 2<br>Industrias del Norte EIRL<br>Juan Diaz<br>DD<br>ernando Silva = 2 .<br>7 '<br><!-- End of picture text -->



<!-- Start of picture text -->
ESOS—_ Dashboard de Ventas a<br>Vista general del pipeline de ventas<br>kein ave Prospeccion 7 Negociacion 0 Cierre 1 Po:<br>Q§= Dashboard Carlos Rodriguez Carlosnversionesartos RodriRodriguezAndinas SAC < > 0 José Gutiérrez > oO A<br>Q MiDesempef @ 20123456789 ConstructoraFIRL; ModModerna da<br>Internet Corporativo —Telefonia $ $3,800 /me<br>S in ositorio de Maria Fernandez eo<br>Wiens Tech Innovators SRL<br>Juan Diaz . .<br>Dv Ricardo Gémez 0<br>Comercial Los Andes SA v<br>1 »<br><!-- End of picture text -->



<!-- Start of picture text -->
BOPACORP € Volver ala lista de clientes a<br>Facturacién Mensual<br>Asesor Admin @ TechRUC: 20987654321 Innovators SRL $0<br>Contacto: Maria Fernandez « maria.fernandez@techinnovators.pe<br>rospeccion<br>08 De . Py c<br>R Q& Servicios Activos 6 Ultima Visita B Documentos<br>Ninguno 19/12/2024 archivos<br>2 Mis Contactos<br>—= : D itoriovent d Planificary Registrar Visitas + Nueva Visita Oferta de Servicios<br>&i 19/12/2024 © 14:30 Seleccionar P producto... v<br>Empresa en crecimiento, interés en soluciones cloud<br>Selecciona productos para crear una oferta<br>. | © Completada Marcar como Pendiente<br>Editar Cliente x<br>RUC *<br>20987654321<br>Razén Social *<br>Tech Innovators SRL<br>Nombre * Apellido *<br>Maria Fernandez<br>Correo Electrénico *<br>maria.fernandez@techinnovators.pe<br>Etapa de Negociacién *<br>Prospeccion v<br><!-- End of picture text -->



<!-- Start of picture text -->
BOPACORPAsesc ntas B2E Dashboard de Ventas ° TechCliente Innovators  actualizado SRL  exitosamente<br>Vista general del pipeline de ventas<br>ia ave Prospeccion Negociacion Cierre Po:<br>$ 2.500 / mes $ 3.800 / mes $4.<br>Q8 Dashboard Maria Fernandez © ?<br>Tech Innovators SRL Carlos Rodriguez, ®@ oO José.  Gutiérrez. > oO A<br>Q——Mi Desempe @ 20987654321 Inversiones Andinas SAC Constructora Moderna D<br>@ 20123456789 EIRL a<br>a Ricardo Gdmez > oO $ $2.500 /mes 4<br>6) Calendario de Visitas Comercial@ 20444555666Los Andes SAC Internet Corporativo Telefonia $Internet$3.800Corporativo/me Cloud Services<br>o D it:<br>ene Sofia Paredes V4<br>Industrias del Norte EIRL<br>@ 20777888999<br>Juan Diaz<br>Db<br>rr ernando Si a = 2 . .<br><!-- End of picture text -->



<!-- Start of picture text -->
BOPACORPAsesc nt E MonitoreaMi Desempefnotus métricasy rendimientoComercialpersonal fr imo mes a<br>; Asesor Clientes o Negociaciones Ventas Cerradas [@ Facturacién $<br>Admin <MS Contactados ~ Activas Acumulada<br>98.© Dashboard 28 1 1 5 $78.500<br>& 22visitas realizadas © Enproceso de cierre ws 414.9% vsanterior<br>Progreso de Meta Mensual<br>fF Calendario de Visitas Facturacién objetivo: $100.000<br>Cas z i<br>= vento: Actual Meta Faltante<br>$78.500 $100.000 $21.500<br>Juan Diaz<br>JD<br>SEEN Pipeline de Clientes Ventas por Servicio<br><!-- End of picture text -->



<!-- Start of picture text -->
BOPACORP a<br>- . Pipeline de Clientes Ventas por Servicio<br>Distribucién de tus clientes por etapa Distribucién de tus ventas cerradas<br>Asesor Admin CMS<br>0.75 Cloud Services: 1, ternet Corporat<br>Q8 Dashboard<br>Q Mi Desempefio os NegociaciénCliente<br>A Mis Contactos 0.25<br>Seguridad Gestionad<br>” Prospecciér Negociacion Cierre Post-venta<br>_5 D lento:<br>Actividad Semanal<br>JD Juan Diaz Tu gestion comercial de la ultima semana<br>12<br><!-- End of picture text -->



<!-- Start of picture text -->
BOPACORP Actividad Semanal aA<br>A . Tu gestion comercial de la ultima semana iy<br>12<br>, Sab<br>Llamadas : 9<br>Asesor Admin CMS 94 | =<br>5 64 a<br>Q8 Dashboard a _-a<br>| ; ;<br>eno> 4 Mis Contactostact EI<br>Lun Ma Mié Jue Vie Sab Dom<br>5 Calendario de Visit - Llamadas © Visitas<br>_5 D lento:<br>Promedio por Venta Tasa de Visitas Servicios Vendidos<br>a $5.233,333 79% de contactados 42 unidades<br><!-- End of picture text -->



<!-- Start of picture text -->
BOPACORP GestionAa  de Clientesp a L\<br>Administra tu cartera de clientes B2B<br>Asesor Admin CMS Qe : :<br>2 Mis Contactos RUC Razén Social Nombre Apellido Correo<br>c ; 20123456789 Inversiones Andinas SAC Carlos Rodriguez carlos.rodriguez@andinas.com<br>~ Repositorio de 20987654321 Tech Innovators SRL Maria Fernandez maria.fernandez@techinnovators.pe<br>_ D 1ento:<br>20555666777 Constructora Moderna EIRL José Gutiérrez jose.gutierrez@moderna.pe<br>Juan Diaz<br>JD ; ; 20111222333 Distribuidora Mega SAC Ana Torres ana.torres@megadist.com<br>BOPACORP GestionAa  de Clientesp aa al<br>Administra tu cartera de clientes B2B<br>Asesor Admin CMS Qe : :<br>2 Mis Contactos RUC Razén Social Nombre Apellido Correo Etapa<br>c ; 20123456789 Inversiones Andinas SAC Carlos Rodriguez carlos.rodriguez@andinas.com Negociacién<br>eer<br>_ D 1ento:<br>Juan Diaz<br>JD<br><!-- End of picture text -->



<!-- Start of picture text -->
Agregar Nuevo Cliente x<br>RUC *<br>Razén Social*<br>Nombre * Apellido *<br>Correo Electrénico *<br>reo@em<br>Etapa de Negociacién *<br>Prospeccién v<br><!-- End of picture text -->



<!-- Start of picture text -->
BOPACORP CalendarioGestionay visualiza todas delas visitas Visitas programadas es<br>Total Visitas Completadas Agendadas Atrasadas<br>Asesor Admin 9 5 3<br>< Enero 2026 ><br>R<br>Dom Lun Mar Mié Jue Vie Sab<br>FF) Calendariode Visitas<br>= R dEeXe<br>7 Document 4 5 6 7 8 9 10<br>© 15:00 © 11:00 © 16:00<br>Carlos Rod... Maria Fern... José Gutiér...<br>Juan Diaz<br>JD<br><!-- End of picture text -->



<!-- Start of picture text -->
X& Servicios activo! 1 uttima v i sta 3) Vocument -<br>BOPACORP Internet Corporativo, Telefonia 14/1/2025 2 archivos a<br>“ms Planificar y Registrar Visitas Nue i Oferta de Servicios<br>Asesor Admin CMS<br>©} 14/1/2025 © 10:00 Seleccionar producto... v<br>Q5 Dashboard Cliente receptivo a propuesta<br>Selecciona productos para crear una oferta<br>i} Cissus | © Completada dient<br>2 Mis Contactos<br>Calendarioj de \Visitas & 27/2/2025 © 10:00 Documentos {Cloud Services J<br>Seguimiento de propuesta de ampliacién .<br>Documentos aplicables para etapa:<br>umento: | © Completada Pendients Cargar Nuevo Documento<br>H H<br>By benAsesor diezSenio "4/1/2026 © 15:00 ' RUC 11ti Propuesta Comercial ;<br>Reunién para cerrar contrato de ampliacin H1 i c ryan !q “<br><!-- End of picture text -->



<!-- Start of picture text -->
BOPACORPAsesc ntas B2E CalendarioGestionay visualiza todas delas visitas Visitasprogramadas toy J<br>Asesor Admin CMS 9 5 °<br>Q8 Dashboard < Febrero 2026 ><br>Dom Lun Mar Mié Jue Vie Sab<br>OR) Et 1 2 3 4 5 6 7<br>6} Calendariode Visitas<br>Can}rn Repositorion Tnede 8 9 10 1 12 13 14<br>Juan Diaz<br>JD<br>15 16 7 18 19 20 a<br><!-- End of picture text -->



<!-- Start of picture text -->
BOPACORP GestionaMatricestus propuestas de Ofertacomerciales y beneficios para clientes [+ rue mate |<br>[rex Total3 B Boveadores Z Pendientes1 © Aprobades G Rechssadas ® SubsidiosS/ 281.04 Aprobados<br>80 Q Buscar por cliente, RUC o ID de matriz Todos los estados Todos los clientes<br>B) Matricesde Oferta Tech Solutions7  SAC (©Aprobads= ) © Detalle<br>QD rp . ID:om-001 RUC:20123456789<br>4~ Productos/Servicios3 Subtotal$/ 2,342.00 Subsidio-S/ 281.04 (12%) TotalS/ 2,060.96 Final 08/01/2026Fecha Creacion<br>6 Observaciones:<br>Cliente con buen historial de pagos. Solucién integral para expansion a nueva sucursal.<br>Comentario del Supervisor:<br>Aprobada. Excelente propuesta integral que cubre las necesidades del cliente.<br>1 archivo(s) adjunto(s)<br>Distribuidora Lima Norte EIRL © Ver Detalle<br>ID:om-002 RUC: 20987654321<br>JD Juan Diaz<br>Productos/Servicios Subtotal Subsidio (8%) Total Final Fecha Creacion<br>Nueva Matriz de Oferta yw<br>Crea una propuesta comercial con calculo automatico de subsidios<br>Informaci6n del Cliente<br>Cliente *<br>Selecciona un cliente<br>Productos y Servicios<br>Haz clic Noen  hay"AgregarproductosProducto”agregp a radoscomenzar<br>Archivos Adjuntos<br>‘Adjuntar documentos (PDF, Excel, JPG, PNG-max. 50 MB)<br>Browse...No files selected & Cargar<br>Observaciones<br>Cancelar<br><!-- End of picture text -->



<!-- Start of picture text -->
Editar Matriz de Oferta 7<br>om-006<br>Producto #1 Loy<br>Producto/Servicio *<br>Central Telefénica Virtual - S/45.00<br>Cantidad * Precio Unitario *<br>1 1 > | 45 B<br>Observaciones<br>10 extensiones<br>Total de esta linea $/ 45.00<br>Archivos Adjuntos<br>Adjuntar documentos (PDF, Excel, JPG, PNG - max. 50 MB)<br>Browse... No files selected. & Cargar<br>Observaciones<br>Matriz simple para servicio telefénico basico.<br>Cancelar Guardar Borrador<br><!-- End of picture text -->



<!-- Start of picture text -->
Matriz de Oferta om-001 (¢ ssc: x<br>Detalles completos de la propuesta comercial<br>Subtotal (sin subsidio) S/ 2,342.00<br>Subsidio aplicable (12%) -S/ 281.04<br>Total Final s/ 2,060.96<br>Nota: El subsidio de 12% se calculé automaticamente considerando la facturacién mensual (S/ 2,500.00) y los 3 servicios activos del cliente.<br>& Archivos Adjuntos (1)<br>B Cotizacion_Detallada.paf L<br>239.92 KB +10/01/2026, 05:30 a. m. a<br>Observaciones del Asesor<br>Cliente con buen historialde pagos. Solucién integral para expansion a nueva sucursal.<br>@ Comentario de Aprobacién<br>Aprobada. Excelente propuesta integral que cubre las necesidades del cliente.<br>Cerrar<br><!-- End of picture text -->



<!-- Start of picture text -->
BOPACORP. i CatalogoGestiona5 el catalogo decompleto Productosde ofertas comercialesy Serviciosee — GN 4<br>; Total Productos Activos Inactivos Descontinuados<br>Aseso Admin CMS<br>8 @ 7 1<br>®@ Catdlogode Productos<br>Q._ Buscar productos Todas las categorias V7 Todos los estados<br>Internet Fibra Optica 500 Internet Fibra Optica 1 Gbps QE Central Telefénica Virtual<br>Mbps . : T<br>Juan Diaz - »s “ : ts<br>ec eS .<br><!-- End of picture text -->



<!-- Start of picture text -->
BOPACORP 30 ; ; ce<br>—_ nie avs Q Buscar productos © Telefonia YY Todos los estados<br>®@ Catdlogode Productos Central Telefénica Virtual<br>(B conte Web OE<br>Sistema de telefonia empresarial basado en<br>la nube. Gestiona todas tus comunicacione<br>Juan Diaz; $ Precio $45<br>JD or Senio Caracteristicas <<br><!-- End of picture text -->



<!-- Start of picture text -->
ow / I -<br>BOPACORP ce<br>Q_ Buscar productos Todas las categorias YY Descontinuados<br>z J<br>Aseso Admin CMS<br>Internet ADSL 20<br>®@ Catdlogo de Productos Mbps<br>Conexién ADSL basica para pequefias<br>oficinas. Solucién econémica para comenzar<br>$ Precio $199<br>Juan Diaz<br>JD Caracteristicas:<br>* Velocidad de 20 Mbps .<br>BOPACORP ge 7 1 ce<br>- , Q_ Internet Fibra Optica 500 Mbps Todas las categorias Y7 Todos los estados<br>Aseso Admin CMS<br>@ Catalogo de Productos Internet Fibra Optica 500<br>Mbps<br>- =<br>Conexién de alta velocidad con fibra dptica<br>dedicada para empresas. Velocidad simétr<br>Juan Diaz $ Precio $899<br>JD<br>Caracteristicas Y<br><!-- End of picture text -->



<!-- Start of picture text -->
4<br>Nuevo Producto x<br>Nombre del Producto *<br>Telefonia<br>Descripcién *<br>Describe el producto 0 servicio...<br>Categoria * Precio (S/) *<br>Internet Corporativo 0<br>Estado *<br>Activo<br>URL de Imagen<br>@ https://ejemplo.com/imagen.jpg<br><!-- End of picture text -->



<!-- Start of picture text -->
4<br>Editar Producto x<br>Nombre del Producto *<br>Internet Fibra Optica 500 Mbps<br>Descripcién *<br>Conexién de alta velocidad con fibra éptica dedicada para empresas. Velocidad simétrica<br>garantizada de 500 Mbps.<br>Categoria * Precio (S/) *<br>Internet Corporativo 899 a<br>Estado *<br>Activo<br>URL de Imagen<br>© https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=400<br><!-- End of picture text -->



<!-- Start of picture text -->
aloe-update-46068256.figma.site dice<br>gEstds seguro de eliminar "Internet Fibra Optica 500 Mbps"?<br><!-- End of picture text -->



<!-- Start of picture text -->
BOPACORP Editor.  de Contenido.  Web &<br>i Gestiona textos, imagenes y enlaces de la pagina publica<br>Total Elementos Contenidos Activos Contenidos Inactivos<br>Ases Admin CMS<br>80 8 @® Oo&8<br>{B Contenido Web<br>Filtrar porseccién: Todaslas secciones<br>Conectamos tu Empresa al Futuro<br>Soluciones de Telecomunicaciones B2B<br>Descubre nuestras soluciones de conectividad, telefonia y seguridad disefiadas especificamente para el crecimiento de tu negocio.<br>Juan Diaz @ Imagen @ Enlace T Informacién<br>JD ¥<br>AL , Conocer mas Ultima actualizacién:<br>iia 4 ——<br><!-- End of picture text -->



<!-- Start of picture text -->
BOPACORP ce<br>80 8 © Oo&8<br>admin Ms Filtrar por seccién: | Banner Principal<br>Q cat F P<br>{Contenido Web Conectamos tu Empresa al Futuro<br>Soluciones de Telecomunicaciones B2B<br>Descubre nuestras soluciones de conectividad, telefonia y seguridad disefiadas especificamente para el crecimiento de tu negocio.<br>@ imagen @ Enlace T Informacién<br>{VJ . Conocer mas Ultima actualizacién:<br>ily!AH i | i”aiaFy servicio 1005:00dic 2024<br>i.<br>ee https://images.unsplash.com/photo-1497366216<br>7<br>4<br>Editar Contenido Web x<br>Banner Principal<br>VisibleEstado endel la Contenidopagina web . @)<br>Seccion *<br>Banner Principal<br>Orden de visualizacién *<br>1<br>Los elementos se muestran en orden ascendente (1, 2, 3...)<br>Titulo *<br>Conectamos tu Empresa al Futuro<br>Subtitulo<br>Soluciones de Telecomunicaciones B2B<br>Deccrincian<br><!-- End of picture text -->



<!-- Start of picture text -->
BOPACORP Rao<br>Dashboard de Meétricas Generales Woe e<br>l Vista consolidada del rendimiento comercial<br>Ases 5 <MS Ventas Totales $ VentasCerradas @& Visitas Realizadas 2, TiempoNegociacién Promedio ©<br>Dashboardde Métricas $11.740 55 82 15 dias<br>A 412.4% vsanterior periodo Tasa de conversion: 52.4% Ay De 105 contactos £3 Promedio ciclo de venta<br>Po Gest \<br>Equipo Comercial<br>& Gest Docur Estado del equipo de ventas<br>lull Reporte de Asesores 6000<br>4500-4<br>3000-4<br>A Actividad Recient 15004<br>2 Ra Es 9° 2 &<br>— a-<br>Prospeccion Negociacién Cierre Post-venta<br>Ases Admin CMS<br>“Dashboardde Métricas<br>2 Top Performers<br>5 Asesores destacados del periodo<br>2+ Gest le Contactos Roberto Mendoza $4.740<br>15 ventas cerradas 22 visitas<br>wy, Gest Docur<br>Carmen Flores $2.750<br>lt Reporte de Asesores 10 ventas cerradas 14 visitas<br>Luis Castillo $2.300<br>A ctividad Recient 18 ventas cerradas 28 visitas<br><!-- End of picture text -->



<!-- Start of picture text -->
BOPACORP Dashboard de MétricasRao Generales Woe 4<br>ti Vista consolidada del rendimiento comercial<br>Notificaciones x<br>, 4sin leer<br>Ventas Totales $ VentasCerradas G@ Visitas Realiz<br>Ases Admin “MS - Marcar todas como X Limpiar todo<br>leidas pravnoee<br>“Dashboardde Métricas $11.740 55 82<br>412.4% vseeepe TasaEENde conversién:II 52.4%SEES Ay De. 105 contac ) Tu"Propuesta_Ampliacion_Internet.pdf" documento ha °<br>Po Gest A r sido aprobado<br>Cliente: Inversiones Andinas SAC<br>2+ Gestidn de Contactos Documento:<br>Equipo Comercial Propuesta_Ampliacion_Internet.pdf<br>4, Gestién de Document Estado del equipo de ventas 02 ene 2026+ 14:30<br>lui Reporte de Asesores 6000: ro) Tu"Contrato_Servicios_Cloud.pdf"documento ha sido e<br>$ R . . rechazado<br>3000-4 Cliente: Inversiones Andinas SAC<br>A 7 Documento: Contrato_Servicios_Cloud.pdf<br>\- Actividad Recient 15004<br>7 “Elcléusulasdocumentode nivelpresentade servicio.inconsistenciasPor favor, enrevisa las la<br><!-- End of picture text -->



<!-- Start of picture text -->
BOPACORP Dashboard de MétricasRao Generales © Notificacionesmarcadas como leidas<br>ti Vista consolidada del rendimiento comercial<br>Notificaciones x<br>Ases amin ~-MS Ventas Totales $ VentasCerradas @& Visitas Realiz X Limpiar todo<br>72) Pete nes $11.740 55 82 Gs) Tu"Propuesta_Ampliacion_Internet.pdf" documento ha sido<br>na 410.49 V3 Periodo Tasa de conversién: 52.4% Ay De 105 contac aprobado ;<br>5 . anterior Cliente: Inversiones Andinas SAC<br>Lo Gest ASesor<br>Documento:<br>Propuesta_Ampliacion_Internet.pdf<br>Equipo Comercial 02 ene 2026+ 14:30<br>wo,lu ReporteGestién dede AsesoresDocument Estado6000del equipo de ventas fo) . "Contrato_Servicios_Cloud.pdf" rechazadou documento ha sido<br>45004 Cliente: Inversiones Andinas SAC<br>$ Report ita Documento: Contrato_Servicios_Cloud.pdf<br>3000-4<br>A Actividad Recient 1500-4a “Elclausulassecci6ndocumento4.2 deynivelactualizapresentade servicio.losinconsistenciastérminosPor favor,de SLArevisaen segunlas la<br>los estandares corporativos.<br>2 é so 02 ene 2026 «11-15<br><!-- End of picture text -->



<!-- Start of picture text -->
BOPACORP Dashboard de MétricasRao  Generales © Notificaciones eliminadas<br>Vista consolidada del rendimiento comercial<br>Admin; Ventas Totales $ VentasCerradas @G@ Visitas Realizadas 2, Tiempo Promedio ©<br>Negociacién<br>Dashboard de Métricas $11 740 55 82 15 dias<br>A 412.4% vs periodo Tasa de conversion: 52.4% Ay De 105 contactos £3 Promedio ciclo de venta<br>255 G anterior<br>Equipo Comercial<br>% G i Estado del equipo de ventas<br>ll t A 6000)<br>4500-4<br>~ 3000-4<br>"Vv Actividad Recient 1500+<br><!-- End of picture text -->



<!-- Start of picture text -->
BOPACORP Gestionid de Asesores He nuevo Asean al<br>Administra el equipo de ventas B2B<br>Total Asesores Activos Inactivos Clientes Total Ventas Mensuales<br>Admin 5 4 1 63 $76.300<br>7 pe Asesores con Documentacion Pendiente de Revision<br>2 Gestidn de Asesores 2 asesores requieren atencién inmediata<br>4G [<br>ul tedeA Q Buscar por nombre o correo Todos losestados  ¥<br>A, tividad R t Asesor Contacto Clientes Documentos Ventas/Mes roxime Estado<br>fo igu 1<br>g 025-<br><!-- End of picture text -->



<!-- Start of picture text -->
Nuevo Asesor x<br>Nombre * Apellido *<br>Correo Electrénico<br>Teléfono *<br>Estado *<br>Activo v<br><!-- End of picture text -->



<!-- Start of picture text -->
deb Panel de Administracién 5 4 63 $76.300 ~<br>Roberto Mendoza Luis Castillo<br>“7 Dashboardde Métricas ; ;<br>+ Gestidn de Contactos Q Inactivos Y<br>4, Gestiénde Documentos<br>luli Reporte de Asesores Asesor Contacto Clientes5 Documentos Ventas/Mes Proximarp Estado<br>$ Reporte de Ventas Miguel<br>Reyes Bm eyes @l com Sin<br>A; Actividad Reciente ; & +51987 654 325<br>£8 Configuracién v<br><!-- End of picture text -->



<!-- Start of picture text -->
BO a<br>Asesor<br>Roberto Mendoza x<br>© roberto.mendoza@bopacorp.com & +51987654321 £4 Ingreso: 14/03/2023<br>Clientes Asignados Ventas Cerradas Total Facturado Tasa Conversion<br>1 15 USD 78,500 0.0%<br>n tistorial de Cambios Clientes (1) Documentos — Métricasde Desempefio _—— Actividades Recientes<br>Ro Gestiq<br>Historial de Cambios en Clientes<br>+ Registro completo de todas las modificaciones realizadas por el asesor<br>RZ <7 Inversiones Andinas SAC 14/01/2025<br>ul Reunién con gerente general para presentar propuesta de ampliacién de ancho de banda ”<br>. MBB inversinnes Andinas SAC 9710119095<br>Ni :<br><!-- End of picture text -->



<!-- Start of picture text -->
BO \<br>Asesor<br>Roberto Mendoza x<br>© roberto.mendoza@bopacorp.com & +51987654321 £4 Ingreso: 14/03/2023<br>Clientes Asignados Ventas Cerradas Total Facturado Tasa Conversion<br>1 15 USD 78,500 0.0%<br>n Historialde Cambios _| Clientes ( Documentos — Métricasde Desempefio _—— Actividades Recientes<br>Ro Gestiq<br>Clientes Asignados Todaslasetapas  ¥<br>+ Lista completade clientes del asesor<br>a) RUC Razén Social Contacto Etapa Ultiiia F ac turaciéturacion Documentos Acciones<br>Visita Mensual<br>ll 20123456789 SACInversiInversiones Andinas: CarlosRodriguez Negociacion 14/01/2025(ov USDSD  2,5002,501 G1 ©1@0 ® DetallesVer PS v<br>Ni :<br><!-- End of picture text -->



<!-- Start of picture text -->
BO S\<br>Asesor<br>Roberto Mendoza x<br>© roberto.mendoza@bopacorp.com %& +51987654321 (4 Ingreso: 14/03/2023<br>Clientes Asignados Ventas Cerradas Total Facturado Tasa Conversion<br>1 15 USD 78,500 0.0%<br>‘ Historialde Cambios Clientes(1) MétricasdeDesempefio _ Actividades Recientes<br>Ro Gestiq<br>Documentos Cargados por el Asesor<br>2+ Consulta de documentos agrupados por cliente empresarial<br>ae | a fC a it<br>ll Total Documentos Aprobados Pendientes Rechazados<br>bs ov<br>$ R Mostrando documentos de 1 cliente Todos losestados  ¥<br>6 a<br><!-- End of picture text -->



<!-- Start of picture text -->
BO S\<br>Asesor<br>Roberto Mendoza x<br>© roberto.mendoza@bopacorp.com %& +51987654321 (4 Ingreso: 14/03/2023<br>Clientes Asignados Ventas Cerradas Total Facturado Tasa Conversion<br>1 15 USD 78,500 0.0%<br>/ Historialde Cambios Clientes(1) Documentos Métricasde Desempefio__ Actividades Recientes<br>Ro Gestiq<br>Métricas de Desempefio<br>2+ Indicadores clave de rendimiento del asesor<br>— ©, Gestion de Clientes $ Facturacién<br>ll Clientes Contactados 28 Total Facturado USD 78,500 my<br>. Clientes Visitados 22 Servicios Vendidos 42<br>6 a<br><!-- End of picture text -->



<!-- Start of picture text -->
BO B\<br>Asesor<br>Roberto Mendoza x<br>Sroberto.mendoza@bopacorp.com & +51987654321 § Ingreso: 14/03/2023<br>Clientes Asignados Ventas Cerradas Total Facturado Tasa Conversion<br>1 15, USD 78,500 0.0%<br>Ro Gestiq<br>Actividades Recientes<br>+ Timelinede acciones del asesor<br>Cliente: Inversiones Andinas SAC<br>lu Contrato de ampliacién de servicios por $2,500/mes<br>bs v<br>~ % MAW Estado actualizado 30/12/2025 12:15<br>fo L 025-<br><!-- End of picture text -->



<!-- Start of picture text -->
BOPACORP Gestionoe de Contactos ra<br>‘ Asigna contactos a tus asesores y gestiona la distribucién de clientes<br>2k ContactosNo Asignados @ 2y Contactos Asignados | 4<br>Admin —<br>Listado de Contactos No Asignados<br>~™ Da rc cas<br>267 G Q Buscar nbre, correo, RUC l<br>Prospeccién Negociacion Cierre Post-venta<br>%} G . r + Agregar Contacto Seleccionar asesor... ¥ C<br>ll t A a RUC Nombre Apellido Correo Empresa Etapa Acciones<br>$ R t Comercial v7<br>ME s.20444555666 Ricardo Gémez ricardo.gomez@losandes.pe Los Andes ® | GE<br>SAC Detalles<br>A, Actividad Recient<br>- Industrias Ver<br>§ Configur ’ Hs 20777888999 Sofia Paredes sofia.paredes@industriasnorte.pe del Norte Prospeccién © Watallec Gt<br><!-- End of picture text -->



<!-- Start of picture text -->
BOPACORP 2X Contactos No Asignados @ 2¥ Contactos Asignados (4 fat<br>Listado de Contactos No Asignados<br>_ Carin _ Q Buscarp nbre, corr C o razon social.<br>&o- Gest A Mostrando5 contactos filtrados x Limpiar Filtros<br>2+ Gestién de Contactos + Agregar Contacto Seleccionar asesor... ¥<br>4, Gestién de Docur @sruc Nombre Apellido Correo Empresa Etapa Acciones<br>lu Reporte de Asesores Comercial — —<br>ME s.20444555666 Ricardo Gémez ricardo.gomez@losandes.pe Los Andes © peniks | Gt<br>: . SAC<br>A ctividad Recien Industrias Ver<br>UP Geen Sea Ms. 20777888999 Sofia Paredes _sofia.paredes@industriasnorte.pe del Norte © petits | Get<br>EIRL<br><!-- End of picture text -->



<!-- Start of picture text -->
Q Buscar nbre, correo, RUC o razén social<br>BOPACORP a<br>t Todos Prospeccién Negociacion Cierre Post-venta<br>Mostrando 5 contactos filtrados * Limpiar Filtros<br>Ases Admin “MS<br>+ Agregar Contacto Patricia Vargas v<br>of) REer reek tiie: ruc Nombre Apellido Correo Empresa Etapa Acciones<br>Po Gest A Comercial —_ —|<br>¥Y = 20444555666 Ricardo Gémez ricardo.gomez@losandes.pe Los Andes ® Daulles | Get<br>2+ Gestin de Contactos SAC<br>V . ; Industrias v |<br>mG © Docu ¥ 20777888999 Sofia Paredes _sofia.paredes@industriasnorte.pe del Norte © eutes WE<br>EIRL Detalles<br>Textiles v<br>$ ereRe dE' 20333222111 Fernando _Silva fernando.silva@textilesperu.com Peruanos © dente WWE<br>SA Detalles<br>A Actividad Recient :<br>Ms Logistica Ver<br>a3 Configur 1 20666777888 Daniela Campos _—_daniela.campos@logisticaexpress.pe ExpressSAC co) Detalles |7Zt<br><!-- End of picture text -->



<!-- Start of picture text -->
2% Contactos No A t 2 2 Contactos Asignados 7 2<br>BOPACORP ry Contactos asignados exitosamente<br>A i Listado de Contactos No Asignados 3 contactos asignados a Patricia Vargas<br>—— Q nbre R<br>1" Dashboardde Métricas Mostrando2 contactos filtrados x Limpiar Filtros<br>+ Agregar Contacto Seleccionar asesor... ¥<br>2+ Gestinde Contactos<br>a RUC Nombre Apellido Correo Empresa Etapa Acciones<br>4 Gestién de Documentos<br>Logistica Ver<br>Li Reporte de Asesores Ms 20666777888 Daniela Campos _daniela.campos@logisticaexpress.pe SACExpress © pesins |—E<br>$ Reporte de Venta Servicios —_<br>MM s.20999888777 Alberto Vega alberto.vega@serviciosfinlima.com° Financieros co) Detalles | E<br>A, Actividad Recient Lima SA<br>£8 Configuracién ~~<br>BOPACORP HF Soreeeoones* a<br>Listado de Contactos Asignados<br>AAseso Admini EMS Q Ir nbret R Filtros<br>RUC Nombre _Apellido Correo Empresa Asesor Etapa weisi<br>2+ Gestinde Contactos<br>, Gestién de Documentos 20123456789 Carlos Rodriguez _carlos.rodriquez@andinas.com ee ow 14/1/2025<br>20987654321 Maria Fernandez maria.fernandez@techinnovators.pe _ Innovators ‘ 19/12/2024<br>$ Reporte de Venta SRL 9<br>A, Actividad Recient Constructora<br>20555666777 José Gutiérrez jose.gutierrez@moderna.pe Moderna 17/11/2025<br>EIRL :<br>£8 Configuracién ~~<br><!-- End of picture text -->



<!-- Start of picture text -->
Agregar Nuevo Cliente x<br>RUC*<br>Razén Social *<br>Er SAC<br>Nombre * Apellido *<br>rlos R ez<br>Correo Electrénico *<br>Etapa de Negociacién *<br>Prospeccién v<br><!-- End of picture text -->



<!-- Start of picture text -->
BOPACORP Gestiona de Documentos 4a<br>‘ Aprueba, rechaza y descarga documentos de forma individual o en lote<br>Admin Q Buscar px te, RUC, documento, etiquet: ¥ Filtros<br>So> G BB Seleccionar todos A c t CD F zarC t ® Descargar Document<br>4, Gestién de Documentos my RobertoInversionesMendozaAndinas* 2 documentosSAC RUC: 20123456789<br>ll tedeA<br>BY Tech Innovators SRL RUC: 20987654321<br>; Patricia Vargas * 1documento<br>A V Actividad Recient my Constructora Moderna EIRL RUC: 20555666777<br>Luis Castillo * 1documento<br><!-- End of picture text -->



<!-- Start of picture text -->
BOPACORP Gestionoe de Documentos 4a<br>° ras Aprueba,rechaza y descarga documentosde forma individualo en lote<br>Aseso Admin CMS Qe r R rent T Filtros<br>“J Dashboardde Métricas<br>Mostrando 3 documentos x Limpiar Filtros<br>2o Gestién de Asesore<br>+ Gestign de Contacto Seleccionar todos<br>4 Gestién de Documentos<br>. gv Inversiones Andinas SAC RUC: 20123456789<br>@v Constructora Moderna EIRL RUC: 20555666777<br>Luis Castillo * 1documento<br>A Actividad Recient<br>{3 Configuracién ComercialLos Andes SAC_ RUC: 20444555666 ~~<br><!-- End of picture text -->



<!-- Start of picture text -->
Aplueug, }eUiaca y UESU!ya UULUT HENS UE FUL Ha HTUIvIUUGL U EH Lee _<br>Q Ir R rent T Filtros<br>Mostrando 3 documentos x Limpiar Filtros<br>“J Dashboardde Métricas<br>WE 1 documento seleccionado  Aprobar Documento(s) GP Rechazar Documento(s) ® Descargar Documento(s)<br>2o Gestién de Asesore<br>mi Gestion de Contactos mv Inversiones Andinas SAC RUC: 20123456789<br>4 Gestién de Documentos<br>Lui Reporte de Asesores > yy Construct@aesmmttcharMod EIRL R UC: 2055 56667 77<br>Luis Castillo » 1documento<br>| i ComercialLos Andes SAC RUC: 20444555666<br>A; Actividad Recient Patricia Vargas * 1documentc<br>£8 Configuracién ~~<br><!-- End of picture text -->



<!-- Start of picture text -->
aloe-update-46068256.figma.site dice<br>Ingresa el motivo de rechazo para todos los documentos<br>seleccionados:<br>Cancelar<br><!-- End of picture text -->



<!-- Start of picture text -->
BOPACORP Gestion deD t y<br>t estion de Vocumentos @ 23298 iniciada<br>Aprueba, rechaza y descarga documentos de forma individual o en lote Djescarganci d oo T1 didocumento t e n fetormatoito ZIP<br>Ases Admin “MS Q Buscar te, RUC, documento, etiquet TY Filtros<br>Mostrando 1 documento x Limpiar Filtros<br>Lo Gest A<br>2+ Gest Cantante § Seleccionar todos c DR D r -<br>4 Gestién de Documentos<br>li Reporte de Asesores BY ComercialPatricia VargasLos* An1 d ocumentoes SAC RUC: 20444555666<br>A Actividad Recient<br><!-- End of picture text -->



<!-- Start of picture text -->
BOPACORP ow ° A<br>Reportes de Desempefio Comercial 4,UEExportar Reporte x<br>A us Analisis de productividad del equipo de ventas<br>= : \/ Filtros de Reporte A<br>BRo Asesor © Periodoi Periodo Seleccionado:<br>m™ Das oard”de Métricas Todos los Asesores v Mes Actual v Mes Actual (Enero 2026)<br>© Zona ® Tipo de Servicio<br>Todas las Zonas a Todos los Servicios v<br>4, Gestién de Documentos<br>Ventas Totales Ventas Cerradas Total Clientes Visitas Realizadas Documentos Promedio x Venta<br>LL Reportede Asesores $284.800 55 9 82 9 $5.178<br>A\, Actividadlad RRecient \ Ventas por Asesor &, Clientes por Etapa<br>100000<br>BOPACORP ow ° A<br>Reportes de Desempefio Comercial 4,UEExportar Reporte x<br>A us Analisis de productividad del equipo de ventas<br>= : \/ Filtros de Reporte A<br>BRo Asesor © Periodoi Periodo Seleccionado:<br>m™ Das oard¥de Métricas Roberto Mendoza v Ultimo Semestre v Ultimo Semestre (Jul-Dic 2025)<br>© Zona ® Tipo de Servicio<br>Este v Internet Corporativo v<br>4, Gestién de Documentos<br>Ventas Totales Ventas Cerradas Total Clientes Visitas Realizadas Documentos Promedio x Venta<br>LL Reportede Asesores $78.500 15 0 2 0 $5.233<br>,\, ActividadconRecient Ll i VentVentas por AAsesor &,2 ClientClientes por EtEtapa<br>80000<br><!-- End of picture text -->



<!-- Start of picture text -->
aloe-update-46068256.figma.site dice<br>Funcion de exportaci6n de reporte en desarrollo. Se<br>generara un PDF con todos los datos visualizados<br><!-- End of picture text -->



<!-- Start of picture text -->
BOPACORP fag<br>t Actividad Reciente actividades<br>J rs) Venta Cerrada por Roberto Mendoza 16:45<br>Ases Admin a ENN<br>Contratode ampliacion de servicios por $2,500/mes<br>5> Gest 5 Documento Subido por Patricia Vargas 15:20<br>; Propuesta Comercial - Internet + Cloud Services<br>, 2025-12-31<br>& Gest Docur<br>Visita Realizada por Luis Castillo 14:10<br>Presentacién de soluciones de conectividad para obra<br>$ Report ’ 2025-12-31<br>A; Actividad Reciente © Visita Agendada por Carmen Flores 3:30<br>rc} sHipaur - Distribuidora MegaSAC<br><!-- End of picture text -->



<!-- Start of picture text -->
BOPACORP  Configuracion de Documentos a<br>Defina los tipos de documentos obligatorios u opcionales sequin el tipo de servicio y etapa de negociacién<br>© Los documentos obligatorios seran requeridos para que el asesor pueda avanzar el cliente a las etapas seleccionadas.<br>Admin Configure si un documento aplica para todos los servicios o solo para servicios especificos (Internet, Telefonia, Cloud, Seguridad).<br>A Da + Agregar Tipo de Documento<br>2 G<br>Tipo de Documento Requerimiento Alcance de Servicios Etapas Aplicables Acciones<br>—<br>&aG ——<br>Ll tedeA () Propuesta Comercial | G Editar | |  Eliminar<br>=) * {§) Contrato Final | G Editar | W Eliminar<br>A, Actividad R t<br>B Acta de Visita | —& editar | etiminar<br><!-- End of picture text -->



<!-- Start of picture text -->
2<br>Editar Tipo de Documento x<br>Nombre del Documento * Requerimiento *<br>RUC Obligatorio v<br>Etapas Aplicables *<br>Y @ Aplica para todos los servicios<br>Cancelar Guardar Cambios<br><!-- End of picture text -->



<!-- Start of picture text -->
aloe-update-46068256.figma.site dice<br>cEsta seguro de eliminar el tipo de documento "RUC"?<br><!-- End of picture text -->



<!-- Start of picture text -->
BOPACORP . o.<br> Configuracion de Documentos e<br>‘ Defina los tipos de documentos obligatorios u opcionales segtin el tipo de servicio y etapa de negociacién<br>: © Los documentos obligatorios seran requeridos para que el asesor pueda avanzar el cliente a las etapas seleccionadas.<br>Ases Admin MS Configure si un documento aplica para todos los servicios o solo para servicios especificos (Internet, Telefonia, Cloud, Seguridad).<br>+ Agregar Nuevo Tipo de Documento<br>Fo Gest ‘ Nombre del Documento * Requerimiento<br>+ Gest Garin Ej: Acta d fi dad Obligatorio v<br>Etapas Aplicables<br>& Gest Docur *<br>Prospeccién Negociacién Cierre Post-venta<br>Y ® Aplica para todos los servicios<br>\ R : Caneslar<br>$8 Configuracién<br><!-- End of picture text -->



<!-- Start of picture text -->
BOPACORP Reportes i i a 4<br>Analisis detallado de detransacciones Ventasde venta y Cierrespor asesor, servicio Comercialesy zona et.<br>‘7 Filtrosde Reporte A<br>‘Admin<br>@ Asesor Comercial ® Tipode Servicio © Zona Geografica 6 Periodo<br>7 Todos los Asesores ¥ Todos los Servicios ¥ Todas las Zonas v Mes Actual yi<br>0 Filtros Aplicados<br>Mes Actual (Enero 2026)<br>¥ ~ Métricas de Ventas<br>nw<br>$ Reportede Ventas Monto Total Facturado Total de Ventas Cerradas Monto Promediopor Venta<br>$2,500 1<br>8 © Analisis Visual de Ventas<br>Ventas por Tipo de Servicio Ventas por Zona Geografica<br>2600<br>1950<br>= . nternet Corporativo: $2,500 1300<br>sini @ 650-4 a<br>BOPACORP Reportes de Ventas y Cierres Comerciales Ga=4<br>Analisis detallado dettransacciones de venta por asesor, servicio yzona<br>‘T7 Filtros deReporte a<br>Admin<br>@ Asesor Comercial fy Tipo de Servicio. © Zona Geografica 63 Periodo<br>a Roberto Mendoza ’ Todos los Servicios Todas las Zonas v Ultimo Semestre v<br>20 Filtros Aplicados<br>———<— |<br>& ~ Métricas de Ventas<br>~<br>$2,240 3<br>$ © Anilisis Visual de Ventas<br>Ventas por Tipo de Servicio Ventas por Zona Geografica<br>-@m ,<br>AD Norte<br><!-- End of picture text -->



<!-- Start of picture text -->
® aloe-update-46068256.figma.site<br>Funcion de exportacionde reporte endesarrollo. Se<br>yeneraré un PDF con todos los datos de ventas<br><!-- End of picture text -->

193 

###### **1.0.4 Mobile app** 



<!-- Start of picture text -->
9:35 p.m. © HORS IO<br>CRM Empresarial<br>Correo electrénico<br>Contrasefia<br>@ Ingresar como Admin<br>Credenciales de Prueba:<br>Asesor: asesor@logicost.ec / 123456<br>Admin: admin@logicost.ec / 123456<br><!-- End of picture text -->



<!-- Start of picture text -->
BOPACORPSA CRM<br>Hola, Asesor1<br>Q<br>Activos<br>Actividad proxima<br>4 dias para cierre<br>Visita<br>Cotizacion<br>Empresa X. SA<br>12-10-25 12:30pm<br>© Proxima actividad<br>Subida de<br>documentaci6n<br>Sapitos Corp.<br>14-10-25 6:00pm<br>BOPACORPSAft MisEaClientes Mis Actividades& Mi2Perfil<br><!-- End of picture text -->



<!-- Start of picture text -->
BOPACORPSA CRM<br>Actividad reciente<br>Visita Técnica<br>Empresa X. SA<br>10-10-25 2:00pm<br>Subida de<br>documentacion<br>Sapitos Corp.<br>09-10-25 4:00pm<br>Clientes (6)<br>Logistica =f Edita’ & Eliminar<br>Costera<br>(LogiCost)<br>Cliente<br>lucrativo<br>BOPACORPSAft MisEaClientes Mis Actividades& Mi2Perfil<br><!-- End of picture text -->



<!-- Start of picture text -->
<€ Actividad - BOPACORPSA<br>Nueva Actividad<br>Crea una nueva actividad para el cliente<br>Titulo de la Actividad *<br>Tipo de Actividad *<br>Visita Técnica<br>Llamada de Seguimiento<br>Envio de Propuesta<br>Subida de documentaci6n Reunion<br>Otro<br>Fecha * Hora *<br>Estado<br><!-- End of picture text -->



<!-- Start of picture text -->
< Actividad - BOPACORPSA<br>Prioridad<br>Descripcion<br>Notas Adicionales<br>Acciones Rapidas<br>Agendar Recordatorio Compartir —Adjuntar Archivo<br>@ Crear Actividad<br>© Cancelar<br>Mis Clientes<br>Mis Clientes 2)<br>Q<br>Activos<br>Logistica =f Editar & Eliminar<br>Costera<br>(LogiCost)<br>Cliente<br>lucrativo<br>Nombre de Contacto:<br>Juan Vélez<br>Correo:<br>jevelez@logicost.ec<br>Andres @ Editar Bi Eliminar<br>Carros Inc.<br>BOPACORPSAft MisEaClientes Mis Actividadesi} Mi2Perfil<br><!-- End of picture text -->



<!-- Start of picture text -->
BOPACORPSA CRM<br>Clientes (6)<br>Logistica =f Edita’ & Eliminar<br>Costera<br>(LogiCost)<br>Cliente<br>lucrativo<br>Nombre de Contacto:<br>Juan Vélez<br>Correo:<br>jcvelez@logicost.ec<br>Andres @ Editar Bi Eliminar<br>Carros Inc.<br>Cliente<br>lucrativo<br>Nombre de Contacto:<br>Adalina Medina<br>Correo:<br>portabilidadCAl@gmail.com<br>BOPACORPSAft MisEaClientes Mis Actividades& Mi2Perfil<br><!-- End of picture text -->



<!-- Start of picture text -->
€ Cliente - BOPACORPSA<br>Nuevo Cliente<br>Ingresa la informacion del nuevo cliente<br>Agregar Foto<br>Nombre de Empresa *<br>Nombre de Contacto *<br>Correo Electrénico *<br>Teléfono *<br><!-- End of picture text -->



<!-- Start of picture text -->
€ Cliente - BOPACORPSA<br>Nombre de Contacto *<br>Correo Electrénico *<br>Teléfono *<br>Direccion<br>Estado<br>Prospecto Inactivo<br>@ Guardar Cliente<br>® Cancelar<br><!-- End of picture text -->



<!-- Start of picture text -->
€ Cliente - BOPACORPSA<br>eH] Logistica(LogiCost) Costera<br>Cliente lucrativo<br>Informacion del Cliente<br>& NOMBRE DE CONTACTO<br>Juan Vélez<br>CORREO ELECTRONICO.<br>jcvelez@logicost.ec<br>&_ TELEFONO<br>+593 98 123 4567<br>@ _DIRECCION<br>Av. Principal 123, Guayaquil<br>Plan de Negocio<br>Ea VozBussiness Gold& Conectividad  Plan Mov<br>14.99 + Iva c/linea Plan Activo<br>— {e) q<br><!-- End of picture text -->



<!-- Start of picture text -->
€ Cliente - BOPACORPSA<br>FA VozBussiness& ConectividadGold Plan Mov<br>14.99 + Ilva c/linea<br>Actividades Recientes<br>Visita Cotizacion<br>Presentacion de servicios de logistica<br>especializada<br>12-10-25 12:30pm<br>Llamada de Seguimiento<br>Seguimiento de propuesta enviada<br>08-10-25 10:15am<br>Envio de Propuesta<br>Propuesta comercial enviada por email<br>05-10-25 3:45pm<br>Zona de Peligro<br><!-- End of picture text -->



<!-- Start of picture text -->
Mis Actividades<br>Mis Actividades 2)<br>Visita<br>Cotizacion<br>Empresa X. SA<br>12-10-25 12:30pm<br>@ Proxima actividad<br>Subida de<br>documentaci6n<br>Sapitos Corp.<br>14-10-25 6:00pm<br>@ Proxima actividad<br>Visita Técnica<br>Fmnresa X SA<br>BOPACORPSAft MisEaClientes Mis Actividadesi} Mi2Perfil<br><!-- End of picture text -->



<!-- Start of picture text -->
Mis Clientes<br>Mis Clientes 2)<br>Q<br>Activos<br>Logistica =f Editar & Eliminar<br>Costera<br>(LogiCost)<br>Cliente<br>lucrativo<br>Nombre de Contacto:<br>Juan Vélez<br>Correo:<br>jevelez@logicost.ec<br>Andres @ Editar Bi Eliminar<br>Carros Inc.<br>BOPACORPSAft MisEaClientes Mis Actividadesi} Mi2Perfil<br><!-- End of picture text -->



<!-- Start of picture text -->
Mi Perfil<br>a<br>Juan Pérez<br>juan.perez@bopacorpsa.com<br>Clientes Actividades Afio<br>c Editar Perfil<br>Actualizar informacion personal<br>@. Gestionar Equipo<br>a) Agregar nuevos asesores<br>BOPACORPSAft MisaClientes Mis Actividades& Mi = Perfil2<br><!-- End of picture text -->



<!-- Start of picture text -->
Mi Perfil<br>c Editar Perfil<br>Actualizar informacion personal<br>@. Gestionar Equipo<br>a) Agregar nuevos asesores<br>a ActualizarCambiar Contrasefiacredenciales de acceso<br>Pet ConfiguracionPreferencias de la aplicacion<br>@ Version 1.0.0<br>EE) BOPACORPSA CRM<br>(F Miembro desde 15/01/2024<br>© Cerrar Sesion<br>BOPACORPSAft MisaClientes Mis Actividades& Mi = Perfil2<br><!-- End of picture text -->



<!-- Start of picture text -->
Admin - BOPACORPSA<br><!-- End of picture text -->

Hola, Admin BOPACORPSA - Administracion 



<!-- Start of picture text -->
Estadisticas Rapidas<br><!-- End of picture text -->



<!-- Start of picture text -->
o<br>156 23<br>Clientes Totales Proyectos Activos<br>$125,000 12<br>Ingresos Mensuales Tareas Pendientes<br>Acciones Administrativas<br>Gestion de Usuarios ><br>Administrar asesores y permisos<br>a ok | a<br>Admin - BOPAC.... Gestion de Usua... Catalogo de Ser. Configuracién<br><!-- End of picture text -->



<!-- Start of picture text -->
Admin - BOPACORPSA<br>Acciones Administrativas<br>Gestion de Usuarios ><br>Administrar asesores y permisos<br>Reportes y Analytics ><br>Ver estadisticas y reportes<br>Gestion de Servicios<br>Administrar catalogo de ><br>servicios<br>Base de Datos ><br>Gestion de datos y backups<br>Estado del Sistema<br>@ Sistema Operativo<br>Todos Ios servicios funcionando correctamente<br>ui ok | a<br>Admin - BOPAC... Gestion de Usua... Catalogo de Ser. Configuracién<br><!-- End of picture text -->



<!-- Start of picture text -->
Gestion de Usuarios<br>Gestion de Usuarios 2)<br>Q<br>Juan Pérez<br>juan.perez@bopacorpsa.com<br>© Ultimo acceso: 15/01/2026 09:30<br>§ Clientes activos: 45<br>7 Editar @ Reset BF Eliminar<br>Maria Gonzalez<br>maria.gonzalez@bopacorpsa.com<br>© Ultimo acceso: 15/01/2026 08:15<br>§ Clientes activos: 38<br>@# Editar @ Reset BF Eliminar<br>Carlos Rodriguez<br>Aaland endeinuntAhananana a<br>Lr a | be<br>Admin ~-BOPAC... Gestiénde Usua.. Catalogo de Ser. Configuraci6n<br><!-- End of picture text -->



<!-- Start of picture text -->
Admin - BOPACORPSA<br>Estado del Sistema<br>@ Sistema Operativo<br>Todos los servicios funcionando correctamente<br>A Ultima Copia de Seguridad<br>Hace 2 horas - 15/01/2026 10:30 AM<br>© Versién del Sistema<br>v2.1.4 - Ultima actualizacin: 12/01/2026<br>Acceso Rapido<br>Lr a<br>Vista Asesor Notificaciones<br>() &<br>Soporte Cerrar Sesion<br>LT a | be<br>Admin -BOPAC.. Gestiénde Usua.._ Catalogode Ser. Configuraci6n<br><!-- End of picture text -->



<!-- Start of picture text -->
< Nuevo Usuario<br>Nuevo Usuario<br>Crea una nueva cuenta de usuario<br>Nombre Completo *<br>Correo Electrénico *<br>Rol<br>Contrasefia *<br>Confirmar Contrasefia *<br>@ Elusuario podra acceder al sistema con su<br>email y contrasefia.<br><!-- End of picture text -->



<!-- Start of picture text -->
Catalogo de Servicios<br>Gestion de Servicios r+)<br>Consultoria * i<br>Empresarial<br>Consultoria<br>Asesoria estratégica para optimizacion de<br>procesos<br>$ $150.00 © 4horas<br>Desarrollo de |<br>Software<br>Tecnologia<br>Creacion de soluciones tecnolégicas a medida<br>$ $2500.00 © Por proyecto<br>AuditoriaSistemas de rn |<br>Auditoria<br>Revision completa de sistemas y procesos<br>$ $800.00 © 2dias<br>Lr a | be<br>Admin - BOPAC. Gestion de Usua.._Catdlogo de Ser. Configuraci6n<br><!-- End of picture text -->



<!-- Start of picture text -->
Soluciones de<br>lelecomunicaciones pala<br>Conectamos tu negocio con tecnologia de punta. Planes corporativos, conectividad de<br>alta velocidad y servicios digitales disefiados para impulsar tu empresa.<br>Ver Catélogode Servicios > Conoce Mas<br>bh Conectividad Empresarial 4 Planes Corporativos fe) Servicios Digitales<br>Soluciones de internet satelital y enlaces dedicados Telefoniamévil y fijaadaptada a las necesidades de Cloud computing y seguridad informatica de nivel<br>de alta velocidad tu negocio empresarial<br>»~CrNnn AN AAs AaAI7 Ar.<br><!-- End of picture text -->



<!-- Start of picture text -->
8 | BOPACORP S.A. Inicio Nosotros Servicios Trabaja con Nosotros Cotizar Servicios<br>Lideres en telecomunicaciones empresariales con mas de 15 anos transformando la<br>conectividad de negocios en toda la region.<br>Nuestra Historia<br>Mision<br>Fundada en 2009, BOPACORP S.A. nacié con la vision de revolucionar las telecomunicaciones Proveer soluciones de telecomunicaciones integrales que impulsen el crecimiento y la<br>empresariales en América Latina. Desde nuestros inicios, nos hemos enfocado en ofrecer soluciones de eficiencia operativa de nuestros clientes empresariales, garantizando conectividad de<br>conectividad robustas y confiables para empresas de todos los tamafios clase mundial con el mejor soporte técnico.<br>A\lo largo de los afios, hemos expandido nuestra red de cobertura, incorporado tecnologias de ultima<br>generacion y construido relaciones duraderas con mas de 500 empresas que confianen nosotros para<br>mantenerse conectadas.<br>© Vision<br>Ser la empresa lider en telecomunicaciones B2B en la region, reconocida por nuestra<br>innovaci6n tecnolégica, excelencia en servicio y capacidad para adaptarnosa las<br>necesidades cambiantes del mercado empresarial<br>Nuestros Valores<br>Q ow[op] ©<br><!-- End of picture text -->



<!-- Start of picture text -->
8 | BOPACORP S.A. Inicio Nosotros Servicios  Trabaja con Nosotros<br>Catalogo de Servicios<br>Soluciones empresariales disefiadas para impulsar tu negocio<br>Q Buscar servicios. Todas las Categorias Todas las Zonas Todos los Precios<br>Mostrando 11 de 11 servicios |<br>& Voz CG Voz 0 Voz<br>Plan Corporativo 100 Plan Corporativo 500+ Smartphones Corporativos<br>Plande voz paraequipos de hasta100 lineas con minutos ilimitados Plan premiumpara grandes empresas con mds de 500 lineas Equiposde ultima generacién con planesflexiblesde financiamiento<br>$25- $35 por linea/mes $18- $25 por linea/mes $300- $1,200<br>Nacional Regional Nacional Internacional Nacional<br>Ver Detalles Ver Detalles Ver Detalles<br><!-- End of picture text -->



<!-- Start of picture text -->
& Plan Corporativo.  100 x<br>Voz Telefonia<br>Plan de voz para equipos de hasta 100 lineas con minutos<br>ilimitados<br>$ Costos Transparentes<br>$25 - $35 por linea/mes<br>Precios més IVA. Instalacion y equipamiento seguin<br>requerimientos especificos.<br>Y Beneficios Clave<br>v_ Minutos ilimitados v_ SMS incluidos<br>v_ Roaming nacional v Soporte 24/7<br>© Zonade Cobertura<br>(6) Condiciones de Uso Especificas<br>+ Contrato minimo de 12 meses con renovacién automatica<br>+ Instalacién incluida en zonas de cobertura confirmada<br><!-- End of picture text -->



<!-- Start of picture text -->
8 | BOPACORP S.A. Inicio Nosotros Servicios Trabaja con Nosotros<br>Q Cloud Servicios Digitales Nacional $100 - $500<br>Mostrando1 de 11 servicios<br>(@s) Digital<br>Cloud Computing Basico<br>Infraestructura en la nube para pequefias empresas<br>$100 - $300/mes<br>Nacional<br>Ver Detalles<br><!-- End of picture text -->



<!-- Start of picture text -->
Unete a nuestro equipo de asesores comerciales y construye una carrera exitosa en el<br>sector de telecomunicaciones empresariales<br>Crecimiento Comisiones Capacitacion Beneficios<br>Plande carrera estructurado Bonos atractivospor resultados Formacién continua Salud, autoy mas<br>Vacantes Disponibles<br>Asesor Comercial B2B - Zona Norte Asesor Comercial B2B - Region Metropolitana<br>© Antofagasta,Chile © Santiago, Chile<br>© Tiempo Completo © Tiempo Completo<br>Buscamos un asesor comercial dinamico para gestionar y ampliar nuestra cartera de clientes empresariales Unete a nuestro equipo comercial en Santiago para desarrollar nuevas oportunidades de negocio y gestionar<br>en la zona norte del pais. cuentas clave.<br><!-- End of picture text -->



<!-- Start of picture text -->
Postular a Asesor Comercial;  B2B - Zona Norte x<br>Antofagasta, Chile - Tiempo Completo<br>Nombre Completo * Email*<br>Juan Pérez juan@email.com<br>Teléfono * Linkedin (Opcional)<br>+569 1234 5678 linkedin.com/in/tu-perfil<br>Curriculum Vitae (PDF) *<br>&<br>Haz clicPDF, paramaximo cargar5MB tu CV<br>Cartade Presentacién (Opcional)<br>Cuéntanospor qué eres el candidatoideal para este puesto.<br><!-- End of picture text -->



<!-- Start of picture text -->
x<br>jPostulacién Enviada!<br>Hemos recibido tu postulacién correctamente. Nuestro equipo de<br>Recursos Humanos la revisaré y te contactaremos pronto.<br>Confirmacién enviada a:<br>das@sad<br><!-- End of picture text -->

###### **APPENDIX II** 

###### **CLIENT ACCEPTANCE LETTER** 

###### **1. Signed Approval Document** 

This appendix includes the official approval letter signed by the stakeholder representative of **BOPACORP S.A.** , which formally validates the Project Specification Document. The signed document confirms the stakeholder’s agreement with the documented project scope, including the risk management artifacts, sprint backlogs, project schedule, UML-based static and behavioral system models, and the system prototype, as defined during the requirements elicitation and analysis phases. 



<!-- Start of picture text -->
CY) O [ PolitécnicaEscuela Superiordel Litoral<br><!-- End of picture text -->

###### Carta de aceptacién de proyecto BOPADIGITAL 

###### Guayaquil, 12 de enero del 2026. 

A la fecha de hoy, ante los documentos presentados, los cuales representan el trabajo realizado en la fase de disefio del proyecto BOPADIGITAL. En el que se ponen a evidencia los siguientes contenidos: 

- e Documentacidn de gestién de riesgos identificados para el proyecto. e Sprint backlogs y cronograma de actividades mediante diagramas activity-on-arrow. e Diagramas de casos de uso con documentacién completa de cada caso de uso del sistema. 

- e Diagramas de clases que contemplan la légica de negocio del sistema, aplicando principios SOLID y patrones de disefio (State, Strategy, Factory Method, Composite, Facade, Observer, Singleton). 

- e Diagramas de objetos que representan los aspectos medulares del sistema. e Diagramas de componentes del sistema. e Diagrama de despliegue del sistema. 

- e Diagramas de actividad de los procesos del sistema. e Diagramas de secuencia de 32 algoritmos transaccionales relevantes del sistema. e Diagramas de colaboracién/comunicacion con fines ilustrativos. e Diagramas de estado para los objetos pertinentes del sistema (Negotiation, OfferMatrix, NegotiationDocument, JobApplication). 

Mediante la presente acta de conformidad, el cliente, representado por Mgtr. Christian Pauta, declara haber recibido, revisado y aceptado el contenido del documento entregado, reconociendo que el disefio propuesto refleja adecuadamente la arquitectura y funcionalidad establecida durante las reuniones previas, manifestando su conformidad con los puntos especificados, los cuales cumplen con los objetivos planteados para la fase de disefio del proyecto BOPADIGITAL. 

De la misma forma, declara su disposicion a continuar trabajando con el equipo establecido en futuras reuniones y discusiones que permitan avanzar hacia las siguientes fases de implementacién del proyecto. 

Por su parte, el equipo de desarrollo reitera su compromiso de continuar trabajando de manera dinamica y profesional, manteniendo la fidelidad a los requerimientos del proyecto en las siguientes fases de desarrollo e implementacién del proyecto BOPADIGITAL. 



<!-- Start of picture text -->
Reciboa s a re rdo con lo establecido en el presente documento.<br>ARE<br>Magtr. Christian Pauta e<br>Propietario Gerente de BOPACORP S.A.<br><!-- End of picture text -->



<!-- Start of picture text -->
SL TT TP LT TT RTE ee ee<br><!-- End of picture text -->

**APPENDIX III REQUIREMENTS SPECIFICATION DOCUMENT** 

212 

BOPACORP S.A. Requirements Specification Document 

by 

###### Grupo 2 BOPADIGITAL 

###### PROJECT PRESENTED TO ESCUELA SUPERIOR POLITÉCNICA DEL LITORAL 

###### GUAYAQUIL, NOVEMBER 13, 2025 

ESCUELA SUPERIOR POLITÉCNICA DEL LITORAL ESPOL 

Grupo 2 BOPADIGITAL, 2025 

213 

This Creative Commons license allows readers to download this work and share it with others as long as the author is credited. The content of this work cannot be modified in any way or used commercially. 

214 

###### **TEAM MEMBERS** 

THIS PROJECT HAS BEEN DEVELOPED 

BY THE FOLLOWING GROUP OF STUDENTS 

Shirley Aragon Facultad de Ingenieria en Electricidad y Computación 

Nahim Díaz 

Facultad de Ingenieria en Electricidad y Computación 

Salvador Muñoz 

Facultad de Ingenieria en Electricidad y Computación 

Gabriel Tumbaco 

Facultad de Ingenieria en Electricidad y Computación 

Anthony Navarrete 

Facultad de Ingenieria en Electricidad y Computación 

215 

###### **TABLE OF CONTENTS** 

||||Page|
|---|---|---|---|
|CHA|PTER 1|PURPOSE OF THE PROJECT ...............................|.................1|
|1.1|Proble|m Description .....................................................|.................1|
|1.2|Project|Description .......................................................|.................1|
|1.3|Project|Purpose ...........................................................|................ 2|
|CHA|PTER 2|STAKEHOLDERS ............................................|................ 4|
|2.1|Busines|s Client ...........................................................|................ 4|
|2.2|Sales A|dvisor .............................................................|................ 4|
|2.3|Immedi|ate Supervisor / Sales Manager .................................|................ 4|
|2.4|Docum|entation Coordinator .............................................|................ 5|
|2.5|Manage|ment / Executive Board .........................................|................ 5|
|2.6|Sales A|dvisor Candidate .................................................|................ 5|
|2.7|Web Ad|ministrator .......................................................|................ 5|
|CHA|PTER 3|CONSTRAINTS ...............................................|................ 7|
|3.1|Solutio|n Constraints ......................................................|................ 7|
|3.2|Implem|entation Environment of the Current System ...................|................ 7|
|CHA|PTER 4|SCOPE OF THE WORK ......................................|................ 8|
|4.1|Public|Website ............................................................|................ 8|
||4.1.1|Hierarchical Service Catalog ..................................|................ 8|
||4.1.2|Detailed Service Information ..................................|................ 8|
||4.1.3|Employment Application Module .............................|................ 9|
|4.2|Interna|l Application (Web and Mobile) .................................|................ 9|
||4.2.1|Negotiation Management ......................................|................ 9|
||4.2.2|Negotiation Tracking ..........................................|................ 9|
||4.2.3|Intelligent Reporting ...........................................|................ 9|
||4.2.4|Document Management .......................................|............... 10|
|4.3|Scope S|ummary ..........................................................|............... 10|
|CHA|PTER 5|FUNCTIONAL REQUIREMENTS ..........................|............... 11|
|5.1|Public|Website ............................................................|............... 12|
||5.1.1|Service Catalog and Website Module (CAT) .................|............... 12|
||5.1.2|Content Management Module (CMS) ........................|............... 13|
||5.1.3|Employability and Application Module (EMP) ..............|............... 14|
|5.2|Interna|<br>l Application ......................................................|............... 15|
||5.2.1|Client Relationship Management Module (CRM) ............<br>|............... 15<br>|
||5.2.2|Ofer Matrix Module (MAT) ..................................|............... 18|
||5.2.3|Supervision and Approvals Module (SUP) ...................|............... 20|
||5.2.4|Document Management Module (DOC) ......................|............... 21|



216 II 

||5.2.5|Reporting Module (REP) ..................................................... 22|
|---|---|---|
||5.2.6|Basic Security Module (SEG) ................................................ 24<br>|
||5.2.7|Notifcations Module (NOT) ................................................. 25|
|CHA|PTER 6|NON-FUNCTIONAL REQUIREMENTS .................................. 26|
|CHA|PTER 7|USER STORIES .............................................................. 33|
|7.1|Service|Catalog and Website Module (CAT) .......................................... 33|
|7.2|Content|Management Module (CMS) .................................................. 35|
|7.3|Employa|bility and Application Module (EMP) ........................................ 37|
|7.4|Client M<br>|anagement Module (CRM) ................................................... 39<br>|
|7.5|Ofer M|atrix Module (MAT) ........................................................... 46|
|7.6|Supervis|ion and Approvals Module (SUP) ............................................ 48|
|7.7|Docume|nt Management Module (DOC) ............................................... 50|
|7.8|Reportin|g Module (REP) ............................................................... 54|
|CHA|PTER 8|PROTOTYPE ................................................................. 58|
|8.1|Link ...|................................................................................... 58|
|CHA|PTER 9|EVIDENCES .................................................................. 59|
|9.1|Require|ments Elicitation Technique .................................................... 59|
|9.2|Evidenc|e Repository .................................................................... 59|
|CHA|PTER 10|INDIVIDUAL CONTRIBUTIONS .......................................... 60|
|CHA|PTER 11|AUTHORSHIP DECLARATION ........................................... 61|
|APPE|NDIX I|PROTOTYPE ................................................................. 62|
|APPE|NDIX II|CLIENT ACCEPTANCE LETTER .......................................... 74|
|APPE|NDIX III|SIGNED AUTORSHIP DECLARATION ................................... 75|



217 

###### **LIST OF TABLES** 

|||Page|
|---|---|---|
|Table 5.1|Functional Requirements - Service Catalog and Website (CAT) .......|.... 12|
|Table 5.2|Functional Requirements - Content Management Module (CMS) .....|.... 13|
|Table 5.3|Functional Requirements - Employability and Application Module<br>(EMP) .....................................................................|.... 14|
|Table 5.4|Functional Requirements - Client Relationship Management Module<br>(CRM) .....................................................................|.... 15|
|Table 5.5|Functional Requirements - Ofer Matrix Module (MAT) ...............|.... 18|
|Table 5.6|Functional Requirements - Supervision and Approvals Module (SUP)|.... 20|
|Table 5.7|Functional Requirements - Document Management Module (DOC) ..|.... 21|
|Table 5.8|Functional Requirements - Reporting Module (REP) ..................|.... 22|
|Table 5.9|Functional Requirements - Basic Security Module (SEG) .............|.... 24|
|Table 5.10|Functional Requirements - Notifcations Module (NOT) ...............|.... 25|
|Table 6.1|Non-Functional Requirements - BOPADIGITAL System ..............|.... 27|
|Table 10.1|Individual Contributions of the Project ..................................|.... 60|



218 

###### **LIST OF FIGURES** 

|||Page|
|---|---|---|
|Figure 8.1|Prototype of BOPADIGITAL ...........................................|.... 58|
|Figure 9.1|Meeting with the managers of BOPACORP S.A. ......................|.... 59|
|Figure I-1|Screenshots of BOPADIGITAL mobile app from the perspective of a<br>Sales Advisor. ...........................................................|.... 63|
|Figure I-2|Screenshots of BOPADIGITAL mobile app from the perspective of a<br>Sales Advisor. ...........................................................|.... 64|
|Figure I-3|Screenshots of BOPADIGITAL mobile app from the perspective of<br>Management. ............................................................|.... 65|
|Figure I-4|Screenshots of BOPADIGITAL CMS website .........................|.... 66|
|Figure I-5|Screenshots of BOPADIGITAL CMS website .........................|.... 67|
|Figure I-6|Website from the perspective of a sales advisor candidate. ...........|.... 68|
|Figure I-7|Screenshots of BOPADIGITAL CRM website for sales consultant ...|.... 69|
|Figure I-8|Screenshots of BOPADIGITAL CRM website for sales consultant ...|.... 70|
|Figure I-9|Screenshots of BOPADIGITAL CRM form the perspective of<br>Management.<br>...........................................................|.... 71|
|Figure I-10|Screenshots of BOPADIGITAL CRM form the perspective of<br>Management.<br>...........................................................|.... 72|
|Figure I-11|Screenshots of BOPADIGITAL CRM form the perspective of<br>Management.<br>...........................................................|.... 73|



219 

###### **LIST OF ABBREVIATIONS** 

BOPACORP S.A. Telecommunications company and main client of the project 

BOPADIGITAL Digital platform developed for BOPACORP S.A. 

- B2B Business-to-Business (commercial model between companies) 

- CMS Content Management System – module for website content administration 

- CRM Customer Relationship Management – module for managing business clients and negotiations 

- DOC Document Management Module 

- EMP Employability / Application Module 

- MAT Offer Matrix Module 

- REP Reporting Module 

- SUP Supervision and Approvals Module 

- CAT Catalog and Website Module 

- SEG Basic Security Module 

- NOT Notifications Module 

- GPS Global Positioning System 

- UI User Interface 

- UX User Experience 

- JWT JSON Web Token (authentication mechanism) 

TLS Transport Layer Security (encryption protocol for HTTPS) PDF Portable Document Format 

220 VI 

|KPI|Key Performance Indicator|
|---|---|
|RUC|Unique Taxpayer Registry|
|ID|Identifer (unique reference or key)|



221 

###### **LIST OF SYMBOLS AND UNITS OF MEASUREMENTS** 

% Percentage (used in performance indicators such as availability or success rate) 

s Seconds (used for system response times, e.g., ≤ 3 s) 

MB Megabytes (used for file upload size limits, e.g., 50 MB) 

h Hours (used for availability and operational timeframes) 

222 

###### **CHAPTER 1** 

###### **PURPOSE OF THE PROJECT** 

###### **1.1 Problem Description** 

BOPACORP is a strategic commercial partner of Movistar, focused on selling telecommunication services to business clients (B2B). The company’s commercial process relies on a team of sales executives (advisors) who perform prospecting, field visits, and contract closures. 

The current operating model is manual, decentralized, and heavily dependent on tools such as Excel, Google Drive, and instant messaging (WhatsApp and Email), which generates three critical bottlenecks directly impacting productivity and profitability: 

1. The main bottleneck occurs after a successful sales close. The executive must collect physical documentation from the client (contract, ID, RUC, etc.) and physically return to the office to deliver it to the operational area. This travel generates "dead time," a significant opportunity cost where the comercial advisor could be making another commercial visit. This delay worsens at month-end, accumulating work for the operations team (coordination) and delaying service activation. 

2. Management and immediate supervisors lack real-time visibility into the sales team’s activities. Supervision is based on manual communication (asking via WhatsApp or chat) to find out an executive’s location or the status of a visit. 

3. All performance tracking and sales pipeline management are done in Excel spreadsheets. Immediate supervisors must consolidate this information manually for their weekly "oneon-one" meetings. 

###### **1.2 Project Description** 

The BOPADIGITAL project is a comprehensive software solution, composed of an administrative web application and a mobile application, custom-designed for BOPACORP. 

223 

2 

The system’s main objective is to digitize and centralize the complete B2B (business-to-business) sales lifecycle. Currently, this process is managed manually using a set of decentralized tools, which includes: 

- Google Drive, for storing and transferring contractual documentation. 

- Excel spreadsheets for reporting and tracking advisor performance. 

- Direct communication channels (such as WhatsApp or email) for daily supervision and status reporting. 

The proposed solution will replace these manual processes by implementing several interconnected modules: 

1. CRM Module (Web and Mobile): Allows for prospect registration, client portfolio management, and updating negotiation statuses (e.g., Initial Visit, Negotiation, Closing). 

2. Mobile Document Management Module: Facilitates the uploading of contractual documentation (ID, RUC, appointment, contract) directly from the advisor’s mobile device in the field. 

3. Supervision Module: Provides management with a feed of recent activity and tools for scheduling and tracking visits, improving visibility of field management. 

4. Intelligent Reporting Module: Centralizes sales data in an administrative dashboard for performance evaluation. 

###### **1.3 Project Purpose** 

The fundamental purpose of BOPADIGITAL is to increase the operational efficiency of the commercial team and improve managerial visibility for strategic decision-making. 

The objectives of the project are: 

1. Mobility and Field Productivity Module: Develop an internal web and mobile application that eliminates “Dead Time” by enabling consultants to upload contractual documentation (RUC, ID, Contract) in real time from the field, while also providing structured client management through the registration and updating of prospects with key commercial data (invoicing, number of lines) and the scheduling of visits. 

224 

3 

2. Content Management and Web Catalog Module (CMS): Design and develop a web product catalog under a content management scheme to facilitate its administration, allowing business clients to contact a sales consultant to initiate negotiation. 

3. Centralize and Automate Supervision: Replace manual supervision (based on asking “Where are you?” or “How’s it going?” via chat) with an active system. The project aims to give management real-time visibility into advisors’ locations, visit statuses, and field activity validation, reducing the likelihood of false or unverified visits. 

4. Enable Data-Driven Decision Making: Transform the current manual report generation process (in Excel) into an automated dashboard. This will make weekly follow-up meetings (“one-on-ones”) more efficient and focused on actionable insights, with consolidated key metrics such as pipeline by stage, billing, closing time, and performance in strategic products. 

225 

###### **CHAPTER 2** 

###### **STAKEHOLDERS** 

###### **2.1 Business Client** 

Business clients are external users who will access BOPACORP’s public website to explore the catalog of products and services offered, including voice, connectivity, digital, satellite tracking, and cloud security solutions. Their main interest is to find suitable options for their companies, compare prices and benefits, and contact a sales advisor to start a negotiation. They expect a clear, reliable, and visually appealing platform that allows them to identify services quickly and communicate effectively with the company. 

###### **2.2 Sales Advisor** 

The sales advisor is the key operational user of the internal system, responsible for managing the entire sales cycle, from client prospecting to post-sale follow-up. They use the web and mobile application to register clients, plan visits, document negotiations, create offer matrices, and upload supporting documentation. Their main goal is to have an agile tool that allows them to work from the client’s office, upload information in real time, and optimize their time without needing to return to the company’s premises, thereby improving customer service efficiency. 

###### **2.3 Immediate Supervisor / Sales Manager** 

The immediate supervisor or sales manager is an administrative user who oversees the work of sales advisors and monitors negotiation progress. Their responsibilities include approving offer matrices, analyzing performance indicators, and generating sales reports by period or by advisor. They need a system that provides complete visibility of the commercial flow, facilitates decision-making, and keeps real-time control over the team’s performance to ensure sales objectives are met. 

226 5 

###### **2.4 Documentation Coordinator** 

The coordinator is responsible for managing documentation and activating contracted services. They use the internal application to define mandatory documents, review files uploaded by sales advisors, and update their approval status. They also coordinate with Telefónica’s platform to complete the service activation process. Their main objective is to reduce bottlenecks during closing periods and ensure all documentation is complete and verified on time, thus improving operational efficiency across departments. 

###### **2.5 Management / Executive Board** 

The management team represents the company’s executive stakeholders, responsible for making strategic decisions based on data generated by the system. Their focus is on analyzing consolidated reports on sales, productivity, and commercial performance through the intelligent reporting module. They expect the platform to provide reliable metrics, visual dashboards, and historical comparisons that support data-driven decision-making and the strategic growth of the organization. 

###### **2.6 Sales Advisor Candidate** 

Sales advisor candidates are external users interested in joining BOPACORP’s commercial team. They use the employment section of the website to view available vacancies, complete online application forms, and upload their resumes in PDF format. They expect a simple, transparent, and automated process that provides visual and email confirmation once their application is submitted, enhancing the company’s professional image and facilitating human resource management. 

###### **2.7 Web Administrator** 

The web administrator is responsible for maintaining and updating the public content of BOPACORP’s website. Through the Content Management System (CMS) module, they can edit 

227 

6 

text, images, links, service categories, and publish new products without requiring advanced technical knowledge. Their goal is to keep the website’s information accurate and attractive, ensuring consistency, branding alignment, and clear communication with potential clients. 

228 

###### **CHAPTER 3** 

###### **CONSTRAINTS** 

###### **3.1 Solution Constraints** 

The development of the BOPADIGITAL platform will be carried out using React for the frontend interface, Node.js with Express for the backend services, and PostgreSQL as the primary relational database. These technologies have been selected due to their proven scalability, active community support, and compatibility with modern web architectures. The use of open-source tools minimizes licensing costs and ensures maintainability by the development team after project delivery. The solution must also use Docker containers for deployment to guarantee consistency across environments. Therefore, the final product must be fully operational using these technologies and deployed within a Dockerized environment, without depending on proprietary or paid software frameworks. 

###### **3.2 Implementation Environment of the Current System** 

The platform will be implemented in a cloud-based environment running on Linux servers, using Docker for containerization and NGINX as the web server. Development and testing will be performed in a controlled cloud environment before being deployed to production. This approach ensures scalability, security, and easy maintenance. The system must be compatible with both web and mobile devices, ensuring that authorized users can access it from any location with an internet connection. 

229 

###### **CHAPTER 4** 

###### **SCOPE OF THE WORK** 

The BOPADIGITAL project aims to design and develop an integrated digital platform for BOPACORP S.A., a company specialized in telecommunications products and services. The system will consist of two main components: a public website and an internal web and mobile application. Together, these components will optimize the company’s commercial processes, from client acquisition to post-sale management. 

###### **4.1 Public Website** 

The website is designed to increase BOPACORP’s online visibility and facilitate interaction with potential business clients. It will provide detailed and up-to-date information on all products and services, allowing external users to explore available options and initiate contact with the sales team. In addition, the site will include a recruitment section to manage job applications for new sales advisors. 

###### **4.1.1 Hierarchical Service Catalog** 

The platform will feature a hierarchical catalog that organizes services into categories such as Voice, Connectivity, and Digital Services. Each category will include subcategories that enable structured navigation and efficient search of service information. 

###### **4.1.2 Detailed Service Information** 

Every service entry will contain comprehensive details, including costs, benefits, and additional conditions. This ensures transparency and allows potential clients to make informed decisions before initiating a commercial contact. 

230 9 

###### **4.1.3 Employment Application Module** 

The website will provide a dedicated employment module allowing prospective sales advisors to view available positions, fill out application forms, and upload their resumes (CVs) in PDF format. This feature will streamline recruitment processes and centralize applicant data. 

###### **4.2 Internal Application (Web and Mobile)** 

The internal application is intended to support the complete sales negotiation process, allowing the commercial team to manage prospects, monitor negotiations, and maintain updated client information. It will also optimize document handling and provide analytical tools to evaluate commercial performance. 

###### **4.2.1 Negotiation Management** 

Sales advisors will register potential clients, track negotiation stages, and record interactions in real time. The application will allow continuous monitoring of each business opportunity until closure. 

###### **4.2.2 Negotiation Tracking** 

Supervisors will be able to visualize the current status of all negotiations, including client details, deal stages, approval matrices, and estimated closing times. This enables greater oversight of the commercial process and advisor productivity. 

###### **4.2.3 Intelligent Reporting** 

The system will include a reporting module that generates metrics and performance analyses, such as sales by period, advisor performance, and clients not yet converted. These reports will serve as a decision-making tool for management and supervisors. 

231 10 

###### **4.2.4 Document Management** 

The internal system will incorporate a document management module allowing advisors to upload required documentation for each negotiation. Coordinators will have access to review, approve, or reject files, ensuring all necessary information is validated for service activation. 

###### **4.3 Scope Summary** 

Overall, the system will enable BOPACORP S.A. to: 

- Present a structured, user-friendly catalog of telecommunications services. 

- Streamline and digitize the commercial process from client prospecting to service activation. 

- Provide real-time visibility of sales operations for supervisors and management. 

- Centralize documentation and standardize approval workflows. 

- Facilitate recruitment of new sales advisors through the corporate website. 

- Ensure scalability for the future integration of new services and strategic partners. 

232 

###### **CHAPTER 5** 

###### **FUNCTIONAL REQUIREMENTS** 

This section defines the functional requirements of the BOPADIGITAL system, which describe the specific behaviors, actions, and processes that the software must perform to meet the needs of its stakeholders. Each requirement has been derived from the system’s modules, stakeholder interviews, and the client’s business processes. 

The functional requirements are organized by modules that represent the main subsystems of BOPADIGITAL, including the public website and the internal application (web and mobile). This structure ensures clarity, traceability, and alignment with the project scope. 

233 

12 

###### **5.1 Public Website** 

###### **5.1.1 Service Catalog and Website Module (CAT)** 

|**ID**|**Version**|**Description**|**User / Role**|**Priority**|
|---|---|---|---|---|
|RF-CAT-001|1.0|The system shall allow the business client<br>to view a catalog of products and services<br>organized into categories such as Voice,<br>Connectivity, and Digital Services.|Business<br>Client|High|
|RF-CAT-002|1.0|The system shall allow the business client to<br>view costs, benefts, and usage conditions<br>for each item in the catalog.|Business<br>Client|High|
|RF-CAT-003|1.0|The system shall allow the business client<br>to flter catalog items by category, coverage,<br>and price.|Business<br>Client|Medium|
|RF-CAT-004|1.0|The system shall allow the business client<br>to contact a sales advisor to initiate<br>a negotiation regarding selected catalog<br>items.|Business<br>Client|High|
|RF-CAT-005|1.0|The system shall allow the business client to<br>view information about BOPACORP S.A.’s<br>history, mission, vision, and values.|Business<br>Client|High|



Table 5.1 Functional Requirements - Service Catalog and Website (CAT) 

234 

13 

###### **5.1.2 Content Management Module (CMS)** 

|**ID**|**Version**|**Desc**|**ription**||||**User / Role**|**Priority**|
|---|---|---|---|---|---|---|---|---|
|RF-CMS-001|1.0|The<br>admi<br>mana<br>authe|system<br>nistrator<br>gement p<br>ntication|shall<br>to<br>ac<br>anel us<br>(userna|allow<br>cess<br>t<br>ing cred<br>me and|the<br>web<br>he<br>content<br>ential-based<br>password).|Web<br>Administrator|High|
|RF-CMS-002|1.0|The<br>admi<br>links|system<br>nistrator <br>of the pu|shall<br> to edit <br>blic we|allow<br> texts, i<br>bsite.|the<br>web<br>mages, and|Web<br>Administrator|High|
|RF-CMS-003|1.0|The<br>admi<br>servic|system<br>nistrator <br>es withi|shall<br>to creat<br>n the cat|allow<br>e new p<br>alog.|the<br>web<br>roducts and|Web<br>Administrator|High|
|RF-CMS-004|1.0|The<br>admi<br>of ex<br>catalo|system<br>nistrator <br>isting pr<br>g.|shall<br> to upd<br>oducts|allow<br>ate the <br>and ser|the<br>web<br> information<br>vices in the|Web<br>Administrator|High|
|RF-CMS-005|1.0|The<br>admi<br>servic|system<br>nistrator <br>es from|shall<br> to de<br>the cata|allow<br>lete pr<br>log.|the<br>web<br>oducts and|Web<br>Administrator|High|



Table 5.2 Functional Requirements - Content Management Module (CMS) 

235 

14 

###### **5.1.3 Employability and Application Module (EMP)** 

|**ID**|**Version**|**Description**|**User / Role**|**Priority**|
|---|---|---|---|---|
|RF-EMP-001|1.0|The system shall allow the sales advisor<br>candidate to view available vacancies,<br>displaying the position title, description,<br>requirements, and publication date.|Sales Advisor<br>Candidate|High|
|RF-EMP-002|1.0|The system shall allow the sales advisor<br>candidate to complete an application form<br>by entering personal details and contact<br>information.|Sales Advisor<br>Candidate|High|
|RF-EMP-003|1.0|The system shall allow the sales advisor<br>candidate to upload their resume (CV) in<br>PDF format as a mandatory part of the<br>application process.|Sales Advisor<br>Candidate|High|
|RF-EMP-004|1.0|The system shall validate that all required<br>felds in the application form are correctly<br>flled before allowing submission.|Sales Advisor<br>Candidate|High|
|RF-EMP-005|1.0|The system shall notify the sales advisor<br>candidate visually and via email once<br>their application has been successfully<br>submitted.|Sales Advisor<br>Candidate|High|
|RF-EMP-006|1.0|The system shall allow the sales advisor<br>candidate to be informed of the result of<br>their application.|Sales Advisor<br>Candidate|Medium|



Table 5.3 Functional Requirements - Employability and Application Module (EMP) 

236 15 

###### **5.2 Internal Application** 

###### **5.2.1 Client Relationship Management Module (CRM)** 

Table 5.4 Functional Requirements - Client Relationship Management Module (CRM) 

|**ID**|**Version**|**Description**|**User / Role**|**Priority**|
|---|---|---|---|---|
|RF-CRM-001|1.0|The system shall allow the sales advisor to<br>fll out a client registration form including<br>the company’s RUC (tax ID), business<br>name, number of active services, and<br>current monthly billing.|Sales Advisor|High|
|RF-CRM-002|1.0|The system shall allow the sales advisor to<br>update the information of assigned business<br>clients.|Sales Advisor|High|
|RF-CRM-003|1.0|The system shall allow the sales advisor<br>to flter and search business clients by<br>negotiation stage or visit date.|Sales Advisor|High|
|RF-CRM-004|1.0|The system shall allow the sales advisor<br>to schedule on-site visits with assigned<br>business clients.|Sales Advisor|High|
|RF-CRM-005|1.0|The system shall allow the sales advisor<br>to register a new client visit by entering<br>date, time, observations, and GPS location<br>automatically obtained from their mobile<br>device.|Sales Advisor|High|
||||Continued o|n next page|



237 

16 

**Table 5.4 (continued) – Client Relationship Management Module (CRM)** 

|**ID**|**Version**|**Description**|**User / Role**|**Priority**|
|---|---|---|---|---|
|RF-CRM-006|1.0|The system shall allow the immediate<br>supervisor to view the GPS location<br>registered by the sales advisor during each<br>visit to verify its validity.|Immediate<br>Supervisor|High|
|RF-CRM-007|1.0|The system shall allow the sales advisor<br>to view a history of visits made to their<br>assigned business clients.|Sales Advisor|High|
|RF-CRM-008|1.0|The system shall allow the sales advisor<br>to update the negotiation status with an<br>assigned business client.|Sales Advisor|High|
|RF-CRM-009|1.0|The system shall allow the immediate<br>supervisor to register new business clients,<br>including RUC, business name, number of<br>active services, and current monthly billing.|Immediate<br>Supervisor|High|
|RF-CRM-010|1.0|The system shall allow the immediate<br>supervisor to update information about<br>business clients.|Immediate<br>Supervisor|High|
|RF-CRM-011|1.0|The system shall allow the immediate<br>supervisor to deactivate business clients<br>when necessary.|Immediate<br>Supervisor|High|
|RF-CRM-012|1.0|The system shall allow the immediate<br>supervisor to assign business clients to sales<br>advisors to initiate negotiations.|Immediate<br>Supervisor|High|
||||Continued o|n next page|



238 

17 

**Table 5.4 (continued) – Client Relationship Management Module (CRM)** 

|**ID**|**Version**|**Description**|**User / Role**|**Priority**|
|---|---|---|---|---|
|RF-CRM-013|1.0|The system shall allow the immediate<br>supervisor to view the list of business<br>clients assigned to each sales advisor.|Immediate<br>Supervisor|High|
|RF-CRM-014|1.0|The system shall allow the immediate<br>supervisor to remove business clients from<br>a sales advisor’s portfolio.|Immediate<br>Supervisor|High|
|RF-CRM-015|1.0|The system shall allow the immediate<br>supervisor to view the recent activity of<br>all company sales advisors.|Immediate<br>Supervisor|High|
|RF-CRM-016|1.0|The system shall allow management to<br>view, for each sales advisor, the number<br>of business clients contacted, visited, and<br>successfully closed.|Management|High|
|RF-CRM-017|1.0|The system shall allow management to view<br>the total billed amount per advisor, along<br>with the total number of services sold and<br>the average revenue per service.|Management|High|
|RF-CRM-018|1.0|The system shall allow management to view<br>the count and total value of terminals and<br>equipment sold by each advisor.|Management|High|
|RF-CRM-019|1.0|The system shall allow management to view,<br>for each advisor, the number of business<br>clients in each sales funnel stage.|Management|High|



|Continued on next page|
|---|



239 

18 

**Table 5.4 (continued) – Client Relationship Management Module (CRM)** 

|**ID**|**Version**|**Description**|**User / Role**|**Priority**|
|---|---|---|---|---|
|RF-CRM-020|1.0|The system shall allow the immediate<br>supervisor to flter and search business<br>clients by negotiation stage, visit date, or<br>assigned advisor.|Immediate<br>Supervisor|High|
|RF-CRM-021|1.0|The system shall restrict access so that sales<br>advisors can only view and modify data of<br>business clients assigned to them.|Sales Advisor|High|
|RF-CRM-022|1.0|The system shall allow the immediate<br>supervisor to consult a detailed history of<br>modifcations made by each sales advisor<br>to their clients.|Immediate<br>Supervisor|High|



###### **5.2.2 Offer Matrix Module (MAT)** 

Table 5.5 Functional Requirements - Offer Matrix Module (MAT) 

|**ID**|**Version**|**Description**|**User / Role**|**Priority**|
|---|---|---|---|---|
|RF-MAT-001|1.0|The system shall allow the sales advisor to<br>create a new ofer matrix associated with a<br>business client and an ongoing negotiation.|Sales Advisor|High|
|RF-MAT-002|1.0|The system shall allow the sales advisor to<br>enter the services and products proposed to<br>the client, specifying quantities, unit prices,<br>totals, and observations as part of the ofer<br>matrix.|Sales Advisor<br>Continued o|High<br>n next page|



240 19 

**Table 5.5 (continued) – Offer Matrix Module (MAT)** 

|**ID**|**Version**|**Description**|**User / Role**|**Priority**|
|---|---|---|---|---|
|RF-MAT-003|1.0|The system shall automatically calculate<br>the applicable subsidy range based on<br>client billing and the number of proposed<br>services, displaying the total estimated<br>beneft amount.|Sales Advisor|High|
|RF-MAT-004|1.0|The system shall allow the sales advisor<br>to attach quotations or supporting fles in<br>PDF, Excel, JPG, or PNG formats up to 50<br>MB to the ofer matrix.|Sales Advisor|High|
|RF-MAT-005|1.0|The system shall allow the sales advisor<br>to save ofer matrices as drafts to edit<br>them before sending them to the immediate<br>supervisor for approval.|Sales Advisor|High|
|RF-MAT-006|1.0|The system shall allow the sales advisor<br>to send the ofer matrix to the immediate<br>supervisor for approval, changing its status<br>to “Pending Approval.”|Sales Advisor|High|
|RF-MAT-007|1.0|The<br>system<br>shall<br>allow<br>the<br>sales<br>advisor to consult the history of their<br>matrices, including creation date, status,<br>observations, and total subsidy amount.|Sales Advisor|High|



241 

20 

###### **5.2.3 Supervision and Approvals Module (SUP)** 

|**ID**|**Version**|**Description**|**User / Role**|**Priority**|
|---|---|---|---|---|
|RF-SUP-001|1.0|The system shall allow the immediate<br>supervisor to view the list of ofer matrices<br>pending approval.|Immediate<br>Supervisor|High|
|RF-SUP-002|1.0|The system shall allow the immediate<br>supervisor to review commercial indicators<br>such as billing, number of services, and<br>the calculated subsidy range for each ofer<br>matrix.|Immediate<br>Supervisor|High|
|RF-SUP-003|1.0|The system shall allow the immediate<br>supervisor to approve or reject ofer<br>matrices, recording a mandatory reason<br>in case of rejection.|Immediate<br>Supervisor|High|
|RF-SUP-004|1.0|The system shall allow the immediate<br>supervisor to view a history of ofer<br>matrices that have been approved or<br>rejected.|Immediate<br>Supervisor|High|
|RF-SUP-005|1.0|The system shall allow the sales advisor to<br>receive an internal notifcation and an email<br>with the result of the approval or rejection<br>of their matrix.|Sales Advisor|High|
|RF-SUP-006|1.0|The system shall allow the immediate<br>supervisor to flter matrices by advisor,<br>date, approval status, or subsidy range to<br>facilitate their review.|Immediate<br>Supervisor|High|



Table 5.6 Functional Requirements - Supervision and Approvals Module (SUP) 

242 21 

###### **5.2.4 Document Management Module (DOC)** 

Table 5.7 Functional Requirements - Document Management Module (DOC) 

|**ID**|**Version**|**Description**|**User / Role**|**Priority**|
|---|---|---|---|---|
|RF-DOC-001|1.0|The system shall allow the sales advisor<br>to attach documents related to negotiations<br>with assigned business clients.|Sales Advisor|High|
|RF-DOC-002|1.0|The system shall allow the sales advisor to<br>upload fles up to 50 MB in PDF, JPG, or<br>PNG formats.|Sales Advisor|High|
|RF-DOC-003|1.0|The system shall require the sales advisor to<br>label each uploaded document with its type<br>(e.g., “Provisional RUC,” “Initial Proposal,”<br>“Visit Report,” “Final Contract”).|Sales Advisor|High|
|RF-DOC-004|1.0|The system shall allow the coordinator to<br>defne mandatory or optional documents<br>depending on the type of service or<br>negotiation.|Coordinator|High|
|RF-DOC-005|1.0|The system shall allow the sales advisor to<br>check the documentation status during a<br>negotiation, displaying which fles have<br>been reviewed, approved, or are still<br>pending.|Sales Advisor|High|
|RF-DOC-006|1.0|The system shall allow the coordinator<br>to review documents uploaded by each<br>sales advisor related to negotiations with<br>business clients.|Coordinator|Medium|
||||Continued o|n next page|



243 

22 

**Table 5.7 (continued) – Document Management Module (DOC)** 

|**ID**|**Version**|**Description**|**User / Role**|**Priority**|
|---|---|---|---|---|
|RF-DOC-007|1.0|The system shall allow the coordinator to<br>download documents individually or in<br>bulk that are associated with a negotiation<br>for review.|Coordinator|Medium|
|RF-DOC-008|1.0|The system shall allow the sales advisor<br>to receive internal and email notifcations<br>when their documents have been reviewed,<br>approved, or rejected by the coordinator.|Sales Advisor|Medium|
|RF-DOC-009|1.0|The system shall allow the coordinator to<br>view a list of sales advisors with pending<br>document uploads or reviews.|Coordinator|Medium|



###### **5.2.5 Reporting Module (REP)** 

Table 5.8 Functional Requirements - Reporting Module (REP) 

|**ID**|**Version**|**Description**|**User / Role**|**Priority**|
|---|---|---|---|---|
|RF-REP-001|1.0|The system shall allow the manager to<br>generate commercial performance reports<br>by advisor, month, or period to evaluate<br>team productivity.|Manager|High|
|RF-REP-002|1.0|The system shall allow the immediate<br>supervisor to generate sales and closure<br>reports for the sales advisors under their<br>supervision, fltered by date, service type,<br>or zone.|Immediate<br>Supervisor|High|



|Continued on next page|
|---|



244 

23 

**Table 5.8 (continued) – Reporting Module (REP)** 

|**ID**|**Version**|**Description**|**User / Role**|**Priority**|
|---|---|---|---|---|
|RF-REP-003|1.0|The system shall allow the manager to view<br>key metrics such as sales, closures, visits,<br>and average negotiation time to assess<br>overall performance.|Manager|High|
|RF-REP-004|1.0|The system shall allow the immediate<br>supervisor to view operational metrics of<br>sales advisors, including sales, closures,<br>and visits made during a specifc period.|Immediate<br>Supervisor|High|
|RF-REP-005|1.0|The system shall allow the immediate<br>supervisor to compare the performance of<br>their sales advisors against the objectives<br>defned by management.|Immediate<br>Supervisor|Medium|
|RF-REP-006|1.0|The system shall allow the manager to<br>export generated reports in PDF or Excel<br>format for analysis or presentation.|Manager|Medium|
|RF-REP-007|1.0|The system shall allow the immediate<br>supervisor to export generated reports in<br>PDF or Excel format for review and follow-<br>up of commercial activities.|Immediate<br>Supervisor|Medium|
|RF-REP-008|1.0|The system shall allow the manager to<br>visualize consolidated information through<br>bar charts, line graphs, or KPI indicators<br>that facilitate interpretation of overall<br>results.|Manager|Medium|
||||Continued o|n next page|



245 

24 

**Table 5.8 (continued) – Reporting Module (REP)** 

|**ID**|**Version**|**Description**|**User / Role**|**Priority**|
|---|---|---|---|---|
|RF-REP-009|1.0|The system shall restrict access to reports<br>according to user roles so that each user<br>only views the information corresponding<br>to their access level.|System|High|
|RF-REP-010|1.0|The<br>system<br>shall<br>allow<br>the<br>sales<br>advisor to view their own commercial<br>performance, including the number of<br>clients contacted,<br>active negotiations,<br>closures, and accumulated billing.|Sales Advisor|High|



###### **5.2.6 Basic Security Module (SEG)** 

|**ID**|**Version**|**Description**|**User / Role**|**Priority**|
|---|---|---|---|---|
|RF-SEG-001|1.0|The system shall require authentication<br>using a valid username and password to<br>allow access to the internal application.|System|High|
|RF-SEG-002|1.0|The system shall assign permissions<br>and restrict functionalities according to<br>the user’s role (Manager,<br>Immediate<br>Supervisor, Sales Advisor, Coordinator,<br>Web Administrator).|System|High|
|RF-SEG-003|1.0|The system shall ensure that users with the<br>Manager role inherit the access privileges<br>of the Immediate Supervisor role.|System|High|



Table 5.9 Functional Requirements - Basic Security Module (SEG) 

246 

25 

###### **5.2.7 Notifications Module (NOT)** 

|**ID**|**Version**|**Description**|**User / Role**|**Priority**|
|---|---|---|---|---|
|RF-NOT-001|1.0|The system shall send internal and email<br>notifcations to users when relevant events<br>occur, such as approvals, rejections, or<br>document reviews.|System|High|
|RF-NOT-002|1.0|The system shall allow each user to view a<br>history of received notifcations within the<br>application.|System|High|



Table 5.10 Functional Requirements - Notifications Module (NOT) 

247 

###### **CHAPTER 6** 

###### **NON-FUNCTIONAL REQUIREMENTS** 

This section specifies the non-functional requirements of the BOPADIGITAL system, which define the quality attributes, constraints, and performance characteristics that the software must meet. Unlike functional requirements, these requirements do not describe specific system behaviors but rather establish the standards and conditions under which the system operates effectively. 

The non-functional requirements ensure that the BOPADIGITAL platform is reliable, secure, efficient, and user-friendly. They address key aspects such as usability, performance, scalability, maintainability, availability, security, and compliance with organizational and technological constraints. 

These requirements apply to both components of the system, the public website and the internal application (web and mobile), ensuring a consistent user experience, operational stability, and compliance with industry best practices. Each non-functional requirement contributes to the overall quality and sustainability of the system throughout its lifecycle. 

248 

27 

Table 6.1 Non-Functional Requirements - BOPADIGITAL System 

|**ID**|**Version**|**Description**|**Validation**<br>**Criterion**|**Priority**|
|---|---|---|---|---|
|RNF-001|1.0|The system shall guarantee a response<br>time below 3 seconds for any user action<br>under a load of up to 50 concurrent<br>users.<br>(Category: Product – Efciency<br>– Performance)|Performance<br>and<br>stress<br>testing<br>with<br>JMeter<br>or<br>equivalent<br>shows ≤3s<br>response time<br>with 50 users.|High|
|RNF-002|1.0|The platform shall ensure at least 99%<br>monthly availability during business hours<br>(08h00–20h00).<br>(Category:<br>Product –<br>Dependability – Availability)|Server<br>logs<br>and<br>uptime<br>reports<br>confrm<br>≥<br>99%<br>availability.|High|
|RNF-003|1.0|The system shall support scaling from 7 to<br>25 concurrent advisors without afecting<br>response time.<br>(Category:<br>Product –<br>Efciency – Performance)|Load<br>test<br>results<br>confrm<br>stability<br>under<br>25<br>simultaneous<br>users.|Medium|



Continued on next page 

249 

28 

**Table 6.1 (continued) – Non-Functional Requirements** 

|**ID**|**Version**|**Description**|**Validation**<br>**Criterion**|**Priority**|
|---|---|---|---|---|
|RNF-004|1.0|User passwords shall be hashed using<br>bcrypt with random salt and at least 12<br>characters. (Category: Product – Security)|Code<br>audit<br>confrms<br>bcrypt usage<br>and required<br>length.|High|
|RNF-005|1.0|All communication between client and<br>server shall use HTTPS with TLS 1.3<br>encryption. (Category: Product – Security)|SSL<br>certifcate<br>and<br>server<br>confguration<br>inspection.|High|
|RNF-006|1.0|The mobile app shall work correctly on<br>Android 10–16 and iOS 13–16.1; the web<br>version shall be compatible with Chrome,<br>Firefox, and Edge. (Category: Product –<br>Usability)|Cross-device<br>and<br>cross-<br>browser<br>compatibility<br>tests.|High|
|RNF-007|1.0|The interface shall remain responsive from<br>360 px to 1440 px width and meet WCAG<br>2.1 AA accessibility. (Category: Product –<br>Usability)|Visual<br>inspection<br>and<br>accessibility<br>validation.|High|
|RNF-008|1.0|The system shall log all critical events<br>(logins, uploads, approvals, rejections) with<br>timestamp and user. (Category: Product –<br>Security)|Audit<br>log<br>verifcation.|High|
||||Continued o|n next page|



250 

29 

**Table 6.1 (continued) – Non-Functional Requirements** 

|**ID**|**Version**|**Description**|**Validation**<br>**Criterion**|**Priority**|
|---|---|---|---|---|
|RNF-009|1.0|Uploaded fles shall be validated by<br>extension (PDF, JPG, PNG, XLSX) and<br>limited to 50 MB. (Category: Product –<br>Efciency – Space)|Upload<br>and<br>validation test<br>results.|High|
|RNF-010|1.0|The system shall perform daily automated<br>database backups for disaster recovery.<br>(Category: Organizational – Operational)|Backup<br>and<br>restore<br>verifcation.|Medium|
|RNF-011|1.0|The source code shall comply with OWASP<br>Top 10 security standards.<br>(Category:<br>Organizational – Development)|Static<br>code<br>analysis<br>and<br>linting<br>validation.|High|
|RNF-012|1.0|The system shall follow an MVC client-<br>server architecture with logical separation<br>of layers.<br>(Category: Organizational –<br>Development)|Design<br>and<br>folder<br>structure<br>review.|Medium|
|RNF-013|1.0|User data shall comply with Ecuador’s<br>Personal Data Protection Law (2021).<br>(Category: External – Legislative)|Legal<br>audit<br>and<br>policy<br>review.|High|
|RNF-014|1.0|Uploaded documents shall be encrypted<br>with AES-256 both in transit and at rest.<br>(Category: Product – Security)|Hosting<br>confguration<br>and<br>encryption<br>validation.|High|
||||Continued o|n next page|



251 

30 

**Table 6.1 (continued) – Non-Functional Requirements** 

|**ID**|**Version**|**Description**|**Validation**<br>**Criterion**|**Priority**|
|---|---|---|---|---|
|RNF-015|1.0|Error messages shall be in Spanish, identify<br>the failing module, and hide technical<br>details. (Category: Product – Usability)|Interface<br>inspection<br>and<br>error<br>testing.|Medium|
|RNF-016|1.0|The system shall ensure data consistency<br>during concurrent writes, avoiding race<br>conditions.<br>(Category:<br>Product<br>–<br>Dependability – Reliability)|Concurrent<br>operation<br>testing<br>confrms<br>integrity.|High|
|RNF-017|1.0|Critical operations (approvals, activations,<br>uploads) shall be recorded in an audit<br>log with user, action, and timestamp.<br>(Category: Product – Security)|Database<br>traceability<br>verifcation.|High|
|RNF-018|1.0|Forms shall validate input on client and<br>server sides with clear feedback and prevent<br>duplicates. (Category: Product – Usability)|Validation<br>tests<br>with<br>incorrect<br>inputs.|High|
|RNF-019|1.0|The application shall run continuously for<br>at least 8 hours without restart. (Category:<br>Product – Dependability – Availability)|Endurance<br>testing<br>demonstrates<br>≥8 h stability.|High|
||||Continued o|n next page|



252 

31 

**Table 6.1 (continued) – Non-Functional Requirements** 

|**ID**|**Version**|**Description**|**Validation**<br>**Criterion**|**Priority**|
|---|---|---|---|---|
|RNF-020|1.0|All components shall include technical<br>documentation and comments in standard<br>format.<br>(Category:<br>Organizational –<br>Development)|Code<br>and<br>documentation<br>review.|Medium|
|RNF-021|1.0|Unit tests shall cover at least 80% of<br>critical code. (Category: Organizational –<br>Development)|Test coverage<br>report review.|Medium|
|RNF-022|1.0|System updates shall not exceed 15 minutes<br>of downtime. (Category: Organizational –<br>Operational)|Controlled<br>deployment<br>and downtime<br>logging.|Medium|
|RNF-023|1.0|Personal data shall be anonymized in testing<br>and development environments. (Category:<br>External – Legislative)|Database<br>audit ensures<br>anonymization.|High|
|RNF-024|1.0|Sessions shall expire after 15 minutes<br>of inactivity, requiring reauthentication.<br>(Category: Product – Security)|Inactivity<br>test confrms<br>session<br>timeout.|High|
|RNF-025|1.0|The system shall restore databases from<br>backups without interrupting ongoing<br>operations.<br>(Category:<br>Product<br>–<br>Dependability)|Recovery<br>testing<br>with<br>data<br>validation.|Medium|
||||Continued on|next page|



253 

32 

**Table 6.1 (continued) – Non-Functional Requirements** 

|**ID**|**Version**|**Description**|**Validation**<br>**Criterion**|**Priority**|
|---|---|---|---|---|
|RNF-026|1.0|Only authenticated users may access API|Token|High|
|||endpoints through JWT tokens with 15-|authentication||
|||minute expiration. (Category: Product –|and||
|||Security)|expiration<br>tests.||



254 

###### **CHAPTER 7** 

###### **USER STORIES** 

This section presents the user stories defined for the BOPADIGITAL system. Each story describes, in concise and user-centered terms, the specific goals, motivations, and expected outcomes of the main actors interacting with the system. These user stories were derived from the functional requirements, stakeholder interviews, and the analysis of the company’s business processes. 

The user stories are organized by modules that correspond to the main subsystems of BOPADIGITAL, ensuring consistency with the system architecture and requirements traceability. Each module groups the stories related to a particular functional area, covering both the public website and the internal application (web and mobile). 

This modular organization allows a clear understanding of the system from the user’s perspective and facilitates the transition to subsequent stages of design, development, and testing. 

###### **7.1 Service Catalog and Website Module (CAT)** 

###### **HU-CAT-001** 

###### **Related Requirement:** RF-CAT-001 

###### **Actor:** Business Client 

**User Story:** As a business client, I want to explore a catalog of products and services organized by categories such as Voice, Connectivity, and Digital Services, so that I can easily find the solutions offered by BOPACORP. 

###### **Acceptance Criteria:** 

- The catalog displays the main categories and available subcategories. 

- The user can navigate between categories without errors. 

- Each category loads its list of services in less than 3 seconds. 

255 

34 

###### **HU-CAT-002** 

###### **Related Requirement:** RF-CAT-002 

###### **Actor:** Business Client 

**User Story:** As a business client, I want to view the costs, benefits, and usage conditions of 

each service, so I can compare options and choose the one that best suits my company. 

###### **Acceptance Criteria:** 

- Each catalog service displays its cost, benefits, and conditions. 

- Information is clearly visible on the website. 

- Services without complete information are not allowed. 

###### **HU-CAT-003** 

###### **Related Requirement:** RF-CAT-003 

###### **Actor:** Business Client 

**User Story:** As a business client, I want to filter services by category, coverage, and price to quickly find the options that meet my needs. 

###### **Acceptance Criteria:** 

- Results update dynamically according to the selected filters. 

- Filters can be combined simultaneously. 

###### **HU-CAT-004** 

###### **Related Requirement:** RF-CAT-004 

###### **Actor:** Business Client 

**User Story:** As a business client, I want to contact a sales advisor directly from the catalog to 

request more information or start a negotiation. 

###### **Acceptance Criteria:** 

- The contact function is available for each listed service. 

- The system processes the contact request successfully. 

- The user receives confirmation of their request. 

256 

35 

###### **HU-CAT-005** 

###### **Related Requirement:** RF-CAT-005 

###### **Actor:** Business Client 

**User Story:** As a business client, I want to learn about BOPACORP’s history, mission, vision, 

and values to better understand the company’s philosophy and reliability. 

###### **Acceptance Criteria:** 

- A “About Us” section is accessible from the main menu. 

- History, mission, vision, and values are displayed correctly. 

- Content is viewable on both desktop and mobile. 

###### **7.2 Content Management Module (CMS)** 

###### **HU-CMS-001** 

###### **Related Requirement:** RF-CMS-001 

###### **Actor:** Web Administrator 

**User Story:** As a web administrator, I want to access the content management panel using 

credentials (username and password), so that I can control editing operations on the website. 

###### **Acceptance Criteria:** 

- The system requests valid credentials before granting access to the panel. 

- Only users with the Web Administrator role can log in. 

- Unauthorized access attempts display an error message. 

###### **HU-CMS-002** 

###### **Related Requirement:** RF-CMS-002 

###### **Actor:** Web Administrator 

**User Story:** As a web administrator, I want to modify texts, images, and links of the published 

content to keep the website’s information accurate and up to date. 

###### **Acceptance Criteria:** 

- All modifications are saved and made available for publication. 

- The system validates file types and sizes before accepting the modification. 

257 

36 

###### **HU-CMS-003** 

###### **Related Requirement:** RF-CMS-003 

###### **Actor:** Web Administrator 

**User Story:** As a web administrator, I want to register new products and services in the catalog to expand the range of offerings available to business clients. 

###### **Acceptance Criteria:** 

- Mandatory fields include name, description, category, and price. 

- The entered data are correctly stored and available for review. 

###### **HU-CMS-004** 

###### **Related Requirement:** RF-CMS-004 

###### **Actor:** Web Administrator 

**User Story:** As a web administrator, I want to update existing product or service information in the catalog to reflect changes in prices, benefits, or conditions. 

###### **Acceptance Criteria:** 

- Every update is recorded with the date and responsible user. 

- The system preserves data integrity after each modification. 

###### **HU-CMS-005** 

###### **Related Requirement:** RF-CMS-005 

###### **Actor:** Web Administrator 

**User Story:** As a web administrator, I want to delete outdated products or services from the catalog to ensure that only current offers are visible and avoid confusion for users. 

###### **Acceptance Criteria:** 

- The system must request explicit confirmation from the administrator before permanent deletion. 

- Once confirmed, the deleted service must no longer appear in the public catalog (verified by a Business Client). 

258 

37 

- The deleted service must also be removed from the active services list in the Content Management Module (CMS). 

###### **7.3 Employability and Application Module (EMP)** 

###### **HU-EMP-001** 

###### **Related Requirement:** RF-EMP-001 

**Actor:** Sales Advisor Candidate 

**User Story:** As a sales advisor candidate, I want to view the available job vacancies with their descriptions and requirements so that I can identify opportunities that fit my professional profile. 

###### **Acceptance Criteria:** 

- The system displays active vacancies with complete information: position title, requirements, description, and publication date. 

- Only valid (non-expired) vacancies are shown. 

- The candidate can access the details of each vacancy without authentication. 

###### **HU-EMP-002** 

###### **Related Requirement:** RF-EMP-002 

**Actor:** Sales Advisor Candidate 

**User Story:** As a sales advisor candidate, I want to enter my personal and contact information 

in an application form so that I can formally apply to an open vacancy. 

###### **Acceptance Criteria:** 

- The form requests defined mandatory fields (name, ID, email, phone, etc.). 

- Entered data are stored correctly in the system. 

- The application is associated with a specific vacancy. 

###### **HU-EMP-003** 

###### **Related Requirement:** RF-EMP-003 

###### **Actor:** Sales Advisor Candidate 

**User Story:** As a sales advisor candidate, I want to upload my resume (CV) in PDF format so 

259 

38 

that my professional information is included in the application process. 

###### **Acceptance Criteria:** 

- The system accepts PDF files only. 

- The file size complies with the defined maximum limit. 

- The uploaded CV is stored together with the corresponding application. 

###### **HU-EMP-004** 

###### **Related Requirement:** RF-EMP-004 

**Actor:** Sales Advisor Candidate 

**User Story:** As a sales advisor candidate, I want the system to validate that all required fields 

are complete before submission so that my application is processed correctly. 

###### **Acceptance Criteria:** 

- The application cannot be submitted if any required fields are missing. 

- The system displays validation messages indicating incomplete fields. 

- Submission is allowed only when all validations pass. 

###### **HU-EMP-005** 

###### **Related Requirement:** RF-EMP-005 

###### **Actor:** Sales Advisor Candidate 

**User Story:** As a sales advisor candidate, I want to receive visual and email confirmation when 

my application is submitted so that I have proof that the process was completed successfully. 

###### **Acceptance Criteria:** 

- Upon submission, the system records the application successfully. 

- The candidate receives an in-app notification and a confirmation email. 

- The submission date and time are recorded. 

###### **HU-EMP-006** 

###### **Related Requirement:** RF-EMP-006 

**Actor:** Sales Advisor Candidate 

260 39 

**User Story:** As a sales advisor candidate, I want to receive the result of my application by email so that I know whether I was accepted or rejected. 

###### **Acceptance Criteria:** 

- The applicant is notified of the application result via email. 

###### **7.4 Client Management Module (CRM)** 

###### **HU-CRM-001** 

###### **Related Requirement:** RF-CRM-001 

###### **Actor:** Sales Advisor 

**User Story:** As a sales advisor, I want to register new business clients with their RUC, name, 

number of services, and monthly billing, so that I can start tracking their negotiations. 

###### **Acceptance Criteria:** 

- The system requires mandatory fields (RUC, name, services, billing). 

- The information is stored correctly. 

- Created records are associated with the responsible advisor. 

###### **HU-CRM-002** 

###### **Related Requirement:** RF-CRM-002 

###### **Actor:** Sales Advisor 

**User Story:** As a sales advisor, I want to update the data of my assigned clients to keep accurate information during the negotiation process. 

###### **Acceptance Criteria:** 

- The system allows modifying only clients assigned to the advisor. 

- After saving, the updated information persists and is visible to the Sales Advisor, Immediate Supervisor, and Management Staff. 

###### **HU-CRM-003** 

###### **Related Requirement:** RF-CRM-003 

**Actor:** Sales Advisor 

261 

40 

**User Story:** As a sales advisor, I want to search and filter my clients by negotiation stage or visit date so that I can prioritize my commercial follow-up. 

###### **Acceptance Criteria:** 

- The results correspond only to the advisor’s clients. 

- Filters can be combined. 

###### **HU-CRM-004** 

###### **Related Requirement:** RF-CRM-004 

###### **Actor:** Sales Advisor 

**User Story:** As a sales advisor, I want to plan on-site visits to my assigned clients to organize my schedule and maintain continuity in the sales process. 

###### **Acceptance Criteria:** 

- The advisor can register the date, time, and client for each planned visit. 

- Visits are stored for later consultation. 

###### **HU-CRM-005** 

###### **Related Requirement:** RF-CRM-005 

**Actor:** Immediate Supervisor 

**User Story:** As an immediate supervisor, I want to view the location recorded by advisors 

during each visit to verify the validity of reported activities. 

###### **Acceptance Criteria:** 

- The supervisor can view the location of past visits. 

- The information includes coordinates and client details. 

###### **HU-CRM-006** 

###### **Related Requirement:** RF-CRM-006 

###### **Actor:** Sales Advisor 

**User Story:** As a sales advisor, I want to consult the history of visits made to analyze my client 

262 41 

follow-up over time. 

###### **Acceptance Criteria:** 

- The history lists all visits made by the advisor. 

- Each record includes date, time, observations, and client. 

- The information can be sorted chronologically. 

###### **HU-CRM-007** 

###### **Related Requirement:** RF-CRM-007 

**Actor:** Sales Advisor 

**User Story:** As a sales advisor, I want to update the negotiation status of my clients to reflect progress in the commercial process. 

###### **Acceptance Criteria:** 

- The system allows selecting valid stages (prospecting, negotiation, closing, post-sale). 

- Each change is recorded with date and user. 

- Only the responsible advisor can modify the status. 

###### **HU-CRM-008** 

###### **Related Requirement:** RF-CRM-008 

**Actor:** Immediate Supervisor 

**User Story:** As an immediate supervisor, I want to register new business clients to include them 

in the system and assign them to available advisors. 

###### **Acceptance Criteria:** 

- The form includes RUC, name, services, and billing fields. 

- Registered clients remain unassigned initially. 

- Only users with the Immediate Supervisor role can perform this action. 

###### **HU-CRM-009** 

###### **Related Requirement:** RF-CRM-009 

**Actor:** Immediate Supervisor 

263 42 

**User Story:** As an immediate supervisor, I want to update information about business clients to correct or maintain company records up to date. 

###### **Acceptance Criteria:** 

- The supervisor can edit any business client record. 

- Each update is logged with date and user. 

- Updated data are reflected in real time. 

###### **HU-CRM-010** 

###### **Related Requirement:** RF-CRM-010 

**Actor:** Immediate Supervisor 

**User Story:** As an immediate supervisor, I want to deactivate business clients to prevent the use 

of inactive or outdated records. 

###### **Acceptance Criteria:** 

- The system allows setting a client status to “Inactive.” 

- Inactive clients do not appear in active searches. 

- The supervisor can revert the status if necessary. 

###### **HU-CRM-011** 

###### **Related Requirement:** RF-CRM-011 

**Actor:** Immediate Supervisor 

**User Story:** As an immediate supervisor, I want to assign business clients to sales advisors to distribute the workload efficiently. 

###### **Acceptance Criteria:** 

- The supervisor selects the advisor and client for assignment. 

- Assigned clients are immediately linked to the advisor. 

- The system prevents duplicate assignments. 

###### **HU-CRM-012** 

**Related Requirement:** RF-CRM-012 

264 

43 

**Actor:** Immediate Supervisor 

**User Story:** As an immediate supervisor, I want to view the list of clients assigned to each 

advisor to monitor each team member’s portfolio. 

###### **Acceptance Criteria:** 

- The list displays clients and their negotiation status. 

- It can be filtered by advisor. 

- The data update in real time. 

###### **HU-CRM-013** 

###### **Related Requirement:** RF-CRM-013 

**Actor:** Immediate Supervisor 

**User Story:** As an immediate supervisor, I want to reassign or remove clients from a sales 

advisor to redistribute them when necessary. 

###### **Acceptance Criteria:** 

- The supervisor can remove the link between advisor and client. 

- All changes are recorded with date and reason. 

###### **HU-CRM-014** 

###### **Related Requirement:** RF-CRM-014 

**Actor:** Immediate Supervisor 

**User Story:** As an immediate supervisor, I want to review recent activity from sales advisors to 

evaluate their compliance with visits and record keeping. 

###### **Acceptance Criteria:** 

- The system displays the latest activity from each advisor. 

- Each record includes action type, date, and affected client. 

###### **HU-CRM-015** 

###### **Related Requirement:** RF-CRM-015 

**Actor:** Management 

265 44 

**User Story:** As management, I want to view contact, visit, and closure indicators per advisor to evaluate team performance. 

###### **Acceptance Criteria:** 

- The system displays the number of clients contacted, visited, and closed. 

- Data are grouped by advisor and updated in real time. 

###### **HU-CRM-016** 

###### **Related Requirement:** RF-CRM-016 

**Actor:** Management 

**User Story:** As management, I want to view total billed amounts and averages per service for each advisor to measure commercial efficiency. 

###### **Acceptance Criteria:** 

- The system consolidates billed amounts per advisor. 

- The average billing per service is calculated automatically. 

###### **HU-CRM-017** 

###### **Related Requirement:** RF-CRM-017 

**Actor:** Management 

**User Story:** As management, I want to view the total terminals and equipment sold by each 

advisor to analyze complementary sales. 

###### **Acceptance Criteria:** 

- The system displays the number and total value of equipment sold. 

- Information is grouped by advisor and based on confirmed records. 

###### **HU-CRM-018** 

###### **Related Requirement:** RF-CRM-018 

**Actor:** Management 

**User Story:** As management, I want to view the number of clients at each stage of the sales 

266 

45 

funnel to identify opportunities and bottlenecks. 

###### **Acceptance Criteria:** 

- The system groups clients by funnel stage (prospecting, negotiation, closing, post-sale). 

- Data can be filtered by advisor. 

- Visualization reflects the most current state. 

###### **HU-CRM-019** 

###### **Related Requirement:** RF-CRM-019 

**Actor:** Immediate Supervisor 

**User Story:** As an immediate supervisor, I want to search and filter clients by negotiation stage, visit date, or assigned advisor to follow up in an organized way. 

###### **Acceptance Criteria:** 

- Filters include stage, date, and advisor. 

- Results are displayed according to the selected criteria. 

- Only active clients are shown. 

###### **HU-CRM-020** 

###### **Related Requirement:** RF-CRM-020 

**Actor:** Sales Advisor 

**User Story:** As a sales advisor, I want to view the clients assigned to me immediately to provide timely follow-up. 

###### **Acceptance Criteria:** 

- The advisor can only view assigned clients. 

- Selecting a client loads the detailed client information view successfully. 

###### **HU-CRM-021** 

###### **Related Requirement:** RF-CRM-021 

**Actor:** Immediate Supervisor 

**User Story:** As an immediate supervisor, I want to consult the change history made by each 

267 

46 

advisor on their clients to maintain control over modifications. 

###### **Acceptance Criteria:** 

- The system keeps a record of all changes made by advisors. 

- Each record includes user, date, modified field, and previous value. 

- The history is accessible only to immediate supervisors. 

###### **7.5 Offer Matrix Module (MAT)** 

###### **HU-MAT-001** 

###### **Related Requirement:** RF-MAT-001 

###### **Actor:** Sales Advisor 

**User Story:** As a sales advisor, I want to create a new offer matrix associated with a client and 

an active negotiation so that I can record the proposed sales conditions. 

###### **Acceptance Criteria:** 

- The created matrix is automatically associated with both the client and the negotiation. 

- The record is saved with the date and responsible user. 

###### **HU-MAT-002** 

###### **Related Requirement:** RF-MAT-002 

###### **Actor:** Sales Advisor 

**User Story:** As a sales advisor, I want to enter the offered products and services, specifying 

quantity, unit prices, totals, and observations so that I can properly structure the commercial proposal. 

###### **Acceptance Criteria:** 

- Each catalog service displays its cost, benefits, and conditions. 

- The information is clearly visible on the interface. 

- Incomplete services cannot be registered in the matrix. 

###### **HU-MAT-003** 

###### **Related Requirement:** RF-MAT-003 

268 

47 

###### **Actor:** Sales Advisor 

**User Story:** As a sales advisor, I want the system to automatically calculate the applicable subsidy based on the client’s billing and number of proposed services, to estimate the total benefit for the client. 

###### **Acceptance Criteria:** 

- The calculated subsidy value is displayed within the matrix. 

- The calculation is reproducible and verifiable in test conditions. 

###### **HU-MAT-004** 

###### **Related Requirement:** RF-MAT-004 

###### **Actor:** Sales Advisor 

**User Story:** As a sales advisor, I want to attach quotations or complementary files to my offer matrix to support the proposal with additional documentation. 

###### **Acceptance Criteria:** 

- The system accepts files in PDF, Excel, JPG, or PNG format. 

- The maximum allowed size per file is 50 MB. 

- Uploaded documents are linked to the matrix and available for download. 

###### **HU-MAT-005** 

###### **Related Requirement:** RF-MAT-005 

###### **Actor:** Sales Advisor 

**User Story:** As a sales advisor, I want to save my offer matrices as drafts so that I can review 

and complete them before submitting them for approval. 

###### **Acceptance Criteria:** 

- Draft matrices can be reopened and edited by the advisor. 

- Drafts are not visible to the immediate supervisor until submission. 

###### **HU-MAT-006** 

###### **Related Requirement:** RF-MAT-006 

269 

48 

###### **Actor:** Sales Advisor 

**User Story:** As a sales advisor, I want to send the offer matrix to my immediate supervisor for approval so that the proposal can be formalized and negotiation can continue. 

###### **Acceptance Criteria:** 

- The matrix status automatically changes to “Pending Approval.” 

- The immediate supervisor receives a notification upon submission. 

- The advisor can no longer modify the matrix after sending it. 

###### **HU-MAT-007** 

###### **Related Requirement:** RF-MAT-007 

###### **Actor:** Sales Advisor 

**User Story:** As a sales advisor, I want to consult the history of my created matrices so that I can 

review their status, observations, and associated subsidy amounts. 

###### **Acceptance Criteria:** 

- The history displays the creation date, total amount, and observations. 

- Previous versions are preserved for audit purposes. 

###### **7.6 Supervision and Approvals Module (SUP)** 

###### **HU-SUP-001** 

###### **Related Requirement:** RF-SUP-001 

###### **Actor:** Immediate Supervisor 

**User Story:** As an immediate supervisor, I want to view all offer matrices pending approval so 

that I can prioritize those that require review and avoid delays in the commercial process. 

###### **Acceptance Criteria:** 

- The system displays only matrices with the status “Pending Approval.” 

- Essential data are shown: client, advisor, submission date, and total amount. 

- The information updates automatically when new matrices are added. 

270 

49 

###### **HU-SUP-002** 

###### **Related Requirement:** RF-SUP-002 

**Actor:** Immediate Supervisor 

**User Story:** As an immediate supervisor, I want to consult the commercial indicators of each matrix, including billing, number of services, and subsidy range, to objectively evaluate each proposal before making a decision. 

###### **Acceptance Criteria:** 

- The system displays billing, number of services, and calculated subsidy indicators. 

- The displayed values match the data from the original matrix. 

- The supervisor cannot modify this information. 

###### **HU-SUP-003** 

###### **Related Requirement:** RF-SUP-003 

**Actor:** Immediate Supervisor 

**User Story:** As an immediate supervisor, I want to approve or reject offer matrices, entering a 

reason in case of rejection, to maintain a clear record of all decisions made. 

###### **Acceptance Criteria:** 

- The supervisor can change the matrix status to “Approved” or “Rejected.” 

- In case of rejection, the system requires entering a mandatory reason. 

- Each decision is recorded with date, time, and user. 

###### **HU-SUP-004** 

###### **Related Requirement:** RF-SUP-004 

**Actor:** Immediate Supervisor 

**User Story:** As an immediate supervisor, I want to access a history of approved or rejected 

matrices so that I can review previous decisions and facilitate audits or follow-ups. 

###### **Acceptance Criteria:** 

- The system stores approval and rejection decisions with their details. 

- The history includes date, user, client, and advisor involved. 

271 50 

- Records cannot be modified once generated. 

###### **HU-SUP-005** 

###### **Related Requirement:** RF-SUP-005 

**Actor:** Sales Advisor 

**User Story:** As a sales advisor, I want to receive a notification when my matrix is approved or rejected so that I can know the review outcome and proceed accordingly. 

###### **Acceptance Criteria:** 

- The system sends both an internal and email notification to the advisor. 

- The message includes the result (approved or rejected) and, if applicable, the rejection reason. 

- Notifications are recorded in the advisor’s history. 

###### **HU-SUP-006** 

###### **Related Requirement:** RF-SUP-006 

**Actor:** Immediate Supervisor 

**User Story:** As an immediate supervisor, I want to filter matrices by advisor, date, status, or 

subsidy range to make searching and analysis easier during the review process. 

###### **Acceptance Criteria:** 

- Filters allow combining multiple criteria (advisor, date, status, subsidy). 

- The displayed results exactly match the selected filters. 

- The supervisor can clear or modify filters at any time. 

###### **7.7 Document Management Module (DOC)** 

###### **HU-DOC-001** 

###### **Related Requirement:** RF-DOC-001 

**Actor:** Sales Advisor 

**User Story:** As a sales advisor, I want to attach documents related to my negotiations so that I can support the commercial process and facilitate its review. 

###### **Acceptance Criteria:** 

272 51 

- The advisor can select an active negotiation and attach the corresponding documents. 

- Documents are associated with the correct client and negotiation. 

- The system records the upload date, time, and responsible user. 

###### **HU-DOC-002** 

###### **Related Requirement:** RF-DOC-002 

###### **Actor:** Sales Advisor 

**User Story:** As a sales advisor, I want to upload files up to 50 MB in PDF, JPG, or PNG formats to ensure that the required documentation is sent in compatible formats. 

###### **Acceptance Criteria:** 

- The system validates file formats (PDF, JPG, PNG). 

- Files exceeding 50 MB are not accepted. 

- Valid files are stored correctly in the system. 

###### **HU-DOC-003** 

###### **Related Requirement:** RF-DOC-003 

###### **Actor:** Sales Advisor 

**User Story:** As a sales advisor, I want to label each uploaded document with its corresponding 

type to maintain a clear organization of each client’s documentation. 

###### **Acceptance Criteria:** 

- The system requires selecting a label type (“Provisional RUC,” “Initial Proposal,” “Visit Report,” “Final Contract”). 

- The label is recorded together with the document. 

- Documents can later be filtered by type. 

###### **HU-DOC-004** 

###### **Related Requirement:** RF-DOC-004 

###### **Actor:** Coordinator 

**User Story:** As a coordinator, I want to define which documents are mandatory or optional 

273 52 

depending on the type of service so that negotiation requirements are standardized. 

###### **Acceptance Criteria:** 

- The coordinator can mark documents as “mandatory” or “optional.” 

- The system enforces the corresponding rules based on service or negotiation type. 

- Advisors can see which documents must be uploaded before closing a negotiation. 

###### **HU-DOC-005** 

###### **Related Requirement:** RF-DOC-005 

###### **Actor:** Sales Advisor 

**User Story:** As a sales advisor, I want to check the status of uploaded documents so that I know which ones have been reviewed, approved, or are still pending. 

###### **Acceptance Criteria:** 

- The system displays the current status of each document (Pending, Approved, Rejected). 

- Statuses update automatically according to the coordinator’s actions. 

- The advisor can consult this information from their account at any time. 

###### **HU-DOC-006** 

###### **Related Requirement:** RF-DOC-006 

###### **Actor:** Coordinator 

**User Story:** As a coordinator, I want to review the documents uploaded by each sales advisor to 

verify compliance with documentation requirements. 

###### **Acceptance Criteria:** 

- The system lists documents grouped by advisor and negotiation. 

- Each record displays document type, upload date, and status. 

- Only coordinators have access to this view. 

###### **HU-DOC-007** 

###### **Related Requirement:** RF-DOC-007 

**Actor:** Coordinator 

274 53 

**User Story:** As a coordinator, I want to download negotiation documents individually or in bulk so that I can review and store the information more efficiently. 

###### **Acceptance Criteria:** 

- The system allows downloading a specific document or all negotiation files. 

- Files are preserved in their original format. 

- A record of downloads is kept in the system. 

###### **HU-DOC-008** 

###### **Related Requirement:** RF-DOC-008 

**Actor:** Sales Advisor 

**User Story:** As a sales advisor, I want to receive a notification when my documents are reviewed, 

approved, or rejected so that I can track the validation progress. 

###### **Acceptance Criteria:** 

- The system sends both an internal notification and an email to the advisor. 

- The message includes the result of the review and any comments. 

- The notification is stored in the user’s history. 

###### **HU-DOC-009** 

###### **Related Requirement:** RF-DOC-009 

###### **Actor:** Coordinator 

**User Story:** As a coordinator, I want to view a list of advisors with pending document uploads 

or reviews so that I can prioritize cases that require follow-up. 

###### **Acceptance Criteria:** 

- The system generates a list of advisors with pending documentation. 

- The list includes associated clients and missing document types. 

- The list updates automatically as uploads are completed. 

275 54 

###### **7.8 Reporting Module (REP)** 

###### **HU-REP-001** 

###### **Related Requirement:** RF-REP-001 

###### **Actor:** Manager 

**User Story:** As a manager, I want to generate commercial performance reports by advisor, 

month, or period so that I can evaluate team productivity and identify areas for improvement. 

###### **Acceptance Criteria:** 

- Reports include metrics such as sales, closures, and billing. 

- Generated data correspond to the selected period. 

###### **HU-REP-002** 

###### **Related Requirement:** RF-REP-002 

###### **Actor:** Immediate Supervisor 

**User Story:** As an immediate supervisor, I want to generate sales and closure reports for the advisors under my supervision, filtering by date, service type, or zone, to conduct detailed performance tracking. 

###### **Acceptance Criteria:** 

- Results include only advisors under the supervisor’s responsibility. 

- Reports display total sales and closures by advisor. 

###### **HU-REP-003** 

###### **Related Requirement:** RF-REP-003 

###### **Actor:** Manager 

**User Story:** As a manager, I want to visualize key metrics such as sales, closures, visits, and 

average negotiation time to measure the overall performance of the sales force. 

###### **Acceptance Criteria:** 

- The system calculates and presents the mentioned metrics. 

- Values are automatically updated based on registered data. 

276 55 

- Information is consolidated by period or defined range. 

###### **HU-REP-004** 

###### **Related Requirement:** RF-REP-004 

**Actor:** Immediate Supervisor 

**User Story:** As an immediate supervisor, I want to view operational metrics of the advisors, 

including sales, closures, and visits made, to monitor their commercial performance. 

###### **Acceptance Criteria:** 

- Data correspond to the selected period. 

- Only advisors under the supervisor’s direct supervision are displayed. 

###### **HU-REP-005** 

###### **Related Requirement:** RF-REP-005 

**Actor:** Immediate Supervisor 

**User Story:** As an immediate supervisor, I want to compare the performance of my advisors against the objectives defined by management so that I can identify deviations and take corrective actions. 

###### **Acceptance Criteria:** 

- The system compares actual metrics with defined objectives. 

- The percentage of compliance for each advisor is displayed. 

- Data update automatically based on registered metrics. 

###### **HU-REP-006** 

###### **Related Requirement:** RF-REP-006 

**Actor:** Manager 

**User Story:** As a manager, I want to export generated reports in PDF or Excel format so that I 

can analyze them externally or present them during meetings. 

###### **Acceptance Criteria:** 

- Exported files retain the original report’s structure and content. 

277 

56 

- The export process completes successfully without errors. 

###### **HU-REP-007** 

###### **Related Requirement:** RF-REP-007 

**Actor:** Immediate Supervisor 

**User Story:** As an immediate supervisor, I want to export generated reports in PDF or Excel 

format so that I can back up the commercial management tracking. 

###### **Acceptance Criteria:** 

- Exported reports preserve applied filters. 

- Files can be downloaded successfully. 

###### **HU-REP-008** 

###### **Related Requirement:** RF-REP-008 

**Actor:** Manager 

**User Story:** As a manager, I want to visualize consolidated information through charts and KPI 

indicators to easily interpret the team’s overall results. 

###### **Acceptance Criteria:** 

- The system presents bar charts, line graphs, or KPI indicators. 

- Displayed data correspond to consolidated reports. 

###### **HU-REP-009** 

###### **Related Requirement:** RF-REP-010 

###### **Actor:** Sales Advisor 

**User Story:** As a sales advisor, I want to view my own performance metrics, including contacted 

clients, active negotiations, closures, and accumulated billing, so that I can assess my personal progress. 

###### **Acceptance Criteria:** 

- The system displays updated personal metrics for the advisor. 

- Data include contacted clients, closures, and total billing. 

278 

57 

- The advisor can only view their own information. 



<!-- Start of picture text -->
[ Actividad Hola, Asesort| — { oD | [ Portatake BORE SEa Bare fi Sais eels EF Agregar Cente ( Editar Servicio ] Agregar Chente ]<br>préxina dX ae =v) Monte ergrete vente ormecion person<br>== Sopitos Corp. a=" aww — ¥) — a ome || u<br>—— : —<br>EE mY] — ——— —— :<br>gee go | | (Ow [Ne] |) (OMe N aT] | | geese a — a<br>os = (Oz205|(9 3 | (Oxaxvs A | ee ret on ee X a<br>| | @. 10%SEEEE38+ | pasido prise (os&NS zaon Epw ate Taalraters necaPsexBassinessaeGold PlanL2AETADONov ED— WwicemanEGRESSX 9 © |<br><!-- End of picture text -->



<!-- Start of picture text -->
zoomWorkplace =r= MeetingMeeting 40-Minutes40-Minute: @ © Recording... Recordinc 1 @ ViewView ia > 0 x<br>Participants (5) @ x<br>Salvador Mufioz Nahim Diaz _ iPhone de Chris... | Mkt - Jose Boh...<br>[m-} Mkt - Jose Bohorquez 8A<br>© Phonede christian Y cA<br>Nahim Diaz BA<br>6B satiador mutoz LC<br>eee<br>YouCyes",can“slownow senddown’,nonverbal etc) fromfeedback“Reactions<br>can= a>- @+- ©O- B- 89 8- @ © 5 on the toolbar.tte tet :<br>Audio Video Participants Chat React Share Hosttools «Apps -—«—Pause/stop recording More End<br>=BE Q Search; a “aeeaagabB2= SB ma @ e ~ GPA aoSMD sopepres5:05 PM<br><!-- End of picture text -->

281 

###### **CHAPTER 10** 

###### **INDIVIDUAL CONTRIBUTIONS** 

|**Name**|**Contributions**|
|---|---|
|Aragon Intriago Shirley|Preparation<br>of<br>functional<br>and<br>non-functional|
|Yamel|requirements, and drafting of user stories.|
|Diaz<br>Osorio<br>Fernando|Communication with the client and participation in the|
|Nahim|preparation of the project specifcation document.|
|Muñoz Sanchez Salvador|Preparation<br>of<br>functional<br>and<br>non-functional|
|Gabriel|requirements, and coordination of the requirements<br>validation process.|
|Navarrete Castillo Anthony|Preparation of the project prototype and collaboration|
|Josue|in the drafting of the specifcation document in LaTeX.|
|Tumbaco Santana Gabriel|Communication with the client, preparation of the|
|Alejandro|prototype, and compilation of the fnal LaTeX<br>document.|



Table 10.1 Individual Contributions of the Project 

282 

###### **CHAPTER 11** 

###### **AUTHORSHIP DECLARATION** 

We, the undersigned members of the BOPADIGITAL development team, hereby declare that the present document titled “BOPACORP S.A. Requirements Specification Document” has been entirely prepared by us as part of the course Software Engineering I at Escuela Superior Politécnica del Litoral (ESPOL). 

We affirm that all sections, analyses, and specifications contained in this document represent our own work and understanding, based on information gathered from the client and the methodologies applied during the software requirements engineering process. 

No part of this document has been copied, plagiarized, or taken from other sources without proper acknowledgment. Any external reference used has been duly cited in the bibliography according to academic integrity standards. 

Each member of the team assumes full responsibility for the authenticity, accuracy, and originality of the content herein. 

**Digital Confirmation:** All members of the team confirm authorship through their electronic submission of this document. 

###### **Team Members:** 

Aragon Intriago Shirley Yamel 

Diaz Osorio Fernando Nahim Muñoz Sanchez Salvador Gabriel Navarrete Castillo Anthony Josue Tumbaco Santana Gabriel Alejandro 

283 

###### **APPENDIX I** 

**PROTOTYPE** 

**1. Prototype’s Screenshots** 



<!-- Start of picture text -->
— Hola, Asesor1 /O \<br>4 dias para cierre / \<br>Actividad prdxima |<br>| Visita Cotizacién 12-10-25 | \<br>Empresa X. SA 12:30pm Ty<br>Estado Actual: Requiere aprobacién ~_<br>; / Sapitos Corp.<br>| SubidaSapitosEstado deActual:Core.tualdocumentaciénCerrado tuao-256:00pm Nombre de Contacto: José B.<br>{ J RUC: 0128342901001<br>Celular: 0912345784<br>Asignade a: Asesor1<br>Actividad reciente Servicios de intéres eselocumentacién delocumentacién de de<br>| Visita Técnica ] * Starter Corporative 2<br>Empresa x. SA S | Cantidad: 25 lineas Facturacin<br>{ Estado Actual: Negociacién J Facturacién estimada: 450USD porestimadaclienteestimadaclientecliente<br>W) Visita Carros Estado Andres Actual:LnicialContacto Ine. Inicial > Cantidad:Facturaciéin@ Microsoft Office365Business15estimada:;licenciasFacturaciéin@ Microsoft Office365Business15estimada:;licencias@ Microsoft Office365Business15estimada:;licencias Microsoft Office365Business15estimada:;licencias15estimada:;licenciasestimada:;licenciaslicencias 2O0OUSD 612USDVU:VU:<br>Observaciones Generales<br>Agregar (oven spsim is snly anny text of the snly anny text of the anny text of the text of the of the the printing ond typesetting instr, ond typesetting instr, typesetting instr, instr, Lore Zp hes hes<br>evento sereLcchanged.Lcchanged. Tt wae popularised in the ‘Cte1960smakewtha typethe ‘Cte1960smakewtha typethe1960smakewtha typethemakewtha typethewtha typethea typethe typethethe teasespernesof beakLetrasetFeeGreate caredcontinin setspernesof beakLetrasetFeeGreate caredcontinin setof beakLetrasetFeeGreate caredcontinin set beakLetrasetFeeGreate caredcontinin setLetrasetFeeGreate caredcontinin setFeeGreate caredcontinin setGreate caredcontinin set caredcontinin setcontinin set set |<br>eeeeesees<br>Historial<br>Visita Técnica<br>(iesFE ETSI ORShUhUuQGUCO EST pie laramcetieenece laramcetieenece Asreger evento<br>Portafolio de Sapitos Corp. Nuevo evento<br>Cliente<br>Tamafio: 22.6 kb v<br>Tipo: PDF file file Fecha y hora 103078 Sir Fotos Fotos 0 document<br>(=) Tomato: ConfirmaciénTipo:Tipo: PDF 22-6  rgpesicionfilefile kb inicial.pd Tipo de evento [ [ Reunion general Vv<br>faContraofertaaContraofertaContraoferta 2.edé<br>Tipo:Tamaiio:PDF46.1filekbTamaiio:PDF46.1filekbPDF46.1filekb46.1filekbfilekbkb Editar progreso / etapa a|| Cotizacién 4 wv]<br>Correo WSP_12322.png Serviciervicioservicios<br>Tamako: 2.3MB<br>ipo:ee Im 9 Cantidad: 12 lineas<br>Facturaci6n estimada: 433USD<br>Observaciones adicionales:<br>Escribe aqui.<br><!-- End of picture text -->



<!-- Start of picture text -->
/O \<br>/ \<br>|<br>\<br>Ty<br>~_<br>Sapitos Corp.<br>Nombre de Contacto: José B.<br>RUC: 0128342901001<br>Celular: 0912345784<br>Asignade a: Asesor1<br>Servicios de intéres eselocumentacién delocumentacién de de<br>* Starter Corporative 2<br>Cantidad: 25 lineas Facturacin<br>Facturacién estimada: 450USD porestimadaclienteestimadaclientecliente<br>Cantidad:Facturaciéin@ Microsoft Office365Business15estimada:;licenciasFacturaciéin@ Microsoft Office365Business15estimada:;licencias@ Microsoft Office365Business15estimada:;licencias Microsoft Office365Business15estimada:;licencias15estimada:;licenciasestimada:;licenciaslicencias 2O0OUSD 612USDVU:VU:<br>Observaciones Generales<br>(oven spsim is snly anny text of the snly anny text of the anny text of the text of the of the the printing ond typesetting instr, ond typesetting instr, typesetting instr, instr, Lore Zp hes hes<br>sereLcchanged.Lcchanged. Tt wae popularised in the ‘Cte1960smakewtha typethe ‘Cte1960smakewtha typethe1960smakewtha typethemakewtha typethewtha typethea typethe typethethe teasespernesof beakLetrasetFeeGreate caredcontinin setspernesof beakLetrasetFeeGreate caredcontinin setof beakLetrasetFeeGreate caredcontinin set beakLetrasetFeeGreate caredcontinin setLetrasetFeeGreate caredcontinin setFeeGreate caredcontinin setGreate caredcontinin set caredcontinin setcontinin set set |<br>eeeeesees<br>Historial<br>Visita Técnica<br>pie laramcetieenece laramcetieenece Asreger evento<br><!-- End of picture text -->



<!-- Start of picture text -->
Portafolio de Sapitos Corp.<br>Tamafio: 22.6 kb<br>Tipo: PDF file file<br>(=) Tomato: ConfirmaciénTipo:Tipo: PDF 22-6  rgpesicionfilefile kb inicial.pd<br>faContraofertaaContraofertaContraoferta 2.edé<br>Tipo:Tamaiio:PDF46.1filekbTamaiio:PDF46.1filekbPDF46.1filekb46.1filekbfilekbkb<br>Correo WSP_12322.png<br>Tamako: 2.3MB<br>ipo:ee Im 9<br><!-- End of picture text -->



<!-- Start of picture text -->
Nuevo evento<br>Cliente<br>v<br>Fecha y hora 103078 Sir Fotos Fotos 0 document<br>Tipo de evento [ [ Reunion general Vv<br>Editar progreso / etapa a|| Cotizacién 4 wv]<br>Serviciervicioservicios<br>Cantidad: 12 lineas<br>Facturaci6n estimada: 433USD<br>Observaciones adicionales:<br>Escribe aqui.<br><!-- End of picture text -->



<!-- Start of picture text -->
(> Hola, Asesor1<br>Chentes 4 dias para cierre<br>Fecha de creacién<br>Octubre v<br>$$$<br>Nombre deEmpresaContacto: FranciscoX. SA Pérez |<br>Correo: Franpe@xindustry.ec<br>Carros Andres Inc.<br>Nowbreoreo: deportabilida coreg Reegmail.comtees<br>; -<br>Sapitos Corp.<br>Ventre de Gontoete, ose B<br>orreo: jose@sopitoscorp.com<br>Septiembre v<br>Grupo Andino Z<br>Nombre de Contacto: Roberto Alvarez<br>aECorreo: r.alvarez@grupo-z.com.ec<br>Agostov<br>6 Innovatec Global S.A.<br>Nombre de Contacto: Marfa Silva<br>Correo: mfsilva@innovatec.ec<br><!-- End of picture text -->



<!-- Start of picture text -->
(- 4 dias para cierre<br>Dashboard<br>/ (15.0%)a $200 WO cierte<br>@ ciertes<br>eA —<br>@oox) adil @ cietesa<br>Visitas realizadas Lineas ofrecidas<br>©) 13 Lo 341<br>Tngreso generado Clentes cevrados<br>@ 2132 usp a 3<br>i ..<br>Actividad prdxima<br>eeVisita Cotizacién soap.2s<br>( EmpresaEstado Actual:X. SARequiere aprobacién 12:30pm J<br>la >)<br>Z Subida de documentacibn 1.5.<br>Sapitos Corp. 6:00em<br><!-- End of picture text -->



<!-- Start of picture text -->
Eventos ~ Adinistrodor Chentes = Adninstrodor<br>(> Hola, Admin (- Hola, Admin<br>Eventos 4 dias para cierre ; 4 dias para cierre<br>Clientes<br>Ingresos || Distribuidor Visita reciente |{ Ingresos Ingresos estimados<br>OINAMartha NOREENLopez v Visitawettestinicialeswettestinicialesinicialeses  V<br>| ReunidnLogisticaModalidad:CosteraCotizaciinOnline (LogiCore) 16-10-252.00pm | SENombreNombre deEmpresaContacto:EmpresaContacto:Contacto: FranciscoX. SAX. SA SA Pérez<br>~ 7 L Correo: Franpe@xindustry.ec }<br>AnthonyMarco Rubio Lipowev. A | Correo:NombreNombre jose@sapitoscorp.comdede SapiContacContac t o:osJoséCorp.B.osJoséCorp.B.JoséCorp.B.Corp.B.B. & )||<br>Subida de documentacibn 1.4.55 Cotizacién v<br>Sapitos Corp. 6:00pm ; :<br>{ Modalidad: Presencial Grupo Andino Z<br>r >) Nombre de Contacto: Roberto Alvarez<br>ReuniénGrupo AndinoCotizaciin. Z 1110-252 oieOban S Correo: r.alvarez@grupo-z.com.ec~~ J|<br>Modalidad: Online Documentos V V<br>( Conchita Lonso v Innovatec Global S.A.<br>| W) VisitaNodalidad:Industriasmee  TriciaicialPresencialdel Norte 22-10-254:00pm )j ~ PendienteNombreCorreo: de Contacto:mFsilva@innovatec.ecdeNombreCorreo: de Contacto:mFsilva@innovatec.ecdeCorreo: de Contacto:mFsilva@innovatec.ecde de Contacto:mFsilva@innovatec.ecdemFsilva@innovatec.ecdede aprobaciénvMariaMaria Silva<br>—— — > Logistica Costera (LogiCost)<br>Visita PostVenta 14-10-25 Nombre de Contacto: Juan Vélez<br>TnnovaTeeModalidad: GlobalPresencialSA 6:00pm | _Correo:Correo: jevelez@logicost.ecyy )<br>Mario Bert a<br>Chentes = Adninstrodor<br>> Hola, Admi (> Hola, Admin<br>4 diasa,a, para cierreminmin 4 dias para cierre<br>Usuarios Dashboard<br>Tipo de usuario [TaeRaoCrRaoCr ETS wl<br>Fecha de cracién nol<br>Admin v v il<br>Ben Hanneshoufer * ol<br>Correo: Franpe@xindustry.ec<br>Clientes asignados: 0 »)<br>Marta Lidio “January, February, March Aon May<br>Correo: mllidio@xindustry.ec Visitas realizadas Lineas of recidas, recidas,<br>Clientes asignados: 0 43 1.2k<br>Ben Hanneshaufer<br>Correo: tec@boca.corp Ingreso generado Clientes nuevos<br>Asesores A 0 14.2k usd usd <i 10<br>Cuentas cerradas, Generaraa reporte<br>= 18 xlsx<br>Asesor top ventas:<br>Shirley Aragén<br>RQ)PSPS  ClienteAnclrelucrativoareAnclrelucrativoarelucrativoareare "<br><!-- End of picture text -->



<!-- Start of picture text -->
Chentes = Adninstrodor<br>(- Hola, Admin<br>; 4 dias para cierre<br>Clientes<br>Visita reciente |{ Ingresos Ingresos estimados<br>Visitawettestinicialeswettestinicialesinicialeses  V<br>SENombreNombre deEmpresaContacto:EmpresaContacto:Contacto: FranciscoX. SAX. SA SA Pérez<br>L Correo: Franpe@xindustry.ec }<br>| Correo:NombreNombre jose@sapitoscorp.comdede SapiContacContac t o:osJoséCorp.B.osJoséCorp.B.JoséCorp.B.Corp.B.B. & )||<br>Cotizacién v<br>; :<br>Grupo Andino Z<br>Nombre de Contacto: Roberto Alvarez<br>S Correo: |<br>r.alvarez@grupo-z.com.ec~~ J|<br>Documentos V V<br>Innovatec Global S.A.<br>~ PendienteNombreCorreo: de Contacto:mFsilva@innovatec.ecdeNombreCorreo: de Contacto:mFsilva@innovatec.ecdeCorreo: de Contacto:mFsilva@innovatec.ecde de Contacto:mFsilva@innovatec.ecdemFsilva@innovatec.ecdede aprobaciénvMariaMaria Silva<br>Logistica Costera (LogiCost)<br>Nombre de Contacto: Juan Vélez<br>_Correo:Correo: jevelez@logicost.ecyy )<br><!-- End of picture text -->



<!-- Start of picture text -->
Chentes = Adninstrodor<br>> Hola, Admi<br>4 diasa,a, para cierreminmin<br>Usuarios<br>Tipo de usuario [TaeRaoCrRaoCr ETS<br>Fecha de cracién<br>Admin v v<br>Ben Hanneshoufer<br>Correo: Franpe@xindustry.ec<br>Clientes asignados: 0<br>Marta Lidio<br>Correo: mllidio@xindustry.ec<br>Clientes asignados: 0<br>Ben Hanneshaufer<br>Correo: tec@boca.corp<br>Asesores A<br><!-- End of picture text -->



<!-- Start of picture text -->
(> Hola, Admin<br>4 dias para cierre<br>Dashboard<br>wl<br>nol<br>il<br>* ol<br>»)<br>“January, February, March Aon May<br>Visitas realizadas Lineas of recidas, recidas,<br>43 1.2k<br>Ingreso generado Clientes nuevos<br>0 14.2k usd usd <i 10<br>Cuentas cerradas, Generaraa reporte<br>= 18 xlsx<br>Asesor top ventas:<br>Shirley Aragén<br>RQ)PSPS  ClienteAnclrelucrativoareAnclrelucrativoarelucrativoareare "<br><!-- End of picture text -->



<!-- Start of picture text -->
BoPACORP Ss.A. Inicio Nosotros Productos Postulaciones<br>mM© Innovamosexperiencia la<br>(E comercial digital<br>(3 conectividad y servicios digitales.<br>= 2 Soluciones integradas para telecomunicaciones,<br>Nuestros Servicios<br>Voz Conectividad Productos Digitales<br>Lorem ipsum dolor Lorem ipsum dolor Lorem ipsum dolor sit<br>Nosotros<br>Lorem ipsum dolor sit amet, consectetur<br>adipiscing elit. Vestibulum sit amet neque<br>dolor.<br>==<br>Postula con nosotros<br>Forma parte de nuestro equipo de trabajo<br><!-- End of picture text -->



<!-- Start of picture text -->
BO PAC O{R P Ss °A ° Inicio Nosotros Productos Postulaciones<br>CatalogoA| dede ProdProductos<br>Nuestros Productos y Servicios<br>Voz ss Productos<br>Conectividad Digitales<br>Pl Celul Internet Satelital<br>anes Celulares Huawei Cloud<br>Terminales Starlink Microsoft365<br><!-- End of picture text -->



<!-- Start of picture text -->
BOPACORP S.A Inicio Nosotros Productos Postulaciones<br>Planes Celulares<br>suscripion PHDOWISCO ree vide 4GB<br>Ss dae Ss Business Pack Ss Business Pack<br>@ + neon © + nse0 @ + ne00<br><!-- End of picture text -->

. * Cerrar Sesid AdminBopaDigital errar Sesién 

###### Listado de Productos y Servicios 



<!-- Start of picture text -->
Movistar Empresas<br>Movistar Empresas<br>Movistar Empresas<br><!-- End of picture text -->



<!-- Start of picture text -->
Pagina web - Postulaciones<br>BOPACORP Ss.A. Inicio Nosotros Productos Postulaciones BoPACORP s A Inicio Nosotros Productos Postulaciones<br>Ubicaci6n; (TT) Modalidad (—___)})<br>TITULO DEL PUESTO<br>Puesto nt: Descripcién del puesto Cargar CV<br>Puesto wt Deseripeién del puesto<br><!-- End of picture text -->



<!-- Start of picture text -->
CRM - Embudo<br>BOPADIGITAL - Asesor<br>Dashboard Prospeccién Contacto Inicial Negociacién Cierre Post-Venta<br>Contactos<br>Ventas Juan Perez Salvador Muiioz Nahin Diaz Gobriel Tumbaco Shirley Aragén<br>Postventas Correo: juanperesz@correc.com Correo: salvadorm@correo.com Correo: nahimd@correc.com Correo: gabrielt@correo.com Corres: shirleya@corres.com<br><!-- End of picture text -->



<!-- Start of picture text -->
CRM - Embudo<br>BOPADIGITAL - Asesor<br>Dashboard Prospeccién Contacto Inicial Negociacién Cierre Post-Venta<br>Contactos<br>Ventas Suan Perez Salvador Muioz Nohim Dioz Gobriel Tumbaco Shirley Aragén<br>Postventas Correo: shirleya@correo.com<br>El cliente fue agregado con éxito a la fase de cierre<br>Ahora sube los documentos requeridos<br>SUBIR DOCUMENTOS<br><!-- End of picture text -->

" 

CRM - Formulario de nuevo contacto 



<!-- Start of picture text -->
BOPADIGITAL - Asesor<br>Dashboard<br>Crear Contacto<br>Contactos<br>Ventas<br>Guardar Contacto Subir Documentos<br><!-- End of picture text -->

CRM - Contactos Vista Asesor 



<!-- Start of picture text -->
BOPADIGITAL - Asesor<br>Dashboard Listado. de Contactos<br>Ventas<br>[5<br>| eae<br>(a| ener<br>[or ens<br>(| eaane ve<br><!-- End of picture text -->



<!-- Start of picture text -->
CRM Administrador<br>BOPADIGITAL - Administrador<br>Asesores registrados<br>Consultar informacion<br>Juan Perez 22 $2500 25 de diciembre de ventas<br>08H00<br>Consultar informacion<br>Nahim | Diaz 35 $6300 25 de diciembre de ventas<br>14HOO<br>| salvador | muioz 2 $1200 78 ae iciem|con A——nta:<br><!-- End of picture text -->



<!-- Start of picture text -->
CRM - Administrador<br>BOPADIGITAL - Adwministrador<br>Ventas Ventas Totales (Mes) Nuevos Clientes (Mes) Tasa de Cierre (%)<br>Postventas $199,899.08 200 50%<br>Embudo de Ventas<br>Prospeccion Visita Inicial Negociacion<br>12 23 43<br>Aprobacién Pendiente Cierre Postventas<br>54 12 32<br>Actividad reciente<br>@p técnica Hace 2 horas<br><!-- End of picture text -->



<!-- Start of picture text -->
CRM Administrador<br>BOPADIGITAL - Adwinistrador<br>Actividad reciente<br>O Asesor. Juan Perez Hoy, 12:30PM<br>Cambio el estado de NOMBRE CONTACTO (NOMBRE EMPRESA) a Contacto inicial<br>NOMBRE EMPRESA<br>OC Asesor. Suan Perez Ayer, 2:30PM<br>Registro una visita con NOMBRE EMPRESA en DIA/FECHA, UBICACION, SEDE<br>NOMBRE EMPRESA<br>O Asesor. Juan Perez Ayer, 2:30PM<br>Agendé una visita con NOMBRE EMPRESA para HORA Y FECHA<br>NOMBRE EMPRESA<br>O Asesor. Juan Perez Ayer, 2:30PM<br>Subid documentacién (VOMBRE DE DOCUMENTACION) para Empresa<br>NOMBRE EMPRESA<br><!-- End of picture text -->



<!-- Start of picture text -->
CRM - Contactos Vista Administrador<br>BOPADIGITAL - Adwinistrador<br>Dashboard Listado de Contactos<br>Contactos<br>Ventas Crear contacto AsignarSig contacto<br>[oan<br>[O<br>| aman<br>(ome ies<br><!-- End of picture text -->



<!-- Start of picture text -->
CRM - Contactos Vista Administrador<br>BOPADIGITAL - Adwministrador<br>Dashboorhboard Listado de Contactos<br>Ventas éA que asesor quieres asignar estos contactos?<br>Postventas<br>Pedro Infante<br><!-- End of picture text -->

295 

###### **APPENDIX II** 

###### **CLIENT ACCEPTANCE LETTER** 

###### **1. Signed Approval Document** 

This appendix contains the official acceptance letter signed by the stakeholder representative of BOPACORP S.A., confirming their agreement with the content of this Requirements Specification Document and validating that it meets the functional and non-functional expectations discussed during the requirements elicitation process. 



<!-- Start of picture text -->
CE) O L PolitécnicaEscuela Superiordeldel Litoral<br><!-- End of picture text -->

### CE) O L Escuela SuperiordelPolitécnicaEscuela Superiordeldel Litoral 

297 

###### **APPENDIX III** 

###### **SIGNED AUTORSHIP DECLARATION** 

###### **1. Signatures and Formal Confirmation** 

This appendix includes the signed authorship declaration, in which the members of the development team formally certify that the work presented in this document is original, was produced collaboratively, and complies with the academic and ethical standards established by the institution. The signatures below represent each member’s personal attestation to this statement and their commitment to the document’s authenticity. 

## ~~ee ee pf~~ ~~<u>mm a</u>~~ t-] . ~~ara~~ ~~<u>ptf</u> |~~ ~~<u>sent |</u>~~ 

