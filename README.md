# AI-Chat

For the content below visit: https://github.com/santteegt/rasa-chatbot-example

## Chatbot example using Rasa

Basic chatbot example using the OpenSource [Rasa Stack](http://www.rasa.com/) (Rasa NLU and Rasa Core). Rasa is written in Python allows developers to expand chatbots and voice assistants beyond answering simple questions by enabling state-of-the-art machine learning models your bots can hold contextual conversations with users.

This repository is based on the official Rasa [quicktart](http://www.rasa.com/docs/core/quickstart/) guide.

## Installation requirements

* Python 3.6
* pip
* Rasa Core and Rasa NLU. Follow official installation [instructions](http://www.rasa.com/docs/core/installation/). Altenatively you can just run the following on a terminal.

## Chatbot setup & deployment

Follow the instructions below to train and test the chatbot. Requires configuration files to setup your bot are:

**Rasa Core**

- **stories.md**: Rasa Core works by learning from example conversations. A story starts with `##` followed by a name (optional). Lines that start with `*` are messages sent by the user. Although you don’t write the actual message, but rather the intent (and the entities) that represent what the user means. Lines that start with - are actions taken by your bot. In general an action can do anything, including calling an API and interacting with the outside world. Find more info about the format [here](http://www.rasa.com/docs/core/stories/).

- **domain.yml**: The domain defines the universe your bot lives in (see [Domain format](http://www.rasa.com/docs/core/domains/)):

| Conf      | Description                                        |
|-----------|----------------------------------------------------|
| actions   | things your bot can do and say                     |
| templates | template strings for the things your bot can say   |
| intents   | things you expect users to say                     |
| entities  | pieces of info you want to extract from messages   |
| slots     | information to keep track of during a conversation |

**Rasa NLU**

- **nlu.md**: define the user messages the bot should be able to handle. It is suggested to define at least five examples of utterances.
- **nlu_config.yml**: NLU parameters configuration

### 1. Train your model

```bash

```

### 2. Train your NLU agent

```bash

```

### 3. Visualizing stories

[Story graph](graph.png) shows an overview of the conversational paths defined in [stories.md](stories.md).
To re-generate the graph see [documentation](http://www.rasa.com/docs/core/debugging/#visualizing-your-stories).

### 4. Deploying custom actions endpoint

```bash

```

### 5. Test your chatbot locally

```bash

```

### 6. Interactive Learning

[Interactive Learning](http://www.rasa.com/docs/core/interactive_learning/) is a powerful way to explore what your bot can do, and the easiest way to fix any mistakes it makes, while covering different possible scenarios that were not taken into account when defining your chatbot domain & stories.

Interactive learning can be started using the following command:

```bash

```

It will enable an interactive prompt where you can train different intents and scenarios.
**However**, current rasa_core version 0.11.1, just allows you to export the last conversation context per interactive session. 
An enhancement issue has been opened [here](https://github.com/RasaHQ/rasa_core/issues/941), so in a near future you wiil be able to export multiple conversation contexts you used during interactive learning.

Another option is to To train your bot in interactive mode during runtime. To do so, you need to start your bot using the `--enable-api` parameter as follows;

```bash

```

# License
Licensed under the Apache License, Version 2.0. See [LICENSE](LICENSE.txt)
