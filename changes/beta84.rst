=========================
Changes in Thunderbird 84
=========================

compose
=======

* The :ref:`beginNew <compose.beginNew>` function now has an optional ``messageId`` argument. If
  ``messageId`` is provided, the referenced message is opened to compose as a new message. This
  works for ordinary messages and templates.

  *This change has been backported to Thunderbird 78.7.0.*
  
* Using :ref:`beginForward <compose.beginForward>` function with a ``forwardInline`` type and
  ``details`` argument specified has been fixed.
  
  *This change has been backported to Thunderbird 78.7.0.*
  

menus
=====

* The standard properties available to :ref:`onShown <menus.onShown>` are now available for
  messages being composed, if your extension has the ``compose`` permission.

  *This change has been backported to Thunderbird 78.6.0.*

tabs
====

* At start-up, :ref:`tabs.create <tabs.create>` will now wait for a window to open before
  attempting to open a tab.

  *This change has been backported to Thunderbird 78.5.0.*
 
windows
=======

* The :ref:`windows.openDefaultBrowser` function has been added. 

  *This change has been backported to Thunderbird 78.6.0.*

browserAction
==================================================

* The :ref:`action.setLabel` and :ref:`action.getLabel` functions have been added. It is now possible to set a label value different from the title (which is used as tooltip text). The label can be set to an empty string to make the action button not have a label at all. If the toolbar is set to text-mode only (no icons), the action button label uses the title as fallback, in case an empty label has been set.

  *This change has been backported to Thunderbird 78.6.0.*

composeAction
==================================================

* The :ref:`composeAction.setLabel` and :ref:`composeAction.getLabel` functions have been added. It is now possible to set a label value different from the title (which is used as tooltip text). The label can be set to an empty string to make the action button not have a label at all. If the toolbar is set to text-mode only (no icons), the action button label uses the title as fallback, in case an empty label has been set.

  *This change has been backported to Thunderbird 78.6.0.*

messageDisplayAction
==================================================

* The :ref:`messageDisplayAction.setLabel` and :ref:`messageDisplayAction.getLabel` functions have been added. It is now possible to set a label value different from the title (which is used as tooltip text). The label can be set to an empty string to make the action button not have a label at all. If the toolbar is set to text-mode only (no icons), the action button label uses the title as fallback, in case an empty label has been set.

  *This change has been backported to Thunderbird 78.6.0.*

____

Bugzilla list of fixed WebExtension API defects in `Thunderbird 84 <https://bugzilla.mozilla.org/buglist.cgi?query_format=advanced&f2=target_milestone&component=Add-Ons%3A%20Extensions%20API&resolution=FIXED&o1=equals&product=Thunderbird&columnlist=bug_type%2Cshort_desc%2Cproduct%2Ccomponent%2Cassigned_to%2Cbug_status%2Cresolution%2Cchangeddate%2Ctarget_milestone&v1=defect&f1=bug_type&v2=84%20Branch&o2=equals>`__.
