<script setup>
</script>

<template>
  <div class='body'>
    <div class='coffee-machine'>
      <div class='top'>
        <div class="inner">
          <div class="coffee-buttons">
            <button>1</button>
            <button>2</button>
            <button>3</button>
            <button>4</button>
            <button>5</button>
            <button>6</button>
          </div>
        </div>
      </div>

      <div class='middle'>
        <div class="coffee-hole-handle">
          <div class="inner"></div>
        </div>
        <div class="coffee-hole">
          <div class="inner"></div>
        </div>

        <div class="random"></div>

        <div class="shadow1"></div>
        <div class="shadow2"></div>
        <div class="shadow3"></div>
        <div class="shadow4"></div>
      </div>

      <div class='bottom'>
        <div class="inner"></div>
      </div>
      <div class='left-foot'>
        <div class="inner"></div>
      </div>
      <div class='right-foot'>
        <div class="inner"></div>
      </div>
    </div>

    <div class="coffee-machine-shadow"></div>
  </div>
</template>

<style scoped>
  .body {
    background: #f9f2e9;
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

  .coffee-machine .bottom {
    width: 100%;
    height: 30px;
    border: 8px solid #2e3248;
    border-bottom-left-radius: 10px;
    border-bottom-right-radius: 10px;
    border-top-left-radius: 10px;
    border-top-right-radius: 10px;
    background: #555463;
    position: relative;
    z-index: 3;
    overflow: hidden;
  }

  .coffee-machine .bottom .inner {
    background: #3c3f50;
    border-bottom-left-radius: 15px;
    width: 100%;
    height: 100%;
    margin-left: 7px;
  }

  .coffee-machine .left-foot {
    border: 8px solid #2e3248;
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
    border: 8px solid #2e3248;
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
</style>
