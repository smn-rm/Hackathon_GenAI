<template>
  <div :class="$style.home">
    <img :class="$style.introIcon" alt="" src="/intro@2x.png" />
    <div :class="$style.introductioncontent">
      <div :class="$style.servicetext">
        <b :class="$style.service">SERVICE</b>
        <div :class="$style.weEmpowerYour">
          We empower your financial journey as an international student in
          Germany with our innovative chatbot, providing personalized and expert
          financial information's to help you navigate and optimize your
          budgeting, savings, and financial well-being throughout your academic
          experience.
        </div>
      </div>
      <div :class="$style.servicebulletlist">
        <b :class="$style.service">TOPICS</b>
        <div :class="$style.funcitonlist">
          <div :class="$style.income">
            <b :class="$style.service">Income</b>
            <div :class="$style.bullet1">
              <img :class="$style.bullet1Child" alt="" src="/worker.png" />
              <div :class="$style.workingStudentJobs">Working Student Jobs</div>
            </div>
            <div :class="$style.bullet1">
              <img :class="$style.bullet1Child" alt="" src="/aktien.png" />
              <div :class="$style.workingStudentJobs">
                Scholarship and grants
              </div>
            </div>
          </div>
          <div :class="$style.income">
            <b :class="$style.service">Costs</b>
            <div :class="$style.bullet1">
              <img :class="$style.bullet1Child" alt="" src="/essen.png" />
              <div :class="$style.workingStudentJobs">Food & Beverages</div>
            </div>
            <div :class="$style.bullet1">
              <img :class="$style.bullet1Child" alt="" src="/frame-5@2x.png" />
              <div :class="$style.workingStudentJobs">Health insurance</div>
            </div>
          </div>
        </div>
      </div>
      <div :class="$style.chatbuttons">
        <b :class="$style.service">YOUR FIRST QUESTION</b>
        <button
          :class="$style.button1"
          message="What possibilities do I have to earn money?"
          @click="onButton1Click"
        >
          <div :class="$style.whatPossibilitiesDo">
            What possibilities do I have to earn money?
          </div>
        </button>
        <button
          :class="$style.button1"
          message="Where can I get a health insurance as a Chinese citizen for my 2-year stay?"
          @click="onButton2Click"
        >
          <div :class="$style.whatPossibilitiesDo">
            Where can I get a health insurance as a Chinese citizen for my
            2-year stay?
          </div>
        </button>
        <button
          :class="$style.button1"
          message="What are most costsaving tips for students in Germany?"
          @click="onButton3Click"
        >
          <div :class="$style.whatPossibilitiesDo">
            What are most costsaving tips for students in Germany?
          </div>
        </button>
        <button
          :class="$style.button1"
          message="What taxes I have to pay in Germany?"
          @click="onButton4Click"
        >
          <div :class="$style.whatPossibilitiesDo">
            What taxes I have to pay in Germany?
          </div>
        </button>
      </div>
    </div>
    <header :class="$style.header">
      <div :class="$style.header">
        <button :class="$style.buttonlang">
          <div :class="$style.en">EN</div>
          <img
            :class="$style.expandArrowIcon"
            alt=""
            src="/expand-arrow@2x.png"
          />
        </button>
        <div :class="$style.menu">
          <button :class="$style.home1">Home</button>
          <button :class="$style.chat" @click="onChatClick">Chat</button>
          <button :class="$style.trends" @click="onTrendsClick">Trends</button>
        </div>
      </div>
      <button :class="$style.home2" @click="onHome1Click" />
    </header>
  </div>
</template>
<script>
  import { defineComponent } from "vue";
  import axios from 'axios';

  export default defineComponent({
    name: "Home",
    methods: {
      onButton1Click() {
        const path = 'http://localhost:5000/chatbot'
        var inputText = "What possibilities do I have to earn money?"
        axios.post(path, { text: inputText})
            .then((res) => {
                console.log(res.data);  
            })
            .catch((error) => {
            console.error(error);
            });
        this.$router.push("/chat");
      },
      onButton2Click() {
        const path = 'http://localhost:5000/chatbot'
        var inputText = "Where can I get a health insurance as a Chinese citizen for my 2-year stay?"
        axios.post(path, { text: inputText})
            .then((res) => {
                console.log(res.data);  
            })
            .catch((error) => {
            console.error(error);
            });
        this.$router.push("/chat");
      },
      onButton3Click() {
        const path = 'http://localhost:5000/chatbot'
        var inputText = "What are most costsaving tips for students in Germany?"
        axios.post(path, { text: inputText})
            .then((res) => {
                console.log(res.data);  
            })
            .catch((error) => {
            console.error(error);
            });
        this.$router.push("/chat");
      },
      onButton4Click() {
        const path = 'http://localhost:5000/chatbot'
        var inputText = "What taxes I have to pay in Germany?"
        axios.post(path, { text: inputText})
            .then((res) => {
                console.log(res.data);  
            })
            .catch((error) => {
            console.error(error);
            });
        this.$router.push("/chat");
      },
      onChatClick() {
        this.$router.push("/chat");
      },
      onTrendsClick() {
        this.$router.push("/trends");
      },
      onHome1Click() {
        this.$router.push("/");
      },
    },
  });
</script>
<style module>
  .introIcon {
    position: absolute;
    height: 100%;
    width: 100%;
    top: 0rem;
    right: 0rem;
    bottom: 0rem;
    left: 0rem;
    max-width: 100%;
    overflow: hidden;
    max-height: 100%;
    object-fit: cover;
  }
  .service {
    align-self: stretch;
    position: relative;
  }
  .weEmpowerYour {
    align-self: stretch;
    position: relative;
    font-size: var(--font-size-11xl);
    color: var(--color-darkslategray);
  }
  .servicetext {
    align-self: stretch;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
  }
  .bullet1Child {
    position: relative;
    width: 6rem;
    height: 6rem;
    overflow: hidden;
    flex-shrink: 0;
    object-fit: cover;
  }
  .workingStudentJobs {
    position: relative;
  }
  .bullet1 {
    overflow: hidden;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: center;
    gap: var(--gap-3xs);
  }
  .income {
    align-self: stretch;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: center;
    gap: var(--gap-3xs);
  }
  .funcitonlist {
    align-self: stretch;
    flex: 1;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: center;
    gap: var(--gap-81xl);
    font-size: var(--font-size-11xl);
    color: var(--color-darkslategray);
  }
  .servicebulletlist {
    align-self: stretch;
    height: 19.44rem;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
  }
  .whatPossibilitiesDo {
    position: relative;
    font-size: var(--font-size-11xl);
    font-family: var(--font-segoe-ui);
    color: var(--color-darkslategray);
    text-align: center;
  }
  .button1 {
    cursor: pointer;
    border: 2px solid var(--color-lightsteelblue);
    padding: var(--padding-3xs) var(--padding-xl);
    background-color: var(--color-lavender);
    border-radius: var(--br-6xl);
    overflow: hidden;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: center;
  }
  .chatbuttons {
    align-self: stretch;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: var(--gap-3xs);
  }
  .introductioncontent {
    position: absolute;
    width: 52.81%;
    top: 0.06rem;
    right: 23.44%;
    left: 23.75%;
    height: 84.5rem;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: var(--gap-81xl);
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
  .home1 {
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
  .chat {
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
  .home2 {
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
    height: 5rem;
  }
  .home {
    position: relative;
    background-color: var(--color-white);
    width: 100%;
    height: 100vh;
    overflow: hidden;
    text-align: center;
    font-size: var(--font-size-5xl);
    color: var(--color-royalblue);
    font-family: var(--font-segoe-ui);
  }
</style>
