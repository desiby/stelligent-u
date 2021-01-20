const AWS = require('aws-sdk');
const { v4: uuidv4 } = require('uuid');
// Set the region 
AWS.config.update({region: 'us-east-1'});

//check if credentials are set
AWS.config.getCredentials(function(err) {
    if (err) console.log(err.stack);
    else {
      console.log("Access key:", AWS.config.credentials.accessKeyId);
    }
  });

// Create the DynamoDB service object
const documentClient = new AWS.DynamoDB.DocumentClient();

//lambda function handler
exports.handler = async (event) => {
    
    const { product_name } = JSON.parse(event.body);
    
    const params = {
        TableName: 'Product',
        Item: {
          Id : uuidv4(),
          Product_Name : product_name
        }
      };
      try {
        // Utilising the put method to insert an item into the table (https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GettingStarted.NodeJs.03.html#GettingStarted.NodeJs.03.01)
        const data = await documentClient.put(params).promise();
        const response = {
          statusCode: 200
        };
        return response; // Returning a 200 if the item has been inserted 
      } catch (e) {
        return {
          statusCode: 500,
          body: JSON.stringify(e)
        };
      }
    };