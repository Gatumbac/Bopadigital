### BOPACORP S.A. Final Project Specification Document

by

Grupo 2 BOPADIGITAL

PROJECT PRESENTED TO ESCUELA SUPERIOR POLITÉCNICA DEL LITORAL

GUAYAQUIL, JANUARY 12, 2026

ESCUELA SUPERIOR POLITÉCNICA DEL LITORAL ESPOL

Grupo 2 BOPADIGITAL, 2026

This Creative Commons license allows readers to download this work and share it with others as long as the author is credited. The content of this work cannot be modified in any way or used commercially.

TEAM MEMBERS

THIS PROJECT HAS BEEN DEVELOPED

BY THE FOLLOWING GROUP OF STUDENTS

Shirley Aragon Facultad de Ingenieria en Electricidad y Computación

Nahim Díaz Facultad de Ingenieria en Electricidad y Computación

Salvador Muñoz Facultad de Ingenieria en Electricidad y Computación

Gabriel Tumbaco Facultad de Ingenieria en Electricidad y Computación

Anthony Navarrete Facultad de Ingenieria en Electricidad y Computación

TABLE OF CONTENTS

Page

CHAPTER 1 RISK MANAGEMENT, SPRINT BACKLOGS, AND PROJECT SCHEDULING. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1

1. 1 Risk Management . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1

1. 1.1 Identified Risks for the BOPADIGITAL Project . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1

1. 2 Product backlog . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4

1. 3 Sprint Backlog . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11

1. 3.1 Sprint 1: Foundation, Auth & Public Web (Weeks 1–4) . . . . . . . . . . . . . . . . . . . . 11

1. 3.2 Sprint 2: CRM Core & Geolocation (Weeks 5–8) . . . . . . . . . . . . . . . . . . . . . . . . . . 12

1. 4 Scheduling . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14

CHAPTER 2 STATIC SYSTEM MODELING AND ARCHITECTURAL DESIGN . . . . 16

2. 1 Use Case Diagram. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18

2. 2 Use Case Documentation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21

2. 3 Class Diagrams . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 92

2. 4 Object Diagrams. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .102

2. 5 Components Diagram . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .108

2. 6 Deployment Diagram . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .110

CHAPTER 3 SYSTEM BEHAVIORAL MODELING . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .112

3. 1 Activity Diagrams. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .113

3. 2 Sequence Diagrams . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .118

3. 3 Collaboration–Communication Diagrams . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 151

3. 4 State Diagrams . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .155

CHAPTER 4 INDIVIDUAL CONTRIBUTIONS . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .159

CHAPTER 5 AUTHORSHIP DECLARATION. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .160

APPENDIX I PROTOTYPE . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 161

APPENDIX II CLIENT ACCEPTANCE LETTER . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .209

APPENDIX III REQUIREMENTS SPECIFICATION DOCUMENT . . . . . . . . . . . . . . . . . . . . . 211

LIST OF TABLES

Page

Table 1.1 Risk Probability Classification . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1

Table 1.2 Identified Risks and Mitigation Strategies for the BOPADIGITAL Project . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3

Table 1.3 Product Backlog for the BOPADIGITAL Project . . . . . . . . . . . . . . . . . . . . . . . . . . . 10

Table 1.4 Sprint 1 Backlog — Foundation, Authentication and Public Web . . . . . . . . . 11

Table 1.5 Sprint 2 Backlog — CRM Core, Geolocation, and Business Logic. . . . . . . 13

Table 1.6 Project Scheduling and Critical Path Overview . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15

Table 2.1 Use Case Documentation - Contact an Advisor from the Catalog . . . . . . . . . 22

Table 2.2 Use Case Documentation - View Job Vacancies . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24

Table 2.3 Use Case Documentation - Apply for a Job Vacancy . . . . . . . . . . . . . . . . . . . . . . . 25

Table 2.4 Use Case Documentation - Access Control Panel with Credentials . . . . . . . . 27

Table 2.5 Use Case Documentation - Manage Product Catalog . . . . . . . . . . . . . . . . . . . . . . . 29

Table 2.6 Use Case Documentation - Register New Client . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31

Table 2.7 Use Case Documentation - Update Existing Client . . . . . . . . . . . . . . . . . . . . . . . . . 33

Table 2.8 Use Case Documentation -Edit Negotiations. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35

Table 2.9 Use Case Documentation - Register Visit . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 37

Table 2.10 Use Case Documentation - View Visit History . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 39

Table 2.11 Use Case Documentation - Update negotiation status . . . . . . . . . . . . . . . . . . . . . . 41

Table 2.12 Use Case Documentation - Assign client to advisor . . . . . . . . . . . . . . . . . . . . . . . . 43

Table 2.13 Use Case Documentation - Unassign or remove client from an advisor . . . 45

Table 2.14 Use Case Documentation - Disable closed negotiations . . . . . . . . . . . . . . . . . . . . 47

Table 2.15 Use Case Documentation - View recent advisor activity . . . . . . . . . . . . . . . . . . . 49

III

Table 2.16 Use Case Documentation - View costs per advisor . . . . . . . . . . . . . . . . . . . . . . . . . 51

Table 2.17 Use Case Documentation - Get progress report . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 53

Table 2.18 Use Case Documentation - Compare Metrics Between Advisors . . . . . . . . . . 54

Table 2.19 Use Case Documentation - View Advisor Metrics . . . . . . . . . . . . . . . . . . . . . . . . . . 57

Table 2.20 Use Case Documentation - Filter Reports . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 60

Table 2.21 Use Case Documentation - Generate Sales and Closing Reports . . . . . . . . . . 63

Table 2.22 Use Case Documentation - Filter Client Lists by Metrics . . . . . . . . . . . . . . . . . . 66

Table 2.23 Use Case Documentation - Reject Matrices. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 69

Table 2.24 Use Case Documentation - Review Operator Availability . . . . . . . . . . . . . . . . . . 71

Table 2.25 Use Case Documentation - Check Matrix Approval Status. . . . . . . . . . . . . . . . 74

Table 2.26 Use Case Documentation - Consult Clients and Their Documentation Status . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 76

Table 2.27 Use Case Documentation - Download Documentation . . . . . . . . . . . . . . . . . . . . . 78

Table 2.28 Use Case Documentation - Tag Documentation . . . . . . . . . . . . . . . . . . . . . . . . . . . . 80

Table 2.29 Use Case Documentation - Review Documentation Uploaded to Profile . . 82

Table 2.30 Use Case Documentation - Add Client Documentation . . . . . . . . . . . . . . . . . . . . 84

Table 2.31 Use Case Documentation - Review and Approve New Matrices . . . . . . . . . . . 86

Table 2.32 Use Case Documentation - Request Supervisor Approval . . . . . . . . . . . . . . . . . . 88

Table 2.33 Use Case Documentation - Create Offer Matrix for Specific Clients . . . . . . 90

Table 4.1 Individual Contributions of the Project . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .159

LIST OF FIGURES

Page

Figure 1.1 Activity on Arrow Diagram . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15

Figure 2.1 BOPADIGITAL Use Case Diagram Part 1 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18

Figure 2.2 BOPADIGITAL Use Case Diagram Part 2 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20

Figure 2.3 BOPADIGITAL Class Diagram Overview . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 93

Figure 2.4 BOPADIGITAL Auth Module Class Diagram . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 94

Figure 2.5 BOPADIGITAL CoreUsers Module Class Diagram . . . . . . . . . . . . . . . . . . . . . . . 95

Figure 2.6 BOPADIGITAL CRM Module Class Diagram . . . . . . . . . . . . . . . . . . . . . . . . . . . . 96

Figure 2.7 BOPADIGITAL Documents Module Class Diagram . . . . . . . . . . . . . . . . . . . . . . 97

Figure 2.8 BOPADIGITAL Employability Module Class Diagram . . . . . . . . . . . . . . . . . . . 98

Figure 2.9 BOPADIGITAL OfferMatrices Module Class Diagram . . . . . . . . . . . . . . . . . . . 99

Figure 2.10 BOPADIGITAL Reports Module Class Diagram . . . . . . . . . . . . . . . . . . . . . . . . .100

Figure 2.11 BOPADIGITAL ServiceCatalogCMS Module Class Diagram. . . . . . . . . . 101

Figure 2.12 BOPADIGITAL CRM Object Diagram Overview . . . . . . . . . . . . . . . . . . . . . . . .103

Figure 2.13 BOPADIGITAL OfferMatrix Object Diagram Overview . . . . . . . . . . . . . . . .104

Figure 2.14 BOPADIGITAL Catalog Object Diagram Overview . . . . . . . . . . . . . . . . . . . . .105

Figure 2.15 BOPADIGITAL Auth Object Diagram Overview . . . . . . . . . . . . . . . . . . . . . . . .106

Figure 2.16 BOPADIGITAL Documents Object Diagram Overview . . . . . . . . . . . . . . . . . 107

Figure 2.17 BOPADIGITAL Components Object Diagram . . . . . . . . . . . . . . . . . . . . . . . . . . .109

Figure 2.18 BOPADIGITAL Deployment Diagram . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 111

Figure 3.1 BOPADIGITAL Activity Diagram – Negotiation Life Cycle . . . . . . . . . . . .113

Figure 3.2 BOPADIGITAL Activity Diagram – Offer Matrices . . . . . . . . . . . . . . . . . . . . .114

Figure 3.3 BOPADIGITAL Activity Diagram – Visit Management . . . . . . . . . . . . . . . . .115

V

Figure 3.4 BOPADIGITAL Activity Diagram – Auth . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .116

Figure 3.5 BOPADIGITAL Activity Diagram – Document Management . . . . . . . . . . . 117

Figure 3.6 BOPADIGITAL Sequence Diagram - registerVisit. . . . . . . . . . . . . . . . . . . . . .119

Figure 3.7 BOPADIGITAL Sequence Diagram - reviewVisit. . . . . . . . . . . . . . . . . . . . . . .120

Figure 3.8 BOPADIGITAL Sequence Diagram - updateNegotiationStatus . . . . . . . . . 121

Figure 3.9 BOPADIGITAL Sequence Diagram - checkVisitHistory. . . . . . . . . . . . . . . .122

Figure 3.10 BOPADIGITAL Sequence Diagram - deactivateClient. . . . . . . . . . . . . . . . . .123

Figure 3.11 BOPADIGITAL Sequence Diagram - createOfferMatrix. . . . . . . . . . . . . . . .124

Figure 3.12 BOPADIGITAL Sequence Diagram - addItemToMatrix. . . . . . . . . . . . . . . .125

Figure 3.13 BOPADIGITAL Sequence Diagram - recalculateTotals. . . . . . . . . . . . . . . . .126

Figure 3.14 BOPADIGITAL Sequence Diagram - saveDraft. . . . . . . . . . . . . . . . . . . . . . . . . 127

Figure 3.15 BOPADIGITAL Sequence Diagram - sendToSupervisor. . . . . . . . . . . . . . . .128

Figure 3.16 BOPADIGITAL Sequence Diagram - Login. . . . . . . . . . . . . . . . . . . . . . . . . . . . .129

Figure 3.17 BOPADIGITAL Sequence Diagram - listPendingMatrices . . . . . . . . . . . . . .130

Figure 3.18 BOPADIGITAL Sequence Diagram - approveMatrix. . . . . . . . . . . . . . . . . . . 131

Figure 3.19 BOPADIGITAL Sequence Diagram - rejectMatrix. . . . . . . . . . . . . . . . . . . . . .132

Figure 3.20 BOPADIGITAL Sequence Diagram - uploadDocument . . . . . . . . . . . . . . . . .133

Figure 3.21 BOPADIGITAL Sequence Diagram - approveDocument. . . . . . . . . . . . . . .134

Figure 3.22 BOPADIGITAL Sequence Diagram - rejectDocument. . . . . . . . . . . . . . . . . .135

Figure 3.23 BOPADIGITAL Sequence Diagram - downloadDocument. . . . . . . . . . . . .136

Figure 3.24 BOPADIGITAL Sequence Diagram - searchCatalog. . . . . . . . . . . . . . . . . . . . 137

Figure 3.25 BOPADIGITAL Sequence Diagram - filterCatalog. . . . . . . . . . . . . . . . . . . . . .138

Figure 3.26 BOPADIGITAL Sequence Diagram - createCatalogItem. . . . . . . . . . . . . . .139

Figure 3.27 BOPADIGITAL Sequence Diagram – checkPermission . . . . . . . . . . . . . . . . .140

VI

Figure 3.28 BOPADIGITAL Sequence Diagram – editWebContents. . . . . . . . . . . . . . . . 141

Figure 3.29 BOPADIGITAL Sequence Diagram – generateReport. . . . . . . . . . . . . . . . . .142

Figure 3.30 BOPADIGITAL Sequence Diagram – exportReport. . . . . . . . . . . . . . . . . . . . .143

Figure 3.31 BOPADIGITAL Sequence Diagram – activeVacancies. . . . . . . . . . . . . . . . . .144

Figure 3.32 BOPADIGITAL Sequence Diagram – applyToVacancy. . . . . . . . . . . . . . . . .145

Figure 3.33 BOPADIGITAL Sequence Diagram – evaluateApplication. . . . . . . . . . . . .146

Figure 3.34 BOPADIGITAL Sequence Diagram – submitApplication . . . . . . . . . . . . . . . 147

Figure 3.35 BOPADIGITAL Sequence Diagram – registrateClient. . . . . . . . . . . . . . . . . .148

Figure 3.36 BOPADIGITAL Sequence Diagram – assignClient . . . . . . . . . . . . . . . . . . . . . .149

Figure 3.37 BOPADIGITAL Sequence Diagram – scheduleVisit. . . . . . . . . . . . . . . . . . . .150

Figure 3.38 BOPADIGITAL Communication Diagram – Auth . . . . . . . . . . . . . . . . . . . . . . .152

Figure 3.39 BOPADIGITAL Communication Diagram – Approve Offer Matrix. . . .153

Figure 3.40 BOPADIGITAL Communication Diagram – uploadDocument. . . . . . . . .154

Figure 3.41 BOPADIGITAL State Diagram – Negotiation . . . . . . . . . . . . . . . . . . . . . . . . . . . .155

Figure 3.42 BOPADIGITAL State Diagram – Offer Matrix . . . . . . . . . . . . . . . . . . . . . . . . . . .156

Figure 3.43 BOPADIGITAL State Diagram – Negotiation Document . . . . . . . . . . . . . . . . 157

Figure 3.44 BOPADIGITAL State Diagram – Job Application. . . . . . . . . . . . . . . . . . . . . . .158

Figure I-1 BOPADIGITAL Prototype - Main view of the Sales Dashboard displaying the Kanban board with customer distribution by stages. . . . . . 161

Figure I-2 BOPADIGITAL Prototype - Visualization of the ability to move clients across stages within the Kanban board.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 161

Figure I-3 BOPADIGITAL Prototype - Detailed view of the client , showing contact information, interaction history, and visit planning panel.. . . . . .162

Figure I-4 BOPADIGITAL Prototype - “Edit Client” modal window allowing the modification of tax information (RUC, Legal Name) and contact details. 162

VII

Figure I-5 BOPADIGITAL Prototype - System notification displayed in the upper-right corner confirming the successful update of client data. . . . . .163

Figure I-6 BOPADIGITAL Prototype - “My Performance” screen displaying key KPI cards and the monthly revenue goal progress bar. . . . . . . . . . . . . . . . . . . .163

Figure I-7 BOPADIGITAL Prototype - Graphical analysis section within “My Performance”, detailing the client pipeline by stage and sales distribution by service. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .164

Figure I-8 BOPADIGITAL Prototype - “Weekly Activity” area chart and commercial efficiency metrics (Average per Sale and Visit Rate).. . . . . .164

Figure I-9 BOPADIGITAL Prototype - “Client Management” module presenting the complete tabular listing of the client portfolio with a global search bar.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .165

Figure I-10 BOPADIGITAL Prototype - Demonstration of the client list filtering functionality, isolating only those in the “Negotiation” stage.. . . . . . . . . . .165

Figure I-11 BOPADIGITAL Prototype - “Add New Client” modal form for registering new prospects, capturing tax data (RUC), contact information, and initial stage. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .166

Figure I-12 BOPADIGITAL Prototype - “Visit Calendar” module (January 2026 view) with status summary (Completed vs. Overdue) and monthly schedule visualization. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .166

Figure I-13 BOPADIGITAL Prototype - Client management panel: visit history displayed on the left and mandatory document upload section on the right.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 167

Figure I-14 BOPADIGITAL Prototype - Calendar navigation to future months (February 2026), enabling long-term visit planning and scheduling. . . . . 167

Figure I-15 BOPADIGITAL Advisor - "Offer Matrices" dashboard managing commercial proposals, displaying status counters (Drafts, Pending, Approved) and a list of client proposals with subsidy details.. . . . . . . . . . .168

Figure I-16 BOPADIGITAL Advisor - "New Offer Matrix" modal allowing the creation of a commercial proposal by selecting a client, adding products, and uploading necessary attachments.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .168

VIII

Figure I-17 BOPADIGITAL Advisor - "Edit Offer Matrix" interface for modifying specific line items within a proposal, such as adjusting quantities, unit prices, and adding item-specific notes. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .169

Figure I-18 BOPADIGITAL Advisor - Detailed view of an "Approved" Offer Matrix, highlighting the automatic subsidy calculation, final total, and supervisor approval comments. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .169

Figure I-19 BOPADIGITAL CMS - Product and Services Catalog dashboard displaying inventory statistics (Total, Active, Discontinued) and the product grid. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .170

Figure I-20 BOPADIGITAL CMS - Catalog filtering functionality, demonstrating the isolation of products within the "Telephony" category.. . . . . . . . . . . . . .170

Figure I-21 BOPADIGITAL CMS - Catalog view filtered by "Discontinued" status, highlighting legacy services with distinct visual tags.. . . . . . . . . . . . . . . . . . . 171

Figure I-22 BOPADIGITAL CMS - Search bar functionality enabling quick retrieval of specific services (e.g., "Internet Fibra Óptica") by name. . . . 171

Figure I-23 BOPADIGITAL CMS - "New Product" modal interface allowing administrators to register new services with defined categories, pricing, and status.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .172

Figure I-24 BOPADIGITAL CMS - "Edit Product" modal for modifying existing service details, including descriptions, pricing attributes, and image URLs. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .172

Figure I-25 BOPADIGITAL CMS - Security confirmation dialog ensuring administrative verification before permanently removing a product from the catalog.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .173

Figure I-26 BOPADIGITAL CMS - Web Content Editor dashboard used to manage public-facing website elements, showing content status and preview cards. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .173

Figure I-27 BOPADIGITAL CMS - Section filtering mechanism in the Web Content Editor, allowing focused management of specific page areas (e.g., Main Banner). . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .174

Figure I-28 BOPADIGITAL CMS - Content modification modal for updating website assets, including visibility toggles, display order, titles, and subtitles.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .174

IX

Figure I-29 BOPADIGITAL Admin - General Metrics Dashboard providing a consolidated view of commercial performance, including sales totals, conversion rates, and active team members.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .175

Figure I-30 BOPADIGITAL Admin - "Top Performers" section ranking sales advisors based on closed sales value and visit volume.. . . . . . . . . . . . . . . . . .175

Figure I-31 BOPADIGITAL Admin - Notification dropdown displaying real-time alerts regarding document approvals and rejections for specific clients. 176

Figure I-32 BOPADIGITAL Admin - System feedback (toast notification) confirming that all alerts have been marked as read.. . . . . . . . . . . . . . . . . . . . .176

Figure I-33 BOPADIGITAL Admin - System feedback confirming the successful deletion of notifications from the user’s history. . . . . . . . . . . . . . . . . . . . . . . . . . . 177

Figure I-34 BOPADIGITAL Admin - "Advisor Management" screen showing the team roster, status indicators, and alerts for pending document reviews. 177

Figure I-35 BOPADIGITAL Admin - "New Advisor" modal form used to register a new sales representative in the system. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .178

Figure I-36 BOPADIGITAL Admin - List view demonstrating the filtering capability to isolate "Inactive" advisors.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .178

Figure I-37 BOPADIGITAL Admin - Advisor Profile Modal: "Change History" tab tracking specific actions and updates made by the advisor. . . . . . . . . . .179

Figure I-38 BOPADIGITAL Admin - Advisor Profile Modal: "Assigned Clients" tab displaying the advisor’s current portfolio and account status.. . . . . . .179

Figure I-39 BOPADIGITAL Admin - Advisor Profile Modal: "Documents" tab summarizing the approval status of files uploaded by the advisor.. . . . . .180

Figure I-40 BOPADIGITAL Admin - Advisor Profile Modal: "Performance Metrics" tab showing KPIs like total invoicing and sales conversion rates.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .180

Figure I-41 BOPADIGITAL Admin - Advisor Profile Modal: "Recent Activities" timeline logging the advisor’s latest interactions and system events. . . . . 181

Figure I-42 BOPADIGITAL Admin - "Contact Management" screen showing the "Unassigned Contacts" tab, a pool of leads waiting for distribution.. . . . 181

Figure I-43 BOPADIGITAL Admin - Unassigned contacts filtered by the "Prospecting" stage to prioritize early-stage lead distribution. . . . . . . . . . . .182

X

Figure I-44 BOPADIGITAL Admin - Bulk selection of unassigned contacts to be transferred to a specific advisor (e.g., Patricia Vargas).. . . . . . . . . . . . . . . . . .182

Figure I-45 BOPADIGITAL Admin - Toast notification confirming the successful assignment of selected contacts to the target advisor.. . . . . . . . . . . . . . . . . . . .183

Figure I-46 BOPADIGITAL Admin - "Assigned Contacts" tab displaying the master list of clients that are currently managed by an advisor. . . . . . . . . . .183

Figure I-47 BOPADIGITAL Admin - "Add New Client" modal allowing administrators to manually inject new leads into the system.. . . . . . . . . . . .184

Figure I-48 BOPADIGITAL Admin - "Document Management" module for centralized bulk processing (approve/reject) of client documentation. . .184

Figure I-49 BOPADIGITAL Admin - Document filtering functionality, showing the list filtered by "Pending" status to prioritize urgent reviews. . . . . . . . . .185

Figure I-50 BOPADIGITAL Admin - Selection mechanism allowing administrators to choose specific documents (or all) to perform bulk actions like approval or rejection. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .185

Figure I-51 BOPADIGITAL Admin - "Reject Document" modal requiring the administrator to provide a mandatory reason for the rejection before processing. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .186

Figure I-52 BOPADIGITAL Admin - System notification confirming the initiation of a secure bulk download for the selected client documentation. . . . . . . .186

Figure I-53 BOPADIGITAL Admin - "Commercial Performance Reports" dashboard offering a high-level overview of sales productivity and team metrics.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 187

Figure I-54 BOPADIGITAL Admin - Advanced reporting filters applied to analyze a specific advisor’s performance (e.g., Roberto Mendoza) over the last semester. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 187

Figure I-55 BOPADIGITAL Admin - "Export Report" function allowing data to be generated and downloaded as a PDF file for external presentation.. .188

Figure I-56 BOPADIGITAL Admin - "Recent Activity" audit log tracking systemwide events such as closed sales, document uploads, and login sessions. 188

Figure I-57 BOPADIGITAL Admin - "Document Configuration" panel used to define mandatory or optional file requirements for different sales stages. 189

XI

Figure I-58 BOPADIGITAL Admin - "Edit Document Type" modal allowing adjustments to validation rules, such as making a document mandatory for all services.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .189

Figure I-59 BOPADIGITAL Admin - "Delete Document Type" confirmation modal ensuring the administrator intends to permanently remove a configuration (e.g., "RUC") from the system. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .190

Figure I-60 BOPADIGITAL Admin - "Add New Document Type" form allowing the definition of new mandatory or optional requirements, specifying applicable sales stages and service scope.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .190

Figure I-61 BOPADIGITAL Admin - "Sales Closings Report" dashboard providing detailed transaction analysis, including total revenue, sales count, and visual breakdowns by service type and geographic zone. . . . . . . . . . . . . . . . . 191

Figure I-62 BOPADIGITAL Admin - Sales Report demonstrating filtering capabilities, isolating performance data for a specific advisor (e.g., Roberto Mendoza) over the "Last Semester" period. . . . . . . . . . . . . . . . . . . . . . 191

Figure I-63 BOPADIGITAL Admin - "Export Report" functionality showing system feedback (modal alert) confirming the generation of a PDF file containing the current sales data visualization. . . . . . . . . . . . . . . . . . . . . . . . . . . .192

Figure I-64 BOPACORP Mobile App - Authentication and Main Dashboard views. 194

Figure I-65 BOPACORP Mobile App - Activity tracking and creation workflow. . . .195

Figure I-66 BOPACORP Mobile App - Detailed activity logging and client portfolio navigation. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .196

Figure I-67 BOPACORP Mobile App - Client administration and registration interface. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 197

Figure I-68 BOPACORP Mobile App - Final step of the new client registration process.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .198

Figure I-69 BOPACORP Mobile App - Comprehensive client profile and history view.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .199

Figure I-70 BOPACORP Mobile App - Operational lists for daily task and portfolio management.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .200

Figure I-71 BOPACORP Mobile App - User profile and application settings. . . . . . . . 201

Figure I-72 BOPACORP Mobile App - Administrative control panel and statistics. 202

XII

Figure I-73 BOPACORP Mobile App - Advanced system management and user administration.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .203

Figure I-74 BOPACORP Mobile App - Administrative tools for user onboarding and service catalog maintenance.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .204

Figure I-75 BOPACORP Website - Homepage featuring the main value proposition, navigation menu, and quick access to services and company information.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .205

Figure I-76 BOPACORP Website - "About Us" section detailing the company’s history, mission, and vision statements to establish corporate identity..205

Figure I-77 BOPACORP Website - complete Service Catalog displaying available corporate plans with filtering options by category, zone, and price. . . . . .206

Figure I-78 BOPACORP Website - Service Detail Modal for "Plan Corporativo 100", showing specific costs, coverage zones, and included benefits.. . .206

Figure I-79 BOPACORP Website - Search results view demonstrating active filters (Cloud, Digital Services, National Coverage) applied to the catalog.. . . 207

Figure I-80 BOPACORP Website - "Work with Us" (Careers) page highlighting employee benefits and listing current job openings. . . . . . . . . . . . . . . . . . . . . . . 207

Figure I-81 BOPACORP Website - Job Application Modal allowing candidates to submit personal details and upload their CV for a specific position.. . . .208

Figure I-82 BOPACORP Website - Success confirmation modal providing feedback to the user that their job application has been successfully sent.. . . . . . . .208

LIST OF ABBREVIATIONS

BOPACORP S.A. Telecommunications company and main client of the project

BOPADIGITAL Digital platform developed for BOPACORP S.A.

B2B Business-to-Business (commercial model between companies)

CMS Content Management System – module for website content administration

CRM Customer Relationship Management – module for managing business clients

and negotiations

DOC Document Management Module

EMP Employability / Application Module

MAT Offer Matrix Module

REP Reporting Module

SUP Supervision and Approvals Module

CAT Catalog and Website Module

SEG Basic Security Module

NOT Notifications Module

GPS Global Positioning System

UI User Interface

UX User Experience

JWT JSON Web Token (authentication mechanism)

TLS Transport Layer Security (encryption protocol for HTTPS)

PDF Portable Document Format

XIV

KPI Key Performance Indicator

RUC Unique Taxpayer Registry

ID Identifier (unique reference or key)

LIST OF SYMBOLS AND UNITS OF MEASUREMENTS

% Percentage (used in performance indicators such as availability or success

rate)

s Seconds (used for system response times, e.g., 3 s)

MB Megabytes (used for file upload size limits, e.g., 50 MB)

h Hours (used for availability and operational timeframes)

CHAPTER 1

RISK MANAGEMENT, SPRINT BACKLOGS, AND PROJECT SCHEDULING

1. 1 Risk Management

In this section, we identify, quantify, and classify the various risks that may arise during the

software development process of BOPADIGITAL. Additionally, a detailed assessment of the

likelihood of occurrence, the potential impact of each risk, and the corresponding protocols to

be followed in the event that they materialize is provided.

Description Probability Range

Not Probable: The event is highly unlikely to occur. 0% – 20%

Low Probability: The event is unlikely but possible. 21% – 40%

Moderate Probability: The event has an even chance

of occurring.

41% – 60%

High Probability: The event is likely to occur. 61% – 80%

Very High Probability: The event is almost certain

to occur.

81% – 100%

Table 1.1 Risk Probability Classification

1. 1.1 Identified Risks for the BOPADIGITAL Project

The following table outlines the risks identified for the BOPADIGITAL project, specifically

associated with its functional modules (CRM, MAT, DOC, SUP) and operational environment.

2

ID Risk Name Risk Description Probability Impact Action Protocol

001 Field

Connectivity

Failures

Sales advisors may lose

network connectivity

when uploading visits

or documents in remote

areas.

Very High Critical Implement a

robust offline-first

architecture that

stores data locally

and synchronizes

automatically once

connectivity is

restored.

002 Geolocation

Inaccuracy

Visit records depend on

accurate GPS coordinates,

which may vary across

devices or environments.

High High Apply tolerance

thresholds for location

validation and allow

supervised manual

correction with system

justification when GPS

data is unreliable.

003 Subsidy

Calculation

Complexity

(MAT)

Business rules for

automatic offer and

subsidy calculations may

be misinterpreted or

incorrectly implemented.

Moderate High Validate calculation

formulas with financial

stakeholders before

development and

implement exhaustive

unit tests for the

calculation engine.

3

Table continued from previous page

ID Risk Name Risk Description Probability Impact Action Protocol

004 Sales Staff

Resistance to

Change

Users accustomed to

manual processes may

resist adopting the mobile

application.

High Moderate Design an intuitive

UX/UI and implement

a training plan focused

on demonstrating

productivity and

administrative

workload reduction.

005 Storage Overload

(DOC Module)

Massive uploads of

contract images and legal

documents may exceed

the projected storage

capacity.

Low High Enable client-side

image compression

and use scalable

storage services with

defined retention

policies.

006 Approval Role

and Permission

Changes

The approval hierarchy

(Advisor → Supervisor

→ Manager) may change

during development or

operation.

Moderate Moderate Develop a flexible,

database-driven RBAC

system that supports

dynamic configuration

without hardcoded

logic.

Table 1.2 Identified Risks and Mitigation Strategies for the BOPADIGITAL Project

4

1. 2 Product backlog

ID Priority Dependencies Backlog Item Description Estimation

(hours)

PB1 0 None Research and Environment: Investigation

of the architecture (Docker, Node.js, React).

Configuration of the Git repository, branch

strategy, and CICD pipeline basics. Includes

creation of the initial "Hello World" to verify

connectivity.

6

PB2 0 PB1 Database Architecture: Design the complete

database schema (PostgreSQL) including

tables for Users, Clients, Matrices, Subsidies,

and Visits. Generation of the ER Diagram

and initial migration scripts.

6

PB3 0 PB1 Cloud Storage Setup: Configuration of

the file storage service (e.g., AWS S3 or

local server storage) to handle PDF and

image uploads securely. Includes access

key generation.

4

PB4 0 PB1 Backend Foundation: Setup of the Express.js

server, error handling middleware, CORS

configuration, and connection pooling for

the database.

4

PB5 1 PB2, PB4 Authentication Logic (Backend):

Implementation of JWT (JSON Web

Token) strategy, password hashing (Bcrypt),

and login/register endpoints.

8

5

Table continued from previous page

ID Priority Dependencies Backlog Item Description Estimation

(hours)

PB6 1 PB5 As a System Admin, I want to create

user accounts with specific roles (Advisor,

Supervisor, Manager) so that I can control

who accesses the platform.

6

PB7 1 PB5 As a Sales Advisor, I want to log in to the

Web Portal using my credentials so that I

can access my dashboard securely.

4

PB8 1 PB5 As a Sales Advisor, I want to log in to the

Mobile App using my credentials so that I

can work from the field.

6

PB9 2 PB7 As a User, I want to reset my password via

email verification in case I forget it, ensuring

I can recover access to my account.

8

PB10 2 PB1 Landing Page Structure: Implementation

of the main public website layout (Header,

Footer, Navigation) using React.

6

PB11 2 PB10 As a Visitor, I want to view the "About Us"

and "Contact" sections on the public site so

that I can learn about BOPACORP.

4

PB12 2 PB2, PB10 As a Visitor, I want to browse the Service

Catalog by categories so that I can easily

find the services I need.

8

PB13 2 PB12 As a Visitor, I want to search for specific

services in the catalog using keywords so

that I can find information faster.

4

6

Table continued from previous page

ID Priority Dependencies Backlog Item Description Estimation

(hours)

PB14 3 PB10 As an Applicant, I want to fill out a "Work

with Us" form on the public site so that I can

apply for a job.

6

PB15 3 PB3, PB14 As an Applicant, I want to upload my CV

(PDF) through the form so that HR can

review my profile.

6

PB16 1 PB2, PB4 Client Management API: Development of

backend endpoints (GET, POST, PUT,

DELETE) for the Clients and Prospects

table.

6

PB17 1 PB7, PB16 As a Sales Advisor, I want to register a new

Client on the Web Dashboard, entering their

RUC, name, and address.

6

PB18 1 PB8, PB16 As a Sales Advisor, I want to register a new

Client from the Mobile App, so that I can

add prospects while in the field.

8

PB19 1 PB17 As a Sales Advisor, I want to edit client

information on the Web to correct errors or

update contact details.

4

PB20 1 PB16 As a Sales Advisor, I want to filter my client

list by status (Active/Inactive) or name, so I

can find specific accounts quickly.

4

PB21 1 PB2 Geolocation Service: Implementation of the

backend logic to store and query geospatial

data (Latitude/Longitude) for visit records.

6

7

Table continued from previous page

ID Priority Dependencies Backlog Item Description Estimation

(hours)

PB22 1 PB8, PB21 As a Sales Advisor, I want to view a map on

the Mobile App showing my current location

to verify my GPS is working.

6

PB23 1 PB22 As a Sales Advisor, I want to "Check-In"

at a client’s location using the Mobile App

so that my visit start time and location are

recorded.

8

PB24 1 PB23 As a Sales Advisor, I want to "Check-Out"

adding a summary note of the visit so that

the interaction is fully documented.

6

PB25 1 PB24 As a Supervisor, I want to view the history of

visits for my team on a map or list to monitor

field compliance.

6

PB26 1 PB2 Matrix Calculation Engine: Implementation

of the backend logic to calculate base prices,

apply subsidies, and compute taxes.

10

PB27 1 PB7, PB26 As a Sales Advisor, I want to create a new

"Offer Matrix" on the Web, selecting a client

to start the quoting process.

4

PB28 1 PB27 As a Sales Advisor, I want to add multiple

services/products to the matrix so that I can

build a comprehensive offer.

6

PB29 1 PB26, PB28 As a Sales Advisor, I want the system to

automatically calculate the total cost and

applicable subsidies as I add items.

8

8

Table continued from previous page

ID Priority Dependencies Backlog Item Description Estimation

(hours)

PB30 2 PB29 As a Sales Advisor, I want to save the Matrix

as a "Draft" so that I can continue working

on it later without losing progress.

4

PB31 2 PB29 As a Sales Advisor, I want to generate a PDF

preview of the offer so that I can show it to

the client for immediate review.

8

PB32 2 PB31 As a Sales Advisor, I want to email the PDF

offer directly to the client from the system

to speed up communication.

4

PB33 2 PB3 Document Management API: Backend setup

to handle multipart form data for uploading

legal documents linked to a Matrix.

6

PB34 2 PB33 As a Sales Advisor, I want to upload the

Client’s RUC and ID scans to the specific

Offer Matrix to fulfill legal requirements.

6

PB35 2 PB34 As a Sales Advisor, I want to validate that

the uploaded files are readable and within

the size limit before saving.

4

PB36 2 PB30, PB34 As a Sales Advisor, I want to submit a

completed Matrix for approval, changing

its status to "Pending".

2

PB37 2 PB36 As a Supervisor, I want to receive a

notification (in-app or email) when an

advisor submits a matrix for approval.

4

9

Table continued from previous page

ID Priority Dependencies Backlog Item Description Estimation

(hours)

PB38 2 PB37 As a Supervisor, I want to view a "Pending

Approvals" inbox so that I can see which

offers require my attention.

4

PB39 2 PB38 As a Supervisor, I want to view the details

and documents of a pending Matrix to decide

whether to approve it.

4

PB40 2 PB39 As a Supervisor, I want to Approve a matrix

so that the sale can be finalized and sent to

billing.

2

PB41 2 PB39 As a Supervisor, I want to Reject a matrix

with a mandatory comment explaining the

reason for rejection.

4

PB42 3 PB2 Reporting Queries: Optimization of SQL

queries to aggregate sales data by month,

advisor, and region.

6

PB43 3 PB42 As a General Manager, I want to view a

dashboard with a bar chart showing "Sales

vs Targets" for the current month.

8

PB44 3 PB43 As a General Manager, I want to export

the monthly sales report to an Excel file for

further analysis.

6

PB45 0 All Integration Testing: Execution of end-to-end

tests covering the flow from Client Creation

- > Visit -> Matrix -> Approval.

16

10

Table continued from previous page

ID Priority Dependencies Backlog Item Description Estimation

(hours)

PB46 0 All Production Deployment: Configuration of

the production server, environment variables,

and final deployment of Web and Mobile

builds.

8

Table 1.3 Product Backlog for the BOPADIGITAL Project

11

1. 3 Sprint Backlog

1. 3.1 Sprint 1: Foundation, Auth & Public Web (Weeks 1–4)

Goal: Establish the technical architecture, security layer, and the public-facing ecosystem (Web

& Employability).

Product Backlog

Item

User Story / Description Tasks Assigned To

PB1 – PB4

(Infrastructure)

Technical setup of the core

infrastructure including

containers, database, cloud

storage, and backend

services.

- Repository and Docker

environment setup

- Database schema creation

- S3 bucket configuration

- Express.js base configuration

Gabriel Tumbaco

Nahim Díaz

PB5 – PB9 (Auth

& Roles)

Implementation of

authentication and

authorization using

JWT and role-based access

control.

- Login and registration

endpoints

- Definition of Admin, Advisor,

and User roles

- Password recovery logic

Anthony

Navarrete

Salvador Muñoz

PB10 – PB13

(Public Web)

Development of the public-

facing website including

landing page and service

catalog.

- React layout (Header and

Footer)

- Dynamic service catalog

- Search functionality

Gabriel Tumbaco

Shirley Aragon

PB14 – PB15

(Employability)

Implementation of the

employability module for

applicant registration and

CV submission.

- “Work with Us” form

- CV file validation

- Secure CV storage

Shirley Aragon

Table 1.4 Sprint 1 Backlog — Foundation, Authentication and Public Web

12

1. 3.2 Sprint 2: CRM Core & Geolocation (Weeks 5–8)

Goal: Enable the management of the client portfolio and tracking of field operations (Visits).

Product Backlog

Item

User Story / Description Tasks Assigned To

PB16 – PB20

(Client Mgmt)

Client CRUD operations

and filtering for effective

portfolio management.

- Client API (PostgreSQL)

- Web forms for client

management

- Mobile “Add Client” view

- Search and status filters

Salvador Muñoz

Nahim Díaz

Anthony

Navarrete

PB21 – PB22

(Geo Services)

Backend geolocation

services and mobile map

visualization.

- Spatial data setup (PostGIS /

Geometry)

- Mobile map integration

Anthony

Navarrete

Shirley Aragon

PB23 – PB25

(Visit Logic)

Visit tracking through

check-in and check-out

processes.

- Visit timer logic

- Coordinate capture on check-

in

- Supervisor visit map view

Anthony

Navarrete

Nahim Díaz

PB26, PB29 (Calc

Engine)

Implementation of pricing,

subsidy, and calculation

logic.

- Subsidy calculation algorithm

- Total cost computation

Shirley Aragon

Salvador Muñoz

PB27 – PB28

(Matrix UI)

User interface for building

offer matrices.

- Product/service selection UI

- Cart state management

Gabriel Tumbaco

Salvador Muñoz

PB30 (Drafts) Save partially completed

matrices for later

continuation.

- “Save as Draft” functionality Salvador Muñoz

13

Product Backlog

Item

User Story / Description Tasks Assigned To

PB31 – PB32

(PDF & Email)

Generation and delivery of

offer documents.

- PDF library integration (e.g.,

PDFKit)

- Email service configuration

(SMTP)

Nahim Díaz

Gabriel Tumbaco

PB33 – PB35

(Doc Upload)

Legal document upload and

validation.

- Multipart upload API

- ID / RUC scanning UI

- File validation

Shirley Aragon

Anthony

Navarrete

PB36 – PB41

(Approvals)

Supervisor approval

workflow for offer matrices.

- State machine (Pending →

Approved / Rejected)

- Notification system

- Approval inbox UI

Anthony

Navarrete

Salvador Muñoz

PB42 – PB44

(Reporting)

Business intelligence

dashboards and report

exports.

- Aggregation queries (sales by

month)

- Chart components (Recharts)

- Excel export logic

Shirley Aragon

Nahim Díaz

PB45 (QA) End-to-end validation of the

system.

- Integration testing (Cypress /

Selenium)

- Bug fixing sprint

All Team

Members

PB46 (Deploy) Final production

deployment and

documentation.

- Server configuration

- Domain setup and SSL

- Final user manual

Nahim Díaz

Gabriel Tumbaco

Table 1.5 Sprint 2 Backlog — CRM Core, Geolocation, and Business Logic

14

1. 4 Scheduling

ID Description Details Product Backlog

Items

Hours Earliest

Start

Latest

Finish

Float

A System

Foundation

& DB

Docker setup,

PostgreSQL

schema, and

backend base

architecture.

PB1, PB2, PB3,

PB4

20 0 20 0

B Auth & Security

Core

JWT, roles, and

user management

implementation.

PB5, PB6, PB7,

PB8, PB9

32 20 52 0

C Public Ecosystem Landing page,

catalog, and

employability

modules.

PB10–PB15 34 20 192 138

D CRM & Field

Operations

Client

management,

geolocation, and

visit tracking.

PB16–PB25 60 52 112 0

E Matrix

Calculation

Engine

Pricing, subsidies,

PDF generation,

and drafts.

PB26–PB32 44 112 156 0

F Docs & Approval

Workflow

Legal docs,

validation,

and approval

processes.

PB33–PB41 36 156 192 0

15

ID Description Details Product Backlog

Items

Hours Earliest

Start

Latest

Finish

Float

G BI, QA &

Deployment

Dashboards,

testing, and

production

release.

PB42–PB46 44 192 236 0

Table 1.6 Project Scheduling and Critical Path Overview

Figure 1.1 Activity on Arrow Diagram

CHAPTER 2

STATIC SYSTEM MODELING AND ARCHITECTURAL DESIGN

17

# 18

# 2.1 Use Case Diagram

BOPADIGITAL

Contact Advisor from Catalog

View Job Vacancies

Apply to Job Vacancy

Access Control Panel

Edit Product Delete Product Register Product extension points

Manage Product Catalog

Register New Client

Update Existing Client

Assign Client to Advisor

Calcular Subsidio extension points

Edit Negotiations

Register Visit

Register Visit extension points

View Visit History

Unassign or Remove Client from Advisor

Update Negotiation Status

Disable Closed Negotiations

View Advisor Recent Activity

View Costs per Advisor

Get Sales Report

Get Progress Report

Authenticate in System

Upload Resume

Get GPS Location

Edit Product

Register Product

Delete Product

Calculate Subsidy

Export Report

Business Client

Sales Advisor Candidate

Web Administrator

Sales Advisor

Immediate Supervisor

Manager

<<Include>>

<<Include>>

<<Include>>

<<Include>>

<<Include>>

<<Include>>

<<Extend>>

<<Include>>

<<Extend>>

<<Include>>

<<Include>>

<<Include>>

<<Extend>>

<<Extend>>

<<Extend>>

<<Include>>

<<Include>>

<<Include>>

Powered By Visual Paradigm Community Edition

19

Figure 2.1 BOPADIGITAL Use Case Diagram Part 1

# 20

CRM

Filtrar listas de cliente segun metricas

Offer Matrix Management

Crear matrices para clientes específicos

Solicitar aprobación de supervisor

Consultar estado de aprobación de matrices

Revisar disponibilidad de operadora

extension pointsRechazar matrices

Visualizar y aprobar nuevas matrices

Rechazar matrices

Document Management System

Etiquetar documentación extension points

Añadir documentación de cliente

Etiquetar documentación

Descargar documentación extension points

Revisar documentación subida a perfil

Descargar documentación

Consultar clientes y su estado de

documentación

Reporting, Performance & Analysis System

Filtrar reportes extension points

Generar reportes de ventas y cierre

Filtrar reportes

Comparar metricas entre asesores

extension points

Visualizar métricas de asesores Generar reportes en PDF o Excel

Comparar metricas entre asesores

Operadora

Administradores

Supervisor Inmediato

Asesor Comercial

<<Include>>

<<Include>>

<<Extend>>

<<Extend>>

<<Include>>

<<Extend>>

<<Extend>>

<<Extend>>

<<Include>>

Powered By Visual Paradigm Community Edition

# Figure 2.2

# BOPADIGITAL Use Case Diagram Part 2

21

2. 2 Use Case Documentation

### 22

Name of Use Case: Contact an Advisor from the Catalog Created By: BOPADIGITAL Last Updated By: BOPADIGITAL Date Created: 21/12/25 Last Revision Date: 11/01/2026

Description: The Business Client browses the service catalog and requests to be contacted by a sales advisor in order to start a negotiation about a product or service of interest. Actors: Business Client Preconditions: 1. The public website must be accessible.

2. The service catalog must contain available products/services.

3. The contact form must be functional.

Postconditions: 1. A contact request is registered in the system.

2. The business client receives an on-screen confirmation message.

3. The assigned advisor receives a notification of the request.

Flow: 1. The Business Client accesses the BOPACORP public website.

2. The System displays the service catalog organized by categories

(Voice, Connectivity, Digital Services).

3. The Business Client navigates through the available categories.

4. The Business Client selects a specific service to view details.

5. The System displays service information including costs, benefits, and

usage conditions.

6. The Business Client clicks the “Contact Advisor” button.

7. The System displays a contact form requesting: Company Name, Tax

ID (RUC), Contact Name, Email, Phone Number.

8. The Business Client completes all form fields.

9. The Business Client clicks “Submit Request”.

10. The System validates the entered information.

11. The System creates a contact request record in the database.

12. The System displays a confirmation message: “We will contact you

shortly.” Alternative Flows: 10a. Validation fails

1. The System displays specific error messages indicating missing or

invalid fields.

2. The Business Client corrects the information.

3. The flow returns to step 9.

Exceptions: 2. Catalog unavailable or empty

1. The System displays: “Service catalog temporarily unavailable.

Please try again later.”

2. The use case ends.

11. Contact request cannot be created

1. The System displays: “Your request could not be processed. Please

try again.”

2. The use case ends.

### Table 2.1 Use Case Documentation - Contact an Advisor from the Catalog

### 23

Requirements: RF-CAT-004: The system shall allow the business client to contact a sales advisor to initiate a negotiation regarding selected catalog items

### Table 2.1 (continued)

### 24

Name of Use Case: View Job Vacancies Created By: BOPADIGITAL Last Updated By: BOPADIGITAL Date Created: 21/12/25 Last Revision Date: 11/01/2026

Description: The Candidate reviews the list of active job opportunities published by BOPACORP to examine requirements, job descriptions, and closing dates. Actors: Sales Advisor Candidate Preconditions: 1. The employability module must be active on the website.

2. The job database must be accessible.

3. At least one active job vacancy must exist.

Postconditions: 1. The candidate views detailed information of the selected vacancy. Flow: 1. The Candidate accesses the “Work With Us” section on the BOPACORP website.

2. The System retrieves available vacancies from the database.

3. The System displays a list including Job Title, City, and Publication

Date.

4. The Candidate reviews the vacancy list.

5. The Candidate selects a specific vacancy.

6. The System displays full vacancy details including job description,

academic requirements, years of experience, and responsibilities. Alternative Flows: 2a. No active vacancies found

1. The System displays: “There are currently no open job

opportunities.”

2. The System suggests subscribing to vacancy notifications.

3. The use case ends.

Exceptions: 2. Database unavailable

1. The System displays: “Service temporarily unavailable. Please try

again later.”

2. The System logs the error.

3. The use case ends.

Requirements: RF-EMP-001: The system shall allow the sales advisor candidate to view available vacancies, displaying the position title, description, requirements, and publication date.

### Table 2.2 Use Case Documentation - View Job Vacancies

### 25

Name of Use Case: Apply for a Job Vacancy Created By: BOPADIGITAL Last Updated By: BOPADIGITAL Date Created: 21/12/25 Last Revision Date: 11/01/2026

Description: The Candidate submits a formal job application by completing an application form and uploading a résumé in PDF format. Actors: Sales Advisor Candidate Preconditions: 1. The candidate has viewed the vacancy details (UC-02).

2. The application system is operational.

3. The résumé is available in PDF format (max 50MB).

Postconditions: 1. The job application is stored in the system.

2. The résumé file is stored and linked to the application.

3. The candidate receives confirmation on screen and by email.

Flow: 1. The Candidate is viewing the details of a job vacancy of interest.

2. The Candidate clicks the “Apply” button on the specific vacancy.

3. The System displays the application form requesting: Full Name,

National ID Number, Email, Phone Number, Address.

4. The Candidate completes all form fields with personal information.

5. The System requests uploading the résumé in PDF format with a

maximum size of 50MB.

6. The Candidate selects and uploads the résumé file from the device.

7. The System validates the file format and size.

8. The System validates that all required fields are complete and correct.

9. The Candidate clicks “Submit Application.”

10. The System stores the application in the database.

11. The System stores the résumé file.

12. The System sends a confirmation email to the provided address.

13. The System displays the success message: “Your application has been

successfully submitted.” Alternative Flows: 7a. If the file is not PDF:

1. The System rejects the file and displays: “Only PDF files are

allowed.”

2. The flow returns to step 5.

7b. If the file exceeds 50MB:

1. The System rejects the file and displays: “The file size must not exceed

50MB.”

2. The flow returns to step 5.

8a. If field validation fails:

1. The System displays specific error messages for each invalid or

missing field.

2. The Candidate corrects the errors according to the instructions.

3. The flow returns to step 9.

### Table 2.3 Use Case Documentation - Apply for a Job Vacancy

### 26

Exceptions: 10. If application storage fails:

1. The System displays the message: “The application could not be

processed. Please try again.”

2. The System logs the error for administrator review.

3. The use case ends.

Requirements: RF-EMP-002, RF-EMP-003, RF-EMP-004, RF-EMP-005

### Table 2.3 (continued)

### 27

Name of Use Case: Access Control Panel with Credentials Created By: BOPADIGITAL Last Updated By: BOPADIGITAL Date Created: 21/12/25 Last Revision Date: 11/01/2026

Description: The Web Administrator authenticates into the system using valid user credentials (username and password) in order to access the Content Management System (CMS) administrative control panel. Actors: Web Administrator Preconditions: 1. The administrator must have valid credentials previously registered in the system.

2. The authentication service must be operational.

3. The administrator account must be active.

Postconditions: 1. The administrator successfully gains access to the CMS administration panel.

2. A user session is created with a valid JWT token.

3. The access event is recorded in the system log with date, time, and

user information.

Flow: 1. The Web Administrator navigates to the administrative login URL.

2. The System displays the login form with the following fields:

Username/Email and Password.

3. The Web Administrator enters their username or email.

4. The Web Administrator enters their password.

5. The Web Administrator clicks the “Log In” button.

6. The System validates the credentials against the users database.

7. The System verifies that the administrator account is active.

8. The System verifies the administrator role permissions.

9. The System generates a JWT token containing the user ID, role, and

expiration time.

10. The System creates a secure user session storing the token.

11. The System records the successful access event including timestamp

and IP address.

12. The System redirects the administrator to the main CMS dashboard.

Alternative Flows: 6a. Invalid credentials (incorrect username or password)

1. The System increments the failed login attempt counter for the

account.

2. The System displays the error message: “Invalid username or

password.”

3. The System allows the administrator to retry the login process.

4. The flow returns to step 2 of the main flow.

6b. Three consecutive failed login attempts

1. The System temporarily locks the account for 15 minutes.

2. The System displays the message:

“Account locked due to multiple failed login attempts. Please try again in 15 minutes.”

### Table 2.4 Use Case Documentation - Access Control Panel with Credentials

### 28

3. The System sends a security alert email to the administrator.

4. The use case ends.

7a. Inactive or disabled account

1. The System displays the message:

“Your account is disabled. Please contact the system administrator.”

2. The use case ends.

Exceptions: 6. Authentication service unavailable

1. The System displays the message:

“Authentication service temporarily unavailable. Please try again later.”

2. The System logs the error for technical review.

3. The use case ends.

9. JWT token generation failure

1. The System logs the internal error.

2. The System displays the message:

“Login error. Please try again.”

3. The use case ends.

Requirements: RF-SEG-001: The system shall require authentication using a valid username and password to allow access to the internal application. RF-CMS-001: The system shall allow the web administrator to access the content management panel using credential-based authentication (username and password).

### Table 2.4 (continued)

### 29

Name of Use Case: Manage Product Catalog Created By: BOPADIGITAL Last Updated By: BOPADIGITAL Date Created: 21/12/25 Last Revision Date: 11/01/2026

Description: The Web Administrator can create, edit, and delete products and services within the public catalog of the BOPACORP website in order to keep service information updated and available for business clients. Actors: Web Administrator. Preconditions: 1. The administrator must be authenticated in the system (Use Case 04).

2. The CMS module must be accessible.

3. The administrator must have catalog management permissions.

Postconditions: 1. All changes made are saved in the database.

2. Changes are immediately reflected in the public service catalog.

3. The system logs the operation with user, date, and action performed.

Flow: 1. The Web Administrator accesses the “Product Catalog” section within the CMS panel.

2. The System retrieves and displays the current list of existing products

and services including: Name, Category, Price, and Status (Active/Inactive).

3. The Web Administrator reviews the list of products.

4. The Web Administrator selects one available action: Register new

product, Edit existing product, or Delete product.

5. The System executes the corresponding flow based on the selected

action.

6. The System confirms the operation performed.

7. The System updates the public catalog in real time.

Alternative Flows: 4a. Register new product

1. The System displays a creation form with the following fields: Name,

Description, Category (Voice / Connectivity / Digital), Price, Benefits, and Terms of Use.

2. The Web Administrator completes all required fields.

3. The Web Administrator optionally uploads a representative product

image.

4. The Web Administrator clicks “Save Product.”

5. The System validates that all mandatory fields are completed.

6. The System validates price format and numeric fields.

7. The System creates a new product record in the database.

8. The flow continues at step 6 of the main flow.

4b. Edit existing product

1. The System displays a pre-filled edit form with the current product

data.

2. The Web Administrator modifies the desired fields.

3. The Web Administrator clicks “Save Changes.”

4. The System validates the modified data.

5. The System updates the product record in the database.

6. The System logs the modification with date, time, and user.

### Table 2.5 Use Case Documentation - Manage Product Catalog

### 30

7. The flow continues at step 6 of the main flow.

4c. Delete product

1. The System displays a confirmation dialog:

“Are you sure you want to delete this product? This action cannot be undone.”

2. The Web Administrator confirms the deletion.

3. The System verifies that the product is not referenced in active

negotiations.

4. The System removes the product from the active catalog.

5. The flow continues at step 6 of the main flow.

Exceptions: 5. Validation error (4a or 4b):

1. The System displays specific validation error messages.

2. The Web Administrator corrects the indicated errors.

3. The flow returns to the corresponding alternative flow step.

3. Product referenced in active negotiations (4c):

1. The System displays the warning:

“This product cannot be deleted because it is used in active negotiations.”

2. The System suggests disabling the product instead of deleting it.

3. The flow returns to step 4 of the main flow.

Requirements: RF-CMS-003: The system shall allow the web administrator to create new products and services within the catalog

RF-CMS-004: The system shall allow the web administrator to update the information of existing products and services in the catalog

RF-CMS-005: The system shall allow the web administrator to delete products and services from the catalog.

### Table 2.5 (continued)

### 31

Name of Use Case: Register New Client Created By: BOPADIGITAL Last Updated By: BOPADIGITAL Date Created: 21/12/25 Last Revision Date: 11/01/2026

Description: The Sales Advisor or Immediate Supervisor creates a new business client record in the CRM system including all commercial and contact information. Actors: Sales Advisor, Immediate Supervisor Preconditions: 1. The user must be authenticated with the appropriate role.

2. The CRM module must be accessible.

3. The user must have permission to create clients.

Postconditions: 1. A new client record is created in the CRM database.

2. The client becomes available to be assigned to sales advisors.

3. A unique client ID is generated by the system.

Flow: 1. The User navigates to the “Clients” section within the CRM module.

2. The User clicks the “Add New Client” button.

3. The System displays the client registration form with mandatory

fields.

4. The User enters the following information: Client RUC, Business

Name or Trade Name, Number of Active Services, Current Monthly Billing, Contact Person Name, Contact Phone Number, Contact Email, and Company Address.

5. The System validates the RUC format in real time.

6. The System verifies that the RUC does not already exist in the

database.

7. The User clicks “Save Client.”

8. The System validates that all mandatory fields are completed.

9. The System validates email and phone formats.

10. The System creates the client record in the database.

11. The System generates and assigns a unique client ID.

12. The System displays a success message including the client ID.

Alternative Flows: 6a. RUC already exists

1. The System displays the message:

“A client with this RUC already exists.”

2. The System displays a “View Existing Client” button.

3. The User may cancel or modify the entered RUC.

4. The use case ends if the user cancels.

8a. Missing required fields

1. The System highlights missing fields.

2. The System displays the message:

“Please complete all required fields.”

3. The User completes the missing information.

4. The flow returns to step 7.

9a. Invalid email or phone format

1. The System displays specific validation messages.

### Table 2.6 Use Case Documentation - Register New Client

### 32

2. The User corrects the data.

3. The flow returns to step 7.

Exceptions: 10. Database failure

1. The System displays the message:

“The client could not be created. Please try again.”

2. The System logs the error.

3. The entered data remains in the form.

4. The use case ends.

Requirements: RF-CRM-001: The system shall allow the sales advisor to fill out a client registration form including the company’s RUC (tax ID), business name, number of active services, and current monthly billing.

### Table 2.6 (continued)

### 33

Name of Use Case: Update Existing Client Created By: BOPADIGITAL Last Updated By: BOPADIGITAL Date Created: 21/12/25 Last Revision Date: 11/01/2026

Description: The Sales Advisor or Immediate Supervisor updates contact, commercial, or administrative information of an existing business client to keep records current. Actors: Sales Advisor, Immediate Supervisor Preconditions: 1. The user must be authenticated in the system.

2. The client record must exist in the database.

3. Sales Advisors can only update clients assigned to them.

4. Immediate Supervisors can update any client within their team.

Postconditions: 1. Client information is updated in the database.

2. The change history is recorded with date, time, and user.

3. The updates are immediately visible in the client profile.

Flow: 4. The User accesses the CRM module.

5. The User searches for a client using RUC or Business Name.

6. The System displays a list of matching clients.

7. The User selects the client to update.

8. The System verifies the user’s permissions.

9. The System displays the client details form with current information.

10. The User modifies the desired fields.

11. The User clicks “Save Changes.”

12. The System validates the modified data.

13. The System updates the client record in the database.

14. The System records the change in the audit history.

15. The System displays a confirmation message.

Alternative Flows: 5a. Unauthorized access

1. The System displays:

“Access denied. This client is not assigned to you.”

2. The User is redirected to their assigned client list.

3. The use case ends.

9a. Validation failure

1. The System displays specific error messages.

2. The User corrects the errors.

3. The flow returns to step 8.

Exceptions: 3. Search returns no results

1. The System displays:

“No clients found with the given criteria.”

2. The User may modify the search or cancel.

10. Database update failure

### Table 2.7 Use Case Documentation - Update Existing Client

### 34

1. The System displays:

“Changes could not be saved. Please try again.”

2. The System logs the error.

3. The use case ends if the user cancels.

Requirements: RF-CRM-002: The system shall allow the sales advisor to update the information of assigned business clients.

### Table 2.7 (continued)

### 35

Name of Use Case: Edit Negotiations Created By: BOPADIGITAL Last Updated By: BOPADIGITAL Date Created: 21/12/25 Last Revision Date: 11/01/2026

Description: The Sales Advisor modifies the details and observations of an ongoing negotiation with an assigned business client in order to keep the commercial progress updated. Actors: Sales Advisor Preconditions: 1. The sales advisor must be authenticated in the system.

2. The negotiation must exist in the system and be in active status.

3. The associated client must be assigned to the sales advisor.

4. The negotiation must not be in closed or canceled status.

Postconditions: 1. The negotiation details are updated in the database.

2. The changes are recorded in the negotiation history with a timestamp.

3. The last modification date of the negotiation is updated.

Flow: 1. The Sales Advisor accesses the client profile within the CRM module.

2. The Sales Advisor navigates to the client’s negotiations section.

3. The System displays the active negotiations associated with the client

and their current status.

4. The Sales Advisor selects the specific negotiation to edit.

5. The Sales Advisor clicks the “Edit Negotiation” button.

6. The System displays the edit form with modifiable fields including:

Progress observations, Estimated closing date, and additional notes.

7. The Sales Advisor modifies the required fields.

8. The Sales Advisor clicks “Save Changes.”

9. The System validates that the entered data is correct (for example, a

valid future date).

10. The System updates the negotiation record in the database.

11. The System records the change in the negotiation history with

timestamp and user.

12. The System displays a confirmation message indicating that the

negotiation was successfully updated. Alternative Flows: 9a. If data validation fails:

1. The System displays specific error messages (for example: “The

closing date must be a future date”).

2. The Sales Advisor corrects the indicated errors.

3. The flow returns to step 8.

Exceptions: 4. If the negotiation is in closed or canceled status:

1. The System displays the message “Closed or canceled negotiations

cannot be edited.”

2. The System disables the edit option.

3. The use case ends.

5. If the advisor attempts to edit a negotiation belonging to another advisor:

### Table 2.8 Use Case Documentation -Edit Negotiations

### 36

1. The System displays the message “Access denied. This negotiation

belongs to another advisor.”

2. The use case ends.

10. If the database update fails:

1. The System displays the message “Error saving changes. Please try

again.”

2. The System logs the error.

3. The use case ends.

Requirements: RF-MAT-001: The system shall allow the sales advisor to create a new offer matrix associated with a business client and an ongoing negotiation. RF-MAT-003: The system shall automatically calculate the applicable subsidy range based on client billing and the number of proposed services, displaying the total estimated benefit amount.

### Table 2.8 (continued)

### 37

Name of Use Case: Register Visit Created By: BOPADIGITAL Last Updated By: BOPADIGITAL Date Created: 21/12/25 Last Revision Date: 11/01/2026

Description: The Sales Advisor registers an in-person visit carried out with a business client, including automatic GPS location, date, time, visit type, and meeting observations. Actors: Sales Advisor Preconditions: 1. The advisor must be authenticated in the mobile application.

2. GPS functionality must be available and enabled on the mobile device.

3. The client must be assigned to the sales advisor.

4. There must be an active negotiation with the client.

Postconditions: 1. A visit record is created in the database with precise GPS coordinates.

2. The visit is automatically added to the client’s visit history.

3. The immediate supervisor can view and verify the registered visit.

4. The client’s last contact date is updated.

Flow: 1. The Sales Advisor opens the BOPADIGITAL mobile application.

2. The Sales Advisor navigates to the profile of the client being visited.

3. The Sales Advisor clicks the “Register Visit” button.

4. The System requests location permissions if they are not enabled.

5. The System automatically captures the device’s GPS coordinates

including latitude, longitude, and accuracy.

6. The System displays the visit registration form pre-filled with current

date, current time, and captured GPS location.

7. The Sales Advisor selects the visit type from a dropdown list: Initial

Visit, Follow-up, Negotiation, Closing, or Post-Sale.

8. The Sales Advisor enters detailed observations and notes about the

visit.

9. The Sales Advisor clicks “Save Visit.”

10. The System validates that all required fields are completed.

11. The System creates a visit record linked to the client and the active

negotiation.

12. The System stores the GPS coordinates for later verification.

13. The System displays a confirmation message including the registered

GPS coordinates. Alternative Flows: 5a. If GPS is not available or the signal is weak:

1. The System displays a warning message indicating that GPS is not

available.

2. The Sales Advisor can choose to wait for GPS signal, continue without

location, or cancel the registration.

3. If continuing without GPS, the flow proceeds without GPS data.

4. The visit is marked as “Unverified GPS.”

10a. If validation fails:

1. The System displays error messages indicating missing fields.

2. The Sales Advisor completes the required information.

### Table 2.9 Use Case Documentation - Register Visit

### 38

3. The flow returns to step 9.

Exceptions: 4. If the user has denied location permissions:

1. The System displays a message indicating that location permission is

required.

2. The System offers to open the device permission settings.

3. If permissions are not granted, the use case ends.

11. If saving fails due to connectivity issues:

1. The System displays an error message indicating connection issues.

2. The System temporarily stores the visit data locally.

3. The System synchronizes the data automatically once connectivity is

restored. Requirements: RF-CRM-005: The system shall allow the sales advisor to register a new client visit by entering date, time, observations, and GPS location automatically obtained from their mobile device.

### Table 2.9 (continued)

### 39

Name of Use Case: View Visit History Created By: BOPADIGITAL Last Updated By: BOPADIGITAL Date Created: 21/12/25 Last Revision Date: 11/01/2026

Description: The Sales Advisor or Immediate Supervisor reviews the complete and chronological history of all visits made to a specific business client for followup analysis. Actors: Sales Advisor, Immediate Supervisor Preconditions: 1. The user must be authenticated in the system.

2. The client record must exist in the database.

3. Sales Advisors can only view visits of their assigned clients.

4. Supervisors can view visits of all clients in their team.

Postconditions: 1. The visit history is displayed in descending chronological order.

2. The user can view full details of each individual visit

Flow: 1. The User accesses the client profile within the CRM module.

2. The User clicks the “Visit History” tab.

3. The System retrieves all visits associated with the client.

4. The System sorts visits by date and time in descending order.

5. The System displays a list of visits including date, time, visit type,

advisor, summarized observations, GPS location link, and verification status.

6. The User selects a specific visit to view detailed information.

7. The System displays the full visit details including complete

observations and an interactive GPS map. Alternative Flows: 3a. If no visits exist:

1. The System displays a message indicating that no visits have been

registered.

2. If the user is an advisor, the system displays an option to register the

first visit.

5a. If filters are applied:

1. The System allows filtering by date range, visit type, and advisor.

2. The System updates the displayed list based on the selected filters.

Exceptions: 3. If the database query fails:

1. The System displays an error message: "The visit history could not be

loaded. Please try again".

2. The System logs the error for technical review.

3. The use case ends.

7. If GPS coordinates are not available for the selected visit:

1. The System displays the remaining visit information.

### Table 2.10 Use Case Documentation - View Visit History

### 40

2. Instead of the map, the System displays: "GPS location not available

for this visit".

Requirements: RF-CRM-007: The system shall allow the sales advisor to view a history of visits made to their assigned business clients

### Table 2.10 (continued)

### 41

Name of Use Case: Update negotiation status Created By: BOPADIGITAL Last Updated By: BOPADIGITAL Date Created: 21/12/25 Last Revision Date: 11/01/2026

Description: The Sales Advisor changes the current status of a negotiation to reflect the progress in the sales process according to the advancement with the client. Actors: Sales Advisor. Preconditions: 1. The advisor must be authenticated in the system.

2. The negotiation must exist and be active in the system.

3. The client must be assigned to the sales advisor.

4. The new status must be valid according to the system status flow

Postconditions: 1. The negotiation status is updated in the database.

2. The status change is recorded in the negotiation history with a

timestamp.

3. Appropriate workflows or notifications are triggered according to the

new status.

4. The advisor’s metrics are automatically updated.

Flow: 1. The Sales Advisor accesses the negotiation detail page of the client.

2. The System prominently displays the current status of the negotiation.

3. The Advisor clicks the “Update Status” button.

4. The System displays a dialog with the next available statuses

according to the flow: Prospecting, Initial Contact, Active Negotiation, Closing, Post-Sale.

5. The Advisor selects the desired new status.

6. The System displays an optional text field to add notes about the status

change.

7. The Advisor optionally enters explanatory notes about the change.

8. The Advisor clicks “Confirm Change”.

9. The System validates that the status transition is allowed (critical

stages cannot be skipped).

10. The System updates the negotiation status in the database.

11. The System records the change in the history with: Previous status,

New status, User, Date and time, Entered notes.

12. The System executes specific actions according to the new status (e.g.,

notify the Immediate Supervisor if it moves to Closing).

13. The System displays a confirmation message: “The negotiation status

has been updated to [new status]”. Alternative Flows: 9a. If the status transition is invalid (e.g., attempting to skip from Prospecting directly to Closing):

1. The System displays a warning message: “Invalid status transition.

You must go through the intermediate stages”.

2. The System displays the next valid status.

3. The flow returns to step 4.

12a. If the new status is “Closing”:

1. The System sends an automatic notification to the Immediate

Supervisor.

### Table 2.11 Use Case Documentation - Update negotiation status

### 42

2. The System requests additional information required for closing

(estimated amount, probable date).

3. The flow continues normally.

Exceptions: 10. If the database update fails:

1. The System displays an error message: “The status could not be

updated. Please try again”.

2. The System logs the error.

3. The negotiation status remains unchanged.

4. The use case ends.

1. If the negotiation is closed or canceled:

1. The System does not display the “Update Status” button.

2. The System displays an informational message: “This negotiation is

closed and cannot be modified”.

3. The use case ends.

Requirements: RF-CRM-008: The system shall allow the sales advisor to update the negotiation status with an assigned business client.

### Table 2.11 (continued)

### 43

Name of Use Case: Assign client to advisor Created By: BOPADIGITAL Last Updated By: BOPADIGITAL Date Created: 21/12/25 Last Revision Date: 11/01/2026

Description: The Immediate Supervisor assigns a business client to a specific sales advisor from their team so that the advisor can start or continue the commercial negotiation process. Actors: Immediate Supervisor. Preconditions: 1. The supervisor must be authenticated in the system.

2. The client must exist in the database.

3. The destination sales advisor must be active and belong to the

supervisor’s team.

4. The client may be unassigned or already assigned to another advisor.

Postconditions: 1. The client is assigned to the selected sales advisor.

2. The advisor can now view and manage the client in their portfolio.

3. The assignment is recorded in the system with date, time, and the

supervisor who performed the assignment.

4. The advisor receives a notification of the new assignment.

Flow: 1. The Immediate Supervisor navigates to the “Client Management” section in the CRM module.

2. The Supervisor searches for the client to assign by RUC or Business

Name.

3. The System displays the search results with basic client information.

4. The Supervisor selects the specific client.

5. The System displays the client details and the current assignment

status.

6. The Supervisor clicks the “Assign to Advisor” or “Reassign” button.

7. The System displays a list of available sales advisors in the

supervisor’s team with: Full name, Sales zone, Current number of assigned clients, Current workload.

8. The Supervisor selects the destination sales advisor from the list.

9. The Supervisor optionally enters notes about the reason for the

assignment.

10. The Supervisor clicks “Confirm Assignment”.

11. The System validates that the client is not already assigned to the same

advisor.

12. The System creates or updates the assignment relationship in the

database.

13. The System records the assignment in the audit log.

14. The System sends a notification to the sales advisor about the newly

assigned client.

15. The System displays a confirmation message: “[Client] has been

successfully assigned to [Advisor]”.

Alternative Flows: 11a. If the client is already assigned to the selected advisor:

### Table 2.12 Use Case Documentation - Assign client to advisor

### 44

1. The System displays an alert: “This client is already assigned to

[Advisor Name]”.

2. The System asks whether the supervisor wants to change the

assignment to another advisor.

3. If the supervisor confirms, the flow returns to step 7.

4. If the supervisor cancels, the use case ends.

6a. If the client is already assigned to another advisor:

5. The System displays information about the current advisor.

6. The System displays a warning: “This client is currently assigned to

[Name]. Do you want to reassign?”.

7. The Supervisor may: Continue with the reassignment, View the client

history before deciding, or Cancel.

8. If the Supervisor continues, the flow proceeds normally from step 7.

Exceptions: 12. If the assignment operation fails in the database:

1. The System displays an error message: “The assignment could not be

completed. Please try again”.

2. The System logs the error for technical review.

3. The assignment is not performed.

4. The use case ends.

14. If sending the notification to the advisor fails:

1. The System completes the assignment anyway.

2. The System records that the notification failed.

3. The System will attempt to resend the notification later.

Requirements: RF-CRM-012: The system shall allow the immediate supervisor to assign business clients to sales advisors to initiate negotiations.

### Table 2.12 (continued)

### 45

Name of Use Case: Unassign or remove client from an advisor Created By: BOPADIGITAL Last Updated By: BOPADIGITAL Date Created: 21/12/25 Last Revision Date: 11/01/2026

Description: The Immediate Supervisor removes the assignment relationship between a business client and a sales advisor, freeing the client for potential reassignment or archiving. Actors: Immediate Supervisor Preconditions: 1. The supervisor must be authenticated in the system.

2. The client must currently be assigned to a sales advisor.

3. The advisor and the client must belong to the supervisor’s

team/portfolio. Postconditions: 1. The assignment relationship is removed from the database.

2. The client becomes available to be reassigned to another advisor.

3. The sales advisor no longer has access to modify that client.

4. The unassignment is recorded in the audit history with reason and user.

Flow: 1. The Immediate Supervisor accesses the team management module in the CRM.

2. The Supervisor views the list of sales advisors on their team.

3. The Supervisor selects a specific advisor to view their client portfolio.

4. The System displays all clients currently assigned to that advisor.

5. The Supervisor selects the client to be unassigned.

6. The Supervisor clicks the “Remove Assignment” or “Unassign

Client” button.

7. The System displays a confirmation dialog with a warning: “Are you

sure you want to unassign this client from [Advisor Name]?”.

8. The System displays a mandatory field requesting the reason for the

unassignment.

9. The Supervisor enters the reason explaining the cause (e.g., “Territory

change”, “Workload reassignment”, “Inactive client”).

10. The Supervisor clicks “Confirm Unassignment”.

11. The System checks whether the client has active negotiations in

progress.

12. The System removes the assignment relationship from the database.

13. The System records the unassignment in the audit history with: User

who performed the action, Date and time, Unassigned client, Advisor from whom the client was unassigned, Provided reason.

14. The System displays a confirmation message: “The client has been

successfully unassigned from [Advisor]”. Alternative Flows: 10a. If the Supervisor cancels the operation:

1. The System closes the confirmation dialog without making changes.

2. The assignment remains intact.

3. The use case ends.

8a. If the Supervisor does not provide a reason:

1. The System displays an error: “The unassignment reason is

mandatory”.

### Table 2.13 Use Case Documentation - Unassign or remove client from an advisor

### 46

2. The System does not allow continuation until a reason is entered.

3. The flow remains at step 9

Exceptions: 11. If the client has active negotiations in a critical state (e.g., imminent Closing):

1. The System displays a warning: “WARNING: This client has active

negotiations in Closing state. Do you want to proceed anyway?”.

2. The System displays details of the active negotiations.

3. The Supervisor may: Confirm and proceed with the unassignment, or

Cancel to review the negotiations first.

4. If the Supervisor confirms, the flow continues at step 12.

5. If the Supervisor cancels, the use case ends.

12. If the database operation fails:

1. The System displays an error message: “The unassignment could not

be completed. Please try again”.

2. The System logs the error.

3. The assignment remains unchanged.

4. The use case ends.

Requirements: RF-CRM-014: The system shall allow the immediate supervisor to remove business clients from a sales advisor’s portfolio.

### Table 2.13 (continued)

### 47

Name of Use Case: Disable closed negotiations Created By: BOPADIGITAL Last Updated By: BOPADIGITAL Date Created: 21/12/25 Last Revision Date: 11/01/2026

Description: The Immediate Supervisor marks negotiations that have been completed (successful or canceled) as closed and inactive to prevent further modifications and preserve the integrity of historical data. Actors: Immediate Supervisor. Preconditions: 1. The supervisor must be authenticated in the system.

2. The negotiation must be in a final state: Post-Sale (successfully

completed) or Canceled.

3. The negotiation must belong to a client within the supervisor’s team.

Postconditions: 1. The negotiation is marked as closed/inactive in the database.

2. No further modifications or status changes are allowed on the

negotiation.

3. The negotiation data is preserved intact for historical reports and

auditing.

4. Historical metrics and reports include this negotiation.

Flow: 1. The Immediate Supervisor navigates to the “Negotiations” section in the CRM module.

2. The Supervisor applies a filter to view negotiations in “Post-Sale” or

“Canceled” status.

3. The System displays the list of completed negotiations that are still

marked as active.

4. The Supervisor reviews the list and selects the negotiation(s) to

permanently close.

5. The Supervisor may select multiple negotiations using checkboxes.

6. The Supervisor clicks the “Close Selected Negotiations” button.

7. The System displays a confirmation dialog listing the negotiations to

be closed: Associated client, Final status, Responsible advisor, Completion date.

8. The System warns: “Closed negotiations cannot be modified later”.

9. The Supervisor reviews the information and clicks “Confirm

Closure”.

10. The System sets the isActive flag to false for each selected negotiation.

11. The System records the closure in the audit log with: User who closed,

Closure date and time, IDs of closed negotiations.

12. The System displays a confirmation message: “[N] negotiation(s)

have been successfully closed”. Alternative Flows: 9a. If the Supervisor cancels the operation:

1. The System closes the dialog without applying changes.

2. All negotiations remain active.

3. The use case ends.

4a. If the Supervisor wants to view details before closing:

1. The Supervisor clicks on a specific negotiation.

2. The System displays the detailed view with the complete history.

### Table 2.14 Use Case Documentation - Disable closed negotiations

### 48

3. The Supervisor reviews the full information.

4. The Supervisor returns to the list.

5. The flow continues at step 4.

Exceptions: 3. If there are no negotiations in final status available for closure:

1. The System displays the message: “There are no completed

negotiations pending closure”.

2. The use case ends.

4. If a selected negotiation is not in a valid final status:

1. The System displays a warning: “Only negotiations in Post-Sale or

Canceled status can be closed”.

2. The System automatically unselects negotiations with invalid status.

3. The System displays which negotiations were unselected and why.

4. The flow continues with the remaining valid negotiations.

10. If the database update operation fails:

1. The System displays an error: “The negotiations could not be closed.

Please try again”.

2. The System logs the error.

3. The negotiations remain active.

4. The use case ends.

Requirements: RF-CRM-011: The system shall allow the immediate supervisor to deactivate business clients when necessary.

### Table 2.14 (continued)

### 49

Name of Use Case: View recent advisor activity Created By: BOPADIGITAL Last Updated By: BOPADIGITAL Date Created: 21/12/25 Last Revision Date: 11/01/2026

Description: The Immediate Supervisor reviews a feed of recent activities performed by the sales advisors on their team in order to monitor productivity, follow-up, and compliance with defined processes. Actors: Immediate Supervisor. Preconditions: 1. The supervisor must be authenticated in the system.

2. The supervisor must have at least one sales advisor assigned to their

team.

3. There must be activity recorded in the system by the advisors.

Postconditions: 1. A chronological feed of recent team activity is displayed.

2. The supervisor can identify work patterns and areas requiring

attention. Flow: 1. The Immediate Supervisor navigates to the “Team Activity” section on the dashboard.

2. The System queries the recent activities of all supervised advisors.

3. The System displays an activity feed in descending chronological

order (most recent first) with: Activity type (Visit registration, Client update, Negotiation status change, Document upload, Offer matrix submission), Advisor who performed the action, Associated client, Exact date and time, Brief summary of the action.

4. The Supervisor may apply filters to refine the view: Filter by specific

advisor or view all, Filter by date range (today, last week, last month, custom), Filter by specific activity type.

5. The Supervisor selects a specific activity to view full details.

6. The System displays the detailed activity view including: All relevant

action data, Client and negotiation context, Links to directly access the related record. Alternative Flows: 2a. If there is no recent activity recorded:

1. The System displays an informational message: “There is no recent

activity to display for the selected period”.

2. The System suggests expanding the date range.

3. The use case ends if the supervisor does not modify filters.

4a. If the Supervisor applies filters:

1. The System updates the feed displaying only activities that match the

criteria.

2. The System displays a counter: “Displaying [N] activities”.

3. The flow continues at step 4 with the filtered results.

5a. If the Supervisor wants to export the activity report:

1. The Supervisor clicks “Export Activity”.

2. The System generates an Excel file with all displayed activities.

### Table 2.15 Use Case Documentation - View recent advisor activity

### 50

3. The flow continues normally.

Exceptions: 2. If the activity feed query fails:

1. The System displays an error message: “The activity feed could not be

loaded. Please try again”.

2. The System logs the error for technical review.

3. The use case ends.

6. If the related record has been deleted:

1. The System displays the available activity information.

2. The System indicates: “The associated record is no longer available”.

3. Links to non-existent records are not enabled.

Requirements: RF-CRM-015: The system shall allow the immediate supervisor to view the recent activity of all company sales advisors.

### Table 2.15 (continued)

### 51

Name of Use Case: View costs per advisor Created By: BOPADIGITAL Last Updated By: BOPADIGITAL Date Created: 21/12/25 Last Revision Date: 11/01/2026

Description: The Immediate Supervisor or Manager reviews cost and sales performance metrics for each advisor on their team. Actors: Immediate Supervisor, Manager Preconditions: 1. The user must be authenticated with the appropriate role.

2. Sales data must be available in the system.

Postconditions: 1. Cost and performance metrics per advisor are displayed.

Flow: 2. The User navigates to the “Advisor Metrics” section.

3. The System displays a list of advisors with key metrics: Total sales

amount, Number of closures, Average deal value, Earned commission, Sales by service category.

4. The User can sort by any metric column.

5. The User selects a specific advisor to view a detailed breakdown.

6. The System displays a detailed cost analysis: Monthly trend chart,

Revenue by service type, Customer acquisition cost, Conversion rates. Alternative Flows: 2a. If no data is available for the selected period:

1. The System displays: “No sales data available for the selected period”.

2. The use case ends.

Exceptions: 2. If metric calculation fails:

1. The System displays: “Metrics could not be calculated. Please try

again”.

2. The use case ends.

Requirements: RF-CRM-017: The system shall allow management to view the total billed amount per advisor, along with the total number of services sold and the average revenue per service.

### Table 2.16 Use Case Documentation - View costs per advisor

### 52

Name of Use Case: Get sales report Created By: BOPADIGITAL Last Updated By: BOPADIGITAL Date Created: 21/12/25 Last Revision Date: 11/01/2026

Description: The Immediate Supervisor or Manager views a commercial progress report that shows negotiation progress, completed visits, and client statuses in order to evaluate goal compliance. Actors: Manager, Immediate Supervisor. Preconditions: 1. The user must be authenticated.

2. Sales data must exist in the system.

Postconditions: 1. The sales report is generated and displayed.

2. The report can be exported for external use.

Flow: 1. The User navigates to the “Reports” section.

2. The User selects the “Sales Report” option.

3. The System displays the report configuration form: Date range,

Advisor filter (all/specific), Service category filter, Grouping option (by advisor/by month/by service).

4. The User configures the desired parameters.

5. The User clicks “Generate Report”.

6. The System queries sales data based on the parameters.

7. The System calculates aggregated metrics: Total sales value, Number

of closed deals, Average deal size, Top-performing advisors, Bestselling services.

8. The System displays the report with charts and tables.

9. The User may export the report in PDF or Excel format.

Alternative Flows: 6a. If no data matches the selected criteria:

1. The System displays: “No sales data found for the selected criteria”.

2. The User may modify parameters and retry.

Exceptions: 6. If a query timeout occurs:

1. The System displays: “Report generation is taking longer than

expected. Please try a smaller date range”.

2. The use case ends.

Requirements: RF-REP-001: The system shall allow the manager to generate commercial performance reports by advisor, month, or period to evaluate team productivity. RF-REP-006: The system shall allow the manager to export generated reports in PDF or Excel format for analysis or presentation

### Table 2.16 (continued)

### 53

Name of Use Case: Get progress report Created By: BOPADIGITAL Last Updated By: BOPADIGITAL Date Created: 21/12/25 Last Revision Date: 11/01/2026

Description: The Immediate Supervisor or Manager generates reports showing the progress of the negotiation pipeline and advisor performance against defined objectives. Actors: Immediate Supervisor, Manager Preconditions: 1. The user must be authenticated.

2. Negotiation and target data must exist.

Postconditions: 1. The progress report is generated showing current status versus objectives.

2. The report can be exported.

Flow: 1. The User navigates to the “Reports” section.

2. The User selects the “Progress Report” option.

3. The System displays the configuration form: Date range, Advisor

filter, Include comparison against objectives.

4. The User configures the parameters.

5. The User clicks “Generate Report”.

6. The System queries negotiation pipeline data.

7. The System calculates metrics: Negotiations by stage

(Prospecting/Active/Closing/Closed), Conversion rates, Average time per stage, Objective compliance percentage, Projected versus actual performance.

8. The System displays the report with pipeline funnel visualization.

9. The User may export the report in PDF or Excel format.

Alternative Flows: 6a. If there are no active negotiations:

1. The System displays: “No negotiations were found for the selected

period”.

2. The use case ends.

Exceptions: 6. If calculation fails:

1. The System displays: “The progress report could not be generated.

Please try again”.

2. The use case ends.

Requirements: RF-CRM-019: The system shall allow management to view, for each advisor, the number of business clients in each sales funnel stage.

### Table 2.17 Use Case Documentation - Get progress report

### 54

Name of Use Case: Compare Metrics Between Advisors Created By: BOPADIGITAL Last Updated By: BOPADIGITAL Date Created: 21/12/25 Last Revision Date: 11/01/2026

Description: The Immediate Supervisor or Manager performs side-by-side comparison of performance metrics between multiple sales advisors to identify best practices, performance gaps, and make informed decisions about coaching, recognition, or resource allocation. Actors: Immediate Supervisor Preconditions: 1. The user must be authenticated with the appropriate role.

2. At least two sales advisors must exist in the system.

3. Performance data must be available for the advisors being compared.

4. For Supervisors, all compared advisors must be in their team.

Postconditions: 1. A comparative analysis of selected advisors is displayed.

2. Performance gaps and leaders are clearly identified.

3. The comparison can be saved or exported for review.

4. Management has insights for decision-making.

Flow: 1. The User accesses the "Team Performance" section in the CRM module.

2. The System displays the list of all advisors in the user's scope.

3. The User selects multiple advisors for comparison using checkboxes

(minimum two, maximum five).

4. The User clicks "Compare Selected Advisors".

5. The System displays a period selector: Current month (default), Last month,

Last quarter, Year to date, Custom range.

6. The User selects the time for comparison.

7. The System queries performance data for all selected advisors for the

specified period.

8. The System calculates comparison metrics for each advisor: Revenue

generated, Number of deals closed, Average deal size, Number of active clients, Client visits performed, Negotiations in pipeline, Closing rate (%), Average time to close, Proposals submitted, Approval rate (%), Documentation completion rate.

9. The System displays the comparison dashboard organized in sections:

Summary Comparison Table: Advisors as columns, Key metrics as rows, Numeric values with color coding (green for above average, red for below). Visual Comparisons: Grouped bar charts for revenue and deals, Line graphs for trends over time, Radar charts for multi-dimensional comparison, Pie charts for market share/contribution. Performance Rankings: Overall performance score, Individual metric rankings, Percentile position within team. Gap Analysis: Identifies largest performance differences, Highlights strengths and weaknesses, Shows distance from team average or top performer.

10. The System color-codes each metric: Green for top performers (top 25%),

Yellow for average performers (middle 50%), Red for below average (bottom 25%).

11. The User reviews the comparison visualizations.

12. The User can interact with charts and tables: Hover for detailed values,

click to drill down into specific data, Toggle metrics on/off, Sort by any column.

### Table 2.18 Use Case Documentation - Compare Metrics Between Advisors

### 55

Alternative Flows: 12a. User adjusts comparison parameters:

1. The User clicks "Adjust Comparison".

2. The System allows modifying: Selected advisors (add/remove), Time

period, Metrics to compare (select/deselect specific metrics).

3. The User makes changes.

4. The System recalculates and updates the comparison.

5. The flow returns to step 11.

12b. User views detailed breakdown for specific metric:

1. The User clicks on a specific metric in the comparison.

2. The System displays a detailed view for that metric only: Individual values

for each advisor, Statistical analysis (mean, median, standard deviation), Distribution chart, Historical trend for each advisor, Target vs. actual comparison.

3. The User can return to the full comparison.

12c. User identifies and analyzes performance gap:

1. The User clicks on a significant performance gap indicator.

2. The System displays gap analysis: Top performer's approach and activities,

Lower performer's activities, Specific recommendations, Best practices from top performer, Suggested coaching focus areas.

3. The User can export the gap analysis.

11a. User exports comparison report:

1. The User clicks "Export Comparison".

2. The System displays export options: Format (PDF/Excel/PowerPoint),

Include all metrics or selected only, Include charts and visualizations, Add executive summary.

3. The User configures export options.

4. The System generates a comprehensive comparison report with: Cover

page, Executive summary, Detailed comparison tables, All visualizations, Insights, and recommendations.

5. The System initiates the download.

12d. User saves comparison for later:

1. The User clicks "Save Comparison".

2. The System prompts for a name and optional description.

3. The User provides comparison details.

4. The System saves the comparison configuration and current results.

5. The System displays: "Comparison saved. Access it from 'My Saved

Comparisons'."

11b. User shares comparison with others:

1. The User clicks "Share Comparison".

2. The System displays sharing options: Share link (view-only), Send via

email, Schedule recurring email.

3. The User selects recipients.

4. The System generates a shareable link or sends the report.

5. The System logs the sharing action.

### Table 2.18 (continued)

### 56

Exceptions:

7. Performance data unavailable for some advisors:

1. The System displays a warning: "Limited data available for [Advisor

Name]. Comparison may be incomplete."

2. The System displays available data with indicators for missing metrics.

3. The System includes a note in the comparison.

4. The User can proceed with partial comparison or exclude the advisor.

9. Calculation error during comparison:

1. The System displays: "An error occurred while calculating comparison

metrics."

2. The System displays successfully calculated metrics with a warning.

3. The System logs the error with details.

4. The User can retry

### Table 2.18 (continued)

### 57

Name of Use Case: View Advisor Metrics Created By: BOPADIGITAL Last Updated By: BOPADIGITAL Date Created: 21/12/25 Last Revision Date: 11/01/2026

Description: The Immediate Supervisor or Manager views detailed performance metrics for individual sales advisors to evaluate productivity, identify top performers, and detect areas needing improvement or support. Actors: Sales Advisor, Immediate Supervisor Preconditions: 1. The user must be authenticated with the appropriate role.

2. Sales advisor accounts must exist in the system.

3. Performance data must be available in the database.

4. For Supervisors, they can only view metrics for advisors in their team.

5. Managers can view metrics for all advisors.

Postconditions: 1. Comprehensive advisor performance metrics are displayed.

2. The user can identify performance trends and patterns.

3. Metric viewing is logged for audit purposes.

4. Performance comparisons can be made between advisors.

Flow: 1. The User accesses the "Team Performance" or "Advisor Metrics" section.

2. The System displays a list of advisors within the user's scope with summary

metrics: Advisor name and photo, Current clients assigned, Active negotiations, Closed deals (current month), Total revenue (current month), Performance rating indicator.

3. The User can sort the list by any metric column.

4. The User selects a specific advisor to view detailed metrics.

5. The System displays comprehensive advisor performance data organized

in sections: Overview Section: Advisor profile information, Team/territory assignment, Hire date and tenure, Current performance rating. Activity Metrics: Total clients assigned, New clients added (period), Client visits registered, Last visit date, Average visits per client. Pipeline Metrics: Total active negotiations, Negotiations by stage (count and percentage), Average negotiation duration, Stage conversion rates, Stalled negotiations (no activity > 30 days). Revenue Metrics: Total closed deals (period), Total revenue generated (period), Average deal size, Largest deal closed, Revenue by service category, Year-to-date revenue. Productivity Metrics: Closing rate (%), Average time to close, Proposals submitted, Proposals approved, Proposals rejected, Documentation completion rate. Comparative Metrics: Performance vs. team average, Performance vs. personal targets, Ranking within team, Trend indicators (improving/declining).

6. The System includes visual indicators: Color-coded performance ratings,

Trend arrows (up/down/stable), Progress bars for targets, Sparklines for trends.

7. The User can select different time periods: Current month, Last month, Last

quarter, Last year, Custom date range.

8. The System updates all metrics for the selected period.

9. The User can view detailed drill-downs: Click on any metric to see

underlying transactions, View individual client details, Review specific negotiations.

### Table 2.19 Use Case Documentation - View Advisor Metrics

### 58

Alternative Flows: 9a. User views advisor activity timeline:

1. The User clicks "Activity Timeline".

2. The System displays a chronological view of all advisor activities: Client

registrations, Visits registered, Matrix submissions, Approvals received, Deal closures, Documentation uploads.

3. Each activity is timestamped and includes details.

4. The User can filter by activity type.

9b. User compares multiple advisors:

1. The User returns to the advisor list.

2. The User selects multiple advisors using checkboxes (2-5 advisors).

3. The User clicks "Compare Selected".

4. The System displays a side-by-side comparison dashboard: Key metrics in

comparison table, Stacked bar charts for visual comparison, Performance ranking, Strengths, and weaknesses analysis.

5. The System highlights significant differences.

9c. User exports advisor metrics:

1. The User clicks "Export Metrics".

2. The System displays export options: Format (Excel/PDF), Include charts

(yes/no), Include all advisors or current selection, Time period to include.

3. The User configures export options.

4. The System generates the export file.

5. The System initiates the download.

5a. User views advisor's client portfolio:

1. The User clicks "View Clients" in the advisor profile.

2. The System displays all clients assigned to the advisor with: Client name

and RUC, Current monthly billing, Negotiation status, Last contact date, Documentation status.

3. The User can click on any client to view full details.

6a. Performance alerts displayed:

1. The System automatically identifies and displays alerts: "Below target for

2 consecutive months", "No client visits in last 14 days", "3 negotiations stalled over 60 days", "Documentation completion below 50%".

2. Each alert includes a severity level (Info/Warning/Critical).

3. The User can click on alerts for recommendations.

Exceptions: 5. Advisor metrics cannot be loaded:

1. The System displays: "Unable to load advisor metrics. Please try again."

2. The System logs the error.

3. The summary metrics remain visible.

4. The use case ends.

8. Time period query timeout:

1. The System displays: "Loading metrics for the selected period is taking too

long. Try a shorter time range."

2. The System displays cached or summary data if available.

3. The User can select a different period.

### Table 2.19 (continued)

### 59

2. No advisors in user's scope:

1. The System displays: "No sales advisors are currently assigned to your

team."

2. For Supervisors, suggests contacting management.

3. The use case ends.

Requirements: RF-CRM-017: The system shall allow management to view the total billed amount per advisor, along with the total number of services sold and the average revenue per service. RF-CRM-019: The system shall allow management to view, for each advisor, the number of business clients in each sales funnel stage. RF-REP-007: The system shall display individual advisor performance metrics including deals closed, revenue, and conversion rates.

### Table 2.19 (continued)

### 60

Name of Use Case: Filter Reports Created By: BOPADIGITAL Last Updated By: BOPADIGITAL Date Created: 21/12/25 Last Revision Date: 11/01/2026

Description: The Immediate Supervisor or Manager applies filters to generated reports to focus on specific segments, time periods, or metrics, enabling detailed analysis of aspects of sales performance. Actors: Immediate Supervisor, Immediate Supervisor Preconditions: 1. The user must be authenticated with the appropriate role.

2. A report must have been generated (sales, progress, or performance report).

3. The report must contain filterable data.

Postconditions: 1. The report view is updated to show only filtered data.

2. Filter settings are temporarily saved for the current session.

3. Filtered data can be exported separately.

4. Charts and visualizations are updated to reflect filtered data.

Flow: 1. The User is viewing a generated report (sales, progress, or performance).

2. The User clicks "Filter Report" or the filter icon in the report interface.

3. The System displays available filter options based on report type: Time

Period Filters: Specific months, Quarters, Date ranges. Advisor Filters: Individual advisors, Teams, Performance levels (Top/Average/Below Average). Service Category Filters: Voice, Connectivity, Digital Services, Specific services. Client Segment Filters: By industry, By company size, By billing range. Performance Filters: Above/below target, Conversion rate ranges, Deal size ranges. Status Filters: Negotiation stages, Documentation status, Approval status.

4. The User selects one or multiple filter criteria.

5. The User specifies filter values or ranges as appropriate.

6. The User can combine filters using AND/OR logic operators.

7. The User clicks "Apply Filters".

8. The System validates the filter criteria.

9. The System recalculates metrics based on filtered data.

10. The System updates all visualizations (charts, graphs, tables).

11. The System displays the filtered report with: Updated summary statistics

reflecting only filtered data, Refreshed charts and graphs, Indicator showing active filters, Number of records displayed vs. total available.

12. The System displays an active filter summary: "Showing [N] of [Total]

records Filters: [list of active filters]".

13. The User can review the filtered report.

14. The User can add more filters, remove filters, or clear all filters.

Alternative Flows: 14a. User clears all filters:

1. The User clicks "Clear All Filters".

2. The System removes all active filters.

3. The System restores the report to show all data.

4. The System recalculates metrics with complete dataset.

5. The flow returns to step 11 with full data.

14b. User saves filter configuration:

1. The User clicks "Save Filter Configuration".

2. The System displays a dialog to name the filter.

3. The User enters a descriptive name.

### Table 2.20 Use Case Documentation - Filter Reports

### 61

4. The System saves the filter configuration.

5. The System displays: "Filter configuration saved. You can load it from 'My

Saved Filters'."

9a. Filtered data results in empty set:

1. The System displays: "No data matches your filter criteria."

2. The System shows which filters eliminated all data.

3. The System suggests: "Try removing or adjusting some filters."

4. The User can modify filters or clear them.

14c. User exports filtered report:

1. The User clicks "Export Filtered Data".

2. The System displays export options (Excel/PDF).

3. The User selects format.

4. The System generates export with only filtered data.

5. The export includes a note indicating active filters.

6. The System initiates the download.

11a. User compares filtered vs. unfiltered data:

1. The User clicks "Compare with Total".

2. The System displays side-by-side comparison: Filtered data metrics, Total

data metrics, Percentage difference.

3. The System highlights significant variances.

4. The User can return to filtered view.

6a. User creates complex filter logic:

1. The User clicks "Advanced Filter Logic".

2. The System displays a filter builder interface.

3. The User creates nested conditions with AND/OR operators.

4. The System validates the logic.

5. The flow continues at step 7.

Exceptions: 9. Filter recalculation fails:

1. The System displays: "Unable to apply filters. Please try again."

2. The System logs the error.

3. The report remains in its previous state.

4. The use case ends.

8. Invalid filter criteria:

1. The System displays: "Invalid filter values. Please check your inputs."

2. The System highlights invalid fields.

3. The User corrects the values.

4. The flow returns to step 7.

10. Chart rendering fails with filtered data:

1. The System displays the filtered data in table format.

2. The System shows a message: "Charts temporarily unavailable. Displaying

data in table format."

3. The System logs the rendering error.

4. The user can still work with the filtered data.

### Table 2.20 (continued)

### 62

Requirements: RF-REP-004: The system shall allow filtering reports by multiple criteria such as date range, advisor, and service type. RF-REP-005: The system shall update report visualizations dynamically when filters are applied.

### Table 2.20 (continued)

### 63

Name of Use Case: Generate Sales and Closing Reports Created By: BOPADIGITAL Last Updated By: BOPADIGITAL Date Created: 21/12/25 Last Revision Date: 11/01/2026

Description: The Immediate Supervisor or Manager generates comprehensive sales reports showing closed deals, revenue, and performance metrics for a specified time period to evaluate commercial success and advisor productivity. Actors: Immediate Supervisor, Administrator Preconditions: 1. The user must be authenticated with the appropriate role.

2. Sales and negotiation data must exist in the system.

3. At least one closed negotiation must exist in the database.

4. The reporting module must be operational.

Postconditions: 1. A sales and closing report is generated and displayed.

2. The report can be exported in PDF or Excel format.

3. Report generation is logged in the system.

4. Management has visibility into sales performance.

Flow: 1. The User accesses the "Reports" section in the CRM module.

2. The User selects "Sales and Closing Report".

3. The System displays the report configuration form with parameters: Date

Range: Start date (required), End date (required), Quick select options (This Month, Last Month, This Quarter, Last Quarter, This Year, Custom). Grouping Options: By Advisor, By Service Category, By Month, By Client Segment. Advisor Filter: All advisors (for Manager), My team (for Supervisor), Specific advisor(s). Service Category Filter: All categories, Voice, Connectivity, Digital Services. Metrics to Include (checkboxes): Total closed deals, Total revenue, Average deal size, Revenue by service type, Top performing advisors, Conversion rates, Deal closure time.

4. The User configures the desired report parameters.

5. The User selects which metrics to include in the report.

6. The User clicks "Generate Report".

7. The System validates that the date range is valid and not excessive.

8. The System displays a progress indicator: "Generating report...".

9. The System queries the database for closed negotiations within the

specified parameters.

10. The System calculates all selected metrics: Total number of closed deals,

Total revenue generated, Average revenue per deal, Revenue breakdown by service category, Individual advisor performance, Month-over-month trends, Conversion rate (closed vs. total negotiations).

11. The System generates visualizations: Bar charts for revenue by advisor,

Pie charts for revenue by service category, Line graphs for trends over time, Performance comparison tables.

12. The System displays the complete report with: Executive Summary: Key

highlights, Overall performance metrics, Period-over-period comparison. Detailed Tables: Individual deal listings, Advisor performance breakdown, Service category analysis. Visual Charts and Graphs: Interactive visualizations, Trend analysis, Comparative metrics.

13. The User reviews the report.

14. The User can interact with charts (hover for details, click to drill down).

### Table 2.21 Use Case Documentation - Generate Sales and Closing Reports

### 64

Alternative Flows: 13a. User exports report to Excel:

1. The User clicks "Export to Excel".

2. The System generates an Excel workbook with multiple sheets: Summary

sheet, Detailed data sheet, Advisor breakdown sheet, Service category sheet, Raw data sheet.

3. The System includes charts and formatting.

4. The System initiates the download.

5. The System logs the export action.

13b. User exports report to PDF:

1. The User clicks "Export to PDF".

2. The System generates a formatted PDF document with: Cover page with

report title and parameters, Executive summary page, Detailed analysis with charts, Appendix with data tables.

3. The System initiates the download.

4. The System logs the export action.

14a. User drills down into specific data:

1. The User clicks on a specific chart element (e.g., a bar for an advisor).

2. The System displays a detailed view of that specific segment.

3. The System shows individual deals comprising that data point.

4. The User can return to the full report view.

7a. Date range exceeds system limits:

1. The System displays: "Date range is too large. Please select a range of 2

years or less."

2. The System highlights the date range fields.

3. The User adjusts the date range.

4. The flow returns to step 6.

9a. No closed deals in the selected period:

1. The System displays: "No closed deals found for the selected period and

filters."

2. The System suggests: "Try selecting a different date range or adjusting

filters."

3. The System shows the nearest periods with available data.

4. The User can modify parameters or cancel.

12a. User schedules recurring report:

1. The User clicks "Schedule Report".

2. The System displays scheduling options: Frequency

(Daily/Weekly/Monthly/Quarterly), Recipients (email addresses), Format (PDF/Excel), Delivery time.

3. The User configures the schedule.

4. The System saves the scheduled report configuration.

5. The System will automatically generate and email the report.

Exceptions: 9. Database query fails:

1. The System displays: "Unable to retrieve sales data. Please try again."

2. The System logs the error with query details.

3. The use case ends.

### Table 2.21 (continued)

### 65

10. Calculation error:

1. The System displays: "An error occurred while calculating metrics. Please

contact support."

2. The System logs the error with partial results.

3. The System displays any successfully calculated metrics with a warning.

4. The use case ends.

9. Query timeout due to large dataset:

1. The System displays: "Report generation is taking longer than expected.

Try a smaller date range or fewer metrics."

2. The System cancels the query.

3. The use case ends.

Requirements: RF-REP-001: The system shall allow the manager to generate commercial performance reports by advisor, month, or period to evaluate team productivity. RF-REP-003: The system shall include metrics such as total deals closed, revenue generated, and average deal size. RF-REP-006: The system shall allow the manager to export generated reports in PDF or Excel format for analysis or presentation.

### Table 2.21 (continued)

### 66

Name of Use Case: Filter Client Lists by Metrics Created By: BOPADIGITAL Last Updated By: BOPADIGITAL Date Created: 21/12/25 Last Revision Date: 11/01/2026

Description: The Sales Advisor, Immediate Supervisor, or Manager applies advanced filters to client lists based on various metrics and criteria to identify specific client segments, prioritize actions, and analyze the client portfolio. Actors: Sales Advisor, Immediate Supervisor, Administrator Preconditions: 1. The user must be authenticated in the system.

2. Client records must exist in the database.

3. The CRM module must be accessible.

4. For Sales Advisors, they can only filter their assigned clients.

5. For Supervisors and Managers, they can filter all clients in their scope.

Postconditions: 1. A filtered list of clients is displayed according to the selected criteria.

2. The filter configuration can be saved for future use.

3. Filter results can be exported for external analysis.

Flow: 1. The User accesses the "Clients" section in the CRM module.

2. The System displays the complete client list with basic information.

3. The User clicks "Advanced Filters" or the filter icon.

4. The System displays the filter panel with available filter categories: Client

Information Filters: Business Name, RUC, Industry Sector, Company Size. Commercial Metrics Filters: Current Monthly Billing (range), Number of Active Services (range), Total Contract Value (range), Customer Lifetime Value. Negotiation Status Filters: Negotiation Stage (Prospecting/Active/Closing/Post-Sale), Last Contact Date (date range), Days Without Contact, Assigned Advisor. Performance Filters: Documentation Status (Complete/Incomplete), Payment Status (Current/Overdue), Risk Level (Low/Medium/High). Geographic Filters: City, Province, Coverage Zone.

5. The User selects one or multiple filter criteria.

6. For numeric or date ranges, the User specifies minimum and maximum

values.

7. For categorical filters, the User selects from dropdown options or

checkboxes.

8. The User can combine multiple filters using AND/OR logic.

9. The User clicks "Apply Filters".

10. The System validates the filter criteria.

11. The System queries the database with the applied filters.

12. The System displays the filtered client list showing: Number of clients

matching criteria, Client details matching all filters, Summary statistics for the filtered set.

13. The User can further refine filters or clear them.

14. The User can save the filter configuration by clicking "Save Filter".

15. The System prompts for a filter name.

16. The User provides a descriptive name for the filter.

17. The System saves the filter configuration for future use.

### Table 2.22 Use Case Documentation - Filter Client Lists by Metrics

### 67

Alternative Flows: 14a. User loads a saved filter:

1. The User clicks "Load Saved Filter".

2. The System displays a list of previously saved filters with: Filter name,

Creation date, Filter criteria summary.

3. The User selects a saved filter.

4. The System applies the saved filter configuration.

5. The flow continues at step 11.

13a. User exports filtered results:

1. The User clicks "Export Results".

2. The System displays export options: Format (Excel/CSV/PDF), Include

columns (customizable), Include summary statistics.

3. The User selects export preferences.

4. The System generates the export file.

5. The System initiates the download.

6. The System logs the export action.

12a. No clients match the filter criteria:

1. The System displays: "No clients match your filter criteria."

2. The System suggests: "Try adjusting your filters or clearing some criteria."

3. The System shows how many clients were excluded by each filter.

4. The User can modify filters or clear them.

8a. User creates complex filter logic:

1. The User clicks "Advanced Logic".

2. The System displays a query builder interface.

3. The User creates complex conditions: (Billing > $1000 AND Services >=

3. OR (Stage = Closing).

4. The System validates the logic syntax.

5. The flow continues at step 9.

12b. User sorts filtered results:

1. The User clicks a column header to sort.

2. The System re-orders the filtered list by that column.

3. The User can toggle between ascending and descending order.

4. The sort preference is maintained during the session.

Exceptions: 11. Database query timeout:

1. The System displays: "Filter query is taking too long. Try using fewer

criteria or narrower ranges."

2. The System logs the timeout.

3. The user can simplify filters and retry.

4. The use case ends if the user cancels.

11. Database query fails:

1. The System displays: "Unable to apply filters. Please try again."

2. The System logs the error.

3. The previous unfiltered list remains displayed.

4. The use case ends.

### Table 2.22 (continued)

### 68

17. Filter save fails:

1. The System displays: "Filter could not be saved. Please try again."

2. The System logs the error.

3. The filter remains applied but is not saved.

4. The user can retry saving.

Requirements: RF-CRM-009: The system shall allow filtering clients by multiple criteria including billing, services, status, and advisor. RF-CRM-018: The system shall provide advanced search and filtering capabilities for client lists. RF-REP-002: The system shall allow users to create custom filters and save them for future use.

### Table 2.22 (continued)

### 69

Name of Use Case: Reject Matrices Created By: BOPADIGITAL Last Updated By: BOPADIGITAL Date Created: 21/12/25 Last Revision Date: 11/01/2026

Description: The Immediate Supervisor rejects an offer matrix submitted by a sales advisor when it does not comply with commercial policies, contains errors, or is not viable for the business, providing detailed reasons for the rejection. Actors: Immediate Supervisor Preconditions: 1. The supervisor must be authenticated in the system.

2. The offer matrix must exist and be in "Pending Approval" status.

3. The matrix must belong to an advisor in the supervisor's team.

4. The supervisor must have rejection permissions.

Postconditions: 1. The matrix status is updated to "Rejected".

2. The rejection reason is stored in the database.

3. The sales advisor receives a notification with rejection details.

4. The matrix cannot be presented to the client without revision.

5. The rejection is recorded in the audit log.

Flow: 1. The Immediate Supervisor accesses the "Matrix Approvals" section.

2. The System displays the list of matrices pending approval.

3. The Supervisor selects a specific matrix to review.

4. The System displays the complete matrix details including services,

pricing, subsidies, and client information.

5. The Supervisor reviews the matrix and identifies issues or non-compliance.

6. The Supervisor clicks the "Reject Matrix" button.

7. The System displays a rejection dialog with: Mandatory text field for

rejection reason, Checklist of common rejection reasons (optional): "Exceeds discount limits", "Services not available in area", "Incorrect subsidy calculation", "Missing required information", "Does not meet company policies", "Pricing errors", Additional comments field (optional).

8. The Supervisor selects applicable reasons from the checklist or enters a

custom reason.

9. The Supervisor provides detailed comments explaining the rejection and

what needs to be corrected.

10. The Supervisor clicks "Confirm Rejection".

11. The System validates that a rejection reason has been provided.

12. The System updates the matrix status to "Rejected".

13. The System records the rejection details in the database including:

Supervisor ID, Rejection timestamp, Selected rejection reasons, Detailed comments, Previous matrix status.

14. The System creates an entry in the matrix history log.

15. The System sends a notification to the sales advisor including: Matrix ID

and client name, Rejection reasons, Supervisor comments, Guidance on next steps.

16. The System sends an email notification to the advisor.

17. The System displays a confirmation message: "Matrix rejected. The

advisor has been notified."

Alternative Flows: 8a. Supervisor requests information instead of rejecting:

### Table 2.23 Use Case Documentation - Reject Matrices

### 70

1. The Supervisor clicks "Request Information" instead of "Reject".

2. The System displays a form to specify what information is needed.

3. The Supervisor enters the information request.

4. The System updates the matrix status to "Information Requested".

5. The System notifies the advisor.

6. The use case ends with matrix in "Information Requested" status.

11a. No rejection reason provided:

1. The System displays a validation error: "Rejection reason is mandatory.

Please provide a detailed explanation."

2. The System highlights the empty reason field.

3. The System prevents proceeding until a reason is entered.

4. The flow returns to step 9.

10a. Supervisor cancels rejection:

1. The Supervisor clicks "Cancel" on the rejection dialog.

2. The System closes the dialog without making changes.

3. The matrix status remains "Pending Approval".

4. The use case ends.

Exceptions: 12. Database update fails:

1. The System displays: "The rejection could not be processed. Please try

again."

2. The System logs the error with full details.

3. The matrix status remains unchanged.

4. The rejection reason is not saved.

5. The use case ends.

15. Notification service fails:

1. The System completes the rejection anyway.

2. The System logs that the notification failed.

3. The System queues the notification for retry.

4. The System displays a warning: "Matrix rejected, but advisor notification

may be delayed."

16. Email delivery fails:

1. The System completes the rejection and in-app notification.

2. The System logs the email failure.

3. The System will retry email delivery later.

4. The rejection is still valid.

Requirements: RF-MAT-004: The system shall allow the immediate supervisor to approve or reject offer matrices submitted by advisors. RF-MAT-005: The system shall require supervisors to provide rejection reasons when rejecting matrices. RF-CRM-013: The system shall allow the immediate supervisor to review and approve commercial proposals generated by advisors.

### Table 2.23 (continued)

### 71

Name of Use Case: Review Operator Availability Created By: BOPADIGITAL Last Updated By: BOPADIGITAL Date Created: 21/12/25 Last Revision Date: 11/01/2026

Description: The Sales Advisor or Coordinator verifies service availability with the telecommunications operator (Telefónica Movistar) for a specific geographic location before creating an offer matrix or activating services. Actors: Sales Advisor, Administrator, Carrier (external) Preconditions: 1. The user must be authenticated in the system.

2. The client must have a registered address or geographic location.

3. The operator's API or verification system must be accessible.

4. Internet connectivity must be available.

Postconditions: 1. Service availability information is retrieved and displayed.

2. The availability check is logged with timestamp and result.

3. The user knows which services can be offered to the client.

4. Unavailable services are identified with reasons.

Flow: 1. The User accesses the client profile in the CRM module.

2. The User navigates to the "Service Availability" section or initiates matrix

creation.

3. The System displays the client's registered address and geographic

coordinates (if available).

4. The User clicks "Check Operator Availability".

5. The System validates that the client has a complete address registered.

6. The System displays a loading indicator: "Checking service availability

with operator..."

7. The System sends a request to the operator's API with: Client address,

Geographic coordinates, Requested service types (Voice, Connectivity, Digital Services).

8. The Operator System processes the request and returns availability data.

9. The System receives the response and processes the information.

10. The System displays service availability results organized by category:

Available Services (green indicator): Service name, Maximum capacity/speed, Estimated installation time. Partially Available Services (yellow indicator): Service name, Limitations or conditions, Alternative options. Unavailable Services (red indicator): Service name, Reason for unavailability, Estimated availability date (if known).

11. The User reviews the availability information.

12. The System logs the availability check with: User ID, Client ID, Check

timestamp, Services queried, Results summary.

13. If you create a matrix, only available services can be selected.

Alternative Flows: 5a. Client address incomplete:

1. The System displays: "Client address is incomplete. Please update the client

address before checking availability."

2. The System provides a link to edit client information.

3. The User can either: Update the address and retry, Cancel the availability

check.

4. The use case ends if canceled.

### Table 2.24 Use Case Documentation - Review Operator Availability

### 72

8a. Operator API is unavailable:

1. The System displays: "Unable to connect to operator system. Using cached

data (last updated: [date])."

2. The System displays the most recent availability data from cache.

3. The System displays a warning: "This information may be outdated. Please

try again later for current availability."

4. The flow continues at step 10 with cached data.

8b. Operator returns partial response:

1. The System displays the available information.

2. The System shows a warning for services without information:

"Availability unknown contact operator directly."

3. The flow continues at step 11.

10a. User requests detailed coverage map:

1. The User clicks "View Coverage Map".

2. The System displays an interactive map showing: Client location, Service

coverage areas by type, Network infrastructure details, Signal strength indicators.

3. The User can zoom and pan to explore coverage.

4. The User closes the map to return to the results.

13a. User saves availability report:

1. The User clicks "Save Availability Report".

2. The System generates a PDF report with all availability information.

3. The System attaches the report to the client's documents.

4. The System displays: "Availability report saved to client documents."

Exceptions: 8. Operator API timeout:

1. The System displays: "The operator system is taking too long to respond.

Please try again in a few minutes."

2. The System logs the timeout error.

3. The availability check is marked as failed.

4. The use case ends.

8. Operator returns error:

1. The System displays: "The operator system returned an error: [error

message]. Please contact support if this persists."

2. The System logs the full error details.

3. The use case ends.

9. Invalid response format:

1. The System displays: "Received invalid data from operator system. Please

try again or contact support."

2. The System logs the response for technical analysis.

3. The use case ends.

5. No client address registered:

1. The System displays: "Cannot check availability without a client address."

2. The System displays a form to enter the client address.

3. The User must enter the address before proceeding.

### Table 2.24 (continued)

### 73

Requirements: RF-MAT-008: The system shall verify service availability with the operator before allowing matrix creation. RF-SRV-001: The system shall integrate with operator APIs to check realtime service availability. RF-SRV-002: The system shall display service coverage information for client locations.

### Table 2.24 (continued)

### 74

Name of Use Case: Check Matrix Approval Status Created By: BOPADIGITAL Last Updated By: BOPADIGITAL Date Created: 21/12/25 Last Revision Date: 11/01/2026

Description: The Sales Advisor consults the current approval status of offer matrices submitted to the immediate supervisor to know whether they can proceed with client presentation or need to adjust. Actors: Sales Advisor Preconditions: 1. The advisor must be authenticated in the system.

2. At least one offer matrix must have been created and submitted for

approval.

3. The matrix must be associated with a client assigned to the advisor.

Postconditions: 1. The advisor is informed of the current matrix status.

2. If rejected, the advisor can view the rejection reasons.

3. The status consultation is logged for tracking purposes.

Flow: 1. The Sales Advisor accesses the CRM module.

2. The Advisor navigates to "My Matrices" or accesses a specific client's

negotiation.

3. The System displays all matrices created by the advisor with the following

information: Matrix ID, Client Name, Creation Date, Submission Date, Current Status, Last Update Date, Reviewing Supervisor.

4. The System displays matrices with status indicators: "Draft" (gray),

"Pending Approval" (yellow), "Approved" (green), "Rejected" (red), "Information Requested" (orange).

5. The Advisor can filter matrices by: Status, Client, Date range, Negotiation.

6. The Advisor selects a specific matrix to view detailed status.

7. The System displays the matrix status details including: Current status with

timestamp, Status history timeline showing all status changes, Supervisor comments (if any), Approval/rejection date (if applicable), Rejection reasons (if rejected), Requested information (if information requested).

8. If the status is "Approved", the System displays: "This matrix has been

approved. You may proceed to present it to the client."

9. If the status is "Rejected", the System displays: "This matrix was rejected.

Please review the comments and create a new matrix addressing the concerns."

10. If the status is "Information Requested", the System displays: "Additional

information is required. Please respond to the supervisor's request."

11. The Advisor can take appropriate action based on the status: View

supervisor comments, Create a revised matrix, Respond to information requests, Download approved matrix for client presentation. Alternative Flows: 5a. Advisor filters by pending status:

1. The Advisor selects "Pending Approval" filter.

2. The System displays only matrices awaiting supervisor review.

3. The System sorts by submission date (oldest first).

4. The System displays: "You have [N] matrices pending approval."

5. The flow continues at step 6.

10a. Advisor responds to information request:

1. The Advisor clicks "Respond to Request".

2. The System displays a form to provide the requested information.

### Table 2.25 Use Case Documentation - Check Matrix Approval Status

### 75

3. The Advisor enters the additional information or clarifications.

4. The Advisor optionally attaches supporting documents.

5. The Advisor clicks "Submit Response".

6. The System updates the matrix status to "Pending Approval" with new

information.

7. The System notifies the supervisor of the response.

8. The System displays: "Response submitted successfully."

9a. Advisor creates revised matrix after rejection:

1. The Advisor clicks "Create Revised Matrix" from the rejected matrix

details.

2. The System creates a new matrix duplicating the original data.

3. The System adds a reference to the rejected matrix.

4. The System displays the rejection comments prominently.

5. The Advisor makes necessary adjustments.

6. The flow continues with matrix creation process.

11a. Advisor downloads approved matrix:

1. The Advisor clicks "Download Matrix" on an approved matrix.

2. The System generates a PDF document with: Matrix details, All services

and pricing, Applied subsidies, Approval information, Terms and conditions.

3. The System downloads the formatted matrix.

4. The System logs the download action.

Exceptions: 3. No matrices found:

1. The System displays: "You have not created any offer matrices yet."

2. The System displays a "Create New Matrix" button.

3. The use case ends.

7. Matrix details cannot be loaded:

1. The System displays: "Matrix details are temporarily unavailable. Please

try again."

2. The System logs the error.

3. The use case ends.

2. Database connection fails:

1. The System displays: "Unable to retrieve matrix information. Please check

your connection and try again."

2. The System logs the error.

3. The use case ends.

Requirements: RF-MAT-006: The system shall allow sales advisors to view the approval status of their submitted matrices. RF-MAT-007: The system shall display supervisor comments and rejection reasons for matrices.

### Table 2.25 (continued)

### 76

Name of Use Case: Consult Clients and Their Documentation Status Created By: BOPADIGITAL Last Updated By: BOPADIGITAL Date Created: 21/12/25 Last Revision Date: 11/01/2026

Description: The Immediate Supervisor or Coordinator views a comprehensive list of clients with their documentation status to identify pending documentation and track which advisor is responsible for each client. Actors: Immediate Supervisor, Administrator Preconditions: 1. The user must be authenticated with the appropriate role.

2. Client records must exist in the database.

3. The document management module must be operational.

Postconditions: 1. The user has visibility of all clients and their documentation status.

2. The user can identify clients with incomplete documentation.

3. The user can track responsible advisors for follow-up.

Flow: 1. The User accesses the "Documentation Management" section in the CRM module.

2. The User selects "Client Documentation Status" from the menu.

3. The System queries all clients within the user's scope (team for supervisors,

all for coordinators).

4. The System displays a table with the following columns: Client Name,

RUC (Tax ID), Assigned Advisor, Documentation Status (Complete/Incomplete/Pending Review), Required Documents (X of Y completed), Optional Documents (count), Last Document Upload Date, Status Indicator (color-coded).

5. The System uses color coding: Green for "Complete", Yellow for "In

Progress", Red for "Missing Critical Documents".

6. The User reviews the list to identify clients requiring attention.

7. The User can sort the list by any column (client name, status, advisor, date).

8. The User can apply filters: Documentation status

(Complete/Incomplete/Pending), Assigned advisor, Date range for last upload, Specific missing documents.

9. The User selects a specific client to view detailed documentation status.

10. The System displays the client's complete documentation dashboard

showing: Checklist of required documents with status, List of optional documents uploaded, Document history timeline, Responsible advisor contact information, Action buttons (Notify Advisor, View Documents, Download All).

11. The User can take action: Notify the advisor about pending documents,

View or download specific documents, Mark documentation as reviewed. Alternative Flows: 8a. User filters by incomplete documentation:

1. The User selects "Incomplete" from the status filter.

2. The System displays only clients with missing required documents.

3. The System sorts by urgency (oldest pending first).

4. The flow continues at step 9.

8b. User filters by specific advisor:

1. The User selects an advisor from the dropdown filter.

2. The System displays only clients assigned to that advisor.

3. The System displays advisor performance metrics: Total clients, Clients

with complete documentation (%), Average documentation completion time.

### Table 2.26 Use Case Documentation - Consult Clients and Their Documentation Status

### 77

4. The flow continues at step 9.

11a. User notifies advisor about pending documents:

1. The User clicks "Notify Advisor" for a specific client.

2. The System displays a notification dialog with: List of missing documents

(pre-selected), Optional message field, Notification urgency level (Normal/Urgent).

3. The User adds a custom message if needed.

4. The User clicks "Send Notification".

5. The System sends an email and in-app notification to the advisor.

6. The System records the notification in the client history.

7. The System displays: "Advisor notified successfully."

11b. User exports documentation status report:

1. The User clicks "Export Report".

2. The System displays export options: Excel or PDF format, Include only

filtered results or all clients, Include detailed document checklist.

3. The User selects preferences and clicks "Generate Report".

4. The System generates the report file.

5. The System initiates download of the report.

Exceptions: 3. Database query fails:

1. The System displays: "Unable to load client documentation status. Please

try again."

2. The System logs the error for technical review.

3. The use case ends.

10. Client details cannot be loaded:

1. The System displays: "Client documentation details are temporarily

unavailable."

2. The System displays basic client information available in cache.

3. The User can retry or return to the list.

4. No clients found:

1. The System displays: "No clients found within your scope."

2. The use case ends.

Requirements: RF-DOC-004: The system shall display documentation status (complete/pending/missing) for each client. RF-CRM-016: The system shall allow coordinators to verify pending documentation and track which advisor is responsible. RF-CRM-010: The system shall allow the immediate supervisor to view all business clients assigned to their team.

### Table 2.26 (continued)

### 78

Name of Use Case: Download Documentation Created By: BOPADIGITAL Last Updated By: BOPADIGITAL Date Created: 21/12/25 Last Revision Date: 11/01/2026

Description: Authorized users download client documentation from the system for review, processing, or external submission to the operator. Actors: Sales Advisor, Immediate Supervisor, Administrator Preconditions: The user must be authenticated in the system.

2. The document must exist in the system.

3. The user must have permission to access the client's documents.

4. For Sales Advisors, the client must be assigned to them or be in their team.

Postconditions: 1. The document file is downloaded to the user's device.

2. The download action is logged in the system audit trail.

3. Document access statistics are updated.

Flow: 1. The User accesses the client profile in the CRM module.

2. The User navigates to the "Documents" tab.

3. The System displays all documents associated with the client including:

Document name, Document type, Upload date, File size, uploaded by, Tags.

4. The User can optionally filter documents by: Document type, Date range,

Tags, Advisor who uploaded.

5. The User locates the desired document.

6. The User clicks the "Download" button or download icon next to the

document.

7. The System verifies the user has permission to access the document.

8. The System retrieves the document file from secure storage.

9. The System initiates the file download to the user's device.

10. The System logs the download action including: User ID, Document ID,

Client ID, Download timestamp, User's IP address.

11. The System increments the document's download counter.

12. The download completes successfully.

13. The System displays a brief confirmation: "Document downloaded

successfully." Alternative Flows: 6a. User previews document before downloading:

1. The User clicks "Preview" instead of "Download".

2. The System displays the document in a preview window (for supported

formats).

3. The User reviews the document.

4. The User clicks "Download" from the preview window.

5. The flow continues at step 7.

6b. User downloads multiple documents:

1. The User selects multiple documents using checkboxes.

2. The User clicks "Download Selected" or "Download All".

3. The System creates a ZIP archive containing all selected documents.

4. The System names the archive: "[Client Name]_Documents_[Date].zip".

5. The flow continues at step 7 with the ZIP file.

### Table 2.27 Use Case Documentation - Download Documentation

### 79

4a. User applies filters:

1. The System updates the document list based on filter criteria.

2. The System displays: "Showing [N] documents matching your filters."

3. The flow continues at step 5 with filtered results.

Exceptions: 7. Permission denied:

1. The System displays: "Access denied. You do not have permission to

download this document."

2. The System logs the unauthorized access attempt.

3. The use case ends.

8. Document file not found:

1. The System displays: "Document file is missing or has been deleted. Please

contact support."

2. The System logs the error with document ID and storage location.

3. The System notifies the system administrator.

4. The use case ends.

9. Download interrupted:

1. The System detects the connection failure.

2. The System attempts to resume the download if the browser supports it.

3. If resume fails, the System displays: "Download interrupted. Please try

again."

4. The partial download action is still logged.

5. The use case ends.

3. No documents available:

1. The System displays: "No documents have been uploaded for this client

yet."

2. If the user is an advisor, the System displays an "Upload Document" button.

3. The use case ends.

Requirements: RF-DOC-006: The system shall allow authorized users to download client documentation. RF-DOC-007: The system shall log all documents and download actions for audit purposes.

### Table 2.27 (continued)

### 80

Name of Use Case: Tag Documentation Created By: BOPADIGITAL Last Updated By: BOPADIGITAL Date Created: 21/12/25 Last Revision Date: 11/01/2026

Description: The Sales Advisor or Coordinator adds or modifies tags to uploaded documents to improve organization, searchability, and categorization within the document management system. Actors: Sales Advisor, Administrators Preconditions: 1. The user must be authenticated in the system.

2. At least one document must be uploaded to a client profile.

3. The user must have permission to manage documentation.

4. For Sales Advisors, the client must be assigned to them.

Postconditions: 1. Document tags are updated in the database.

2. The tag modification is recorded in the document history.

3. Document searchability is improved based on new tags.

4. The tagging action is logged with user ID and timestamp.

Flow: 1. The User accesses the client profile in the CRM module.

2. The User navigates to the "Documents" tab.

3. The System displays all documents uploaded for the client with their

current tags.

4. The User selects a specific document to tag.

5. The User clicks "Edit Tags" or the tag icon.

6. The System displays the tag management interface showing: Current tags

(removable), Suggested tags based on document type, Custom tag input field, Recently used tags.

7. The User can perform any of the following actions: Add new tags by typing

and pressing Enter, Select from suggested tags, Remove existing tags by clicking the X icon, Add multiple tags separated by commas.

8. The System validates tag format (alphanumeric, max 50 characters per tag).

9. The System prevents duplicate tags.

10. The User clicks "Save Tags".

11. The System updates the document record with the new tag set.

12. The System records the tag modification in the document history with:

User ID, Previous tags, New tags, Timestamp.

13. The System updates the document search index.

14. The System displays a confirmation message: "Tags updated

successfully." Alternative Flows: 6a. Document has no tags:

1. The System displays: "No tags currently assigned. Add tags to improve

document organization."

2. The System suggests tags based on document type and client category.

3. The flow continues at step 7.

8a. Invalid tag format:

1. The System displays a validation error: "Tag '[tag name]' is invalid. Tags

must be alphanumeric and under 50 characters."

2. The System highlights the invalid tag.

3. The User corrects the tag.

4. The flow returns to step 8.

### Table 2.28 Use Case Documentation - Tag Documentation

### 81

9a. Duplicate tag detected:

1. The System silently prevents adding the duplicate tag.

2. The System displays a brief notification: "Duplicate tag ignored."

3. The flow continues normally.

7a. User applies bulk tags to multiple documents:

1. The User selects multiple documents using checkboxes.

2. The User clicks "Bulk Tag".

3. The System displays a tag input for multiple documents.

4. The User enters tags to apply to all selected documents.

5. The System applies tags to all selected documents.

6. The flow continues at step 11 for each document.

Exceptions: 11. Database update fails:

1. The System displays: "Tags could not be saved. Please try again."

2. The System logs the error.

3. The previous tags remain unchanged.

4. The use case ends.

13. Search index update fails:

1. The System completes the tag update anyway.

2. The System logs the indexing error.

3. The System schedules a reindex operation.

4. The tags are saved but may not be immediately searchable.

Requirements: RF-DOC-002: The system shall automatically tag uploaded documents based on document type. RF-DOC-005: The system shall allow users to add custom tags to documents for improved organization.

### Table 2.28 (continued)

### 82

Name of Use Case: Review Documentation Uploaded to Profile Created By: BOPADIGITAL Last Updated By: BOPADIGITAL Date Created: 21/12/25 Last Revision Date: 11/01/2026

Description: The Immediate Supervisor or Coordinator reviews all documentation uploaded by sales advisors to client profiles to verify completeness and compliance before service activation. Actors: Immediate Supervisor, Administrator Preconditions: 1. The user must be authenticated with the appropriate role.

2. The client profile must exist in the database.

3. At least one document must have been uploaded to the client profile.

4. The user must have permission to review documentation.

Postconditions: 1. The user has reviewed the client's documentation status.

2. Document review actions are logged in the system.

3. The user can identify missing or incomplete documentation.

Flow: 1. The User accesses the "Document Management" section in the CRM module.

2. The User searches for a client by RUC or Business Name.

3. The System displays search results with basic client information.

4. The User selects the specific client.

5. The System displays the client's document dashboard showing: Required

documents checklist with status (Complete/Pending/Missing), Optional documents list, Total number of uploaded documents, Last document upload date and user.

6. The User reviews the documentation status summary.

7. The User clicks on a specific document category to view details.

8. The System displays a list of all documents in that category including:

Document name, Upload date, Uploaded by (advisor name), File size, Tags, Status (Pending Review/Approved/Rejected).

9. The User selects a specific document to view.

10. The System displays the document preview or download option.

11. The User reviews the document content.

12. The User may mark the document as "Reviewed", "Approved", or

"Requires Correction".

13. If marking as "Requires Correction", the System requests a comment

explaining the issue.

14. The System records the review action with user ID and timestamp.

15. The System updates the document status.

16. If all required documents are approved, the System updates the client

status to "Documentation Complete". Alternative Flows: 6a. Missing required documents:

1. The System highlights missing required documents in red.

2. The System displays: "Missing required documents: [list of documents]."

3. The User may click "Notify Advisor" to send a reminder.

4. The System sends a notification to the responsible advisor.

5. The flow continues at step 7.

### Table 2.29 Use Case Documentation - Review Documentation Uploaded to Profile

### 83

12a. User requests document re-upload:

1. The User clicks "Request Re-upload".

2. The System displays a text field for specifying the reason.

3. The User enters the reason.

4. The System marks the document as "Rejected Re-upload Required".

5. The System sends a notification to the advisor who uploaded it.

6. The flow continues at step 14.

10a. Document preview not available:

1. The System displays: "Preview not available for this file type."

2. The System offers a "Download" button instead.

3. The flow continues at step 11.

Exceptions: 2. Search returns no results:

1. The System displays: "No clients found with the given criteria."

2. The User may modify search parameters or cancel.

3. The use case ends if canceled.

8. Document retrieval fails:

1. The System displays: "Unable to load documents at this time. Please try

again."

2. The System logs the error for technical review.

3. The use case ends.

10. Document file not found in storage:

1. The System displays: "Document file is missing or corrupted. Please

contact support."

2. The System logs the error with document ID.

3. The User can see document metadata but cannot view content.

Requirements: RF-DOC-003: The system shall allow supervisors and coordinators to review documentation uploaded to client profiles. RF-DOC-004: The system shall display documentation status (complete/pending/missing) for each client. RF-CRM-016: The system shall allow coordinators to verify pending documentation and track which advisor is responsible.

### Table 2.29 (continued)

### 84

Name of Use Case: Add Client Documentation Created By: BOPADIGITAL Last Updated By: BOPADIGITAL Date Created: 21/12/25 Last Revision Date: 11/01/2026

Description: The Sales Advisor uploads required and optional documents to the client's profile to support the negotiation and service activation process. Actors: Sales Advisor Preconditions: 1. The advisor must be authenticated in the system.

2. The client must exist in the database and be assigned to the advisor.

3. The document management module must be operational.

4. Documents must be in supported formats (PDF, JPG, PNG, DOCX).

5. Document size must not exceed 50MB per file.

Postconditions: 1. The document is stored in the system linked to the client profile.

2. The document receives automatic tags based on content type.

3. The upload event is recorded in the client history.

4. The document becomes visible to authorized users.

5. Pending documentation counters are updated.

Flow: 1. The Sales Advisor accesses the client profile in the CRM module.

2. The Advisor navigates to the "Documents" tab.

3. The System displays the current documentation list and pending

requirements.

4. The Advisor clicks "Upload New Document".

5. The System displays the document upload form with fields: Document type

(dropdown), Description (optional), Tags (optional), File selector.

6. The Advisor selects the document type from available options: RUC (Tax

ID), Constitutional document, Legal representative ID, Power of attorney, Proof of address, Other.

7. The Advisor optionally enters a description.

8. The Advisor clicks "Select File" and chooses the document from their

device.

9. The System validates the file format.

10. The System validates the file size.

11. The Advisor reviews the selected file information.

12. The Advisor clicks "Upload Document".

13. The System uploads the file to secure storage.

14. The System automatically generates tags based on document type.

15. The System creates a document record in the database linked to the client.

16. The System records metadata: Upload date and time, Uploading user, File

name and size, Document type.

17. The System updates pending documentation status.

18. The System displays a success message: "Document uploaded

successfully." Alternative Flows: 9a. Invalid file format:

1. The System rejects the file and displays: "Invalid file format. Accepted

formats are: PDF, JPG, PNG, DOCX."

2. The flow returns to step 8.

10a. File size exceeds limit:

1. The System rejects the file and displays: "File size exceeds the 50MB limit.

Please compress the file or upload a smaller version."

### Table 2.30 Use Case Documentation - Add Client Documentation

### 85

2. The flow returns to step 8.

14a. Advisor adds custom tags:

1. The Advisor clicks "Add Custom Tag".

2. The System displays a text field.

3. The Advisor enters custom tags separated by commas.

4. The System validates and adds the tags.

5. The flow continues at step 15.

Exceptions: 13. Upload fails due to connectivity issues:

1. The System displays: "Upload failed due to connection issues. Please check

your internet connection and try again."

2. The System logs the error.

3. The selected file remains in the form for retry.

4. The use case ends.

15. Database record creation fails:

1. The System displays: "The document was uploaded but could not be

registered. Please contact support."

2. The System logs the error with file reference.

3. The uploaded file is quarantined for manual recovery.

4. The use case ends.

Requirements: RF-DOC-001: The system shall allow sales advisors to upload client documentation to support negotiations. RF-DOC-002: The system shall automatically tag uploaded documents based on document type.

### Table 2.30 (continued)

### 86

Name of Use Case: Review and Approve New Matrices Created By: BOPADIGITAL Last Updated By: BOPADIGITAL Date Created: 21/12/25 Last Revision Date: 11/01/2026

Description: The Immediate Supervisor reviews offer matrices submitted by sales advisors and approves or rejects them based on commercial policies and business rules. Actors: Immediate Supervisor Preconditions: 1. The supervisor must be authenticated in the system.

2. At least one offer matrix must be in "Pending Approval" status.

3. The matrix must belong to an advisor in the supervisor's team.

4. The supervisor must have approval permissions.

Postconditions: 1. The matrix status is updated to "Approved" or "Rejected".

2. The sales advisor receives a notification of the decision.

3. The approval or rejection is recorded in the audit log.

4. If approved, the matrix becomes available to present to the client.

Flow: 1. The Immediate Supervisor accesses the "Matrix Approvals" section in the CRM module.

2. The System displays a list of pending matrices including: Client name,

Sales advisor, Creation date, Total value, Subsidy amount, Current status.

3. The Supervisor reviews the list of pending approvals.

4. The Supervisor selects a specific matrix to review.

5. The System displays the complete matrix details including: Selected

services and quantities, Individual and total prices, Applied subsidies and calculations, Client information and current billing, Advisor observations.

6. The Supervisor reviews the commercial viability of the offer.

7. The Supervisor verifies compliance with company policies.

8. The Supervisor clicks either "Approve Matrix" or "Reject Matrix".

9. If rejecting, the System displays a mandatory field requesting motive.

10. The Supervisor enters comments explaining the decision.

11. The Supervisor clicks "Confirm Decision".

12. The System validates that comments are provided if rejecting.

13. The System updates the matrix status accordingly.

14. The System records the decision in the audit log with: Supervisor ID,

Decision (Approved/Rejected), Timestamp, Comments.

15. The System sends a notification to the sales advisor.

16. The System displays a confirmation message: "Matrix

[Approved/Rejected] successfully." Alternative Flows: 8a. Supervisor needs more information:

1. The Supervisor clicks "Request Additional Information".

2. The System displays a text field for the information request.

3. The Supervisor enters the required information details.

4. The System updates the matrix status to "Information Requested".

5. The System sends a notification to the advisor.

6. The use case ends.

12a. Missing rejection comments:

1. The System displays: "Rejection reason is mandatory. Please provide

comments."

2. The System does not allow proceeding until comments are entered.

3. The flow returns to step 10.

### Table 2.31 Use Case Documentation - Review and Approve New Matrices

### 87

Exceptions: 13. Status update fails:

1. The System displays: "The decision could not be processed. Please try

again."

2. The System logs the error.

3. The matrix status remains unchanged.

4. The use case ends.

2. No pending matrices:

1. The System displays: "There are no matrices pending approval at this time."

2. The use case ends.

Requirements: RF-MAT-004: The system shall allow the immediate supervisor to approve or reject offer matrices submitted by advisors. RF-CRM-013: The system shall allow the immediate supervisor to review and approve commercial proposals generated by advisors.

### Table 2.31 (continued)

### 88

Name of Use Case: Request Supervisor Approval Created By: BOPADIGITAL Last Updated By: BOPADIGITAL Date Created: 21/12/25 Last Revision Date: 11/01/2026

Description: The Sales Advisor submits an offer matrix for review and approval by the immediate supervisor before presenting it to the client. Actors: Sales Advisor Preconditions: 1. The advisor must be authenticated in the system.

2. An offer matrix must exist and be in "Draft" or "Pending Approval" status.

3. The matrix must be complete with all required information.

4. The advisor must have permission to request approval.

Postconditions: 1. The matrix status changes to "Pending Approval".

2. The immediate supervisor receives a notification.

3. The matrix becomes visible in the supervisor's approval queue.

4. The request is logged with timestamp and advisor information.

Flow: 1. The Sales Advisor accesses the client's negotiation details.

2. The Advisor navigates to the "Offer Matrices" section.

3. The System displays all matrices associated with the negotiation and their

current status.

4. The Advisor selects a matrix in "Draft" status.

5. The Advisor reviews the matrix details.

6. The Advisor clicks "Request Approval".

7. The System displays a confirmation dialog: "Are you sure you want to

submit this matrix for supervisor approval?".

8. The Advisor confirms the submission.

9. The System validates that the matrix is complete.

10. The System updates the matrix status to "Pending Approval".

11. The System records the approval request with date, time, and advisor ID.

12. The System sends a notification to the immediate supervisor.

13. The System sends a notification email to the supervisor.

14. The System displays a confirmation message: "Approval request

submitted successfully. Your supervisor will review the matrix shortly." Alternative Flows: 9a. Matrix incomplete:

1. The System displays: "The matrix cannot be submitted. Please complete

all required fields: [list of missing fields]."

2. The Advisor clicks "Edit Matrix" to complete the information.

3. The use case ends.

8a. Advisor cancels:

1. The System closes the confirmation dialog.

2. The matrix status remains unchanged.

3. The use case ends.

Exceptions: 10. Status update fails:

1. The System displays: "The approval request could not be processed. Please

try again."

2. The System logs the error.

3. The matrix status remains unchanged.

4. The use case ends.

### Table 2.32 Use Case Documentation - Request Supervisor Approval

### 89

12. Notification service unavailable:

1. The System completes the status update anyway.

2. The System logs that the notification failed.

3. The System will attempt to resend the notification later.

4. The System displays a warning: "Approval requested, but supervisor

notification may be delayed." Requirements: RF-MAT-002: The system shall allow the sales advisor to submit offer matrices for supervisor approval.

### Table 2.32 (continued)

### 90

Name of Use Case: Create Offer Matrix for Specific Clients Created By: BOPADIGITAL Last Updated By: BOPADIGITAL Date Created: 21/12/25 Last Revision Date: 11/01/2026

Description: The Sales Advisor creates a new offer matrix for a specific business client, defining the proposed services, quantities, and calculating the applicable subsidies based on the client's billing and service portfolio. Actors: Sales Advisor Preconditions: 1. The advisor must be authenticated in the system.

2. The client must be registered and assigned to the advisor.

3. There must be an active negotiation with the client.

4. The service catalog must be accessible.

Postconditions: 1. A new offer matrix is created and stored in the database.

2. The matrix is linked to the client and the active negotiation.

3. The subsidy amount is automatically calculated based on business rules.

4. The matrix enters "Pending Approval" status.

5. The immediate supervisor receives a notification of the new matrix.

Flow: 1. The Sales Advisor accesses the client profile in the CRM module.

2. The Advisor navigates to the "Negotiations" section of the client.

3. The Advisor selects an active negotiation.

4. The Advisor clicks the "Create Offer Matrix" button.

5. The System displays the matrix creation form with available services

organized by category (Voice, Connectivity, Digital Services).

6. The Advisor selects the services to include in the offer.

7. The Advisor specifies the quantity for each selected service.

8. The System validates service availability with the operator.

9. The System automatically retrieves the client's current monthly billing.

10. The System automatically retrieves the client's number of active services.

11. The System calculates the applicable subsidy range based on: Client's

current billing amount, Number of services currently contracted, Number of new services proposed in the matrix.

12. The System displays the total estimated benefit amount.

13. The Advisor adds observations or special notes about the offer.

14. The Advisor clicks "Save Matrix".

15. The System validates that all required fields are completed.

16. The System creates the matrix record in the database with status "Pending

Approval".

17. The System links the matrix to the client and negotiation.

18. The System sends a notification to the immediate supervisor for approval.

19. The System displays a confirmation message: "Offer matrix created

successfully. Awaiting supervisor’s approval." Alternative Flows: 8a. Service unavailable with operator

1. The System displays a warning message: "The service [Service Name] is

not available in the client's geographic area."

2. The System removes the unavailable service from the selection.

3. The Advisor may select alternative services.

4. The flow returns to step 7.

### Table 2.33 Use Case Documentation - Create Offer Matrix for Specific Clients

### 91

15a. Validation fails

1. The System displays specific error messages indicating missing or invalid

fields.

2. The Advisor completes or corrects the required information.

3. The flow returns to step 14.

Exceptions: 8. Operator availability check fails:

1. The System displays: "Cannot verify service availability at this time. Please

try again later."

2. The System logs the error.

3. The use case ends.

16. Matrix creation fails:

1. The System displays: "The offer matrix could not be created. Please try

again."

2. The System logs the error for administrator review.

3. The entered data remains in the form.

4. The use case ends.

Requirements: RF-MAT-001: The system shall allow the sales advisor to create a new offer matrix associated with a business client and an ongoing negotiation. RF-MAT-003: The system shall automatically calculate the applicable subsidy range based on client billing and the number of proposed services,

### Table 2.33 (continued)

92

2. 3 Class Diagrams

# 93

1. BOPACORP S.A.

Auth

CoreUsers

ServiceCatalogCMS

Employability

CRM

OfferMatrices

Documents

Reports

SequenceDiagrams

Powered By Visual Paradigm Community Edition

# Figure 2.3

# BOPADIGITAL Class Diagram Overview

# 94

Auth

- email : String-passwordHash : String-isActive : boolean-createdAt : LocalDateTime-lastConnection : LocalDateTime-employee : Employee-role : Role+verifyActive() : boolean+addRole(role : Role) : boolean+hasPermission(resource : String, action : String) : boolean

SystemUser

+findByEmail(email : String) : SystemUser

<<Interface>> UserRepository

+generateHash(password : String) : String+verifyPassword(plainPassword : String, hashPassword : String) : boolean

<<Interface>> PasswordHasher

- hasher : PasswordHasher-users : UserRepository-tokenService : TokenService+login(email : String, plainPassword : String) : String+checkPermission(token : String, resource : String, action : String) : boolean

AuthService

+findByEmail(email : String) : SystemUser

PostgresUserRepository

+generateHash(password : String) : String+verifyPassword(plainPassword : String, hashPassword : String) : boolean

BcryptHasher

+generateToken(user : SystemUser) : String+validateToken(token : String) : boolean+getUserFromToken(token : String) : SystemUser

<<Interface>>TokenService

+generateToken(user : SystemUser) : String+validateToken(token : String) : boolean+getUserFromToken(token : String) : SystemUser

JwtTokenService

- name : String-description : String-permissions : Permission[]+addPermission(permission : Permission) : boolean+hasPermission(resource : String, action : String) : boolean

Role

- name : String-resourceCode : String-action : String+checkMatch(resource : String, action : String) : boolean

Permission

- role

1

- users

1

- tokenService

1

- hasher

1

- permissions

*

has

has

has

has

has

Powered By Visual Paradigm Community Edition

# Figure 2.4

# BOPADIGITAL Auth Module Class Diagram

# 95

CoreUsers

- employeeCode : String-firstName : String-secondName : String-lastName : String-secondLastName : String-credentials : SystemUser+getFullName() : String+getEmail() : String

Employee

SystemUser (Auth)

- commissionRate : double-salesZone : String-monthlySalesTarget : BigDecimal-accumulativeSales : BigDecimal-totalSalesMonth : int-currentMonthBilling : BigDecimal-createdMatrices : OfferMatrix[]-supervisors : ImmediateSupervisor[]-clients : BusinessClient[]-negotiationHistory : Negotiation[]-visitHistory : Visit[]+createOffer(negotiation : Negotiation) : OfferMatrix+registerClient(rucValue : String, businessName : String, contactName : String) : BusinessClient+addClient(client : BusinessClient) : void+removeClient(client : BusinessClient) : void+registerVisitResult(visit : Visit, gps : GPSCoordinates, observations : String) : void+advanceNegotiation(negotiation : Negotiation) : void+getClientVisitHistory(client : BusinessClient) : List<Visit>+startNegotiation(client : BusinessClient) : Negotiation+getMatricesPendingApproval() : List<OfferMatrix>+uploadDocumentToNegotiation(negotiation : Negotiation, file : File, docType : DocumentType) : NegotiationDocument+scheduleVisit(client : BusinessClient, type : VisitType, notes : String, date : Date) : Visit

SalesAdvisor

- managementRegion : String-objectives : SalesObjective[]+defineStrategicObjetctive(objective : SalesObjective) : void+managesZone(zone : String) : boolean+generateReport(facade : ReportFacade, filter : ReportFilter) : CommercialPerformanceReport+exportReportToPdf(report : Report) : void

Executive

- salesZone : String-subordinates : SalesAdvisor[]+addAdvisorToTeam(advisor : SalesAdvisor) : void+reviewOfferMatrix(matrix : OfferMatrix, isApproved : boolean, reason : String) : void+assignClientToAdvisor(client : BusinessClient, advisor : SalesAdvisor) : void+deactivateClient(client : BusinessClient) : void+getPendingMatrices() : List<OfferMatrix>+approveMatrix(matrix : OfferMatrix) : void+rejectMatrix(matrix : OfferMatrix, reason : String) : void+reviewVisit(visit : Visit, comments : String) : void+getSubordinates() : List<SalesAdvisor>

ImmediateSupervisor

- department : String+reviewDocument(document : NegotiationDocument, isApproved : boolean, reason : String) : void+authorizeServiceActivation(negotiation : Negotiation) : void+downloadDocument(document : NegotiationDocument) : File

Coordinator

+createCatalogItem(facade : CMSFacade, categoryName : String, item : CatalogItem) : boolean+editCompanyContent(facade : CMSFacade, key : String, newContent : String) : boolean+evaluateApplication(application : JobApplication, isApproved : boolean) : void

WebAdministrator

- serviceCatalog : Catalog-companyInfo : CompanyInfo

CMSFacade

(ServiceCatalogCMS)

- vacancies : JobVacancy[]

VacancyFacade(Employability)

GPSCoordinates

(CRM) VisitType (CRM)

Visit(CRM) OfferMatrix (OfferMatrices)

BusinessClient

(CRM)

Negotiation (CRM)

NegotiationDocument

(Documents)

ReportFacade (Reports)

SalesObjective (Reports)

- supervisors

- subordinates

*

*

- employee

- credentials

1

1

- manager

1 -objectives

*

defines

has

has

Powered By Visual Paradigm Community Edition

# Figure 2.5

# BOPADIGITAL CoreUsers Module Class Diagram

# 96

CRM

- activeServicesCount : int-currentMonthlyBilling : BigDecimal-isActive : boolean-address : String-contactName : String-contactPhone : String-contactEmail : String-seller : SalesAdvisor-visitLog : Visit[]-ruc : RUC-negotiationHistory : Negotiation[]-businessName : String+deactivate() : void+assignToAdvisor(advisor : SalesAdvisor) : void+unassignAdvisor() : void+addVisitToLog(visit : Visit) : void+addNegotiation(negotiation : Negotiation) : void+isActive() : boolean+searchCatalog(catalog : Catalog, keyword : String) : List<CatalogComponent>+filterServices(catalog : Catalog, criteria : CatalogFilterCriteria) : List<CatalogComponent>

BusinessClient

- value : String+isValid() : boolean+RUC(value : String)

RUC

SalesAdvisor(CoreUsers)

- startDate : Date-estimatedClosedDate : Date-observations : String-isActive : boolean-client : BusinessClient-advisor : SalesAdvisor-state : NegotiationState-visits : Visit[]-documents : NegotiationDocument[]-matrices : OfferMatrix[]-mandatoryDocuments : DocumentType[]+changeState(newState : NegotiationState) : void+getCurrentState() : NegotiationState+proceedToNextState() : void+cancel() : void+addVisitReport(visit : Visit) : void+addDocument(doc : NegotiationDocument) : void+addMatrix(matrix : OfferMatrix) : void+isActive() : boolean+hasApprovedMatrix() : boolean

Negotiation

- name : String-description : String#context : Negotiation+handleNextStage() : void+handleCancellation() : void+registerVisit(visit : Visit) : void+attachDocument(doc : NegotiationDocument) : void+generateOffer(matrix : OfferMatrix) : void

NegotiationState

- date : Date-observations : String-isVerified : boolean-supervisorComment : String-negotiation : Negotiation-verifiedBy : ImmediateSupervisor-advisor : SalesAdvisor-type : VisitType-coordinates : GPSCoordinates-client : BusinessClient+markAsRejected(supervisor : ImmediateSupervisor, reason : String) : void+calculateDistanceToClientOffice() : double+registerCheckIn(gps : GPSCoordinates, observations : String) : void+markAsVerified(supervisor : ImmediateSupervisor, comment : String) : void+isVerified() : boolean

Visit

+handleNextStage() : void

ProspectingState

+handleNextStage() : void InitialContactState

ActiveNegotiationState+handleNextStage() : void

+handleNextStage() : void

ClosingState

+handleNextStage() : void

PostSaleState

+handleNextStage() : void+handleCancellation() : void

CanceledState

- latitude : double-longitude : double-accuracy : double-timestamp : Date+getMapsLink() : String+GPSCoordinates(latitude : double, longitude : double, accuracy : double)+calculateDistance(targetLat : double, targetLon : double) : double

GPSCoordinates

- code : String-name : String-description : String

VisitType

ImmediateSupervisor

(CoreUsers)

NegotiationDocument

(Documents)

DocumentUploadService

(Documents)

OfferMatrix(OfferMatrices)

- name : String-description : String-isMandatory : boolean

DocumentType (Documents)

- advisor

- negotiationHistory

1

*

- mandatoryDocuments

*

- ruc

1

- seller

- clients

1

*

- type

1

- negotiation

- documents

1

*

#context

- state

1

1

- client

- negotiationHistory

1

*

1 -advisor -visitHistory

*

- negotiation

- visits

1

*

- visitLog

- client

*

1

- verifiedBy

1

- coordinates

1

- negotiation

- matrices

1

*

- type

1

has

has

has

has

receives

makes

supervises

has

has

has

has

has

has

hasAssigned

has

Powered By Visual Paradigm Community Edition

# Figure 2.6

# BOPADIGITAL CRM Module Class Diagram

# 97

Documents

- filename : String-fileExtension : String-fileSizeMb : double-storagePath : String-uploadDate : LocalDateTime-mimeType : String-extractExtension(name : String) : String+getAllowedExtensions() : String[]+validateFormat() : void+updateFileInfo(newFilePath : String, newSize : double) : void#setFilename(filename : String) : void#setStoragePath(path : String) : void

BaseDocument

- candidate : SalesAdvisorCandidate+getAllowedExtensions() : String[]

CandidateResume

- reviewDate : Date-coordinatorMessage : String-negotiation : Negotiation-type : DocumentType-state : DocumentNegotiationState-reviewedBy : Coordinator+changeState(newState : DocumentNegotiationState) : void+approveDocument(coordinator : Coordinator) : void+rejectDocument(coordinator : Coordinator, reason : String) : void+reuploadFile(newPath : String, newSize : double) : void+NegotiationDocument(negotiation : Negotiation, type : DocumentType, filename : String, storagePath : String)+getRecipientEmail() : String+getNotificationMessage() : String+getNotificationTitle() : String+getAllowedExtensions() : String[]

NegotiationDocument

- name : String-description : String-isMandatory : boolean

- name : String-description : String#context : NegotiationDocument+approve(coordinator : Coordinator) : void+replaceFile(newFilePath : String, newSize : double) : void+reject(coordinator : Coordinator, reason : String) : void DocumentType

DocumentNegotiationState

PendingApprovalState RejectedStateAcceptedState

Coordinator(CoreUsers)

+downloadFile(storagePath : String) : File+uploadFile(file : File, destinationFolder : String) : String

<<Interface>> FileStorageService

+uploadFile(file : File, destinationFolder : String) : String+downloadFile(storagePath : String) : File-extractFilename(path : String) : String

S3EmcryptedStorage

- storageService : FileStorageService-instance : DocumentUploadService-documentFactory : DocumentFactory-DocumentUploadService()+uploadFile(file : File, destinationFolder : String) : BaseDocument+setFactory(factory : DocumentFactory) : void

DocumentUploadService

+withMandatory(isMandatory : boolean) : DocumentConfig+withCoordinatorMessage(message : String) : DocumentConfig+withDocumentType(type : DocumentType) : DocumentConfig+withMimeType(mimeType : String) : DocumentConfig+withDescription(description : String) : DocumentConfig+DocumentConfig(filename : String, storagePath : String)+withReviewDate(reviewDate : Date) : DocumentConfig+withNegotiation(negotiation : Negotiation) : DocumentConfig

DocumentConfig

+createDocument(config : DocumentConfig) : BaseDocument+processDocument(config : DocumentConfig) : BaseDocument

DocumentFactory

CandidateResumeFactory

NegotiationDocumentFactory

- description : String-matrix : OfferMatrix+getAllowedExtensions() : String[]

MatrixAttachment

MatrixAttachmentFactory

- subscribers : Subscriber[]+subscribe(observer : Subscriber) : void+unsubscribe(observer : Subscriber) : void+notifySubscribers() : void+Publisher()

Publisher (Employability)

+getRecipientEmail() : String+getNotificationMessage() : String+getNotificationTitle() : String

<<Interface>> NotifiableEntity (Employability)

ObserverPattern

- instance

1

- reviewedBy

1

#context

- state

1

1

- type

1

- type

1

- storageService

1

- documentFactory

1

has

has

has

has

reviews

has

has

Powered By Visual Paradigm Community Edition

# Figure 2.7

# BOPADIGITAL Documents Module Class Diagram

# 98

Employability

- title : String-description : String-requirements : String[]-publicatioDate : LocalDateTime-closingDate : LocalDateTime-requiredDocuments : String[]-isActive : boolean-isPublished : boolean-applications : JobApplication[]+closeVacancy() : void+isActive() : boolean+isExpired() : boolean+isPublished() : boolean+updateVacancy(title : String, closingDate : LocalDateTime) : boolean+addApplication(application : JobApplication) : void

JobVacancy

- applicationDate : LocalDateTime-coverLetter : String-isReviewed : boolean-reviewNotes : String-reviewDate : String-candidate : SalesAdvisorCandidate-currentState : ApplicationState-attachedResume : CandidateResume-vacancy : JobVacancy+changeState(newState : ApplicationState) : void+submit() : void+evaluateApplication(isApproved : boolean) : void+JobApplication(candidate : SalesAdvisorCandidate, vacancy : JobVacancy)+attachResume(resume : CandidateResume) : void+getRecipientEmail() : String+getNotificationMessage() : String+getNotificationTitle() : String

JobApplication

- name : String-description : String#context : JobApplication+submitApplication() : void+evaluate(isApproved : boolean) : void

ApplicationState

DraftState

PendingState

AcceptedState

RejectedState

- name : String-lastname : String-email : String-phone : String-address : String-applicationCount : int-applications : JobApplication[]-resumeHistory : CandidateResume[]+getApplications() : JobApplication[]+getLatestResume() : CandidateResume+applyToVacancy(vacancy : JobVacancy, resumeFile : File) : JobApplication+uploadResume(file : File) : CandidateResume+viewActiveVacancies(facade : VacancyFacade) : List<JobVacancy>

SalesAdvisorCandidate

- subscribers : Subscriber[]+subscribe(observer : Subscriber) : void+unsubscribe(observer : Subscriber) : void+notifySubscribers() : void+Publisher()

Publisher

+update(context : NotifiableEntity) : void

<<Interface>> Subscriber

+getRecipientEmail() : String+getNotificationMessage() : String+getNotificationTitle() : String

<<Interface>> NotifiableEntity

+update(context : NotifiableEntity) : void+sendEmail(to : String, subject : String, body : String) : void

EmailService

+update(context : NotifiableEntity) : void+sendPushNotification(title : String, body : String) : void

InternNotificationService

- vacancies : JobVacancy[]+getActiveVacancies() : List<JobVacancy>+createJobVacancy(vacancy : JobVacancy) : boolean+updateJobVacancy(vacancy : JobVacancy) : boolean+deleteJobVacancy(vacancy : JobVacancy) : boolean+publishJobVacancy(vacancy : JobVacancy) : boolean+unpublishJobVacancy(vacancy : JobVacancy) : boolean

VacancyFacade

CandidateResume (Documents)

DocumentUploadService

(Documents)

- subscribers

*

- candidate

- resumeHistory

1

*

vacancy

applications

1

*

- vacancies

*

- attachedResume

1

#context

- currentState

1

1

- candidate

- applications

1

*

has

hasAttached

has

manages

has

apply

has

Powered By Visual Paradigm Community Edition

# Figure 2.8

# BOPADIGITAL Employability Module Class Diagram

# 99

OfferMatrices

- creationDate : Date-observations : String-totalAmount : BigDecimal-calculatedSubsidy : BigDecimal-isApproved : boolean-approvalDate : Date-supervisorMessage : String-negotiation : Negotiation-state : MatrixState-subsidyStrategy : SubsidyCalculationStrategy-items : MatrixLineItem[]-approvedBy : ImmediateSupervisor-creator : SalesAdvisor-attachments : MatrixAttachment[]+changeState(newState : MatrixState) : void+getCurrentState() : MatrixState+sendToSupervisor() : void+approve(supervisor : ImmediateSupervisor) : void+reject(supervisor : ImmediateSupervisor, reason : String) : void+recalculateTotals() : void+addAttachment(attachment : MatrixAttachment) : void+OfferMatrix(negotiation : Negotiation, creator : SalesAdvisor)+addItem(catalogItem : CatalogItem, quantity : int, customPrice : BigDecimal) : boolean+saveDraft(observations : String) : void+hasItems() : boolean+getRecipientEmail() : String+getNotificationMessage() : String+getNotificationTitle() : String

OfferMatrix

- name : String-description : String#context : OfferMatrix+editDetails() : void+sendForApproval() : void+approve(supervisor : ImmediateSupervisor) : void+reject(supervisor : ImmediateSupervisor, reason : String) : void

MatrixState

+editDetails() : void+sendForApproval() : void

DraftMatrixState

+approve(supervisor : ImmediateSupervisor) : void+reject(supervisor : ImmediateSupervisor, reason : String) : void

PendingApprovalState

ApprovedMatrixState

RejectedMatrixState+editDetails() : void

+calculate(totalMatrixValue : BigDecimal, clientCurrentBilling : BigDecimal, serviceCount : BigDecimal) : BigDecimal

<<Interface>>

SubsidyCalculationStrategy

+calculate(totalMatrixValue : BigDecimal, clientCurrentBilling : BigDecimal, serviceCount : BigDecimal) : BigDecimal-calculateBillingFactor(billing : BigDecimal) : BigDecimal-calculateServiceFactor(services : BigDecimal) : BigDecimal

StandardSubsidyStrategy

- quantity : int-unitPrice : BigDecimal-total : BigDecimal-matrix : OfferMatrix-item : CatalogItem+calculateTotal() : BigDecimal+MatrixLineItem(matrix : OfferMatrix, item : CatalogItem, quantity : int, customPrice : BigDecimal)

MatrixLineItem

CatalogItem (ServiceCatalogCMS)

ImmediateSupervisor

(CoreUsers)

SalesAdvisor(CoreUsers)

MatrixAttachment

(Documents)

DocumentUploadService

(Documents)

- subscribers : Subscriber[]+subscribe(observer : Subscriber) : void+unsubscribe(observer : Subscriber) : void+notifySubscribers() : void

Publisher (Employability)

+getRecipientEmail() : String+getNotificationMessage() : String+getNotificationTitle() : String

<<Interface>> NotifiableEntity (Employability)

#context

- state

1

1

- matrix

- items

1

*

- item

1

- matrix

- attachments

1

*

- approvedBy

1

- subsidyStrategy

1

- createdMatrices

- creator

*

1

has

creates

supervises

has

has

has

has

Powered By Visual Paradigm Community Edition

# Figure 2.9

# BOPADIGITAL OfferMatrices Module Class Diagram

# 100

Reports

- title : String-generationDate : LocalDateTime-exporter : ReportExporter-generatedBy : Employee-metrics : PerformanceMetric[]-visualizations : ReportChart[]+addMetric(metric : PerformanceMetric) : void+operation() : void+Report(generatedBy : Employee, title : String)+addVisualization(chart : ReportChart) : void+getMetrics() : List<PerformanceMetric>+exportData(exporter : ReportExporter) : File+setExporter(exporter : ReportExporter) : void+getTitle() : String+getGenerationDate() : LocalDateTime+getGeneratedBy()

Report

+export(report : Report) : File

<<Interface>> ReportExporter

+export(report : Report) : File-generateFilename(title : String) : String-writeMetricsToPdf(file : File, metrics : List<PerformanceMetric>) : void

PDFExporter

+export(report : Report) : File

ExcelExporter

- startDate : Date-endDate : Date-zone : String-serviceType : Category+validateDates() : boolean+ReportFilter(startDate : Date, endDate : Date)+matchesDate(dateToCheck : Date) : boolean+withZone(zone : String) : ReportFilter+withServiceType(type : Category) : ReportFilter

ReportFilter

Category

(ServiceCatalogCMS)

- metricName : String-value : double-unit : String-report : Report+validateData() : boolean+PerformanceMetric(metricName : String, value : double, unit : String)

PerformanceMetric

- targetSalesAmount : BigDecimal-targetClosedDeals : int-periodStart : Date-periodEnd : Date-manager : Executive+calculateSalesCompletionPercentage(actualValue : BigDecimal) : BigDecimal

SalesObjective

Employee (CoreUsers)

- analyzedAdvisors : SalesAdvisor[]-marketInsights : List<String>+addMarketInsight(insight : String) : void+CommercialPerformanceReport(manager : Executive)+addAnalyzedAdvisor(advisor : SalesAdvisor) : void+getAnalyzedAdvisors() : List<SalesAdvisor>

CommercialPerformanceReport

- benchmarkObjective : SalesObjective+OperationalReport(supervisor : ImmediateSupervisor)

OperationalReport

SalesAdvisor(CoreUsers)

AdvisorDashboard

- title : String-description : String-labels : String[]-values : double[]-report : Report-type : ChartType+addDataPoint(label : String, value : double) : void

ReportChart

- name : String-description : String

ChartType

+generateManagerReport(manager : Executive, filter : ReportFilter) : CommercialPerformanceReport+generateSupervisorReport(supervisor : ImmediateSupervisor, filter : ReportFilter) : OperationalReport

ReportFacade

Executive(CoreUsers)

- type

1

- advisor

1

- report

- metrics

1

*

- exporter

1

- generatedBy

1

- benchmarkObjective

1

- report

- visualizations

1

*

- analyzedAdvisors

*

- serviceType

1

has

has

has

has

has

has

has generates

has

Powered By Visual Paradigm Community Edition

# Figure 2.10

# BOPADIGITAL Reports Module Class Diagram

# 101

ServiceCatalogCMS

- name : String-description : String+getDetails() : String+getPrice() : BigDecimal+search(keyword : String) : List<CatalogComponent>+filter(criteria : CatalogFilterCriteria) : List<CatalogComponent>

CatalogComponent

- children : CatalogComponent[]+add(component : CatalogComponent) : boolean+remove(component : CatalogComponent) : boolean+getItems() : List<CatalogComponent>+Category()+search(keyword : String) : List<CatalogComponent>+filter(criteria : CatalogFilterCriteria) : List<CatalogComponent>+getPrice() : BigDecimal

Category

- price : BigDecimal-conditions : Condition[]-benefits : Benefit[]+isMatch(criteria : CatalogFilterCriteria) : boolean+filter(criteria : CatalogFilterCriteria) : List<CatalogComponent>+addCondition(condition) : void+addBenefit(benefit) : void

CatalogItem

- gigasTotal : int-minutes : int-sms : int

VoiceService

ConectivityService-bandWidth : double

- provider : String

DigitalService

- categories : CatalogComponent[]+filter(criteria : CatalogFilterCriteria) : List<CatalogComponent>+search(keyword : String) : List<CatalogComponent>+addItem(component : CatalogComponent) : boolean+removeItem(component : CatalogComponent) : boolean+getCategory(categoryName : String) : CatalogComponent+Catalog()+getAllCategories() : List<CatalogComponent>

Catalog

+getDetails() : void <<Interface>> Benefit

+getDetails() : void <<Interface>> Condition

+getDetails() : void ElectiveBenefit

TemporalBenefit+getDetails() : void

+getDetails() : void AgeCondition

+getDetails() : void LegalCondition

- key : String-content : String-type : ContentType+updateContent(newContent : String) : boolean+ContentBlock(key : String, type : ContentType)

ContentBlock

- code : String-name : String-description : String

ContentType

- searchTerm : String-minPrice : BigDecimal-maxPrice : BigDecimal-coverage : String-categoryName : String+CatalogFilterCriteria()+withSearchTerm(term : String) : CatalogFilterCriteria+withPriceRange(min : BigDecimal, max : BigDecimal) : CatalogFilterCriteria+withCategory(category : String) : CatalogFilterCriteria

CatalogFilterCriteria

- contents : ContentBlock[]+getMission() : ContentBlock+getVision() : ContentBlock+getHistory() : ContentBlock+getValues() : ContentBlock+CompanyInfo()-findByKey(key : String) : ContentBlock+updateInfo(key : String, content : String) : void

CompanyInfo

- serviceCatalog : Catalog-companyInfo : CompanyInfo+updateCatalogComponent(item : CatalogComponent) : boolean+deleteCatalogComponent(item : CatalogComponent) : boolean+editWebsiteContent(content : ContentBlock) : boolean+editCompanyInfo(key : String, content : String) : boolean+CMSFacade()+addRootCategory(category : Category) : boolean+addItemToCategory(categoryName : String, item : CatalogItem) : boolean+browseCategories() : List<CatalogComponent>+filterServices(criteria : CatalogFilterCriteria) : List<CatalogComponent>

CMSFacade

- serviceCatalog

1

- type

1

- categories

*

- companyInfo

1

- conditions

*

- benefits

*

- children

*

- contents

*

manages

manages

has

has

has

has

has

owns

Powered By Visual Paradigm Community Edition

# Figure 2.11

# BOPADIGITAL ServiceCatalogCMS Module Class Diagram

102

2. 4 Object Diagrams

# 103

1_CRM

employeeCode = SA-2024-011firstName = JuanlastName = PerezsalesZone = Guayaquil NortecommissionRate = 0.05monthlySalesTarget = 15000.00 advisor1 : SalesAdvisor

businessName = TechSolutions S.A.contactName = Carlos MendozacontactPhone = 0991234567contactEmail = cmendoza@espol.edu.ecaddress = Av. Francisco de OrellanaisActive = trueactiveServicesCount = 0

client1 : BusinessClient

value = 0991234567001

ruc1 : RUC

startDate = 2025-10-10estimatedClosedDate = 2025-12-15observations = Cliente interesado en plan corporativoisActive = true

neg1 : Negotiation

activeStatus : ActiveNegotiationStatename = ACTIVE

date = 2025-10-10observations = Primera visita - presentacion de serviciosisVerified = truesupervisorComment = Visita verificada correctamente

visit1 : Visit

latitude = -2.1894longitude = -79.8891accuracy = 5.0timestamp = 2025-10-10 10:30:00

gps1 : GPSCoordinates

Powered By Visual Paradigm Community Edition

# Figure 2.12

# BOPADIGITAL CRM Object Diagram Overview

# 104

2_OfferMatrix

creationDate = 2025-01-15observations = Oferta plan corporativototalAmount = 850.00calculatedSubsidy = 85.00isApproved = falseapprovalDate = null

matrix1 : OfferMatrix

pendingStatus : PendingApprovalStatename = PENDING

strategy1 : StandardSubsidyStrategy

item1 : MatrixLineItemquantity = 5unitPrice = 120.00total = 600.00 item2 : MatrixLineItemquantity = 2unitPrice = 125.00total = 250.00

name = Plan Voz Corporativo 500description = 500 min nacionalesprice = 120.00

service1 : CatalogItem

name = Internet Fibra 100Mbpsdescription = Fibra optica empresarialprice = 125.00

service2 : CatalogItem

employeeCode = SA-2024-011firstName = JuanlastName = PerezsalesZone = Guayaquil NortecommissionRate = 0.05monthlySalesTarget = 15000.00 advisor1 : SalesAdvisor

startDate = 2025-10-10estimatedClosedDate = 2025-12-15observations = Cliente interesado en plan corporativoisActive = true

neg1 : Negotiation

Powered By Visual Paradigm Community Edition

# Figure 2.13

# BOPADIGITAL OfferMatrix Object Diagram Overview

# 105

3_Catalog

catalog1 : Catalog

name = Servicios de Vozdescription = Planes de telefonía móvil

voiceCat : Category

name = Conectividaddescription = Internet y fibra óptica

internetCat : Category

name = Servicios Digitalesdescription = Apps y plataformas

digitalCat : Category

name = Plan Voz 500description = 500 min nacionalesprice = 25.00minutes = 500sms = 100gigasTotal = 5 voicePlan1 : VoiceService

name = Plan Voz 1000description = 1000 min + roamingprice = 45.00minutes = 1000sms = 100gigasTotal = 5

voicePlan2 : VoiceService

conectivity1 : ConectivityServicename = Fibra 100mbpsdescription = Internet Empresarialprice = 89.00bandWidth = 100.00

conectivity2 : ConectivityServicename = Fibra 300mbpsdescription = Alta velocidadprice = 129.00bandWidth = 300.0

name = Cloud Storage 1 TBdescription = Almacenamiento nubeprice = 15.00provider = Movistar Cloud

digital1 : DigitalService

3FreeMonths : TemporalBenefit

includedRouter : ElectiveBenefit

Powered By Visual Paradigm Community Edition

# Figure 2.14

# BOPADIGITAL Catalog Object Diagram Overview

# 106

4_Auth

authService :AuthService

hasher : BcryptHasher

tokenService : JwtTokenService

users :

PostgresUserRepository

email = jperez@bopacorp.ecpasswordHash = $2a$10$N9qo8uLO...isActive = truecreatedAt = 2024-06-15 08:00:00lastConnection = 2025-12-15 09:30:00

user1 : SystemUser

name = SALES_ADVISORdescription = Asesor Comercial de Bopacorp

advisorRole : Role

name = Gestionar clientesaction = manageresourceCode = clients perm1 : Permission name = Crear negociacionesaction = createresourceCode = negotiations

perm2 : Permission

name = Registrar Visitasaction = createresourceCode = visits perm3 : Permission

employeeCode = SA-2024-011firstName = JuanlastName = PerezsalesZone = Guayaquil NortecommissionRate = 0.05monthlySalesTarget = 15000.00 advisor1 : SalesAdvisor

Powered By Visual Paradigm Community Edition

# Figure 2.15

# BOPADIGITAL Auth Object Diagram Overview

# 107

5_Documents

startDate = 2025-10-10estimatedClosedDate = 2025-12-15observations = Cliente interesado en plan corporativoisActive = true

neg1 : Negotiation

factory1 :

NegotiationDocumentFactory

filename = contrato_empresarial.pdfstoragePath = s3://bopa-docs/neg-2025-001/mimeType = application/pdfisMandatory = truedescription = contrato de servicios

config1 : DocumentConfig

acceptedState :AcceptedState

rejectedState :RejectedState

filename = contrato_empresarial.pdffileExtension = pdffileSizeMb = 1.8storagePath = s3://bopa-docs/neg-2025-001/uploadDate = 2025-01-15 10:30:00reviewDate = nullcoordinatorMessage = null

doc1 : NegotiationDocument pendingState :

PendingApprovalState

employeeCode = CORD-001firstName = MarialastName = Gonzálezdepartment = Documentacion

coord1 : Coordinator

employeeCode = SA-2024-011firstName = JuanlastName = PerezsalesZone = Guayaquil NortecommissionRate = 0.05monthlySalesTarget = 15000.00 advisor1 : SalesAdvisor

Powered By Visual Paradigm Community Edition

# Figure 2.16

# BOPADIGITAL Documents Object Diagram Overview

108

2. 5 Components Diagram

# 109

<<component>> BOPADIGITAL System

Presentation Layer

Business Domain

Application Services

Infrastructure Components

External Systems

<<component>> <<component>>Public Web Portal

Internal Management Web

<<component>>

Sales Advisor Mobile App

CRM Subsystem <<component>>

Negotiation Management

Offer Matrix Subsystem

<<component>>

Offer Matrix Management

<<component>>

Matrix State Management

<<component>> Subsidy Calculation

<<component>> Approval Management

Commercial Support<<component>>

Catalog Management <<component>> Vacancy Management

<<component>>Visit Management

<<component>> Client Management

<<component>> Notification Service <<component>>

Authentication Service

<<component>>

Content Management Service

<<component>>Reporting Service<<component>>

Document Management Service

<<component>> Persistence Service <<component>>Email Service<<component>>GPS Service<<component>> Telecommunication

Platform

<<component>>

File Storage Components

Powered By Visual Paradigm Community Edition

# Figure 2.17

# BOPADIGITAL Components Object Diagram

110

2. 6 Deployment Diagram

# 111

<<component>> Client Layer

Web Browser

Mobile App (iOS/Android)

<<component>>

DMZ Load Balancer

nginx Firewall

<<component>> Application Server

Web Server (Apache/nginx)

Application Server (Node.js/Java)

<<artifact>>CMS Module

<<artifact>>CRM Module

<<artifact>> Reporting Module

<<artifact>>

Document Management

<<artifact>> Search Engine

<<component>> File Storage File Server

Document Storage

<<artifact>> Database Server

Database Postgres SQL / MySQL

Cache Redils

<<artifact>> External ServicesCarrier API Activation

Service

SMTP (Email Services)

API CallsNotifications

Cache SQL

Store/Retrieve

HTTPS

HTTPS

Powered By Visual Paradigm Community Edition

# Figure 2.18

# BOPADIGITAL Deployment Diagram

CHAPTER 3 SYSTEM BEHAVIORAL MODELING

# 113

# 3.1 Activity Diagrams

act [1_NegotiationLifeCycle]

Register Client

Assign client to advisor

Create Negotiation

Set state: Prospecting

Schedule and make visit

Registrate check-in GPS

Set state: Canceled

State: PostSale

Negotiation Completed

Advance Status Repeat Visit

Negotiation

State !- PostSale?

Cancel negotiation?

Visit was verified by supervisor?

Valid RUC?

[no]

[yes]

[no]

[yes]

[no] [yes]

[yes]

[no]

Powered By Visual Paradigm Community Edition

# Figure 3.1 BOPADIGITAL Activity Diagram – Negotiation Life Cycle

# 114

act [2_OfferMatrices]

Create Offer Matrix

Set State: Draft

Add line items (services from catalog)

Calculate Subsidy

Save draft

Send for approval

Set state: PendingApproval

Supervisor reviews matrix

Set state: Approved Set state: Rejected

Notify Advisor Notify advisor with reason

Edit and retry?

Approved?

Has items?

More items?

[yes]

[no]

[no]

[yes]

[yes] [no]

[no] [yes]

Powered By Visual Paradigm Community Edition

# Figure 3.2 BOPADIGITAL Activity Diagram – Offer Matrices

# 115

act [3_VisitManagement]

Management

Schedule visit (client, date, type)

Travel to client location

Register check-in

Capture GPS coordinates

Add observations

Supervisor reviews visit

Mark as verified Mark As Rejected

Add to negotiation history Request new visit

Add visit report to negotiation

Link to negotiation?

GPS distance <= 100m? [yes] [no]

[no]

[yes]

Powered By Visual Paradigm Community Edition

# Figure 3.3 BOPADIGITAL Activity Diagram – Visit Management

# 116

act [4_Auth]

Enter email and password

Find user by email

Alert user not found

Get stored password hash

Verify password with BcryptHasher

Check user is active Alert invalid credentials

Generate JWT Alert inactive user

Return token to user

Update last connection

is active?

Password valid?

User exists?

[yes] [no]

[yes] [no]

[yes] [no]

Powered By Visual Paradigm Community Edition

# Figure 3.4 BOPADIGITAL Activity Diagram – Auth

# 117

act [5_DocumentManagement]

Upload document

Set State: PendingApproval

Coordinator reviews document

Set State: Approved Set State: Rejected

Notify advisor with reason

Replace file

Reupload?

is Approved?

[yes] [no]

[yes]

[no]

Powered By Visual Paradigm Community Edition

# Figure 3.5 BOPADIGITAL Activity Diagram – Document Management

118

3. 2 Sequence Diagrams

# 119

sd

[10_registerVisit]

opt

[negotiation != null] : SalesAdvisor

visit : Visit

negotiation : Negotiation

gps : GPSCoordinates

1. 6:

1. 4: negotiation

1. 1.2:

1. 2:

1. 1.1: setTimestamp(timestamp : Date = new Date()) : void

1. 7:

1. 5: addVisitReport(visit : Visit = visit) : void

1. 3: getNegotiation() : Negotiation

1. 1: registerCheckIn(gps : GPSCoordinates = gps, observations : String = observations) : void

1: registerVisitResult(visit : Visit, gps : GPSCoordinates, observations : String) : void

Powered By Visual Paradigm Community Edition

# Figure 3.6

# BOPADIGITAL Sequence Diagram - registerVisit

# 120

sd

[11_reviewVisit]

alt

[distance <= maxAllowedDistance][else] : ImmediateSupervisor

visit : Visit

coordinates : GPSCoordinates

1. 4: 1.6:

1. 1.2: visitLat 1.1.4: visitLon 1.1.6: distance

1. 1.5: calculateDistance(targetLat : double = visitLat, targetLon : double = visitLon) : double1.2: distance

1. 1.3: getLongitude() : double

1. 1.1: getLatitude() : double

1. 7:

1. 5: markAsRejected(supervisor : ImmediateSupervisor = this, reason : String = comments) : void

1. 3: markAsVerified(supervisor : ImmediateSupervisor = this, comment : String = comments) : void

1. 1: calculateDistanceToClientOffice() : double

1: reviewVisit(visit : Visit, comments : String) : void

Powered By Visual Paradigm Community Edition

# Figure 3.7

# BOPADIGITAL Sequence Diagram - reviewVisit

# 121

sd

[12_updateNegotiationStatus]

opt

[hasApproved]

: SalesAdvisor

negotiation : Negotiation

currentState : ActiveNegotiationState

newtState : ClosingState

1. 1.1.5:

1. 1.1.4: changeState(newState : NegotiationState) : void

1. 1.1.4: <<create>>

1. 1.1.3: hasApproved

1. 1.1.2: hasApprovedMatrix() : boolean

2: getContext() : Negotiation1.1.1.1: negotiation

1. 1.1.6:

1. 1.1.6.1:

1. 1.1: handleNextStage() : void

1. 1.1.6.1.1:

1. 1: proceedToNextState() : void

1: advanceNegotiation(negotiation : Negotiation) : void

Powered By Visual Paradigm Community Edition

# Figure 3.8

# BOPADIGITAL Sequence Diagram - updateNegotiationStatus

# 122

sd

[13_checkVisitHistory]

loop

[for each allVisits]

opt

[isVerified] : SalesAdvisor

client : BusinessClient

verifiedVisits : ArrayList

visit : Visit

1. 5: isVerified

1. 2: allVisits

1. 7: verifiedVisits

1. 6: add(visit)

1. 4: isVerified() : boolean

1. 3: <<create>>

1. 1: getVisitHistory() : List<Visit>

1: getClientVisitHistory(client : BusinessClient) : List<Visit>

Powered By Visual Paradigm Community Edition

# Figure 3.9

# BOPADIGITAL Sequence Diagram - checkVisitHistory

# 123

sd

[14_deactivateClient]

opt

[seller != null] : ImmediateSupervisor

client : BusinessClient

previousAdvisor : SalesAdvisor

1. 6:

3. 1:

2. 1:

1. 3.2: previousAdvisor

1. 4:

3: removeClient(client : BusinessClient = this) : void

1. 3.1: getSeller() : SalesAdvisor2: setSeller(seller : SalesAdvisor = null) : void

1. 2: seller

1. 7:

1. 5: deactivate() : void

1. 1: getSeller() : SalesAdvisor1.3: unassignAdvisor() : void

1: deactivateClient(client : BusinessClient) : void

Powered By Visual Paradigm Community Edition

# Figure 3.10

# BOPADIGITAL Sequence Diagram - deactivateClient

# 124

sd

[15_createOfferMatrix]

: SalesAdvisor

matrix : OfferMatrix

createdMatrices :List<OfferMatrix>

negotiation : Negotiation

matrices :

List<OfferMatrix>

1. 3.2:

1. 4:

1. 3.1: add(matrix)

1. 5: matrix

1. 3: addMatrix(matrix : OfferMatrix = matrix) : void

1. 2: add(matrix)

1. 1: <<create>>

1: createOffer(negotiation : Negotiation) : OfferMatrix

Powered By Visual Paradigm Community Edition

# Figure 3.11

# BOPADIGITAL Sequence Diagram - createOfferMatrix

# 125

sd

[16_addItemToMatrix]

opt

[wasAdded] : OfferMatrix

lineItem : MatrixLineItem

items : List<MatrixLineItem>

1. 4:

2: wasAdded

1. 3: recalculateTotals() : void

1. 2: add(lineItem)

1. 1: <<create>>

1: addItem(catalogItem : CatalogItem, quantity : int, customPrice : BigDecimal) : boolean

Powered By Visual Paradigm Community Edition

# Figure 3.12

# BOPADIGITAL Sequence Diagram - addItemToMatrix

# 126

sd

[17_recalculateTotals]

loop

[for each this.items] : OfferMatrix

item : MatrixLineItem

itemsTotal : BigDecimal

negotiation : Negotiation

client : BusinessClient

servicesBD : BigDecimal

subsidyStrategy : SubsidyCalculationStrategy

4. 1: servicesCount

6. 1: subsidy

3. 1: clientBilling

2. 1: client

1. 6: 7.1:

1. 4:

1. 2: itemTotal

8:

7: setCalculatedSubsidy(calculatedSubsidy : BigDecimal = subsidy) : void 6: calculate(totalMatrixValue : BigDecimal = this.totalAmount, clientCurrentBilling : BigDecimal = clientBilling, serviceCount : BigDecimal = servicesBD) : BigDecimal

5: <<create>>

4: getActiveServicesCount() : int

3: getCurrentMonthlyBilling() : BigDecimal

2: getClient() : BusinessClient

1. 5: setTotalAmount(totalAmount : BigDecimal = itemsTotal) : void

1. 3: add(itemTotal)

1. 1: calculateTotal() : BigDecimal

1: recalculateTotals() : void

Powered By Visual Paradigm Community Edition

# Figure 3.13

# BOPADIGITAL Sequence Diagram - recalculateTotals

# 127

sd

[18_saveDraft]

opt

[hasItems] matrix : OfferMatrix

currentState : DraftMatrixState

4. 1:

3. 1: hasItems

2. 2: matrix

1. 2: currentState

4. 2:

4: recalculateTotals() : void 3: hasItems() : boolean

2. 1: getContext() : OfferMatrix

4. 3:

2: editDetails() : void

1. 1: getCurrentState() : MatrixState

1: saveDraft(observations : String) : void

Powered By Visual Paradigm Community Edition

# Figure 3.14

# BOPADIGITAL Sequence Diagram - saveDraft

# 128

sd

[19_sendToSupervisor] opt

[hasItems]

: OfferMatrix

currentState : DraftMatrixState

nextState : PendingApprovalState

4. 1: 5.1:

4: changeState(newState : MatrixState = nextState) : void

5:

2. 1: hasItems

1. 1.2: matrix

5. 2:

3: <<create>>

2: hasItems() : boolean

1. 1.1: getContext() : OfferMatrix

5. 3:

1. 1: sendForApproval() : void

1: sendToSupervisor() : void

Powered By Visual Paradigm Community Edition

# Figure 3.15

# BOPADIGITAL Sequence Diagram - sendToSupervisor

# 129

sd

[1_Login]

opt

[isValid] : AuthService

users : UserRepository

user : SystemUser

hasher : PasswordHasher

tokenService : TokenService

1. 8: token

1. 6: isValid

1. 4: storedHash

1. 2: user

1. 9: token

1. 7: generateToken(user : SystemUser = user) : String

1. 5: verifyPassword(plainPassword : String = plainPassword, hashPassword : String = storedHash) : boolean

1. 3: getPasswordHash() : String

1. 1: findByEmail(email : String = email) : SystemUser

1: login(email : String, plainPassword : String) : String

Powered By Visual Paradigm Community Edition

# Figure 3.16

# BOPADIGITAL Sequence Diagram - Login

# 130

sd

[20_listPendingMatrices]

loop

loop opt

[for each subordinates]

[for each this.createdMatrices][isPending]

: ImmediateSupervisor

pendingMatrices : ArrayList<OfferMatrix>

advisor : SalesAdvisor

pendingMatrices : ArrayList<OfferMatrix>

matrix : OfferMatrix

2. 5:

2. 3: currentState

2. 6: advisorMatrices

2. 4: add(matrix)

2. 2: getCurrentState() : MatrixState

2. 1: <<create>>

1. 3: subordinates

4: pendingMatrices

3: addAll(advisorMatrices)

2: getMatricesPendingApproval() : List<OfferMatrix>

1. 2: getSubordinates() : List<SalesAdvisor>

1. 1: <<create>>

1: getPendingMatrices() : List<OfferMatrix>

Powered By Visual Paradigm Community Edition

# Figure 3.17

# BOPADIGITAL Sequence Diagram - listPendingMatrices

# 131

sd

[21_approveMatrix]

: ImmediateSupervisor

matrix : OfferMatrix

currentState : PendingApprovalState

this.approvalDate : Date

approvedState : ApprovedMatrixState

{}

2. 4: 3.1:

3. 2:

2. 3: changeState(newState : MatrixState = approvedState) : void3: notifySubscribers() : void

2. 2: <<create>>

2. 1: <<create>>

1. 3.2: matrix

1. 4:

2: approve(supervisor : ImmediateSupervisor = supervisor) : void

1. 3.1: getContext() : OfferMatrix

1. 2: currentState

1. 5:

1. 3: approve(supervisor : ImmediateSupervisor = this) : void

1. 1: getCurrentState() : MatrixState

1: approveMatrix(matrix : OfferMatrix) : void

Powered By Visual Paradigm Community Edition

# Figure 3.18

# BOPADIGITAL Sequence Diagram - approveMatrix

# 132

sd

[22_rejectMatrix]

: ImmediateSupervisor

matrix : OfferMatrix

currentState : PendingApprovalState

rejectedState : RejectedMatrixState

2. 3: 3.1:

3. 2:

2. 2: changeState(newState : MatrixState = rejectedState) : void3: notifySubscribers() : void

2. 1: <<create>>

1. 3.2: matrix

1. 2: currentState

1. 4:

2: reject(supervisor : ImmediateSupervisor = supervisor, reason : String = reason) : void

1. 3.1: getContext() : OfferMatrix

1. 5:

1. 3: reject(supervisor : ImmediateSupervisor = this, reason : String = reason) : void

1. 1: getCurrentState() : MatrixState

1: rejectMatrix(matrix : OfferMatrix, reason : String) : void

Powered By Visual Paradigm Community Edition

# Figure 3.19

# BOPADIGITAL Sequence Diagram - rejectMatrix

# 133

sd

[23_uploadDocument]

: SalesAdvisor

storage : S3EmcryptedStorage

negotiation : Negotiation

file : File

config : DocumentConfig

factory : NegotiationDocumentFactory

1. 15: doc

1. 10: 1.12:

1. 7: fileName

1. 5: storagePath

1. 3: hashCode

1. 17:

1. 16: addDocument(doc : NegotiationDocument = document) : void

1. 14: processDocument(config : DocumentConfig = config) : BaseDocument

1. 13: <<create>>

1. 11: withNegotiation(negotiation : Negotiation = negotiation) : DocumentConfig

1. 9: withDocumentType(type : DocumentType = docType) : DocumentConfig

1. 8: <<create>>

1. 6: getName()

1. 4: uploadFile(file : File = file, destinationFolder : String = destinationFolder) : String

1. 2: hashCode()

1. 1: <<create>>

1: uploadDocumentToNegotiation(negotiation : Negotiation, file : File, docType : DocumentType) : NegotiationDocument

Powered By Visual Paradigm Community Edition

# Figure 3.20

# BOPADIGITAL Sequence Diagram - uploadDocument

# 134

sd

[24_approveDocument]

alt

[isApproved] [else] : Coordinator

document : NegotiationDocument

currentState : PendingApprovalState

acceptedState : AcceptedState

1. 2.2: document

1. 5:

2. 3:

2. 4:

2. 2: changeState(newState : DocumentNegotiationState = acceptedState) : void

2. 1: <<create>>

1. 3:

2: approveDocument(coordinator : Coordinator = coordinator) : void

1. 2.1: getContext() : NegotiationDocument

1. 6:

1. 4: reject(coordinator : Coordinator = this, reason : String = reason) : void

1. 2: approve(coordinator : Coordinator = this) : void

1. 1: getState() : DocumentNegotiationState

1: reviewDocument(document : NegotiationDocument, isApproved : boolean, reason : String) : void

Powered By Visual Paradigm Community Edition

# Figure 3.21

# BOPADIGITAL Sequence Diagram - approveDocument

# 135

sd

[25_rejectDocument]

alt

[isApproved] [else] : Coordinator

document : NegotiationDocument

currentState : PendingApprovalState

rejectedState : RejectedState

emailService : EmailService

4. 1:

2. 3:

4. 2:

4: update(context : NotifiableEntity = this) : void

3:

2. 2: changeState(newState : DocumentNegotiationState = rejectedState) : void

2. 1:

1. 5.2: document

1. 6:

2: rejectDocument(coordinator : Coordinator = coordinator, reason : String = reason) : void

1. 5.1: getContext() : NegotiationDocument

1. 4:

1. 2: currentState

1. 7:

1. 5: reject(coordinator : Coordinator = this, reason : String = reason) : void

1. 3: approve(coordinator : Coordinator = this) : void

1. 1: getState() : DocumentNegotiationState

1: reviewDocument(document : NegotiationDocument, isApproved : boolean, reason : String) : void

Powered By Visual Paradigm Community Edition

# Figure 3.22

# BOPADIGITAL Sequence Diagram - rejectDocument

# 136

sd

[26_downloadDocument]

: Coordinator

document : NegotiationDocument

storage : S3EmcryptedStorage

downloadedFile : File

1. 4.2: filename

3: downloadedFile

2: <<create>>

1. 4.1: extractFilename(path : String = storagePath) : String

1. 2: storagePath

1. 5: downloadedFile

1. 4: downloadFile(storagePath : String = storagePath) : File

1. 3: <<create>>

1. 1: getStoragePath() : String

1: downloadDocument(document : NegotiationDocument) : File

Powered By Visual Paradigm Community Edition

# Figure 3.23

# BOPADIGITAL Sequence Diagram - downloadDocument

# 137

sd

[27_searchCatalog]

loop

[for each categories]

: BusinessClient

catalog : Catalog

results : ArrayList<CatalogComponent>

category : CatalogComponent

2. 1: categoryResults

1. 1.3: categories

4: results

3: addAll(categoryResults)

2: search(keyword : String = keyword) : List<CatalogComponent>

1. 1.2: getAllCategories() : List<CatalogComponent>

1. 1.1: <<create>>

1. 1: search(keyword : String = keyword) : List<CatalogComponent> 1.2: results

1: searchCatalog(catalog : Catalog, keyword : String) : List<CatalogComponent>

Powered By Visual Paradigm Community Edition

# Figure 3.24

# BOPADIGITAL Sequence Diagram - searchCatalog

# 138

sd

[28_filterCatalog]

loop

[for each categories]

: BusinessClient

catalog : Catalog

results : ArrayList<CatalogComponent>

category : CatalogComponent

3. 1:

2. 1: categoryResults

1. 1.3: categories

1. 2: results

3: addAll(categoryResults)

2: filter(criteria : CatalogFilterCriteria = criteria) : List<CatalogComponent>

1. 1.2: getAllCategories() : List<CatalogComponent>

1. 1.1: <<create>>

1. 3: results

1. 1: filter(criteria : CatalogFilterCriteria = criteria) : List<CatalogComponent>

1: filterServices(catalog : Catalog, criteria : CatalogFilterCriteria) : List<CatalogComponent>

Powered By Visual Paradigm Community Edition

# Figure 3.25

# BOPADIGITAL Sequence Diagram - filterCatalog

# 139

sd

[29_createCatalogItem]

loop

[for each this.categories]

: WebAdministrator

facade : CMSFacade

serviceCatalog : Catalog

category : Category

category : CatalogComponent

name : String

1. 1.1.4: matches

1. 1.1.2: name

1. 1.4: wasAdded

1. 1.2: category

1. 1.1.3: equals(categoryName)

1. 1.1.1: getName() : String

1. 2: wasAdded

1. 1.3: add(component : CatalogComponent = item) : boolean

1. 1.1: getCategory(categoryName : String = categoryName) : CatalogComponent

1. 3: wasAdded

1. 1: addItemToCategory(categoryName : String = categoryName, item : CatalogItem = item) : boolean

1: createCatalogItem(facade : CMSFacade, categoryName : String, item : CatalogItem) : boolean

Powered By Visual Paradigm Community Edition

# Figure 3.26

# BOPADIGITAL Sequence Diagram - createCatalogItem

## 140

sd

[2_checkPermission]

opt

[isValidToken]

opt

[isActive] : AuthService

tokenService : TokenService

user : SystemUser

1. 8: hasPermission

1. 6: isActive

1. 4: user

1. 2: isValidToken

1. 9: hasPermission

1. 7: hasPermission(resource : String = resource, action : String = action) : boolean

1. 5: verifyActive() : boolean

1. 3: getUserFromToken(token : String = token) : SystemUser

1. 1: validateToken(token : String = token) : boolean

1: checkPermission(token : String, resource : String, action : String) : boolean

Powered By Visual Paradigm Community Edition

## Figure 3.27

## BOPADIGITAL Sequence Diagram – checkPermission

# 141

sd

[30_editWebContents]

opt

[block != null]

: WebAdministrator

facade : CMSFacade

companyInfo : CompanyInfo

block : ContentBlock

1. 1.1.3: wasUpdated

1. 1.2:

1. 1.1.2: updateContent(newContent : String = content) : boolean

1. 1.1.1: findByKey(key : String = key) : ContentBlock

1. 2: wasEdited

1. 1.1: updateInfo(key : String = key, content : String = content) : void

1. 3: wasEdited

1. 1: editCompanyInfo(key : String = key, content : String = newContent) : boolean

1: editCompanyContent(facade : CMSFacade, key : String, newContent : String) : boolean

Powered By Visual Paradigm Community Edition

# Figure 3.28

# BOPADIGITAL Sequence Diagram – editWebContents

# 142

sd

[31_generateReport]

opt

[validFilter]

: Executive

facade : ReportFacade

filter : ReportFilter

report : CommercialPerformanceReport

salesMetric : PerformanceMetric

conversionMetric : PerformanceMetric

1. 1.6: 1.1.9: 1.1.11:

1. 1.2: validFilters

1. 2: report

1. 1.8: addMetric(metric : PerformanceMetric = conversionMetric) : void1.1.10: addMarketInsight(insight : String = "Analisis del periodo") : void

1. 1.7: <<create>>

1. 1.5: addMetric(metric : PerformanceMetric = salesMetric) : void

1. 1.4: <<create>>

1. 1.3: <<create>>

1. 1.1: validateDates() : boolean

1. 3: report

1. 1: generateManagerReport(manager : Executive = this, filter : ReportFilter = filter) : CommercialPerformanceReport

1: generateReport(facade : ReportFacade, filter : ReportFilter) : CommercialPerformanceReport

Powered By Visual Paradigm Community Edition

# Figure 3.29

# BOPADIGITAL Sequence Diagram – generateReport

# 143

sd

[32_exportReport]

: Executive

pdfExporter : PDFExporter

report : Report

currentExporter : PDFExporter

pdfFile : File

3. 1: metrics

3: getMetrics() : List<PerformanceMetric>

1. 2.2.4: filename

1. 2.2.2: title

5: pdfFile

4:

2: <<create>>

1. 2.2.3: generateFilename(title : String = title) : String

1. 2.2.1: getTitle() : String

1. 3: exportedFile

1. 2.2: export(report : Report = this) : File

1. 2.1: setExporter(exporter : ReportExporter = exporter) : void

1. 4:

1. 2: exportData(exporter : ReportExporter = pdfExporter) : File

1. 1: <<create>>

1: exportReportToPdf(report : Report) : void

Powered By Visual Paradigm Community Edition

# Figure 3.30

# BOPADIGITAL Sequence Diagram – exportReport

## 144

sd

[3_activeVacancies]

loop

[for each vacancies]

opt

[isActive && isPublished] : VacancyFacade

activeList : ArrayList

vacancy : JobVacancy

1. 7:

1. 5: isPublished

1. 3: isActive

1. 8: activeList

1. 6: add(vacancy)

1. 4: isPublished() : boolean

1. 2: isActive() : boolean

1. 1: <<create>>

1: getActiveVacancies() : List<JobVacancy>

Powered By Visual Paradigm Community Edition

## Figure 3.31

## BOPADIGITAL Sequence Diagram – activeVacancies

## 145

sd

[4_applyToVacancy]

: SalesAdvisorCandidate

application : JobApplication

vacancy : JobVacancy

1. 9:

1. 7:

1. 5:

1. 3: resume

1. 10: application

1. 8: submit() : void

1. 6: addApplication(application : JobApplication = application) : void

1. 4: attachResume(resume : CandidateResume = resume) : void

1. 2: uploadResume(file : File = resumeFile) : CandidateResume

1. 1: <<create>>

1: applyToVacancy(vacancy : JobVacancy, resumeFile : File) : JobApplication

Powered By Visual Paradigm Community Edition

## Figure 3.32

## BOPADIGITAL Sequence Diagram – applyToVacancy

# 146

sd

[5_evaluateApplication]

alt

[isApproved] [else]

loop

[for each subscribers] : JobApplication

currentState : PendingState

nextState : AcceptedState

nextState : RejectedState

subscriber : Subscriber

1. 1.5.2:

1. 1.5.1.1: update(context : NotifiableEntity = (NotifiableEntity) this) : void

1. 1.4:1.1.5:

1. 1.3: changeState(newState : ApplicationState = nextState) : void

1. 1.2: <<create>>

1. 1.1: <<create>>

1. 1.5.3:

1. 1.5.1:

1. 1: evaluate(isApproved : boolean = isApproved) : void

1: evaluateApplication(isApproved : boolean) : void

Powered By Visual Paradigm Community Edition

# Figure 3.33

# BOPADIGITAL Sequence Diagram – evaluateApplication

# 147

sd

[6_submitApplication]

loop

[for each subscribers] : JobApplication

currentState : DraftState

nextState : PendingState

subscriber : Subscriber

1. 1.4.2:

1. 1.3:

1. 1.4.1:

1. 1.4.1.1: update(context : NotifiableEntity = (NotifiableEntity) this) : void

1: submit() : void

1. 1: submitApplication() : void

1. 1.4.3:

1. 1.4:

1. 1.2: changeState(newState : ApplicationState = nextState) : void

1. 1.1: <<create>>

Powered By Visual Paradigm Community Edition

# Figure 3.34

# BOPADIGITAL Sequence Diagram – submitApplication

# 148

sd

[7_registrateClient]

opt

[isValidRuc] : SalesAdvisor

ruc : RUC

client : BusinessClient

1. 5.2: 1.5.3:

1. 5.1: addClient(client : BusinessClient = this) : void

1. 3: isValidRuc

1. 5.4: client

1. 5: assignToAdvisor(advisor : SalesAdvisor = this) : void

1. 4: <<create>>

1. 1: <<create>>1.2: isValid() : boolean

1: registerClient(rucValue : String, businessName : String, contactName : String) : BusinessClient

Powered By Visual Paradigm Community Edition

# Figure 3.35

# BOPADIGITAL Sequence Diagram – registrateClient

# 149

sd

[8_assignClient]

opt

[hasCurrentAdvisor] : ImmediateSupervisor

client : BusinessClient

previousAdvisor : SalesAdvisor

advisor : SalesAdvisor

1. 5.2:

1. 6:

1. 5.1: addClient(client : BusinessClient = this) : void

1. 3.2:

1. 4:

1. 3.1: removeClient(client : BusinessClient = this) : void

1. 2: currentAdvisor

1. 7:

1. 5: assignToAdvisor(advisor : SalesAdvisor = advisor) : void

1. 1: getSeller() : SalesAdvisor1.3: unassignAdvisor() : void

1: assignClientToAdvisor(client : BusinessClient, advisor : SalesAdvisor) : void

Powered By Visual Paradigm Community Edition

# Figure 3.36

# BOPADIGITAL Sequence Diagram – assignClient

# 150

sd

[9_scheduleVisit]

: SalesAdvisor

visit : Visit

visitHistory : List<Visit>

client : BusinessClient

visitLog : List<Visit>

1. 3:

1. 4.2:

1. 5:

1. 4.1: add(visit)

1. 6: visit

1. 4: addVisitToLog(visit : Visit = visit) : void

1. 2: add(visit)

1. 1: <<create>>

1:

Powered By Visual Paradigm Community Edition

# Figure 3.37

# BOPADIGITAL Sequence Diagram – scheduleVisit

151

3. 3 Collaboration–Communication Diagrams

# 152

sd

1_Auth

authService : AuthService

postgresUserRepository : PostgresUserRepository

systemUser : SystemUser

bcryptHasher : BcryptHasher

jwtTokenService : JwtTokenService

7: return token

6: generateToken(user) 5: return true

4: verifyPassword(plain, hash) 3: return user

2: getPasswordHash()

1: findByEmail(email)

Powered By Visual Paradigm Community Edition

# Figure 3.38

# BOPADIGITAL Communication Diagram – Auth

# 153

sd

2_ApproveOfferMatrix immediateSupervisor : ImmediateSupervisor

offerMatrix : OfferMatrix

pendingApprovalState : PendingApprovalState

approvedMatrixState : ApprovedMatrixState

emailService : EmailService

6: notifySubscribers()

5: setContext(matrix)

4: changeState(approvedState)

3: matrix.approve(sup)

2: approve(supervisor)

1: approveMatrix(matrix)

Powered By Visual Paradigm Community Edition

# Figure 3.39

# BOPADIGITAL Communication Diagram – Approve Offer Matrix

# 154

sd

3_uploadDocument salesAdvisor : SalesAdvisor

negotiation : Negotiation

negotiationDocumentFactory : NegotiationDocumentFactory

negotiationDocument : NegotiationDocument

documentUploadService : DocumentUploadService

7: setNegotiation(negotiation)

6: addDocument(doc)

5: return doc

4: createDocument(config)

3: processDocument(config)

2: return storagePath

1: uploadFile(file, folder)

Powered By Visual Paradigm Community Edition

# Figure 3.40

# BOPADIGITAL Communication Diagram – uploadDocument

# 155

# 3.4 State Diagrams

stm [1_Negotiation]

Cancelled

PostSale

Closing

ActiveNegotiation

InitialContact

Prospecting

handleCancelation()

handleCancelation()

handleCancelation()

handleCancelation()

handleNextStage()

handleNextStage() [hasApprovedMatrix]

handleNextStage()

handleNextStage()

create negotiation

Powered By Visual Paradigm Community Edition

# Figure 3.41 BOPADIGITAL State Diagram – Negotiation

## 156

stm [2_OfferMatrix]

Rejected

Approved

PendingApproval

Draft

editDetails()

reject(supervisor, reason)

approve(supervisor)

sendForApproval [hasItems]

editDetails() create matrix

Powered By Visual Paradigm Community Edition

## Figure 3.42 BOPADIGITAL State Diagram – Offer Matrix

## 157

stm [3_NegotiationDocument]

Rejected Accepted

PendingApproval replaceFile(newPath, newSize)

reject(coordinator, reason) approve(coordinator)

upload document

Powered By Visual Paradigm Community Edition

## Figure 3.43 BOPADIGITAL State Diagram – Negotiation Document

## 158

stm [4_JobApplication]

Accepted Rejected

Pending

Draft

submitApplication()

create application

evaluate(true) evaluate(false)

Powered By Visual Paradigm Community Edition

## Figure 3.44 BOPADIGITAL State Diagram – Job Application

CHAPTER 4 INDIVIDUAL CONTRIBUTIONS

Name Contributions

Aragon Intriago Shirley

Yamel

Documentation of sprint backlogs and project schedule,

development of activity diagrams for system processes,

and support in the modeling of collaboration and state

diagrams.

Diaz Osorio Fernando

Nahim

Identification and documentation of project risks,

participation in sprint planning activities, and

contribution to the definition and documentation of

use case diagrams.

Muñoz Sanchez Salvador

Gabriel

Design and documentation of class diagrams aligned

with SOLID principles, modeling of object diagrams

for key system aspects, and contribution to the system

component and deployment diagrams.

Navarrete Castillo Anthony

Josue

Development of the system prototype, modeling of

sequence diagrams for transactional algorithms, and

participation in the documentation of system behavior

diagrams.

Tumbaco Santana Gabriel

Alejandro

Integration and consistency of project documentation,

coordination of static and behavioral UML modeling

(use case, component, deployment, and activity

diagrams), and consolidation of the system prototype.

Table 4.1 Individual Contributions of the Project

CHAPTER 5 AUTHORSHIP DECLARATION

We, the undersigned members of the BOPADIGITAL development team, hereby declare that

the present document titled “BOPACORP S.A. Requirements Specification Document” has

been entirely prepared by us as part of the course Software Engineering I at the Escuela

Superior Politécnica del Litoral (ESPOL).

We affirm that all sections, analyses, and specifications contained in this document represent our

own work and understanding, based on information gathered from the client and the

methodologies applied during the software requirements engineering process.

No part of this document has been copied, plagiarized, or taken from other sources without

proper acknowledgment. Any external reference used has been duly cited in the bibliography

according to academic integrity standards.

Each member of the team assumes full responsibility for the authenticity, accuracy, and

originality of the content herein.

Digital Confirmation: All members of the team confirm authorship through their electronic

submission of this document.

Team Members:

Aragon Intriago Shirley Yamel

Diaz Osorio Fernando Nahim

Muñoz Sanchez Salvador Gabriel

Navarrete Castillo Anthony Josue

Tumbaco Santana Gabriel Alejandro

APPENDIX I PROTOTYPE

1. Prototype’s Screenshots

1. 0.1 Sales Advisor’s flow

Figure-A I-1 BOPADIGITAL Prototype - Main view of the Sales Dashboard displaying the Kanban board with customer distribution by stages.

Figure-A I-2 BOPADIGITAL Prototype - Visualization of the ability to move clients across stages within the Kanban board.

162

Figure-A I-3 BOPADIGITAL Prototype - Detailed view of the client , showing contact information, interaction history, and visit planning panel.

Figure-A I-4 BOPADIGITAL Prototype - “Edit Client” modal window allowing the modification of tax information (RUC, Legal Name) and contact details.

163

Figure-A I-5 BOPADIGITAL Prototype - System notification displayed in the upper-right corner confirming the successful update of client data.

Figure-A I-6 BOPADIGITAL Prototype - “My Performance” screen displaying key KPI cards and the monthly revenue goal progress bar.

164

Figure-A I-7 BOPADIGITAL Prototype - Graphical analysis section within “My Performance”, detailing the client pipeline by stage and sales distribution by service.

Figure-A I-8 BOPADIGITAL Prototype - “Weekly Activity” area chart and commercial efficiency metrics (Average per Sale and Visit Rate).

165

Figure-A I-9 BOPADIGITAL Prototype - “Client Management” module presenting the complete tabular listing of the client portfolio with a global search bar.

Figure-A I-10 BOPADIGITAL Prototype - Demonstration of the client list filtering functionality, isolating only those in the “Negotiation” stage.

166

Figure-A I-11 BOPADIGITAL Prototype - “Add New Client” modal form for registering new prospects, capturing tax data (RUC), contact information, and initial stage.

Figure-A I-12 BOPADIGITAL Prototype - “Visit Calendar” module (January 2026 view) with status summary (Completed vs. Overdue) and monthly schedule visualization.

167

Figure-A I-13 BOPADIGITAL Prototype - Client management panel: visit history displayed on the left and mandatory document upload section on the right.

Figure-A I-14 BOPADIGITAL Prototype - Calendar navigation to future months (February 2026), enabling long-term visit planning and scheduling.

168

Figure-A I-15 BOPADIGITAL Advisor - "Offer Matrices" dashboard managing commercial proposals, displaying status counters (Drafts, Pending, Approved) and a list of client proposals with subsidy details.

Figure-A I-16 BOPADIGITAL Advisor - "New Offer Matrix" modal allowing the creation of a commercial proposal by selecting a client, adding products, and uploading necessary attachments.

169

Figure-A I-17 BOPADIGITAL Advisor - "Edit Offer Matrix" interface for modifying specific line items within a proposal, such as adjusting quantities, unit prices, and adding item-specific notes.

Figure-A I-18 BOPADIGITAL Advisor - Detailed view of an "Approved" Offer Matrix, highlighting the automatic subsidy calculation, final total, and supervisor approval comments.

170

1. 0.2 CMS screenshots

Figure-A I-19 BOPADIGITAL CMS - Product and Services Catalog dashboard displaying inventory statistics (Total, Active, Discontinued) and the product grid.

Figure-A I-20 BOPADIGITAL CMS - Catalog filtering functionality, demonstrating the isolation of products within the "Telephony" category.

171

Figure-A I-21 BOPADIGITAL CMS - Catalog view filtered by "Discontinued" status, highlighting legacy services with distinct visual tags.

Figure-A I-22 BOPADIGITAL CMS - Search bar functionality enabling quick retrieval of specific services (e.g., "Internet Fibra Óptica") by name.

172

Figure-A I-23 BOPADIGITAL CMS - "New Product" modal interface allowing administrators to register new services with defined categories, pricing, and status.

Figure-A I-24 BOPADIGITAL CMS - "Edit Product" modal for modifying existing service details, including descriptions, pricing attributes, and image URLs.

173

Figure-A I-25 BOPADIGITAL CMS - Security confirmation dialog ensuring administrative verification before permanently removing a product from the catalog.

Figure-A I-26 BOPADIGITAL CMS - Web Content Editor dashboard used to manage public-facing website elements, showing content status and preview cards.

174

Figure-A I-27 BOPADIGITAL CMS - Section filtering mechanism in the Web Content Editor, allowing focused management of specific page areas (e.g., Main Banner).

Figure-A I-28 BOPADIGITAL CMS - Content modification modal for updating website assets, including visibility toggles, display order, titles, and subtitles.

175

1. 0.3 Administrator’s flow

Figure-A I-29 BOPADIGITAL Admin - General Metrics Dashboard providing a consolidated view of commercial performance, including sales totals, conversion rates, and active team members.

Figure-A I-30 BOPADIGITAL Admin - "Top Performers" section ranking sales advisors based on closed sales value and visit volume.

176

Figure-A I-31 BOPADIGITAL Admin - Notification dropdown displaying real-time alerts regarding document approvals and rejections for specific clients.

Figure-A I-32 BOPADIGITAL Admin - System feedback (toast notification) confirming that all alerts have been marked as read.

177

Figure-A I-33 BOPADIGITAL Admin - System feedback confirming the successful deletion of notifications from the user’s history.

Figure-A I-34 BOPADIGITAL Admin - "Advisor Management" screen showing the team roster, status indicators, and alerts for pending document reviews.

178

Figure-A I-35 BOPADIGITAL Admin - "New Advisor" modal form used to register a new sales representative in the system.

Figure-A I-36 BOPADIGITAL Admin - List view demonstrating the filtering capability to isolate "Inactive" advisors.

179

Figure-A I-37 BOPADIGITAL Admin - Advisor Profile Modal: "Change History" tab tracking specific actions and updates made by the advisor.

Figure-A I-38 BOPADIGITAL Admin - Advisor Profile Modal: "Assigned Clients" tab displaying the advisor’s current portfolio and account status.

180

Figure-A I-39 BOPADIGITAL Admin - Advisor Profile Modal: "Documents" tab summarizing the approval status of files uploaded by the advisor.

Figure-A I-40 BOPADIGITAL Admin - Advisor Profile Modal: "Performance Metrics" tab showing KPIs like total invoicing and sales conversion rates.

181

Figure-A I-41 BOPADIGITAL Admin - Advisor Profile Modal: "Recent Activities" timeline logging the advisor’s latest interactions and system events.

Figure-A I-42 BOPADIGITAL Admin - "Contact Management" screen showing the "Unassigned Contacts" tab, a pool of leads waiting for distribution.

182

Figure-A I-43 BOPADIGITAL Admin - Unassigned contacts filtered by the "Prospecting" stage to prioritize early-stage lead distribution.

Figure-A I-44 BOPADIGITAL Admin - Bulk selection of unassigned contacts to be transferred to a specific advisor (e.g., Patricia Vargas).

183

Figure-A I-45 BOPADIGITAL Admin - Toast notification confirming the successful assignment of selected contacts to the target advisor.

Figure-A I-46 BOPADIGITAL Admin - "Assigned Contacts" tab displaying the master list of clients that are currently managed by an advisor.

184

Figure-A I-47 BOPADIGITAL Admin - "Add New Client" modal allowing administrators to manually inject new leads into the system.

Figure-A I-48 BOPADIGITAL Admin - "Document Management" module for centralized bulk processing (approve/reject) of client documentation.

185

Figure-A I-49 BOPADIGITAL Admin - Document filtering functionality, showing the list filtered by "Pending" status to prioritize urgent reviews.

Figure-A I-50 BOPADIGITAL Admin - Selection mechanism allowing administrators to choose specific documents (or all) to perform bulk actions like approval or rejection.

186

Figure-A I-51 BOPADIGITAL Admin - "Reject Document" modal requiring the administrator to provide a mandatory reason for the rejection before processing.

Figure-A I-52 BOPADIGITAL Admin - System notification confirming the initiation of a secure bulk download for the selected client documentation.

187

Figure-A I-53 BOPADIGITAL Admin - "Commercial Performance Reports" dashboard offering a high-level overview of sales productivity and team metrics.

Figure-A I-54 BOPADIGITAL Admin - Advanced reporting filters applied to analyze a specific advisor’s performance (e.g., Roberto Mendoza) over the last semester.

188

Figure-A I-55 BOPADIGITAL Admin - "Export Report" function allowing data to be generated and downloaded as a PDF file for external presentation.

Figure-A I-56 BOPADIGITAL Admin - "Recent Activity" audit log tracking system-wide events such as closed sales, document uploads, and login sessions.

189

Figure-A I-57 BOPADIGITAL Admin - "Document Configuration" panel used to define mandatory or optional file requirements for different sales stages.

Figure-A I-58 BOPADIGITAL Admin - "Edit Document Type" modal allowing adjustments to validation rules, such as making a document mandatory for all services.

190

Figure-A I-59 BOPADIGITAL Admin - "Delete Document Type" confirmation modal ensuring the administrator intends to permanently remove a configuration (e.g., "RUC") from the system.

Figure-A I-60 BOPADIGITAL Admin - "Add New Document Type" form allowing the definition of new mandatory or optional requirements, specifying applicable sales stages and service scope.

191

Figure-A I-61 BOPADIGITAL Admin - "Sales Closings Report" dashboard providing detailed transaction analysis, including total revenue, sales count, and visual breakdowns by service type and geographic zone.

Figure-A I-62 BOPADIGITAL Admin - Sales Report demonstrating filtering capabilities, isolating performance data for a specific advisor (e.g., Roberto Mendoza) over the "Last Semester" period.

192

Figure-A I-63 BOPADIGITAL Admin - "Export Report" functionality showing system feedback (modal alert) confirming the generation of a PDF file containing the current sales data visualization.

193

1. 0.4 Mobile app

194

a) Secure Login Screen: Entry point for advisors offering role-based access (Advisor/Admin) and credential input.

b) Mobile Home Dashboard: Personalized welcome screen displaying "Next Activity" alerts and pending documentation tasks.

Figure-A I-64 BOPACORP Mobile App - Authentication and Main Dashboard views.

195

a) Recent Activity Feed: Timeline view showing completed visits and status updates for assigned clients.

b) Create Activity (Step 1): Interface to log new interactions, selecting activity type (e.g., Quotation Visit) and date.

Figure-A I-65 BOPACORP Mobile App - Activity tracking and creation workflow.

196

a) Create Activity (Step 2): Advanced details form for setting priority levels, adding notes, and quick action shortcuts.

b) My Clients Portfolio: Searchable list of all assigned accounts with filtering options for "New Users" or "Active" clients.

Figure-A I-66 BOPACORP Mobile App - Detailed activity logging and client portfolio navigation.

197

a) Client Management Cards: Quick-action view allowing advisors to edit details or delete client records directly from the list.

b) New Client Registration (Part 1): Form to input essential business information, contact name, and profile photo.

Figure-A I-67 BOPACORP Mobile App - Client administration and registration interface.

198

a) New Client Registration (Part 2): Finalizing the record with contact details (email, phone, address) and assigning a status (e.g., Lucrative Client).

Figure-A I-68 BOPACORP Mobile App - Final step of the new client registration process.

199

a) Client Profile Header: Detailed contact information view featuring quick-action buttons (Call, Email) and address details.

b) Client Business Overview: Display of current subscription plan (Business Gold) and a timeline of recent interactions.

Figure-A I-69 BOPACORP Mobile App - Comprehensive client profile and history view.

200

a) My Activities: Task management list filtered by status (All, Upcoming, Recent) with priority indicators.

b) Client Portfolio: Searchable directory of assigned accounts, providing a quick overview of the advisor’s book of business.

Figure-A I-70 BOPACORP Mobile App - Operational lists for daily task and portfolio management.

201

a) Advisor Profile: User dashboard summarizing key performance statistics (Total Clients, Activities, Year).

b) Profile Settings: Configuration menu for account management, including password changes and app preferences.

Figure-A I-71 BOPACORP Mobile App - User profile and application settings.

202

a) Admin Dashboard: Executive overview showing high-level metrics such as Total Clients, Monthly Revenue, and Active Projects.

b) Administrative Actions: Quick access menu for User Management, Reports, Service Configuration, and Database tools.

Figure-A I-72 BOPACORP Mobile App - Administrative control panel and statistics.

203

a) User Management: Interface to view, edit, or remove system users (Advisors/Admins) and monitor their last access.

b) System Status: Health check monitor displaying operating system status, backup timestamps, and software version.

Figure-A I-73 BOPACORP Mobile App - Advanced system management and user administration.

204

a) New User Registration: Administrative form to onboard new staff, allowing the definition of roles (Advisor/Admin) and initial credentials.

b) Service Management: Mobile catalog administration view permitting real-time updates to service listings, pricing, and active status.

Figure-A I-74 BOPACORP Mobile App - Administrative tools for user onboarding and service catalog maintenance.

205

1. 0.5 BOPACORP Landing Page

Figure-A I-75 BOPACORP Website - Homepage featuring the main value proposition, navigation menu, and quick access to services and company information.

Figure-A I-76 BOPACORP Website - "About Us" section detailing the company’s history, mission, and vision statements to establish corporate identity.

206

Figure-A I-77 BOPACORP Website - complete Service Catalog displaying available corporate plans with filtering options by category, zone, and price.

Figure-A I-78 BOPACORP Website - Service Detail Modal for "Plan Corporativo 100", showing specific costs, coverage zones, and included benefits.

207

Figure-A I-79 BOPACORP Website - Search results view demonstrating active filters (Cloud, Digital Services, National Coverage) applied to the catalog.

Figure-A I-80 BOPACORP Website - "Work with Us" (Careers) page highlighting employee benefits and listing current job openings.

208

Figure-A I-81 BOPACORP Website - Job Application Modal allowing candidates to submit personal details and upload their CV for a specific position.

Figure-A I-82 BOPACORP Website - Success confirmation modal providing feedback to the user that their job application has been successfully sent.

APPENDIX II CLIENT ACCEPTANCE LETTER

1. Signed Approval Document

This appendix includes the official approval letter signed by the stakeholder representative of

BOPACORP S.A., which formally validates the Project Specification Document. The signed

document confirms the stakeholder’s agreement with the documented project scope, including

the risk management artifacts, sprint backlogs, project schedule, UML-based static and

behavioral system models, and the system prototype, as defined during the requirements

elicitation and analysis phases.

210

APPENDIX III REQUIREMENTS SPECIFICATION DOCUMENT

### BOPACORP S.A. Requirements Specification Document

by

Grupo 2 BOPADIGITAL

PROJECT PRESENTED TO ESCUELA SUPERIOR POLITÉCNICA DEL LITORAL

GUAYAQUIL, NOVEMBER 13, 2025

ESCUELA SUPERIOR POLITÉCNICA DEL LITORAL ESPOL

Grupo 2 BOPADIGITAL, 2025

212

This Creative Commons license allows readers to download this work and share it with others as long as the author is credited. The content of this work cannot be modified in any way or used commercially.

### 213

TEAM MEMBERS

THIS PROJECT HAS BEEN DEVELOPED

BY THE FOLLOWING GROUP OF STUDENTS

Shirley Aragon Facultad de Ingenieria en Electricidad y Computación

Nahim Díaz Facultad de Ingenieria en Electricidad y Computación

Salvador Muñoz Facultad de Ingenieria en Electricidad y Computación

Gabriel Tumbaco Facultad de Ingenieria en Electricidad y Computación

Anthony Navarrete Facultad de Ingenieria en Electricidad y Computación

214

TABLE OF CONTENTS

Page

CHAPTER 1 PURPOSE OF THE PROJECT . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1

1. 1 Problem Description . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1

1. 2 Project Description . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1

1. 3 Project Purpose . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2

CHAPTER 2 STAKEHOLDERS. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4

2. 1 Business Client . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4

2. 2 Sales Advisor . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4

2. 3 Immediate Supervisor / Sales Manager . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4

2. 4 Documentation Coordinator . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5

2. 5 Management / Executive Board. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5

2. 6 Sales Advisor Candidate . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5

2. 7 Web Administrator . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5

CHAPTER 3 CONSTRAINTS . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7

3. 1 Solution Constraints . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7

3. 2 Implementation Environment of the Current System . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7

CHAPTER 4 SCOPE OF THE WORK . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8

4. 1 Public Website . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8

4. 1.1 Hierarchical Service Catalog . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8

4. 1.2 Detailed Service Information . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8

4. 1.3 Employment Application Module . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9

4. 2 Internal Application (Web and Mobile) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9

4. 2.1 Negotiation Management . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9

4. 2.2 Negotiation Tracking. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9

4. 2.3 Intelligent Reporting . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9

4. 2.4 Document Management. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10

4. 3 Scope Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10

CHAPTER 5 FUNCTIONAL REQUIREMENTS. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11

5. 1 Public Website . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12

5. 1.1 Service Catalog and Website Module (CAT) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12

5. 1.2 Content Management Module (CMS). . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13

5. 1.3 Employability and Application Module (EMP). . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14

5. 2 Internal Application . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15

5. 2.1 Client Relationship Management Module (CRM) . . . . . . . . . . . . . . . . . . . . . . . . . . . 15

5. 2.2 Offer Matrix Module (MAT) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18

5. 2.3 Supervision and Approvals Module (SUP) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20

5. 2.4 Document Management Module (DOC) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21

215

II

5. 2.5 Reporting Module (REP) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22

5. 2.6 Basic Security Module (SEG) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24

5. 2.7 Notifications Module (NOT) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25

CHAPTER 6 NON-FUNCTIONAL REQUIREMENTS. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26

CHAPTER 7 USER STORIES . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33

7. 1 Service Catalog and Website Module (CAT) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33

7. 2 Content Management Module (CMS) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35

7. 3 Employability and Application Module (EMP) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 37

7. 4 Client Management Module (CRM). . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 39

7. 5 Offer Matrix Module (MAT) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 46

7. 6 Supervision and Approvals Module (SUP) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 48

7. 7 Document Management Module (DOC) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 50

7. 8 Reporting Module (REP) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 54

CHAPTER 8 PROTOTYPE . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 58

8. 1 Link . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 58

CHAPTER 9 EVIDENCES . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 59

9. 1 Requirements Elicitation Technique . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 59

9. 2 Evidence Repository . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 59

CHAPTER 10 INDIVIDUAL CONTRIBUTIONS . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 60

CHAPTER 11 AUTHORSHIP DECLARATION. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 61

APPENDIX I PROTOTYPE . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 62

APPENDIX II CLIENT ACCEPTANCE LETTER . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 74

APPENDIX III SIGNED AUTORSHIP DECLARATION . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 75

216

LIST OF TABLES

Page

Table 5.1 Functional Requirements - Service Catalog and Website (CAT) . . . . . . . . . . . 12

Table 5.2 Functional Requirements - Content Management Module (CMS) . . . . . . . . . 13

Table 5.3 Functional Requirements - Employability and Application Module (EMP) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14

Table 5.4 Functional Requirements - Client Relationship Management Module (CRM) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15

Table 5.5 Functional Requirements - Offer Matrix Module (MAT) . . . . . . . . . . . . . . . . . . . 18

Table 5.6 Functional Requirements - Supervision and Approvals Module (SUP) . . . . 20

Table 5.7 Functional Requirements - Document Management Module (DOC) . . . . . . 21

Table 5.8 Functional Requirements - Reporting Module (REP). . . . . . . . . . . . . . . . . . . . . . 22

Table 5.9 Functional Requirements - Basic Security Module (SEG) . . . . . . . . . . . . . . . . . 24

Table 5.10 Functional Requirements - Notifications Module (NOT) . . . . . . . . . . . . . . . . . . . 25

Table 6.1 Non-Functional Requirements - BOPADIGITAL System . . . . . . . . . . . . . . . . . . 27

Table 10.1 Individual Contributions of the Project . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 60

217

LIST OF FIGURES

Page

Figure 8.1 Prototype of BOPADIGITAL . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 58

Figure 9.1 Meeting with the managers of BOPACORP S.A. . . . . . . . . . . . . . . . . . . . . . . . . . . 59

Figure I-1 Screenshots of BOPADIGITAL mobile app from the perspective of a Sales Advisor.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 63

Figure I-2 Screenshots of BOPADIGITAL mobile app from the perspective of a Sales Advisor.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 64

Figure I-3 Screenshots of BOPADIGITAL mobile app from the perspective of Management.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 65

Figure I-4 Screenshots of BOPADIGITAL CMS website . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 66

Figure I-5 Screenshots of BOPADIGITAL CMS website . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 67

Figure I-6 Website from the perspective of a sales advisor candidate.. . . . . . . . . . . . . . . 68

Figure I-7 Screenshots of BOPADIGITAL CRM website for sales consultant . . . . . . . 69

Figure I-8 Screenshots of BOPADIGITAL CRM website for sales consultant . . . . . . . 70

Figure I-9 Screenshots of BOPADIGITAL CRM form the perspective of Management.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 71

Figure I-10 Screenshots of BOPADIGITAL CRM form the perspective of Management.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 72

Figure I-11 Screenshots of BOPADIGITAL CRM form the perspective of Management.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 73

218

LIST OF ABBREVIATIONS

BOPACORP S.A. Telecommunications company and main client of the project

BOPADIGITAL Digital platform developed for BOPACORP S.A.

B2B Business-to-Business (commercial model between companies)

CMS Content Management System – module for website content administration

CRM Customer Relationship Management – module for managing business clients

and negotiations

DOC Document Management Module

EMP Employability / Application Module

MAT Offer Matrix Module

REP Reporting Module

SUP Supervision and Approvals Module

CAT Catalog and Website Module

SEG Basic Security Module

NOT Notifications Module

GPS Global Positioning System

UI User Interface

UX User Experience

JWT JSON Web Token (authentication mechanism)

TLS Transport Layer Security (encryption protocol for HTTPS)

PDF Portable Document Format

219

VI

KPI Key Performance Indicator

RUC Unique Taxpayer Registry

ID Identifier (unique reference or key)

220

LIST OF SYMBOLS AND UNITS OF MEASUREMENTS

% Percentage (used in performance indicators such as availability or success

rate)

s Seconds (used for system response times, e.g., ≤ 3 s)

MB Megabytes (used for file upload size limits, e.g., 50 MB)

h Hours (used for availability and operational timeframes)

221

CHAPTER 1

PURPOSE OF THE PROJECT

1. 1 Problem Description

BOPACORP is a strategic commercial partner of Movistar, focused on selling telecommunication

services to business clients (B2B). The company’s commercial process relies on a team of sales

executives (advisors) who perform prospecting, field visits, and contract closures.

The current operating model is manual, decentralized, and heavily dependent on tools such

as Excel, Google Drive, and instant messaging (WhatsApp and Email), which generates three

critical bottlenecks directly impacting productivity and profitability:

1. The main bottleneck occurs after a successful sales close. The executive must collect

physical documentation from the client (contract, ID, RUC, etc.) and physically return to

the office to deliver it to the operational area. This travel generates "dead time," a significant

opportunity cost where the comercial advisor could be making another commercial visit.

This delay worsens at month-end, accumulating work for the operations team (coordination)

and delaying service activation.

2. Management and immediate supervisors lack real-time visibility into the sales team’s

activities. Supervision is based on manual communication (asking via WhatsApp or chat)

to find out an executive’s location or the status of a visit.

3. All performance tracking and sales pipeline management are done in Excel spreadsheets.

Immediate supervisors must consolidate this information manually for their weekly "one-

on-one" meetings.

1. 2 Project Description

The BOPADIGITAL project is a comprehensive software solution, composed of an administrative

web application and a mobile application, custom-designed for BOPACORP.

222

2

The system’s main objective is to digitize and centralize the complete B2B (business-to-business)

sales lifecycle. Currently, this process is managed manually using a set of decentralized tools,

which includes:

- Google Drive, for storing and transferring contractual documentation.

- Excel spreadsheets for reporting and tracking advisor performance.

- Direct communication channels (such as WhatsApp or email) for daily supervision and status

reporting.

The proposed solution will replace these manual processes by implementing several interconnected

modules:

1. CRM Module (Web and Mobile): Allows for prospect registration, client portfolio

management, and updating negotiation statuses (e.g., Initial Visit, Negotiation, Closing).

2. Mobile Document Management Module: Facilitates the uploading of contractual documentation

(ID, RUC, appointment, contract) directly from the advisor’s mobile device in the field.

3. Supervision Module: Provides management with a feed of recent activity and tools for

scheduling and tracking visits, improving visibility of field management.

4. Intelligent Reporting Module: Centralizes sales data in an administrative dashboard for

performance evaluation.

1. 3 Project Purpose

The fundamental purpose of BOPADIGITAL is to increase the operational efficiency of the

commercial team and improve managerial visibility for strategic decision-making.

The objectives of the project are:

1. Mobility and Field Productivity Module: Develop an internal web and mobile application

that eliminates “Dead Time” by enabling consultants to upload contractual documentation

(RUC, ID, Contract) in real time from the field, while also providing structured client

management through the registration and updating of prospects with key commercial data

(invoicing, number of lines) and the scheduling of visits.

223

3

2. Content Management and Web Catalog Module (CMS): Design and develop a web product

catalog under a content management scheme to facilitate its administration, allowing

business clients to contact a sales consultant to initiate negotiation.

3. Centralize and Automate Supervision: Replace manual supervision (based on asking

“Where are you?” or “How’s it going?” via chat) with an active system. The project aims

to give management real-time visibility into advisors’ locations, visit statuses, and field

activity validation, reducing the likelihood of false or unverified visits.

4. Enable Data-Driven Decision Making: Transform the current manual report generation

process (in Excel) into an automated dashboard. This will make weekly follow-up meetings

(“one-on-ones”) more efficient and focused on actionable insights, with consolidated key

metrics such as pipeline by stage, billing, closing time, and performance in strategic products.

224

CHAPTER 2

STAKEHOLDERS

2. 1 Business Client

Business clients are external users who will access BOPACORP’s public website to explore the

catalog of products and services offered, including voice, connectivity, digital, satellite tracking,

and cloud security solutions. Their main interest is to find suitable options for their companies,

compare prices and benefits, and contact a sales advisor to start a negotiation. They expect a

clear, reliable, and visually appealing platform that allows them to identify services quickly and

communicate effectively with the company.

2. 2 Sales Advisor

The sales advisor is the key operational user of the internal system, responsible for managing

the entire sales cycle, from client prospecting to post-sale follow-up. They use the web and

mobile application to register clients, plan visits, document negotiations, create offer matrices,

and upload supporting documentation. Their main goal is to have an agile tool that allows them

to work from the client’s office, upload information in real time, and optimize their time without

needing to return to the company’s premises, thereby improving customer service efficiency.

2. 3 Immediate Supervisor / Sales Manager

The immediate supervisor or sales manager is an administrative user who oversees the work

of sales advisors and monitors negotiation progress. Their responsibilities include approving

offer matrices, analyzing performance indicators, and generating sales reports by period or by

advisor. They need a system that provides complete visibility of the commercial flow, facilitates

decision-making, and keeps real-time control over the team’s performance to ensure sales

objectives are met.

225

5

2. 4 Documentation Coordinator

The coordinator is responsible for managing documentation and activating contracted services.

They use the internal application to define mandatory documents, review files uploaded by sales

advisors, and update their approval status. They also coordinate with Telefónica’s platform to

complete the service activation process. Their main objective is to reduce bottlenecks during

closing periods and ensure all documentation is complete and verified on time, thus improving

operational efficiency across departments.

2. 5 Management / Executive Board

The management team represents the company’s executive stakeholders, responsible for making

strategic decisions based on data generated by the system. Their focus is on analyzing

consolidated reports on sales, productivity, and commercial performance through the intelligent

reporting module. They expect the platform to provide reliable metrics, visual dashboards, and

historical comparisons that support data-driven decision-making and the strategic growth of the

organization.

2. 6 Sales Advisor Candidate

Sales advisor candidates are external users interested in joining BOPACORP’s commercial

team. They use the employment section of the website to view available vacancies, complete

online application forms, and upload their resumes in PDF format. They expect a simple,

transparent, and automated process that provides visual and email confirmation once their

application is submitted, enhancing the company’s professional image and facilitating human

resource management.

2. 7 Web Administrator

The web administrator is responsible for maintaining and updating the public content of

BOPACORP’s website. Through the Content Management System (CMS) module, they can edit

226

6

text, images, links, service categories, and publish new products without requiring advanced

technical knowledge. Their goal is to keep the website’s information accurate and attractive,

ensuring consistency, branding alignment, and clear communication with potential clients.

227

CHAPTER 3

CONSTRAINTS

3. 1 Solution Constraints

The development of the BOPADIGITAL platform will be carried out using React for the frontend

interface, Node.js with Express for the backend services, and PostgreSQL as the primary

relational database. These technologies have been selected due to their proven scalability, active

community support, and compatibility with modern web architectures. The use of open-source

tools minimizes licensing costs and ensures maintainability by the development team after

project delivery. The solution must also use Docker containers for deployment to guarantee

consistency across environments. Therefore, the final product must be fully operational using

these technologies and deployed within a Dockerized environment, without depending on

proprietary or paid software frameworks.

3. 2 Implementation Environment of the Current System

The platform will be implemented in a cloud-based environment running on Linux servers,

using Docker for containerization and NGINX as the web server. Development and testing will

be performed in a controlled cloud environment before being deployed to production. This

approach ensures scalability, security, and easy maintenance. The system must be compatible

with both web and mobile devices, ensuring that authorized users can access it from any location

with an internet connection.

228

CHAPTER 4

SCOPE OF THE WORK

The BOPADIGITAL project aims to design and develop an integrated digital platform for

BOPACORP S.A., a company specialized in telecommunications products and services. The

system will consist of two main components: a public website and an internal web and mobile

application. Together, these components will optimize the company’s commercial processes,

from client acquisition to post-sale management.

4. 1 Public Website

The website is designed to increase BOPACORP’s online visibility and facilitate interaction with

potential business clients. It will provide detailed and up-to-date information on all products

and services, allowing external users to explore available options and initiate contact with the

sales team. In addition, the site will include a recruitment section to manage job applications for

new sales advisors.

4. 1.1 Hierarchical Service Catalog

The platform will feature a hierarchical catalog that organizes services into categories such as

Voice, Connectivity, and Digital Services. Each category will include subcategories that enable

structured navigation and efficient search of service information.

4. 1.2 Detailed Service Information

Every service entry will contain comprehensive details, including costs, benefits, and additional

conditions. This ensures transparency and allows potential clients to make informed decisions

before initiating a commercial contact.

229

9

4. 1.3 Employment Application Module

The website will provide a dedicated employment module allowing prospective sales advisors

to view available positions, fill out application forms, and upload their resumes (CVs) in PDF

format. This feature will streamline recruitment processes and centralize applicant data.

4. 2 Internal Application (Web and Mobile)

The internal application is intended to support the complete sales negotiation process, allowing

the commercial team to manage prospects, monitor negotiations, and maintain updated client

information. It will also optimize document handling and provide analytical tools to evaluate

commercial performance.

4. 2.1 Negotiation Management

Sales advisors will register potential clients, track negotiation stages, and record interactions in

real time. The application will allow continuous monitoring of each business opportunity until

closure.

4. 2.2 Negotiation Tracking

Supervisors will be able to visualize the current status of all negotiations, including client details,

deal stages, approval matrices, and estimated closing times. This enables greater oversight of

the commercial process and advisor productivity.

4. 2.3 Intelligent Reporting

The system will include a reporting module that generates metrics and performance analyses,

such as sales by period, advisor performance, and clients not yet converted. These reports will

serve as a decision-making tool for management and supervisors.

230

10

4. 2.4 Document Management

The internal system will incorporate a document management module allowing advisors to

upload required documentation for each negotiation. Coordinators will have access to review,

approve, or reject files, ensuring all necessary information is validated for service activation.

4. 3 Scope Summary

Overall, the system will enable BOPACORP S.A. to:

- Present a structured, user-friendly catalog of telecommunications services.

- Streamline and digitize the commercial process from client prospecting to service activation.

- Provide real-time visibility of sales operations for supervisors and management.

- Centralize documentation and standardize approval workflows.

- Facilitate recruitment of new sales advisors through the corporate website.

- Ensure scalability for the future integration of new services and strategic partners.

231

CHAPTER 5

FUNCTIONAL REQUIREMENTS

This section defines the functional requirements of the BOPADIGITAL system, which describe

the specific behaviors, actions, and processes that the software must perform to meet the needs

of its stakeholders. Each requirement has been derived from the system’s modules, stakeholder

interviews, and the client’s business processes.

The functional requirements are organized by modules that represent the main subsystems of

BOPADIGITAL, including the public website and the internal application (web and mobile).

This structure ensures clarity, traceability, and alignment with the project scope.

232

12

5. 1 Public Website

5. 1.1 Service Catalog and Website Module (CAT)

ID Version Description User / Role Priority

RF-CAT-001 1.0 The system shall allow the business client

to view a catalog of products and services

organized into categories such as Voice,

Connectivity, and Digital Services.

Business

Client

High

RF-CAT-002 1.0 The system shall allow the business client to

view costs, benefits, and usage conditions

for each item in the catalog.

Business

Client

High

RF-CAT-003 1.0 The system shall allow the business client

to filter catalog items by category, coverage,

and price.

Business

Client

Medium

RF-CAT-004 1.0 The system shall allow the business client

to contact a sales advisor to initiate

a negotiation regarding selected catalog

items.

Business

Client

High

RF-CAT-005 1.0 The system shall allow the business client to

view information about BOPACORP S.A.’s

history, mission, vision, and values.

Business

Client

High

Table 5.1 Functional Requirements - Service Catalog and Website (CAT)

233

13

5. 1.2 Content Management Module (CMS)

ID Version Description User / Role Priority

RF-CMS-001 1.0 The system shall allow the web

administrator to access the content

management panel using credential-based

authentication (username and password).

Web

Administrator

High

RF-CMS-002 1.0 The system shall allow the web

administrator to edit texts, images, and

links of the public website.

Web

Administrator

High

RF-CMS-003 1.0 The system shall allow the web

administrator to create new products and

services within the catalog.

Web

Administrator

High

RF-CMS-004 1.0 The system shall allow the web

administrator to update the information

of existing products and services in the

catalog.

Web

Administrator

High

RF-CMS-005 1.0 The system shall allow the web

administrator to delete products and

services from the catalog.

Web

Administrator

High

Table 5.2 Functional Requirements - Content Management Module (CMS)

234

14

5. 1.3 Employability and Application Module (EMP)

ID Version Description User / Role Priority

RF-EMP-001 1.0 The system shall allow the sales advisor

candidate to view available vacancies,

displaying the position title, description,

requirements, and publication date.

Sales Advisor

Candidate

High

RF-EMP-002 1.0 The system shall allow the sales advisor

candidate to complete an application form

by entering personal details and contact

information.

Sales Advisor

Candidate

High

RF-EMP-003 1.0 The system shall allow the sales advisor

candidate to upload their resume (CV) in

PDF format as a mandatory part of the

application process.

Sales Advisor

Candidate

High

RF-EMP-004 1.0 The system shall validate that all required

fields in the application form are correctly

filled before allowing submission.

Sales Advisor

Candidate

High

RF-EMP-005 1.0 The system shall notify the sales advisor

candidate visually and via email once

their application has been successfully

submitted.

Sales Advisor

Candidate

High

RF-EMP-006 1.0 The system shall allow the sales advisor

candidate to be informed of the result of

their application.

Sales Advisor

Candidate

Medium

Table 5.3 Functional Requirements - Employability and Application Module (EMP)

235

15

5. 2 Internal Application

5. 2.1 Client Relationship Management Module (CRM)

Table 5.4 Functional Requirements - Client Relationship Management Module (CRM)

ID Version Description User / Role Priority

RF-CRM-001 1.0 The system shall allow the sales advisor to

fill out a client registration form including

the company’s RUC (tax ID), business

name, number of active services, and

current monthly billing.

Sales Advisor High

RF-CRM-002 1.0 The system shall allow the sales advisor to

update the information of assigned business

clients.

Sales Advisor High

RF-CRM-003 1.0 The system shall allow the sales advisor

to filter and search business clients by

negotiation stage or visit date.

Sales Advisor High

RF-CRM-004 1.0 The system shall allow the sales advisor

to schedule on-site visits with assigned

business clients.

Sales Advisor High

RF-CRM-005 1.0 The system shall allow the sales advisor

to register a new client visit by entering

date, time, observations, and GPS location

automatically obtained from their mobile

device.

Sales Advisor High

Continued on next page

236

16

Table 5.4 (continued) – Client Relationship Management Module (CRM)

ID Version Description User / Role Priority

RF-CRM-006 1.0 The system shall allow the immediate

supervisor to view the GPS location

registered by the sales advisor during each

visit to verify its validity.

Immediate

Supervisor

High

RF-CRM-007 1.0 The system shall allow the sales advisor

to view a history of visits made to their

assigned business clients.

Sales Advisor High

RF-CRM-008 1.0 The system shall allow the sales advisor

to update the negotiation status with an

assigned business client.

Sales Advisor High

RF-CRM-009 1.0 The system shall allow the immediate

supervisor to register new business clients,

including RUC, business name, number of

active services, and current monthly billing.

Immediate

Supervisor

High

RF-CRM-010 1.0 The system shall allow the immediate

supervisor to update information about

business clients.

Immediate

Supervisor

High

RF-CRM-011 1.0 The system shall allow the immediate

supervisor to deactivate business clients

when necessary.

Immediate

Supervisor

High

RF-CRM-012 1.0 The system shall allow the immediate

supervisor to assign business clients to sales

advisors to initiate negotiations.

Immediate

Supervisor

High

Continued on next page

237

17

Table 5.4 (continued) – Client Relationship Management Module (CRM)

ID Version Description User / Role Priority

RF-CRM-013 1.0 The system shall allow the immediate

supervisor to view the list of business

clients assigned to each sales advisor.

Immediate

Supervisor

High

RF-CRM-014 1.0 The system shall allow the immediate

supervisor to remove business clients from

a sales advisor’s portfolio.

Immediate

Supervisor

High

RF-CRM-015 1.0 The system shall allow the immediate

supervisor to view the recent activity of

all company sales advisors.

Immediate

Supervisor

High

RF-CRM-016 1.0 The system shall allow management to

view, for each sales advisor, the number

of business clients contacted, visited, and

successfully closed.

Management High

RF-CRM-017 1.0 The system shall allow management to view

the total billed amount per advisor, along

with the total number of services sold and

the average revenue per service.

Management High

RF-CRM-018 1.0 The system shall allow management to view

the count and total value of terminals and

equipment sold by each advisor.

Management High

RF-CRM-019 1.0 The system shall allow management to view,

for each advisor, the number of business

clients in each sales funnel stage.

Management High

Continued on next page

238

18

Table 5.4 (continued) – Client Relationship Management Module (CRM)

ID Version Description User / Role Priority

RF-CRM-020 1.0 The system shall allow the immediate

supervisor to filter and search business

clients by negotiation stage, visit date, or

assigned advisor.

Immediate

Supervisor

High

RF-CRM-021 1.0 The system shall restrict access so that sales

advisors can only view and modify data of

business clients assigned to them.

Sales Advisor High

RF-CRM-022 1.0 The system shall allow the immediate

supervisor to consult a detailed history of

modifications made by each sales advisor

to their clients.

Immediate

Supervisor

High

5. 2.2 Offer Matrix Module (MAT)

Table 5.5 Functional Requirements - Offer Matrix Module (MAT)

ID Version Description User / Role Priority

RF-MAT-001 1.0 The system shall allow the sales advisor to

create a new offer matrix associated with a

business client and an ongoing negotiation.

Sales Advisor High

RF-MAT-002 1.0 The system shall allow the sales advisor to

enter the services and products proposed to

the client, specifying quantities, unit prices,

totals, and observations as part of the offer

matrix.

Sales Advisor High

Continued on next page

239

19

Table 5.5 (continued) – Offer Matrix Module (MAT)

ID Version Description User / Role Priority

RF-MAT-003 1.0 The system shall automatically calculate

the applicable subsidy range based on

client billing and the number of proposed

services, displaying the total estimated

benefit amount.

Sales Advisor High

RF-MAT-004 1.0 The system shall allow the sales advisor

to attach quotations or supporting files in

PDF, Excel, JPG, or PNG formats up to 50

MB to the offer matrix.

Sales Advisor High

RF-MAT-005 1.0 The system shall allow the sales advisor

to save offer matrices as drafts to edit

them before sending them to the immediate

supervisor for approval.

Sales Advisor High

RF-MAT-006 1.0 The system shall allow the sales advisor

to send the offer matrix to the immediate

supervisor for approval, changing its status

to “Pending Approval.”

Sales Advisor High

RF-MAT-007 1.0 The system shall allow the sales

advisor to consult the history of their

matrices, including creation date, status,

observations, and total subsidy amount.

Sales Advisor High

240

20

5. 2.3 Supervision and Approvals Module (SUP)

ID Version Description User / Role Priority

RF-SUP-001 1.0 The system shall allow the immediate

supervisor to view the list of offer matrices

pending approval.

Immediate

Supervisor

High

RF-SUP-002 1.0 The system shall allow the immediate

supervisor to review commercial indicators

such as billing, number of services, and

the calculated subsidy range for each offer

matrix.

Immediate

Supervisor

High

RF-SUP-003 1.0 The system shall allow the immediate

supervisor to approve or reject offer

matrices, recording a mandatory reason

in case of rejection.

Immediate

Supervisor

High

RF-SUP-004 1.0 The system shall allow the immediate

supervisor to view a history of offer

matrices that have been approved or

rejected.

Immediate

Supervisor

High

RF-SUP-005 1.0 The system shall allow the sales advisor to

receive an internal notification and an email

with the result of the approval or rejection

of their matrix.

Sales Advisor High

RF-SUP-006 1.0 The system shall allow the immediate

supervisor to filter matrices by advisor,

date, approval status, or subsidy range to

facilitate their review.

Immediate

Supervisor

High

Table 5.6 Functional Requirements - Supervision and Approvals Module (SUP)

241

21

5. 2.4 Document Management Module (DOC)

Table 5.7 Functional Requirements - Document Management Module (DOC)

ID Version Description User / Role Priority

RF-DOC-001 1.0 The system shall allow the sales advisor

to attach documents related to negotiations

with assigned business clients.

Sales Advisor High

RF-DOC-002 1.0 The system shall allow the sales advisor to

upload files up to 50 MB in PDF, JPG, or

PNG formats.

Sales Advisor High

RF-DOC-003 1.0 The system shall require the sales advisor to

label each uploaded document with its type

(e.g., “Provisional RUC,” “Initial Proposal,”

“Visit Report,” “Final Contract”).

Sales Advisor High

RF-DOC-004 1.0 The system shall allow the coordinator to

define mandatory or optional documents

depending on the type of service or

negotiation.

Coordinator High

RF-DOC-005 1.0 The system shall allow the sales advisor to

check the documentation status during a

negotiation, displaying which files have

been reviewed, approved, or are still

pending.

Sales Advisor High

RF-DOC-006 1.0 The system shall allow the coordinator

to review documents uploaded by each

sales advisor related to negotiations with

business clients.

Coordinator Medium

Continued on next page

242

22

Table 5.7 (continued) – Document Management Module (DOC)

ID Version Description User / Role Priority

RF-DOC-007 1.0 The system shall allow the coordinator to

download documents individually or in

bulk that are associated with a negotiation

for review.

Coordinator Medium

RF-DOC-008 1.0 The system shall allow the sales advisor

to receive internal and email notifications

when their documents have been reviewed,

approved, or rejected by the coordinator.

Sales Advisor Medium

RF-DOC-009 1.0 The system shall allow the coordinator to

view a list of sales advisors with pending

document uploads or reviews.

Coordinator Medium

5. 2.5 Reporting Module (REP)

Table 5.8 Functional Requirements - Reporting Module (REP)

ID Version Description User / Role Priority

RF-REP-001 1.0 The system shall allow the manager to

generate commercial performance reports

by advisor, month, or period to evaluate

team productivity.

Manager High

RF-REP-002 1.0 The system shall allow the immediate

supervisor to generate sales and closure

reports for the sales advisors under their

supervision, filtered by date, service type,

or zone.

Immediate

Supervisor

High

Continued on next page

243

23

Table 5.8 (continued) – Reporting Module (REP)

ID Version Description User / Role Priority

RF-REP-003 1.0 The system shall allow the manager to view

key metrics such as sales, closures, visits,

and average negotiation time to assess

overall performance.

Manager High

RF-REP-004 1.0 The system shall allow the immediate

supervisor to view operational metrics of

sales advisors, including sales, closures,

and visits made during a specific period.

Immediate

Supervisor

High

RF-REP-005 1.0 The system shall allow the immediate

supervisor to compare the performance of

their sales advisors against the objectives

defined by management.

Immediate

Supervisor

Medium

RF-REP-006 1.0 The system shall allow the manager to

export generated reports in PDF or Excel

format for analysis or presentation.

Manager Medium

RF-REP-007 1.0 The system shall allow the immediate

supervisor to export generated reports in

PDF or Excel format for review and follow-

up of commercial activities.

Immediate

Supervisor

Medium

RF-REP-008 1.0 The system shall allow the manager to

visualize consolidated information through

bar charts, line graphs, or KPI indicators

that facilitate interpretation of overall

results.

Manager Medium

Continued on next page

244

24

Table 5.8 (continued) – Reporting Module (REP)

ID Version Description User / Role Priority

RF-REP-009 1.0 The system shall restrict access to reports

according to user roles so that each user

only views the information corresponding

to their access level.

System High

RF-REP-010 1.0 The system shall allow the sales

advisor to view their own commercial

performance, including the number of

clients contacted, active negotiations,

closures, and accumulated billing.

Sales Advisor High

5. 2.6 Basic Security Module (SEG)

ID Version Description User / Role Priority

RF-SEG-001 1.0 The system shall require authentication

using a valid username and password to

allow access to the internal application.

System High

RF-SEG-002 1.0 The system shall assign permissions

and restrict functionalities according to

the user’s role (Manager, Immediate

Supervisor, Sales Advisor, Coordinator,

Web Administrator).

System High

RF-SEG-003 1.0 The system shall ensure that users with the

Manager role inherit the access privileges

of the Immediate Supervisor role.

System High

Table 5.9 Functional Requirements - Basic Security Module (SEG)

245

25

5. 2.7 Notifications Module (NOT)

ID Version Description User / Role Priority

RF-NOT-001 1.0 The system shall send internal and email

notifications to users when relevant events

occur, such as approvals, rejections, or

document reviews.

System High

RF-NOT-002 1.0 The system shall allow each user to view a

history of received notifications within the

application.

System High

Table 5.10 Functional Requirements - Notifications Module (NOT)

246

CHAPTER 6

NON-FUNCTIONAL REQUIREMENTS

This section specifies the non-functional requirements of the BOPADIGITAL system, which

define the quality attributes, constraints, and performance characteristics that the software must

meet. Unlike functional requirements, these requirements do not describe specific system

behaviors but rather establish the standards and conditions under which the system operates

effectively.

The non-functional requirements ensure that the BOPADIGITAL platform is reliable, secure,

efficient, and user-friendly. They address key aspects such as usability, performance, scalability,

maintainability, availability, security, and compliance with organizational and technological

constraints.

These requirements apply to both components of the system, the public website and the internal

application (web and mobile), ensuring a consistent user experience, operational stability, and

compliance with industry best practices. Each non-functional requirement contributes to the

overall quality and sustainability of the system throughout its lifecycle.

247

27

Table 6.1 Non-Functional Requirements - BOPADIGITAL System

ID Version Description Validation

Criterion

Priority

RNF-001 1.0 The system shall guarantee a response

time below 3 seconds for any user action

under a load of up to 50 concurrent

users. (Category: Product – Efficiency

– Performance)

Performance

and stress

testing with

JMeter or

equivalent

shows ≤ 3s

response time

with 50 users.

High

RNF-002 1.0 The platform shall ensure at least 99%

monthly availability during business hours

(08h00–20h00). (Category: Product –

Dependability – Availability)

Server logs

and uptime

reports

confirm

≥ 99%

availability.

High

RNF-003 1.0 The system shall support scaling from 7 to

25 concurrent advisors without affecting

response time. (Category: Product –

Efficiency – Performance)

Load test

results

confirm

stability

under 25

simultaneous

users.

Medium

Continued on next page

248

28

Table 6.1 (continued) – Non-Functional Requirements

ID Version Description Validation

Criterion

Priority

RNF-004 1.0 User passwords shall be hashed using

bcrypt with random salt and at least 12

characters. (Category: Product – Security)

Code audit

confirms

bcrypt usage

and required

length.

High

RNF-005 1.0 All communication between client and

server shall use HTTPS with TLS 1.3

encryption. (Category: Product – Security)

SSL

certificate

and server

configuration

inspection.

High

RNF-006 1.0 The mobile app shall work correctly on

Android 10–16 and iOS 13–16.1; the web

version shall be compatible with Chrome,

Firefox, and Edge. (Category: Product –

Usability)

Cross-device

and cross-

browser

compatibility

tests.

High

RNF-007 1.0 The interface shall remain responsive from

360 px to 1440 px width and meet WCAG

2. 1 AA accessibility. (Category: Product –

Usability)

Visual

inspection

and

accessibility

validation.

High

RNF-008 1.0 The system shall log all critical events

(logins, uploads, approvals, rejections) with

timestamp and user. (Category: Product –

Security)

Audit log

verification.

High

Continued on next page

249

29

Table 6.1 (continued) – Non-Functional Requirements

ID Version Description Validation

Criterion

Priority

RNF-009 1.0 Uploaded files shall be validated by

extension (PDF, JPG, PNG, XLSX) and

limited to 50 MB. (Category: Product –

Efficiency – Space)

Upload and

validation test

results.

High

RNF-010 1.0 The system shall perform daily automated

database backups for disaster recovery.

(Category: Organizational – Operational)

Backup

and restore

verification.

Medium

RNF-011 1.0 The source code shall comply with OWASP

Top 10 security standards. (Category:

Organizational – Development)

Static code

analysis

and linting

validation.

High

RNF-012 1.0 The system shall follow an MVC client-

server architecture with logical separation

of layers. (Category: Organizational –

Development)

Design

and folder

structure

review.

Medium

RNF-013 1.0 User data shall comply with Ecuador’s

Personal Data Protection Law (2021).

(Category: External – Legislative)

Legal audit

and policy

review.

High

RNF-014 1.0 Uploaded documents shall be encrypted

with AES-256 both in transit and at rest.

(Category: Product – Security)

Hosting

configuration

and

encryption

validation.

High

Continued on next page

250

30

Table 6.1 (continued) – Non-Functional Requirements

ID Version Description Validation

Criterion

Priority

RNF-015 1.0 Error messages shall be in Spanish, identify

the failing module, and hide technical

details. (Category: Product – Usability)

Interface

inspection

and error

testing.

Medium

RNF-016 1.0 The system shall ensure data consistency

during concurrent writes, avoiding race

conditions. (Category: Product –

Dependability – Reliability)

Concurrent

operation

testing

confirms

integrity.

High

RNF-017 1.0 Critical operations (approvals, activations,

uploads) shall be recorded in an audit

log with user, action, and timestamp.

(Category: Product – Security)

Database

traceability

verification.

High

RNF-018 1.0 Forms shall validate input on client and

server sides with clear feedback and prevent

duplicates. (Category: Product – Usability)

Validation

tests with

incorrect

inputs.

High

RNF-019 1.0 The application shall run continuously for

at least 8 hours without restart. (Category:

Product – Dependability – Availability)

Endurance

testing

demonstrates

≥8 h stability.

High

Continued on next page

251

31

Table 6.1 (continued) – Non-Functional Requirements

ID Version Description Validation

Criterion

Priority

RNF-020 1.0 All components shall include technical

documentation and comments in standard

format. (Category: Organizational –

Development)

Code and

documentation

review.

Medium

RNF-021 1.0 Unit tests shall cover at least 80% of

critical code. (Category: Organizational –

Development)

Test coverage

report review.

Medium

RNF-022 1.0 System updates shall not exceed 15 minutes

of downtime. (Category: Organizational –

Operational)

Controlled

deployment

and downtime

logging.

Medium

RNF-023 1.0 Personal data shall be anonymized in testing

and development environments. (Category:

External – Legislative)

Database

audit ensures

anonymization.

High

RNF-024 1.0 Sessions shall expire after 15 minutes

of inactivity, requiring reauthentication.

(Category: Product – Security)

Inactivity

test confirms

session

timeout.

High

RNF-025 1.0 The system shall restore databases from

backups without interrupting ongoing

operations. (Category: Product –

Dependability)

Recovery

testing

with data

validation.

Medium

Continued on next page

252

32

Table 6.1 (continued) – Non-Functional Requirements

ID Version Description Validation

Criterion

Priority

RNF-026 1.0 Only authenticated users may access API

endpoints through JWT tokens with 15-

minute expiration. (Category: Product –

Security)

Token

authentication

and

expiration

tests.

High

253

CHAPTER 7

USER STORIES

This section presents the user stories defined for the BOPADIGITAL system. Each story

describes, in concise and user-centered terms, the specific goals, motivations, and expected

outcomes of the main actors interacting with the system. These user stories were derived from

the functional requirements, stakeholder interviews, and the analysis of the company’s business

processes.

The user stories are organized by modules that correspond to the main subsystems of

BOPADIGITAL, ensuring consistency with the system architecture and requirements traceability.

Each module groups the stories related to a particular functional area, covering both the public

website and the internal application (web and mobile).

This modular organization allows a clear understanding of the system from the user’s perspective

and facilitates the transition to subsequent stages of design, development, and testing.

7. 1 Service Catalog and Website Module (CAT)

HU-CAT-001

Related Requirement: RF-CAT-001

Actor: Business Client

User Story: As a business client, I want to explore a catalog of products and services organized

by categories such as Voice, Connectivity, and Digital Services, so that I can easily find the

solutions offered by BOPACORP.

Acceptance Criteria:

- The catalog displays the main categories and available subcategories.

- The user can navigate between categories without errors.

- Each category loads its list of services in less than 3 seconds.

254

34

HU-CAT-002

Related Requirement: RF-CAT-002

Actor: Business Client

User Story: As a business client, I want to view the costs, benefits, and usage conditions of

each service, so I can compare options and choose the one that best suits my company.

Acceptance Criteria:

- Each catalog service displays its cost, benefits, and conditions.

- Information is clearly visible on the website.

- Services without complete information are not allowed.

HU-CAT-003

Related Requirement: RF-CAT-003

Actor: Business Client

User Story: As a business client, I want to filter services by category, coverage, and price to

quickly find the options that meet my needs.

Acceptance Criteria:

- Results update dynamically according to the selected filters.

- Filters can be combined simultaneously.

HU-CAT-004

Related Requirement: RF-CAT-004

Actor: Business Client

User Story: As a business client, I want to contact a sales advisor directly from the catalog to

request more information or start a negotiation.

Acceptance Criteria:

- The contact function is available for each listed service.

- The system processes the contact request successfully.

- The user receives confirmation of their request.

255

35

HU-CAT-005

Related Requirement: RF-CAT-005

Actor: Business Client

User Story: As a business client, I want to learn about BOPACORP’s history, mission, vision,

and values to better understand the company’s philosophy and reliability.

Acceptance Criteria:

- A “About Us” section is accessible from the main menu.

- History, mission, vision, and values are displayed correctly.

- Content is viewable on both desktop and mobile.

7. 2 Content Management Module (CMS)

HU-CMS-001

Related Requirement: RF-CMS-001

Actor: Web Administrator

User Story: As a web administrator, I want to access the content management panel using

credentials (username and password), so that I can control editing operations on the website.

Acceptance Criteria:

- The system requests valid credentials before granting access to the panel.

- Only users with the Web Administrator role can log in.

- Unauthorized access attempts display an error message.

HU-CMS-002

Related Requirement: RF-CMS-002

Actor: Web Administrator

User Story: As a web administrator, I want to modify texts, images, and links of the published

content to keep the website’s information accurate and up to date.

Acceptance Criteria:

- All modifications are saved and made available for publication.

- The system validates file types and sizes before accepting the modification.

256

36

HU-CMS-003

Related Requirement: RF-CMS-003

Actor: Web Administrator

User Story: As a web administrator, I want to register new products and services in the catalog

to expand the range of offerings available to business clients.

Acceptance Criteria:

- Mandatory fields include name, description, category, and price.

- The entered data are correctly stored and available for review.

HU-CMS-004

Related Requirement: RF-CMS-004

Actor: Web Administrator

User Story: As a web administrator, I want to update existing product or service information in

the catalog to reflect changes in prices, benefits, or conditions.

Acceptance Criteria:

- Every update is recorded with the date and responsible user.

- The system preserves data integrity after each modification.

HU-CMS-005

Related Requirement: RF-CMS-005

Actor: Web Administrator

User Story: As a web administrator, I want to delete outdated products or services from the

catalog to ensure that only current offers are visible and avoid confusion for users.

Acceptance Criteria:

- The system must request explicit confirmation from the administrator before permanent

deletion.

- Once confirmed, the deleted service must no longer appear in the public catalog (verified by

a Business Client).

257

37

- The deleted service must also be removed from the active services list in the Content

Management Module (CMS).

7. 3 Employability and Application Module (EMP)

HU-EMP-001

Related Requirement: RF-EMP-001

Actor: Sales Advisor Candidate

User Story: As a sales advisor candidate, I want to view the available job vacancies with their

descriptions and requirements so that I can identify opportunities that fit my professional profile.

Acceptance Criteria:

- The system displays active vacancies with complete information: position title, requirements,

description, and publication date.

- Only valid (non-expired) vacancies are shown.

- The candidate can access the details of each vacancy without authentication.

HU-EMP-002

Related Requirement: RF-EMP-002

Actor: Sales Advisor Candidate

User Story: As a sales advisor candidate, I want to enter my personal and contact information

in an application form so that I can formally apply to an open vacancy.

Acceptance Criteria:

- The form requests defined mandatory fields (name, ID, email, phone, etc.).

- Entered data are stored correctly in the system.

- The application is associated with a specific vacancy.

HU-EMP-003

Related Requirement: RF-EMP-003

Actor: Sales Advisor Candidate

User Story: As a sales advisor candidate, I want to upload my resume (CV) in PDF format so

258

38

that my professional information is included in the application process.

Acceptance Criteria:

- The system accepts PDF files only.

- The file size complies with the defined maximum limit.

- The uploaded CV is stored together with the corresponding application.

HU-EMP-004

Related Requirement: RF-EMP-004

Actor: Sales Advisor Candidate

User Story: As a sales advisor candidate, I want the system to validate that all required fields

are complete before submission so that my application is processed correctly.

Acceptance Criteria:

- The application cannot be submitted if any required fields are missing.

- The system displays validation messages indicating incomplete fields.

- Submission is allowed only when all validations pass.

HU-EMP-005

Related Requirement: RF-EMP-005

Actor: Sales Advisor Candidate

User Story: As a sales advisor candidate, I want to receive visual and email confirmation when

my application is submitted so that I have proof that the process was completed successfully.

Acceptance Criteria:

- Upon submission, the system records the application successfully.

- The candidate receives an in-app notification and a confirmation email.

- The submission date and time are recorded.

HU-EMP-006

Related Requirement: RF-EMP-006

Actor: Sales Advisor Candidate

259

39

User Story: As a sales advisor candidate, I want to receive the result of my application by email

so that I know whether I was accepted or rejected.

Acceptance Criteria:

- The applicant is notified of the application result via email.

7. 4 Client Management Module (CRM)

HU-CRM-001

Related Requirement: RF-CRM-001

Actor: Sales Advisor

User Story: As a sales advisor, I want to register new business clients with their RUC, name,

number of services, and monthly billing, so that I can start tracking their negotiations.

Acceptance Criteria:

- The system requires mandatory fields (RUC, name, services, billing).

- The information is stored correctly.

- Created records are associated with the responsible advisor.

HU-CRM-002

Related Requirement: RF-CRM-002

Actor: Sales Advisor

User Story: As a sales advisor, I want to update the data of my assigned clients to keep accurate

information during the negotiation process.

Acceptance Criteria:

- The system allows modifying only clients assigned to the advisor.

- After saving, the updated information persists and is visible to the Sales Advisor, Immediate

Supervisor, and Management Staff.

HU-CRM-003

Related Requirement: RF-CRM-003

Actor: Sales Advisor

260

40

User Story: As a sales advisor, I want to search and filter my clients by negotiation stage or

visit date so that I can prioritize my commercial follow-up.

Acceptance Criteria:

- The results correspond only to the advisor’s clients.

- Filters can be combined.

HU-CRM-004

Related Requirement: RF-CRM-004

Actor: Sales Advisor

User Story: As a sales advisor, I want to plan on-site visits to my assigned clients to organize

my schedule and maintain continuity in the sales process.

Acceptance Criteria:

- The advisor can register the date, time, and client for each planned visit.

- Visits are stored for later consultation.

HU-CRM-005

Related Requirement: RF-CRM-005

Actor: Immediate Supervisor

User Story: As an immediate supervisor, I want to view the location recorded by advisors

during each visit to verify the validity of reported activities.

Acceptance Criteria:

- The supervisor can view the location of past visits.

- The information includes coordinates and client details.

HU-CRM-006

Related Requirement: RF-CRM-006

Actor: Sales Advisor

User Story: As a sales advisor, I want to consult the history of visits made to analyze my client

261

41

follow-up over time.

Acceptance Criteria:

- The history lists all visits made by the advisor.

- Each record includes date, time, observations, and client.

- The information can be sorted chronologically.

HU-CRM-007

Related Requirement: RF-CRM-007

Actor: Sales Advisor

User Story: As a sales advisor, I want to update the negotiation status of my clients to reflect

progress in the commercial process.

Acceptance Criteria:

- The system allows selecting valid stages (prospecting, negotiation, closing, post-sale).

- Each change is recorded with date and user.

- Only the responsible advisor can modify the status.

HU-CRM-008

Related Requirement: RF-CRM-008

Actor: Immediate Supervisor

User Story: As an immediate supervisor, I want to register new business clients to include them

in the system and assign them to available advisors.

Acceptance Criteria:

- The form includes RUC, name, services, and billing fields.

- Registered clients remain unassigned initially.

- Only users with the Immediate Supervisor role can perform this action.

HU-CRM-009

Related Requirement: RF-CRM-009

Actor: Immediate Supervisor

262

42

User Story: As an immediate supervisor, I want to update information about business clients to

correct or maintain company records up to date.

Acceptance Criteria:

- The supervisor can edit any business client record.

- Each update is logged with date and user.

- Updated data are reflected in real time.

HU-CRM-010

Related Requirement: RF-CRM-010

Actor: Immediate Supervisor

User Story: As an immediate supervisor, I want to deactivate business clients to prevent the use

of inactive or outdated records.

Acceptance Criteria:

- The system allows setting a client status to “Inactive.”

- Inactive clients do not appear in active searches.

- The supervisor can revert the status if necessary.

HU-CRM-011

Related Requirement: RF-CRM-011

Actor: Immediate Supervisor

User Story: As an immediate supervisor, I want to assign business clients to sales advisors to

distribute the workload efficiently.

Acceptance Criteria:

- The supervisor selects the advisor and client for assignment.

- Assigned clients are immediately linked to the advisor.

- The system prevents duplicate assignments.

HU-CRM-012

Related Requirement: RF-CRM-012

263

43

Actor: Immediate Supervisor

User Story: As an immediate supervisor, I want to view the list of clients assigned to each

advisor to monitor each team member’s portfolio.

Acceptance Criteria:

- The list displays clients and their negotiation status.

- It can be filtered by advisor.

- The data update in real time.

HU-CRM-013

Related Requirement: RF-CRM-013

Actor: Immediate Supervisor

User Story: As an immediate supervisor, I want to reassign or remove clients from a sales

advisor to redistribute them when necessary.

Acceptance Criteria:

- The supervisor can remove the link between advisor and client.

- All changes are recorded with date and reason.

HU-CRM-014

Related Requirement: RF-CRM-014

Actor: Immediate Supervisor

User Story: As an immediate supervisor, I want to review recent activity from sales advisors to

evaluate their compliance with visits and record keeping.

Acceptance Criteria:

- The system displays the latest activity from each advisor.

- Each record includes action type, date, and affected client.

HU-CRM-015

Related Requirement: RF-CRM-015

Actor: Management

264

44

User Story: As management, I want to view contact, visit, and closure indicators per advisor to

evaluate team performance.

Acceptance Criteria:

- The system displays the number of clients contacted, visited, and closed.

- Data are grouped by advisor and updated in real time.

HU-CRM-016

Related Requirement: RF-CRM-016

Actor: Management

User Story: As management, I want to view total billed amounts and averages per service for

each advisor to measure commercial efficiency.

Acceptance Criteria:

- The system consolidates billed amounts per advisor.

- The average billing per service is calculated automatically.

HU-CRM-017

Related Requirement: RF-CRM-017

Actor: Management

User Story: As management, I want to view the total terminals and equipment sold by each

advisor to analyze complementary sales.

Acceptance Criteria:

- The system displays the number and total value of equipment sold.

- Information is grouped by advisor and based on confirmed records.

HU-CRM-018

Related Requirement: RF-CRM-018

Actor: Management

User Story: As management, I want to view the number of clients at each stage of the sales

265

45

funnel to identify opportunities and bottlenecks.

Acceptance Criteria:

- The system groups clients by funnel stage (prospecting, negotiation, closing, post-sale).

- Data can be filtered by advisor.

- Visualization reflects the most current state.

HU-CRM-019

Related Requirement: RF-CRM-019

Actor: Immediate Supervisor

User Story: As an immediate supervisor, I want to search and filter clients by negotiation stage,

visit date, or assigned advisor to follow up in an organized way.

Acceptance Criteria:

- Filters include stage, date, and advisor.

- Results are displayed according to the selected criteria.

- Only active clients are shown.

HU-CRM-020

Related Requirement: RF-CRM-020

Actor: Sales Advisor

User Story: As a sales advisor, I want to view the clients assigned to me immediately to provide

timely follow-up.

Acceptance Criteria:

- The advisor can only view assigned clients.

- Selecting a client loads the detailed client information view successfully.

HU-CRM-021

Related Requirement: RF-CRM-021

Actor: Immediate Supervisor

User Story: As an immediate supervisor, I want to consult the change history made by each

266

46

advisor on their clients to maintain control over modifications.

Acceptance Criteria:

- The system keeps a record of all changes made by advisors.

- Each record includes user, date, modified field, and previous value.

- The history is accessible only to immediate supervisors.

7. 5 Offer Matrix Module (MAT)

HU-MAT-001

Related Requirement: RF-MAT-001

Actor: Sales Advisor

User Story: As a sales advisor, I want to create a new offer matrix associated with a client and

an active negotiation so that I can record the proposed sales conditions.

Acceptance Criteria:

- The created matrix is automatically associated with both the client and the negotiation.

- The record is saved with the date and responsible user.

HU-MAT-002

Related Requirement: RF-MAT-002

Actor: Sales Advisor

User Story: As a sales advisor, I want to enter the offered products and services, specifying

quantity, unit prices, totals, and observations so that I can properly structure the commercial

proposal.

Acceptance Criteria:

- Each catalog service displays its cost, benefits, and conditions.

- The information is clearly visible on the interface.

- Incomplete services cannot be registered in the matrix.

HU-MAT-003

Related Requirement: RF-MAT-003

267

47

Actor: Sales Advisor

User Story: As a sales advisor, I want the system to automatically calculate the applicable

subsidy based on the client’s billing and number of proposed services, to estimate the total

benefit for the client.

Acceptance Criteria:

- The calculated subsidy value is displayed within the matrix.

- The calculation is reproducible and verifiable in test conditions.

HU-MAT-004

Related Requirement: RF-MAT-004

Actor: Sales Advisor

User Story: As a sales advisor, I want to attach quotations or complementary files to my offer

matrix to support the proposal with additional documentation.

Acceptance Criteria:

- The system accepts files in PDF, Excel, JPG, or PNG format.

- The maximum allowed size per file is 50 MB.

- Uploaded documents are linked to the matrix and available for download.

HU-MAT-005

Related Requirement: RF-MAT-005

Actor: Sales Advisor

User Story: As a sales advisor, I want to save my offer matrices as drafts so that I can review

and complete them before submitting them for approval.

Acceptance Criteria:

- Draft matrices can be reopened and edited by the advisor.

- Drafts are not visible to the immediate supervisor until submission.

HU-MAT-006

Related Requirement: RF-MAT-006

268

48

Actor: Sales Advisor

User Story: As a sales advisor, I want to send the offer matrix to my immediate supervisor for

approval so that the proposal can be formalized and negotiation can continue.

Acceptance Criteria:

- The matrix status automatically changes to “Pending Approval.”

- The immediate supervisor receives a notification upon submission.

- The advisor can no longer modify the matrix after sending it.

HU-MAT-007

Related Requirement: RF-MAT-007

Actor: Sales Advisor

User Story: As a sales advisor, I want to consult the history of my created matrices so that I can

review their status, observations, and associated subsidy amounts.

Acceptance Criteria:

- The history displays the creation date, total amount, and observations.

- Previous versions are preserved for audit purposes.

7. 6 Supervision and Approvals Module (SUP)

HU-SUP-001

Related Requirement: RF-SUP-001

Actor: Immediate Supervisor

User Story: As an immediate supervisor, I want to view all offer matrices pending approval so

that I can prioritize those that require review and avoid delays in the commercial process.

Acceptance Criteria:

- The system displays only matrices with the status “Pending Approval.”

- Essential data are shown: client, advisor, submission date, and total amount.

- The information updates automatically when new matrices are added.

269

49

HU-SUP-002

Related Requirement: RF-SUP-002

Actor: Immediate Supervisor

User Story: As an immediate supervisor, I want to consult the commercial indicators of each

matrix, including billing, number of services, and subsidy range, to objectively evaluate each

proposal before making a decision.

Acceptance Criteria:

- The system displays billing, number of services, and calculated subsidy indicators.

- The displayed values match the data from the original matrix.

- The supervisor cannot modify this information.

HU-SUP-003

Related Requirement: RF-SUP-003

Actor: Immediate Supervisor

User Story: As an immediate supervisor, I want to approve or reject offer matrices, entering a

reason in case of rejection, to maintain a clear record of all decisions made.

Acceptance Criteria:

- The supervisor can change the matrix status to “Approved” or “Rejected.”

- In case of rejection, the system requires entering a mandatory reason.

- Each decision is recorded with date, time, and user.

HU-SUP-004

Related Requirement: RF-SUP-004

Actor: Immediate Supervisor

User Story: As an immediate supervisor, I want to access a history of approved or rejected

matrices so that I can review previous decisions and facilitate audits or follow-ups.

Acceptance Criteria:

- The system stores approval and rejection decisions with their details.

- The history includes date, user, client, and advisor involved.

270

50

- Records cannot be modified once generated.

HU-SUP-005

Related Requirement: RF-SUP-005

Actor: Sales Advisor

User Story: As a sales advisor, I want to receive a notification when my matrix is approved or

rejected so that I can know the review outcome and proceed accordingly.

Acceptance Criteria:

- The system sends both an internal and email notification to the advisor.

- The message includes the result (approved or rejected) and, if applicable, the rejection reason.

- Notifications are recorded in the advisor’s history.

HU-SUP-006

Related Requirement: RF-SUP-006

Actor: Immediate Supervisor

User Story: As an immediate supervisor, I want to filter matrices by advisor, date, status, or

subsidy range to make searching and analysis easier during the review process.

Acceptance Criteria:

- Filters allow combining multiple criteria (advisor, date, status, subsidy).

- The displayed results exactly match the selected filters.

- The supervisor can clear or modify filters at any time.

7. 7 Document Management Module (DOC)

HU-DOC-001

Related Requirement: RF-DOC-001

Actor: Sales Advisor

User Story: As a sales advisor, I want to attach documents related to my negotiations so that I

can support the commercial process and facilitate its review.

Acceptance Criteria:

271

51

- The advisor can select an active negotiation and attach the corresponding documents.

- Documents are associated with the correct client and negotiation.

- The system records the upload date, time, and responsible user.

HU-DOC-002

Related Requirement: RF-DOC-002

Actor: Sales Advisor

User Story: As a sales advisor, I want to upload files up to 50 MB in PDF, JPG, or PNG formats

to ensure that the required documentation is sent in compatible formats.

Acceptance Criteria:

- The system validates file formats (PDF, JPG, PNG).

- Files exceeding 50 MB are not accepted.

- Valid files are stored correctly in the system.

HU-DOC-003

Related Requirement: RF-DOC-003

Actor: Sales Advisor

User Story: As a sales advisor, I want to label each uploaded document with its corresponding

type to maintain a clear organization of each client’s documentation.

Acceptance Criteria:

- The system requires selecting a label type (“Provisional RUC,” “Initial Proposal,” “Visit

Report,” “Final Contract”).

- The label is recorded together with the document.

- Documents can later be filtered by type.

HU-DOC-004

Related Requirement: RF-DOC-004

Actor: Coordinator

User Story: As a coordinator, I want to define which documents are mandatory or optional

272

52

depending on the type of service so that negotiation requirements are standardized.

Acceptance Criteria:

- The coordinator can mark documents as “mandatory” or “optional.”

- The system enforces the corresponding rules based on service or negotiation type.

- Advisors can see which documents must be uploaded before closing a negotiation.

HU-DOC-005

Related Requirement: RF-DOC-005

Actor: Sales Advisor

User Story: As a sales advisor, I want to check the status of uploaded documents so that I know

which ones have been reviewed, approved, or are still pending.

Acceptance Criteria:

- The system displays the current status of each document (Pending, Approved, Rejected).

- Statuses update automatically according to the coordinator’s actions.

- The advisor can consult this information from their account at any time.

HU-DOC-006

Related Requirement: RF-DOC-006

Actor: Coordinator

User Story: As a coordinator, I want to review the documents uploaded by each sales advisor to

verify compliance with documentation requirements.

Acceptance Criteria:

- The system lists documents grouped by advisor and negotiation.

- Each record displays document type, upload date, and status.

- Only coordinators have access to this view.

HU-DOC-007

Related Requirement: RF-DOC-007

Actor: Coordinator

273

53

User Story: As a coordinator, I want to download negotiation documents individually or in bulk

so that I can review and store the information more efficiently.

Acceptance Criteria:

- The system allows downloading a specific document or all negotiation files.

- Files are preserved in their original format.

- A record of downloads is kept in the system.

HU-DOC-008

Related Requirement: RF-DOC-008

Actor: Sales Advisor

User Story: As a sales advisor, I want to receive a notification when my documents are reviewed,

approved, or rejected so that I can track the validation progress.

Acceptance Criteria:

- The system sends both an internal notification and an email to the advisor.

- The message includes the result of the review and any comments.

- The notification is stored in the user’s history.

HU-DOC-009

Related Requirement: RF-DOC-009

Actor: Coordinator

User Story: As a coordinator, I want to view a list of advisors with pending document uploads

or reviews so that I can prioritize cases that require follow-up.

Acceptance Criteria:

- The system generates a list of advisors with pending documentation.

- The list includes associated clients and missing document types.

- The list updates automatically as uploads are completed.

274

54

7. 8 Reporting Module (REP)

HU-REP-001

Related Requirement: RF-REP-001

Actor: Manager

User Story: As a manager, I want to generate commercial performance reports by advisor,

month, or period so that I can evaluate team productivity and identify areas for improvement.

Acceptance Criteria:

- Reports include metrics such as sales, closures, and billing.

- Generated data correspond to the selected period.

HU-REP-002

Related Requirement: RF-REP-002

Actor: Immediate Supervisor

User Story: As an immediate supervisor, I want to generate sales and closure reports for the

advisors under my supervision, filtering by date, service type, or zone, to conduct detailed

performance tracking.

Acceptance Criteria:

- Results include only advisors under the supervisor’s responsibility.

- Reports display total sales and closures by advisor.

HU-REP-003

Related Requirement: RF-REP-003

Actor: Manager

User Story: As a manager, I want to visualize key metrics such as sales, closures, visits, and

average negotiation time to measure the overall performance of the sales force.

Acceptance Criteria:

- The system calculates and presents the mentioned metrics.

- Values are automatically updated based on registered data.

275

55

- Information is consolidated by period or defined range.

HU-REP-004

Related Requirement: RF-REP-004

Actor: Immediate Supervisor

User Story: As an immediate supervisor, I want to view operational metrics of the advisors,

including sales, closures, and visits made, to monitor their commercial performance.

Acceptance Criteria:

- Data correspond to the selected period.

- Only advisors under the supervisor’s direct supervision are displayed.

HU-REP-005

Related Requirement: RF-REP-005

Actor: Immediate Supervisor

User Story: As an immediate supervisor, I want to compare the performance of my advisors

against the objectives defined by management so that I can identify deviations and take corrective

actions.

Acceptance Criteria:

- The system compares actual metrics with defined objectives.

- The percentage of compliance for each advisor is displayed.

- Data update automatically based on registered metrics.

HU-REP-006

Related Requirement: RF-REP-006

Actor: Manager

User Story: As a manager, I want to export generated reports in PDF or Excel format so that I

can analyze them externally or present them during meetings.

Acceptance Criteria:

- Exported files retain the original report’s structure and content.

276

56

- The export process completes successfully without errors.

HU-REP-007

Related Requirement: RF-REP-007

Actor: Immediate Supervisor

User Story: As an immediate supervisor, I want to export generated reports in PDF or Excel

format so that I can back up the commercial management tracking.

Acceptance Criteria:

- Exported reports preserve applied filters.

- Files can be downloaded successfully.

HU-REP-008

Related Requirement: RF-REP-008

Actor: Manager

User Story: As a manager, I want to visualize consolidated information through charts and KPI

indicators to easily interpret the team’s overall results.

Acceptance Criteria:

- The system presents bar charts, line graphs, or KPI indicators.

- Displayed data correspond to consolidated reports.

HU-REP-009

Related Requirement: RF-REP-010

Actor: Sales Advisor

User Story: As a sales advisor, I want to view my own performance metrics, including contacted

clients, active negotiations, closures, and accumulated billing, so that I can assess my personal

progress.

Acceptance Criteria:

- The system displays updated personal metrics for the advisor.

- Data include contacted clients, closures, and total billing.

277

57

- The advisor can only view their own information.

278

CHAPTER 8

PROTOTYPE

8. 1 Link

The prototype of the BOPADIGITAL system was developed using Excalidraw, providing a

visual representation of the main modules, navigation flow, and user interface layout. More

images and the user flow can be found in the appendix section. The prototype can be accessed

through the following link: BOPADIGITAL Prototype.

Figure 8.1 Prototype of BOPADIGITAL

279

CHAPTER 9

EVIDENCES

9. 1 Requirements Elicitation Technique

For the requirements elicitation process, the development team applied the interview technique

with the project’s client representatives from BOPACORP S.A. Through structured interviews,

relevant information was gathered regarding the company’s current commercial processes,

operational challenges, and expectations for the new system. This technique enabled the team to

capture detailed functional and non-functional needs directly from key stakeholders, ensuring

that the defined requirements aligned with real business objectives and daily workflows.

Figure 9.1 Meeting with the managers of BOPACORP S.A.

9. 2 Evidence Repository

The evidence can be accessed through the following link: Repository.

280

CHAPTER 10

INDIVIDUAL CONTRIBUTIONS

Name Contributions

Aragon Intriago Shirley

Yamel

Preparation of functional and non-functional

requirements, and drafting of user stories.

Diaz Osorio Fernando

Nahim

Communication with the client and participation in the

preparation of the project specification document.

Muñoz Sanchez Salvador

Gabriel

Preparation of functional and non-functional

requirements, and coordination of the requirements

validation process.

Navarrete Castillo Anthony

Josue

Preparation of the project prototype and collaboration

in the drafting of the specification document in LaTeX.

Tumbaco Santana Gabriel

Alejandro

Communication with the client, preparation of the

prototype, and compilation of the final LaTeX

document.

Table 10.1 Individual Contributions of the Project

281

CHAPTER 11

AUTHORSHIP DECLARATION

We, the undersigned members of the BOPADIGITAL development team, hereby declare that

the present document titled “BOPACORP S.A. Requirements Specification Document” has

been entirely prepared by us as part of the course Software Engineering I at Escuela Superior

Politécnica del Litoral (ESPOL).

We affirm that all sections, analyses, and specifications contained in this document represent

our own work and understanding, based on information gathered from the client and the

methodologies applied during the software requirements engineering process.

No part of this document has been copied, plagiarized, or taken from other sources without

proper acknowledgment. Any external reference used has been duly cited in the bibliography

according to academic integrity standards.

Each member of the team assumes full responsibility for the authenticity, accuracy, and originality

of the content herein.

Digital Confirmation: All members of the team confirm authorship through their electronic

submission of this document.

Team Members:

Aragon Intriago Shirley Yamel

Diaz Osorio Fernando Nahim

Muñoz Sanchez Salvador Gabriel

Navarrete Castillo Anthony Josue

Tumbaco Santana Gabriel Alejandro

282

APPENDIX I

PROTOTYPE

1. Prototype’s Screenshots

283

63

a) Advisor’s event view b) Client’s profile

c) Client Document Management d) Create an event associated with a client

Figure-A I-1 Screenshots of BOPADIGITAL mobile app from the perspective of a Sales Advisor.

284

64

a) Advisor’s assigned clients by assignment date b) Monthly performance overview of a sales advisor

Figure-A I-2 Screenshots of BOPADIGITAL mobile app from the perspective of a Sales Advisor.

285

65

a) Admin’s event view grouped by Sales Advisor b) Clients grouped by state

c) System’s users grouped by role d) Dashboard showing overall client statistics and performance indicators.

Figure-A I-3 Screenshots of BOPADIGITAL mobile app from the perspective of Management.

286

66

a) Website Home

b) Product catalog

Figure-A I-4 Screenshots of BOPADIGITAL CMS website

287

67

a) Product catalog by section

b) Web admin view

Figure-A I-5 Screenshots of BOPADIGITAL CMS website

288

68

Figure-A I-6 Website from the perspective of a sales advisor candidate.

289

69

a) Sales funnel overview

b) Sales funnel overview 2

Figure-A I-7 Screenshots of BOPADIGITAL CRM website for sales consultant

290

70

a) Form to create contacts

b) List of assigned contacts

Figure-A I-8 Screenshots of BOPADIGITAL CRM website for sales consultant

291

71

a) Table view of all sales advisors

b) Dashboard of overall business statistics

Figure-A I-9 Screenshots of BOPADIGITAL CRM form the perspective of Management.

292

72

a) View of the recent activity of all sales advisors

b) Table view of all clients

Figure-A I-10 Screenshots of BOPADIGITAL CRM form the perspective of Management.

293

73

a) View for assigning a client to a sales advisor

Figure-A I-11 Screenshots of BOPADIGITAL CRM form the perspective of Management.

294

APPENDIX II

CLIENT ACCEPTANCE LETTER

1. Signed Approval Document

This appendix contains the official acceptance letter signed by the stakeholder representative of

BOPACORP S.A., confirming their agreement with the content of this Requirements Specification

Document and validating that it meets the functional and non-functional expectations discussed

during the requirements elicitation process.

295

### Carta de aceptación de proyecto BOPADIGITAL

Guayaquil, 4 de Noviembre del 2025.

A la fecha de hoy, ante los documentos presentados, los cuales representan el trabajo realizado hacia el proyecto BOPADIGITAL. En el que se ponen a evidencia los siguientes contenidos:

● Perfiles de interés en el marco del proyecto (Stakeholders). ● Funcionalidad básica en formato de requerimientos funcionales del aplicativo móvil establecido. ● Funcionalidad básica en formato de requerimientos funcionales del sitio web público acordado. ● Restricciones y limitaciones del alcance del proyecto BOPADIGITAL en formato de requerimientos no funcionales del aplicativo móvil y web acordadas. ● Casos de uso del proyecto BOPADIGITAL en formato de historias de usuario, separadas y organizadas según perfiles de interés (Stakeholders) del aplicativo móvil y web acordadas. ● Prototipado e ideación de estructura visual del aplicativo móvil interno acordado. ● Prototipado e ideación de estructura visual del sitio web público acordado. ● Prototipo de flujo de navegación básico para el aplicativo móvil y el sitio web acordados.

Mediante la presente acta de conformidad, el cliente, representado por Mgtr. Christian Pauta, declara haber recibido, revisado y aceptado el contenido del documento entregado, reconociendo que refleja adecuadamente lo establecido durante las reuniones y manifestando su conformidad con los puntos especificados previamente, los cuales cumplen con los objetivos planteados para el proyecto BOPADIGITAL.

De la misma forma, declara su disposición a continuar trabajando con el equipo establecido, en futuras reuniones y discusiones que den lugar para seguir realizando avances en el proyecto ya mencionado.

Por su parte, el equipo de desarrollo reitera su compromiso a seguir trabajando de manera dinámica y continua, fieles a los intereses que presenta el proyecto, en las siguientes fases de desarrollo del proyecto BOPADIGITAL.

Recibo conforme y en acuerdo con lo establecido en el presente documento.

______________________________________ Mgtr. Christian Pauta Propietario Gerente de BOPACORP S.A.

### 296

APPENDIX III

SIGNED AUTORSHIP DECLARATION

1. Signatures and Formal Confirmation

This appendix includes the signed authorship declaration, in which the members of the

development team formally certify that the work presented in this document is original, was

produced collaboratively, and complies with the academic and ethical standards established

by the institution. The signatures below represent each member’s personal attestation to this

statement and their commitment to the document’s authenticity.

297

FIRMAS - DECLARACIÓN DE AUTORÍA

Nombre Firma Fecha

Aragon Intriago Shirley Yamel

Estudiante de Ingeniería en Computación

Escuela Superior Politécnica del Litoral

(ESPOL)

12/11/2025

Díaz Osorio Fernando Nahim

Estudiante de Ingeniería en Computación Escuela Superior Politécnica del Litoral (ESPOL)

12/11/2025

Navarrete Castillo Anthony Josué

Estudiante de Ingeniería en Computación Escuela Superior Politécnica del Litoral (ESPOL)

12/11/2025

Muñoz Sánchez Salvador Gabriel

Estudiante de Ingeniería en Computación Escuela Superior Politécnica del Litoral (ESPOL)

12/11/2025

Tumbaco Santana Gabriel Alejandro

Estudiante de Ingeniería en Computación Escuela Superior Politécnica del Litoral (ESPOL)

12/11/2025

298