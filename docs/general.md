<!-- markdownlint-enable require-heading-body -->
<div class="section-1" markdown="1">
<style>
  .section-1 { counter-set: section 1; }
</style>

# General {.body}

## Scope {.body}

This document specifies a set of rules for organizing, describing, and defining transportation management information to be exchanged between transportation management applications and transportation equipment. This document defines the Structure and Identification of Management Information (SMI) used in transportation-related devices. This document is applicable to the NTCIP 1200 series and other NTCIP standards that deal with device data dictionaries.

NOTE&mdash;This document relies on widely accepted conventions, generally designated as “SMIv2” and defined in the Internet Architecture Board (IAB) Standard (STD) 58.

## References {.body}

The following documents are referenced by this document. At the time of publication, the editions indicated were valid.

### Normative References {.body}

Normative references contain provisions that, through reference in this text, constitute provisions of this document. All standards are subject to revision, and parties to agreements based on this standard are encouraged to investigate the possibility of applying the most recent editions of the standard listed.

|Identifier| Title  |
|----------|-----------|
|IAB STD 58|(RFC 2578, Structure of Management Information Version 2 (SMIv2), 1999;<br>RFC 2579, Textual Conventions for SMIv2, 1999;<br>RFC 2580, Conformance Statements for SMIv2, 1999)|
|RFC 3416  |Version 2 of the Protocol Operations for the Simple Network Management Protocol (SNMP), 2002|
|RFC 3419  |Textual Conventions for Transport Addresses, 2002|
|RFC 3584  |Coexistence between Version 1, Version 2, and Version 3 of the Internet-standard Network Management Framework, Internet Engineering Task Force (IETF), August 2003|
|RFC 4001  |Textual Conventions for Internet Network Addresses, 2005|
|RFC 4181  |Guidelines for Authors and Reviewers of MIB Documents, Internet Engineering Task Force (IETF), September 2005|
|ITU-T X.208|Open Systems Interconnection Model and Notation – Specification of Abstract Syntax Notation One (ASN.1), 1988[^a]|
|ITU-T X.680<br>(ISO/IEC 8824-1:2015)|Information technology—Abstract Syntax Notation One (ASN.1): Specification of basic notation|
|ITU-T X.690<br>(ISO/IEC 8825-1)|Information technology—ASN.1 encoding rules: Specification of Basic Encoding Rules (BER), Canonical Encoding Rules (CER), and Distinguished Encoding Rules (DER)|
|ITU-T X.696<br>(ISO/IEC 8825-7)|Information technology—ASN.1 encoding rules: Specification of Octet Encoding Rules (OER)|
|BIPM SI|The International System of Units (SI) — 9th edition (2019), https://www.bipm.org/documents/20126/41483022/SI-Brochure-9-EN.pdf|

### Other References {.body}

Other references are included to provide a more complete understanding of this
document and its relationship to other documents.

#### Other Resources for Contributors {.body}

This document standardizes and tailors certain aspects of the information
contained in open-sauced; however, it is not a complete replacement of that
material. If you wish to learn more about open-source development, the following
materials may be of interest:

 |Identifier| Title  |
|----------|-----------|
| IAB STD 8 | (_RFC 0854: 1983, Telnet Protocol Specification_, and RFC 0855: 1983, _Telnet Options Specifications_; J. Postel, J. Reynolds) |
| RFC 2021 | _Remote Network Monitoring Management Information Base Version 2 using SMIv2_, 1997 |
| RFC 2287 | _Definitions of System-level Managed Objects for Applications_, 1998 |
| RFC 2856 | _Textual Conventions for Additional High Capacity Data Types_, 2000 |
| RFC 2981 | _Event MIB_, 2000 |
| RFC 2982 | _Distributed Management Expression MIB_, 2000 |
| RFC 3014 | _Notification Log MIB_, 2000 |
| RFC 3231 | _Definitions of Managed Objects for Scheduling Management Operations_, 2002 |
| RFC 3411 | _An Architecture for Describing Simple Network Management Protocol (SNMP) Management Frameworks_, 2002 |
| RFC 3433 | _Entity Sensor Management Information Base_, 2002 |
| RFC 3877 | _Alarm Management Information Base (MIB)_, 2001 |
| RFC 4268 | _Entity State MIB_, 2005 |
| RFC 6933 | _Entity MIB (Version 4)_, 2013 |
| AASHTO / ITE / NEMA NTCIP 1201 v03 | _Global Object (GO) Definitions—version 03_, published March 2011 |
| AASHTO / ITE / NEMA NTCIP 1202 v03 | _Object Definitions for Actuated Signal Controllers (ASC) Interface—version 03A_, published May 2019 |
| AASHTO / ITE / NEMA NTCIP 8005 v02 | _Procedures for Creating Management Information Base (MIB) Files_, Proposed |
| ISO 26048-1:2025 [^b] | _Intelligent transport systems – Roadside modules SNMP data interface – Part 1: Global Objects_ |
| ISO/IEC 9834-1:2012 | _Information technology — Procedures for the operation of object identifier registration authorities: General procedures and top arcs of the international object identifier tree — Part 1:_ |
| ISO/TS 20684-2:2021 | _Intelligent transport systems – Roadside modules SNMP data interface – Part 2: Generalized field device basic management_ |
| ISO/WD 20684-3 | _Intelligent transport systems – Roadside modules SNMP data interface – Part 3: Triggers_ |
| ISO/WD 20684-4 | _Intelligent transport systems – Roadside modules SNMP data interface – Part 4: Notifications_ |
| ISO/WD 20684-5 | _Intelligent transport systems – Roadside modules SNMP data interface – Part 5: Logs_ |
| ITU-T X.660 (07/2011) | _Identical to ISO/IEC 9834-1:2012. Recommended status._ |
| ISO/WD 20684-6 | _Intelligent transport systems – Roadside modules SNMP data interface – Part 6: Commands_ |
| ISO/WD 20684-7 | _Intelligent transport systems – Roadside modules SNMP data interface – Part 7: Support Features_ |
| NEMA TS_2-2016 | _Traffic Controller Assemblies with NTCIP Requirements_, 2016 |
||IETF, Generic and Common Textual Conventions (TCs), https://trac.ietf.org/trac/ops/wiki/mib-common-tcs, accessed June 10, 2021|
||Perkins, D; McGinnis, E., Understanding SNMP MIBs, Prentice-Hall, Inc., 1997, ISBN 0-13-437708-7|
||Stallings, William, SNMP, SNMPv2, and CMIP: The Practical Guide to Network-Management Standards, Massachusetts, Addison-Wesley Publishing Company, 1993, ISBN 0-201-63331-0|
||Larmouth, John, ASN.1 Complete, Academic Press, a Harcourt Science and Technology Company, May 1999, ISBN 0-12233-435-3, http://www.oss.com/asn1/booksintro.html (October 9, 2000)|
||Dubuisson, Olivier, ASN.1 Communication between Heterogeneous Systems, June 5, 2000, ISBN 0-12-6333361-0, http://www.oss.com/asn1/bookintro.html (October 9, 2000)|
||Booch, Grady, Rumbaugh, James, Jacobson, Ivar, Unified Modeling Language User Guide, September 30, 1998, ISBN 0-20157-168-4|
||UML basics: An introduction to the Unified Modeling Language, www-106.ibm.com/developerworks/rational/library/769.html#N10090.|

### Contact Information {.body}

#### Internet Documents {.body}

Obtain Request for Comment (RFC) electronic documents from several repositories online at:

> [www.rfc-editor.org](http://www.rfc-editor.org)<br>[www.rfc-editor.org/repositories.html](http://www.rfc-editor.org/repositories.html)

#### Architecture Reference for Cooperative and Intelligent Transportation (ARC-IT) {.body}

The Architecture Reference for Cooperative and Intelligent Transportation (ARC-IT) may be viewed online at:

> <http://arc-it.net>

#### ISO, IEC, and ISO/IEC Standards {.body}

ISO, IEC, and ISO/IEC standards can be purchased on-line in electronic format or printed copy from:

> Techstreet<br>6300 Interfirst Dr.<br>Ann Arbor, MI 48108<br>(800) 699-9277<br>[www.techstreet.com](http://www.techstreet.com)

#### IEEE Standards {.body}

IEEE standards can be purchased on-line in electronic format or printed copy from:

> Techstreet<br>6300 Interfirst Dr.<br>Ann Arbor, MI 48108<br>(800) 699-9277<br>[www.techstreet.com](http://www.techstreet.com)

#### NTCIP Standards {.body}

Copies of NTCIP standards may be obtained from:

> NTCIP Coordinator<br>National Electrical Manufacturers Association<br>1300 N.17th Street, Suite 900<br>Rosslyn, Virginia 22209-3801<br>[www.ntcip.org](http://www.ntcip.org)<br>e-mail: [ntcip@nema.org](mailto:ntcip@nema.org)

Draft amendments, which are under discussion by the relevant NTCIP Working Group, and amendments recommended by the NTCIP Joint Committee are available.

## General Statements {.body}

The remainder of this document is broken into the following chapters:

- **Background:** Describes the purpose of this document
- **Object Identification:** Discusses the object identifier tree and defines the nodes related to the NTCIP effort.
- **Rules for Module Development:** Defines the rules for developing MIB modules within the NTCIP standards efforts, including the specialized fields used by the NTCIP.
- **Requirements for Agent Implementations:** Requirements for implementations of agents that claim conformance to NTCIP standards.
- **Guidelines for Agencies:** Advice for agencies on operating NTCIP devices.
- **NTCIP Structure of Management Information:** The formal MIB module that defines the structure of the NTCIP portion of the object identifier tree and key textual conventions.
- **Conversion from SMIv1 to SMIv2:** Rules for converting SNMPv1 MIBs to support SNMPv3.
- **Macro Examples:** Examples of applying the rules defined in this document.
- **History of Changes:** A list of changes made with the current version from the last major version.

## Terms {.body}

For the purposes of this document, the following terms and definitions apply. Terms not defined here are used in accordance with their definitions in ISO/IEC/IEEE 24765. Words not defined here or in ISO/IEC/IEEE 24765 are used in accordance with their definitions in _Webster’s New Collegiate Dictionary_.

| **Term** | **Definition** |
| --- | --- |
| **agent** | The entity that receives requests and transmits responses to the received requests. |
| **block object type** | An object type that represents a standardized data structure of elemental object types. |
| **compatibility** | The ability of two or more systems or components to exchange information.<br><br>\[ISO/IEC/IEEE 24765\] |
| **configurable object** | An object type that represents a data structure that can be configured at run-time to include elemental object types. |
| **context** | An instance of a management information base (MIB).<br><br>NOTE—A single SNMP agent (e.g., a unique UDP/IP address) typically represents a single context, but might support multiple contexts if it, for example, serves as the interface for multiple field devices (e.g., two dynamic message signs controlled by a single controller) or serves as a proxy agent for multiple field devices. When there are multiple contexts, there might be multiple object instances with the same object identifier and the context is used to disambiguate. |
| **current** | Reflecting the conditions at the present time (or at the time at which the data is time stamped) as determined by the Controller. Within the context of a status value, indicates the most up-to-date design of the element (e.g., user need, requirement, object). |
| **data** | Information before it is interpreted. |
| **datagram** | A self-contained unit of data transmitted independently of other datagrams. |
| **deprecated** | A status value that indicates the user need, requirement, dialog, or object is valid in limited circumstances, but has been replaced by another.<br><br>NOTE—This definition is modified from “Understanding SNMP MIBS.” Procurements can require support for deprecated objects to anable multi-version interoperability (e.g., backward compatibility) with legacy implementations. |
| **file** | A grouping of data into a single sequence of bytes that can be referred to by file operations.<br><br>NOTE—A file exists nominally in a directory, and can have an associated path. |
| **intelligent transportation systems (ITS)** | The application of advanced information processing and communications, sensing, and control technologies to surface transportation with the objective of promoting more efficient use of the existing highway and transportation network, increasing safety and mobility, and decreasing environmental impacts.<br><br>NOTE—Also known as "intelligent transport systems" |
| **International Organization for Standardization (ISO)** | An international standards organization.<br><br>NOTE—ANSI is the primary interface to ISO within the United States. Often thought to be International Standards Organization, because of its acronym ISO. |
| **internet** | A large collection of connected networks, primarily in the United States, running the Internet suite of protocols.<br><br>NOTE—Sometimes referred to as the _DARPA Internet, NSF/DARPA Internet_, or the _Federal Research Internet._ |
| **Interchangeable** | A condition which exists when two or more items possess such functional and physical characteristics as to be equivalent in performance and durability, and are capable of being exchanged one for the other without alteration of the items themselves, or adjoining items, except for adjustment, and without selection for fit and performance.<br><br>Note: See National Telecommunications and Information Administration, U.S. Department of Commerce |
| **interoperability** | Degree to which two or more systems, products or components can exchange information and use the information that has been exchanged.<br><br>\[ISO/IEC/IEEE 24765\] |
| **leaf object type** | An object type that does not have any sub-identifiers assigned (other than for object instances) |
| **management information base (MIB)** | A structured collection of managed information contained within a SNMP context. A MIB represents the instantiated data objects defined by one or more MIB modules and integrated into a device or management station. |
| **Management Station** | The computer system with which the device communicates. Typically, the management station commands and monitors the device. |
| **MIB module** | A sequence of NVT ASCII characters conforming to X.208 Abstract Syntax Notation One (ASN.1) and IAB STD 58. MIB modules are used to define the data objects that are to make up the instantiated objects of the MIB.<br><br>NOTE—A MIB module can be, and within NTCIP typically is, presented as both part of a standard and as a stand-alone, computer-readable text file. |
| **National Transportation Communications for ITS Protocol (NTCIP)** | A family of protocols that provide common control and data collection services as well as accommodating various system topologies and data routing duties.<br><br>NOTE—NTCIP is designed to support not only currently deployed systems, but also new systems and technologies as they become available. |
| **network** | A collection of devices connected by intermediate systems and populated by end systems. |
| **notification** | An unsolicited event message issued by an SNMP agent for a management station with an expectation of an acknowledgement. |
| **object** | An entity identified by a node on the international object identifier tree.<br><br>NOTE – See object instance and object type, both of which are types of objects, along with any other entity that can be identified, such as a standard. This document attempts to use the most precise term within its text to assist in distinguishing among "object type" or "object instance". The use of the term "object" is typically limited to registering items on the international object identifier tree. |
| **OBJECT IDENTIFIER** | A unique name (identifier) that is associated with each type of object in a MIB that is a defined ASN.1 type. |
| **object instance** | An instance of an object type, which is an actual instance of data.<br><br>NOTE – This document avoids using the term “object” to describe this concept to prevent any ambiguity with an object referenced by the international object identifier tree or an object type. |
| **object type** | An abstract specification for a specific piece of data that can be instantiated within a device (zero or many times depending on how it is specified). It specifies the data using the OBJECT-TYPE macro. |
| **OBJECT-TYPE** | An X.208 ASN.1 macro used to define the meta-attributes of an object type in an SNMP MIB module. |
| **obsolete** | A status value that indicates the definition is no longer valid, was found to be flawed, was redundant, or was not useful.<br><br>NOTE—In the next (or some future) edition of a standard, any element (e.g., requirement, object) with a status of “obsolete” can be removed. This definition is modified from “Understanding SNMP MIBS.” |
| **protocol** | A specific set of rules, procedures, and conventions defining the format and timing of data transmissions between devices that are accepted and used to understand each other. |
| **Requirement** | A requirement describes a condition or capability to which a system shall conform; either derived directly from user needs, or stated in a contract, standard, specification, or other normative document. A desired feature, property, or behavior of a system. |
| **Requirements Traceability** | The ability to follow or study the logical progression among the needs, requirements, and design details in a step-by-step fashion. |
| **Simple Network Management Protocol (SNMP)** | A communications protocol developed by the Internet Engineering Task Force (IETF), used for configuration and monitoring of network devices. |
| **Trap** | An unsolicited event message issued by an SNMP agent for a management station without any expectation of an acknowledgement. |
| **User** | A person using the system that is developed. |
| **User Need** | The business or operational problem (opportunity) that is to be fulfilled to justify procurement or use.<br><br>Note: While this is termed a “user need” within the NTCIP community, it reflects needs of all stakeholders. |

## Abbreviations {.body}

The abbreviations and acronyms used in this document are defined as follows:

| **ASCII** | American National Standard Code for Information Interchange |
| --- | --- |
| **ASN.1** | Abstract Syntax Notation One, as defined by either ITU-T X.208 or ITU-T X.680 (ISO/IEC 8824-1) (within the context used, both apply) |
| **BER** | Basic Encoding Rules, as defined by ITU-T X.690 (ISO/IEC 8825-1) |
| **IAB STD** | Internet Architecture Board Standard |
| **IANA** | Internet Assigned Numbers Authority |
| **IEC** | International Electrotechnical Commission |
| **IEEE** | Institute of Electrical and Electronics Engineers |
| **IETF** | Internet Engineering Task Force |
| **IP** | Internet Protocol |
| **ITU-T** | International Telecommunication Union – Telecommunication Standardization Sector |
| **MVI** | Multi-Version Interoperability (formerly Backward Compatibility) |
| **NVT** | Network Virtual Terminal |
| **OER** | Octet Encoding Rules, as defined by ITU-T X.696 (ISO/IEC 8825-7) |
| **OSI** | Open Systems Interconnection |
| **PDU** | Protocol Data Unit |
| **PRL** | Protocol Requirements List |
| **RFC** | Request for Comments |
| **SMI** | Structure and Identification of Management Information |
| **SNMP** | Simple Network Management Protocol version 3 |
| **TCP** | Transport Control Protocol |
| **UML** | Unified Modeling Language |
| **X.208 ASN.1** | Abstract Syntax Notation One, as defined by ITU-T X.208 |
| **X.680 ASN.1** | Abstract Syntax Notation One, as defined by ITU-T X.680 (ISO/IEC 8824-1) |

</div>

[^a]: IAB STD 58 is still based on ITU-T X.208, which is now withdrawn, but defines the fundamental concept of a macro and MIB module as used for SNMP.

[^b]: See the [ISO maintenance portal for ISO 26048-1](https://standards.iso.org/iso/20684/-1/ed-1/en/) for maintained electronic files.
