import React, { useState, useEffect } from 'react';
import axios from 'axios';

const API_BASE = "https://8ew2pse1t4.execute-api.us-east-1.amazonaws.com/dev";

function App() {
  const [orders, setOrders] = useState([]);
  const [product, setProduct] = useState('');
  const [quantity, setQuantity] = useState(1);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  // Fetch orders from API
  const fetchOrders = async () => {
    setLoading(true);
    setError(null); // Reset error state before making the request
    try {
      const response = await axios.get(`${API_BASE}/orders`);
      setOrders(response.data);
    } catch (err) {
      setError("Error fetching orders");
    } finally {
      setLoading(false);
    }
  };

  // Create a new order
  const createOrder = async () => {
    setLoading(true);
    setError(null); // Reset error state before making the request
    try {
      await axios.post(`${API_BASE}/orders`, { product, quantity });
      fetchOrders(); // Refresh the orders list after creating a new order
    } catch (err) {
      setError("Error creating order");
    } finally {
      setLoading(false);
    }
  };

  // UseEffect to fetch orders on initial load
  useEffect(() => {
    fetchOrders();
  }, []);

  return (
    <div className="App">
      <h2>Order Microservice</h2>
      
      {/* Loading state message */}
      {loading && <p>Loading...</p>}

      {/* Error state message */}
      {error && <p style={{ color: 'red' }}>{error}</p>}

      {/* Form to create order */}
      <input 
        value={product} 
        onChange={e => setProduct(e.target.value)} 
        placeholder="Product" 
      />
      <input 
        type="number" 
        value={quantity} 
        onChange={e => setQuantity(Number(e.target.value))} 
      />
      <button onClick={createOrder}>Create Order</button>

      {/* List of orders */}
      <ul>
        {orders.length > 0 ? (
          orders.map(o => (
            <li key={o.id}>{o.product} - {o.quantity}x</li>
          ))
        ) : (
          <p>No orders found</p>
        )}
      </ul>
    </div>
  );
}

export default App;

