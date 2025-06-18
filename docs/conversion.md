<!-- markdownlint-enable require-heading-annex -->
<div class="section-2" markdown="1">
<style>
  .section-2 { counter-set: section 2; }
</style>

# Conversion From SMIv1 To SMIv2 \[Normative\] {.annex}

The following defines additional requirements notes that apply to NTCIP
modules being converted from SMIv1 to SMIv2.

1. The value assigned in the SMIv2 `MAX-ACCESS` clause shall be
    consistent with the previous SMIv1 `ACCESS` clause (i.e., it must
    provide greater or equal access)

2. The value assigned in the `MAX-ACCESS` clause shall be `read-create`,
    if the previous `ACCESS` clause indicated `read-write` and the table
    supports row creation

3. The `STATUS` clause shall be updated to reflect the SMIv2 validity of
    the object type rather than the SMIv1 optionality of the object type
    (e.g., change `mandatory` and `optional` to `current`)

4. The `<Units>` subclause from the NTCIP SMIv1 conventions shall be
    converted to the SMIv2 `UNITS` clause

5. Each `TRAP-TYPE` macro shall be converted to a `NOTIFICATION-TYPE` macro
    per the rules of RFC 3584 Clause 2.1.2

6. A `NOTIFICATION-TYPE` that is being converted from an SMIv1 `TRAP-TYPE`
    shall be assigned an object identifier that equates to the
    `TRAP-TYPE`'s `ENTERPRISE` clause followed by a zero and followed by
    the value assigned to the SMIv1 `TRAP-TYPE`.

7. Deprecating object types on the basis of converting to
    IETF-recognized textual conventions (e.g., `INTEGER` to `Gauge32`) is
    encouraged when the textual conventions provide significant
    additional semantics that off-the-shelf tools can benefit from

8. Converting from `Counter` to `Counter32` requires ensuring that the
    semantics defined in RFC 2578 Clause 7.1.6 are satisfied

9. The `SYNTAX` of an object type shall not be changed in a way that
    modifies the data type when encoded using BER or OER. When necessary,
    the existing object can be deprecated and replaced with a new
    object. The following conversions (among others) are prohibited
    based on this rule:

    1. `INTEGER` to `Unsigned32`
    2. `INTEGER` to `Counter32`
    3. `INTEGER` to `Gauge32`
    4. `Counter` to `ZeroBasedCounter32`
    5. `Counter` to `Counter64`
    6. `Counter` to `ZeroBasedCounter64`

10. The counter-based timekeeping solution used by `globalTime` is not
    conformant with SNMPv3 and shall be deprecated. When time-related
    object types need to be defined (e.g., a timestamp), they should be
    based on the textual conventions defined in ISO 20684-1.

11. Developers should consider migrating object types that represent
    general sensor data to the general-purpose input/output feature of
    ISO 20684-2 if and when any backwards compatibility issues arise.

</div>
