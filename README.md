# Bonfire LLM Backend
> Open source AI driven security tool

DO NOT USE IT IN PRODUCTION!

## What is Bonfire?

Bonfire is a set of tools to integrate AI into zero-trust environments. 
Bonfire is also my thesis project ;) .

## How does it work?

Bonfire interacts with your shell in order to protect from running malicious commands.
Bonfire queries an LLM to provide details for each command in relation to the current tasks of the user.
Basically it checks the difference of what should be and what is happening.
The parameters are then used in a neural network to extract the probability of an attack.

## Why or where would I use it?

Probably you do not need Bonfire.
Bunfire was created to solve the weakest-link-in-the-chain problem. 
People are the weakest link in any organization and as such are the most vulnerable and targeted. 
Even the most trusted person can act maliciously whether by accident or on purpose.
Bonfire only allows commands to be run that contribute to the goal of the organization, set in the management software.
Think of it like a human level firewall.
It catches bad guys before they commit crime but also is a pain to work with and your employees probably won't like if you take away their freedom.
One benefactor could be the military.

## Where are the components?

You can find all components on github under ehlkristofhenrik/bonfire-*.

* Bonfire Server  (grpc server)
  * Serves Bonfire Client
  * Queries management API ( github issues )
  * Queries LLM ( llamafile )
  * Runs ML inference
* Bonfire Client  (grpc client)
  * Communicates to Bonfire Server
  * Returns success status to shell script in Bonfire Shell
* Bonfire ML      (neural net)
  * Translates LLM output parameters to probability
  * Returns whether the probability is greater than 0.5
* Bonfire Dataset (dataset for the neural net)
  * For training the ML component
* Bonfire LLM Backend
* Bonfire Shell   (shell wrapper)
  * Safe in-memory executor for shell
  * Initializes shell with script
