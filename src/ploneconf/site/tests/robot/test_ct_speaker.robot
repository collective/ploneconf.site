# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s ploneconf.site -t test_speaker.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src ploneconf.site.testing.PLONECONF_SITE_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/ploneconf/site/tests/robot/test_speaker.robot
#
# See the http://docs.plone.org for further details (search for robot
# framework).
#
# ============================================================================

*** Settings *****************************************************************

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
Test Teardown  Close all browsers


*** Test Cases ***************************************************************

Scenario: As a site administrator I can add a speaker
  Given a logged-in site administrator
    and an add speaker form
   When I type 'My speaker' into the title field
    and I submit the form
   Then a speaker with the title 'My speaker' has been created

Scenario: As a site administrator I can view a speaker
  Given a logged-in site administrator
    and a speaker 'My speaker'
   When I go to the speaker view
   Then I can see the speaker title 'My speaker'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add speaker form
  Go To  ${PLONE_URL}/++add++speaker

a speaker 'My speaker'
  Create content  type=speaker  id=my-speaker  title=My speaker

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the speaker view
  Go To  ${PLONE_URL}/my-speaker
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a speaker with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the speaker title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
