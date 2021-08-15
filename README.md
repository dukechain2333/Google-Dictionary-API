# Google Dictionary API
 A command line implement of Google dictionary

## Acknowledge

API provider: https://api.dictionaryapi.dev/

## Installation

Install Python packages by running:

```
pip install -r requirements
```

## Usage

1. Input a word to inquiry its meaning.
2. Commands:

About language.

`@lang en`: Switch language to English, require the argument 'language code'. For other languages, replance `en` with another language code. (default English)

`@langtb`: Display all supported language code.

About history.

`@clr`: Clear all searching history.

`@disp`: Display all searching history.

`@track on`: Start to record searching history, require the argument `on` or `off`. (default off)

Exit program.

`@save`: Exit and save the config.

