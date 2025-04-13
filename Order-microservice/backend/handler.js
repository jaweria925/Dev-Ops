const AWS = require('aws-sdk');
const dynamoDB = new AWS.DynamoDB.DocumentClient();
const sqs = new AWS.SQS();
const QUEUE_URL = 'https://sqs.us-east-1.amazonaws.com/123456789012/OrderQueue'; // Replace with your SQS queue URL

// Producer: Sends a message to SQS
module.exports.createOrder = async (event) => {
  const { product, quantity } = JSON.parse(event.body);

  const params = {
    TableName: 'Orders',
    Item: {
      id: Date.now().toString(),
      product,
      quantity,
    },
  };

  try {
    // Insert order into DynamoDB
    await dynamoDB.put(params).promise();

    // Send message to SQS
    const sqsParams = {
      QueueUrl: QUEUE_URL,
      MessageBody: JSON.stringify({ id: params.Item.id, product, quantity }),
    };

    await sqs.sendMessage(sqsParams).promise();

    return {
      statusCode: 200,
      body: JSON.stringify({ message: 'Order created and message sent to SQS successfully!' }),
    };
  } catch (error) {
    console.error(error);
    return {
      statusCode: 500,
      body: JSON.stringify({ message: 'Error creating order or sending message to SQS' }),
    };
  }
};

// Consumer: Processes messages from SQS
module.exports.processOrderMessage = async (event) => {
  for (const record of event.Records) {
    try {
      const order = JSON.parse(record.body);

      // Here you can process the order further (e.g., logging, updating database, etc.)
      console.log('Processing Order:', order);

      // Example of logging to console (you can perform actual business logic here)
      // For example, update another DynamoDB table or send an email, etc.
      // Add your logic here...

      // Optionally, you could delete the message from the SQS queue after successful processing
      // This happens automatically if the function returns successfully (default behavior).

    } catch (error) {
      console.error('Error processing SQS message:', error);
      // Optionally, you can send the message to a dead-letter queue if necessary.
    }
  }

  return {
    statusCode: 200,
    body: JSON.stringify({ message: 'Order messages processed successfully!' }),
  };
};

// Fetch all orders from DynamoDB
module.exports.getOrders = async (event) => {
  const params = {
    TableName: 'Orders',
  };

  try {
    const result = await dynamoDB.scan(params).promise();
    return {
      statusCode: 200,
      body: JSON.stringify(result.Items),
    };
  } catch (error) {
    console.error(error);
    return {
      statusCode: 500,
      body: JSON.stringify({ message: 'Error fetching orders' }),
    };
  }
};
