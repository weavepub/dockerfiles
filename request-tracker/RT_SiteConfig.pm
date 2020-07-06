use utf8;

Set($WebPort, 80);
Set($WebBaseURL, 'http://rt4.wmq.com');
Set($rtname, 'wmq');
Set($Organization, 'wmq');
Set($MailCommand, "testfile");
# External auth specifications
Set(@Plugins, (qw(RT::Authen::ExternalAuth)));
Set($ExternalAuthPriority,  [ 'My_LDAP' ]);
Set($ExternalInfoPriority,  [ 'My_LDAP', ]);
Set($AutoCreateNonExternalUsers,    0);
Set($ExternalSettings, {
	'My_LDAP'       =>  {
	    'type'                      =>  'ldap',
	    'server'                    =>  'ldaps://ldap.wmq.com:636',
	    'user'                      =>  'cn=manager,dc=wmq,dc=com',
	    'pass'                      =>  '******',
	    'base'                      =>  'ou=员工,dc=wmq,dc=com',
	    'filter'                    =>  '(objectClass=inetOrgPerson)',
	    'attr_match_list' => [
	        'Name',
	        'EmailAddress',
	    ],
	    'attr_map' => {
	        'Name' => 'uid',
	        'EmailAddress' => 'mail',
	        'RealName' => 'sn',
		'WorkPhone' => 'telephoneNumber'
	    },
	},
});

1;
