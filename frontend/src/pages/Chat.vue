<template>
  <div :class="$style.chat">
    <div :class="$style.sidebar">
      <div :class="$style.chatHistory">
        <div :class="$style.headhistory">
          <div :class="$style.yourChats">Your Chats</div>
          <div :class="$style.line" />
        </div>
        <div :class="$style.history">
          <button :class="$style.buttonnew">
            <div :class="$style.text">
              <div :class="$style.newChat">New Chat</div>
              <img :class="$style.pencilIcon" alt="" src="/pencil@2x.png" />
            </div>
          </button>
          <div :class="$style.line1" />
          <button :class="$style.buttonhistory1">
            <div :class="$style.text1">
              <div :class="$style.bafg">Bafög</div>
            </div>
          </button>
          <button :class="$style.buttonnew">
            <div :class="$style.text1">
              <div :class="$style.bafg">Jobs</div>
            </div>
          </button>
        </div>
      </div>
      <div :class="$style.frame">
        <div :class="$style.line2" />
        <img :class="$style.vectorIcon" alt="" src="/vector.svg" />
        <div :class="$style.bernhardH">Bernhard H.</div>
      </div>
    </div>
    <div :class="$style.chatwindow">
      <div :class="$style.chatarea">
        <div :class="$style.chat1" id="chatScroll">
          <div :class="$style.messages" v-for="message in history">
            <div v-if="message.from=='Human'" :class="$style.chatmessage1">
              <div :class="$style.whereCanIFindDiscountCodeWrapper">
                <div :class="$style.whereCanI">
                  {{ message.content }}
                </div>
              </div>
            </div>
            <div v-if="message.from=='AI'" :class="$style.chatmessage2">
              <div :class="$style.thereAreVariousWaysToFindWrapper">
                <div :class="$style.thereAreVarious">
                  {{ message.content }}
                </div>
              </div>
            </div>
          </div>
        </div>
        <div :class="$style.inputarea">
          <input
            v-model="inputText"
            v-on:keyup.enter="onEnter()"
            :class="$style.input"
            id="chatInput"
            placeholder="Type your message here..."
            type="text"
          />
          <button :class="$style.inputareaInner" @click="submitText()">
            <img :class="$style.frameChild" alt="" src="/arrow-2.svg" />
          </button>
        </div>
      </div>
    </div>
    <header :class="$style.header">
      <div :class="$style.content">
        <button :class="$style.buttonlang">
          <div :class="$style.en">EN</div>
          <img
            :class="$style.expandArrowIcon"
            alt=""
            src="/expand-arrow@2x.png"
          />
        </button>
        <div :class="$style.menu">
          <button :class="$style.home" @click="onHomeClick">Home</button>
          <button :class="$style.chat2">Chat</button>
          <button :class="$style.trends" @click="onTrendsClick">Trends</button>
        </div>
      </div>
      <button :class="$style.home1" @click="onHome1Click" />
    </header>
  </div>
</template>
<script>
  import axios from 'axios';
  import { defineComponent } from "vue";

  export default defineComponent({
    name: "Chat",
    data() {
            return {
            msg: '',
            inputText: '',
            history: [],
            };
    },
    methods: {
      onEnter: function() {
        this.submitText();
      },
      onHomeClick() {
        this.$router.push("/");
      },
      onTrendsClick() {
        this.$router.push("/trends");
      },
      onHome1Click() {
        this.$router.push("/");
      },
      getMessage() {
        const path = 'http://localhost:5000/chatbot';
        axios.get(path)
            .then((res) => {
            this.history = res.data;
            console.log(this.history)
            })
            .catch((error) => {

            console.error(error);
            });
            },
      submitText() {
        this.history.push({from: "Human", content: this.inputText})
        const path = 'http://localhost:5000/chatbot'
        axios.post(path, { text: this.inputText})
            .then((res) => {
                console.log(res.data);
                this.history = res.data;  
            })
            .catch((error) => {
            console.error(error);
            });
        this.inputText = "";
        chatInput.value = "";
      },
    },
    created() {
            this.getMessage();
        },
    updated() {
      var scrollableDiv = document.getElementById('chatScroll');
      scrollableDiv.scrollTop = scrollableDiv.scrollHeight;
    },
  });
</script>
<style module>
  .yourChats {
    position: absolute;
    top: 0.56rem;
    left: 7.13rem;
    display: inline-block;
    width: 11.38rem;
    height: 2rem;
  }
  .line {
    position: absolute;
    top: 2.88rem;
    left: -0.06rem;
    border-top: 2px solid var(--color-lightsteelblue);
    box-sizing: border-box;
    width: 18.63rem;
    height: 0.13rem;
  }
  .headhistory {
    position: relative;
    width: 19rem;
    height: 2.94rem;
  }
  .newChat {
    position: relative;
    font-size: var(--font-size-11xl);
    font-family: var(--font-segoe-ui);
    color: var(--color-darkslategray);
    text-align: center;
  }
  .pencilIcon {
    position: relative;
    width: 1.56rem;
    height: 1.56rem;
    object-fit: cover;
  }
  .text {
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: flex-start;
    gap: var(--gap-xl);
  }
  .buttonnew {
    cursor: pointer;
    border: 2px solid var(--color-darkgray);
    padding: var(--padding-4xs) 0rem;
    background-color: var(--color-white);
    border-radius: var(--br-xl);
    box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
    box-sizing: border-box;
    width: 19.31rem;
    display: flex;
    flex-direction: row;
    align-items: flex-start;
    justify-content: center;
  }
  .line1 {
    position: relative;
    border-top: 2px solid var(--color-lightsteelblue);
    box-sizing: border-box;
    width: 18.63rem;
    height: 0.13rem;
  }
  .bafg {
    align-self: stretch;
    flex: 1;
    position: relative;
    font-size: var(--font-size-11xl);
    font-family: var(--font-segoe-ui);
    color: var(--color-darkslategray);
    text-align: center;
    display: flex;
    align-items: center;
    justify-content: center;
  }
  .text1 {
    width: 18.68rem;
    height: 1.98rem;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: flex-start;
  }
  .buttonhistory1 {
    cursor: pointer;
    border: 2px solid var(--color-darkgray);
    padding: var(--padding-4xs) 0rem;
    background-color: var(--color-white);
    border-radius: var(--br-xl);
    box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
    box-sizing: border-box;
    width: 19.31rem;
    overflow: hidden;
    display: flex;
    flex-direction: row;
    align-items: flex-start;
    justify-content: center;
  }
  .history {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: flex-start;
    padding: 0rem var(--padding-3xs);
    gap: 1.63rem;
  }
  .chatHistory {
    position: absolute;
    top: 0rem;
    left: 0rem;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: flex-start;
    gap: 2.63rem;
  }
  .line2 {
    position: absolute;
    top: 1.5rem;
    left: -0.06rem;
    border-top: 2px solid var(--color-lightsteelblue);
    box-sizing: border-box;
    width: 18.63rem;
    height: 0.13rem;
  }
  .vectorIcon {
    position: absolute;
    height: 43.96%;
    width: 23.76%;
    top: 32.42%;
    right: 66.34%;
    bottom: 23.63%;
    left: 9.9%;
    max-width: 100%;
    overflow: hidden;
    max-height: 100%;
  }
  .bernhardH {
    position: absolute;
    top: 4.94rem;
    left: 8.38rem;
  }
  .frame {
    position: absolute;
    top: 80%;
    left: 0rem;
    width: 18.94rem;
    height: 11.38rem;
    overflow: hidden;
    text-align: left;
  }
  .sidebar {
    position: absolute;
    height: calc(100% - 80px);
    top: 5rem;
    bottom: 0rem;
    left: 0rem;
    background-color: var(--color-whitesmoke-100);
    width: 20.44rem;
  }
  .messages {
    width: inherit;
  }

  .whereCanI {
    word-wrap: break-word;
    align-self: stretch;
    position: relative;
    display: inline-block;
    max-width: 1000px;
    flex-shrink: 0;
  }
  .whereCanIFindDiscountCodeWrapper {
    border-radius: var(--br-31xl);
    background-color: var(--color-lavender);
    border: 2px solid var(--color-lightsteelblue);
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: center;
    padding: var(--padding-xl);
  }
  .chatmessage1 {
    float: right;
    width: 100%;
    align-self: stretch;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: flex-end;
    padding: 0rem 0rem 0rem var(--padding-481xl);
  }
  .thereAreVarious {
    word-wrap: break-word;
    align-self: stretch;
    position: relative;
    display: inline-block;
    max-width: 1000px;
    flex-shrink: 0;
  }
  .thereAreVariousWaysToFindWrapper {
    border-radius: var(--br-31xl);
    background-color: var(--color-white);
    border: 2px solid var(--color-silver);
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: center;
    padding: var(--padding-xl);
  }
  .chatmessage2 {
    width: 95.13rem;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: flex-start;
    padding: 0rem var(--padding-481xl) 0rem 0rem;
    box-sizing: border-box;
  }
  .chat1 {
    width: 100%;
    align-self: stretch;
    flex: 1;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: flex-start;
    padding: 3.13rem 0rem 0rem 0rem;
    gap: var(--gap-31xl);
    overflow-y: scroll;
    overflow-x: hidden;
  }
  .input {
    border: 3px solid var(--color-silver);
    outline: none;
    font-family: var(--font-segoe-ui);
    font-size: var(--font-size-11xl);
    background-color: var(--color-white);
    align-self: stretch;
    flex: 1;
    border-radius: var(--br-6xl);
    overflow: hidden;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: flex-start;
    padding: var(--padding-7xs) 1rem;
    color: black;
  }
  .frameChild {
    position: relative;
    max-height: 100%;
    width: 2.44rem;
  }
  .inputareaInner {
    border-radius: 100px;
    background-color: var(--color-royalblue);
    width: 4.69rem;
    height: 4.69rem;
    overflow: hidden;
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
  }
  .inputarea {
    width: 100%;
    align-self: stretch;
    height: 4.69rem;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: flex-start;
    gap: var(--gap-xl);
  }
  .chatarea {
    position: absolute;
    height: calc(100% - 57px);
    width: calc(100% - 650px);
    margin: right = 0;
    top: 0rem;
    right: 25.25rem;
    bottom: 3.56rem;
    left: 19.19rem;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: flex-start;
  }
  .chatwindow {
    position: absolute;
    height: calc(100% - 79px);
    width: calc(100% - 327px);
    top: 4.94rem;
    right: 0rem;
    bottom: 0rem;
    left: 20.44rem;
    background-color: #f4f4f4;
    border-top: 3px solid var(--color-lightsteelblue);
    border-left: 3px solid var(--color-lightsteelblue);
    box-sizing: border-box;
    text-align: left;
    color: var(--color-darkslategray);
  }
  .en {
    align-self: stretch;
    flex: 1;
    position: relative;
    font-size: var(--font-size-5xl);
    font-weight: 300;
    font-family: var(--font-inter);
    color: var(--color-darkslategray);
    text-align: center;
    display: flex;
    align-items: center;
    justify-content: center;
  }
  .expandArrowIcon {
    align-self: stretch;
    flex: 1;
    position: relative;
    max-width: 100%;
    overflow: hidden;
    max-height: 100%;
    object-fit: cover;
  }
  .buttonlang {
    cursor: pointer;
    border: 3px solid var(--color-lightsteelblue);
    padding: var(--padding-3xs) var(--padding-7xs);
    background-color: transparent;
    position: absolute;
    top: 0.56rem;
    right: 0.63rem;
    border-radius: var(--br-3xs);
    box-sizing: border-box;
    width: 5.25rem;
    height: 3.94rem;
    overflow: hidden;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: center;
  }
  .home {
    cursor: pointer;
    border: none;
    padding: 0;
    background-color: transparent;
    align-self: stretch;
    position: relative;
    font-size: var(--font-size-11xl);
    font-weight: 700;
    font-family: var(--font-segoe-ui);
    color: var(--color-darkslategray);
    text-align: center;
    display: flex;
    align-items: center;
    justify-content: center;
    width: 5.38rem;
    flex-shrink: 0;
  }
  .chat2 {
    cursor: pointer;
    border: none;
    padding: 0;
    background-color: transparent;
    align-self: stretch;
    position: relative;
    font-size: var(--font-size-11xl);
    font-weight: 700;
    font-family: var(--font-segoe-ui);
    color: var(--color-darkslategray);
    text-align: center;
    display: flex;
    align-items: center;
    justify-content: center;
    width: 4.06rem;
    flex-shrink: 0;
  }
  .trends {
    cursor: pointer;
    border: none;
    padding: 0;
    background-color: transparent;
    align-self: stretch;
    position: relative;
    font-size: var(--font-size-11xl);
    font-weight: 700;
    font-family: var(--font-segoe-ui);
    color: var(--color-darkslategray);
    text-align: center;
    display: flex;
    align-items: center;
    justify-content: center;
    width: 5.94rem;
    flex-shrink: 0;
  }
  .menu {
    position: absolute;
    top: 0.13rem;
    left: calc(50% - 152.8px);
    height: 4.88rem;
    overflow: hidden;
    display: flex;
    flex-direction: row;
    align-items: flex-start;
    justify-content: flex-start;
    gap: var(--gap-11xl);
  }
  .content {
    position: absolute;
    width: 100%;
    top: 0rem;
    right: 0rem;
    left: 0rem;
    height: 5rem;
  }
  .home1 {
    cursor: pointer;
    border: none;
    padding: 0;
    background-color: transparent;
    position: absolute;
    top: 0.38rem;
    left: 4.25rem;
    width: 12.38rem;
    height: 4.38rem;
    overflow: hidden;
    background-image: url("/home@3x.png");
    background-size: cover;
    background-repeat: no-repeat;
    background-position: top;
  }
  .header {
    position: absolute;
    width: 100%;
    top: 0rem;
    right: 0rem;
    left: 0rem;
    background-color: var(--color-whitesmoke-100);
    height: 5rem;
  }
  .chat {
    position: relative;
    background-color: #c4c4c4;
    width: 100%;
    height: 100vh;
    overflow: hidden;
    text-align: right;
    font-size: var(--font-size-11xl);
    color: var(--color-black);
    font-family: var(--font-segoe-ui);
  }
</style>
