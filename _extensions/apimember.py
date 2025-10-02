from docutils import nodes
from docutils.parsers.rst import Directive
from docutils.parsers.rst import directives
from docutils.statemachine import ViewList
from sphinx.util.nodes import nested_parse_with_titles
import uuid

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
        "annotation": directives.unchanged,
        # Api members can get a label (.. _api.func.parameter:),
        # refid is the guessed anchor used by sphinx (api-func-parameter) and
        # refname is the display name for the resolved $(ref:api.func.parameter)
        # in the document.
        "refid": directives.unchanged,
        "refname": directives.unchanged,
        "depth": directives.unchanged,
    }
    
    def run(self):
        nodes_to_return = []

        depth = int(self.options.get('depth', 0))

        if 'refid' in self.options:
            # Create a hidden "title-like" element, for Sphinx to be able to
            # attach a label to (in RST, before the api-member).
            # Use 'name' if available, otherwise fallback to 'refid' for rubric text
            rubric_text = self.options.get('refname', self.options.get('name', self.options['refid']))
            rubric = nodes.rubric(text=rubric_text)
            
            rubric['ids'] = [f"api-member-{uuid.uuid4().hex}"] 
            # Add a custom class so we can hide it via CSS
            rubric['classes'].append('api-member-rubric-hidden')
            nodes_to_return.append(rubric)

        apiMemberNode = nodes.container()
        apiMemberNode['classes'] = ["api-member-node"]
        
        if depth > 0:
            apiMemberNode['classes'].append(f"api-member-depth-{depth}")

        if depth % 2 == 1:
            apiMemberNode['classes'].append("api-member-hide-bullet-point")

        apiMemberDefinition = nodes.container()
        apiMemberDefinition['classes'] = ["api-member-definition"]
        apiMemberDefinition.extend(make_div_node(self, "api-member-bullet", ['-']))

        if 'name' in self.options:
            apiMemberDefinition.extend(make_div_node(self, "api-member-name", [self.options['name']]))
        if 'type' in self.options:
            apiMemberDefinition.extend(make_div_node(self, "api-member-type", [self.options['type']]))
        if 'annotation' in self.options:
            apiMemberDefinition.extend(make_div_node(self, "api-member-annotation", [self.options['annotation']]))

        if 'refid' in self.options:
            link = nodes.reference('', '', internal=True, refid=self.options['refid'])
            link['classes'].append('headerlink')
            para = nodes.paragraph()
            para += link
            apiMemberDefinition.extend([para])

        apiMemberNode.append(apiMemberDefinition)

        if len(self.content) > 0:
            apiMemberDescription = nodes.container()
            apiMemberDescription['classes'] = ["api-member-description"]
            self.state.nested_parse(self.content, self.content_offset, apiMemberDescription)
            apiMemberNode.append(apiMemberDescription)
        
        nodes_to_return.append(apiMemberNode)

        return nodes_to_return


def setup(app):
    app.add_directive("api-member", ApiMemberDirective)

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }