{
	inputs = {
    nixpkgs.url = "nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };
  outputs = { self, nixpkgs, flake-utils }:
    (flake-utils.lib.eachDefaultSystem
      (system:
        let 
					pkgs = import nixpkgs { inherit system; };

          pythonEnv = pkgs.python39.withPackages (ps: [
            (ps.buildPythonPackage rec {
              pname = "PyDesmos";
              version = "0.1.3";
              src = pkgs.fetchPypi {
                inherit pname version;
                sha256 = "f22d353430fe87118a84da105437cdeb5e292ba875b062d9978c3a639f3e0d6c";
              };
            })
          ]);
        in
        {
					devShells.default = pkgs.mkShell {
						buildInputs = [
              pythonEnv
            ];
					};
				})
    );
}
