#!/usr/bin/perl
# down-this-from.pl

use 5.22.1;
use strict;
use warnings;
use open qw< :encoding(UTF-8) >;
use LWP::Simple;

my $filename = "id.txt";
my $handle = undef;

open($handle, "<", $filename)  || die;

my $img_regex = "([0-9]{4,6}\.jpg)";
my @imgs = ();
my $uri_regex = "(^https?://.*)";
my $uri;

while (<$handle>) {
  if (m/^$img_regex$/) {
    push @imgs, $1;
  } elsif (m/^$uri_regex$/) {
    $uri = $1;
  }
}

for my $img (@imgs) {
  my $path = "imgs/" . $img;
  my $link = $uri . $img;
  getstore($link, $path);
}
