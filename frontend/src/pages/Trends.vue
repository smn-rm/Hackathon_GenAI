<template>
  <div :class="$style.trends">
    <img :class="$style.introIcon" alt="" src="/intro@2x.png" />
    <div :class="$style.trend">
      <div :class="$style.frameParent">
        <div :class="$style.trend1Parent">
          <div :class="$style.trend1">
            <div :class="$style.trend1Child" />
            <div :class="$style.trend1Item" />
            <img
              :class="$style.windTurbineIcon"
              alt=""
              src="/wind-turbine@2x.png"
            />
            <b :class="$style.energyPricesIn">Energy prices in Germany</b>
            <div :class="$style.risingEnergyPricesContainer">
              <ul :class="$style.risingEnergyPricesDueToGl">
                <li :class="$style.risingEnergyPrices">
                  Rising energy prices due to global developments and the
                  Ukraine conflict
                </li>
                <li>
                  While the electricity price peaked at 70 cents/kWh, it was be
                  38 cents/kWh for new customers in 2023 and slightly lower for
                  existing customers
                </li>
              </ul>
            </div>
          </div>
          <div :class="$style.trend1">
            <div :class="$style.trend1Child" />
            <div :class="$style.trend1Item" />
            <img :class="$style.increaseIcon" alt="" src="/increase@2x.png" />
            <b :class="$style.inflation">Inflation</b>
            <div :class="$style.inflationPeakedInContainer">
              <ul :class="$style.risingEnergyPricesDueToGl">
                <li :class="$style.risingEnergyPrices">
                  Inflation peaked in 2023 at an average of 8,8%
                </li>
                <li>At the the end of 2022 is at 3,2%</li>
              </ul>
            </div>
          </div>
        </div>
        <div :class="$style.trend1Parent">
          <div :class="$style.trend1">
            <div :class="$style.trend1Child" />
            <div :class="$style.trend1Item" />
            <img
              :class="$style.organicFoodIcon"
              alt=""
              src="/organic-food@2x.png"
            />
            <b :class="$style.farmerProtests">Farmer protests</b>
            <div :class="$style.farmersPubliclyProtestContainer">
              <ul :class="$style.risingEnergyPricesDueToGl">
                <li :class="$style.risingEnergyPrices">
                  Farmers publicly protest plans to cut subsidies
                </li>
                <li :class="$style.risingEnergyPrices">
                  concessions from the government were deemed insufficient by
                  farmers.
                </li>
                <li>
                  Removal of tax concessions, especially impacting small and
                  medium-sized farms, is seen as unjust, fueling continued
                  dissatisfaction.
                </li>
              </ul>
            </div>
          </div>
          <div :class="$style.trend4">
            <div :class="$style.trend1Child" />
            <div :class="$style.trend1Item" />
            <img
              :class="$style.fundAccountingIcon"
              alt=""
              src="/fund-accounting@2x.png"
            />
            <b :class="$style.howToBudget">How to budget</b>
            <div :class="$style.aBudgetHelpsContainer">
              <ul :class="$style.risingEnergyPricesDueToGl">
                <li :class="$style.risingEnergyPrices">
                  A Budget helps you in keeping an overview off your expenses.
                  Initailly there are two important steps
                </li>
                <li :class="$style.risingEnergyPrices">
                  Prioritize and Categorize Expenses
                </li>
                <li>Create and Stick to a Financial Plan</li>
              </ul>
            </div>
          </div>
        </div>
      </div>
      <div :class="$style.thisPageDisplays">
        This page displays current trends in the requests the Scholar$ has been
        asked recently.
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
          <button :class="$style.home" @click="onHomeClick">Home</button>
          <button :class="$style.chat" @click="onChatClick">Chat</button>
          <button :class="$style.trends1">Trends</button>
        </div>
      </div>
      <button :class="$style.home1" @click="onHome1Click" />
    </header>
  </div>
</template>
<script>
  import { defineComponent } from "vue";

  export default defineComponent({
    name: "Trends",
    methods: {
      onHomeClick() {
        this.$router.push("/");
      },
      onChatClick() {
        this.$router.push("/chat");
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
  .trend1Child {
    position: absolute;
    top: 0rem;
    left: 0rem;
    border-radius: var(--br-3xs);
    background-color: var(--color-whitesmoke-100);
    border: 2px solid var(--color-lightsteelblue);
    box-sizing: border-box;
    width: 46.88rem;
    height: 24.69rem;
  }
  .trend1Item {
    position: absolute;
    top: 7.5rem;
    left: -0.06rem;
    border-top: 2px solid var(--color-lightsteelblue);
    box-sizing: border-box;
    width: 47rem;
    height: 0.13rem;
  }
  .windTurbineIcon {
    position: absolute;
    top: 0.69rem;
    left: 1rem;
    width: 6rem;
    height: 6rem;
    object-fit: cover;
  }
  .energyPricesIn {
    position: absolute;
    top: 2.44rem;
    left: 12.19rem;
  }
  .risingEnergyPrices {
    margin-bottom: false;
  }
  .risingEnergyPricesDueToGl {
    margin: 0;
    font-family: inherit;
    font-size: inherit;
    padding-left: var(--padding-21xl);
  }
  .risingEnergyPricesContainer {
    position: absolute;
    top: 7.56rem;
    left: 2.38rem;
    text-align: left;
    display: flex;
    align-items: center;
    width: 43.13rem;
    height: 16.44rem;
  }
  .trend1 {
    position: relative;
    width: 46.88rem;
    height: 24.69rem;
    overflow: hidden;
    flex-shrink: 0;
  }
  .increaseIcon {
    position: absolute;
    top: 1rem;
    left: 0.94rem;
    width: 6rem;
    height: 6rem;
    object-fit: cover;
  }
  .inflation {
    position: absolute;
    top: 2.75rem;
    left: 19.69rem;
  }
  .inflationPeakedInContainer {
    position: absolute;
    top: 7.56rem;
    left: 0.94rem;
    text-align: left;
    display: flex;
    align-items: center;
    width: 44.63rem;
    height: 7.63rem;
  }
  .trend1Parent {
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: center;
    gap: var(--gap-331xl);
  }
  .organicFoodIcon {
    position: absolute;
    top: 0.88rem;
    left: 1.44rem;
    width: 6rem;
    height: 6rem;
    object-fit: cover;
  }
  .farmerProtests {
    position: absolute;
    top: 2.63rem;
    left: 16.5rem;
  }
  .farmersPubliclyProtestContainer {
    position: absolute;
    top: 9.06rem;
    left: 0rem;
    text-align: left;
    display: flex;
    align-items: center;
    width: 46.88rem;
    height: 14.94rem;
  }
  .fundAccountingIcon {
    position: absolute;
    top: 0.94rem;
    left: 1.88rem;
    width: 6rem;
    height: 6rem;
    object-fit: cover;
  }
  .howToBudget {
    position: absolute;
    top: 2.69rem;
    left: 16.69rem;
  }
  .aBudgetHelpsContainer {
    position: absolute;
    top: 9.94rem;
    left: 0.88rem;
    text-align: left;
    display: flex;
    align-items: center;
    width: 44.81rem;
  }
  .trend4 {
    position: relative;
    border-radius: var(--br-3xs);
    width: 46.88rem;
    height: 24.69rem;
    overflow: hidden;
    flex-shrink: 0;
  }
  .frameParent {
    position: absolute;
    top: calc(50% - 315.5px);
    left: calc(50% - 925.5px);
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: var(--gap-31xl);
  }
  .thisPageDisplays {
    position: absolute;
    top: 11.56rem;
    left: calc(50% - 708px);
    display: flex;
    align-items: center;
    justify-content: center;
    width: 83.81rem;
    height: 7.44rem;
  }
  .trend {
    position: absolute;
    height: 100%;
    width: 100%;
    top: 0rem;
    right: 0rem;
    bottom: 0rem;
    left: 0rem;
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
  .trends1 {
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
    height: 5rem;
  }
  .trends {
    position: relative;
    background-color: var(--color-white);
    width: 100%;
    height: 100vh;
    overflow: hidden;
    text-align: center;
    font-size: var(--font-size-11xl);
    color: var(--color-darkslategray);
    font-family: var(--font-segoe-ui);
  }
</style>
