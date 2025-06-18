<!-- markdownlint-enable require-heading-annex -->
<div class="section-1" markdown="1">
<style>
  .section-1 { counter-set: section 1; }
</style>

# NTCIP Structure of Management Information (SMI) \[Normative\] {.annex}

Annex A defines the overall structure of the NTCIP-defined management
information and several textual conventions that are believed to be
useful for a broad range of applications. The text provided in Annex A.1
constitutes the standard NTCIP8004-NemaV1 MIB. Annex A.2 (except the
headings) constitutes the standard NTCIP8004-TransportationV1 MIB.

## NEMA Module {.annex}

```asn1
NTCIP8004-NEMA DEFINITIONS ::= BEGIN

IMPORTS
  MODULE-IDENTITY, OBJECT-IDENTITY, enterprises
                                                 FROM SNMPv2-SMI;
                                                   -- RFC 2578

nema MODULE-IDENTITY
  LAST-UPDATED "202212120500Z"
  ORGANIZATION "NTCIP BSP2 WG"
  CONTACT-INFO
    "name:    NTCIP Coordinator
     email:   ntcip@nema.org
     postal:  National Electrical Manufacturers Association
              1300 North 17th Street, Suite 1752
              Rosslyn, VA 22209-3801
              USA"
  DESCRIPTION 
    "IANA delegated sub-identifier 1206 under the enterprise node to NEMA
     This MIB defines the overall structure of management information 
     that is believed to be useful for a broad range of applications."
  REVISION     "202212120500Z"
  DESCRIPTION  
    "Updated to SMIv2. Divided module into a separate NEMA managed parent 
     module and an NTCIP managed module. "
  REVISION     "200507190500Z"
  DESCRIPTION  "MIB moved into NTCIP 8004 with updated module name."
  REVISION     "200112010500Z"
  DESCRIPTION  "NEMA TS 3.2 republished as NTCIP 1101 v01."
  REVISION     "199610010500Z"
  DESCRIPTION  "NEMA TS 3.2 approved."
  ::= { enterprises 1206 }

nemaMgmt                OBJECT-IDENTITY
  STATUS      current
  DESCRIPTION "The mgmt subtree is used for standard NEMA object definitions 
    that span different NEMA sections."
  ::=  { nema 1 }

nemaExperimental        OBJECT-IDENTITY
  STATUS      current
  DESCRIPTION "The experimental subtree is used to identify object types used 
    only on an experimental basis. Changing OBJECT IDENTIFIERs once assigned     
    is challenging due to an installed base. Thus, this node should only be 
    used for experiments, such as research efforts that are strictly limited 
    to be short-term projects to investigate and test ideas. More permanent 
    node assignments should be obtained prior to any longer-term or larger-
    scale deployment to prevent complications if, and when, the solution 
    becomes more widely adopted."
  ::=  { nema 2 }

expGlobal OBJECT-IDENTITY 
  STATUS  deprecated
  DESCRIPTION
    "<Definition> A node that contains the experimental auxiliary 
     input/output objects.
     <Object Identifier> 1.3.6.1.4.1.1206.2.2"
::= {nemaExperimental 2} 

nemaPrivate             OBJECT-IDENTITY
  STATUS      current
    DESCRIPTION
"The private subtree is used to identify object types defined unilaterally. NEMA assigns nodes to enterprises for purposes such as defining enterprise-specific MIB modules. A request for a node assignment can be sent to the NTCIP Coordinator at ntcip@nema.org. When a sub-node is assigned, the responsibility for managing that sub-node is transferred to the enterprise making the request.

   Upon receiving a node, the enterprise may, for example, define new MIB modules and object types under this node. In addition, it is strongly recommended that the enterprise also register its transportation devices under this subtree, to provide an unambiguous identification mechanism for use in management protocols. For example, if the 'ABC, Inc.' enterprise produced transportation devices, then it could request a node under the nemaPrivate node from NEMA. Such a node might be numbered: 1.3.6.1.4.1.1206.3.99

   The 'ABC, Inc.' enterprise might then register their 'Widget Controller' under the name of 1.3.6.1.4.1.1206.3.99.1, ensuring a unique identification. Thereafter, each enterprise is responsible for ensuring unique identification of information objects within their subtree. NEMA delegates the role of assigning numbers under each nemaPrivate node to those to which they are assigned, except of course for the initial enterprise number."
  ::= { nema 3 }

END -- NTCIP8004-NEMA
```

## Transportation Module {.annex}

```asn1
NTCIP8004-Transportation DEFINITIONS ::= BEGIN

IMPORTS
  MODULE-IDENTITY, OBJECT-IDENTITY, Integer32
                                                 FROM SNMPv2-SMI
                                                   -- RFC 2578
  TEXTUAL-CONVENTION
                                                 FROM SNMPv2-TC
                                                   -- RFC 2579
  nema
                                                 FROM NTCIP8004-NEMA;

transportation MODULE-IDENTITY
  LAST-UPDATED "202212120500Z"
  ORGANIZATION "NTCIP BSP2 WG"
  CONTACT-INFO
    "name:    NTCIP Coordinator
     email:   ntcip@nema.org
     postal:  National Electrical Manufacturers Association
              1300 North 17th Street, Suite 1752
              Rosslyn, VA 22209-3801
              USA"
  DESCRIPTION 
    "NEMA delegated its sub-identifier 4 to the Joint Committee on the NTCIP 
     with its previously assigned descriptor of 'transportation'. This MIB 
     defines the overall structure of NTCIP-defined management information 
     and textual conventions that are believed to be useful for a broad range 
     of applications."
  REVISION     "202212120500Z"
  DESCRIPTION  
    "Updated to SMIv2. Divided module into a separate NEMA managed parent 
     module and an NTCIP managed module. Commented out most sub-identifiers, 
     so that they can be assigned by the MODULE-IDENTITY macro within other 
     NTCIP standards. Formalized textual conventions."
  REVISION     "200711290000Z"
  DESCRIPTION  "Added tmdd and ntcipTraps nodes."
  REVISION     "200507190500Z"
  DESCRIPTION  "MIB moved into NTCIP 8004 with updated module name and added
                nodes for chap, modem, and tmdd."
  REVISION     "200112010500Z"
  DESCRIPTION  "NEMA TS 3.2 republished as NTCIP 1101 v01."
  REVISION     "199610010500Z"
  DESCRIPTION  "NEMA TS 3.2 approved."
  ::= { nema 4 }

-- A.2.1	Nodal Structure
protocols         OBJECT-IDENTITY
  STATUS      current
  DESCRIPTION "This node is the root of a subtree for protocol-related 
    management information, such as information related to 1) various layers 
    of the protocol stack, 2) profiles that cover several layers, 3) dynamic 
    object management, and NTCIP traps."
  ::=  { transportation 1 }

devices           OBJECT-IDENTITY
  STATUS      current
  DESCRIPTION 
    "<Definition> This node is the root of a subtree for management 
     information for various transportation devices. Management of this node 
     is delegated to the NTCIP Base Standards, Protocols, and Profiles (BSP2) 
     WG.
     <Informative> The following assignments have been made under this node 
     as formally declared (or to be declared upon upgrade to SMIv2) in the 
     indicated standard:
     Node   descriptor    Defined in
      1     asc           NTCIP 1202 
      2     ramp          NTCIP 1207
      3     dms           NTCIP 1203
      4     tss           NTCIP 1209
      5     ess           NTCIP 1204
      6     global        NTCIP 1201
      7     cctv          NTCIP 1205
      8     cctvSwitch    NTCIP 1208
      9     dcm           NTCIP 1206
     10     ssm           NTCIP 1210
     11     scp           NTCIP 1211
     12     networkCamera <reserved>
     13     elms          NTCIP 1213
     17     saeNtcip      NTCIP 1202
     18     rsu           NTCIP 1218
     19     globalV2      NTCIP 1201"
  ::=  { transportation 2 }


tcip              OBJECT-IDENTITY
  STATUS      current
  DESCRIPTION "This node has been assigned to the Transit Communications 
    Interface Profiles Technical Working Group. Assignment of any nodes under 
    this subtree is delegated to that group."
  ::=  { transportation 3 }

tmdd              OBJECT-IDENTITY
  STATUS      current
  DESCRIPTION "This node has been assigned to the ITE Traffic Management Data 
    Dictionary Steering Committee. Assignment of any nodes under this subtree 
    is delegated to that group."
  ::=  { transportation 4 }

deviceAdmin    OBJECT-IDENTITY
  STATUS      current
  DESCRIPTION "This node has been assigned for the definition of 
    administrative data that is related to the other other nodes under the 
    transportation node. Its sub-node structure is intended to parallel that 
    of the transporation node."
  ::=  { devices 126 }

-- **************************************************************************
-- Protocols branch of tree
-- **************************************************************************
layers            OBJECT-IDENTITY
  STATUS      current
  DESCRIPTION 
    "<Definition> This node contains management information related to 
     various layers of the OSI protocol stack. 
     <Informative> The following subnodes have 
     been defined:
     Node  Descriptor
1     chap
2     modem 
7     application"
  ::=  { protocols 1 }

application       OBJECT-IDENTITY
  STATUS      current
  DESCRIPTION "This node contains management information related to 
    protocols assigned to the application layer of the OSI stack."
  ::=  { layers 7 }

profiles          OBJECT-IDENTITY
  STATUS      current
  DESCRIPTION "This node contains management information related to profiles 
    that cover several layers of the OSI stack."
  ::=  { protocols 2 }

ntcipSmi          OBJECT-IDENTITY
  STATUS      current
  DESCRIPTION "A node used to manage information related to the NTCIP SMI."
  ::= { protocols 5 }
 
-- A.2.2	Common Textual Conventions
-- MIB developers should use textual conventions to the extent possible so 
-- that 1) associated semantics can be automated and code easily reused, and 
-- 2) generic SNMP implementations are guided on how to present values to 
-- users. The following lists/defines several textual conventions that are 
-- most widely used. The list also includes some of the APPLICATION types 
-- defined in RFC 2578 for a more complete reference set.
-- MIB developers are also encouraged to consider the textual conventions 
-- listed at https://trac.ietf.org/trac/ops/wiki/mib-common-tcs, which is 
-- maintained with all IETF defined conventions. 
-- **************************************************************************
-- Integers
-- **************************************************************************
-- "Byte", "Ubyte", "Short", "Ushort", and "Long" were defined in 
-- NTCIP8004v02, but have identical ranges to the following defined textual
-- conventions defined in ISO 20684-1, which should be used instead
-- From FIELD-DEVICE-TC-MIB
-- @ https://standards.iso.org/iso/20684/-1/ed-2/en/iso20684-1-tc.mib
--      ITSInteger8:      Replaces NTCIP8004v02 "Byte"
--      ITSInteger16:     Replaces NTCIP8004v02 "Short"  
--      ITSPositive8  
--      ITSPositive16 
--      ITSPositive32
--      ITSUnsigned8:     Replaces NTCIP8004v02 "Ubyte"  
--      ITSUnsigned16:    Replaces NTCIP8004v02 "Ushort"
-- From SNMPv2-SMI
-- @ RFC 2578
--      Integer32:        Replaces NTCIP8004v02 "Long" and "INTEGER", both
--                        of which have identical ranges
--      Unsigned32
NtcipPercent   ::= TEXTUAL-CONVENTION
  DISPLAY-HINT "d"
  STATUS       deprecated
  DESCRIPTION  
   "<Definition> An expression of a percentage from 0 to 100 contained in 
    an Integer32 type. 
   <Informative> This textual convention is defined to support values 
    converted from the SNMPv1 INTEGER type; new objects should use 
    ITSPercent as defined in ISO 20684-1, which is based on Unsigned32."
  SYNTAX       Integer32 (0..100)


-- **************************************************************************
-- Counters and Gauges
-- **************************************************************************
-- From FIELD-DEVICE-TC-MIB
-- @ https://standards.iso.org/iso/20684/-1/ed-2/en/iso20684-1-tc.mib
--      ITSCounter8:       8-bit, zero-based, resetable
--      ITSCounter16:     16-bit, zero-based, resetable  
--      ITSCounter32:     32-bit, zero-based, resetable  
--      ITSCounter64:     64-bit, zero-based, resetable  
--      ITSGauge8:         8-bit gauge
--      ITSGauge16:       16-bit gauge
-- From SNMPv2-SMI
-- @ RFC 2578
--      Counter32         32-bit, random base, non-resetable
--      Counter64         64-bit, random base, non-resetable
--      Gauge32           32-bit gauge
-- From RMON2-MIB
-- @ RFC 2021
--      ZeroBasedCounter32   32-bit, zero-based, non-resetable
-- From HCNUM-TC
-- @ RFC 2856
--      ZeroBasedCounter64   64-bit, zero-based, non-resetable
--      CounterBasedGauge64  64-bit gauge
-- **************************************************************************
-- Date/Time
-- **************************************************************************
-- From FIELD-DEVICE-TC-MIB 
-- @ https://standards.iso.org/iso/20684/-1/ed-2/en/iso20684-1-tc.mib 
--      ITSDailyTimeStamp
--      ITSDateStamp
--      ITSDayOfMonth
--      ITSDayOfWeek
--      ITSMonth
-- **************************************************************************
-- Other Enumerations
-- **************************************************************************
-- From SNMPv2-TC
-- @ RFC 2579
--      TruthValue
--      TestAndIncr
--      RowStatus
--      StorageType
-- From FIELD-DEVICE-TC-MIB 
-- @ https://standards.iso.org/iso/20684/-1/ed-2/en/iso20684-1-tc.mib 
--      ITSPduErrorStatus
--      ITSUnits

NtcipRowStatusStatic   ::= TEXTUAL-CONVENTION
  STATUS       deprecated
  DESCRIPTION  
    "<Definition>RowStatusStatic has four states and two commands associated 
     with it. 
     <Format> The four possible states are defined as:
     1) other: The status is controlled or defined by a user- or 
          manufacturer-specific object.
     2) standby: All columnar data in the row have passed (any) defined 
          consistency checks but are not to be used by the end application.
     3) available: All columnar data in the row have passed (any) defined
          consistency checks and are available to be used by the end 
          application.
     4) invalid: One or more columnar objects has a value that caused the 
          row to fail at least one defined consistency check. 

     Setting RowStatusStatic equal to one of the above values shall return 
     an error (e.g., 'wrongValue' in SNMPv3).

     The only two possible command values that may be set by a management 
     application are: 
     5) activate: Makes the columnar data in the row available for use by 
          the end application.
     6) deactivate: Makes the columnar data in the row unavailable for use 
          by the end application.

     <Informative> In a static table, all rows exist irrespective of whether 
     the columnar objects contain appropriate values. The value of a 
     columnar object within a row may be inappropriate when the values of 
     other columnar objects in the row are considered. An entire row itself 
     may also be considered inappropriate under some circumstances. If this 
     is the case, a static table shall include an additional columnar object 
     that defines row status and has the SYNTAX of RowStatusStatic. 

     UML state transition diagrams for RowStatusStatic are defined in NTCIP 
     8004.

     RowStatusStatic was deprecated in NTCIP8004v03.01 in favor of RowStatus, 
     which allows implementations to create rows when needed and to destroy 
     them when not needed. This allows the potential for better memory 
     management in implementations that wish to provide this capability."
  SYNTAX       INTEGER                    { other (1),                      standby (2),                      available (3),
                     invalid (4), 
                     activate (5),
                     deactivate (6)}


-- **************************************************************************
-- Bitmaps 
-- **************************************************************************
-- New objects should use "BITS", unless 1) there is a need to conserve the
-- extra bits and 2) there is confidence that the object will never need to 
-- expand to a larger value. 
NtcipOctetBitmap8   ::= TEXTUAL-CONVENTION
  DISPLAY-HINT "1x"
  STATUS       current
  DESCRIPTION  
   "<Definition> A bitmap of up to 8 bits with Bit 0 in the low-order bit. 
      When a bit is on (1), the indicated feature is on or supported; when a 
      bit is off (0), the indicated feature is off or not supported.
    <Informative> This object orders the bits in the reverse order of the 
    BITS construct but in the same order as used by INTEGERs."
  SYNTAX       OCTET STRING (SIZE (1))

NtcipOctetBitmap16   ::= TEXTUAL-CONVENTION
  DISPLAY-HINT "1x "
  STATUS       current
  DESCRIPTION  
   "<Definition>A bitmap of up to 16 bits with Bit 0 in the low-order bit of 
      the trailing octet and Bit 15 in the high-order bit of the first octet. 
      When a bit is on (1), the indicated feature is on or supported; when a 
      bit is off (0), the indicated feature is off or not supported.
    <Informative> This object orders the bits in the reverse order of the 
    BITS construct but in the same order as used by INTEGERs."
  SYNTAX       OCTET STRING (SIZE (2))

NtcipOctetBitmap32   ::= TEXTUAL-CONVENTION
  DISPLAY-HINT "1x "
  STATUS       deprecated
  DESCRIPTION  
   "<Definition>A bitmap of up to 32 bits with Bit 0 in the low-order bit of 
      the trailing octet and Bit 31 in the high-order bit of the first octet. 
      When a bit is on (1), the indicated feature is on or supported; when a 
      bit is off (0), the indicated feature is off or not supported.

    <Informative>This has been deprecated in favor of the SNMP-standard BITS 
      construct, which orders the bits in the reverse order and allows for 
      growth in a bit field."
  SYNTAX       OCTET STRING (SIZE (4))

NtcipOctetBitmap512   ::= TEXTUAL-CONVENTION
  DISPLAY-HINT "1x "
  STATUS       deprecated
  DESCRIPTION  
   "<Definition>A bitmap of up to 512 bits (64 octets) with the meaning of 
      bits defined by the object type but in no case shall there be more than
      seven pad bits (i.e., the length of the octet string may be less than 
      64 octets). 
      
      When a bit is set (1), the indicated feature/error is on, active,
      supported (as defined by the object using this textual convention);
      when a bit is not set (0), the indicated feature/error is off, not 
      active, or not supported.

    <Informative>This has been deprecated in favor of the SNMP-standard BITS 
      construct, which orders the bits in the reverse order and allows for 
      growth in a bit field."
  SYNTAX       OCTET STRING (SIZE (0..64))

NtcipOctetBitmap2040   ::= TEXTUAL-CONVENTION
  DISPLAY-HINT "1x "
  STATUS       deprecated
  DESCRIPTION  
   "<Definition>A bitmap of up to 2040 bits (255 octets) with the meaning of
      bits defined by the object type but in no case shall there be more than
      seven pad bits (i.e., the length of the octet string may be less than 
      255 octets). 
      
      When a bit is set (1), the indicated feature/error is on, active,
      supported (as defined by the object using this textual convention);
      when a bit is not set (0), the indicated feature/error is off, not 
      active, or not supported.

    <Informative>This has been deprecated in favor of the SNMP-standard BITS 
      construct, which orders the bits in the reverse order and allows for 
      growth in a bit field."
  SYNTAX       OCTET STRING (SIZE (0..255))

NtcipOctetBitmap3200   ::= TEXTUAL-CONVENTION
  DISPLAY-HINT "1x "
  STATUS       deprecated
  DESCRIPTION  
   "<Definition>A bitmap of up to 3200 bits (400 octets) with the meaning of
      bits defined by the object type but in no case shall there be more than
      seven pad bits (i.e., the length of the octet string may be less than 
      400 octets). 
      
      When a bit is set (1), the indicated feature/error is on, active,
      supported (as defined by the object using this textual convention);
      when a bit is not set (0), the indicated feature/error is off, not 
      active, or not supported.

    <Informative>This has been deprecated in favor of the SNMP-standard BITS 
      construct, which orders the bits in the reverse order and allows for 
      growth in a bit field."
  SYNTAX       OCTET STRING (SIZE (1..400))

NtcipIntegerBitmap8   ::= TEXTUAL-CONVENTION
  DISPLAY-HINT "x"
  STATUS       current
  DESCRIPTION  
   "<Definition> A bitmap of up to 8 bits with Bit 0 in the low-order bit. 
    <Informative> This object orders the bits in the reverse order of the 
    BITS construct but in the same order as used by INTEGERs."
  SYNTAX       Integer32 (0..255)

NtcipIntegerBitmap16   ::= TEXTUAL-CONVENTION
  DISPLAY-HINT "x"
  STATUS       current
  DESCRIPTION  
   "<Definition>A bitmap of up to 16 bits with Bit 0 in the low-order bit of 
      the trailing octet. 
    <Informative> This object orders the bits in the reverse order of the 
    BITS construct but in the same order as used by INTEGERs."
  SYNTAX       Integer32 (0..65535)

NtcipIntegerBitmap31   ::= TEXTUAL-CONVENTION
  DISPLAY-HINT "x"
  STATUS       deprecated
  DESCRIPTION  
   "<Definition>A bitmap of up to 31 bits with Bit 0 in the low-order bit of 
      the trailing octet. 
    <Informative>This has been deprecated in favor of the SNMP-standard BITS 
      construct, which orders the bits in the reverse order and allows for 
      growth in a bit field. Prior versions of NTCIP sometimes indicated a 
      value for Bit 31 (i.e., the high-order bit) with an unsigned range on 
      INTEGER; this was a technically invalid definition and resulted in 
      ambiguities as to whether it should be encoded in 4 octets (which is 
      technically a signed value, or 5 octets, which many off-the-shelf SNMP 
      engines do not support. As a result, implementation response to a value 
      that uses Bit 31 is undefined and should be avoided."
  SYNTAX       Integer32 

-- **************************************************************************
-- Text 
-- **************************************************************************
-- From SNMP-FRAMEWORK-MIB
-- @ RFC 3411
--      SnmpAdminString: UTF8 String 0..255 octets 

NtcipOwnerString   ::= TEXTUAL-CONVENTION
  DISPLAY-HINT "127t"
  STATUS       deprecated
  DESCRIPTION  
   "<Definition>This data type is used to model an administratively assigned 
      name of the owner of a resource, preferably in human-readable form.
      The string is encoded in UTF-8. It is suggested that this name contain
      one or more of the following: management station name, manager’s name,
      location or phone number.
    <Informative> Versions prior to 2023 limited this textual convention to 
      the NVT ASCII character set; however, the range was expanded to allow 
      for more language support and UTF-8 is fully compatible with NVT
      ASCII. This textual convention has been deprecated as there is seldom a
      need to force a limit of 127 characters (as this convention does)
      rather than 255 characters (as SnmpAdminString does). "
  SYNTAX       OCTET STRING (SIZE (0..127)) 

-- **************************************************************************
-- Other OCTET STRING conventions
-- **************************************************************************
-- From FIELD-DEVICE-TC-MIB 
-- @ https://standards.iso.org/iso/20684/-1/ed-1/en/iso20684-1-1-a.mib
--      ITSOerString
NtcipTwoColors  ::= TEXTUAL-CONVENTION
  DISPLAY-HINT  "1dR1dG1dB1dR1dG1dB"
  STATUS  current
  DESCRIPTION
  "A 6-octet value representing two colors, each encoded as a 3-octet RGB
    value."
  SYNTAX  OCTET STRING (SIZE(6))

-- **************************************************************************
-- OBJECT IDENTIFIER conventions
-- **************************************************************************
-- From SNMPv2-TC
-- @ RFC 2579
--      AutonomousType
--      VariablePointer
--      RowPointer

END -- NTCIP8004-Transportation 
```

</div>
