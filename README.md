# simple-blockchain-implementation
Simple implementation of Blockchain for Blockchain course

## API Endpoint

### GET /mine_block
Make a block without data

### GET /chain
Show the chain of the block

### GET /valid
Show chain validity

### POST /block

Make a block with data


**Request Headers**:

- Content-Type: application/json

**Request Body**:

| Key      | Type   | Default | Required | Description      |
| -------- | ------ | ------- | -------- | ---------------- |
| data     | String |         | Yes      | New data for the block|
### PUT /block/:id

Modify block data

**Request Headers**:

- Content-Type: application/json

**Request Body**:

| Key      | Type   | Default | Required | Description      |
| -------- | ------ | ------- | -------- | ---------------- |
| data     | String |         | No      | New data for the block|
| hash     | String |         | No      | New hash for the block|

> At least one of 'hash' or 'data' must be provided

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