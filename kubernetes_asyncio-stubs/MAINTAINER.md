# Maintainer instructions

1. Update the `kubernetes-client-python` submodule if necessary:

   ```
   VERSION=v...
   pushd kubernetes-client-python
   git fetch --all --tags
   git checkout $VERSION
   popd
   ```

2. Do code generation:

   ```
   poetry run python codegen
   ```

3. Format:

   ```
   bin/fmt
   ```

4. Update the version in pyproject.toml.

5. Check for any new files in this release, add them:

   ```
   git diff
   git add ...
   ```

6. Add and push a corresponding tag:

   ```
   VERSION=v...
   git commit -am "Release $VERSION"
   git tag -a $VERSION -m $VERSION
   git push --follow-tags
   ```
