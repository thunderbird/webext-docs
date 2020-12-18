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
    
class ApiMemberDirective(Directive):

    optional_arguments = 0
    final_argument_whitespace = False
    has_content = True
    option_spec = {
        "type": directives.unchanged,
        "name": directives.unchanged,
        "annotation": directives.unchanged
    }
        
    def run(self):
        apiMemberNode = nodes.container()
        apiMemberNode['classes'] = ["api-member-node"]

        apiMemberDefinition = nodes.container()
        apiMemberDefinition['classes'] = ["api-member-definition"]
        apiMemberDefinition.extend(make_div_node(self, "api-member-bullet", ['-']))

        if 'name' in self.options:
            apiMemberDefinition.extend(make_div_node(self, "api-member-name", [self.options['name']]))
        if 'type' in self.options:
            apiMemberDefinition.extend(make_div_node(self, "api-member-type", [self.options['type']]))
        if 'annotation' in self.options:
            apiMemberDefinition.extend(make_div_node(self, "api-member-annotation", [self.options['annotation']]))
        apiMemberNode.append(apiMemberDefinition)

        if len(self.content) > 0:
            apiMemberDescription = nodes.container()
            apiMemberDescription['classes'] = ["api-member-description"]
            self.state.nested_parse(self.content, self.content_offset, apiMemberDescription)
            apiMemberNode.append(apiMemberDescription)
        
        return [apiMemberNode]


def setup(app):
    app.add_directive("api-member", ApiMemberDirective)

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }