# Installs puppet-lint on a machine
package { 'puppet-lint':
    ensure   => '2.1.1',
    provider => 'gem',
}
