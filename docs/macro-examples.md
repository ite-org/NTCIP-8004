<!-- markdownlint-enable require-heading-annex -->
<div class="section-3" markdown="1">
<style>
  .section-3 { counter-set: section 3; }
</style>

# Macro Examples \[Informative\] {.annex}

The following examples provide various examples of properly formatted
invocations of the macros discussed by this document.

NOTE---While the macros shown are similar to real invocations, the
details are frequently shortened to save space and the macros often
represent translations of SMIv1 entities for which the indicated SMIv2
translations have not yet been approved. The examples within this annex
are strictly informative and provided as examples, they should not be
interpreted as standardized information. To prevent any confusion, the
formal OIDs in this section are shown with a parent node of \"example\".

## Module Identity Macro {.annex}

```asn1
transportation MODULE-IDENTITY
  LAST-UPDATED \"202212120500Z\"
  ORGANIZATION \"NTCIP BSP2 WG\"
  CONTACT-INFO
    "name: NTCIP Coordinator
     email: ntcip@nema.org
     postal: National Electrical Manufacturers Association
             1300 North 17th Street, Suite 1752
             Rosslyn, VA 22209-3801
             USA"
  DESCRIPTION
    "NEMA delegated its sub-identifier 4 to the Joint Committee on the NTCIP
     with its previously assigned descriptor of \'transportation\'. This MIB
     defines the overall structure of NTCIP-defined management information
     and textual conventions that are believed to be useful for a broad range
     of applications."
  REVISION "202212120500Z"
  DESCRIPTION
    "Updated to SMIv2. Divided module into a separate NEMA managed parent
     module and an NTCIP managed module. Commented out most sub-identifiers,
     so that they can be assigned by the MODULE-IDENTITY macro within other
     NTCIP standards. Formalized textual conventions.\"
  REVISION "200711290000Z"
  DESCRIPTION "Added tmdd and ntcipTraps nodes."
  REVISION "200507190500Z"
  DESCRIPTION 
    "MIB moved into NTCIP 8004 with updated module name and added
     nodes for chap, modem, and tmdd."
  REVISION "200112010500Z"
  DESCRIPTION "NEMA TS 3.2 republished as NTCIP 1101 v01."
  REVISION "199610010500Z"
  DESCRIPTION "NEMA TS 3.2 approved."
::= { example 1}
```

## Object Identity Macro {.annex}

```asn1
protocols OBJECT-IDENTITY
  STATUS current
  DESCRIPTION "This node is the root of a subtree for protocol-related
    management information, such as information related to 1) various layers
    of the protocol stack, 2) profiles that cover several layers, 3) dynamic
    object management, and NTCIP traps."
::= { example 2 }
```

## Conceptual Table Object Type {.annex}

```asn1
phaseTable OBJECT-TYPE
  SYNTAX SEQUENCE OF PhaseEntry
  MAX-ACCESS not-accessible
  STATUS current
  DESCRIPTION
    "<Definition> A table containing Controller Unit phase parameters.
     The number of rows in this table is equal to the maxPhases object.
     <TableType> static
     <Object Identifier> 1.3.6.1.4.1.1206.4.2.x.1.2"
::= { example 3 }
```

## Conceptual Row Object Type {.annex}

```asn1
phaseEntry OBJECT-TYPE
  SYNTAX PhaseEntry
  MAX-ACCESS not-accessible
  STATUS current
  DESCRIPTION
    "<Definition> Parameters for a specific Controller Unit phase.
     <Object Identifier> 1.3.6.1.4.1.1206.4.2.x.1.2.1"
  INDEX { phaseNumber }
::= { example 4 }

PhaseEntry ::= SEQUENCE {
  phaseNumber Integer32,
  phaseWalk Integer32,
  phasePedestrianClear Integer32,
  phaseMinimumGreen Integer32,
  phaseYellowChange Integer32,
  phaseRedClear Integer32 }
```

## Row Status Object Type {.annex}

```asn1
vacmAccessStatus OBJECT-TYPE
  SYNTAX RowStatus
  MAX-ACCESS read-create
  STATUS current
  DESCRIPTION
    "<Definition> The status of this conceptual row.
       The RowStatus TC [RFC2579] requires that this
       DESCRIPTION clause states under which circumstances
       other objects in this row can be modified:
       The value of this object has no effect on whether
       other objects in this conceptual row can be modified.
     <Object Identifier> 1.3.6.1.6.3.16.1.4.1.9"
::= { example 5 }
```

## Enumeration {.annex}

```asn1
dmsMemoryMgmt OBJECT-TYPE
  SYNTAX     INTEGER {
               other (1), -- deprecated
               normal (2),
               clearChangeableMessages (3),
               clearVolatileMessages (4) }
  MAX-ACCESS read-write
  STATUS mandatory
  DESCRIPTION
    "<Definition> Allows the system to manage the device's memory. SNMP
      Get operations on this object should always return normal (2).
      
      clearChangeableMessages (3): the controller shall set dmsMessageStatus
      for all changeable messages to notUsed (1), and release all memory
      associated with changeable messages. This action does not affect any
      changeable graphics or fonts.

      clearVolatileMessages (4): the controller shall set dmsMessageStatus for
      all volatile messages to notUsed (1), and release all memory associated
      with volatile messages. This action does not affect any changeable
      graphics or fonts.

     <Object Identifier> 1.3.6.1.4.1.1206.4.2.3.6.16"
  DEFVAL {normal}
::= { example 6 }
```

## Integer32 {.annex}

```asn1
maxPhases OBJECT-TYPE
  SYNTAX     Integer32 (2..255)
  UNITS      "phase"
  MAX-ACCESS read-only
  STATUS     current
  DESCRIPTION
    "<Definition> The Maximum Number of Phases this Controller Unit
       supports. This object indicates the maximum rows which shall appear in
       the phaseTable object.
     <Object Identifier> 1.3.6.1.4.1.1206.4.2.1.1.1"
::= { example 7 }
```

## Gauge32 {.annex}

```asn1
dcmBatteryVoltage OBJECT-TYPE
  SYNTAX Gauge32 (0..255)
  UNITS "tenths of volts"
  MAX-ACCESS read-only
  STATUS current
  DESCRIPTION
    "<Definition> Indicates the voltage of the battery at the time of the
      request. The value range shall be 00.0-25.5V in 0.1 increments.
     <Object Identifier> 1.3.6.1.4.1.1206.4.2.9.2.2"
::= {example 8}
```

## Counter32 {.annex}

```asn1
dcmVehicleSeqNum OBJECT-TYPE
  SYNTAX Counter32 (0..65535)
  MAX-ACCESS not-accessible
  STATUS current
  DESCRIPTION
    "<Definition> A number assigned to each vehicle that traverses a
      sensor array. The numbers are assigned sequentially over all sensor
      arrays. The starting value is not defined and the value shall roll over
      to a value of 0 after reaching the maximum. This number along with a
      time tag (controller-localTime) is used to uniquely identify vehicles.
     <Object Identifier> 1.3.6.1.4.1.1206.4.9.1.26"
::= {example 9}
```

## Unsigned32 {.annex}

```asn1
dmsSignWidth OBJECT-TYPE
  SYNTAX Unsigned32 (0..65535)
  UNITS "millimeters"
  MAX-ACCESS read-only
  STATUS current
  DESCRIPTION
    "<Definition> Indicates the sign width in millimeters including the
      border (dmsHorizontalBorder).
     <Object Identifier> 1.3.6.1.4.1.1206.4.2.3.1.4"
::= { example 10 }
```

## Object Identifier {.annex}

```asn1
dcmVCOID OBJECT-TYPE
  SYNTAX InstancePointer
  MAX-ACCESS read-only
  STATUS current
  DESCRIPTION
    "<Definition> This field contains the OID of a Vehicle Criteria
      object that is supported by this device. The OID specified must be a
      full OID from the root of the iso tree, relative OID's cannot be used.
      This allows referring to objects outside of this MIB. The specified OID
      can also be an OID from a table (if the object is only defined within a
      table (e.g. Array Number), but it shall be the OID of the object from
      the table in which the specified object is defined (e.g. if Array Number
      is to be used, the OID shall be taken from the Logical IO To Array Map
      Table.
     <Object Identifier> 1.3.6.1.4.1.1206.4.2.3.1.4"
::= {example 11 }
```

## BITS {.annex}

```asn1
systemCameraEquipped OBJECT-TYPE
  SYNTAX     BITS { cameraPower (0),
                    heaterPower (1),
                    wiper (2),
                    washer (3),
                    blower (4) }
  MAX-ACCESS read-only
  STATUS current
  DESCRIPTION
    "<Definition> A bit mapped value as defined below:
      Bit When set, denotes the availability of a controllable:
        0 Camera Power supply,
        1 Heater Power supply,
        2 Wiper,
        3 Washer,
        4 Blower
      All other bits reserved.
     <Object Identifier> 1.3.6.1.4.1.1206.4.2.7.5.3"
::= {example 12}
```

## Internet Address {.annex}

```asn1
intersectionAddressType OBJECT-TYPE
  SYNTAX InetAddressType
  ACCESS read-write
  STATUS current
  DESCRIPTION
    "<Definition> This object identifies the type of address stored in
      intersectionAddress.
     <Object Identifier> 1.3.6.1.4.1.1206.4.2.10.2.2.1.13"
DEFVAL { ipv4 }
::= { example 13 }

intersectionAddress OBJECT-TYPE
  SYNTAX InetAddress
  ACCESS read-write
  STATUS current
  DESCRIPTION
    "<Definition> This object provides the Internet address for the entry
      and shall be a unicast address.
     <Object Identifier> 1.3.6.1.4.1.1206.4.2.10.2.2.1.2"
  DEFVAL { '00000000'h }
::= { example 13 }
```

## Text {.annex}

```asn1
fontName OBJECT-TYPE
  SYNTAX SnmpAdminString (SIZE (0..64))
  MAX-ACCESS read-write
  STATUS current
  DESCRIPTION
    "<Definition> Indicates the name of the font.
     <Object Identifier> 1.3.6.1.4.1.1206.4.2.3.3.2.1.3"
::= { example 14 }
```

## Textual Convention Macro {.annex}

```asn1
MessageActivationCode ::= TEXTUAL-CONVENTION
  DISPLAY-HINT \"2dm1dp1dt2dn2xc1d.1d.1d.1d\"
  STATUS current
  DESCRIPTION
    "The MessageActivationCode consists of those parameters required to
     activate a message on a DMS. It is defined as an OCTET STRING containing
     the OER-encoding of the following ASN.1 structure:

     MessageActivationCodeStructure ::= SEQUENCE {
       duration INTEGER (0..65535),
       activatePriority INTEGER (0..255),
       messageMemoryType INTEGER (0..255),
       messageNumber INTEGER (0..65535),
       messageCRC OCTET STRING (SIZE (2)),
       sourceAddress OCTET STRING (SIZE (4))
       }
     where,
     duration = the maximum amount of time, in minutes, the message may be
     displayed prior to activating the dmsDefaultEndDurationMessage.
     dmsMessageTimeRemaining shall be set to this value upon successful
     display of the indicated message. A value of 65535 shall indicate an
     infinite duration.

     activatePriority = the activation priority of the message. If this value
     is greater than or equal to the dmsMessageRunTimePriority of the
     currently displayed message, the new message shall be displayed unless
     errors are detected.

     messageMemoryType = the dmsMessageMemoryType of the desired message.
     messageNumber = the dmsMessageNumber of the desired message.
     messageCRC = the dmsMessageCRC of the desired message.
     sourceAddress = the 4-byte IPv4 address of the device that requested the 
                     activation.

     For example, given the MULTI string '[jp3]TEST
     \[fl\]Flashing[/fl]\', stored in volatile memory slot 5 with no
     beacons and no pixel service, the message ID Code is '04 00 05 95 F9'.
     If this message is to be displayed for 267 minutes with activation
     priority 55 from IP address 103.8.9.10, the message Activation Code is
     '01 0B 37 04 00 05 95 F9 67 08 09 0A' in hex and would be displayed
     to a user as the following based on the DISPLAY-HINT:
     '267m55p4t5n95F9c103.8.9.10'."
  SYNTAX OCTET STRING (SIZE 12))
```

## Block Object Using Identifier and Type {.annex}

As defined in Section 4.5.4, the definition of a Block Object consists
of two parts:

1. The `OBJECT-TYPE` macro used for all object types and

2. A definition of the data structure using a slightly modified version
    of X.680 ASN.1, as defined in Clause 4.5.4.2; this definition can be
    placed in a `TEXTUAL-CONVENTION`, in the `<Definition>` subclause of
    the `OBJECT-TYPE` macro, or in a location external to the MIB module
    and referenced.

The following uses the textual convention defined in Clause C.15.

```asn1
dmsActivateMessage OBJECT-TYPE
  SYNTAX MessageActivationCode
  MAX-ACCESS read-write
  STATUS current
  DESCRIPTION
    "<Definition> A code indicating the active message. The value of this
      object may be SET by a management station or modified by logic internal
      to the DMS (e.g., activation of the end duration message, etc.).

      When modified by internal logic with a reference to a message ID code,
      the duration indicates 65535 (infinite), the activate priority indicates
      255, and the source address indicates an address of 127.0.0.1.

      If a GET is performed on this object, the DMS shall respond with the
      value for the last message that was successfully activated.

     <Object Identifier> 1.3.6.1.4.1.1206.4.2.3.6.3"
::= { example 16 }
```

## Block Object Using Value Reference and a Defined Value {.annex}

In the following example, because the fields within the ASN.1 structure
are optional, a more meaningful value of DISPLAY-HINT cannot be
provided. As a result, the object type macro references the
ITSOerString.

The reference to \"essNtcipCategory.0\" is an example of a
valuereference that uses a number as an index.
essTemperatureSensorHeight.x\" is an example of a valuereference that
uses a DefinedValue as an index.

```asn1
essStationMetaDataBlock OBJECT-TYPE
  SYNTAX ITSOerString
  MAX-ACCESS read-only
  STATUS current
  DESCRIPTION
    "<Definition> The OER-encoding of the following ASN.1 structure:
        MessageActivationCodeStructure ::= SEQUENCE {
            essNtcipCategory.0 OPTIONAL, -- @NTCIP1204-v03
            essTypeOfStation.0 OPTIONAL, -- @NTCIP1204-v03
            essLatitude.0 OPTIONAL, -- @NTCIP1204-v03
            essLongitude.0 OPTIONAL, -- @NTCIP1204-v03
            tempMetaData SEQUENCE OF TemperatureMetaData OPTIONAL
            }

        TemperatureMetaData ::= SEQUENCE {
            essTemperatureSensorIndex.x OPTIONAL, -- @NTCIP1204-v03
            essTemperatureSensorHeight.x OPTIONAL -- @NTCIP1204-v03
            }

      where,
      x = the essTemperatureSensorIndex for the value being reported
      For example, the following left-hand hexadecimal code would be decoded
      as follows:

      17           All optional fields other than essTypeOfStation are present
      02           Category = \'permanent\'
      02 50 AA 26  Latitude = 38.840870 degrees
      F9 BD 2E AD  Longitude = -105.042259 degrees
      02           Count for SEQUENCE OF = 2
      03           Both optional fields are present
      01           Index = 1
      01           Height for index 1 = 1 meter
      03           Both optional fields are present
      02           Index = 2
      05           Height for index 2 = 5 meters
     <Object Identifier> 1.3.6.1.4.1.1206.4.2.5.2.15.4"
::= { example 17 }
```

## Block Object Using Value Dereferencing {.annex}

In the following example, the fields within the ASN.1 structure are not
known at design time. Since a more meaningful value of DISPLAY-HINT
cannot be provided, the object type macro references the ITSOerString.

The reference to `essNtcipCategory.0` is an example of a
`valuereference` that uses a number as an index.
`essTemperatureSensorHeight.x` is an example of a `valuereference` that
uses a `DefinedValue` as an index.

```asn1
fdObjectGroupCurrentValue OBJECT-TYPE
  SYNTAX ITSOerString
  MAX-ACCESS read-only
  STATUS current
  DESCRIPTION
    "The OER encoded string of the following ASN.1 structure using the
     refinements defined in Clause 4.5.4.2 of NTCIP 8004:
     SEQUENCE {
       *fdObjectGroupFieldObject.x.y.* -- @OBJECT-GROUP-MIB
     }
     where x and y represent the fdObjectGroupOwner and fdObjectGroupName of
     the requested fdObjectGroupCurrentValue.
     
     If an error occurs in retrieving any value, fdObjectGroupLastError shall
     be updated to reflect the reported error and the value of this object
     (fdObjectGroupCurrentValue) shall be a zero-length string. "
  REFERENCE "NTCIP 1103 watchBlockValue"
::= {example 18}
```

## Notification Type Macro {.annex}

```asn1
sampleNotification NOTIFICATION-TYPE
  OBJECTS { sampleObject }
  STATUS current
  DESCRIPTION
    "A sample notification."
::= { example 19 }
```

## Object Group Macro {.annex}

```asn1
essCharacteristicsGroup OBJECT-GROUP
  OBJECTS { essNtcipCategory,
            essNtcipSiteDescription,
            essTypeOfStation,
            essLatitude,
            essLongitude,
            essReferenceHeight }
  STATUS current
  DESCRIPTION
    "Management information that characterizes the ESS."
::= {example 20}
```

## Notification Group Macro {.annex}

```asn1
sampleNotificationGroup NOTIFICATION-GROUP
  NOTIFICATIONS { sampleNotification }
  STATUS current
  DESCRIPTION
    "Notifications included in this document."
::= {example 21}
```

## Module Compliance Macro {.annex}

sampleCompliance MODULE-COMPLIANCE
  STATUS current
  DESCRIPTION
    "The conformance statement for this sample"
  MODULE -- this module
  MANDATORY-GROUPS {
      essCharacteristicsGroup,
      sampleNotificationGroup }
::= {example 22}

</div>