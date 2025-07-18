use ruff_python_ast::{self as ast, Stmt};

use ruff_macros::{ViolationMetadata, derive_message_formats};
use ruff_python_ast::identifier::Identifier;

use crate::Violation;
use crate::checkers::ast::Checker;

/// ## What it does
/// Checks for docstrings that are written via f-strings.
///
/// ## Why is this bad?
/// Python will interpret the f-string as a joined string, rather than as a
/// docstring. As such, the "docstring" will not be accessible via the
/// `__doc__` attribute, nor will it be picked up by any automated
/// documentation tooling.
///
/// ## Example
/// ```python
/// def foo():
///     f"""Not a docstring."""
/// ```
///
/// Use instead:
/// ```python
/// def foo():
///     """A docstring."""
/// ```
///
/// ## References
/// - [PEP 257 – Docstring Conventions](https://peps.python.org/pep-0257/)
/// - [Python documentation: Formatted string literals](https://docs.python.org/3/reference/lexical_analysis.html#f-strings)
#[derive(ViolationMetadata)]
pub(crate) struct FStringDocstring;

impl Violation for FStringDocstring {
    #[derive_message_formats]
    fn message(&self) -> String {
        "f-string used as docstring. Python will interpret this as a joined string, rather than a docstring.".to_string()
    }
}

/// B021
pub(crate) fn f_string_docstring(checker: &Checker, body: &[Stmt]) {
    let Some(stmt) = body.first() else {
        return;
    };
    let Stmt::Expr(ast::StmtExpr {
        value,
        range: _,
        node_index: _,
    }) = stmt
    else {
        return;
    };
    if !value.is_f_string_expr() {
        return;
    }
    checker.report_diagnostic(FStringDocstring, stmt.identifier());
}
