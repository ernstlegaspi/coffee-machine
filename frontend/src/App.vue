<script setup>
  import { onMounted, onUnmounted, ref, watch } from 'vue'
  import { PaperAirplaneIcon } from '@heroicons/vue/24/solid'

  const BASE_URL = 'http://localhost:8000/api/coffee/'

  // assume ID = 1 since we have only 1 Coffee Machine
  const COFFEE_MACHINE_ID = 1

  const chat = ref('')
  const prevChat = ref('')
  const chatSubmitted = ref(false)

  let chatbox = null
  let chatboxCanvas = null

  const windowWidth = ref(window.innerWidth)

  const scrollToBottom = () => {
    chatboxCanvas.scrollTo({ behavior: 'smooth', top: chatboxCanvas.scrollHeight })
  }

  const numberButtonClick = async type => {
    try {
      const res = await fetch(
        `${BASE_URL}`,
        {
          method: 'PATCH',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            coffee_machine_id: COFFEE_MACHINE_ID,
            type
          })
        }
      )

      const body = await res.json()

      alert(
        body?.detail ? body.detail
        : body?.message.replace('_', ' ')
      )
    } catch(e) {
      alert('Unable to make your Coffee. Try again later.')
    }
  }

  const sendClick = () => {
    if(!chatbox || !chat.value) return

    const div = document.createElement('div')
    div.classList.add('user-chat')

    const p = document.createElement('p')
    p.innerHTML = chat.value

    div.appendChild(p)

    chatbox.appendChild(div)

    prevChat.value = chat.value
    chat.value = ''

    scrollToBottom()

    chatSubmitted.value = true
  }

  watch(chatSubmitted, async (newVal, oldVal) => {
    if(!chatSubmitted.value) return

    const div = document.createElement('div')
    div.classList.add('chat')

    switch(prevChat.value) {
      case '1':
        div.innerHTML = `
          <img
            alt='Robot'
            src='/robot.png'
          />

          <div class='chat-content'>
            <p>Click <strong>1</strong> to order <strong>Espresso</strong></p>
            <br />

            <p>Click <strong>2</strong> to order <strong>Double Espresso</strong></p>
            <br />

            <p>Click <strong>3</strong> to order <strong>Americano</strong></p>
          </div>
        `
        break
      case '2':
        try {
          const res = await fetch(`${BASE_URL}${COFFEE_MACHINE_ID}/status/`)
          const body = await res.json()

          div.innerHTML = `
            <img
              alt='Robot'
              src='/robot.png'
            />

            <div class='chat-content'>
              <p>Coffee Container: <strong>${body.coffee_amount}</strong></p>
              <br />
              <p>Water Container: <strong>${body.water_amount}</strong></p>
            </div>
          `
        } catch(e) {
          alert('Unable to show the status. Try again later.')
        }
        break

      case '3':
        try {
          const res = await fetch(
            `${BASE_URL}${COFFEE_MACHINE_ID}/refill-coffee/`,
            {
              method: 'PATCH'
            }
          )
          const body = await res.json()

          div.innerHTML = `
            <img
              alt='Robot'
              src='/robot.png'
            />

            <div class='${body.detail ? "chat-content-angry" : "chat-content"}'>
              <p>${body.detail ? body.detail : body.message}</p>
            </div>
          `
        } catch(e) {
          alert('Unable to refill Coffee Container. Try again later.')
        }
        break

      case '4':
        try {
          const res = await fetch(
            `${BASE_URL}${COFFEE_MACHINE_ID}/refill-water/`,
            {
              method: 'PATCH'
            }
          )
          const body = await res.json()

          div.innerHTML = `
            <img
              alt='Robot'
              src='/robot.png'
            />

            <div class='${body.detail ? "chat-content-angry" : "chat-content"}'>
              <p>${body.detail ? body.detail : body.message}</p>
            </div>
          `
        } catch(e) {
          alert('Unable to refill Water Container. Try again later.')
        }
        break
      default:
        div.innerHTML = `
          <img
            alt='Robot'
            src='/robot.png'
          />

          <div class='chat-content-angry'>
            <p>Not in the choices!</p>
          </div>
        `
    }

    chatbox.appendChild(div)
    scrollToBottom()

    chatSubmitted.value = false
  })

  onMounted(() => {
    chatbox = document.getElementById('chatbox')
    chatboxCanvas = document.getElementById('chatbox-canvas')
    window.addEventListener('resize', updateWidth)
  })

  const updateWidth = () => {
    windowWidth.value = window.innerWidth
  }

  onUnmounted(() => {
    window.removeEventListener('resize', updateWidth)
  })
</script>

<template>
  <div v-if='windowWidth < 531' class='not-avail'>
    <p>Our Coffee Machine is not available on this device. Sorry! 🙇‍♀️</p>
  </div>
  <div v-else class='body'>
    <div class='coffee-machine'>
      <div class='top'>
        <div class='inner'>
          <div class='coffee-buttons'>
            <button @click="numberButtonClick('espresso')">1</button>
            <button @click="numberButtonClick('double_espresso')">2</button>
            <button @click="numberButtonClick('americano')">3</button>
          </div>
        </div>
      </div>

      <div class='middle'>
        <div class='coffee-hole-handle'>
          <div class='inner'></div>
        </div>
        <div class='coffee-hole'>
          <div class='inner'></div>
        </div>

        <div class='random'></div>

        <div class='shadow1'></div>
        <div class='shadow2'></div>
        <div class='shadow3'></div>
        <div class='shadow4'></div>
      </div>

      <img
        alt='Mug'
        src='/mug.png'
      />

      <div class='mug-shadow'></div>
      <div class='mug-shadow2'></div>

      <div class='bottom'>
        <div class='inner'></div>
      </div>
      <div class='left-foot'>
        <div class='inner'></div>
      </div>
      <div class='right-foot'>
        <div class='inner'></div>
      </div>
    </div>

    <div class='coffee-machine-shadow'></div>

    <div class='chatbot-box'>
      <div class='header'>
        <div class='robot'>
          <img
            alt='Robot'
            src='/robot.png'
          />
          <p>CoffeeBot</p>
        </div>
      </div>
      <div id='chatbox-canvas' class='middle'>
        <div id="chatbox" class='inner'>
          <div class='chat'>
            <img
              alt='Robot'
              src='/robot.png'
            />
            <p class="text">Hello, Coffee Lover! Here is a quick guide to our Cafe! 😊</p>
          </div>

          <div class='chat2'>
            <div>
              <p>
                Type '<strong>1</strong>' to show the <strong>Menu.</strong>
              </p>
              <br />
              <p>
                Type '<strong>2</strong>' to show the Status of the <strong>Coffee Machine</strong>.
              </p>
              <br />
              <p>Type '<strong>3</strong>' to refill the <strong>Coffee Container</strong></p>
              <br />
              <p>Type '<strong>4</strong>' to refill the <strong>Water Container</strong></p>
            </div>
          </div>
        </div>
      </div>
      <div class='bottom'>
        <input v-model='chat' type='text' placeholder='Reply to CoffeeBot' />

        <div @click="sendClick">
          <PaperAirplaneIcon class='send' />
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
  .not-avail {
    padding: 0 30px;
    text-align: center;
    margin: 0 auto;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
  }

  .body {
    background: linear-gradient(180deg, #f6ede3, #e9d5b8);
    min-height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    position: relative;
    z-index: 2;
  }

  .coffee-machine {
    width: 400px;
  }

  .coffee-machine .top {
    width: 100%;
    height: 100px;
    border: 8px solid #2e3248;
    border-top-left-radius: 30px;
    border-top-right-radius: 30px;
    border-bottom-left-radius: 10px;
    border-bottom-right-radius: 10px;
    background: #555463;
    position: relative;
    z-index: 3;
  }

  .coffee-machine .top .inner {
    background: #3c3f50;
    border-top-left-radius: 30px;
    border-top-right-radius: 30px;
    border-bottom-right-radius: 5px;
    width: 98%;
    height: 95%;
    position: absolute;
    right: 0;
    bottom: 0;
    z-index: 2;
  }

  .coffee-machine .top .inner .coffee-buttons {
    display: flex;
    gap: 7px;
    margin: 12px 0 0 10px;
  }

  .coffee-machine .top .inner .coffee-buttons button {
    border-radius: 50px;
    border: 6px solid #1e2435;
    padding: 5px 10px;
    height: max-content;
    color: #fff;
    background: #2d2f60;
    cursor: pointer;
    transition: all .3s;
  }

  .coffee-machine .top .inner .coffee-buttons button:hover {
    background: #1e2435;
  }

  .coffee-machine .middle {
    height: 250px;
    background: #2f2c3d;
    width: 90%;
    border: 8px solid #1e2435;
    border-bottom: 0;
    margin-left: 20px;
    position: relative;
    z-index: 1;
  }

  .coffee-machine .middle .coffee-hole-handle {
    border: 8px solid #2e3248;
    background: #555463;
    position: absolute;
    z-index: 4;
    width: 60px;
    height: 23px;
    margin-left: 60px;
    margin-top: -10px;
    border-bottom-left-radius: 17px;
    border-bottom-right-radius: 17px;
    overflow: hidden;
  }

  .coffee-machine .middle .coffee-hole-handle .inner {
    background: #3c3f50;
    position: absolute;
    width: 100%;
    height: 100%;
    margin-left: 10px;
    border-bottom-left-radius: 10px;
  }

  .coffee-machine .middle .coffee-hole {
    width: 30px;
    height: 15px;
    position: absolute;
    z-index: 3;
    border: 6px solid #2e3248;
    background: #555463;
    border-bottom-left-radius: 10px;
    border-bottom-right-radius: 10px;
    margin-left: 77px;
    margin-top: 18px;
    overflow: hidden;
  }

  .coffee-machine .middle .coffee-hole .inner {
    background: #3c3f50;
    position: absolute;
    width: 100%;
    height: 100%;
    margin-left: 5px;
    border-bottom-left-radius: 10px;
  }

  .coffee-machine .middle .random {
    background: #2e3248;
    width: 50px;
    height: 18px;
    position: absolute;
    z-index: 2;
    border-radius: 30px;
    margin-left: 250px;
    margin-top: -10px;
  }

  .coffee-machine .middle .shadow1 {
    width: 100%;
    height: 20px;
    background: #1e2435;
    position: absolute;
    z-index: 1;
  }

  .coffee-machine .middle .shadow2 {
    width: 100px;
    height: 50px;
    background: #1e2435;
    position: absolute;
    z-index: 1;
    margin-top: 10px;
    margin-left: 95px;
    border-bottom-left-radius: 17px;
    border-bottom-right-radius: 17px;
  }

  .coffee-machine .middle .shadow3 {
    width: 50px;
    height: 20px;
    background: #1e2435;
    position: absolute;
    z-index: 1;
    margin-top: 53px;
    margin-left: 120px;
    border-bottom-left-radius: 10px;
    border-bottom-right-radius: 10px;
  }

  .coffee-machine .middle .shadow4 {
    width: 50px;
    height: 20px;
    background: #1e2435;
    position: absolute;
    z-index: 1;
    margin-top: 10px;
    margin-left: 280px;
    border-bottom-left-radius: 10px;
    border-bottom-right-radius: 10px;
  }

  .coffee-machine img {
    position: absolute;
    height: 200px;
    width: 200px;
    margin: -132px 0 0 30px;
    z-index: 5;
  }

  .coffee-machine .mug-shadow {
    background: #1e2435;
    width: 90px;
    height: 85px;
    border-radius: 100%;
    position: absolute;
    z-index: 4;
    margin: -83px 0 0 135px;
  }

  .coffee-machine .mug-shadow2 {
    background: #1e2435;
    width: 120px;
    height: 11px;
    position: absolute;
    z-index: 4;
    margin: 8px 0 0 90px;
    border-bottom-right-radius: 5px;
  }

  .coffee-machine .bottom {
    width: 100%;
    height: 30px;
    border: 8px solid #1e2435;
    border-bottom-left-radius: 10px;
    border-bottom-right-radius: 10px;
    border-top-left-radius: 10px;
    border-top-right-radius: 10px;
    background: #47455e;
    position: relative;
    z-index: 3;
    overflow: hidden;
  }

  .coffee-machine .bottom .inner {
    background: #3c3f50c2;
    width: 100%;
    height: 100%;
    margin-top: 15px;
  }

  .coffee-machine .left-foot {
    border: 8px solid #1e2435;
    width: 50px;
    height: 20px;
    background: #555463;
    margin-left: 70px;
    border-bottom-left-radius: 10px;
    border-bottom-right-radius: 10px;
    position: absolute;
    z-index: 3;
    margin-top: -5px;
    overflow: hidden;
  }

  .coffee-machine .left-foot .inner {
    background: #3c3f50;
    border-bottom-left-radius: 10px;
    width: 100%;
    height: 100%;
    margin-left: 5px
  }

  .coffee-machine .right-foot {
    border: 8px solid #1e2435;
    width: 50px;
    height: 20px;
    background: #555463;
    margin-left: 270px;
    border-bottom-left-radius: 10px;
    border-bottom-right-radius: 10px;
    position: absolute;
    z-index: 3;
    margin-top: -5px;
    overflow: hidden;
  }

  .coffee-machine .right-foot .inner {
    background: #3c3f50;
    border-bottom-left-radius: 10px;
    width: 100%;
    height: 100%;
    margin-left: 5px
  }

  .coffee-machine-shadow {
    position: absolute;
    border-radius: 10px;
    width: 500px;
    height: 20px;
    z-index: 2;
    background: #eecea5;
    margin-top: 460px;
    margin-left: 15px;
  }

  .chatbot-box {
    width: 250px;
    position: absolute;
    z-index: 6;
    right: 0;
    bottom: 0;
    margin: 0 10px 10px 0;
    box-shadow: 0 15px 10px rgba(0, 0, 0, .3);
  }

  .chatbot-box .header {
    background: #eecea5;
    border-top-left-radius: 10px;
    border-top-right-radius: 10px;
    padding: 7px 10px;
    color: #1e2435;
    display: flex;
    align-items: center;
    justify-content: space-between;
  }

  .chatbot-box .header .robot {
    display: flex;
    align-items: center;
  }

  :deep(.chatbot-box img) {
    width: 30px;
    height: 30px;
    background: #555463;
    border-radius: 100%;
  }

  .chatbot-box .header .robot p {
    margin: 5px 0 0 6px;
  }

  .chatbot-box .header .icon {
    width: 25px;
    height: 25px;
    cursor: pointer;
    margin-top: 5px;
  }

  .chatbot-box .middle {
    background: #fff;
    height: 0;
    width: 100%;
    overflow-x: hidden;
    overflow-y: scroll;
    color: #2e3248;
    animation: expand .3s forwards;
  }

  @keyframes expand {
    100% {
      height: 330px;
    }
  }

  .chatbot-box .middle .inner {
    padding: 10px;
  }

  :deep(.chat) {
    display: flex;
    margin-bottom: 10px;
    width: 90%;
  }

  .chatbot-box .middle .inner .chat .text,
  :deep(.chat-content),
  :deep(.chat-content-angry) {
    margin-left: 10px;
    background: #f9f2e9;
    border-radius: 5px;
    padding: 5px;
  }

  :deep(.chat-content-angry) {
    background: #f85757;
    color: #fff;
  }

  .chatbot-box .middle .inner .chat2 {
    width: 90%;
    margin-bottom: 10px;
  }

  .chatbot-box .middle .inner .chat2 div {
    margin-left: 40px;
    background: #f9f2e9;
    border-radius: 5px;
    padding: 5px;
  }

  :deep(.user-chat) {
    width: 100%;
    display: flex;
    justify-content: end;
    margin-bottom: 10px;
  }

  :deep(.user-chat p) {
    width: max-content;
    max-width: 65%;
    background: #2b2e8b;
    color: #fff;
    padding: 5px;
    border-radius: 5px;
  }

  .chatbot-box .bottom {
    width: 100%;
    display: flex;
    background: #fff;
    border-top: 1px solid #eecea5;
    align-items: center;
  }

  .chatbot-box .bottom input {
    border: 0;
    outline: none;
    width: 100%;
    box-sizing: border-box;
    padding: 10px;
    color: #2f2c3d;
  }

  .chatbot-box .bottom input::placeholder {
    color: rgb(179, 179, 179)
  }

  .chatbot-box .bottom div {
    cursor: pointer;
    width: 20px;
    height: 20px;
    margin-right: 5px;
  }

  .chatbot-box .bottom div .send {
    color: #1e2435;
    width: 20px;
  }

  ::-webkit-scrollbar {
    width: 6px;
  }

  ::-webkit-scrollbar-thumb {
    background: #2e3248;
  }
</style>
