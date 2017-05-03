import json


def dataFlowGenerator():
    dataFlow = {
                   "name":"Linda TV",
                   "description":"this describe the dataflow",
                   "steps":[
                      {
                         "id":"account",
                         "type":"datasource.read.gigya.account",
                         "params":{
                            "select":"isVerified,profile.email,profile.firstName,profile.lastName,created,data.lindatv_v1_optin_dagelijkse_nieuwsbrief",
                            "where":"isVerified = true and data.lindatv_v1_optin_dagelijkse_nieuwsbrief = true"
                         },
                         "next":[
                            "flat"
                         ]
                      },
                      {
                         "id":"flat",
                         "type":"field.flat",
                         "params":{
                            "fields":[
                               "profile",
                               "data"
                            ]
                         },
                         "next":[
                            "dsv"
                         ]
                      },
                      {
                         "id":"dsv",
                         "type":"file.format.dsv",
                         "params":{
                            "filePrefix":"linda_",
                            "fileDateFormat":"yyyyMMdd",
                            "fileExtension":"csv",
                            "columnSeparator":",",
                            "quoteFields":"true"
                         },
                         "next":[
                            "gzip"
                         ]
                      },
                      {
                         "id":"gzip",
                         "type":"file.compress.gzip",
                         "next":[
                            "sftp"
                         ]
                      },
                      {
                         "id":"sftp",
                         "type":"datasource.write.sftp",
                         "params":{
                            "host":"idx-etl.gigya.net",
                            "username":"idx",
                            "password":"idx",
                            "remotePath":"linda"
                         }
                      }
                   ]
                }

    dataFlow = {"name":"SH_Welcome1_US_outbound","description":"accounts > renameFields > csv","steps":[{"id":"accounts","type":"datasource.read.gigya.account","params":{"select":"UID,created,createdTimestamp,emails.verified,emails.unverified,iRank,isActive,isLockedOut,isRegistered,isVerified,lastLogin,lastLoginLocation.city,lastLoginLocation.coordinates.lon,lastLoginLocation.coordinates.lat,lastLoginLocation.country,lastLoginLocation.state,lastLoginTimestamp,lastUpdated,lastUpdatedTimestamp,loginIDs.emails,loginIDs.unverifiedEmails,loginIDs.username,loginProvider,oldestDataUpdated,oldestDataUpdatedTimestamp,regSource,registered,registeredTimestamp,socialProviders,verified,verifiedTimestamp,profile.address,profile.age,profile.birthDay,profile.birthMonth,profile.birthYear,profile.city,profile.country,profile.email,profile.firstName,profile.followersCount,profile.followingCount,profile.gender,profile.hometown,profile.isConnected,profile.iRank,profile.isSiteUID,profile.isSiteUser,profile.languages,profile.lastLoginLocation,profile.loginProvider,profile.loginProviderUID,profile.lastName,profile.locale,profile.nickname,profile.oldestDataAge,profile.oldestDataUpdatedTimestamp,profile.photoURL,profile.profileURL,profile.relationshipStatus,profile.religion,profile.state,profile.thumbnailURL,profile.timezone,profile.username,profile.verified,profile.zip,data.newsletter_sallyhansen,data.subscribe,data.terms","where":"isRegistered = true"},"next":["renameFields"]},{"id":"renameFields","type":"field.rename","params":{"fields":[{"sourceField":"emails.verified","targetField":"emails_verified"},{"sourceField":"emails.unverified","targetField":"emails_unverified"},{"sourceField":"lastLoginLocation.city","targetField":"lastLoginLocation_city"},{"sourceField":"lastLoginLocation.coordinates.lon","targetField":"lastLoginLocation_coordinates_long"},{"sourceField":"lastLoginLocation.coordinates.lat","targetField":"lastLoginLocation_coordinates_lat"},{"sourceField":"lastLoginLocation.country","targetField":"lastLoginLocation_country"},{"sourceField":"lastLoginLocation.state","targetField":"lastLoginLocation_state"},{"sourceField":"loginIDs.emails","targetField":"loginIDs_emails"},{"sourceField":"loginIDs.unverifiedEmails","targetField":"loginIDs_unverifiedEmails"},{"sourceField":"loginIDs.username","targetField":"loginIDs_username"},{"sourceField":"profile.address","targetField":"profile_address"},{"sourceField":"profile.age","targetField":"profile_age"},{"sourceField":"profile.birthDay","targetField":"profile_birthDay"},{"sourceField":"profile.birthMonth","targetField":"profile_birthMonth"},{"sourceField":"profile.birthYear","targetField":"profile_birthYear"},{"sourceField":"profile.city","targetField":"profile_city"},{"sourceField":"profile.country","targetField":"profile_country"},{"sourceField":"profile.email","targetField":"profile_email"},{"sourceField":"profile.firstName","targetField":"profile_firstName"},{"sourceField":"profile.followersCount","targetField":"profile_followersCount"},{"sourceField":"profile.followingCount","targetField":"profile_followingCount"},{"sourceField":"profile.gender","targetField":"profile_gender"},{"sourceField":"profile.hometown","targetField":"profile_hometown"},{"sourceField":"profile.isConnected","targetField":"profile_isConnected"},{"sourceField":"profile.iRank","targetField":"profile_iRank"},{"sourceField":"profile.isSiteUID","targetField":"profile_isSiteUID"},{"sourceField":"profile.isSiteUser","targetField":"profile_isSiteUser"},{"sourceField":"profile.languages","targetField":"profile_languages"},{"sourceField":"profile.lastLoginLocation","targetField":"profile_lastLoginLocation"},{"sourceField":"profile.loginProvider","targetField":"profile_loginProvider"},{"sourceField":"profile.loginProviderUID","targetField":"profile_loginProviderUID"},{"sourceField":"profile.lastName","targetField":"profile_lastName"},{"sourceField":"profile.locale","targetField":"profile_locale"},{"sourceField":"profile.nickname","targetField":"profile_nickname"},{"sourceField":"profile.oldestDataAge","targetField":"profile_oldestDataAge"},{"sourceField":"profile.oldestDataUpdatedTimestamp","targetField":"profile_oldestDataUpdatedTimestamp"},{"sourceField":"profile.photoURL","targetField":"profile_photoURL"},{"sourceField":"profile.profileURL","targetField":"profile_profileURL"},{"sourceField":"profile.relationshipStatus","targetField":"profile_relationshipStatus"},{"sourceField":"profile.religion","targetField":"profile_religion"},{"sourceField":"profile.state","targetField":"profile_state"},{"sourceField":"profile.thumbnailURL","targetField":"profile_thumbnailURL"},{"sourceField":"profile.timezone","targetField":"profile_timezone"},{"sourceField":"profile.username","targetField":"profile_username"},{"sourceField":"profile.verified","targetField":"profile_verified"},{"sourceField":"profile.zip","targetField":"profile_zip"},{"sourceField":"data.newsletter_sallyhansen","targetField":"data_newsletter_sallyhansen"},{"sourceField":"data.subscribe","targetField":"data_subscribe"},{"sourceField":"data.terms","targetField":"data_terms"}]},"next":["csv"]},{"id":"csv","type":"file.format.dsv","params":{"fileName":"SH_Welcome1_US_${now:yyyyMMddHHmmss}.csv","columnSeparator":",","quoteFields":True},"next":["sftp"]},{"id":"sftp","type":"datasource.write.sftp","params":{"host":"idx-etl","username":"idx","password":"idx","remotePath":"outbound"}}]}

    dataFlow = json.dumps(dataFlow)

    return dataFlow