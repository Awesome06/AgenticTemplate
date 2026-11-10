# Contributing Guidelines

Thank you for contributing to this project! We welcome pull requests, bug reports, and architectural improvements.

---

## 1. Code of Conduct

All contributors and maintainers are expected to adhere to our [Code of Conduct](CODE_OF_CONDUCT.md). Please treat all participants with professional respect.

---

## 2. Development Setup

1. Fork and clone the repository.
2. Configure your local environment and toolchain.
3. Install dependencies and run the automated test suite locally to verify parity:
   ```bash
   # Run tests and static analysis
   make test
   # Or via active package runner (pytest / cargo test / npm test / go test)
   ```

---

## 3. Pull Request Guidelines

1. **Focused Diffs:** Keep pull requests concise and tightly scoped. Avoid bundling unrelated formatting churn or reformatting whole files.
2. **Automated Testing:** All new features, bug fixes, or performance enhancements must include automated regression tests.
3. **Documentation:** Update relevant docstrings and README documentation when modifying public API surfaces.
4. **Conventional Commits:** Write clear commit messages adhering to `globals/git-release`:
   - `feat:` A new feature or capability
   - `fix:` A bug fix
   - `perf:` A code change that improves performance
   - `docs:` Documentation-only changes
   - `test:` Adding or correcting tests
   - `chore:` Changes to build process, dependencies, or auxiliary tools

---

## 4. Submitting a Pull Request

1. Push your branch to your fork.
2. Open a Pull Request against the `main` branch.
3. Fill out the provided [Pull Request Template](.github/PULL_REQUEST_TEMPLATE.md) completely.
4. Ensure all continuous integration checks pass across Linux, macOS, and Windows.
