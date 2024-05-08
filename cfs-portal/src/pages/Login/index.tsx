import React, { useState } from 'react';
import { TextField, Button, Typography, Container, CssBaseline, InputLabel, FormControl, OutlinedInput, useTheme } from '@mui/material';
import { ThemeContext } from '@emotion/react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';

const Login = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const theme = useTheme();
  const navigate = useNavigate();

  const handleUsernameChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setUsername(event.target.value);
  };

  const handlePasswordChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setPassword(event.target.value);
  };

  const handleLogin = async () => {
    axios.post(
      'http://10.255.41.31/osm/admin/v1/users/admin',
      {
        username: username,
        password: password
      }
    ).then(res => {
      console.log(res.data);
      navigateToDashboard();
    }).catch(err => {
      console.log(err);
    });
  };

  const navigateToDashboard = () => {
    navigate('/dashboard');
  };

  return (
    <div style={{ display: 'flex', height: '100vh' }}>
      <div style={{ flex: 1, background: '#d9d9d9', display: 'flex', justifyContent: 'flex-end' }}>
      </div>
      <div style={{ flex: 1, background: '#b6b6b6', display: 'flex', justifyContent: 'center', alignItems: 'center' }}>
        <Container
          component="main"
          maxWidth="xs">
          <CssBaseline />
          <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'flex-start', marginTop: '10px' }}>
            <Typography
              component="h1"
              variant="h5"
              style={{ fontWeight: 'bold', marginBottom: '10px', marginTop: '-10px' }}>
              Login
            </Typography>
            <form style={{ width: '100%', marginTop: '10px' }} noValidate>
              <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'flex-start', marginBottom: '10px', marginTop: '10px' }}>
                <FormControl fullWidth variant="outlined">
                  <InputLabel htmlFor="username-input">Username*</InputLabel>
                  <OutlinedInput
                    id="username-input"
                    value={username}
                    onChange={handleUsernameChange}
                    label="Username*"
                    style={{ backgroundColor: '#d9d9d9' }}
                  />
                </FormControl>
              </div>
              <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'flex-start', marginTop: '10px', marginBottom: '10px' }}>
                <FormControl fullWidth variant="outlined">
                  <InputLabel htmlFor="password-input">Password*</InputLabel>
                  <OutlinedInput
                    id="password-input"
                    value={password}
                    onChange={handlePasswordChange}
                    label="Password*"
                    type="password"
                    style={{ backgroundColor: '#d9d9d9' }}
                  />
                </FormControl>
              </div>
              <div style={{ display: 'flex', justifyContent: 'flex-end', width: '100%', marginTop: '25px' }}>
                <Button
                  type="button"
                  variant="contained"
                  style={{ fontSize: '15px', width: '40%', backgroundColor: theme.palette.primary.main, color: '#fff', textTransform: 'none', fontWeight: 'bold' }}
                  // onClick={handleLogin}>
                  onClick={handleLogin}>
                  Login
                </Button>
              </div>
            </form>
          </div>
        </Container>
      </div>
    </div>
  );
};

export default Login;