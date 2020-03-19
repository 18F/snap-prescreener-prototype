# Prototype: SNAP Pre-screener

## Preamble

This is a sketchpad prototype built by 18F's [Eligibility APIs Initiative](https://github.com/18F/eligibility-rules-service/blob/master/README.md) to explore the financial factors of SNAP eligibility.

:warning: ***None of the eligibility rules expressed in this repository should be considered official interpretations of SNAP rules or policy. This is a sketchpad prototyping repo only.*** :warning:

## What does this do?

This is a demo pre-screener for SNAP benefits. It could help someone decide if it is worth their time and energy to submit a full application to SNAP by giving them an understanding of their likely eligibility and their estimated benefit amount if eligible.

This pre-screener uses the **[snap-api-prototype](https://github.com/18F/snap-api-prototype)**, which we are building in parallel. The goal is for the pre-screener to be able to call the API both over the wire and as an internal Python library.

This pre-screener is optimized for quick results (single page), and for ease of changing inputs and seeing different output values (data loaded client-side with JS). These are optimizations for testing, QA'ing, and demo-ing the application.

## Environment

To run the project locally, you will need:

* [Python 3.8.1](https://www.python.org/downloads/).
* [Pipenv](https://pipenv.kennethreitz.org/en/latest/), for installing and managing dependencies.
* [Pyenv](https://github.com/pyenv/pyenv), for managing Python versions. (Optional but recommended.)

## Install the dependencies

```
make install
```

## Run tests & checks

```
make check-all
```

## Run locally

```
make serve
```

## Deploy

This app includes a `manifest.yml` file with deploy configuration for [Cloud.gov](https://cloud.gov/) or another [Cloud Foundry](https://www.cloudfoundry.org/) system.

The [pre-screener is deployed to Cloud.gov](https://snap-prescreener-prototype.app.cloud.gov/). Since this application falls under [ATO pre-assessment](https://before-you-ship.18f.gov/ato/types/#conditions-for-pre-assessment), it is password-protected and only available to Federal staff.

Please reach out via [email](mailto:eligibility-apis-initiative@gsa.gov) if you are a Federal employee and would like a demonstration of the web API and pre-screener.
