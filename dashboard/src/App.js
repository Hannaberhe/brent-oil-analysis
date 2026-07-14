import React, { useState, useEffect } from 'react';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer, ReferenceLine } from 'recharts';

function App() {
  const [prices, setPrices] = useState([]);
  const [events, setEvents] = useState([]);
  const [stats, setStats] = useState({});
  const [changepoints, setChangepoints] = useState({});

  useEffect(() => {
    fetch('http://localhost:5000/api/prices').then(r => r.json()).then(setPrices);
    fetch('http://localhost:5000/api/events').then(r => r.json()).then(setEvents);
    fetch('http://localhost:5000/api/stats').then(r => r.json()).then(setStats);
    fetch('http://localhost:5000/api/changepoints').then(r => r.json()).then(setChangepoints);
  }, []);

  const keyDates = ['1990-08-03', '2008-09-15', '2020-03-06', '2022-02-24'];

  return (
    <div style={{padding: 30, fontFamily: 'Arial', maxWidth: 1200, margin: 'auto'}}>
      <h1 style={{color: '#1a237e'}}>Brent Oil Price Analysis Dashboard</h1>
      <p>Birhan Energies - Change Point Detection Results</p>

      <div style={{display: 'flex', gap: 20, marginBottom: 30}}>
        <div style={{background: '#e3f2fd', padding: 20, borderRadius: 10, flex: 1}}>
          <h3>Min Price</h3>
          <h2>${stats.min?.toFixed(2)}</h2>
        </div>
        <div style={{background: '#e8f5e9', padding: 20, borderRadius: 10, flex: 1}}>
          <h3>Max Price</h3>
          <h2>${stats.max?.toFixed(2)}</h2>
        </div>
        <div style={{background: '#fff3e0', padding: 20, borderRadius: 10, flex: 1}}>
          <h3>Mean Price</h3>
          <h2>${stats.mean?.toFixed(2)}</h2>
        </div>
        <div style={{background: '#fce4ec', padding: 20, borderRadius: 10, flex: 1}}>
          <h3>Change Points</h3>
          <h2>{changepoints.count || 30}</h2>
        </div>
      </div>

      <div style={{background: 'white', padding: 20, borderRadius: 10, marginBottom: 30}}>
        <h3>Price History with Change Points</h3>
        <ResponsiveContainer width="100%" height={400}>
          <LineChart data={prices.slice(-500)}>
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="date" tick={{fontSize: 10}} />
            <YAxis />
            <Tooltip />
            <Legend />
            <Line type="monotone" dataKey="price" stroke="#1a237e" dot={false} name="Brent Oil Price" />
            {keyDates.map(d => (
              <ReferenceLine key={d} x={d} stroke="red" strokeDasharray="3 3" label="" />
            ))}
          </LineChart>
        </ResponsiveContainer>
      </div>

      <div style={{background: 'white', padding: 20, borderRadius: 10}}>
        <h3>Major Events Timeline</h3>
        <table style={{width: '100%', borderCollapse: 'collapse'}}>
          <thead>
            <tr style={{background: '#1a237e', color: 'white'}}>
              <th style={{padding: 10}}>Date</th>
              <th style={{padding: 10}}>Event</th>
              <th style={{padding: 10}}>Description</th>
            </tr>
          </thead>
          <tbody>
            {events.map((e, i) => (
              <tr key={i} style={{background: i % 2 === 0 ? '#f5f5f5' : 'white'}}>
                <td style={{padding: 10}}>{e.date}</td>
                <td style={{padding: 10, fontWeight: 'bold'}}>{e.event}</td>
                <td style={{padding: 10}}>{e.description}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default App;
