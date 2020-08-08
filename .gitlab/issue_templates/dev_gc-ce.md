# Developer Task [General Corrections-Code Affecting]
*Issue template for general code corrections that may affect calls. This is for tasks that are not specifically related to any issue.*

## Cause for Correction:
*Why should this be corrected?*

## Summary of Correction:
*Put a brief description of your issue here.*

### File(s) Affected:
*Here you can enter a list of files in dot-form that are affected by this change.*

 - nude_man.lib.config   

#### Calls Changed:
*What internal program calls/attributes changed as a result of this*
 - nude_man.lib.config.start_config() -> nude_man.lib.config.Config().start()

#### Calls Added:
*What calls are added?*
 - nude_man.lib.config.Config().write()

#### Calls Removed:
*What calls are deprecated?*
- nude_man.lib.config.start_config() (See 'Calls Changed')


## Task Checklist:
*What do you need to do to complete this task?*
 - [ ] Write docstrings
 - [ ] Make correction
 - [ ] Etc
   - [ ] Etc

## Additional Comments:
*Any additional information that might help troubleshoot this issue?*


/label ~dev-task
/cc @tayjaybabee
/assign @tayjaybabee
/confidential
