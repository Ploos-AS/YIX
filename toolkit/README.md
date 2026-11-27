# µIX Deployment Toolkit

Alpha, MIT. Offline Python 3 standard-library CLI. No credentials, network calls or deployment actions.

Run from the repository root:

    python3 toolkit/muixctl.py validate toolkit/examples/nano.json
    python3 toolkit/muixctl.py plan toolkit/examples/micro.json
    python3 -m unittest discover -s toolkit -p 'test_*.py'

JSON is the initial inventory format to avoid external dependencies; YAML support is deferred. Inventory checks cover only basic profile topology counts and declared host failure domains. They do not verify physical independence, redundant switching paths, routing policy, addressing, or full specification conformance. Plan output is advisory. BIRD configuration rendering, Compose support and deployment are future work.
