# Security considerations

### Description

Bonfire is a secure service that allows automated command line inspection
as well as prevention of various kinds of attacks commited through the
command line. This is achieved using SoTA LLM queries whereby the LLM decides
about the harmfulness of the user based on factors such as the command and the
expectations.

### Requirement analysis

> Server

[✔] Compatibility with API standards

[✔] gRPC for secure communication

[✔] Disable gRPC reflection for improved security

[✔] E2E HTTPS encryption between server and client

[✘] Defense against injection attacks

[✔] Configurability

[✔] Logging for non-repudiation

[✘] Origin authentication

> Client

[✔] gRPC for secure communication

[✔] E2E HTTPS encryption between client and server

[✔] Compile time configurability to avoid spoofing addresses

[✔] Embedded shell environment to restrict spoofing of executable

[✘] Origin authentication

[✔] Implement Fail Open

[✔] Implement Fail Closed strategy

### Acceptance testing

[✔] Solves the problem of command line attacks

[✔] Costs and time efficiency

[✘] Secure as in fool proof

### System design

* Use LLMs to generate description semantic meaning of commands
* Allow the LLM to ponder on an answer to yield better results
* Constrain the LLM to give a one-token ( hard to miss ) prediction on the following criteria:
    * Malignity: how malicious the intent is
    * Severity: how bad the effects are
    * Utility: how useful in context of current task
    * Expectance: how usual the command is with regards to context
* Calculate probability based on the scores from a machine learning algorithm ( NN, Logistic Regression, etc. )
* Apply defensive techniques on the client side based on probability ( user deletion etc. )

### System testing

* Statistical testing has shown a strong correlation between the scores and the simulated environment
* Larger LLMs tend to do better
* Needs more testing, synthetic data was unsatisfactory
* LLama3.2-1B shown lots of false pos, neg ( due to low size ), needs refining in the system prompt
* LLM is the bottleneck
* Hallucination is a problem

### Architecture design

* Non-reflective client-server grpc connection for enhanced protection
* Stateless completions from the LLM http server ( as chat is not needed )
* The core logic is in the server, reduce risk and computation on client
* Modular architecture, necessary due to rapid changes in the field + easy support for different LLMs
* LLM + ML <-> Server <-[Certificate authority]-> Client <-> Shell <-> User 

### Architecture testing

* User spoofing -> DOS attack ( denying legitimate users )
* User creation & deletion weakness ( opt for uid instead in next sprint )
* Downloading untrusted programs is the main problem
    * Solution 2: Have a diff-ed filesystem with security rankings and AI-based script evaluation scoring, ( + hashing metadata to avoid double checking ), out of scope

### Module design

* Server
    * Api providers ( modular )
        * Github
        * Gitlab
        * ...
    * Config ( flexible configuration using JSON )
    * ML inference runner
    * gRPC implementation without reflection
    * LLM providers through llamafile
        * Plug & play any Llamafile
        * Easy distribution, creation and inference

* Client
    * gRPC implementation
    * Always quiet mode ( no stderr / stdout ), custom panic handler

* Shell
  * Memfd executable & init file storage
  * Command executor

## Unit tests

> Server

* Test working case
* Test unknown ip
* Test timeout
* Test ip denied
* Test user denied

> Client

Since the client is fail open, it does not need to be tested.

> Shell

Since the shell is just a wrapper, it does not need to be tested.
