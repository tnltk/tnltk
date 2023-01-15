.. highlight:: shell

============
Contributing
============

Contributions are welcome, and they are greatly appreciated! Every little bit
helps, and credit will always be given.

You can contribute in many ways:

Types of Contributions
----------------------

Report Bugs
~~~~~~~~~~~

Report bugs at https://github.com/tnltk/tnltk/issues.

If you are reporting a bug, please include:

* Your operating system name and version.
* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.

Be sure to take a look at the template here: https://github.com/TarikKaanKoc/tnltk/tree/main/docs/source/_templates

Fix Bugs
~~~~~~~~

Look through the GitHub issues for bugs. Anything tagged with "bug" and "help
wanted" is open to whoever wants to implement it.

Implement Features
~~~~~~~~~~~~~~~~~~

Look through the GitHub issues for features. Anything tagged with "enhancement"
and "help wanted" is open to whoever wants to implement it.

Write Documentation
~~~~~~~~~~~~~~~~~~~

The TNLTK library can always benefit from more documentation. This includes official documentation, docstrings, and even blog posts and articles on the web.

Submit Feedback
~~~~~~~~~~~~~~~

The most effective way to provide feedback is by creating an issue on the TNLTK GitHub repository at https://github.com/tnltk/tnltk/issues.

If you would like to propose a new feature:
- Clearly explain how it would work.
- Keep the scope of the feature as narrow as possible to make it easier to implement.
- Remember that this is a volunteer-driven project and contributions are always welcome.

Get Started!
------------

Ready to contribute? Follow these steps to set up tnltk for local development:

1. Fork the `tnltk`  repository on GitHub.  
2. Clone your fork locally using the following command:

    $ git clone https://github.com/your_github_username/tnltk.git

3. Create a new branch for your local development by running the following command:

    $ git checkout -b branch-name

   This will allow you to make changes locally without affecting the master branch.

4. Make the necessary changes and commit them to the branch using the following commands:

    $ git add .
    $ git commit -m "Your detailed description of your changes."

5. Push the changes to your forked repository on GitHub by running the following command:

    $ git push origin branch-name

6. Submit a pull request through the GitHub website to have your changes reviewed and potentially merged into the main repository.

Pull Request Guidelines
-----------------------

Before submitting a pull request, please ensure that it meets the following guidelines:

1. We strongly recommend creating a dedicated branch when modifying core features. This allows for easy testing by others and can then be merged into the **main** branch.
   
3. If you are adding a new feature, function, etc., be sure to write test cases before submitting a pull request.
   
4. The pull request should include tests. Test locally using **pytest** before submitting the pull request:
   
   $ pytest --durations=0 tests/
    
5. Not all tests may be necessary for a given modification to the source code. We recommend using the   pytest plugin testmon (https://github.com/tarpas/pytest-testmon) to select the appropriate tests to be executed at each commit/pull request:
    
    $ pytest --durations=0 --testmon tests/
   
6. If the pull request adds functionality, the documentation should be updated. Be sure to include a docstring for new functionality and update the documentation if necessary.

7. The pull request should be compatible with Python versions  3.8 => || <= 3.10.