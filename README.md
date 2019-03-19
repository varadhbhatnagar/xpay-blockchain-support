# xpay-blockchain-support
## Introduction
A Blockchain application which aims to store and verify integrity of transactions done using <b>Xpay</b>.
It is built using <b>Hyperledger Fabric and Composer</b>.

Specific transaction attributes are stored on a blockchain and transaction integrity can be verified by querying the blockchain for a particular transaction.

## Running Instructions 
For all purpose,

<b>Name of network : xpay-blockchain-support</b>

<b>Version : 0.0.14</b>

Step 1: From the fabric installation directory, Start fabric instance on host machine using `./startFabric.sh`.

Step 2: Create peer admin car using `./createPeerAdminCard.sh`.

Step 3: From the business network directory, install the network on the host machine using `composer network install -a xpay-blockchain-support@0.0.14.bna -c PeerAdmin@hlfv1`.

Step 4: Start the network on the host machine using `composer network start --networkName xpay-blockchain-support --networkVersion 0.0.14 --networkAdmin admin --networkAdminEnrollSecret adminpw --card PeerAdmin@hlfv1 --file networkadmin.card`.

Step 5: Start the rest server using `composer-rest-server`. Enter name of business network card `admin@xpay-blockchain-support` when prompted. Select other options as per convenience.

Whenever the network is started for the first time, `SetUp` should be run as it initializes the network with appropritate assets and participants.

While posting transactions to the blockchain, in the `.json` always

<b>"commodity" : "resource:org.xpay.Commodity#Default"</b>

<b>"newOwner" : "resource:org.xpay.Trader#DB" </b>

Step 6: For closing the fabric instance, run `./stopFabric.sh`, followed by `./tearDownFabric.sh` inside the fabric installation directory.

## Description of API Endpoints

<b>1. SetUp</b> - Initializes the network with an asset `Default` and a participant `DB`. A `POST` request must be sent to this end point to initialize the network everytime it is started.

<b>2. Trade</b> - Most important endpoint which is used to store transaction data to the blockchain. A '`POST` request must be sent to this end point, along with all the transaction data in `.json` format to save the data. `GET` request on this endpoint will retreive details of all the trades which have occured on the blockchain.

<b>3. Query</b> - This is used to query the blockchain for a particular transaction. A `GET` request to this endpoint along with `PaymentTokenID` value as the parameter will retreive details of that particular transaction.

## Data Persistence

https://stackoverflow.com/questions/50420225/hyperledger-data-persistence-between-fabric-restarts
