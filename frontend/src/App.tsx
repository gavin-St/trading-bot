import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import { TradingBotLandingComponent } from './components/trading-bot-landing'
import { TradingBotAccountsComponent } from './components/trading-bot-accounts'

function App() {

  return (
    <div className='flex justify-center w-full items-center'>
      <TradingBotAccountsComponent/>
    </div>
  )
}

export default App
