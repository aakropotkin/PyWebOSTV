{ pkgs ? import <nixpkgs> {}
, stdenv ? ( import <nixpkgs> {} ).stdenv
}:
let

in
  stdenv.mkDerivation {

    name = "lg-webos-remote-env";

    buildInputs = ( with pkgs.python37Packages; [
      requests
      future
      ws4py
      pytest
      pylint
      coveralls
      twine
      wheel
      #lg-webos-remote
    ] ) ++ ( with pkgs; [
      nodejs-10_x
    ] );

    shellHook = ''
      alias pip="PIP_PREFIX='$(pwd)/_build/pip_packages' \pip"
      export PYTHONPATH="$(pwd)/_build/pip_packages/lib/python3.7/site-packages:$PYTHONPATH"
      unset SOURCE_DATE_EPOCH
    '';

  }
