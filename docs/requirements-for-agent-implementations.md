<!-- markdownlint-enable require-heading-body -->
<div class="section-5" markdown="1">
<style>
  .section-5 { counter-set: section 5; }
</style>

# Requirements for Agent Implementations \[Normative\]

## Agent Capabilities

Manufacturers supplying transportation equipment should make
AGENT-CAPABILITIES statements available for their equipment. All
manufacturers need to obtain a vendor number from either NEMA or IANA
prior to creating MIB modules that have manufacturer-specific data.

## Requirements for Non-Standard MIBs

All MIB modules shall conform to the basic compilation rules defined for
SMIv2 in addition to the requirements defined within this section.
Developers of non-standard MIB modules are encouraged to adopt the
requirements defined in this document to the extent to which they might
apply.

## Default Values

The value specified in a `DEFVAL` clause should be used when initializing
a new object instance (e.g., during reboot or row creation), if feasible
unless another value is provided. [^63]

## Extensions of Standardized Enumerations

Unless stated otherwise within an object type `<Definition>` subclause,
a `NamedNumber` (i.e., an enumerated item in an enumeration) that is
assigned an identifier of "other" shall be treated as a read-only value.
An attempt to set an object instance to a read-only value shall return
an error (`wrongValue` in the case of SNMPv3).

Unless normative text is added to specifically prohibit the use of the
`other` state, a user- or manufacturer-specific object shall be
permitted to define an object specification that extends the possible
states, For example, NTCIP 1202:2005 includes the following object:

```asn1
coordCorrectionMode OBJECT-TYPE
SYNTAX      INTEGER { other (1),
                      dwell (2),
                      shortway (3),
                      addOnly (4) }
MAX-ACCESS  read-write
STATUS      mandatory
DESCRIPTION
"<Definition> This object defines the Coord Correction
Mode. The possible modes are:
other: the coordinator establishes a new offset by
   a mechanism not defined in this standard.
dwell: when changing offset, the coordinator shall
   establish a new offset by dwelling in the coord
   phase(s) until the desired offset is reached.
shortway (Smooth): when changing offset, the
   coordinator shall establish a new offset by
   adding or subtracting to/from the timings in a
   manner that limits the cycle change. This
   operation is performed in a device specific
   manner.
addOnly: when changing offset, the coordinator
   shall establish a new offset by adding to the
   timings in a manner that limits the cycle
   change. This operation is performed in a device
   specific manner.
...
```

To define a new correction mode, something like the following
proprietary object could be used:

```asn1
xxxCoordCorrectionModeExt OBJECT-TYPE
SYNTAX      INTEGER { other (1),
                      subOnly (2) }
MAX-ACCESS  read-write
STATUS      mandatory
DESCRIPTION
"<Definition> This object defines an extension to the Coord
Correction Mode as defined in NTCIP 1202. The possible modes are:
other: the coordinator establishes a new offset according to
   NTCIP-1202::coordCorrectionMode.
subOnly: when changing offset, the coordinator shall
   establish a new offset by subtracting from the timings in such a
   manner that limits the cycle change. This operation is performed
   in a device specific manner
...
```

In this case, setting `xxxCoordCorrectionModeExt` equal to `subOnly`
forces `coordCorrectionMode` equal to `other`. Setting
`coordCorrectionMode` equal to `shortway` forces
`xxxCoordCorrectionModeExt` equal to `other`.

[^63]: Clause 7.9 of RFC 2578 indicates that implementing the default
    value is optional. This clause makes it recommended.

</div>