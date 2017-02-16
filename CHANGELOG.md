# Change Log

## [2.0.0](https://github.com/muccg/rdrf/tree/2.0.0) (2017-02-16)
[Full Changelog](https://github.com/muccg/rdrf/compare/1.7.15...2.0.0)

**Implemented enhancements:**

- Adds possibility to order follow up forms by their name. [\#410](https://github.com/muccg/rdrf/issues/410)
- Patient delete [\#409](https://github.com/muccg/rdrf/issues/409)
- settings: add DATA\_UPLOAD\_MAX\_NUMBER\_FIELDS [\#408](https://github.com/muccg/rdrf/issues/408)
- Clean up questionnaire response view [\#407](https://github.com/muccg/rdrf/issues/407)
- questionnaire view: make auth checks more defensive [\#406](https://github.com/muccg/rdrf/issues/406)
- Remove unused admin templates [\#405](https://github.com/muccg/rdrf/issues/405)
- Remove FEATURES setting [\#404](https://github.com/muccg/rdrf/issues/404)
- remove unused views [\#403](https://github.com/muccg/rdrf/issues/403)
- admin: add user active and password expiry to list display [\#402](https://github.com/muccg/rdrf/issues/402)
- Clinical conversion from mongo to sql database [\#401](https://github.com/muccg/rdrf/issues/401)
- settings: Use Django settings, not env directly [\#382](https://github.com/muccg/rdrf/issues/382)
- If test zips are bad in some way - bail out of aloe tests early [\#371](https://github.com/muccg/rdrf/issues/371)
- The users should be warned that their password will expire soon [\#369](https://github.com/muccg/rdrf/issues/369)
- Make it obvious why the user has been deactivated  [\#368](https://github.com/muccg/rdrf/issues/368)
- Read the django-useraudit settings in from environment variables [\#367](https://github.com/muccg/rdrf/issues/367)
- Allow ordering of follow up forms by chronological order [\#366](https://github.com/muccg/rdrf/issues/366)
- Enable patient archiving \(soft deletion\) and hard deletion for admin [\#365](https://github.com/muccg/rdrf/issues/365)

**Fixed bugs:**

- DataError at /explorer/query/download/12/download [\#391](https://github.com/muccg/rdrf/issues/391)
- Error redirecting after deleting \(archiving\) a patient [\#389](https://github.com/muccg/rdrf/issues/389)
- Error creating  a patient from a Questionnaire Response [\#388](https://github.com/muccg/rdrf/issues/388)
- ValueError at /admin/rdrf/questionnaireresponse/ [\#386](https://github.com/muccg/rdrf/issues/386)
- AttributeError at /DM1/questionnaire/ [\#385](https://github.com/muccg/rdrf/issues/385)
- TypeError at /patientslisting [\#384](https://github.com/muccg/rdrf/issues/384)
- RegistryRouter: fix connections may not be iterable, remove same db [\#383](https://github.com/muccg/rdrf/issues/383)
- Error running data migration for cdefile [\#380](https://github.com/muccg/rdrf/issues/380)
- Field size for registry form name on cde file model too small [\#377](https://github.com/muccg/rdrf/issues/377)

**Closed issues:**

- Modjgo management command converted dates to isostrings  [\#393](https://github.com/muccg/rdrf/issues/393)
- django-useraudit 1.4.0 [\#356](https://github.com/muccg/rdrf/issues/356)
- django-iprestrict 1.1.1 [\#351](https://github.com/muccg/rdrf/issues/351)
- django 1.10.5 [\#350](https://github.com/muccg/rdrf/issues/350)

## [1.7.15](https://github.com/muccg/rdrf/tree/1.7.15) (2017-01-16)
[Full Changelog](https://github.com/muccg/rdrf/compare/1.7.14...1.7.15)

**Closed issues:**

- django-useraudit 1.4.0 [\#357](https://github.com/muccg/rdrf/issues/357)
- django-iprestrict 1.1.1 for rdrf 1.7.15 [\#355](https://github.com/muccg/rdrf/issues/355)

## [1.7.14](https://github.com/muccg/rdrf/tree/1.7.14) (2016-12-07)
[Full Changelog](https://github.com/muccg/rdrf/compare/1.7.13...1.7.14)

**Fixed bugs:**

- TypeError at /\<REG\>/register/ [\#348](https://github.com/muccg/rdrf/issues/348)

## [1.7.13](https://github.com/muccg/rdrf/tree/1.7.13) (2016-12-06)
[Full Changelog](https://github.com/muccg/rdrf/compare/1.7.12...1.7.13)

**Fixed bugs:**

- Misconfigured reverse url lookup in menu [\#347](https://github.com/muccg/rdrf/issues/347)
- Questionnaire error template syntax error [\#346](https://github.com/muccg/rdrf/issues/346)

## [1.7.12](https://github.com/muccg/rdrf/tree/1.7.12) (2016-12-06)
[Full Changelog](https://github.com/muccg/rdrf/compare/1.7.11...1.7.12)

**Implemented enhancements:**

- Top-left title action should take user to appropriate home page [\#337](https://github.com/muccg/rdrf/issues/337)
- Top-left title should be customizable  [\#336](https://github.com/muccg/rdrf/issues/336)
- Consistent container width across all pages [\#342](https://github.com/muccg/rdrf/issues/342)
- Additional RDRF URLs in menu [\#341](https://github.com/muccg/rdrf/issues/341)
- Add error message on unsuccessful login attempt  [\#340](https://github.com/muccg/rdrf/issues/340)
- Menu cleanup [\#338](https://github.com/muccg/rdrf/issues/338)

**Fixed bugs:**

- Fix for upgraded registration redux [\#333](https://github.com/muccg/rdrf/issues/333)

**Closed issues:**

- Remove 'Support' and 'Report a bug' from the footer [\#335](https://github.com/muccg/rdrf/issues/335)
- Remove 'dash' icon from menu items [\#339](https://github.com/muccg/rdrf/issues/339)

## [1.7.11](https://github.com/muccg/rdrf/tree/1.7.11) (2016-11-28)
[Full Changelog](https://github.com/muccg/rdrf/compare/1.7.10...1.7.11)

**Implemented enhancements:**

- pyparsing==2.1.10 [\#332](https://github.com/muccg/rdrf/issues/332)
- polib==1.0.8 [\#331](https://github.com/muccg/rdrf/issues/331)
- SQLAlchemy==1.0.16 [\#330](https://github.com/muccg/rdrf/issues/330)
- djangorestframework==3.5.3 [\#328](https://github.com/muccg/rdrf/issues/328)
- django-registration-redux==1.4 [\#327](https://github.com/muccg/rdrf/issues/327)
- django-anymail==0.6.1 [\#326](https://github.com/muccg/rdrf/issues/326)
- version lock django-ajax-selects==1.5.2 [\#325](https://github.com/muccg/rdrf/issues/325)
- iprestrict 1.1.0 [\#324](https://github.com/muccg/rdrf/issues/324)
- Management command to trigger form progress recalculation [\#322](https://github.com/muccg/rdrf/issues/322)

**Fixed bugs:**

- models: realign RegistryForm.position [\#323](https://github.com/muccg/rdrf/issues/323)

**Closed issues:**

- fh custom field file save form error \(modjgo branch\) [\#321](https://github.com/muccg/rdrf/issues/321)
- Key error on save patient demographics ID [\#320](https://github.com/muccg/rdrf/issues/320)

## [1.7.10](https://github.com/muccg/rdrf/tree/1.7.10) (2016-11-21)
[Full Changelog](https://github.com/muccg/rdrf/compare/1.7.9...1.7.10)

**Closed issues:**

- Data Import Script [\#318](https://github.com/muccg/rdrf/issues/318)

## [1.7.9](https://github.com/muccg/rdrf/tree/1.7.9) (2016-11-08)
[Full Changelog](https://github.com/muccg/rdrf/compare/1.7.8...1.7.9)

**Fixed bugs:**

- 'NoneType' object has no attribute 'pk' [\#294](https://github.com/muccg/rdrf/issues/294)

**Closed issues:**

- explorer download error [\#313](https://github.com/muccg/rdrf/issues/313)

## [1.7.8](https://github.com/muccg/rdrf/tree/1.7.8) (2016-11-02)
[Full Changelog](https://github.com/muccg/rdrf/compare/1.7.7...1.7.8)

**Implemented enhancements:**

- settings: LOGIN\_FAILURE\_LIMIT [\#309](https://github.com/muccg/rdrf/issues/309)
- django 1.10.3 [\#308](https://github.com/muccg/rdrf/issues/308)

**Fixed bugs:**

- template error rdrf/explorer/templates/explorer/query\_download.htm [\#307](https://github.com/muccg/rdrf/issues/307)
- Edit password of user in Admin screen \( by admin\) gives 404 [\#306](https://github.com/muccg/rdrf/issues/306)

## [1.7.7](https://github.com/muccg/rdrf/tree/1.7.7) (2016-11-01)
[Full Changelog](https://github.com/muccg/rdrf/compare/1.7.6...1.7.7)

**Implemented enhancements:**

- Clean up user group membership test [\#302](https://github.com/muccg/rdrf/issues/302)

**Fixed bugs:**

- Email notification error [\#304](https://github.com/muccg/rdrf/issues/304)
- Fix NoReverseMatch exception on main registry page [\#303](https://github.com/muccg/rdrf/issues/303)
- NoReverseMatch at /admin/useraudit/loginattempt/ \(django-useraudit==1.3.3\) [\#298](https://github.com/muccg/rdrf/issues/298)

## [1.7.6](https://github.com/muccg/rdrf/tree/1.7.6) (2016-10-31)
[Full Changelog](https://github.com/muccg/rdrf/compare/1.7.5...1.7.6)

**Fixed bugs:**

- csrf failure on dd live site after 1.7.5 deploy [\#301](https://github.com/muccg/rdrf/issues/301)

## [1.7.5](https://github.com/muccg/rdrf/tree/1.7.5) (2016-10-27)
[Full Changelog](https://github.com/muccg/rdrf/compare/1.7.4...1.7.5)

**Fixed bugs:**

- ValueError at /admin/rdrf/registryform/add/ Cannot force an update in save\(\) with no primary key. [\#296](https://github.com/muccg/rdrf/issues/296)

**Closed issues:**

- missing migration prod \( settings dependant model field\) [\#295](https://github.com/muccg/rdrf/issues/295)

## [1.7.4](https://github.com/muccg/rdrf/tree/1.7.4) (2016-10-25)
[Full Changelog](https://github.com/muccg/rdrf/compare/1.7.3...1.7.4)

**Implemented enhancements:**

- Get rid of system check complain about '/reactivate' URL [\#285](https://github.com/muccg/rdrf/issues/285)

**Fixed bugs:**

- Demographics field \(upload family pedigree\) file upload not uploading file  [\#292](https://github.com/muccg/rdrf/issues/292)

**Closed issues:**

- Styling of 'delete' button  [\#287](https://github.com/muccg/rdrf/issues/287)

## [1.7.3](https://github.com/muccg/rdrf/tree/1.7.3) (2016-10-24)
[Full Changelog](https://github.com/muccg/rdrf/compare/1.7.2...1.7.3)

**Fixed bugs:**

- develop.sh MacOS compatibility [\#286](https://github.com/muccg/rdrf/issues/286)

**Closed issues:**

- develop.sh: macos compatability [\#289](https://github.com/muccg/rdrf/issues/289)
- patient listing module drop down [\#288](https://github.com/muccg/rdrf/issues/288)

## [1.7.2](https://github.com/muccg/rdrf/tree/1.7.2) (2016-10-21)
[Full Changelog](https://github.com/muccg/rdrf/compare/1.7.1...1.7.2)

**Fixed bugs:**

- Django 1.10: Revert a render\_to\_response → render [\#284](https://github.com/muccg/rdrf/issues/284)

## [1.7.1](https://github.com/muccg/rdrf/tree/1.7.1) (2016-10-18)
[Full Changelog](https://github.com/muccg/rdrf/compare/1.7.0...1.7.1)

**Implemented enhancements:**

- account lockout event [\#283](https://github.com/muccg/rdrf/issues/283)

## [1.7.0](https://github.com/muccg/rdrf/tree/1.7.0) (2016-10-17)
[Full Changelog](https://github.com/muccg/rdrf/compare/1.6.10...1.7.0)

**Fixed bugs:**

- Import of fh failed with runtime error [\#274](https://github.com/muccg/rdrf/issues/274)
- reexport\_test\_zips fails with error [\#282](https://github.com/muccg/rdrf/issues/282)
- runtests fail because migrations invoked against reporting test database \( which is in fact the main db\) [\#279](https://github.com/muccg/rdrf/issues/279)
- Spurious AddressType of POST gets created as side effect in base registration module [\#278](https://github.com/muccg/rdrf/issues/278)
- Javascript error in report explorer [\#277](https://github.com/muccg/rdrf/issues/277)
- Modules drop down not appearing on next\_release for fh import [\#273](https://github.com/muccg/rdrf/issues/273)

**Closed issues:**

- recreate test zips after schema change [\#281](https://github.com/muccg/rdrf/issues/281)
- refs to removed smtp container in yamls [\#280](https://github.com/muccg/rdrf/issues/280)

## [1.6.10](https://github.com/muccg/rdrf/tree/1.6.10) (2016-10-07)
[Full Changelog](https://github.com/muccg/rdrf/compare/1.6.9...1.6.10)

**Fixed bugs:**

- referebce data not being created \(AddressTypes\) on inital site load [\#271](https://github.com/muccg/rdrf/issues/271)
- CDE status fixes [\#270](https://github.com/muccg/rdrf/issues/270)

## [1.6.9](https://github.com/muccg/rdrf/tree/1.6.9) (2016-10-03)
[Full Changelog](https://github.com/muccg/rdrf/compare/1.6.8...1.6.9)

**Fixed bugs:**

- consents unicode error  [\#261](https://github.com/muccg/rdrf/issues/261)

## [1.6.8](https://github.com/muccg/rdrf/tree/1.6.8) (2016-09-29)
[Full Changelog](https://github.com/muccg/rdrf/compare/1.6.7...1.6.8)

**Fixed bugs:**

- Yaml export/import - 'information text' in 'Consent section' is not retained [\#250](https://github.com/muccg/rdrf/issues/250)

**Closed issues:**

- SERVER\_EMAIL define twice [\#258](https://github.com/muccg/rdrf/issues/258)
- configurable selenium timeout [\#257](https://github.com/muccg/rdrf/issues/257)

## [1.6.7](https://github.com/muccg/rdrf/tree/1.6.7) (2016-09-23)
[Full Changelog](https://github.com/muccg/rdrf/compare/1.6.6...1.6.7)

**Implemented enhancements:**

- Updated django-useraudit to 1.3.0 [\#249](https://github.com/muccg/rdrf/issues/249)
- gender choices for ParentGuardian [\#247](https://github.com/muccg/rdrf/issues/247)
- Create utility script to re-export test zipfiles [\#240](https://github.com/muccg/rdrf/issues/240)
- Registry export: if there is just one registry in the system default to that [\#239](https://github.com/muccg/rdrf/issues/239)
- Make registry yaml export more suitable for diffing/merging [\#234](https://github.com/muccg/rdrf/issues/234)
- \[RDR-1395\] Configurable file storage backend [\#214](https://github.com/muccg/rdrf/issues/214)

**Fixed bugs:**

- dynamic\_data: fix variable referenced before assignment [\#248](https://github.com/muccg/rdrf/issues/248)
- AccountLockout emails not being sent [\#246](https://github.com/muccg/rdrf/issues/246)
- Problems with display of download links of File CDEs in multisections [\#243](https://github.com/muccg/rdrf/issues/243)
- \[RDR-1432\] File cde download link not appearing after upload in post view [\#219](https://github.com/muccg/rdrf/issues/219)
- \[RDR-1396\] Show original unmunged filename for consent form file uploads [\#213](https://github.com/muccg/rdrf/issues/213)

**Closed issues:**

- Re-export the lettuce zip files [\#241](https://github.com/muccg/rdrf/issues/241)

## [1.6.6](https://github.com/muccg/rdrf/tree/1.6.6) (2016-09-13)
[Full Changelog](https://github.com/muccg/rdrf/compare/1.6.5...1.6.6)

**Fixed bugs:**

- Wrong name assigned to parent's user object [\#237](https://github.com/muccg/rdrf/issues/237)

## [1.6.5](https://github.com/muccg/rdrf/tree/1.6.5) (2016-09-09)
[Full Changelog](https://github.com/muccg/rdrf/compare/1.6.4...1.6.5)

## [1.6.4](https://github.com/muccg/rdrf/tree/1.6.4) (2016-08-31)
[Full Changelog](https://github.com/muccg/rdrf/compare/1.6.3...1.6.4)

**Implemented enhancements:**

- Added registry\_version template tag [\#229](https://github.com/muccg/rdrf/issues/229)

**Closed issues:**

- \[RDR-1285\] DM1 regression - create patient failed due to index error in set\_context [\#227](https://github.com/muccg/rdrf/issues/227)
- \[RDR-1306\] fh.yaml has   ====  in calcs [\#226](https://github.com/muccg/rdrf/issues/226)
- \[RDR-1236\] merge in latest from rdrf 1.2 series into Angelman [\#225](https://github.com/muccg/rdrf/issues/225)
- \[RDR-1237\] Admin can't re-activate 'inactive' user [\#223](https://github.com/muccg/rdrf/issues/223)
- \[RDR-1435\] Recreate test zips  [\#221](https://github.com/muccg/rdrf/issues/221)
- \[RDR-1322\] DM1- password reset email needs site changed [\#212](https://github.com/muccg/rdrf/issues/212)
- \[RDR-1379\] report not saving edit to sql query [\#209](https://github.com/muccg/rdrf/issues/209)
- \[RDR-1366\] Navigation through 'next, back' arrows needs to navigate through all Forms [\#206](https://github.com/muccg/rdrf/issues/206)
- \[RDR-1413\] Password reset not working on FH live site- server error reported on site, but error email is not sent to RDRF. [\#205](https://github.com/muccg/rdrf/issues/205)
- \[RDR-1299\] Add email and phone number to ClinicianOther model [\#204](https://github.com/muccg/rdrf/issues/204)
- \[RDR-1296\] Implement management command to load sets of initial data [\#203](https://github.com/muccg/rdrf/issues/203)
- \[RDR-1313\] questionnaire PatientCentres datasource error [\#202](https://github.com/muccg/rdrf/issues/202)
- \[RDR-1315\] FH- adjusting calculations to pass validation [\#199](https://github.com/muccg/rdrf/issues/199)
- \[RDR-1222\] Report Datatable improvements [\#52](https://github.com/muccg/rdrf/issues/52)
- \[RDR-1224\] Spreadsheet Report [\#51](https://github.com/muccg/rdrf/issues/51)
- \[RDR-1298\] charts js error [\#46](https://github.com/muccg/rdrf/issues/46)
- Remove all registration templates [\#228](https://github.com/muccg/rdrf/issues/228)

## [1.6.3](https://github.com/muccg/rdrf/tree/1.6.3) (2016-08-23)
[Full Changelog](https://github.com/muccg/rdrf/compare/1.6.2...1.6.3)

**Closed issues:**

- \[RDR-1436\] Importer: --force doesn't work on schema version mismatch [\#186](https://github.com/muccg/rdrf/issues/186)
- \[RDR-1419\] DD Add Patient test fails with integrity error [\#185](https://github.com/muccg/rdrf/issues/185)
- \[RDR-1420\] Add patient integrity error after export / import [\#184](https://github.com/muccg/rdrf/issues/184)
- \[RDR-1421\] Django 1.8.14 [\#183](https://github.com/muccg/rdrf/issues/183)
- \[RDR-1415\] FH export - import fails because a Section missing  [\#182](https://github.com/muccg/rdrf/issues/182)
- \[RDR-1361\] Create some lettuce features and steps  [\#181](https://github.com/muccg/rdrf/issues/181)
- \[RDR-1417\] FH steps need implementing [\#180](https://github.com/muccg/rdrf/issues/180)
- \[RDR-1414\] regression after 1.6 merge into next\_release Location contains link to form group in 1.6 \( it shouldn't\) [\#179](https://github.com/muccg/rdrf/issues/179)
- \[RDR-1418\] Mongo restore error [\#178](https://github.com/muccg/rdrf/issues/178)
- \[RDR-1416\] FH export import fails because cdes collection populated on patient creation [\#177](https://github.com/muccg/rdrf/issues/177)
- \[RDR-1354\] TypeError at /fh/patient/ - patient handler should not be accessible by FH, returns server error on live site. Should return 404 error.  [\#176](https://github.com/muccg/rdrf/issues/176)
- \[RDR-1427\] psycopg2 2.6.2 [\#175](https://github.com/muccg/rdrf/issues/175)
- \[RDR-1430\] Consent form checkbox help text is squashed to right of form [\#174](https://github.com/muccg/rdrf/issues/174)
- \[RDR-1431\] AttributeError: 'AnonymousUser' object has no attribute 'is\_patient' [\#173](https://github.com/muccg/rdrf/issues/173)
- \[RDR-1429\] Fix remaining feature files in line with the implementation of the steps [\#172](https://github.com/muccg/rdrf/issues/172)
- \[RDR-1425\] DoesNotExist at /ang/forms/60/25/18 \#119 [\#171](https://github.com/muccg/rdrf/issues/171)
- \[RDR-1424\] Form Print Button url is missing context id [\#170](https://github.com/muccg/rdrf/issues/170)
- \[RDR-1385\] Regression in DM1 questionnaire after fkrp/angelman merge [\#169](https://github.com/muccg/rdrf/issues/169)
- \[RDR-1426\] Required CDEs for progress indicator' to be renamed 'Progress on this page' \(like FKRP\) \#116 [\#168](https://github.com/muccg/rdrf/issues/168)
- \[RDR-1434\] Lettuce tests: get rid of automatic acceptance of alert boxes [\#167](https://github.com/muccg/rdrf/issues/167)
- \[RDR-1433\] Form with calculated field is detected as changed even if no fields are changed [\#166](https://github.com/muccg/rdrf/issues/166)
- \[RDR-1422\] Error in FH live site -TypeError: get\(\) got an unexpected keyword argument 'context\_id' [\#165](https://github.com/muccg/rdrf/issues/165)

## [1.6.2](https://github.com/muccg/rdrf/tree/1.6.2) (2016-08-23)
[Full Changelog](https://github.com/muccg/rdrf/compare/1.6.1...1.6.2)

## [1.6.1](https://github.com/muccg/rdrf/tree/1.6.1) (2016-08-19)
[Full Changelog](https://github.com/muccg/rdrf/compare/1.6.0...1.6.1)

## [1.6.0](https://github.com/muccg/rdrf/tree/1.6.0) (2016-08-18)
[Full Changelog](https://github.com/muccg/rdrf/compare/1.5.8...1.6.0)

## [1.5.8](https://github.com/muccg/rdrf/tree/1.5.8) (2016-08-02)
[Full Changelog](https://github.com/muccg/rdrf/compare/1.5.7...1.5.8)

**Closed issues:**

- \[RDR-1384\] Import from spreadsheet failed on live site [\#163](https://github.com/muccg/rdrf/issues/163)
- \[RDR-1401\] Grid errors [\#162](https://github.com/muccg/rdrf/issues/162)
- \[RDR-1353\] Fix lettuce tests [\#161](https://github.com/muccg/rdrf/issues/161)
- \[RDR-1403\] buttons on patient listing expanded \( on staging\) [\#160](https://github.com/muccg/rdrf/issues/160)
- \[RDR-1337\] Remove support/doco for RPM generation is no longer being maintained [\#159](https://github.com/muccg/rdrf/issues/159)
- \[RDR-1350\] pymongo 2.9.3 [\#158](https://github.com/muccg/rdrf/issues/158)
- \[RDR-1349\] When runtime error occurs in questionnaire handling the error message can't be returned because of a name error  [\#157](https://github.com/muccg/rdrf/issues/157)
- \[RDR-1326\] patient edit link on new questionnaire approval form broken [\#156](https://github.com/muccg/rdrf/issues/156)
- \[RDR-1348\] Python dependency upgrades [\#155](https://github.com/muccg/rdrf/issues/155)
- \[RDR-1347\] Getting import error importing the live Dm1\_nz yaml file into dev [\#154](https://github.com/muccg/rdrf/issues/154)
- \[RDR-1324\] Javascript error in importer \( doesn't prevent import though\) [\#153](https://github.com/muccg/rdrf/issues/153)
- \[RDR-1397\] some grid columns display NA  [\#152](https://github.com/muccg/rdrf/issues/152)
- \[RDR-1402\] Import of new FH yaml file created another Checkup form group [\#151](https://github.com/muccg/rdrf/issues/151)
- \[RDR-1409\] FH new patient doesn't set currency of clinical form despite setting index field [\#150](https://github.com/muccg/rdrf/issues/150)
- \[RDR-1389\] Patient listing to show only one row per patient with form drop down showing all links to all forms \( in fixed and multiple form groups \) [\#149](https://github.com/muccg/rdrf/issues/149)
- \[RDR-1408\] AttributeError at /DM1/questionnaire/nz [\#148](https://github.com/muccg/rdrf/issues/148)
- \[RDR-1375\] Move custom permissions and grid configuration out of settings [\#147](https://github.com/muccg/rdrf/issues/147)
- \[RDR-1374\] Make User validation more relaxed [\#146](https://github.com/muccg/rdrf/issues/146)
- \[RDR-1373\] Patient Listing Page - handle edge cases better [\#145](https://github.com/muccg/rdrf/issues/145)
- \[RDR-1406\] FH doesn't have form progress CDEs defined but 0% progress number appears in form dropdown [\#144](https://github.com/muccg/rdrf/issues/144)
- \[RDR-1370\] upgrade iprestrict [\#143](https://github.com/muccg/rdrf/issues/143)
- \[RDR-1376\] handle admin login [\#142](https://github.com/muccg/rdrf/issues/142)
- \[RDR-1380\] some float columns are being presented with empty strings on insert causing fails [\#141](https://github.com/muccg/rdrf/issues/141)
- \[RDR-1338\] Create new yaml file for FH context groups [\#140](https://github.com/muccg/rdrf/issues/140)
- \[RDR-1372\] Can add additional 'Main' form group by clicking on hyperlink to 'Main' from a clinical form [\#139](https://github.com/muccg/rdrf/issues/139)
- \[RDR-1371\] 'FH report' on live site is only exporting 30 patients \(109 in patient list\) [\#138](https://github.com/muccg/rdrf/issues/138)
- \[RDR-1290\] FH Form Links on sidebar broken [\#137](https://github.com/muccg/rdrf/issues/137)
- \[RDR-1280\] DM1 Regression: Create patient failed in questionnaire [\#136](https://github.com/muccg/rdrf/issues/136)
- \[RDR-1284\] Regression - Family Linkage operation fails [\#135](https://github.com/muccg/rdrf/issues/135)
- \[RDR-1287\] Sidebar on the multiple form group edit \( or add\) page appears on the right [\#134](https://github.com/muccg/rdrf/issues/134)
- \[RDR-1286\] Form Navigation Corrections [\#133](https://github.com/muccg/rdrf/issues/133)
- \[RDR-1288\] Family Linkage page not using same template as main forms [\#132](https://github.com/muccg/rdrf/issues/132)
- \[RDR-1292\] The list of forms in the "Fixed" context for FH is showing the FollowUp form link [\#131](https://github.com/muccg/rdrf/issues/131)
- \[RDR-1291\] The dropdown of forms in the patient listing is incorrect for fixed form group Main in FH [\#130](https://github.com/muccg/rdrf/issues/130)
- \[RDR-1283\] Family Linkage screen links [\#129](https://github.com/muccg/rdrf/issues/129)
- \[RDR-1293\] Family Linkage page not initialised with index [\#128](https://github.com/muccg/rdrf/issues/128)
- \[RDR-1282\] DM1 regression: update of existing patient fails [\#127](https://github.com/muccg/rdrf/issues/127)
- \[RDR-1294\] Regression - FH - Create patient from relative fails [\#126](https://github.com/muccg/rdrf/issues/126)
- \[RDR-1358\] remove references to django suits [\#125](https://github.com/muccg/rdrf/issues/125)
- \[RDR-1339\] docker 1.11 docker-compose 1.7.1 [\#124](https://github.com/muccg/rdrf/issues/124)
- \[RDR-1399\] Ensure  form group names don't appear for FH [\#123](https://github.com/muccg/rdrf/issues/123)
- \[RDR-1400\] Exporter does not export naming cde on context form group [\#122](https://github.com/muccg/rdrf/issues/122)
- \[RDR-1377\] Ordering on patient listing not correct with addition of 'checkup' form to existing patients [\#121](https://github.com/muccg/rdrf/issues/121)
- \[RDR-1398\] New Follow Up forms can't be "cancelled" [\#120](https://github.com/muccg/rdrf/issues/120)
- \[RDR-1378\] Reports are not reporting properly - missing patients, missing data [\#119](https://github.com/muccg/rdrf/issues/119)
- \[RDR-1316\] storages branch has issue with FH saving demographics [\#118](https://github.com/muccg/rdrf/issues/118)
- \[RDR-1352\] base image update - pip 8.1.2 [\#117](https://github.com/muccg/rdrf/issues/117)
- \[RDR-1382\] Styling on the report table view  page has altered slightly [\#116](https://github.com/muccg/rdrf/issues/116)
- \[RDR-1383\] LaboratoryLookupWidget no longer looking up laboratories [\#115](https://github.com/muccg/rdrf/issues/115)
- \[RDR-1363\] ip restrict vars for settings [\#114](https://github.com/muccg/rdrf/issues/114)
- \[RDR-1364\] FH Mongo splitting script does not update contexts for patients without mongo data [\#113](https://github.com/muccg/rdrf/issues/113)
- \[RDR-1365\] TemplateSyntaxError at /fh/consent [\#112](https://github.com/muccg/rdrf/issues/112)
- \[RDR-1368\] stack trace [\#111](https://github.com/muccg/rdrf/issues/111)
- \[RDR-1367\] TemplateSyntaxError at /reset/OQ/4de-fb368361167f24cf1337/ [\#110](https://github.com/muccg/rdrf/issues/110)
- \[RDR-1362\] django root logger [\#109](https://github.com/muccg/rdrf/issues/109)
- \[RDR-1390\] django mailgun deprecated - replace with anymail [\#108](https://github.com/muccg/rdrf/issues/108)
- \[RDR-1388\] The display name of a followup should come from the date of assessment cde [\#107](https://github.com/muccg/rdrf/issues/107)
- \[RDR-1391\] Modify launcher component to show Add Followup link directly  [\#106](https://github.com/muccg/rdrf/issues/106)
- \[RDR-1359\] remove js/css cdns [\#105](https://github.com/muccg/rdrf/issues/105)
- \[RDR-1387\] Skip showing the context view with attached form links in the followup form creation workflow [\#104](https://github.com/muccg/rdrf/issues/104)
- \[RDR-1258\] upgrading python dependencies [\#103](https://github.com/muccg/rdrf/issues/103)
- \[RDR-1357\] deprecate django-secure [\#102](https://github.com/muccg/rdrf/issues/102)
- \[RDR-1405\] Patient grid ordering by name doesn't suborder by first name [\#101](https://github.com/muccg/rdrf/issues/101)
- \[RDR-1411\] Selenium Test failed [\#100](https://github.com/muccg/rdrf/issues/100)
- \[RDR-1404\] Form currency doesn't work for FH Follow Up form [\#99](https://github.com/muccg/rdrf/issues/99)

## [1.5.7](https://github.com/muccg/rdrf/tree/1.5.7) (2016-08-01)
[Full Changelog](https://github.com/muccg/rdrf/compare/1.5.6...1.5.7)

## [1.5.6](https://github.com/muccg/rdrf/tree/1.5.6) (2016-07-29)
[Full Changelog](https://github.com/muccg/rdrf/compare/1.5.5...1.5.6)

## [1.5.5](https://github.com/muccg/rdrf/tree/1.5.5) (2016-07-15)
[Full Changelog](https://github.com/muccg/rdrf/compare/1.5.4...1.5.5)

## [1.5.4](https://github.com/muccg/rdrf/tree/1.5.4) (2016-07-12)
[Full Changelog](https://github.com/muccg/rdrf/compare/1.5.3...1.5.4)

## [1.5.3](https://github.com/muccg/rdrf/tree/1.5.3) (2016-07-08)
[Full Changelog](https://github.com/muccg/rdrf/compare/1.5.2...1.5.3)

## [1.5.2](https://github.com/muccg/rdrf/tree/1.5.2) (2016-07-07)
[Full Changelog](https://github.com/muccg/rdrf/compare/1.5.1...1.5.2)

## [1.5.1](https://github.com/muccg/rdrf/tree/1.5.1) (2016-07-07)
[Full Changelog](https://github.com/muccg/rdrf/compare/1.5.0...1.5.1)

## [1.5.0](https://github.com/muccg/rdrf/tree/1.5.0) (2016-07-06)
[Full Changelog](https://github.com/muccg/rdrf/compare/1.4.0...1.5.0)

## [1.4.0](https://github.com/muccg/rdrf/tree/1.4.0) (2016-06-10)
[Full Changelog](https://github.com/muccg/rdrf/compare/1.3.8...1.4.0)

**Closed issues:**

- \[RDR-1242\] Consent- need to restrict view by working groups [\#98](https://github.com/muccg/rdrf/issues/98)
- \[RDR-1321\] export registry not working [\#97](https://github.com/muccg/rdrf/issues/97)
- \[RDR-1319\] questionnaire patient update table was overflowing sometimes [\#96](https://github.com/muccg/rdrf/issues/96)
- \[RDR-1320\] DM1 Questionnaire Patient Creation message doesn't include link [\#95](https://github.com/muccg/rdrf/issues/95)
- \[RDR-1318\] Patient lookup not working when admin logged in [\#94](https://github.com/muccg/rdrf/issues/94)
- \[RDR-1235\] File collection CDE [\#93](https://github.com/muccg/rdrf/issues/93)
- \[RDR-1265\] GridFS → Django storage framework for CDE files [\#92](https://github.com/muccg/rdrf/issues/92)
- \[RDR-1266\] CDE History Charts and revert [\#91](https://github.com/muccg/rdrf/issues/91)
- \[RDR-1229\] Allow curators to pair up questionnaire responses with existing patients [\#90](https://github.com/muccg/rdrf/issues/90)
- \[RDR-1276\] Empty state "allowed" in DM1 questionnaire which blocks questionnaire handling from completing [\#89](https://github.com/muccg/rdrf/issues/89)
- \[RDR-1239\] Implement password strength for password reset function [\#88](https://github.com/muccg/rdrf/issues/88)
- \[RDR-1241\] Partial deletion of patients \(when deleted by dev\)- patient information still appears in 'Family Linkage' 'Consents' and in downloaded 'Report' [\#87](https://github.com/muccg/rdrf/issues/87)
- \[RDR-1323\] Included dm1 update to calc in the yaml export  from live [\#86](https://github.com/muccg/rdrf/issues/86)

## [1.3.8](https://github.com/muccg/rdrf/tree/1.3.8) (2016-06-09)
[Full Changelog](https://github.com/muccg/rdrf/compare/1.3.7.0...1.3.8)

## [1.3.7.0](https://github.com/muccg/rdrf/tree/1.3.7.0) (2016-06-08)
[Full Changelog](https://github.com/muccg/rdrf/compare/1.3.7...1.3.7.0)

## [1.3.7](https://github.com/muccg/rdrf/tree/1.3.7) (2016-06-08)
[Full Changelog](https://github.com/muccg/rdrf/compare/1.3.6.0...1.3.7)

## [1.3.6.0](https://github.com/muccg/rdrf/tree/1.3.6.0) (2016-06-03)
[Full Changelog](https://github.com/muccg/rdrf/compare/1.3.6...1.3.6.0)

## [1.3.6](https://github.com/muccg/rdrf/tree/1.3.6) (2016-06-02)
[Full Changelog](https://github.com/muccg/rdrf/compare/1.3.5...1.3.6)

**Closed issues:**

- \[RDR-1307\] Lookup field CDE no longer working- DM1TestingLaboratory [\#85](https://github.com/muccg/rdrf/issues/85)
- \[RDR-1301\] Handle utf-8 encoded characters in CDE calculation script validation [\#84](https://github.com/muccg/rdrf/issues/84)
- \[RDR-1302\] Looks like we'll need ADsafe to run CDE calculation scripts [\#83](https://github.com/muccg/rdrf/issues/83)
- \[RDR-1303\] Blank red box shown in admin, form errors aren't prominent [\#82](https://github.com/muccg/rdrf/issues/82)
- \[RDR-1304\] Error in Patient API - missing Next of kin relationship [\#81](https://github.com/muccg/rdrf/issues/81)
- \[RDR-1308\] script to add default contexts for patients without mongo data [\#80](https://github.com/muccg/rdrf/issues/80)
- \[RDR-1311\] Snapshot error/form progress [\#79](https://github.com/muccg/rdrf/issues/79)
- \[RDR-1310\] TypeError at /DM1/forms/39/384/6'NoneType' object has no attribute '\_\_getitem\_\_' [\#78](https://github.com/muccg/rdrf/issues/78)
- \[RDR-1309\] context wasn't being set on approved questionnaire [\#77](https://github.com/muccg/rdrf/issues/77)
- \[RDR-1312\] TransactionManagementError at /DM1/approval/38 [\#76](https://github.com/muccg/rdrf/issues/76)

## [1.3.5](https://github.com/muccg/rdrf/tree/1.3.5) (2016-06-02)
[Full Changelog](https://github.com/muccg/rdrf/compare/1.3.4...1.3.5)

## [1.3.4](https://github.com/muccg/rdrf/tree/1.3.4) (2016-06-02)
[Full Changelog](https://github.com/muccg/rdrf/compare/1.3.3...1.3.4)

## [1.3.3](https://github.com/muccg/rdrf/tree/1.3.3) (2016-06-01)
[Full Changelog](https://github.com/muccg/rdrf/compare/1.3.2.1...1.3.3)

## [1.3.2.1](https://github.com/muccg/rdrf/tree/1.3.2.1) (2016-05-30)
[Full Changelog](https://github.com/muccg/rdrf/compare/1.3.2.0...1.3.2.1)

## [1.3.2.0](https://github.com/muccg/rdrf/tree/1.3.2.0) (2016-05-27)
[Full Changelog](https://github.com/muccg/rdrf/compare/1.3.2...1.3.2.0)

## [1.3.2](https://github.com/muccg/rdrf/tree/1.3.2) (2016-05-27)
[Full Changelog](https://github.com/muccg/rdrf/compare/1.3.1.2...1.3.2)

**Closed issues:**

- \[RDR-1264\] Some templates fail with NoReverseMatch on clinician\_list [\#75](https://github.com/muccg/rdrf/issues/75)
- \[RDR-1263\] FH- family linkage- look up index function is no longer working [\#74](https://github.com/muccg/rdrf/issues/74)
- \[RDR-1254\] permissions view has a empty "modules" menu [\#73](https://github.com/muccg/rdrf/issues/73)
- \[RDR-1230\] Security Upgrade to Django 1.8.12 [\#72](https://github.com/muccg/rdrf/issues/72)
- \[RDR-1272\] Allow REST API listing countries and states for unauthenticated users. [\#71](https://github.com/muccg/rdrf/issues/71)
- \[RDR-1257\] javascript alert on new sql explorer report creation [\#70](https://github.com/muccg/rdrf/issues/70)
- \[RDR-1267\] Validate user-provided CDE calculation scripts [\#69](https://github.com/muccg/rdrf/issues/69)
- \[RDR-1234\] Create a script to delete test data on a site prior to launch [\#68](https://github.com/muccg/rdrf/issues/68)
- \[RDR-1246\] REST API - problem with all calls being restricted to authenticated users [\#67](https://github.com/muccg/rdrf/issues/67)
- \[RDR-1256\] mongo database names inconsistent case handling [\#66](https://github.com/muccg/rdrf/issues/66)
- \[RDR-1295\] Fix broken 500.html and 404.html [\#65](https://github.com/muccg/rdrf/issues/65)
- \[RDR-1275\] Lookup index retrieves deleted patients- error then received when trying to 'load this index and family' [\#64](https://github.com/muccg/rdrf/issues/64)
- \[RDR-1274\] jquery.min.js:5 GET https://rdrf.ccgapps.com.au/ophg/api/v1/registries/fh/patients/413/ 500 \(INTERNAL SERVER ERROR\) [\#63](https://github.com/muccg/rdrf/issues/63)
- \[RDR-1252\] Revised REST API [\#62](https://github.com/muccg/rdrf/issues/62)
- \[RDR-1253\] runtime error on Family Linkage rel promo [\#61](https://github.com/muccg/rdrf/issues/61)
- \[RDR-1255\] calculated fields have a javascript alert [\#60](https://github.com/muccg/rdrf/issues/60)
- \[RDR-1269\] @login\_required\_method on views [\#59](https://github.com/muccg/rdrf/issues/59)
- \[RDR-1270\] ccg-django-utils==0.4.2 [\#58](https://github.com/muccg/rdrf/issues/58)
- \[RDR-1259\] FH- Clinical Form NoReverseMatch at /fh/forms/45/397/19 [\#57](https://github.com/muccg/rdrf/issues/57)
- \[RDR-1260\] NoReverseMatch for patient details [\#56](https://github.com/muccg/rdrf/issues/56)
- \[RDR-1277\] FH- include all demographics and consents fields in "FH report" [\#55](https://github.com/muccg/rdrf/issues/55)

## [1.3.1.2](https://github.com/muccg/rdrf/tree/1.3.1.2) (2016-05-26)
[Full Changelog](https://github.com/muccg/rdrf/compare/1.3.1.1...1.3.1.2)

## [1.3.1.1](https://github.com/muccg/rdrf/tree/1.3.1.1) (2016-05-25)
[Full Changelog](https://github.com/muccg/rdrf/compare/1.3.1.0...1.3.1.1)

## [1.3.1.0](https://github.com/muccg/rdrf/tree/1.3.1.0) (2016-05-23)
[Full Changelog](https://github.com/muccg/rdrf/compare/1.3.1...1.3.1.0)

## [1.3.1](https://github.com/muccg/rdrf/tree/1.3.1) (2016-05-20)
[Full Changelog](https://github.com/muccg/rdrf/compare/1.3.0...1.3.1)

## [1.3.0](https://github.com/muccg/rdrf/tree/1.3.0) (2016-05-19)
[Full Changelog](https://github.com/muccg/rdrf/compare/1.2.4.0...1.3.0)

## [1.2.4.0](https://github.com/muccg/rdrf/tree/1.2.4.0) (2016-05-16)
[Full Changelog](https://github.com/muccg/rdrf/compare/1.2.4...1.2.4.0)

## [1.2.4](https://github.com/muccg/rdrf/tree/1.2.4) (2016-05-13)
[Full Changelog](https://github.com/muccg/rdrf/compare/1.2.3.0...1.2.4)

## [1.2.3.0](https://github.com/muccg/rdrf/tree/1.2.3.0) (2016-05-13)
[Full Changelog](https://github.com/muccg/rdrf/compare/1.2.3...1.2.3.0)

## [1.2.3](https://github.com/muccg/rdrf/tree/1.2.3) (2016-05-13)
[Full Changelog](https://github.com/muccg/rdrf/compare/1.2.2...1.2.3)

## [1.2.2](https://github.com/muccg/rdrf/tree/1.2.2) (2016-05-12)
[Full Changelog](https://github.com/muccg/rdrf/compare/1.2.2.0...1.2.2)

## [1.2.2.0](https://github.com/muccg/rdrf/tree/1.2.2.0) (2016-05-12)
[Full Changelog](https://github.com/muccg/rdrf/compare/1.2.1...1.2.2.0)

## [1.2.1](https://github.com/muccg/rdrf/tree/1.2.1) (2016-04-29)
[Full Changelog](https://github.com/muccg/rdrf/compare/1.2.0...1.2.1)

**Closed issues:**

- \[RDR-1225\] Report wide format  [\#54](https://github.com/muccg/rdrf/issues/54)
- \[RDR-1226\] Report ordering [\#53](https://github.com/muccg/rdrf/issues/53)



\* *This Change Log was automatically generated by [github_changelog_generator](https://github.com/skywinder/Github-Changelog-Generator)*