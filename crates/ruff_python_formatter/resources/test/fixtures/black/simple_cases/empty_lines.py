"""Docstring."""


# leading comment
def f():
    SPACE = ' '
    t = leaf.type
    p = leaf.parent  # trailing comment
    v = leaf.value

    if t == token.COMMENT:  # another trailing comment
        return '  '
    assert p is not None, f"INTERNAL ERROR: hand-made leaf without parent: {leaf!r}"


    prev = leaf.prev_sibling
    if not prev:
        prevp = preceding_leaf(p)
        NO = ''
        if not prevp or prevp.type in OPENING_BRACKETS:


            return NO


        if prevp.type == token.EQUAL:
            if prevp.parent and prevp.parent.type in {
                syms.typedargslist,
                syms.varargslist,
                syms.parameters,
                syms.arglist,
                syms.argument,
            }:
                return NO

        elif prevp.type == token.DOUBLESTAR:
            if prevp.parent and prevp.parent.type in {
                syms.typedargslist,
                syms.varargslist,
                syms.parameters,
                syms.arglist,
                syms.dictsetmaker,
            }:
                return NO

###############################################################################
# SECTION BECAUSE SECTIONS
###############################################################################

def g():
    SPACE = ' '
    t = leaf.type
    p = leaf.parent
    v = leaf.value

    if t == token.COMMENT:
        return '  '
    # Another comment because more comments
    assert p is not None, f'INTERNAL ERROR: hand-made leaf without parent: {leaf!r}'

    prev = leaf.prev_sibling
    if not prev:
        prevp = preceding_leaf(p)

        NO = ''
        if not prevp or prevp.type in OPENING_BRACKETS:
            # Start of the line or a bracketed expression.
            # More than one line for the comment.
            return NO

        if (
            prevp.type == token.EQUAL
            and prevp.parent
            and prevp.parent.type
            in {
                syms.typedargslist,
                syms.varargslist,
                syms.parameters,
                syms.arglist,
                syms.argument,
            }
        ):
            return NO
