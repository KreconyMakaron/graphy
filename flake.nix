{
	inputs = {
    nixpkgs.url = "nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };
  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem
      (system:
        let 
					pkgs = import nixpkgs { inherit system; };
          python = pkgs.python3.withPackages (ps: [
            ps.numpy
            ps.sympy
            ps.matplotlib
            ps.discordpy
          ]);
        in
        {
					devShells.default = pkgs.mkShell {
						buildInputs = [
              python
            ];
					};

          packages = {
            myapp = pkgs.writeShellScriptBin "run" ''
              ${python}/bin/python3 bot.py
            '';
            default = self.packages.${system}.myapp;
          };
				});
}
