<!-- markdownlint-enable require-heading-body -->
<style>
  body { counter-reset: section 1; }
</style>

# General \[Informative\]

## Scope

This document specifies a set of rules for organizing, describing, and
defining transportation management information to be exchanged between
transportation management applications and transportation equipment.
This document defines the Structure and Identification of Management
Information (SMI) used in transportation-related devices. This document
is applicable to the NTCIP 1200 series and other NTCIP standards that
deal with device data dictionaries.

NOTE---This document relies on widely accepted conventions, generally
designated as "SMIv2" and defined in the Internet Architecture Board
(IAB) Standard (STD) 58.

## References

The following documents are referenced by this document. At the time of
publication, the editions indicated were valid.

### Normative References

Normative references contain provisions that, through reference in this
text, constitute provisions of this document. All standards are subject
to revision, and parties to agreements based on this standard are
encouraged to investigate the possibility of applying the most recent
editions of the standard listed.

+-----------------+--------------------------------------------------------------------+
| **Identifier**  | **Title**                                                          |
+=================+====================================================================+
| IAB STD 58      | (RFC 2578, Structure of Management Information Version 2 (SMIv2),  |
|                 | 1999;                                                              |
|                 |                                                                    |
|                 | RFC 2579, Textual Conventions for SMIv2, 1999;\                    |
|                 | RFC 2580, Conformance Statements for SMIv2, 1999)                  |
+-----------------+--------------------------------------------------------------------+
| RFC 3416        | Version 2 of the Protocol Operations for the Simple Network        |
|                 | Management Protocol (SNMP), 2002                                   |
+-----------------+--------------------------------------------------------------------+
| RFC 3419        | Textual Conventions for Transport Addresses, 2002                  |
+-----------------+--------------------------------------------------------------------+
| RFC 3584        | Coexistence between Version 1, Version 2, and Version 3 of the     |
|                 | Internet-standard Network Management Framework, Internet           |
|                 | Engineering Task Force (IETF), August 2003                         |
+-----------------+--------------------------------------------------------------------+
| RFC 4001        | Textual Conventions for Internet Network Addresses, 2005           |
+-----------------+--------------------------------------------------------------------+
| RFC 4181        | Guidelines for Authors and Reviewers of MIB Documents, Internet    |
|                 | Engineering Task Force (IETF), September 2005                      |
+-----------------+--------------------------------------------------------------------+
| ITU-T X.208     | *Open Systems Interconnection Model and Notation -- Specification  |
|                 | of Abstract Syntax Notation One (ASN.1),* 1988[^1]                 |
+-----------------+--------------------------------------------------------------------+
| ITU-T X.680     | *Information technology---Abstract Syntax Notation One (ASN.1):    |
|                 | Specification of basic notation*                                   |
| (ISO/IEC        |                                                                    |
| 8824-1:2015)    |                                                                    |
+-----------------+--------------------------------------------------------------------+
| ITU-T X.690     | *Information technology---ASN.1 encoding rules: Specification of   |
|                 | Basic Encoding Rules (BER), Canonical Encoding Rules (CER), and    |
| (ISO/IEC        | Distinguished Encoding Rules (DER)*                                |
| 8825-1)         |                                                                    |
+-----------------+--------------------------------------------------------------------+
| ITU-T X.696     | *Information technology---ASN.1 encoding rules: Specification of   |
|                 | Octet Encoding Rules (OER)*                                        |
| (ISO/IEC        |                                                                    |
| 8825-7)         |                                                                    |
+-----------------+--------------------------------------------------------------------+
| BIPM SI         | *The International System of Units (SI)* *--- 9th edition (2019)*, |
|                 | https://www.bipm.org/documents/20126/41483022/SI-Brochure-9-EN.pdf |
+-----------------+--------------------------------------------------------------------+
|                 |                                                                    |
+-----------------+--------------------------------------------------------------------+

### Other References

Other references are included to provide a more complete understanding
of this document and its relationship to other documents.

+-----------------+----------------------------------------------------+
| **Identifier**  | **Title**                                          |
+=================+====================================================+
| IAB STD 8       | (*RFC 0854: 1983, Telnet Protocol Specification*,  |
|                 | and RFC 0855: 1983, *Telnet Options                |
|                 | Specifications*; J. Postel, J. Reynolds)           |
+-----------------+----------------------------------------------------+
| RFC 2021        | *Remote Network Monitoring Management Information  |
|                 | Base Version 2 using SMIv2*, 1997                  |
+-----------------+----------------------------------------------------+
| RFC 2287        | *Definitions of System-level Managed Objects for   |
|                 | Applications*, 1998                                |
+-----------------+----------------------------------------------------+
| RFC 2856        | *Textual Conventions for Additional High Capacity  |
|                 | Data Types*, 2000                                  |
+-----------------+----------------------------------------------------+
| RFC 2981        | *Event MIB*, 2000                                  |
+-----------------+----------------------------------------------------+
| RFC 2982        | *Distributed Management Expression MIB*, 2000      |
+-----------------+----------------------------------------------------+
| RFC 3014        | *Notification Log MIB*, 2000                       |
+-----------------+----------------------------------------------------+
| RFC 3231        | *Definitions of Managed Objects for Scheduling     |
|                 | Management Operations*, 2002                       |
+-----------------+----------------------------------------------------+
| RFC 3411        | *An Architecture for Describing Simple Network     |
|                 | Management Protocol (SNMP) Management Frameworks*, |
|                 | 2002                                               |
+-----------------+----------------------------------------------------+
| RFC 3433        | *Entity Sensor Management Information Base*, 2002  |
+-----------------+----------------------------------------------------+
| RFC 3877        | *Alarm Management Information Base (MIB)*, 2001    |
+-----------------+----------------------------------------------------+
| RFC 4268        | *Entity State MIB*, 2005                           |
+-----------------+----------------------------------------------------+
| RFC 6933        | *Entity MIB (Version 4)*, 2013                     |
+-----------------+----------------------------------------------------+
| AASHTO / ITE /  | *Global Object (GO) Definitions---version 03*      |
| NEMA            |                                                    |
|                 | published March 2011                               |
| NTCIP 1201 v03  |                                                    |
+-----------------+----------------------------------------------------+
| AASHTO / ITE /  | *Object Definitions for Actuated Signal            |
| NEMA            | Controllers (ASC) Interface---version 03A*         |
|                 |                                                    |
| NTCIP 1202 v03  | published May 2019                                 |
+-----------------+----------------------------------------------------+
| AASHTO / ITE /  | *Procedures for Creating Management Information    |
| NEMA            | Base (MIB) Files*                                  |
|                 |                                                    |
| NTCIP 8005 v02  | Proposed                                           |
+-----------------+----------------------------------------------------+
| ISO             | *Intelligent transport systems -- Roadside modules |
| 20684-1:2021    | SNMP data interface -- Part 1: Overview* [^2]      |
+-----------------+----------------------------------------------------+
| ISO/IEC         | *Information technology --- Procedures for the     |
| 9834-1:2012     | operation of object identifier registration        |
|                 | authorities: General procedures and top arcs of    |
|                 | the international object identifier tree --- Part  |
|                 | 1:*                                                |
+-----------------+----------------------------------------------------+
| ISO/TS          | *Intelligent transport systems -- Roadside modules |
| 20684-2:2021    | SNMP data interface -- Part 2: Generalized field   |
|                 | device basic management*                           |
+-----------------+----------------------------------------------------+
| ISO/WD 20684-3  | *Intelligent transport systems -- Roadside modules |
|                 | SNMP data interface -- Part 3: Triggers*           |
+-----------------+----------------------------------------------------+
| ISO/WD 20684-4  | *Intelligent transport systems -- Roadside modules |
|                 | SNMP data interface -- Part 4: Notifications*      |
+-----------------+----------------------------------------------------+
| ISO/WD 20684-5  | *Intelligent transport systems -- Roadside modules |
|                 | SNMP data interface -- Part 5: Logs*               |
+-----------------+----------------------------------------------------+
| ITU-T X.660     | *Identical to ISO/IEC 9834-1:2012. Recommended     |
| (07/2011)       | status.*                                           |
+-----------------+----------------------------------------------------+
| ISO/WD 20684-6  | *Intelligent transport systems -- Roadside modules |
|                 | SNMP data interface -- Part 6: Commands*           |
+-----------------+----------------------------------------------------+
| ISO/WD 20684-7  | *Intelligent transport systems -- Roadside modules |
|                 | SNMP data interface -- Part 7: Support Features*   |
+-----------------+----------------------------------------------------+
| NEMA TS_2-2016  | *Traffic Controller Assemblies with NTCIP          |
|                 | Requirements*                                      |
|                 |                                                    |
|                 | 2016                                               |
+-----------------+----------------------------------------------------+

IETF, Generic and Common Textual Conventions (TCs),
<https://trac.ietf.org/trac/ops/wiki/mib-common-tcs>, accessed June 10,
2021

Perkins, D; McGinnis, E., *Understanding SNMP MIBs*, Prentice-Hall,
Inc., 1997, ISBN 0-13-437708-7

Stallings, William, *SNMP, SNMPv2, and CMIP: The Practical Guide to
Network-Management Standards*, Massachusetts, Addison-Wesley Publishing
Company, 1993, ISBN 0-201-63331-0

Larmouth, John, *ASN.1 Complete*, Academic Press, a Harcourt Science and
Technology Company, May 1999, ISBN 0-12233-435-3,
<http://www.oss.com/asn1/booksintro.html> (October 9, 2000)

Dubuisson, Olivier, ASN.1 Communication between Heterogeneous Systems,
June 5, 2000, ISBN 0-12-6333361-0,
<http://www.oss.com/asn1/bookintro.html> (October 9, 2000)

Booch, Grady, Rumbaugh, James, Jacobson, Ivar, *Unified Modeling
Language User Guide*, September 30, 1998, ISBN 0-20157-168-4

*UML basics: An introduction to the Unified Modeling Language,*

[www-106.ibm.com/developerworks/rational/library/769.html#N10090](http://www-106.ibm.com/developerworks/rational/library/769.html#N10090).

### Contact Information 

#### Internet Documents

Obtain Request for Comment (RFC) electronic documents from several
repositories online at:

[www.rfc-editor.org](http://www.rfc-editor.org)

[www.rfc-editor.org/repositories.html](http://www.rfc-editor.org/repositories.html)

#### Architecture Reference for Cooperative and Intelligent Transportation (ARC-IT) 

The Architecture Reference for Cooperative and Intelligent
Transportation (ARC-IT) may be viewed online

at:

<http://local.iteris.com/arc-it/>

ARC-IT is the US ITS reference architecture and includes all content
from the (now deprecated) National

ITS Architecture v7.1 and the Connected Vehicle Reference Implementation
Architecture (CVRIA) v2.2.

#### ISO, IEC, and ISO/IEC Standards

ISO, IEC, and ISO/IEC standards can be purchased on-line in electronic
format or printed copy from:

Techstreet

6300 Interfirst Dr.

Ann Arbor, MI 48108

\(800\) 699-9277

[www.techstreet.com](http://www.techstreet.com)

#### IEEE Standards

IEEE standards can be purchased on-line in electronic format or printed
copy from:

Techstreet

6300 Interfirst Dr.

Ann Arbor, MI 48108

\(800\) 699-9277

[www.techstreet.com](http://www.techstreet.com)

#### NTCIP Standards

Copies of NTCIP standards may be obtained from:

NTCIP Coordinator

National Electrical Manufacturers Association

1300 N.17th Street, Suite 900

Rosslyn, Virginia 22209-3801

[www.ntcip.org](http://www.ntcip.org)

e-mail: <ntcip@nema.org>

Draft amendments, which are under discussion by the relevant NTCIP
Working Group, and amendments recommended by the NTCIP Joint Committee
are available.

## General Statements

\<In the opinion of the responsible NTCIP working group, Section 1.3
does not apply in the context of NTCIP 8004.\>

## Terms

For the purposes of this document, the following terms and definitions
apply. Terms not defined here are used in accordance with their
definitions in ISO/IEC/IEEE 24765. Words not defined here or in
ISO/IEC/IEEE 24765 are used in accordance with their definitions in
*Webster's New Collegiate Dictionary*.

+----------------------+-----------------------------------------------+
| **Term**             | **Definition**                                |
+======================+===============================================+
| **agent**            | The entity that receives requests and         |
|                      | transmits responses to the received requests. |
+----------------------+-----------------------------------------------+
| **block object       | An object type that represents a standardized |
| type**               | data structure of elemental object types.     |
+----------------------+-----------------------------------------------+
| **compatibility**    | The ability of two or more systems or         |
|                      | components to exchange information.           |
|                      |                                               |
|                      | \[ISO/IEC/IEEE 24765\]                        |
+----------------------+-----------------------------------------------+
| **configurable       | An object type that represents a data         |
| object**             | structure that can be configured at run-time  |
|                      | to include elemental object types.            |
+----------------------+-----------------------------------------------+
| **context**          | An instance of a management information base  |
|                      | (MIB).                                        |
|                      |                                               |
|                      | NOTE---A single SNMP agent (e.g., a unique    |
|                      | UDP/IP address) typically represents a single |
|                      | context, but might support multiple contexts  |
|                      | if it, for example, serves as the interface   |
|                      | for multiple field devices (e.g., two dynamic |
|                      | message signs controlled by a single          |
|                      | controller) or serves as a proxy agent for    |
|                      | multiple field devices. When there are        |
|                      | multiple contexts, there might be multiple    |
|                      | object instances with the same object         |
|                      | identifier and the context is used to         |
|                      | disambiguate.                                 |
+----------------------+-----------------------------------------------+
| **current**          | Reflecting the conditions at the present time |
|                      | (or at the time at which the data is time     |
|                      | stamped) as determined by the Controller.     |
|                      | Within the context of a status value,         |
|                      | indicates the most up-to-date design of the   |
|                      | element (e.g., user need, requirement,        |
|                      | object).                                      |
+----------------------+-----------------------------------------------+
| **data**             | Information before it is interpreted.         |
+----------------------+-----------------------------------------------+
| **datagram**         | A self-contained unit of data transmitted     |
|                      | independently of other datagrams.             |
+----------------------+-----------------------------------------------+
| **deprecated**       | A status value that indicates the user need,  |
|                      | requirement, dialog, or object is valid in    |
|                      | limited circumstances, but has been replaced  |
|                      | by another.                                   |
|                      |                                               |
|                      | NOTE---This definition is modified from       |
|                      | "Understanding SNMP MIBS." Procurements can   |
|                      | require support for deprecated objects to     |
|                      | enable multi-version interoperability (e.g.,  |
|                      | backward compatibility) with legacy           |
|                      | implementations.                              |
+----------------------+-----------------------------------------------+
| **file**             | A grouping of data into a single sequence of  |
|                      | bytes that can be referred to by file         |
|                      | operations.                                   |
|                      |                                               |
|                      | NOTE---A file exists nominally in a           |
|                      | directory, and can have an associated path.   |
+----------------------+-----------------------------------------------+
| **intelligent        | The application of advanced information       |
| transportation       | processing and communications, sensing, and   |
| systems (ITS)**      | control technologies to surface               |
|                      | transportation with the objective of          |
|                      | promoting more efficient use of the existing  |
|                      | highway and transportation network,           |
|                      | increasing safety and mobility, and           |
|                      | decreasing environmental impacts.             |
|                      |                                               |
|                      | NOTE---Also known as \"intelligent transport  |
|                      | systems\"                                     |
+----------------------+-----------------------------------------------+
| **International      | An international standards organization.      |
| Organization for     |                                               |
| Standardization      | NOTE---ANSI is the primary interface to ISO   |
| (ISO)**              | within the United States. Often thought to be |
|                      | International Standards Organization, because |
|                      | of its acronym ISO.                           |
+----------------------+-----------------------------------------------+
| **internet**         | A large collection of connected networks,     |
|                      | primarily in the United States, running the   |
|                      | Internet suite of protocols.                  |
|                      |                                               |
|                      | NOTE---Sometimes referred to as the *DARPA    |
|                      | Internet, NSF/DARPA Internet*, or the         |
|                      | *Federal Research Internet.*                  |
+----------------------+-----------------------------------------------+
| **Interchangeable**  | A condition which exists when two or more     |
|                      | items possess such functional and physical    |
|                      | characteristics as to be equivalent in        |
|                      | performance and durability, and are capable   |
|                      | of being exchanged one for the other without  |
|                      | alteration of the items themselves, or        |
|                      | adjoining items, except for adjustment, and   |
|                      | without selection for fit and performance.    |
|                      |                                               |
|                      | Note: See National Telecommunications and     |
|                      | Information Administration, U.S. Department   |
|                      | of Commerce                                   |
+----------------------+-----------------------------------------------+
| **interoperability** | Degree to which two or more systems, products |
|                      | or components can exchange information and    |
|                      | use the information that has been exchanged.  |
|                      |                                               |
|                      | \[ISO/IEC/IEEE 24765\]                        |
+----------------------+-----------------------------------------------+
| **leaf object type** | An object type that does not have any         |
|                      | sub-identifiers assigned (other than for      |
|                      | object instances)                             |
+----------------------+-----------------------------------------------+
| **management         | A structured collection of managed            |
| information base     | information contained within a SNMP context.  |
| (MIB)**              | A MIB represents the instantiated data        |
|                      | objects defined by one or more MIB modules    |
|                      | and integrated into a device or management    |
|                      | station.                                      |
+----------------------+-----------------------------------------------+
| **Management         | The computer system with which the device     |
| Station**            | communicates. Typically, the management       |
|                      | station commands and monitors the device.     |
+----------------------+-----------------------------------------------+
| **MIB module**       | A sequence of NVT ASCII characters conforming |
|                      | to X.208 Abstract Syntax Notation One (ASN.1) |
|                      | and IAB STD 58. MIB modules are used to       |
|                      | define the data objects that are to make up   |
|                      | the instantiated objects of the MIB.          |
|                      |                                               |
|                      | NOTE---A MIB module can be, and within NTCIP  |
|                      | typically is, presented as both part of a     |
|                      | standard and as a stand-alone,                |
|                      | computer-readable text file.                  |
+----------------------+-----------------------------------------------+
| **National           | A family of protocols that provide common     |
| Transportation       | control and data collection services as well  |
| Communications for   | as accommodating various system topologies    |
| ITS Protocol         | and data routing duties.                      |
| (NTCIP)**            |                                               |
|                      | NOTE---NTCIP is designed to support not only  |
|                      | currently deployed systems, but also new      |
|                      | systems and technologies as they become       |
|                      | available.                                    |
+----------------------+-----------------------------------------------+
| **network**          | A collection of devices connected by          |
|                      | intermediate systems and populated by end     |
|                      | systems.                                      |
+----------------------+-----------------------------------------------+
| **notification**     | An unsolicited event message issued by an     |
|                      | SNMP agent for a management station with an   |
|                      | expectation of an acknowledgement.            |
+----------------------+-----------------------------------------------+
| **object**           | An entity identified by a node on the         |
|                      | international object identifier tree.         |
|                      |                                               |
|                      | NOTE -- See object instance and object type,  |
|                      | both of which are types of objects, along     |
|                      | with any other entity that can be identified, |
|                      | such as a standard. This document attempts to |
|                      | use the most precise term within its text to  |
|                      | assist in distinguishing among \"object       |
|                      | type\" or \"object instance\". The use of the |
|                      | term \"object\" is typically limited to       |
|                      | registering items on the international object |
|                      | identifier tree.                              |
+----------------------+-----------------------------------------------+
| **OBJECT             | A unique name (identifier) that is associated |
| IDENTIFIER**         | with each type of object in a MIB that is a   |
|                      | defined ASN.1 type.                           |
+----------------------+-----------------------------------------------+
| **object instance**  | An instance of an object type, which is an    |
|                      | actual instance of data.                      |
|                      |                                               |
|                      | NOTE -- This document avoids using the term   |
|                      | "object" to describe this concept to prevent  |
|                      | any ambiguity with an object referenced by    |
|                      | the international object identifier tree or   |
|                      | an object type.                               |
+----------------------+-----------------------------------------------+
| **object type**      | An abstract specification for a specific      |
|                      | piece of data that can be instantiated within |
|                      | a device (zero or many times depending on how |
|                      | it is specified). It specifies the data using |
|                      | the OBJECT-TYPE macro.                        |
+----------------------+-----------------------------------------------+
| **OBJECT-TYPE**      | An X.208 ASN.1 macro used to define the       |
|                      | meta-attributes of an object type in an SNMP  |
|                      | MIB module.                                   |
+----------------------+-----------------------------------------------+
| **obsolete**         | A status value that indicates the definition  |
|                      | is no longer valid, was found to be flawed,   |
|                      | was redundant, or was not useful.             |
|                      |                                               |
|                      | NOTE---In the next (or some future) edition   |
|                      | of a standard, any element (e.g.,             |
|                      | requirement, object) with a status of         |
|                      | "obsolete" can be removed. This definition is |
|                      | modified from "Understanding SNMP MIBS."      |
+----------------------+-----------------------------------------------+
| **protocol**         | A specific set of rules, procedures, and      |
|                      | conventions defining the format and timing of |
|                      | data transmissions between devices that are   |
|                      | accepted and used to understand each other.   |
+----------------------+-----------------------------------------------+
| **Requirement**      | A requirement describes a condition or        |
|                      | capability to which a system shall conform;   |
|                      | either derived directly from user needs, or   |
|                      | stated in a contract, standard,               |
|                      | specification, or other normative document. A |
|                      | desired feature, property, or behavior of a   |
|                      | system.                                       |
+----------------------+-----------------------------------------------+
| **Requirements       | The ability to follow or study the logical    |
| Traceability**       | progression among the needs, requirements,    |
|                      | and design details in a step-by-step fashion. |
+----------------------+-----------------------------------------------+
| **Simple Network     | A communications protocol developed by the    |
| Management Protocol  | Internet Engineering Task Force (IETF), used  |
| (SNMP)**             | for configuration and monitoring of network   |
|                      | devices.                                      |
+----------------------+-----------------------------------------------+
| **Trap**             | An unsolicited event message issued by an     |
|                      | SNMP agent for a management station without   |
|                      | any expectation of an acknowledgement.        |
+----------------------+-----------------------------------------------+
| **User**             | A person using the system that is developed.  |
+----------------------+-----------------------------------------------+
| **User Need**        | The business or operational problem           |
|                      | (opportunity) that is to be fulfilled to      |
|                      | justify procurement or use.                   |
|                      |                                               |
|                      | Note: While this is termed a "user need"      |
|                      | within the NTCIP community, it reflects needs |
|                      | of all stakeholders.                          |
+----------------------+-----------------------------------------------+

## Abbreviations 

The abbreviations and acronyms used in this document are defined as
follows:

  -------------- --------------------------------------------------------
  **ASCII**      American National Standard Code for Information
                 Interchange

  **ASN.1**      Abstract Syntax Notation One, as defined by either ITU-T
                 X.208 or ITU-T X.680 (ISO/IEC 8824-1) (within the
                 context used, both apply)

  **BER**        Basic Encoding Rules, as defined by ITU-T X.690 (ISO/IEC
                 8825-1)

  **IAB STD**    Internet Architecture Board Standard

  **IANA**       Internet Assigned Numbers Authority

  **IEC**        International Electrotechnical Commission

  **IEEE**       Institute of Electrical and Electronics Engineers

  **IETF**       Internet Engineering Task Force

  **IP**         Internet Protocol

  **ITU-T**      International Telecommunication Union --
                 Telecommunication Standardization Sector

  **MVI**        Multi-Version Interoperability (formerly Backward
                 Compatibility)

  **NVT**        Network Virtual Terminal

  **OER**        Octet Encoding Rules, as defined by ITU-T X.696 (ISO/IEC
                 8825-7)

  **OSI**        Open Systems Interconnection

  **PDU**        Protocol Data Unit

  **PRL**        Protocol Requirements List

  **RFC**        Request for Comments

  **SMI**        Structure and Identification of Management Information

  **SNMP**       Simple Network Management Protocol version 3

  **TCP**        Transport Control Protocol

  **UML**        Unified Modeling Language

  **X.208        Abstract Syntax Notation One, as defined by ITU-T X.208
  ASN.1**        

  **X.680        Abstract Syntax Notation One, as defined by ITU-T X.680
  ASN.1**        (ISO/IEC 8824-1)
  -------------- --------------------------------------------------------

