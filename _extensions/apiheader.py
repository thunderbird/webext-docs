from docutils import nodes
from docutils.parsers.rst import Directive
from docutils.parsers.rst import directives
from docutils.statemachine import ViewList
from sphinx.util.nodes import nested_parse_with_titles


def make_div_node(self, classname, lines):
    div = nodes.container()
    div['classes'] = [classname]
    
    rst = ViewList()
    # Add the content one line at a time.
    # Second argument is the filename to report in any warnings
    # or errors, third argument is the line number.
    for line in lines:
        rst.append(line, "make_div.rst", 0)
    # Create a node.
    node = nodes.section()
    node.document = self.state.document
    # Parse the rst.
    nested_parse_with_titles(self.state, rst, node)        

    div.extend(node)
    return [div]
    
class ApiHeaderDirective(Directive):

    optional_arguments = 1
    final_argument_whitespace = False
    has_content = True
    option_spec = {
        "label": directives.unchanged_required,
        "annotation": directives.unchanged_required
    }
        
    def run(self):
        ApiHeaderNode = nodes.container()
        ApiHeaderNode['classes'] = ["api-header-node"]

        ApiHeaderSection = nodes.container()
        ApiHeaderSection['classes'] = ["api-header-section"]
        if 'label' in self.options:
            ApiHeaderSection.extend(make_div_node(self, "api-header-label", [self.options['label']]))
        if 'annotation' in self.options:
            ApiHeaderSection.extend(make_div_node(self, "api-header-annotation", [self.options['annotation']]))
        ApiHeaderNode.append(ApiHeaderSection)

        self.state.nested_parse(self.content, self.content_offset, ApiHeaderNode)
        
        return [ApiHeaderNode]


def setup(app):
    app.add_directive("api-header", ApiHeaderDirective)

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }