#!/usr/bin/perl
# down-this-from.pl

use 5.22.1;
use strict;
use warnings;
use open qw< :encoding(UTF-8) >;
use LWP::Simple;

my $filename = "info.txt";
my $handle = undef;

open($handle, "<", $filename)  || die;

my $img_regex = "([0-9]{1,6}\.jpg)";
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

close($handle) || warn $_[0];

for my $img (@imgs) {
  #my $path = "img/" . $img;
  #my $link = $uri . $img;
  down_this($uri . $img, "img/" . $img);
}

sub down_this {
  my ($url, $path) = @_;
  getstore($url, $path) if check_this($url);
}

sub check_this {
  my @response = head(shift(@_));
  return 1 if @response and $response[0] eq "image/jpeg";
  return 0;
}
