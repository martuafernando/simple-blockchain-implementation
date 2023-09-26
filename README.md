# simple-blockchain-implementation
Simple implementation of Blockchain for Blockchain course

## API Endpoint

### GET /mine_block

### GET /get_chain

### GET /valid
### PUT /block
#### Body
| Key      | Type   | Default | Required | Description      |
| -------- | ------ | ------- | -------- | ---------------- |
| id       | String |         | Yes      | Id of the block  |
| hash     | String |         | Yes      | New hash for the block|

## Getting Started

### Prerequisites

- flask

### Installation

1. Clone the repo

```bash
$ git clone https://github.com/martuafernando/simple-blockchain-implementation.git
$ cd simple-blockchain-implementation
```

2. Install requirements.txt

```bash
pip install -r requirements.txt
```

3. Run program

```bash
python main.py
```