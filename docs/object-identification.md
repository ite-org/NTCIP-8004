<!-- markdownlint-enable require-heading-body -->
<div class="section-3" markdown="1">
<style>
  .section-3 { counter-set: section 3; }
</style>

# Object Identification \[Normative\]

SNMP allows managers and agents to implement MIB modules from multiple
independent sources. Allowing this combination of object types presents
a potential for naming conflicts (i.e., two sources defining different
pieces of data using the same name). SNMP overcomes this challenge by
identifying object types using the international object identifier tree,
as defined by the ISO/IEC 9834-1 standard.

## International Object Identifier Tree

The international object identifier tree consists of three root
nodes[^3]. Each root node can be assigned multiple sub-nodes. Each
sub-node may, in turn, have sub-nodes of its own.

Each node, whether a root node or a sub-node, is managed by some
organization. For example, the three root nodes are managed by ISO, the
International Telecommunication Union Telecommunication Standardization
Sector (ITU-T), and jointly by ISO and ITU-T. The manager of any node
may delegate the management responsibility for any sub-node underneath
its branch. In this case, the delegated node is termed a subtree. Just
as any sub-node may have its own set of sub-nodes, subtrees can have
their own subtrees.

Except for the first two root nodes (which are limited to 40 sub-nodes
each), the number of sub-nodes that any node may have is unlimited.
Likewise, the number of sub-node levels is unlimited. As a result, the
international object identifier tree can contain an unlimited number of
nodes using a tree structure managed by multiple organizations.[^4]

### Node Identification

Each node is assigned an integral number and optionally a label. The
label is called the `OBJECT DESCRIPTOR` and provides a user-friendly
textual name that can concisely express what the node is intended to
represent. While the `OBJECT DESCRIPTOR` provides a useful human-language
term to describe the node and should be designed to be unique within the
scope of other sibling nodes of the same branch and level, there is no
guarantee that it is unique within the entire international object
identifier tree. Nonetheless, any node can be uniquely defined by
following the sequence of nodes from the root to the specific node that
needs to be identified. Unfortunately, this can produce a rather lengthy
description since each name might consist of several characters.
Alternatively, the same identifier can be produced by using the integral
numbers assigned to each node rather than the `OBJECT DESCRIPTOR`s. This
representation typically results in a much more compact identifier that
can more easily be processed by computers. This ordered list of integral
values is called an `OBJECT IDENTIFIER`, which is known to identify a
globally unique position on the identifier tree when properly
registered.

The globally unique identifier can be used for any purpose for which an
identifier may be useful. For example, most standards organizations have
been assigned an `OBJECT IDENTIFIER` for the purposes of identification.
The tree can also be used for managing groups of related data. For
example, all objects related to an Actuated Signal Controller are
organized under a node defined as 'asc'. In short, these attributes are
a means for identifying some object, regardless of the semantics
associated with the object.

### Object Identifiers and SNMP

Within SNMP, the international object identifier tree is used to
register object types with globally unique identifiers. The formal
assignment of an `OBJECT IDENTIFIER` to each object type is contained in
the MIB module.

SNMP also identifies object instances by using the international object
identifier tree, but with a slight twist in that the instance portion of
the identifier is only unique within its SNMP agent and context[^5] --
not globally unique. For example, while the MIB provides a globally
unique identifier for the object type of `essAirTemperature`, there might
be multiple environmental sensor stations each containing multiple air
temperature sensors. To identify a specific object instance within a
specific environmental sensor station, SNMP extends the object type
object identifier with an instance identifier (e.g., `essAirTemperature.1`
to identify the reading from the first sensor). However, the instance
value is not unique across different SNMP agents (i.e., every
environmental sensor station will use `essAirTemperature.1` to identify
the reading from its first air temperature sensor). The SNMP manager is
responsible for distinguishing among these readings by combining the
object instance identifier with the network address of the device and
the context used within the message.

## Registered Nodes

### Root Nodes

The first two root nodes of the naming tree are administered by ITU-T
(`itu-t`) and ISO (`iso`). The third node is jointly administered by ISO and
ITU-T (`joint-iso-itu-t`, or sometimes shortened to `joint`).

NOTE---Until 1991, the U.S. name-registration authority conducted its
business under the `{iso(1) member-body(2) us(840)}` arc, registering
names for ANSI standards, private organizations with U.S. national
standing, and the names of U.S. states and "state equivalents." In
1991, changes in the registration authority procedures standard ISO/IEC
9834 (ITU-T X.660) invalidated this procedure, requiring private
organization names with national standing to be registered under the
`{joint-iso-itu-t(2) country(16) us(840)}` arc. The existing register of
private organization names moved, in fact, from the `{1 2 840}` arc to the
`{2 16 840 1}` arc, with ANSI serving as the registration authority.
Therefore, two equivalent prefixes exist (in perpetuity) for currently
registered organization names. Post-1991 registrations are made only
under the `{2 16 840 1}` arc, and organizations with pre-1991
registrations are encouraged (but not required) to construct no new
identifiers under the `{1 2 840}` arc. Various sources provide current OID
descriptions, including
[www.oid-info.com/index.htm](http://www.oid-info.com/index.htm).

NOTE--- The International Telecommunication Union Telecommunication
Standardization Sector (ITU-T) is the part of ITU (an agency of the
United Nations) that provides standards for telecommunication equipment
and systems. The Consultative Committee for International Telephony and
Telegraphy (CCITT) was renamed ITU-T in 1993. The `itu-t(0)` arc is also
named `ccitt` in remembrance that CCITT was previously an organization
independent from ITU-T. Similarly, the `joint-iso-itu-t(2)` arc is also
named `joint-iso-ccitt`.

### NEMA Node

Under the `iso` node, ISO has designated one subtree for use by other
(inter)national organizations (org). Under that subtree, one of the U.S.
National Institute of Standards and Technology nodes is assigned to the
U.S. Department of Defense (dod). The initial development of the
Internet was a Department of Defense project and, therefore, the
Internet community was assigned a node in the `dod` subtree. The Internet
Architecture Board (IAB) administers the `internet` node. The
descriptive name `internet` is defined as:

```asn.1
internet OBJECT IDENTIFIER ::= { iso org dod 1 }
```

(also known as 1.3.6.1)

Because of the ease of obtaining a node from IAB, NEMA requested and
received a node that NEMA administers. This node is defined as:

```asn.1
nema OBJECT IDENTIFIER ::= { iso org dod internet private enterprise 1206 }
```

(also known as 1.3.6.1.4.1.1206)

All NTCIP-defined data related to device data dictionaries or protocols
shall be defined under the NEMA branch of the tree. The organization of
the naming tree down to the `nema` node is shown in Figure 3. The
figure also shows the node for the ITS industry as used by the ISO 20684
standard series.

Portion of ISO Global Tree Showing Location of NEMA Node

The subtree for the NEMA node is shown in Figure 4. The description of
each of the nodes are found in Annex A.1.

[^3]: ISO 9834-1 uses the term "arc" instead of "node".

[^4]: SNMP limits access to the first 2\^32-1 nodes at any one level and to 128 levels, but from a practical perspective, this is still nearly limitless.

[^5]: A context represents a coherent "collection of management information". Often, a physical controller will have a single context, but a single physical controller could control multiple NTCIP devices (e.g., multiple message signs, multiple traffic signals, etc.) and/or serve as a proxy agent to multiple non-NTCIP devices. In this case, each device should be assigned a separate context within the controller so that the management information for each device is kept as distinctly separate instances.

</div>
